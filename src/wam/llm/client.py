"""OpenRouter LLM client with tiered routing, validated JSON output, and cost tracking.

OpenRouter exposes an OpenAI-compatible API, so we drive it with the ``openai`` SDK pointed
at the OpenRouter base URL. Three usage paths:

- :meth:`complete` — free-form text.
- :meth:`complete_json` — forces a JSON object, validates it against a Pydantic model, and
  retries with the validation error fed back to the model on malformed output.

Every call logs a structured record (tier, model, tokens, latency, cost) and updates the
shared :data:`wam.logging.COST` tracker.
"""

from __future__ import annotations

import json
import time
from typing import Type, TypeVar

from openai import (APIConnectionError, APITimeoutError, APIStatusError, OpenAI,
                    RateLimitError)
from pydantic import BaseModel, ValidationError
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from wam.config import Config, load_config
from wam.logging import COST, get_logger

log = get_logger("llm")
T = TypeVar("T", bound=BaseModel)


class LLMError(RuntimeError):
    pass


def _is_transient(exc: BaseException) -> bool:
    """Retry only on rate limits, timeouts, connection drops, and 5xx — not 4xx."""
    if isinstance(exc, (RateLimitError, APITimeoutError, APIConnectionError)):
        return True
    if isinstance(exc, APIStatusError):
        return exc.status_code >= 500
    return False


