# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-06-16 · **Tracked:** 282 core · 292 adjacent ·
130 news · **8234** benchmark rows across **3060** model
variants · **30** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **Vision-Language-Action Models for Robotics** | 81 | 📈 rising | Develops and improves VLA models for robotic manipulation, navigation, and control, focusing on architecture, training… |
| **World Models for Video Generation and Control** | 51 | 📈 rising | Develops video generation models as world models that predict future frames conditioned on actions or controls… |
| **Benchmarking and Evaluation of World Models and VLAs** | 26 | 📈 rising | Creates benchmarks and evaluation frameworks to diagnose capabilities, safety, robustness, and generalization of world… |
| **Theoretical Foundations and Architectures for World Models** | 23 | 📈 rising | Provides theoretical frameworks, architectural innovations, and training paradigms for world models, including latent… |
| **Reasoning and Planning with World Models** | 23 | 📈 rising | Integrates world models with reasoning and planning, including LLM-based planning, search, and policy optimization for… |
| **Efficient Inference and Deployment of Generative Models** | 20 | 📈 rising | Develops techniques to accelerate inference, reduce memory, and enable deployment of video generation and VLA models on… |
| **Long-Horizon and Consistent Video Generation** | 20 | 📈 rising | Addresses temporal consistency, memory, and drift in long video generation through novel architectures and… |
| **Controllable and Interactive Video Generation** | 19 | 📈 rising | Enables fine-grained control over video generation through conditioning on actions, camera parameters, language, or… |
| **Multimodal and Embodied Understanding** | 19 | 📈 rising | Explores multimodal integration, representation learning, and understanding for embodied AI, including spatial… |
| **Safety, Robustness, and Verification of VLA Policies** | 17 | 📈 rising | Addresses safety, robustness, and runtime verification for VLA models, including adversarial attacks, failure… |
| **Miscellaneous** | 11 | 📈 rising | Papers that do not fit neatly into the above directions, covering diverse topics from music recommendation to medical… |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **8.23** | Flash-WAM: Modality-Aware Distillation for World Action Models | 2026-06-03 | spd 9 · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.05254) · [pdf](https://arxiv.org/pdf/2606.05254v1) |
| **7.73** | BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving | 2026-06-07 | spd 8 · gen 3 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2606.08684) · [pdf](https://arxiv.org/pdf/2606.08684v1) · [code](https://github.com/George-Ling3/BLUE) |
| **7.71** | LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies | 2026-06-14 | spd 7 · gen 7 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15768) · [pdf](https://arxiv.org/pdf/2606.15768v1) |
| **7.67** | vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models | 2026-06-06 | spd 8 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.08094) · [pdf](https://arxiv.org/pdf/2606.08094v1) · [code](https://github.com/ggml-org/llama.cpp) |
| **7.66** | Cosmos 3: Omnimodal World Models for Physical AI | 2026-06-01 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02800) · [pdf](https://arxiv.org/pdf/2606.02800v1) · [code](https://github.com/nvidia/cosmos) |
| **7.61** | AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing | 2026-06-08 | spd 8 · gen 3 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.09811) · [pdf](https://arxiv.org/pdf/2606.09811v1) |
| **7.61** | GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation | 2026-06-07 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.08530) · [pdf](https://arxiv.org/pdf/2606.08530v1) · [code](https://github.com/babynabeauty/GEAR-VLA) |
| **7.58** | Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation | 2026-06-02 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.03784) · [pdf](https://arxiv.org/pdf/2606.03784v2) |
| **7.57** | SANTS: A State-Adaptive Scheduler for World Action Models | 2026-05-27 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2605.27947) · [pdf](https://arxiv.org/pdf/2605.27947v1) |
| **7.52** | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis | 2026-06-04 | spd 8 · gen 7 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.05979) · [pdf](https://arxiv.org/pdf/2606.05979v1) · [code](https://github.com/SJTU-DENG-Lab/WLA) |
| **7.51** | FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation | 2026-06-11 | spd – · gen 8 · spec 6 · cost – | [abs](https://arxiv.org/abs/2606.13102) · [pdf](https://arxiv.org/pdf/2606.13102v1) |
| **7.49** | 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training | 2026-06-03 | spd – · gen 6 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.04436) · [pdf](https://arxiv.org/pdf/2606.04436v1) |
| **7.49** | $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation | 2026-06-11 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.13672) · [pdf](https://arxiv.org/pdf/2606.13672v1) · [code](https://github.com/mseitzer/pytorch-fid) |
| **7.48** | LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World | 2026-05-31 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458v1) |
| **7.47** | DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model | 2026-06-10 | spd 8 · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.12105) · [pdf](https://arxiv.org/pdf/2606.12105v1) |
| **7.46** | Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning | 2026-05-29 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.30795) · [pdf](https://arxiv.org/pdf/2605.30795v1) |
| **7.46** | Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments | 2026-05-28 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.30280) · [pdf](https://arxiv.org/pdf/2605.30280v2) · [code](https://github.com/QwenLM/Qwen-VLA) |
| **7.46** | Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance | 2026-05-22 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.24203) · [pdf](https://arxiv.org/pdf/2605.24203v1) |
| **7.45** | QPILOTS: Efficient Test-Time Q-Steering for Flow Policies | 2026-06-11 | spd – · gen 6 · spec 8 · cost 4 | [abs](https://arxiv.org/abs/2606.14801) · [pdf](https://arxiv.org/pdf/2606.14801v1) |
| **7.44** | VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies | 2026-05-28 | spd 8 · gen 7 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2605.30011) · [pdf](https://arxiv.org/pdf/2605.30011v1) · [code](https://github.com/DCDmllm/VisualThink-VLA) |
| **7.44** | Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination | 2026-06-08 | spd 8 · gen 5 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2606.10040) · [pdf](https://arxiv.org/pdf/2606.10040v1) |
| **7.38** | Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation | 2026-06-01 | spd 5 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.02486) · [pdf](https://arxiv.org/pdf/2606.02486v1) |
| **7.38** | Wall-OSS-0.5 Technical Report | 2026-05-29 | spd – · gen 8 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.30877) · [pdf](https://arxiv.org/pdf/2605.30877v2) · [code](https://github.com/X-Square-Robot/wall-x) |
| **7.36** | SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models | 2026-05-30 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.00664) · [pdf](https://arxiv.org/pdf/2606.00664v1) |
| **7.35** | Colosseum V2: Benchmarking Generalization for Vision Language Action Models | 2026-05-26 | spd – · gen 8 · spec – · cost – | [abs](https://arxiv.org/abs/2605.27759) · [pdf](https://arxiv.org/pdf/2605.27759v1) |
| **7.33** | DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World | 2026-06-10 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.11901) · [pdf](https://arxiv.org/pdf/2606.11901v1) · [code](https://github.com/isaac-sim/IsaacSim) |
| **7.31** | CausalDrive: Real-time Causal World Models for Autonomous Driving | 2026-06-13 | spd 6 · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.15341) · [pdf](https://arxiv.org/pdf/2606.15341v1) |
| **7.28** | Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation | 2026-06-14 | spd 6 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.15869) · [pdf](https://arxiv.org/pdf/2606.15869v1) |
| **7.26** | Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models | 2026-06-09 | spd – · gen 8 · spec 7 · cost 5 | [abs](https://arxiv.org/abs/2606.11324) · [pdf](https://arxiv.org/pdf/2606.11324v1) · [code](https://github.com/pickxiguapi/Embodied-R1.5) |
| **7.25** | SparseWorld: Enhancing End-to-End Autonomous Driving via World Models with Sparse Scene Representation | 2026-05-23 | spd – · gen 2 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2605.24354) · [pdf](https://arxiv.org/pdf/2605.24354v1) |
| **7.25** | DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions | 2026-05-20 | spd 5 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2605.21273) · [pdf](https://arxiv.org/pdf/2605.21273v2) |
| **7.25** | Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models | 2026-06-13 | spd 8 · gen 3 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15099) · [pdf](https://arxiv.org/pdf/2606.15099v1) |
| **7.24** | Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR | 2026-05-19 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.19282) · [pdf](https://arxiv.org/pdf/2605.19282v1) |
| **7.23** | ProgVLA: Progress-Aware Robot Manipulation Skill Learning | 2026-05-27 | spd – · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2605.28231) · [pdf](https://arxiv.org/pdf/2605.28231v1) |
| **7.23** | ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation | 2026-06-12 | spd 8 · gen 5 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2606.14255) · [pdf](https://arxiv.org/pdf/2606.14255v1) |
| **7.22** | DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions | 2026-05-29 | spd – · gen 3 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2605.31271) · [pdf](https://arxiv.org/pdf/2605.31271v1) |
| **7.22** | T-Rex: Tactile-Reactive Dexterous Manipulation | 2026-06-15 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.17055) · [pdf](https://arxiv.org/pdf/2606.17055v1) · [code](https://github.com/xiaoxiaoxh/reactive_diffusion_policy) |
| **7.21** | ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models | 2026-05-28 | spd 8 · gen 6 · spec – · cost 8 | [abs](https://arxiv.org/abs/2605.29438) · [pdf](https://arxiv.org/pdf/2605.29438v1) |
| **7.19** | C$^3$ache: Accelerating World Action Models with Cross Inference Chunk Cache | 2026-06-08 | spd 8 · gen – · spec 5 · cost 7 | [abs](https://arxiv.org/abs/2606.08962) · [pdf](https://arxiv.org/pdf/2606.08962v1) |
| **7.19** | YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale | 2026-06-08 | spd – · gen 7 · spec 5 · cost – | [abs](https://arxiv.org/abs/2606.10244) · [pdf](https://arxiv.org/pdf/2606.10244v1) |
| **7.18** | From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model | 2026-05-21 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.22671) · [pdf](https://arxiv.org/pdf/2605.22671v2) |
| **7.18** | Next Forcing: Causal World Modeling with Multi-Chunk Prediction | 2026-06-09 | spd 6 · gen 5 · spec 8 · cost 4 | [abs](https://arxiv.org/abs/2606.11187) · [pdf](https://arxiv.org/pdf/2606.11187v1) |
| **7.15** | Dexora: Open-source VLA for High-DoF Bimanual Dexterity | 2026-05-18 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.18722) · [pdf](https://arxiv.org/pdf/2605.18722v1) |
| **7.14** | FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies | 2026-05-26 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.27284) · [pdf](https://arxiv.org/pdf/2605.27284v1) · [code](https://github.com/NVIDIA/Isaac-GR00T) |
| **7.13** | MAD: Mapping-Aware World Models for Agile Quadrotor Flight | 2026-06-03 | spd 7 · gen 3 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.04534) · [pdf](https://arxiv.org/pdf/2606.04534v1) |
| **7.13** | RhinoVLA Technical Report | 2026-06-05 | spd 8 · gen 6 · spec 4 · cost 7 | [abs](https://arxiv.org/abs/2606.07383) · [pdf](https://arxiv.org/pdf/2606.07383v1) · [code](https://github.com/HuixiAI/RhinoVLA) |
| **7.1** | GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models | 2026-06-02 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.03240) · [pdf](https://arxiv.org/pdf/2606.03240v1) |
| **7.09** | World-Task Factorization for Robot Learning | 2026-06-01 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02027) · [pdf](https://arxiv.org/pdf/2606.02027v1) |
| **7.09** | EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models | 2026-05-25 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.25477) · [pdf](https://arxiv.org/pdf/2605.25477v1) |
| **7.09** | RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation | 2026-06-12 | spd 8 · gen 2 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2606.14010) · [pdf](https://arxiv.org/pdf/2606.14010v1) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _874 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| KV baseline (growing cache) | — | inference state size at 100k steps | 25600000.0 | authors |
| OpenVLA-7B _(LIBERO)_ | — | I(X; X~) (attack channel capacity) | 5000.0 | authors |
| AURA-Mem | — | inference state size | 4224.0 | authors |
| Wan 2.2 (chunked) _(LIBERO-90)_ | — | FVD | 4177.0 | 3rd-party |
| SimpleVLA-RL _(LIBERO)_ | Long | iterations to 90% success rate | 2450.0 | authors |
| vla.cpp | — | peak RSS | 2031.0 | authors |
| vla.cpp | — | VRAM usage | 1312.0 | authors |
| ConfidenceVLA | — | avg inference time | 712.9 | 3rd-party |
| Agentic-VLA _(LIBERO)_ | Long | iterations to 90% success rate | 700.0 | authors |
| SKIP _(LIBERO-90)_ | — | FVD | 458.0 | authors |

#### CALVIN  ·  _69 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 99.5 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (1 task) | 99.3 | authors |
| MPCoT _(LIBERO, CALVIN ABC→D)_ | — | 3-step success rate | 96.8 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (2 tasks) | 96.6 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (2 tasks) | 95.9 | authors |
| VLM4VLA + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 94.4 | authors |
| MPCoT _(LIBERO, CALVIN ABC→D)_ | — | 4-step success rate | 93.7 | authors |
| VLM4VLA _(CALVIN ABC)_ | — | success rate (1 task) | 93.4 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (3 tasks) | 91.2 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (3 tasks) | 90.5 | authors |

#### RoboTwin  ·  _193 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LingBot-VA | — | per-chunk latency | 8100.0 | authors |
| WAM4D _(RoboTwin 2.0)_ | — | inference latency | 525.43 | authors |
| Fast-WAM _(RoboTwin 2.0)_ | — | inference latency | 425.53 | 3rd-party |
| Flash-WAM _(LingBot-VA)_ | — | per-chunk latency | 348.0 | authors |
| π0.5 _(RoboTwin2.0)_ | Grab Roller | success rate | 98.6 | authors |
| Ours _(RoboTwin 2.0 demonstration data (50 per task, easy setting))_ | S3 (Lift Pot) | success rate | 97.0 | authors |
| SANTS _(RoboTwin 2.0 + real-robot data)_ | — | success rate | 94.4 | authors |
| Next Forcing _(in-house general video dataset (3.5M clips) + RoboTwin)_ | — | success rate | 94.1 | authors |
| AHA-WAM _(RoboTwin 2.0)_ | — | success rate | 93.4 | authors |
| AdaWAM _(LIBERO + RoboTwin 2.0 + real-world ALOHA/PiPER)_ | Clean Overall SR | success rate | 93.11 | authors |

#### SimplerEnv  ·  _115 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GeoAlign _(robot-domain RGB-D + Dpol (SimplerEnv-Fractal demonstrations))_ | Pick Coke Can | success rate | 100.0 | authors |
| OpenVLA-7b | Pick up | failure rate (FR) | 97.5 | authors |
| GR00T-N1.6 | Pick up | failed object coverage (FOC) | 97.1 | authors |
| Afford-VLA _(LIBERO + Affordance dataset)_ | Put Eggplant | Success rate | 96.8 | authors |
| Embodied-R1.5-VLA | — | success rate | 92.4 | authors |
| TBD-VLA _(Fractal)_ | Visual Matching | success rate | 91.0 | authors |
| GeoAlign _(robot-domain RGB-D + Dpol (SimplerEnv-Fractal demonstrations))_ | — | unweighted average success rate | 85.3 | authors |
| EO-1 | Pick up | trajectory coverage (TC) | 84.0 | authors |
| InternVLA-M1 | Variant Aggregation | success rate | 83.7 | 3rd-party |
| Coarse-to-Control _(SimplerEnv-WidowX)_ | — | success rate | 83.3 | authors |

#### RLBench  ·  _33 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PointACT _(RLBench (10 tasks))_ | Close laptop lid | success rate | 99.0 | authors |
| EO1 (reproduced) _(RLBench (10 tasks))_ | Mean | success rate | 73.2 | 3rd-party |
| GR00T(arch) + Point _(LIBERO-Spatial / RLBench-10Tasks)_ | Mean | success rate | 69.7 | authors |
| GR00T(arch) + Point (final layer) _(RLBench-10Tasks)_ | Mean | success rate | 69.7 | authors |
| GR00T(arch) + Point (multi-scale, K=128) _(RLBench-10Tasks)_ | Mean | success rate | 65.6 | authors |
| GR00T(arch) + Point (multi-scale, K=64) _(RLBench-10Tasks)_ | Mean | success rate | 65.2 | authors |
| GR00T(arch) _(LIBERO-Spatial / RLBench-10Tasks)_ | Mean | success rate | 50.8 | authors |
| HARP-SRPD | — | average success rate | 46.59 | authors |
| HARP-SR | 18 tasks | average success rate | 43.41 | authors |
| Unadapted | 18 tasks | average success rate | 37.56 | authors |

#### Meta-World  ·  _16 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| VICX _(Meta-World (drawer-open, reach, basketball))_ | coffee-button | success rate | 100.0 | authors |
| ProgVLA (0.1B) _(Meta-World MT50)_ | — | success rate | 78.5 | authors |
| SmolVLA (2.25B) | — | success rate | 68.24 | 3rd-party |
| AVDC _(Meta-World (11 tasks))_ | — | success rate | 55.0 | 3rd-party |
| π0.5-Finetune _(Meta-World MT50)_ | — | success rate | 26.1 | 3rd-party |
| π0.5-Scratch _(Meta-World MT50)_ | — | success rate | 20.6 | 3rd-party |
| Gemini-1.5-Pro | — | PIB (bits) | 2.65 | authors |

#### ManiSkill  ·  _21 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 98.68 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 97.44 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 95.78 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 93.14 | authors |
| OpenVLA-OFT + Feat2Go | — | success rate | 82.9 | authors |
| OpenVLA-OFT + Steps-To-Go | — | success rate | 79.0 | 3rd-party |
| OpenVLA-OFT + PPO | — | success rate | 76.8 | 3rd-party |
| FlowMPC _(expert trajectories from SAC policy on PickSingleYCB-v1)_ | PickSingleYCB-v1 | anytime success rate | 69.78 | authors |
| FM policy _(expert trajectories from SAC policy on PickSingleYCB-v1)_ | PickSingleYCB-v1 | anytime success rate | 68.77 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickSingleYCB-v1)_ | PickSingleYCB-v1 | end success rate | 66.41 | authors |

#### RoboCasa  ·  _84 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GR00T-N1.5 _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.7 | authors |
| Late Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.0 | authors |
| Early Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 69.7 | authors |
| Spatial Forcing _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 68.3 | authors |
| World Pilot _(LIBERO)_ | — | success rate | 65.5 | authors |
| X-DiffVLA _(GR00T dataset (RoboCasa tasks))_ | — | Success Rate | 64.5 | authors |
| RLDX-1-FT-RC365 | — | success rate (SR) | 58.4 | authors |
| μ0 _(TraceExtract)_ | SlideToasterOvenRack | success rate | 56.0 | authors |
| π0.5 | — | safety | 55.7 | authors |
| Qwen3-VL-4B _(G+E then AgiBot-World-Beta (LoRA r64))_ | — | Success Rate | 55.2 | authors |

#### Open-X / RT  ·  _38 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| 4DNeX | 300 held-out trajectories | FVD | 818.0 | 3rd-party |
| TesserAct | 300 held-out trajectories | FVD | 746.0 | 3rd-party |
| Wan 2.1 14B | 300 held-out trajectories | FVD | 671.0 | 3rd-party |
| LVP | 300 held-out trajectories | FVD | 330.0 | 3rd-party |
| PointAction _(BridgeData V2 + DROID (filtered ~75K clips))_ | 300 held-out trajectories | FVD | 320.0 | authors |
| VisualThink-VLA _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 89.49 | authors |
| FullSoft _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 88.45 | authors |
| ECoT | — | success rate | 85.09 | 3rd-party |
| BaseVLA _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 75.37 | authors |
| OpenVLA + RL | speed steering | success rate | 48.9 | authors |

#### ALFWorld  ·  _6 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GIGPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 90.4 | authors |
| GRPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 77.9 | authors |
| FQE _(πb trajectories (Llama-3.1-8B-Instr.))_ | iter1 policy | Spearman ρ | 0.82 | 3rd-party |
| ADWM _(πb trajectories (Llama-3.1-8B-Instr.))_ | iter3 policy | Spearman ρ | 0.8 | authors |

#### VBench  ·  _547 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Wan-I2V | Cut & Drag | Flow-Err | 181.1 | 3rd-party |
| GWTF | Cut & Drag | Flow-Err | 152.81 | 3rd-party |
| PTQ4DiT | — | FVD-FP | 124.2 | authors |
| Q-ARVD | — | FVD-FP | 116.26 | authors |
| Wan-T2V | T2V Motion Transfer | Flow-Err | 103.26 | 3rd-party |
| TTM | Cut & Drag | Flow-Err | 102.39 | 3rd-party |
| ϕ-Noise | Cut & Drag | Flow-Err | 101.49 | authors |
| IAMFlow | — | Temporal Flickering | 99.438 | authors |
| LongLive | — | Temporal Flickering | 99.402 | 3rd-party |
| MemFlow | — | Temporal Flickering | 99.386 | 3rd-party |

#### Habitat  ·  _6 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ViewCrafter | sparse views-to-video | FVD | 778.207 | 3rd-party |
| TrajectoryCrafter | sparse views-to-video | FVD | 690.322 | 3rd-party |
| GEN3C | sparse views-to-video | FVD | 511.039 | 3rd-party |
| Pantheon360 _(360-1M (filtered))_ | sparse views-to-video | FVD | 450.696 | authors |
| multiple (LLaVA-1.6, GPT-4V, Gemini-1.5-Pro, InternVL2, OpenVLA) | — | success rate relative to oracle | 94.2 | authors |
| Gemini-1.5-Pro | — | PIB (bits) | 1.05 | authors |

#### BEHAVIOR  ·  _27 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| MPVI _(none (no additional training))_ | — | Q-score improvement | 113.0 | authors |
| SERF _(per-task finetune on BEHAVIOR-1K)_ | Failure recovery (object drop) | recovery success rate | 95.0 | authors |
| PI0.5 (ft) _(per-task finetune on BEHAVIOR-1K)_ | Failure recovery (object drop) | recovery success rate | 65.0 | authors |
| SERF _(per-task finetune on BEHAVIOR-1K)_ | Collecting Children's Toys | task progress | 63.5 | authors |
| SERF (env) _(per-task finetune on BEHAVIOR-1K)_ | Putting Shoes On Rack | task progress | 59.0 | authors |
| SBP _(per-task finetune on BEHAVIOR-1K)_ | Collecting Children's Toys | task progress | 57.9 | authors |
| PI0.5 (ft) _(per-task finetune on BEHAVIOR-1K)_ | Scene-configuration generalization (Additional Objects) | task progress | 50.6 | authors |
| PI0.5 (pre) _(BEHAVIOR-1K (50 tasks))_ | Assembling Gift Baskets | task progress | 44.1 | authors |
| PI0.5 (ft) _(per-task finetune on BEHAVIOR-1K)_ | Failure recovery (object drop) | recovery time | 24.3 | authors |
| SERF _(per-task finetune on BEHAVIOR-1K)_ | Failure recovery (object drop) | recovery time | 20.5 | authors |

#### Context-as-Memory dataset  ·  _98 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| State-Space (block-wise) _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 69.0 | authors |
| Context learning, K=20 _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 58.63 | authors |
| Context learning, K=5 _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 50.75 | authors |
| Length r=4 _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 43.25 | authors |
| State-Space (legacy hybrid) _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 34.75 | authors |
| Length r=2 _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 24.0 | authors |
| Compression weight-only _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 22.38 | authors |
| Spatial cross-attn RO _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 17.12 | authors |
| Spatial inject-none _(Context-as-Memory dataset)_ | open-domain return | Open-domain VLM | 15.5 | authors |
| Spatial inject-none _(Context-as-Memory dataset)_ | replay | Replay PSNR | 14.66 | authors |

#### T2VSafetyBench  ·  _84 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Wan | Copyright & Trademarks | Violation Rate | 71.0 | 3rd-party |
| [9] | Copyright & Trademarks | Violation Rate | 71.0 | 3rd-party |
| [69] | Copyright & Trademarks | Violation Rate | 65.0 | 3rd-party |
| SAFREE [10] | Copyright & Trademarks | Violation Rate | 51.5 | 3rd-party |
| LA-LQR (ours) | Copyright & Trademarks | Violation Rate | 37.0 | authors |
| Wan | Copyright & Trademarks | VBench (Subject Consistency) | 0.977 | 3rd-party |
| [9] | Copyright & Trademarks | VBench (Subject Consistency) | 0.976 | 3rd-party |
| [69] | Copyright & Trademarks | VBench (Subject Consistency) | 0.976 | 3rd-party |
| LA-LQR (ours) | Copyright & Trademarks | VBench (Subject Consistency) | 0.976 | authors |
| SAFREE [10] | Copyright & Trademarks | VBench (Subject Consistency) | 0.973 | 3rd-party |

#### SafeSora  ·  _84 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SAFREE [10] | Sexual | Violation Rate | 45.5 | 3rd-party |
| [9] | Sexual | Violation Rate | 45.5 | 3rd-party |
| [69] | Sexual | Violation Rate | 45.5 | 3rd-party |
| Hunyuan | Sexual | Violation Rate | 43.8 | 3rd-party |
| LA-LQR (ours) | Terrorism | Violation Rate | 24.0 | authors |
| LA-LQR (ours) | Animal Abuse | VBench (Subject Consistency) | 0.975 | authors |
| Hunyuan | Sexual | VBench (Subject Consistency) | 0.966 | 3rd-party |
| [9] | Animal Abuse | VBench (Subject Consistency) | 0.943 | 3rd-party |
| [69] | Racism | VBench (Subject Consistency) | 0.937 | 3rd-party |
| SAFREE [10] | Sexual | VBench (Subject Consistency) | 0.933 | 3rd-party |

#### nuScenes  ·  _82 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SparseWorld-S _(nuScenes)_ | Inference memory | Inference Memory (IM) | 4397.0 | authors |
| Direct Regression (AnchoredVAEDiT) | future frame prediction | FID | 370.8 | authors |
| Diffusion (calibrated) - AnchoredVAEDiT | future frame prediction | FID | 162.5 | authors |
| SparseWorld-S _(nuScenes)_ | Inference speed | Inference Generation Time (IGT) | 70.0 | authors |
| ResWorld baseline _(nuScenes)_ | — | Inference Latency (ms) | 64.8 | 3rd-party |
| PLAN-S (ResWorld instantiation) _(nuScenes)_ | — | Inference Latency (ms) | 59.0 | authors |
| SparseWorld-S _(nuScenes)_ | Instance forecasting (Online Mapping) | mAP (Avg) | 52.87 | authors |
| OccWorld + VISA _(nuScenes)_ | 16 foreground classes | IoU | 31.8 | authors |
| OccWorld _(nuScenes)_ | 16 foreground classes | IoU | 31.63 | authors |
| GaussianWorld + VISA _(nuScenes)_ | 16 foreground classes | mIoU | 21.91 | authors |

#### Bench2Drive  ·  _62 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| BLUE _(SimLingo training set (~400 routes))_ | — | latency | 549.5 | authors |
| VLGA _(Bench2Drive train routes)_ | — | Efficiency | 194.63 | authors |
| BLUE _(SimLingo training set (~400 routes))_ | — | driving score | 90.58 | authors |
| BLUE (CriticVLA) _(CriticVLA training set)_ | — | driving score | 90.37 | authors |
| TakeVLA _(PDM-Lite)_ | — | driving score | 89.72 | 3rd-party |
| PersonaDrive | — | Driving Score | 88.95 | authors |
| BevAD _(PDM-Lite)_ | — | driving score | 88.11 | 3rd-party |
| CriticVLA | — | driving score | 88.02 | 3rd-party |
| HiP-AD _(Think2Drive)_ | — | driving score | 86.77 | 3rd-party |
| HiP-AD | — | Driving Score | 86.77 | 3rd-party |

#### RealisDance-Val  ·  _56 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| MeshToken _(internal 300K video clips)_ | — | Motion Smooth | 98.79 | authors |
| RealisDance-DiT | — | Motion Smooth | 98.71 | 3rd-party |
| MusePose | — | Motion Smooth | 98.57 | 3rd-party |
| Animate-X | — | Motion Smooth | 98.52 | 3rd-party |
| MeshToken _(internal 300K video clips)_ | — | Temporal Flicker | 98.32 | authors |
| MimicMotion | — | Motion Smooth | 98.2 | 3rd-party |
| ControlNeXt | — | Motion Smooth | 98.05 | 3rd-party |
| MusePose | — | Temporal Flicker | 97.88 | 3rd-party |
| RealisDance-DiT | — | Temporal Flicker | 97.76 | 3rd-party |
| Animate-X | — | Temporal Flicker | 97.4 | 3rd-party |

#### SIMMER  ·  _49 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Llama 3.3 70B | — | plans with any failure | 100.0 | authors |
| Llama 3.3 70B | — | plans with immediate failures | 99.0 | authors |
| DeepSeek V3.2 | — | plans with any failure | 99.0 | authors |
| Qwen 3.5 27B | — | plans with any failure | 99.0 | authors |
| Qwen 3.5 27B | — | plans with immediate failures | 99.0 | authors |
| DeepSeek V3.2 | — | plans with immediate failures | 96.0 | authors |
| Claude Opus 4.6 | — | plans with any failure | 89.0 | authors |
| GPT-5.4 | — | plans with any failure | 87.0 | authors |
| Claude Opus 4.6 | — | plans with immediate failures | 85.0 | authors |
| Gemini 3 Flash | — | plans with any failure | 83.0 | authors |

#### EGO STATIC SCENE  ·  _45 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| AnchorWorld _(200K single-person action videos + 101K MultiCamVideo UE + Ego-Exo4D + LEMMA)_ | — | Mat. Pix.(K) | 4493.4 | authors |
| CaM-Ego _(same as AnchorWorld (egocentric data))_ | — | Mat. Pix.(K) | 4379.4 | 3rd-party |
| PlayerOne-Scene _(same as AnchorWorld (re-implemented with anchor-view injection))_ | — | Mat. Pix.(K) | 4334.8 | 3rd-party |
| PlayerOne _(same as AnchorWorld (re-implemented))_ | — | Mat. Pix.(K) | 3961.6 | 3rd-party |
| CaM-UE _(official UE dataset)_ | — | Mat. Pix.(K) | 3706.9 | 3rd-party |
| AnchorWorld _(200K single-person action videos + 101K MultiCamVideo UE + Ego-Exo4D + LEMMA)_ | — | PSNR | 16.06 | authors |
| CaM-Ego _(same as AnchorWorld (egocentric data))_ | — | PSNR | 15.16 | 3rd-party |
| PlayerOne-Scene _(same as AnchorWorld (re-implemented with anchor-view injection))_ | — | PSNR | 14.38 | 3rd-party |
| PlayerOne _(same as AnchorWorld (re-implemented))_ | — | PSNR | 13.26 | 3rd-party |
| CaM-UE _(official UE dataset)_ | — | PSNR | 11.57 | 3rd-party |

#### SpelkeBench  ·  _42 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PSI _(3 million real-world RGB video clips)_ | point-prompted movable object segmentation | mIoU | 0.681 | authors |
| SAM2 | unprompted movable object segmentation | mIoU | 0.68 | 3rd-party |
| SAM2 | unprompted movable object segmentation | AR | 0.62 | 3rd-party |
| FPT | point-prompted movable object segmentation | mIoU | 0.566 | 3rd-party |
| PSI _(3 million real-world RGB video clips)_ | point-prompted movable object segmentation | AR | 0.541 | authors |
| MaskFormer | point-prompted movable object segmentation | mIoU | 0.506 | 3rd-party |
| CWM | point-prompted movable object segmentation | mIoU | 0.481 | 3rd-party |
| MaskFormer | point-prompted movable object segmentation | AR | 0.439 | 3rd-party |
| ProMerge | point-prompted movable object segmentation | mIoU | 0.431 | 3rd-party |
| CutLER | point-prompted movable object segmentation | mIoU | 0.423 | 3rd-party |

#### Perceptual Evaluation (human study)  ·  _42 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| StreamForce _(Synthetic force-conditioned video + Pexels image-force pairs)_ | Global Force - Change | Force Adherence | 86.5 | authors |
| StreamForce _(Synthetic force-conditioned video + Pexels image-force pairs)_ | Global Force - Change | Realism / Physics | 77.3 | authors |
| StreamForce _(Synthetic force-conditioned video + Pexels image-force pairs)_ | Global Force - Change | Visual Quality | 76.9 | authors |
| ForcePrompt (reproduced on Wan2.2) _(Synthetic force videos (ForcePrompt pipeline))_ | Global Force - Preserve | Force Adherence | 74.2 | 3rd-party |
| Kling 1.5 Motion Brush | Local Force - Preserve | Visual Quality | 52.3 | 3rd-party |
| ForcePrompt (reproduced on Wan2.2) _(Synthetic force videos (ForcePrompt pipeline))_ | Global Force - Preserve | Realism / Physics | 47.3 | 3rd-party |
| Kling 1.5 Motion Brush | Local Force - Preserve | Realism / Physics | 45.8 | 3rd-party |
| Kling 1.5 Motion Brush | Local Force - Preserve | Force Adherence | 44.2 | 3rd-party |
| Wan2.2 TI2V | Global Force - Preserve | Visual Quality | 40.4 | 3rd-party |
| ForcePrompt (reproduced on Wan2.2) _(Synthetic force videos (ForcePrompt pipeline))_ | Global Force - Preserve | Visual Quality | 38.8 | 3rd-party |

#### ReactSim-Bench  ·  _42 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| MTR _(nuPlan)_ | — | Steering-curvature Infeasibility Rate | 14.29 | authors |
| CTG _(nuPlan)_ | — | Acceleration Infeasibility Rate | 10.87 | authors |
| CATK _(nuPlan)_ | — | Acceleration Infeasibility Rate | 10.25 | authors |
| SMART _(nuPlan)_ | — | Acceleration Infeasibility Rate | 9.74 | authors |
| CTG _(nuPlan)_ | — | Steering-curvature Infeasibility Rate | 7.08 | authors |
| CATK _(nuPlan)_ | — | Steering-curvature Infeasibility Rate | 5.02 | authors |
| CTG _(nuPlan)_ | — | Agent-Agent Collision Rate | 4.88 | authors |
| SMART _(nuPlan)_ | — | Steering-curvature Infeasibility Rate | 4.83 | authors |
| TrajTok _(nuPlan)_ | — | Steering-curvature Infeasibility Rate | 3.93 | authors |
| MTR _(nuPlan)_ | — | Agent-Agent Collision Rate | 3.29 | authors |

#### NAVSIM  ·  _40 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ours† _(OpenScene (NAVSIM train split))_ | planning | Comf. | 100.0 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | NC | 98.7 | authors |
| SafeAlign-VLA _(NAVSIM navtrain)_ | trajectory planning | NC | 98.6 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | DAC | 98.2 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | TTC | 95.9 | authors |
| RAP _(NAVSIM trainval)_ | — | PDMS | 93.8 | 3rd-party |
| Ours-Rep+Geo+MCB _(OpenScene (NAVSIM train split))_ | planning (frozen tokenizer + lightweight decoder) | PDMS | 91.8 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | PDMS | 91.8 | authors |
| DriveMA-4B _(NAVSIM trainval)_ | — | PDMS | 91.2 | authors |
| DriveMA-2B _(NAVSIM trainval)_ | — | PDMS | 90.5 | authors |

## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
- **ActionMap: Robot Policy Learning via Voxel Action Heatmap** — ActionMap replaces the unstructured single-point action decoder in VLA models with a voxel heatmap action head that predicts a probability distribution over a discretized 3D action space, explicitly exploiting the geometric proximity of neighboring actions rather than treating the action space as unstructured… _(→ WAM: In World Action Models, the action conditioning mechanism is critical for predicting how actions transform world states. The voxel heatmap representation can transfer in two ways: (1) as a structured action encoding input to the world model—replacing flat…)_ [abs](https://arxiv.org/abs/2606.06904) · [pdf](https://arxiv.org/pdf/2606.06904v1) · [code](https://github.com/showlab/ActionMap)
- **World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications** — A unifying multi-axis taxonomy for world models that integrates architecture, methodological families, reasoning strategies (particularly the convergence of chain-of-thought reasoning with world-model imagination), and applications, providing a structured framework to map the fragmented landscape of world model… _(→ WAM: The taxonomy's explicit categorization of reasoning strategies (imagination-based planning, latent policy learning, counterfactual reasoning) directly informs how WAMs can be architected to generate actions rather than just passive predictions. Specifically…)_ [abs](https://arxiv.org/abs/2606.00133) · [pdf](https://arxiv.org/pdf/2606.00133v1)
- **PhAIL: A Real-Robot VLA Benchmark and Distributional Methodology** — Replacing binary success rate metrics with a distributional evaluation methodology based on the time-to-success cumulative distribution function (CDF), scored via Human-Relative Throughput (HRT) and compared using macro-averaged Kolmogorov-Smirnov significance tests to resolve close model comparisons with small sample… _(→ WAM: Evaluating World Action Models often relies on binary task completion metrics, which fail to capture the speed-efficiency trade-offs of different policies. By adopting the time-to-success CDF and HRT scoring, WAM evaluations can distinguish between models…)_ [abs](https://arxiv.org/abs/2605.29710) · [pdf](https://arxiv.org/pdf/2605.29710v1) · [code](https://github.com/Positronic-Robotics/phail-paper)
- **VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models** — A lightweight, one-class discriminative confidence head that leverages frozen pretrained VLA internal representations and step-conditioned modeling to estimate step-wise anomaly scores in a single forward pass, avoiding the computational overhead of resampling and generalizing to continuous action spaces. _(→ WAM: World Action Models (WAMs) often suffer from compounding errors over long horizons and need to know when their world state predictions become unreliable. VLAConf's lightweight confidence head can be directly attached to a WAM's internal representations to…)_ [abs](https://arxiv.org/abs/2605.29605) · [pdf](https://arxiv.org/pdf/2605.29605v1)
- **When Does LeJEPA Learn a World Model?** — LeJEPA (alignment plus Gaussian regularization) provably achieves linear identifiability—linearly recovering the world's true latent variables from nonlinear observations—and Gaussian is the unique latent distribution for which this guarantee holds. Alignment strictly penalizes each degree of nonlinearity via a… _(→ WAM: World Action Models require latent spaces that faithfully preserve the world's true degrees of freedom to support reliable action-conditioned planning and compositional generalization. If the representation scrambles these degrees of freedom, planning becomes…)_ [abs](https://arxiv.org/abs/2605.26379) · [pdf](https://arxiv.org/pdf/2605.26379v1) · [code](https://github.com/klindtlab/lejepa-identifiability)
- **Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts** — A preemptive runtime verification architecture (Pre-VLA) that assesses candidate action chunks before physical execution or world-model imagination, using a lightweight dual-branch head predicting safety confidence and critic-derived advantage scores, trained with a multi-task objective (Focal classification +… _(→ WAM: World Action Models inherently couple world-model rollouts with action generation, making them vulnerable to error accumulation when low-quality actions corrupt the imagined future state. Pre-VLA's preemptive verification layer transfers directly: before a…)_ [abs](https://arxiv.org/abs/2605.22446) · [pdf](https://arxiv.org/pdf/2605.22446v1)
- **Key-Gram: Extensible World Knowledge for Embodied Manipulation** — Key-Gram introduces a conditional-memory framework that decouples language-derived world knowledge from visual-state reasoning in embodied control models. It decomposes language instructions into task-specific 'key-grams', retrieves static linguistic priors via deterministic hashed lookup (O(1) complexity) from an… _(→ WAM: World Action Models (WAMs) inherently rely on language instructions to guide future world state predictions and action generation. By adopting Key-Gram's externalized linguistic memory, WAMs could decouple static language semantics from the heavy…)_ [abs](https://arxiv.org/abs/2605.18556) · [pdf](https://arxiv.org/pdf/2605.18556v1)
- **HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning** — HapTile introduces a dual-level haptic integration for contact-rich manipulation: (1) fingertip tactile sensors at the robot end-effector provide contact-grounded visuotactile observations, and (2) haptic feedback to the teleoperator during demonstration collection improves the quality and physical realism of the… _(→ WAM: World Action Models must predict future world states and actions, but for contact-rich manipulation, critical physical dynamics—contact forces, pressure distribution, slip, deformation—are largely unobservable from vision alone. A WAM trained only on visual…)_ [abs](https://arxiv.org/abs/2606.04825) · [pdf](https://arxiv.org/pdf/2606.04825v1)
- **OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics** — OSCAR introduces 2D kinematic skeleton rendering as a unified action-conditioning representation for video world models, which abstracts away embodiment-specific details (joint configurations, action spaces) into a common visual format that generalizes across different robot arms and even human hands. This is paired… _(→ WAM: The 2D kinematic skeleton representation directly addresses a core challenge for World Action Models: unifying action spaces across diverse embodiments. WAMs must reason about and generate actions for heterogeneous robots and possibly humans; skeleton…)_ [abs](https://arxiv.org/abs/2606.04463) · [pdf](https://arxiv.org/pdf/2606.04463v2)
- **Exact equivariance, kept through training, buys zero-shot generalisation across the symmetry group** — Building a latent world model from exactly equivariant encoder and predictor yields a training loss that is provably invariant across the entire symmetry group, meaning training on a restricted slice of orientations mathematically determines the dynamics on the full orbit. Crucially, this exact equivariance survives… _(→ WAM: World Action Models are latent world models with action-conditioned prediction and planning. By constructing the WAM's encoder, dynamics predictor, and planner to be exactly equivariant under relevant symmetry groups (e.g., SE(3) for robotic manipulation)…)_ [abs](https://arxiv.org/abs/2606.03003) · [pdf](https://arxiv.org/pdf/2606.03003v1)
- **Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test** — The paper introduces the Embodied Turing Test benchmark (Wow-wo-val) with a comprehensive evaluation protocol of 22 metrics across five core abilities (perception, planning, prediction, generalization, execution) for assessing video foundation models as world models. The most novel component is the Inverse Dynamic… _(→ WAM: The IDM Turing Test concept transfers directly and critically to World Action Models. WAMs must generate not just plausible future states but futures that are grounded in correct action dynamics. The IDM test provides a concrete, automated methodology to…)_ [abs](https://openreview.net/forum?id=uZD81YIUPz) · [pdf](https://openreview.net/pdf?id=uZD81YIUPz)
- **VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models** — A 3D-aware action verification framework (VeriSpace) that evaluates candidate actions at test time by fusing visual semantics with explicit 3D geometry (Dual-Path 3D-Injected Scene Encoding) and reasoning over spatial relations, geometric validity, and goal progress (Spatially-Grounded Action Reasoning). _(→ WAM: World Action Models (WAMs) predict future states given actions and often struggle with spatial consistency in imagined rollouts. VeriSpace's dual-path 3D-injected encoding can be adapted to construct the state representations within a WAM, ensuring the world…)_ [abs](https://arxiv.org/abs/2606.10568) · [pdf](https://arxiv.org/pdf/2606.10568v1)
- **What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents** — A systematic study that unifies hierarchical VLA agents under an options-style control framework, benchmarking core design choices—planner selection, controller selection, switching mechanisms between levels, and observation/memory representations—to derive practical principles showing how model choices and interface… _(→ WAM: World Action Models must handle complex, long-horizon tasks requiring temporal abstraction. The options-style hierarchical framework and the derived interface design principles directly transfer: (1) WAMs can adopt the options framework to structure world…)_ [abs](https://arxiv.org/abs/2606.10267) · [pdf](https://arxiv.org/pdf/2606.10267v1)
- **MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models** — The core technical innovation is the dual use of object masks—both as first-frame visual prompts (inputs) to provide precise spatial grounding and as prediction targets (outputs) for object-centric semantic supervision—unified within a Mixture of Transformers (MoT) architecture. _(→ WAM: World Action Models typically suffer from referential ambiguity from text inputs and visual noise from predicting raw RGB pixels. Transferring this mask-based approach allows WAMs to replace or augment noisy RGB prediction with mask prediction, suppressing…)_ [abs](https://arxiv.org/abs/2606.13515) · [pdf](https://arxiv.org/pdf/2606.13515v1) · [code](https://github.com/QwenLM/Qwen3-VL)
- **A Tutorial on World Models and Physical AI** — A unifying framework that distinguishes explicit world models (learning structured dynamics for rollout-based reasoning and planning) from implicit world models (encoding predictive structure within scalable learned representations), and proposes that diverse world modeling approaches are unified through shared… _(→ WAM: The explicit/implicit distinction provides a principled architectural blueprint for World Action Models: WAMs can integrate explicit structured dynamics for action-conditioned rollout planning (enabling precise, hierarchical action generation and long-horizon…)_ [abs](https://arxiv.org/abs/2606.12783) · [pdf](https://arxiv.org/pdf/2606.12783v1)
- **Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends** — The paper systematically identifies and categorizes three crucial technical challenges for interactive world modeling: action-conditioned controllability, long-horizon interactions and memory, and action-following responsiveness for real-time interactivity. _(→ WAM: World Action Models fundamentally rely on action-conditioned state transitions. Addressing these three identified challenges—ensuring actions reliably control state evolution, maintaining coherent long-term memory across extended action sequences, and…)_ [abs](https://arxiv.org/abs/2606.01164) · [pdf](https://arxiv.org/pdf/2606.01164v1) · [code](https://github.com/liujiuming123/Awesome-Interactive-World-Model)
- **Coarse-to-Fine Compositional Diffusion for Long-Horizon Planning** — Coarse-to-Fine Compositional Diffusion (CoFi) separates global structure formation from local detail refinement during inference-time compositional generation. It first aligns local denoised estimates around a shared coarse scaffold capturing long-range task-level arrangement, then diffuses this scaffold to an… _(→ WAM: World Action Models must generate long-horizon action sequences or world-state trajectories that are both globally coherent (the overall plan makes sense) and locally precise (each step's actions are physically valid). CoFi's coarse-to-fine composition…)_ [abs](https://arxiv.org/abs/2606.00837) · [pdf](https://arxiv.org/pdf/2606.00837v1) · [code](https://github.com/KAIST-Visual-AI-Group/SyncDiffusion)
- **MBench: A Comprehensive Benchmark on Memory Capability for Video World Models** — A systematic decomposition of world model memory capability into three hierarchical and complementary dimensions—entity consistency, environment consistency, and causal consistency—further refined into 12 quantifiable sub-dimensions, enabling objective evaluation of long-term state retention in video world models… _(→ WAM: World Action Models must maintain coherent internal world states over extended action sequences, making memory capability critical. The three-dimensional decomposition transfers directly: (1) Entity consistency ensures WAMs track object identities and…)_ [abs](https://arxiv.org/abs/2606.00793) · [pdf](https://arxiv.org/pdf/2606.00793v1) · [code](https://github.com/study-overflow/MBench)
- **SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models** — Formalizing task-aware safety requirements as Signal Temporal Logic (STL) specifications and introducing metrics that expose the success-safety gap: Succ-But-Unsafe (SBU) rate measuring successful-yet-unsafe episodes, and Violation Severity Index (VSI) quantifying worst-case violation depth, revealing that high task… _(→ WAM: World Action Models generate action sequences and predict world states; they could inherit this STL-based safety specification framework to formally constrain their generated trajectories during planning. Currently, WAMs optimizing solely for task-completion…)_ [abs](https://arxiv.org/abs/2606.00773) · [pdf](https://arxiv.org/pdf/2606.00773v1)
- **Closed-Loop Neural Activation Control in Vision-Language-Action Models** — CTRL-STEER decouples representation from regulation in test-time steering of VLA models: rather than applying a fixed steering coefficient along an internal activation direction (open-loop), it uses a closed-loop feedback controller (PID or RL-based) that adaptively adjusts intervention magnitude online based on the… _(→ WAM: World Action Models face the same fundamental problem when being steered at test time: fixed-coefficient interventions on internal representations cause overcorrection and oscillation, especially for temporal/action concepts (speed, smoothness, force). The…)_ [abs](https://arxiv.org/abs/2606.00269) · [pdf](https://arxiv.org/pdf/2606.00269v1)
- **StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement** — Steering diffusion-based world model imaginations toward high-impact yet plausible outcomes at inference time by optimizing the initial noise with two complementary objectives: a semantic objective (using a VLM to provide gradients toward user-specified target events) and a plausibility objective (preventing the… _(→ WAM: World Action Models must evaluate and improve policies by imagining futures conditioned on actions. StressDream's inference-time noise optimization directly transfers: WAMs could stress-test action policies by steering their imaginations toward plausible but…)_ [abs](https://arxiv.org/abs/2606.00267) · [pdf](https://arxiv.org/pdf/2606.00267v1) · [code](https://github.com/CMU-IntentLab/StressDream)
- **Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning** — Factorizing the latent state of a recurrent state-space model (RSSM) into separate environment and teammate components, and learning an auxiliary Theory-of-Mind (ToM) head to infer latent embeddings of partner behavior (such as intent, character, and predicted actions) from partial trajectories to condition the… _(→ WAM: World Action Models can adopt this factorized latent space to explicitly disentangle passive environmental dynamics from the active dynamics of other agents. By integrating a ToM head, a WAM could infer the hidden intentions and predict the future actions of…)_ [abs](https://arxiv.org/abs/2605.31361) · [pdf](https://arxiv.org/pdf/2605.31361v1)
- **DecMem: Towards Minute-Long Consistent World Generation with Decoupled Memory** — DecMem introduces a decoupled memory architecture that splits learnable memory into two complementary components: Sparse Global Memory for efficient fine-grained access to long-range history, and Anchored Local Memory for stable, high-quality local extrapolation. This addresses two fundamental failure modes of naïve… _(→ WAM: World Action Models must maintain consistent world state over long action sequences, which is essentially the same long-horizon consistency problem DecMem solves. The decoupled memory design transfers directly: Sparse Global Memory gives the WAM efficient…)_ [abs](https://arxiv.org/abs/2605.31336) · [pdf](https://arxiv.org/pdf/2605.31336v1)
- **AR Forcing: Towards Long-Horizon Robot Navigation World Model** — AR Forcing, an autoregressive training strategy for diffusion-based world models that mitigates the train-inference distribution shift by using the model's own generated predictions as context for subsequent steps during training, rather than relying solely on ground-truth parallel supervision. _(→ WAM: World Action Models inherently rely on autoregressive rollouts to predict future states conditioned on actions, making them highly susceptible to compounding errors from train-test distribution shifts (teacher forcing vs. autoregressive inference). By…)_ [abs](https://arxiv.org/abs/2605.31314) · [pdf](https://arxiv.org/pdf/2605.31314v1)
- **Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring** — Hide-and-Seek formulates VLA failure detection as a coarsely supervised learning problem, using inter-trajectory and intra-trajectory contrastive objectives to localize failure-indicative actions from trajectory-level labels alone—discovering temporally structured, step-level failure signals without requiring any… _(→ WAM: World Action Models generate predicted action trajectories that must be monitored for reliability before or during execution. Hide-and-Seek's coarse-to-fine localization directly transfers: WAMs typically only receive trajectory-level success/failure signals…)_ [abs](https://arxiv.org/abs/2605.30834) · [pdf](https://arxiv.org/pdf/2605.30834v1)
- **BOKBO (Best of K Bad Options): Calibrated Abstention for VLA Policies** — BOKBO introduces a conformal abstention layer for K-sample VLA inference that provides finite-sample, distribution-free guarantees on executed-violation rate. It reveals that policy-internal nonconformity scores (confidence proxies, K-sample disagreement) are structurally unreliable under perturbation-based… _(→ WAM: World Action Models face the same fundamental problem: when generating K candidate action-conditioned world trajectories and selecting the best, they need to know when all K options are bad and should abstain. BOKBO's conformal abstention layer transfers…)_ [abs](https://arxiv.org/abs/2605.30660) · [pdf](https://arxiv.org/pdf/2605.30660v1)
- **Physically Viable World Models: A Case for Query-Conditioned Embodied AI** — World models for embodied AI must be query-conditioned and physically viable: rather than predicting future observations (which can be visually plausible but physically wrong under intervention), they should identify the simplest physical abstraction sufficient to answer an intervention query. This is achieved through… _(→ WAM: World Action Models inherently need to predict the consequences of actions, making them vulnerable to the same structural failure: predicting visually plausible but physically infeasible outcomes. The modular decomposition transfers directly—WAMs can separate…)_ [abs](https://arxiv.org/abs/2605.30542) · [pdf](https://arxiv.org/pdf/2605.30542v1) · [code](https://github.com/pvwm/physically-viable-world-models)
- **ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models via Plug-and-Play Adaptation** — ELAN4D introduces an embodiment-centric 4D-aware training framework for VLA models that uses forward kinematics to derive 3D displacement tracks of robot keypoints (joints, end-effector) as predictive spatio-temporal supervision. A plug-and-play auxiliary branch with a lightweight track decoder injects this 4D signal… _(→ WAM: World Action Models (WAMs) inherently require modeling future dynamics and spatio-temporal trajectories. ELAN4D's method of using forward kinematics to generate cheap, metric 4D keypoint tracks as auxiliary supervision can directly transfer to WAMs to provide…)_ [abs](https://arxiv.org/abs/2605.30484) · [pdf](https://arxiv.org/pdf/2605.30484v1)
- **NeuROK: Generative 4D Neural Object Kinematics** — Learning a data-driven latent space of object kinematic states and a decoder that maps these latents to plausibly deformed 3D shapes, reducing complex 4D physical dynamics generation to modeling low-dimensional latent dynamics (via Lagrangian mechanics) without relying on predefined physical models. _(→ WAM: World Action Models need to predict action-conditioned future states, which is computationally expensive and often physically implausible in high-dimensional pixel/voxel spaces. By adopting NeuROK's data-driven kinematic latent space as the state…)_ [abs](https://arxiv.org/abs/2605.30347) · [pdf](https://arxiv.org/pdf/2605.30347v1)
- **Mitigating State Aliasing in Vision-Language-Action Models via Inverse Dynamics Learning** — The core technical innovation is using inverse dynamics learning as an auxiliary objective to directly supervise the vision encoder in VLA models, mitigating state aliasing—where visually similar states require different actions. By training the encoder to predict the action between current and future observations, it… _(→ WAM: World Action Models similarly rely on visual representations to predict future states and plan actions, making them equally vulnerable to state aliasing—visually similar states that demand different action outcomes would lead to incorrect world predictions or…)_ [abs](https://arxiv.org/abs/2605.29577) · [pdf](https://arxiv.org/pdf/2605.29577v1)

## 👥 Influential Authors & Groups
- **[Pengfei Wan](https://www.semanticscholar.org/author/2363570130)** (3 papers · Kling Team, Kuaishou Technology) — Pengfei Wan's research focuses on long-horizon consistent video world generation, particularly through decoupled memory architectures and geometry-aware implicit memory to maintain spatio-temporal and geometric consistency in minute-long video generation.
- **[Bin Zhu](https://www.semanticscholar.org/author/2337784762)** (3 papers · Singapore Management University) — Bin Zhu's research focuses on world-action models (WAMs) for robotic manipulation, including benchmarking the trustworthiness of video world models, developing unified video-action world models (τ0-WM) that integrate policy learning, video prediction, and…
- **[Xiaotong Zhao](https://www.semanticscholar.org/author/2290452230)** (3 papers · Tencent) — Research on reasoning-driven controllable video generation, interactive video world models with object-level control, and expert-calibrated evaluation frameworks for professional cinematic video generation.
- **[Alan Zhao](https://www.semanticscholar.org/author/2346976453)** (3 papers · Tencent) — Alan Zhao's research focuses on controllable video generation and evaluation, including reasoning-driven frameworks for creative intent cognition, interactive video world models for object manipulation, and pipeline-aware benchmarking for professional…
- **[Pinar Yanardag](https://www.semanticscholar.org/author/3137679)** (2 papers · Virginia Tech) — Pinar Yanardag's research focuses on advancing autoregressive video diffusion and world models, particularly through training-free methods for controllable video generation. Key contributions include SPAWN for inserting user-specified visual concepts into…
- **[Kun Gai](https://www.semanticscholar.org/author/2385564054)** (2 papers · Kuaishou Technology) — Kun Gai's research focuses on long-horizon consistent world generation using decoupled memory architectures for video generation, and on improving video reasoning by using Vision-Language Models as teachers to guide Video Generation Models via adaptive…
- **[Qixing Hu](https://www.semanticscholar.org/author/152280941)** (2 papers · NVIDIA) — Qixing Hu's research focuses on long video generation, specifically addressing error accumulation and efficiency bottlenecks through retrieval-augmented generation (LongLive-RAG) and NVFP4-based parallel infrastructure (LongLive-2.0) for training and…
- **[Shuai Yang](https://www.semanticscholar.org/author/2256555282)** (2 papers · NVIDIA) — Shuai Yang's research focuses on efficient long video generation, specifically developing retrieval-augmented generation (RAG) frameworks to reduce error accumulation and designing NVFP4-based parallel infrastructures for faster training and inference.
- **[Yukang Chen](https://www.semanticscholar.org/author/2109297557)** (2 papers · NVIDIA) — Long video generation using retrieval-augmented generation (RAG) to reduce error accumulation, and efficient training/inference with NVFP4 precision for speed and memory optimization.
- **[Minseok Joo](https://www.semanticscholar.org/author/2313642518)** (2 papers · Korea University) — Research on vision-language-action models for robot manipulation, focusing on mitigating state aliasing through inverse dynamics learning, and on long video generation, improving geometric consistency via coverage-maximizing retrieval.
- **[Kyujin Lee](https://www.semanticscholar.org/author/2439353694)** (2 papers · KAIST) — Kyujin Lee's research focuses on improving visual representations for robot control and video generation, specifically addressing state aliasing in Vision-Language-Action (VLA) models via inverse dynamics learning, and enhancing long-horizon geometric…
- **[Min Wei](https://www.semanticscholar.org/author/2357859140)** (2 papers · DAMO Academy, Alibaba Group) — Improving geometric awareness and 3D structure understanding in video diffusion and world models, using tokenized 3D representations (mesh tokens) and geometry-aware implicit memory to achieve consistent long-horizon motion and scene generation.
- **[Weihua Chen](https://www.semanticscholar.org/author/2365043710)** (2 papers · DAMO Academy, Alibaba Group) — Weihua Chen's WAM research focuses on developing video diffusion models that incorporate 3D structural awareness (using mesh tokenization for render-free human motion control) and efficient frequency bridging for high-fidelity video unified generation, aiming…
- **[Fan Wang](https://www.semanticscholar.org/author/2320184479)** (2 papers · DAMO Academy, Alibaba Group) — Fan Wang's research focuses on interactive world modeling and 3D-aware video generation, particularly exploring action-conditioned video generation for world models and developing render-free frameworks using 3D human mesh tokenization to improve motion…
- **[Hanyang Wang](https://www.semanticscholar.org/author/2291393860)** (2 papers · AIRC, Midea Group) — Hanyang Wang's research focuses on developing Vision-Language-Action (VLA) foundation models for generalizable deformable manipulation, such as folding clothing items across diverse categories and environments, and on evaluating memory capabilities in video…
- **[Yifan Li](https://www.semanticscholar.org/author/2281904596)** (2 papers · Shanghai Innovation Institute) — Yifan Li's research focuses on developing world models for video prediction and robotic manipulation, including benchmarks for evaluating memory in video world models (MBench) and unified video-action world models that integrate policy learning, video…
- **[Songli Wang](https://www.semanticscholar.org/author/2117075811)** (2 papers · Southern University of Science and Technology) — Wang's research focuses on improving world models for latent planning in reinforcement learning, particularly by addressing the limitations of world-model-only planners through intuition models that guide action search, and by developing robust task…
- **[Jun Nie](https://www.semanticscholar.org/author/2315126639)** (2 papers · Peking University) — Jun Nie's research focuses on improving robot policy performance by probing value-like information from frozen VLA representations and developing training-free test-time execution methods that dynamically select action chunk horizons based on phase-dependent…
- **[Jiachen Zhang](https://www.semanticscholar.org/author/2376800622)** (2 papers · Peking University) — Research on understanding and improving vision-language-action (VLA) robot policies, including probing value-like structures in frozen representations to guide action selection and developing adaptive execution strategies for action-chunking policies to…
- **[Junying Lao](https://www.semanticscholar.org/author/2176256865)** (2 papers · Peking University) — Research on extracting value-like information from frozen VLA policies to guide action selection, and developing training-free methods for adaptive execution horizon selection in action-chunking robot policies.
- **[Songfang Huang Peking University](https://www.semanticscholar.org/author/2438923144)** (2 papers · Peking University) — Songfang Huang's research focuses on improving the test-time performance of robot foundation policies, particularly vision-language-action (VLA) models, by probing frozen representations for value-like structure about task success and developing training-free…
- **[Xintao Wang](https://www.semanticscholar.org/author/2305033532)** (2 papers · Kling Team, Kuaishou Technology) — Xintao Wang's research focuses on long-horizon consistent world generation and video world models, specifically developing memory architectures (e.g., decoupled memory with sparse global and anchored local components, and geometry-aware implicit memory) to…
- **[Anya Singh](https://www.semanticscholar.org/author/2352685268)** (2 papers · rellingsystems.com) — Anya Singh researches vision-language-action (VLA) policies for robotics, focusing on safety guarantees through conformal abstention (BOKBO) and sample-efficient transfer learning via primitive-aware training for few-shot task adaptation.
- **[Cabrel Happi](https://www.semanticscholar.org/author/2439647145)** (2 papers · rellingsystems.com) — Cabrel Happi's research focuses on improving the reliability and transfer learning capabilities of vision-language-action (VLA) policies for robot manipulation. Specifically, they investigate primitive-aware training to enable sample-efficient few-shot…
- **[Jai Relan](https://www.semanticscholar.org/author/2439647839)** (2 papers · rellingsystems.com) — Jai Relan researches vision-language-action (VLA) policies for robot manipulation, focusing on improving sample efficiency and safety. His work proposes primitive-aware training to enable few-shot transfer to novel assembly tasks and introduces a conformal…

## 📰 Embodied / Physical-AI News
- [Kawasaki Robotics to debut RL030N physical AI platform at Automate](https://www.therobotreport.com/kawasaki-robotics-debut-rl030n-physical-ai-platform-automate/) — _The Robot Report_
- [Genesis AI launches Eno general-purpose robot](https://www.therobotreport.com/genesis-ai-launches-eno-general-purpose-robot/) — _The Robot Report_
- [Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/) — _The Robot Report_
- [PSYONIC partners with ABB Robotics to apply human touch to robot dexterity](https://www.therobotreport.com/psyonic-abb-robotics-partner-apply-human-touch-data-robot-dexterity/) — _The Robot Report_
- [Autonomous freight developer Einride goes public via SPAC](https://www.therobotreport.com/autonomous-freight-developer-einride-goes-public-via-spac/) — _The Robot Report_
- [Burro introduces Grande 44 with proven outdoor autonomy built for heavy industry](https://www.therobotreport.com/burro-introduces-grande-44-with-proven-outdoor-autonomy-built-for-heavy-industry/) — _The Robot Report_
- [Modernizing the global economy with industrial robotics is needed but not inevitable](https://www.therobotreport.com/modernizing-global-economy-industrial-robotics-needed-not-inevitable/) — _The Robot Report_
- [Windows for robots: Edge AI expands usability](https://www.therobotreport.com/computers-software-windows-utility-robots/) — _The Robot Report_
- [Visual Language Models Train Robots to Read Human Emotions](https://spectrum.ieee.org/robot-emotions-visual-language-models) — _IEEE Spectrum_
- [olmo-eval: An evaluation workbench for the model development loop](https://huggingface.co/blog/allenai/olmo-eval) — _Hugging Face - Blog_
- [AI in warehousing: Akash Gupta’s vision for the future](https://www.therobotreport.com/ai-in-warehousing-akash-guptas-vision-for-the-future/) — _The Robot Report_
- [MassRobotics announces the winners of 2026 Robotics Medal and Rising Star awards](https://www.therobotreport.com/massrobotics-announces-winners-2026-robotics-medal-rising-star-awards/) — _The Robot Report_
- [Robotics Summit panel explores the state of humanoid robot design](https://www.therobotreport.com/robotics-summit-panel-explores-state-humanoid-robot-design/) — _The Robot Report_
- [Gatik to bring autonomous freight to PepsiCo’s North American supply chain](https://www.therobotreport.com/gatik-brings-autonomous-freight-pepsico-north-american-supply-chain/) — _The Robot Report_
- [Award-Winning Researcher Trains Robots to Make Educated Guesses](https://spectrum.ieee.org/researcher-trains-robots-to-guess) — _IEEE Spectrum_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
