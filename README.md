# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-10-29 · **Tracked:** 2037 core · 1394 adjacent ·
683 news · **36731** benchmark rows across **15732** model
variants · **30** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **Vision-Language-Action Models and Post-Training** | 1384 | 📈 rising | Covers VLA model design, action generation, RL fine-tuning, instruction following, and adaptation. |
| **World Model Architectures and Training** | 280 | 📈 rising | Focuses on JEPA-based latent dynamics, action-conditioned prediction, inverse dynamics, and representation learning for… |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **8.31** | IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies | 2026-09-10 | spd 9 · gen 7 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2609.10915) · [pdf](https://arxiv.org/pdf/2609.10915v1) |
| **8.23** | Flash-WAM: Modality-Aware Distillation for World Action Models | 2026-06-03 | spd 9 · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.05254) · [pdf](https://arxiv.org/pdf/2606.05254v1) |
| **8.23** | VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models | 2026-09-03 | spd 8 · gen 6 · spec 9 · cost 7 | [abs](https://arxiv.org/abs/2609.04355) · [pdf](https://arxiv.org/pdf/2609.04355v1) |
| **8.18** | GreenWAM: A World Foundation Model for Robotics | 2026-10-13 | spd 5 · gen 9 · spec 8 · cost – | [abs](https://arxiv.org/abs/2610.18774) · [pdf](https://arxiv.org/pdf/2610.18774v1) |
| **8.15** | Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models | 2026-10-01 | spd 9 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2610.00864) · [pdf](https://arxiv.org/pdf/2610.00864v1) · [code](https://github.com/IntelChina-AI/K-MF) |
| **8.12** | TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM | 2026-07-29 | spd 9 · gen 3 · spec 8 · cost 9 | [abs](https://arxiv.org/abs/2607.27205) · [pdf](https://arxiv.org/pdf/2607.27205v1) · [code](https://github.com/H-EmbodVis/TurboVLA) |
| **8.12** | MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO? | 2026-09-03 | spd 9 · gen 3 · spec 8 · cost 9 | [abs](https://arxiv.org/abs/2609.03715) · [pdf](https://arxiv.org/pdf/2609.03715v1) · [code](https://github.com/k1000dai/MINERVA) |
| **8.11** | Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving | 2026-07-17 | spd 9 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2607.15621) · [pdf](https://arxiv.org/pdf/2607.15621v1) |
| **8.1** | CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators | 2026-08-27 | spd – · gen 9 · spec 7 · cost – | [abs](https://arxiv.org/abs/2608.27406) · [pdf](https://arxiv.org/pdf/2608.27406v1) · [code](https://github.com/omni-CLAP/clap) |
| **8.09** | DriftWorld: Fast World Modeling through Drifting | 2026-07-16 | spd 9 · gen 6 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2607.15065) · [pdf](https://arxiv.org/pdf/2607.15065v1) · [code](https://github.com/Susie-Lu/driftworld) |
| **8.09** | Keep the Future, Drop the Rollout: RIFT for World Action Models | 2026-08-12 | spd 8 · gen 6 · spec 9 · cost 7 | [abs](https://arxiv.org/abs/2608.11521) · [pdf](https://arxiv.org/pdf/2608.11521v1) |
| **8.09** | Action Jets: Learning the Local Shape of the Action-conditioned Data Manifold | 2026-10-13 | spd 9 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2610.19007) · [pdf](https://arxiv.org/pdf/2610.19007v1) |
| **8.01** | RealtimeWAM: How Fast Can I Run My World Action Model? | 2026-10-07 | spd 9 · gen 7 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2610.10079) · [pdf](https://arxiv.org/pdf/2610.10079v1) |
| **8.01** | 1Step-WAM: Your World Action Model but Faster using 1-Step Action Generation | 2026-10-11 | spd 9 · gen 6 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2610.15625) · [pdf](https://arxiv.org/pdf/2610.15625v1) · [code](https://github.com/changdong1687/1Step-WAM) |
| **7.96** | VLA-ULAP: Interleaving Cloud VLA Calls with Ultra-Lightweight Local Action Prediction at the Edge | 2026-09-16 | spd 9 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2609.18663) · [pdf](https://arxiv.org/pdf/2609.18663v1) |
| **7.94** | SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model | 2026-10-20 | spd – · gen 5 · spec 9 · cost – | [abs](https://arxiv.org/abs/2610.28480) · [pdf](https://arxiv.org/pdf/2610.28480v1) |
| **7.87** | Reinforced Planning with Latent World Models | 2026-08-19 | spd 8 · gen 6 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2608.18669) · [pdf](https://arxiv.org/pdf/2608.18669v1) |
| **7.87** | RealtimeWAM: One-Step Asynchronous World Action Models | 2026-10-05 | spd 8 · gen 6 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2610.06617) · [pdf](https://arxiv.org/pdf/2610.06617v1) · [code](https://github.com/ModelTC/LightX2V) |
| **7.87** | Self-Improving Video-to-Action Models | 2026-10-16 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2610.24177) · [pdf](https://arxiv.org/pdf/2610.24177v1) |
| **7.85** | RoboJEPA: Scaling Robotic Latent World Models | 2026-10-07 | spd – · gen 8 · spec 6 · cost – | [abs](https://arxiv.org/abs/2610.10515) · [pdf](https://arxiv.org/pdf/2610.10515v1) · [code](https://github.com/facebookresearch/robo_jepa) |
| **7.84** | Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience | 2026-10-19 | spd 7 · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2610.26855) · [pdf](https://arxiv.org/pdf/2610.26855v1) |
| **7.83** | Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference | 2026-08-05 | spd 9 · gen – · spec 4 · cost 7 | [abs](https://arxiv.org/abs/2608.04428) · [pdf](https://arxiv.org/pdf/2608.04428v1) |
| **7.8** | Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks | 2026-09-29 | spd 8 · gen 6 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2609.36471) · [pdf](https://arxiv.org/pdf/2609.36471v1) |
| **7.79** | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models | 2026-06-24 | spd 8 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.25473) · [pdf](https://arxiv.org/pdf/2606.25473v1) · [code](https://github.com/NVlabs/rcm) |
| **7.79** | OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining | 2026-09-07 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2609.07398) · [pdf](https://arxiv.org/pdf/2609.07398v1) · [code](https://github.com/OpenWAM-Official/OpenWAM) |
| **7.79** | Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation | 2026-09-17 | spd 8 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2609.19579) · [pdf](https://arxiv.org/pdf/2609.19579v1) |
| **7.79** | What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling | 2026-09-28 | spd 8 · gen 7 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2609.34981) · [pdf](https://arxiv.org/pdf/2609.34981v1) |
| **7.79** | TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency | 2026-10-13 | spd 8 · gen 7 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2610.17540) · [pdf](https://arxiv.org/pdf/2610.17540v1) · [code](https://github.com/NVlabs/alpasim) |
| **7.74** | Video Prediction Policy 2: Predict Better, Act Better | 2026-10-07 | spd – · gen 8 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2610.10270) · [pdf](https://arxiv.org/pdf/2610.10270v1) |
| **7.74** | VioLA: Learning Generalist Humanoid Control Policies from Human Data | 2026-10-08 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2610.12435) · [pdf](https://arxiv.org/pdf/2610.12435v1) |
| **7.73** | BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving | 2026-06-07 | spd 8 · gen 3 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2606.08684) · [pdf](https://arxiv.org/pdf/2606.08684v1) · [code](https://github.com/George-Ling3/BLUE) |
| **7.73** | Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies | 2026-09-21 | spd 8 · gen 7 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2609.24682) · [pdf](https://arxiv.org/pdf/2609.24682v1) · [code](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| **7.73** | $Δ$ Flow Matching for Robot Foundation Models | 2026-10-11 | spd 8 · gen 6 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2610.15794) · [pdf](https://arxiv.org/pdf/2610.15794v1) |
| **7.72** | Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model | 2026-07-13 | spd – · gen 7 · spec 8 · cost 2 | [abs](https://arxiv.org/abs/2607.11643) · [pdf](https://arxiv.org/pdf/2607.11643v1) |
| **7.72** | Forward Dynamics Models | 2026-10-09 | spd 5 · gen 6 · spec 9 · cost 6 | [abs](https://arxiv.org/abs/2610.13117) · [pdf](https://arxiv.org/pdf/2610.13117v1) |
| **7.71** | LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies | 2026-06-14 | spd 7 · gen 7 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15768) · [pdf](https://arxiv.org/pdf/2606.15768v1) |
| **7.71** | StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models | 2026-08-12 | spd 5 · gen 8 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2608.11671) · [pdf](https://arxiv.org/pdf/2608.11671v1) |
| **7.67** | vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models | 2026-06-06 | spd 8 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.08094) · [pdf](https://arxiv.org/pdf/2606.08094v1) · [code](https://github.com/ggml-org/llama.cpp) |
| **7.67** | Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models | 2026-06-16 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.17846) · [pdf](https://arxiv.org/pdf/2606.17846v1) · [code](https://github.com/QwenLM/Qwen-RobotManip) |
| **7.67** | One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation | 2026-08-26 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2608.26058) · [pdf](https://arxiv.org/pdf/2608.26058v1) |
| **7.67** | Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA | 2026-10-04 | spd 7 · gen 5 · spec 6 · cost 9 | [abs](https://arxiv.org/abs/2610.05025) · [pdf](https://arxiv.org/pdf/2610.05025v1) |
| **7.67** | World Action Modeling with Progressive Visual Planning | 2026-10-01 | spd 5 · gen 8 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2610.02508) · [pdf](https://arxiv.org/pdf/2610.02508v1) |
| **7.67** | Long-WAM: Scaling the Context of World-Action Models | 2026-10-07 | spd 7 · gen 8 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2610.10528) · [pdf](https://arxiv.org/pdf/2610.10528v1) |
| **7.67** | World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer | 2026-10-27 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2610.37518) · [pdf](https://arxiv.org/pdf/2610.37518v1) · [code](https://github.com/enactic/openarm) |
| **7.66** | Cosmos 3: Omnimodal World Models for Physical AI | 2026-06-01 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02800) · [pdf](https://arxiv.org/pdf/2606.02800v1) · [code](https://github.com/nvidia/cosmos) |
| **7.66** | Multiplayer Interactive World Models with Representation Autoencoders | 2026-07-06 | spd 7 · gen 2 · spec 8 · cost 2 | [abs](https://arxiv.org/abs/2607.05352) · [pdf](https://arxiv.org/pdf/2607.05352v1) · [code](https://github.com/mira-wm/mira) |
| **7.66** | GlanceWAM: Sparse Test-Time Imagination for World-Action Models | 2026-08-25 | spd 8 · gen 6 · spec 7 · cost 5 | [abs](https://arxiv.org/abs/2608.23927) · [pdf](https://arxiv.org/pdf/2608.23927v1) · [code](https://github.com/linhanwang/GlanceWAM) |
| **7.66** | Reinforcement Learning for Real-Time Vision-Language-Action Policies | 2026-09-16 | spd 7 · gen 5 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2609.18207) · [pdf](https://arxiv.org/pdf/2609.18207v1) |
| **7.66** | Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining | 2026-09-30 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2610.00438) · [pdf](https://arxiv.org/pdf/2610.00438v1) |
| **7.66** | UNITAS: A 3D-Native World Action Model for Embodied Manipulation | 2026-10-08 | spd – · gen 7 · spec 8 · cost 4 | [abs](https://arxiv.org/abs/2610.12099) · [pdf](https://arxiv.org/pdf/2610.12099v1) · [code](https://github.com/DexForce/UNITAS) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _4860 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| KV baseline (growing cache) | — | inference state size at 100k steps | 25600000.0 | authors |
| π0.5 (LeRobot) _(lerobot/libero)_ | — | inference time per chunk | 12781.0 | authors |
| VLA-0 _(LIBERO-10)_ | — | median end-to-end latency | 6300.0 | authors |
| OpenVLA-7B _(LIBERO)_ | — | I(X; X~) (attack channel capacity) | 5000.0 | authors |
| AURA-Mem | — | inference state size | 4224.0 | authors |
| Wan 2.2 (chunked) _(LIBERO-90)_ | — | FVD | 4177.0 | 3rd-party |
| π0.5 (BF16) _(π0.5)_ | — | energy per successful episode | 2836.0 | 3rd-party |
| OpenVLA-OFT (BF16) _(OpenVLA-OFT)_ | — | energy per successful episode | 2830.0 | 3rd-party |
| SimpleVLA-RL _(LIBERO)_ | Long | iterations to 90% success rate | 2450.0 | authors |
| vla.cpp | — | peak RSS | 2031.0 | authors |

#### CALVIN  ·  _214 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 99.5 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (1 task) | 99.3 | authors |
| MPCoT _(LIBERO, CALVIN ABC→D)_ | — | 3-step success rate | 96.8 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (2 tasks) | 96.6 | authors |
| AffordanceWAM _(Human videos + robot videos (affordance-annotated joint pre-training then task-specific fine-tuning))_ | — | Success Rate (1/5) | 96.1 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (2 tasks) | 95.9 | authors |
| SAPS (Cosine) _(CALVIN)_ | long-horizon chains (5 subtasks) | subtask success rate (ST-SR) | 94.85 | authors |
| VLM4VLA + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 94.4 | authors |
| MPCoT _(LIBERO, CALVIN ABC→D)_ | — | 4-step success rate | 93.7 | authors |
| VLM4VLA _(CALVIN ABC)_ | — | success rate (1 task) | 93.4 | authors |

#### RoboTwin  ·  _1305 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LingBot-VA | — | per-chunk latency | 8100.0 | authors |
| FARE _(RoboTwin 2.0)_ | — | inference latency | 6872.4 | authors |
| LingBot-VA _(RoboTwin 2.0)_ | — | inference latency | 6200.7 | authors |
| Fixed-interval Naive | 7-task aggregate | recovery attempts | 3781.0 | authors |
| Motus (Native) | — | observation-to-action latency | 2343.14 | authors |
| Async+RTC | — | mean jerk norm | 2022.2 | authors |
| π0.5 H10E10 | — | mean jerk norm | 1468.8 | authors |
| π0.5 H50E10 | — | mean jerk norm | 1463.7 | authors |
| Motus (Native) | — | GPU inference time per replan | 1455.69 | authors |
| REACT | — | mean jerk norm | 1219.0 | authors |

#### SimplerEnv  ·  _398 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Astra + GR00T _(SimplerEnv Bridge)_ | — | inference cost | 164.61 | authors |
| dense | pick-coke | serve latency p50 | 102.1 | authors |
| VLA-Pruner | pick-coke | serve latency p50 | 101.2 | authors |
| GeoAlign _(robot-domain RGB-D + Dpol (SimplerEnv-Fractal demonstrations))_ | Pick Coke Can | success rate | 100.0 | authors |
| S2-VLA | Eggplant in Basket | success rate | 100.0 | authors |
| actuation-slack refresh | pick-coke | serve latency p50 | 100.0 | authors |
| H-VLA _(FractalData (fine-tuned))_ | Google Robot (VM), Drawer+Apple | success rate | 98.0 | authors |
| OpenVLA-7b | Pick up | failure rate (FR) | 97.5 | authors |
| GR00T-N1.6 | Pick up | failed object coverage (FOC) | 97.1 | authors |
| Afford-VLA _(LIBERO + Affordance dataset)_ | Put Eggplant | Success rate | 96.8 | authors |

#### RLBench  ·  _80 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PointACT _(RLBench (10 tasks))_ | Close laptop lid | success rate | 99.0 | authors |
| Uni-LaDiR | — | success rate | 87.0 | authors |
| LaST0 | — | success rate | 82.0 | 3rd-party |
| FASA (3D-DA) | — | average success rate | 77.48 | authors |
| AWAM | — | success rate | 76.5 | authors |
| 3D Diffuser Actor | — | average success rate | 75.96 | 3rd-party |
| TVVE | — | success rate | 75.0 | 3rd-party |
| EO1 (reproduced) _(RLBench (10 tasks))_ | Mean | success rate | 73.2 | 3rd-party |
| ARP | — | success rate | 73.0 | 3rd-party |
| RVT2 | — | success rate | 72.8 | 3rd-party |

#### Meta-World  ·  _223 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| TROJANWORLD _(clean training data from victim agent)_ | average across Drawer Open and Window Close | CR | 1665.11 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | push | return | 1641.0 | authors |
| Oracle inverse | reach, push, pick-place | mean cumulative reward | 485.5 | authors |
| RLS | reach, push, pick-place | mean cumulative reward | 434.41 | authors |
| Replay | reach, push, pick-place | mean cumulative reward | 428.59 | authors |
| SpikeWorld _(multimodal cache (SHD, SSC, text, image, video) + Meta-World)_ | reach, push, pick-place | mean cumulative reward | 422.58 | authors |
| Full prediction tuning _(same as SpikeWorld (further tuning on Meta-World))_ | reach, push, pick-place | mean cumulative reward | 422.19 | authors |
| SmolVLA | Mug position | Natural MAE | 128.314 | authors |
| VICX _(Meta-World (drawer-open, reach, basketball))_ | coffee-button | success rate | 100.0 | authors |
| RECON _(expert demonstrations + online interaction)_ | Drawer Open | success rate | 100.0 | authors |

#### ManiSkill  ·  _153 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| CompCPZ _(ManiSkill3 (200 synthetic frames for YOLOv8n fine-tune))_ | Pooled 18 families | paired sign test wins | 1900.0 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.99)_ | lift-cube | return | 175.0 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | pick-cube | return | 147.0 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 98.68 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 97.44 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 95.78 | authors |
| Teacher _(OpenVLA-OFT after GRPO RL)_ | PutOnPlateInScene25Main-v3 | success-once | 93.8 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 93.14 | authors |
| π0.5 | — | success rate | 89.8 | authors |
| π0.5 _(RL on ManiSkill)_ | — | success rate | 89.1 | authors |

#### RoboCasa  ·  _511 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Always train | Composite-Unseen | GPU minutes (training) | 3411.0 | authors |
| Joint-WAM _(RoboCasa)_ | — | inference latency | 593.1 | authors |
| LAWA _(RoboCasa + egocentric videos)_ | — | inference latency | 338.5 | authors |
| Fast-WAM _(RoboCasa)_ | — | inference latency | 196.5 | authors |
| Axiom-0 _(pretrain_human300)_ | — | mean generation latency | 135.55 | authors |
| Xiaomi-Robotics-1 | — | mean generation latency | 133.25 | authors |
| Cosmos-Policy | Turn Off Microwave | success rate | 100.0 | authors |
| ALDER | Drawer and Door (pooled) | prediction coverage | 100.0 | authors |
| Z-1 RL _(RoboCasa demonstrations)_ | Door | success rate | 97.0 | authors |
| Z-1 SFT _(RoboCasa demonstrations)_ | Door | success rate | 93.2 | authors |

#### Open-X / RT  ·  _114 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LAVLA (w/ PCA w/ weighted) _(Open-X-Embodiment)_ | — | CH Index | 1651.0 | authors |
| LAVLA (w/ PCA) _(Open-X-Embodiment)_ | — | CH Index | 1063.9 | authors |
| 4DNeX | 300 held-out trajectories | FVD | 818.0 | 3rd-party |
| TesserAct | 300 held-out trajectories | FVD | 746.0 | 3rd-party |
| Wan 2.1 14B | 300 held-out trajectories | FVD | 671.0 | 3rd-party |
| LAVLA (baseline) _(Open-X-Embodiment)_ | — | CH Index | 402.12 | authors |
| LVP | 300 held-out trajectories | FVD | 330.0 | 3rd-party |
| PointAction _(BridgeData V2 + DROID (filtered ~75K clips))_ | 300 held-out trajectories | FVD | 320.0 | authors |
| VisualThink-VLA _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 89.49 | authors |
| FullSoft _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 88.45 | authors |

#### ALFWorld  ·  _65 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GIGPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 90.4 | authors |
| Online WMSFT _(ALFWorld)_ | — | success rate | 90.4 | authors |
| KnOTS(V) _(ALFWorld)_ | — | success rate | 87.8 | authors |
| GRPO-COIN _(ALFWorld)_ | — | pass@64 | 87.23 | authors |
| WMRL->PRL _(ALFWorld)_ | — | success rate | 87.0 | authors |
| PRL _(ALFWorld)_ | — | success rate | 84.6 | authors |
| GRPO-GT _(ALFWorld)_ | — | pass@64 | 83.94 | authors |
| GRPO-MIS _(ALFWorld)_ | — | pass@64 | 83.21 | authors |
| GRPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 77.9 | authors |
| OPSD-MIS _(ALFWorld)_ | — | pass@64 | 75.55 | authors |

#### VBench  ·  _1565 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| HunyuanVideo (no caching) | 33 prompts from VBench | Latency | 1359.0 | authors |
| Full | — | Latency | 1075.7 | authors |
| Wan2.1-14B | — | latency | 948.0 | authors |
| RoPeSLR _(OpenVid-1M (subset))_ | — | Latency | 598.3 | authors |
| RoLA _(OpenVid-1M (subset))_ | — | Latency | 409.3 | authors |
| MDD | — | latency | 321.0 | authors |
| EasyAnimateV5.1-12B | — | latency | 246.0 | authors |
| Wan-I2V | Cut & Drag | Flow-Err | 181.1 | 3rd-party |
| GWTF | Cut & Drag | Flow-Err | 152.81 | 3rd-party |
| PTQ4DiT | — | FVD-FP | 124.2 | authors |

#### AgiBot / GENIE  ·  _137 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| NebulaVLA-Homo | — | avg inference latency | 115.0 | authors |
| TAO-DA (Dual-Tower) _(AGIBOT G1 real-world teleoperation dataset)_ | Collaborative Tea | success rate | 100.0 | authors |
| π0.5 _(AGIBOT G1 real-world teleoperation dataset (fine-tuned))_ | Collaborative Tea | success rate | 100.0 | 3rd-party |
| V-Link _(AGIBOT A3 Ultra teleoperation data)_ | Autonomous Power-On | success rate | 98.0 | authors |
| TAO-DA (Dual-Tower) _(AGIBOT G1 real-world teleoperation dataset)_ | Dual-arm routing accuracy | per-class accuracy | 96.13 | authors |
| RoboRender (video) _(AgiBot-World-Alpha + DROID (~130k clips))_ | — | FVD | 93.9 | authors |
| Egocentric (ours) _(HumanNet (egocentric portion, 5000h subset))_ | Seen tasks (in-distribution) | success rate | 92.5 | authors |
| NebulaVLA-Heter | Packaging Line Material Feeding | success rate | 92.5 | authors |
| Reward as an Agent | — | Overall Accuracy | 91.0 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | Scene Consistency | 90.41 | authors |

#### Habitat  ·  _51 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ViewCrafter | sparse views-to-video | FVD | 778.207 | 3rd-party |
| TrajectoryCrafter | sparse views-to-video | FVD | 690.322 | 3rd-party |
| GEN3C | sparse views-to-video | FVD | 511.039 | 3rd-party |
| Pantheon360 _(360-1M (filtered))_ | sparse views-to-video | FVD | 450.696 | authors |
| multiple (LLaVA-1.6, GPT-4V, Gemini-1.5-Pro, InternVL2, OpenVLA) | — | success rate relative to oracle | 94.2 | authors |
| Qwen3.5-27B+SVA | — | success rate | 64.17 | authors |
| Qwen3.5-9B+SVA | — | success rate | 57.22 | authors |
| GPT-4o | — | success rate | 55.83 | authors |
| Qwen3.5-4B+SVA | — | success rate | 53.06 | authors |
| Qwen3.5-27B | — | success rate | 47.22 | 3rd-party |

#### BEHAVIOR  ·  _80 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| MPVI _(none (no additional training))_ | — | Q-score improvement | 113.0 | authors |
| π0.5 _(cleaned BEHAVIOR-1K demonstrations)_ | place_on | success rate | 100.0 | authors |
| SERF _(per-task finetune on BEHAVIOR-1K)_ | Failure recovery (object drop) | recovery success rate | 95.0 | authors |
| PI0.5 (ft) _(per-task finetune on BEHAVIOR-1K)_ | Failure recovery (object drop) | recovery success rate | 65.0 | authors |
| SERF _(per-task finetune on BEHAVIOR-1K)_ | Collecting Children's Toys | task progress | 63.5 | authors |
| SERF (env) _(per-task finetune on BEHAVIOR-1K)_ | Putting Shoes On Rack | task progress | 59.0 | authors |
| SBP _(per-task finetune on BEHAVIOR-1K)_ | Collecting Children's Toys | task progress | 57.9 | authors |
| PI0.5 (ft) _(per-task finetune on BEHAVIOR-1K)_ | Scene-configuration generalization (Additional Objects) | task progress | 50.6 | authors |
| π0.5 _(cleaned BEHAVIOR-1K demonstrations)_ | Turn on radio | progress score | 50.0 | authors |
| PI0.5 (pre) _(BEHAVIOR-1K (50 tasks))_ | Assembling Gift Baskets | task progress | 44.1 | authors |

#### nuScenes  ·  _394 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| DiST-4D | midpoint (α=0.5) | FVMD | 5381.67 | 3rd-party |
| SparseWorld-S _(nuScenes)_ | Inference memory | Inference Memory (IM) | 4397.0 | authors |
| FreeVS | midpoint (α=0.5) | FVMD | 4216.99 | 3rd-party |
| SymRegFlow (joint-generated) _(nuScenes)_ | midpoint (α=0.5) | FVMD | 2519.17 | authors |
| DriveGAN | video generation | FVD | 502.3 | 3rd-party |
| DriveDreamer | video generation | FVD | 452.0 | 3rd-party |
| Direct Regression (AnchoredVAEDiT) | future frame prediction | FID | 370.8 | authors |
| Vanilla Flow _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 304.1 | 3rd-party |
| REPA w/ DINOv2 _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 295.9 | 3rd-party |
| Self-Flow _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 283.3 | 3rd-party |

#### PushT  ·  _179 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LeWM _(LeWM offline datasets)_ | — | planning time | 669.6 | 3rd-party |
| LeWM + CEM | — | eval time | 198.92 | 3rd-party |
| Teacher (canonical encoding) _(canonical encoding)_ | — | retrieval rank (held-out) | 169.8 | authors |
| LeWM + AITS | — | success rate | 100.0 | authors |
| DA-LeWM | — | success rate | 98.7 | authors |
| VIS-WM | — | success rate | 98.0 | authors |
| SA+IDM | — | success rate | 98.0 | authors |
| UVA | — | success rate | 97.47 | authors |
| MemWM | — | success rate | 96.7 | authors |
| FF-JEPA (DM) _(PushT filtered successful demonstrations)_ | Short-horizon (t=25) | success rate | 96.09 | authors |

#### Bench2Drive  ·  _178 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| BLUE _(SimLingo training set (~400 routes))_ | — | latency | 549.5 | authors |
| ORION _(Bench2Drive, Chat-B2D)_ | trajectory prediction | decoder latency | 497.52 | authors |
| CLEAR (InternVL3-1B) _(SimLingo dataset (~3.1M samples))_ | — | Efficiency | 275.4 | authors |
| SimLingo+SA _(SimLingo dataset)_ | — | Latency | 214.01 | authors |
| Reflect-VLA-4B | — | Effi | 212.2 | authors |
| VLGA _(Bench2Drive train routes)_ | — | Efficiency | 194.63 | authors |
| ORION _(Bench2Drive, Chat-B2D)_ | command probe | command-probe accuracy | 97.7 | authors |
| LinkVLA _(PDM-Lite)_ | — | Driving Score | 91.01 | 3rd-party |
| BLUE _(SimLingo training set (~400 routes))_ | — | driving score | 90.58 | authors |
| OccWAM _(Bench2Drive (PDM-Lite expert), Chat-B2D)_ | — | Driving Score | 90.45 | authors |

#### NAVSIM  ·  _176 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ours† _(OpenScene (NAVSIM train split))_ | planning | Comf. | 100.0 | authors |
| WCog-VLA-2B _(NAVSIM + 158k open-source driving VQA samples + 170k NAVSIM-tailored samples (85k trajectory-specific VQA + 85k Game-CoT))_ | — | NC (no at-fault collision) | 99.4 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | NC | 98.7 | authors |
| SafeAlign-VLA _(NAVSIM navtrain)_ | trajectory planning | NC | 98.6 | authors |
| WCog-VLA-2B _(NAVSIM + 158k open-source driving VQA samples + 170k NAVSIM-tailored samples (85k trajectory-specific VQA + 85k Game-CoT))_ | — | TTC (time-to-collision) | 98.5 | authors |
| S2-VLA _(ReCogDrive VQA + NAVSIM)_ | — | NC | 98.4 | authors |
| GeoCoTDrive _(NAVSIM + PlanningGrounding)_ | — | NC | 98.4 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | DAC | 98.2 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | TTC | 95.9 | authors |
| GeoCoTDrive _(NAVSIM + PlanningGrounding)_ | — | DAC | 95.6 | authors |

#### DROID  ·  _162 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Wan2.2 TI2V 5B _(DROID 700-sample pick-and-place subset)_ | — | inference time | 400.0 | 3rd-party |
| π0-FAST _(DROID (zero-shot))_ | average across three tasks (successful trajectories only) | action steps length | 269.0 | 3rd-party |
| MiniWorld-3B _(DROID)_ | — | Trajectory Accuracy improvement | 249.0 | authors |
| MiniWorld-3B _(DROID)_ | — | Depth Accuracy improvement | 238.0 | authors |
| MiniWorld-3B _(DROID)_ | — | LPIPS improvement | 216.0 | authors |
| SWAP _(offline trajectories from candidate policies on DROID tasks)_ | average across three tasks (successful trajectories only) | action steps length | 193.0 | authors |
| TesserAct | — | FID | 164.54 | 3rd-party |
| MiniWorld-3B _(DROID)_ | — | SSIM improvement | 125.0 | authors |
| SWAP _(offline trajectories from candidate policies on DROID tasks)_ | Marker → Bowl | success rate | 100.0 | authors |
| Causally Interleaved _(DROID)_ | — | Accuracy@0.5 | 94.52 | authors |

#### NAVSIM v1  ·  _154 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| UNIVERSE w.o. Mask _(NAVSIM v1)_ | — | inference latency | 1623.0 | authors |
| UNIVERSE Two-DiT _(NAVSIM v1)_ | — | inference latency | 551.0 | authors |
| AMPT _(NAVSIM)_ | failure recovery | recovered scenes | 440.0 | authors |
| UNIVERSE _(NAVSIM v1)_ | — | inference latency | 376.0 | authors |
| Original GRPO _(NAVSIM)_ | failure recovery | recovered scenes | 367.0 | authors |
| Full-depth planner _(NAVSIM)_ | — | end-to-end planning latency | 320.0 | authors |
| Fixed B15 (single trajectory) _(NAVSIM)_ | — | end-to-end planning latency | 190.0 | authors |
| Adaptive-WAM _(NAVSIM)_ | — | end-to-end planning latency | 170.0 | authors |
| CoPhy _(NAVSIM v1+v2)_ | — | C | 100.0 | authors |
| CoPhy _(NAVSIM v1+v2)_ | — | NC | 99.0 | authors |

#### Real-world  ·  _151 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| InSight _(50 human scooping demonstrations + acquired lateral-push primitive)_ | sweeping | success rate | 100.0 | authors |
| SAGE-SFT _(π0.5)_ | Place the green cube on the plate | Success rate | 100.0 | authors |
| OASIS | Goal | success rate | 98.6 | authors |
| MambaAct | Nut Pouring | final success rate | 96.9 | authors |
| InSight _(50 human pick-and-place demonstrations + 20 successful pour primitives)_ | pour beans into bowl | success rate | 96.0 | authors |
| 3DThinkVLA (Ours) _(VLA data + 3D reasoning data (co-training))_ | Transparent container placement | success rate | 93.3 | authors |
| Seer + FlowVLA _(Real-world 40 demos per task)_ | Stack Cups | success rate | 93.3 | authors |
| InSight _(50 human pick-and-place demonstrations + 20 successful twist primitives)_ | twist cap open | success rate | 92.0 | authors |
| π0.5 | Nut Pouring | final success rate | 91.3 | authors |
| CF-Prune (α=35%) _(Real-world demonstration)_ | — | overall success rate | 90.7 | authors |

#### DAVIS  ·  _141 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Image Conductor | joint object and camera control | EPE | 91.64 | 3rd-party |
| Ours VAE _(in-house synthetic dataset)_ | reconstruction | VBench Total | 82.93 | authors |
| LightX2V VAE | reconstruction | VBench Total | 82.44 | authors |
| CoTracker3 | — | DCAavg | 71.81 | 3rd-party |
| CoTracker3 | — | AJ | 62.9 | 3rd-party |
| LPA-CWM _(MOVi-F)_ | — | DCAavg | 58.98 | authors |
| APA-CWM | — | DCAavg | 55.79 | authors |
| RAFT | — | DCAavg | 49.0 | 3rd-party |
| SEA-RAFT | — | DCAavg | 47.39 | 3rd-party |
| LPA-CWM _(MOVi-F)_ | — | AJ | 45.29 | authors |

#### OGBench  ·  _135 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| CoFi | PointMaze-Giant | success rate | 96.0 | authors |
| ProWorld _(OGBench)_ | PushT | success rate | 94.0 | authors |
| QPILOTS-M _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 90.0 | authors |
| QPILOTS-U _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 89.0 | authors |
| FIRM-WM | Cube | success rate | 88.0 | authors |
| WMPA | scene-play | success rate | 87.0 | authors |
| QAM-E _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 85.0 | 3rd-party |
| DTRC | HumanoidMaze-Medium | success rate | 84.7 | authors |
| CDGS | AntMaze-Giant | success rate | 84.0 | 3rd-party |
| LeWM _(OGBench)_ | PushT | success rate | 83.33 | authors |

#### RoboMME  ·  _133 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Human | — | success rate | 90.5 | 3rd-party |
| Human Performance | — | average success rate | 90.5 | 3rd-party |
| TacitVLA | Counting | success rate | 89.5 | authors |
| SimpleMemVLA _(RoboMME)_ | — | success rate | 88.3 | authors |
| SimpleMemVLA | — | success rate | 88.3 | authors |
| LTM-pi (CD-LAM) _(RoboMME-10x)_ | — | success rate | 87.5 | authors |
| Tracker _(RoboMME demonstrations)_ | Permanence suite | success rate | 87.2 | authors |
| LEDGER _(RoboMME demonstrations)_ | Permanence suite | success rate | 86.7 | authors |
| Explicit Reasoning | Counting | success rate | 86.7 | authors |
| Oracle | — | success rate | 84.1 | 3rd-party |

#### TwoRoom  ·  _125 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LeWM + CEM | — | eval time | 224.78 | 3rd-party |
| DINO-WM | — | success rate | 100.0 | 3rd-party |
| LeFlow _(offline trajectory data from LeWM benchmarks)_ | — | success rate | 100.0 | authors |
| GCBC | — | success rate | 100.0 | 3rd-party |
| GCIVL | — | success rate | 100.0 | 3rd-party |
| GCIQL | — | success rate | 100.0 | 3rd-party |
| SA+IDM | — | success rate | 100.0 | authors |
| ALeWM _(TwoRoom)_ | — | success rate | 100.0 | authors |
| LeWM + NGC (Oracle Predictor) | offset 75 | success rate | 100.0 | authors |
| RWM | — | success rate | 99.67 | authors |

#### Push-T  ·  _108 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PPO-3K+AIM500 _(3k expert episodes + 500 AIM actively collected episodes)_ | BC (H=33) | BC Arena Elo | 1190.0 | authors |
| PPO-3K _(3k expert episodes (PPO))_ | BC (H=33) | BC Arena Elo | 732.0 | authors |
| Traj-LeWM _(public LeWM datasets (Push-T, OGBench-Cube, Reacher, Two-Room))_ | — | success rate | 99.0 | authors |
| SD-JEPA _(offline datasets (LEWM protocol))_ | — | success rate | 97.3 | authors |
| LeWM _(offline datasets)_ | — | success rate | 96.0 | 3rd-party |
| LeWM _(public LeWM datasets (Push-T, OGBench-Cube, Reacher, Two-Room))_ | — | success rate | 96.0 | authors |
| F-JEPA | — | success rate | 96.0 | authors |
| LeWM | — | success rate | 96.0 | 3rd-party |
| LRC-JEPA _(simulated environments)_ | — | success rate | 96.0 | authors |
| IMWM _(demonstration windows per task)_ | — | success rate | 92.7 | authors |

## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
- **ActionMap: Robot Policy Learning via Voxel Action Heatmap** — ActionMap replaces the unstructured single-point action decoder in VLA models with a voxel heatmap action head that predicts a probability distribution over a discretized 3D action space, explicitly exploiting the geometric proximity of neighboring actions rather than treating the action space as unstructured… _(→ WAM: In World Action Models, the action conditioning mechanism is critical for predicting how actions transform world states. The voxel heatmap representation can transfer in two ways: (1) as a structured action encoding input to the world model—replacing flat…)_ [abs](https://arxiv.org/abs/2606.06904) · [pdf](https://arxiv.org/pdf/2606.06904v1) · [code](https://github.com/showlab/ActionMap)
- **Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs** — ST-Merge is a plug-and-play, training-free spatio-temporal visual token merging framework that reduces inference latency by fusing redundant visual tokens during the visual encoding phase. It constructs 3D spatiotemporal coordinates for multi-queue parallel matching and weighted aggregation across frames, and… _(→ WAM: World Action Models must process long video histories to predict future world states and generate actions, making visual token count a critical computational bottleneck. ST-Merge's spatio-temporal token merging could be directly applied to the visual encoder…)_ [abs](https://arxiv.org/abs/2606.29350) · [pdf](https://arxiv.org/pdf/2606.29350v1) · [code](https://github.com/Junzhou-Chen/ST_Merge)
- **WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models** — A multi-dimensional, long-horizon evaluation framework for interactive world models that introduces novel metrics: per-frame action metrics to bypass semantic scale disparity, segment-based drift metrics to capture mid-sequence visual collapse, controllability-gated physics evaluation to isolate physical plausibility… _(→ WAM: World Action Models (WAMs) inherently suffer from compounding errors over long horizons, leading to visual drift, physical inconsistencies, and memory loss. The benchmark's metrics—particularly the controllability-gated physics evaluation and action-decoupled…)_ [abs](https://arxiv.org/abs/2606.31672) · [pdf](https://arxiv.org/pdf/2606.31672v1)
- **DWM: Separating World Effects from Actions in Latent World Models** — DWM decomposes latent world model transitions into an action-invariant world effect (environment-intrinsic dynamics like gravity, inertia, drift) and a complementary action-driven component, using an auxiliary world head regularized by a normalized world-contrastive objective to be action-invariant, coupled with an… _(→ WAM: World Action Models must predict future states conditioned on actions and then use those predictions to select or generate actions. DWM's decomposition transfers directly: (1) By separating action-invariant dynamics from action-driven effects, a WAM can more…)_ [abs](https://arxiv.org/abs/2607.18715) · [pdf](https://arxiv.org/pdf/2607.18715v1)
- **The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping** — The core innovation is identifying that the provenance of the gate signal—not the token-skipping mechanism itself (reuse vs. deletion)—determines closed-loop reliability in accelerated VLAs. When the gate is 'dirty' (harvested from the model's own accelerated/skipped forwards), compounding visibility errors cause… _(→ WAM: World Action Models operate in closed-loop rollouts where compounding prediction errors are already a central challenge. If WAMs adopt token skipping, caching, or pruning for efficient world-state prediction, the same self-harvested gate collapse will occur…)_ [abs](https://arxiv.org/abs/2608.00391) · [pdf](https://arxiv.org/pdf/2608.00391v1)
- **Proxy Policy Steering** — Proxy Policy Steering (PPS) adapts a frozen diffusion-based generalist policy at inference time by training two lightweight proxy policies—a reference proxy that models the base policy's behavior on target-task observations, and a task proxy initialized from the reference that captures behavior changes under task… _(→ WAM: WAMs that use diffusion-based action generation can adopt PPS's dual-proxy velocity-space steering to achieve task-specific adaptation without fine-tuning the world model. A generalist WAM encodes broad world dynamics and recovery capabilities; PPS would…)_ [abs](https://arxiv.org/abs/2609.09148) · [pdf](https://arxiv.org/pdf/2609.09148v1)
- **Spatial Grafting: Grounding 3D Features for Flow-Matching Robot Policies** — Spatial Grafting, a lightweight spatial module that binds frozen 3D reconstruction features to metric, robot-relative geometry and injects them into a flow-matching action expert via cross-attention, without modifying the host model's perceptual pathway. _(→ WAM: World Action Models (WAMs) typically leave interaction-relevant metric geometry implicit. Spatial Grafting can be directly applied to WAMs to provide them with explicit, robot-relative 3D spatial awareness. By injecting these grounded spatial tokens via…)_ [abs](https://arxiv.org/abs/2609.35249) · [pdf](https://arxiv.org/pdf/2609.35249v1) · [code](https://github.com/Physical-Intelligence/openpi)
- **ActionGround: Training-Free Runtime Refinement of Frozen VLA Policies** — A training-free, neuro-symbolic runtime layer that augments frozen Vision-Language-Action (VLA) policies by combining a phase-aware finite-state machine for symbolic, rule-based action corrections with an inertia-weighted Euler-Lagrange dynamics term that enforces physical constraints during action execution. _(→ WAM: World Action Models (WAMs) inherently generate action-conditioned future states but can suffer from generating physically implausible trajectories or losing track of task phase structure. This neuro-symbolic approach transfers directly to WAMs as a runtime…)_ [abs](https://arxiv.org/abs/2609.33256) · [pdf](https://arxiv.org/pdf/2609.33256v1)
- **GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives** — The core technical innovation is GroundingPI, a 4B grounding foundation model that reformulates visual grounding (points and boxes) as quantized coordinates in a shared vocabulary. It is trained via a multi-stage pipeline combining multimodal and spatial pretraining, supervised fine-tuning, and reinforcement learning… _(→ WAM: World Action Models (WAMs) typically rely on general-purpose video generation backbones that struggle with precise spatial localization, leading to errors in predicting object interactions and positions. GroundingPI's approach can transfer to WAMs by…)_ [abs](https://arxiv.org/abs/2609.39601) · [pdf](https://arxiv.org/pdf/2609.39601v1) · [code](https://github.com/groundingpi/GroundingPI)
- **WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation** — A safety framework that dynamically models a robot's whole-body and grasp-dependent attached geometry, converting this evolving geometry into differentiable Control Barrier Function (CBF) constraints to minimally modify actions for collision avoidance. _(→ WAM: WAMs predict future world states for planning and lookahead. WBAG's grasp-conditioned safe sets and differentiable CBFs can be integrated directly into a WAM's trajectory optimization or rollout loop. As the WAM predicts future states (including grasp…)_ [abs](https://arxiv.org/abs/2610.01083) · [pdf](https://arxiv.org/pdf/2610.01083v1)
- **A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies** — Feasible-Future Decoding: a training-free inference-time reranker that addresses the feasibility-likelihood gap in VLA policies. Instead of selecting actions solely by likelihood, it evaluates each candidate action by computing its 'feasible-future mass'—a quantity derived from the exact next-block marginal of the… _(→ WAM: World Action Models inherently combine action generation with world state prediction, making them naturally suited to evaluate the feasibility-likelihood gap. The feasible-future decoding approach can transfer directly: when a WAM proposes candidate actions…)_ [abs](https://arxiv.org/abs/2610.05166) · [pdf](https://arxiv.org/pdf/2610.05166v1)
- **Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation** — A graph-native agentic harness that coordinates the full pipeline from asset generation through scene construction to demonstration synthesis, with bounded repair — detecting failures at any stage, routing them back to the responsible module for targeted correction, while preserving unaffected scene state. This… _(→ WAM: The bounded repair mechanism directly transfers to WAM training and inference. At training time, the data engine already produces validated, replayable demonstrations that improved WAM success from 77.17% to 89.43% on LIBERO-Plus — proving that…)_ [abs](https://arxiv.org/abs/2610.02274) · [pdf](https://arxiv.org/pdf/2610.02274v1)
- **WAMJET: A Harness for World Action Model Acceleration** — An agentic, bottleneck-driven harness (WAMJET) that automates the selection, composition, and iterative refinement of inference acceleration techniques for World Action Models by equipping coding agents with reusable optimization guidance, profiling/measurement tools, and validation mechanisms. _(→ WAM: This innovation is directly applicable to World Action Models as it is specifically designed to solve their deployment bottleneck: the high computational cost of large video backbones and video-action co-prediction. By automating the engineering-heavy process…)_ [abs](https://arxiv.org/abs/2610.03797) · [pdf](https://arxiv.org/pdf/2610.03797v1) · [code](https://github.com/liulixinkerry/WAMJET)
- **Reading, Writing, Sharing, and Interacting with the World through Video** — A unifying conceptual framework that decomposes video world models into four complementary operations—Reading (inferring world properties), Writing (synthesizing video), Sharing (jointly understanding and generating), and Interacting (updating states under actions)—while explicitly distinguishing between temporal… _(→ WAM: The 'Interacting' operation directly maps to the core loop of a World Action Model (predicting and updating world states under actions). Additionally, the explicit distinction between video-level temporal coherence and latent world-state consistency provides…)_ [abs](https://arxiv.org/abs/2610.31668) · [pdf](https://arxiv.org/pdf/2610.31668v1) · [code](https://github.com/vid-gen/awesome-video-world-model)
- **Beyond Behaviour: A Stimulus-Response Safety Evaluation of Vision-Language-Action Models** — A stimulus-response safety evaluation framework that probes the dissociation between internal hazard registration and action output in VLA models, revealing that models can internally represent danger (visible hazards, harmful consequences) yet still default to task-execution actions rather than safety-oriented… _(→ WAM: This finding is critical for World Action Models because it reveals that simply having accurate world knowledge (internally registering danger) is insufficient for safe action generation. WAMs must explicitly bridge the gap between hazard perception and…)_ [abs](https://arxiv.org/abs/2610.34837) · [pdf](https://arxiv.org/pdf/2610.34837v1)
- **World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models** — CureWM introduces execution-verified counterfactual replay for post-hoc repair of world models' failure insensitivity (optimism bias). It constructs alternative actions from successful demonstrations across a severity grid, verifies their outcomes through actual execution in simulation or on hardware, and fine-tunes… _(→ WAM: World Action Models must predict action consequences and support planning/action selection, making failure insensitivity equally damaging. The counterfactual construction method transfers directly: take successful trajectories, perturb actions to create…)_ [abs](https://arxiv.org/abs/2610.09134) · [pdf](https://arxiv.org/pdf/2610.09134v1) · [code](https://github.com/jiuyixu25/CureWM)
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

## 👥 Influential Authors & Groups
- **[Kai-Peng Zhang](https://www.semanticscholar.org/author/2349384231)** (22 papers) — Kai-Peng Zhang's research focuses on video world models, particularly interactive, long-horizon, and controllable generation. This includes dynamic resource allocation, state decoupling, multi-agent simulation, and dataset construction for enabling real-time…
- **[Hao-Ang Li](https://www.semanticscholar.org/author/2384363611)** (17 papers) — Hao-Ang Li's research focuses on advancing World-Action Models (WAM) and Vision-Language-Action models for robotic manipulation and autonomous driving, with key contributions in spatial-aware semantic guidance, multi-view geometry, cross-embodiment learning…
- **[Hao-Yang Huang](https://www.semanticscholar.org/author/2345959136)** (15 papers) — Hao-Yang Huang's research focuses on world action models and world simulators, including action-conditioned video generation for robotic manipulation, long-horizon autoregressive video generation with memory mechanisms, and scaling real-time high-resolution…
- **[Wen-Xuan Song](https://www.semanticscholar.org/author/2293142288)** (15 papers) — World-Action Models (WAMs) enhancement for embodied AI, including spatiotemporal awareness, semantic foresight alignment, physical grounding, unified architectures, and extension to mobile manipulation and tactile dynamics, along with scalable embodied data…
- **[Nan Duan](https://www.semanticscholar.org/author/2360369479)** (14 papers) — Nan Duan's research focuses on advancing world models and real-time video generation for embodied AI, including action-conditioned video generation, long-horizon autoregressive video generation, and scalable world simulation for robotic manipulation.
- **[Jia-Jun Wu](https://www.semanticscholar.org/author/2326444500)** (14 papers) — Jia-Jun Wu's research centers on world-action models, unifying world modeling with robot control through shared latent actions, visual tracks, and action-conditioned video generation. The work spans foundation models for robot manipulation, test-time memory…
- **[Shang-Hang Zhang](https://www.semanticscholar.org/author/2346116279)** (14 papers) — Develops world action models (WAM) for robotic manipulation, focusing on safe exploration through interactive world models, latent action learning, process reward modeling, and improving action-conditioned simulator fidelity for policy learning.
- **[Pei-Yan Li](https://www.semanticscholar.org/author/2305635155)** (13 papers) — Developing data-efficient and generalizable Vision-Language-Action (VLA) models for robotic manipulation, including world action models, embodied chain-of-thought, and test-time scaling.
- **[Yan Huang](https://www.semanticscholar.org/author/2375031786)** (13 papers) — Yan Huang's WAM-related research centers on World Action Models (WAMs) for embodied AI, including architecture designs that unify action generation with visual foresight in latent space, memory-augmented and efficient variants, and analyses of world-model…
- **[Randall Balestriero](https://www.semanticscholar.org/author/2378151189)** (12 papers) — Randall Balestriero主要研究基于联合嵌入预测架构（JEPA）的世界模型和动作建模，包括防止时间特征坍塌的正则化方法（如DISReg）、端到端世界与动作联合建模（LeWAM）、利用辛哈密顿动力学保持潜在相空间体积（LeHami）、通过频谱对齐控制潜在表示（SpecWM）等。同时他也致力于开源世界模型平台（stable-worldmodel）和评估指标（VIScore）的研发。
- **[Jian-Fei Yang](https://www.semanticscholar.org/author/2404007795)** (12 papers) — Research focuses on Vision-Language-Action (VLA) models for robot manipulation, including gesture understanding, policy execution, spatial-semantic prompting, planning-execution gap closure, failure-driven self-improvement, multi-robot coordination, and…
- **[Peng-Wei Wang](https://www.semanticscholar.org/author/2338357829)** (12 papers) — Peng-Wei Wang's research focuses on scaling embodied intelligence for robotic manipulation through world action models, diffusion-based frameworks, and vision-language-action models. Key areas include data generation via self-improving simulations…
- **[Yan Wang](https://www.semanticscholar.org/author/2386705642)** (12 papers) — Developing World Action Models (WAMs) and Vision-Language-Action (VLA) models for autonomous driving and robot manipulation, focusing on improving spatiotemporal awareness, instruction following, and robustness to distribution shifts.
- **[Xin Zhang](https://www.semanticscholar.org/author/2333419153)** (11 papers) — Xin Zhang's research focuses on world models and world action models (WAM) for robotics, with contributions in density-guided KV cache compression, causal action effect reweighting, mixture-of-experts frameworks, tactile prediction, and geometry-aware action…
- **[Ye-Ying Jin](https://www.semanticscholar.org/author/2357234267)** (11 papers) — Ye-Ying Jin's research focuses on interactive world models for games and autonomous driving, using natural language as an action interface for multi-entity control (Incantation, H3-World), achieving cross-game generalization (SCOPE), state-aware…
- **[Yao Mu](https://www.semanticscholar.org/author/2348161293)** (11 papers) — Research focuses on world models and vision-language-action models for embodied control, including efficient representation learning (Enfold, GaussianWAM), safety evaluation (LIBERO-Safety), equivariant architectures (EquiVLA), video generation for world…
- **[Yi-Xiang Chen](https://www.semanticscholar.org/author/2366155958)** (11 papers) — Yi-Xiang Chen focuses on developing data-efficient Vision-Language-Action (VLA) frameworks for robotic manipulation, integrating world models and memory modules to improve generalization, long-horizon task performance, and real-world applicability.
- **[Zi-Ying Song](https://www.semanticscholar.org/author/2367119325)** (11 papers) — Zi-Ying Song's WAM-related research focuses on world models for embodied AI and autonomous driving, particularly improving joint embedding predictive architecture (JEPA) world models, latent dynamics learning, action-conditioned future prediction, and…
- **[Yann LeCun](https://www.semanticscholar.org/author/2270469816)** (10 papers) — Yann LeCun's WAM research focuses on developing and optimizing Joint-Embedding Predictive Architecture (JEPA) and its variants (e.g., AD-E2E-JEPA, LeHami, H-JEPA, AdaJEPA) for world models, applied to autonomous driving, robotic planning, and manipulation. He…
- **[Yong Li](https://www.semanticscholar.org/author/2300459663)** (10 papers) — Yong Li's research centers on world models and world-action models for planning, control, and video generation, including adaptive multi-modal reasoning, interaction-aware training, causal action effect reweighting, and mixture-of-experts architectures…
- **[M. Shou](https://www.semanticscholar.org/author/2047358650)** (10 papers) — M. Shou's research focuses on Vision-Language-Action (VLA) models for robot manipulation and autonomous driving, including improving VLA robustness via failure-boundary learning, trajectory priors, voxel action heatmaps, and geometry-guided adaptation from…
- **[Guo-Cai Yao](https://www.semanticscholar.org/author/2376597393)** (10 papers) — Guo-Cai Yao's research focuses on developing hierarchical visuo-tactile world models and physically-grounded vision-language-action models for dexterous and contact-rich robot manipulation, with emphasis on contact prediction, planning, safety, and…
- **[Yuan Xu](https://www.semanticscholar.org/author/2313357459)** (10 papers) — Yuan Xu's WAM research focuses on developing data-efficient Vision-Language-Action (VLA) models for robotic manipulation, integrating world models, memory augmentation, and test-time scaling to improve generalization and long-horizon task performance.
- **[Qi-Feng Chen](https://www.semanticscholar.org/author/2257095769)** (10 papers) — Qi-Feng Chen works on building controllable world simulators with persistent dynamic memory (WorldDirector), decoupling actions for plausible hand-object interactions (EgoACT), and developing real-time interactive audio-visual world models (HelixWorld…
- **[Xiao-Wei Chi](https://www.semanticscholar.org/author/2192825554)** (10 papers) — Xiao-Wei Chi's research focuses on developing World-Action Models (WAMs) for embodied AI, including safe RL with world models, efficient video-based action planning, and multimodal (vision, tactile) world modeling for robotic manipulation, with a strong…

## 📰 Embodied / Physical-AI News
- [AGIBOT introduces Worken to measure robot productivity at AGIBOT Innovation Day 2026](https://www.therobotreport.com/agibot-introduces-worken-measure-robot-productivity-innovation-day-2026/) — _The Robot Report_
- [Granite Switch 4.1.1 — Update models like you update software](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1) — _Hugging Face - Blog_
- [Announcing Project ProtoStar: Making Publicly Funded Science AI-Ready](https://huggingface.co/blog/announcing-project-protostar) — _Hugging Face - Blog_
- [Welcome Le Chonk: Mistral Large 4 on Hugging Face](https://huggingface.co/blog/mistral-large4) — _Hugging Face - Blog_
- [Introducing AnySpeechRecognizer and AnyDecisionModel: Open Models for Speech and Decisions on Apple Platforms](https://huggingface.co/blog/anydecisionmodel) — _Hugging Face - Blog_
- [Warp Sciences emerges from stealth, to apply robotics to drug research](https://www.therobotreport.com/warp-sciences-emerges-stealth-apply-robotics-drug-research/) — _The Robot Report_
- [WorldOracle Tests Whether World Models Can Reliably Predict Real-World Executions](https://www.therobotreport.com/worldoracle-tests-whether-world-models-can-reliably-predict-real-world-executions/) — _The Robot Report_
- [NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription You Can Prompt and Adapt](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) — _Hugging Face - Blog_
- [North American robot orders climb 24.8% in Q3 of 2026, says A3](https://www.therobotreport.com/north-american-robot-orders-climb-24-8-q3-2026-says-a3/) — _The Robot Report_
- [What Symbotic’s Walmart growth teaches robotics startups about anchor customers](https://www.therobotreport.com/what-symbotic-growth-with-walmart-teaches-robotics-startups-about-anchor-customers/) — _The Robot Report_
- [ANYbotics begins delivering ANYmal X legged robot for explosive atmospheres](https://www.therobotreport.com/anybotics-begins-delivering-anymal-x-legged-robot-explosive-atmospheres/) — _The Robot Report_
- [Embotech and BMW move 1M vehicles with automated driving technology](https://www.therobotreport.com/embotech-bmw-move-1m-vehicles-automated-driving-technology/) — _The Robot Report_
- [Xpanner launches autonomous pile driver for solar farm contruction](https://www.therobotreport.com/xpanner-launches-new-autonomous-pile-driver-solar-farm-contruction/) — _The Robot Report_
- [Build specialized multimodal models with LFM3](https://huggingface.co/blog/LiquidAI/lfm3) — _Hugging Face - Blog_
- [Can we trust LLMs to judge whether a research idea is novel?](https://huggingface.co/blog/allenai/novelty-bench) — _Hugging Face - Blog_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