class LLMClient:
    def __init__(self, config: Config | None = None):
        self.cfg = config or load_config()
        api_key = self.cfg.require_env(self.cfg.get("provider.api_key_env", "OPENROUTER_API_KEY"))
        self.client = OpenAI(
            base_url=self.cfg.get("provider.base_url", "https://openrouter.ai/api/v1"),
            api_key=api_key,
            timeout=self.cfg.get("constants.request_timeout", 90),
            default_headers={
                # OpenRouter attribution headers (optional).
                "HTTP-Referer": self.cfg.get("provider.http_referer", ""),
                "X-Title": self.cfg.get("provider.app_title", "Awesome-WAM"),
            },
        )
        self._cost_table = self.cfg.get("models.cost_per_million", {}) or {}
        self._max_retries = int(self.cfg.get("constants.max_retries", 4))
        self._backoff = float(self.cfg.get("constants.retry_backoff", 3.0))

    # --- model resolution ------------------------------------------------------
    def resolve_model(self, tier_or_stage: str) -> str:
        """Accept a tier name ('cheap'/'mid'/'strong') or a stage name."""
        tiers = self.cfg.get("models.tiers", {}) or {}
        if tier_or_stage in tiers:
            return tiers[tier_or_stage]
        return self.cfg.model_for_stage(tier_or_stage)

    def _estimate_cost(self, model: str, in_tok: int, out_tok: int) -> float:
        rates = self._cost_table.get(model)
        if not rates:
            return 0.0
        return (in_tok * rates.get("input", 0.0) + out_tok * rates.get("output", 0.0)) / 1_000_000

    # --- core call -------------------------------------------------------------
    def _call(self, model: str, messages: list[dict], *, temperature: float, max_tokens: int,
              json_mode: bool, label: str) -> tuple[str, int, int]:
        @retry(
            reraise=True,
            stop=stop_after_attempt(self._max_retries),
            wait=wait_exponential(multiplier=self._backoff, max=60),
            retry=retry_if_exception(_is_transient),
        )
        def _do() -> tuple[str, int, int]:
            kwargs: dict = {"model": model, "messages": messages, "temperature": temperature}
            if max_tokens:
                kwargs["max_tokens"] = max_tokens
            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}
            t0 = time.monotonic()
            resp = self.client.chat.completions.create(**kwargs)
            dt = time.monotonic() - t0
            choice = resp.choices[0]
            content = choice.message.content or ""
            usage = resp.usage
            in_tok = getattr(usage, "prompt_tokens", 0) or 0
            out_tok = getattr(usage, "completion_tokens", 0) or 0
            cost = self._estimate_cost(model, in_tok, out_tok)
            COST.record(model, in_tok, out_tok, cost)
            log.debug("call[%s] model=%s tokens=%d+%d cost=$%.5f %.2fs finish=%s",
                      label, model, in_tok, out_tok, cost, dt, choice.finish_reason)
            return content, in_tok, out_tok

        return _do()

    # --- public API ------------------------------------------------------------
    def complete(self, tier: str, system: str, user: str, *, temperature: float | None = None,
                 max_tokens: int | None = None, label: str = "complete",
                 model: str | None = None) -> str:
        model = model or self.resolve_model(tier)
        temperature = self.cfg.get("models.defaults.temperature", 0.2) if temperature is None else temperature
        max_tokens = self.cfg.get("models.defaults.max_tokens", 4096) if max_tokens is None else max_tokens
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        content, _, _ = self._call(model, messages, temperature=temperature,
                                    max_tokens=max_tokens, json_mode=False, label=label)
        return content

    def complete_json(self, tier: str, system: str, user: str, schema: Type[T], *,
                      temperature: float | None = None, max_tokens: int | None = None,
                      label: str = "json", max_repair: int = 2, model: str | None = None) -> T:
        """Return an instance of ``schema``. Retries with the validation error on failure."""
        model = model or self.resolve_model(tier)
        temperature = self.cfg.get("models.defaults.temperature", 0.2) if temperature is None else temperature
        max_tokens = self.cfg.get("models.defaults.max_tokens", 4096) if max_tokens is None else max_tokens
        schema_json = json.dumps(schema.model_json_schema(), indent=2)
        keys = ", ".join(schema.model_fields.keys())
        sys_full = (f"{system}\n\nReturn ONLY a JSON object with exactly these top-level keys: "
                    f"{keys}. Put the values directly at the top level — do NOT wrap them in a "
                    f"'properties' object and do NOT echo the schema. Schema for reference:\n"
                    f"{schema_json}")
        messages = [{"role": "system", "content": sys_full}, {"role": "user", "content": user}]

        last_err: Exception | None = None
        for attempt in range(max_repair + 1):
            content, _, _ = self._call(model, messages, temperature=temperature,
                                        max_tokens=max_tokens, json_mode=True,
                                        label=f"{label}#{attempt}")
            try:
                return schema.model_validate(_extract_obj(content, schema))
            except (ValidationError, json.JSONDecodeError, ValueError) as e:
                last_err = e
                log.warning("JSON validation failed for %s (attempt %d): %s", label, attempt,
                            str(e)[:200])
                messages.append({"role": "assistant", "content": content})
                messages.append({"role": "user", "content":
                                 f"That did not validate: {e}. Return ONLY the corrected JSON "
                                 f"object with top-level keys {keys}."})
        raise LLMError(f"Could not get valid {schema.__name__} from {model}: {last_err}")


def _strip_fences(text: str) -> str:
    """Remove ```json ... ``` fences some models add despite json_mode."""
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else t
        if t.endswith("```"):
            t = t[: t.rfind("```")]
    return t.strip()


# Envelope keys some models wrap the real object in (e.g. deepseek echoes the JSON schema's
# "properties"; others use "output"/"result").
_ENVELOPES = ("properties", "output", "result", "data", "response", "json")


def _extract_obj(content: str, schema: type[BaseModel]) -> dict:
    """Parse model content to the target dict, tolerating common wrapper envelopes."""
    raw = _strip_fences(content)
    if not raw:
        raise ValueError("empty content (model likely spent the token budget on reasoning)")
    data = json.loads(raw)
    if isinstance(data, dict):
        required = set(schema.model_fields.keys())
        if not (required & data.keys()):  # none of the expected keys at top level → unwrap
            for key in _ENVELOPES:
                inner = data.get(key)
                if isinstance(inner, dict) and (required & inner.keys()):
                    return inner
    return data
