# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-07-16 · **Tracked:** 572 core · 517 adjacent ·
260 news · **14230** benchmark rows across **5683** model
variants · **30** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **World Action Models for Robotics** | 588 | ➡️ steady | World models that predict future states and generate actions for robotic manipulation and navigation. |
| **Video Generation and World Simulation** | 208 | ➡️ steady | Generative video models as world simulators with control over dynamics, camera, and interaction. |
| **Vision-Language-Action Model Architecture** | 146 | ➡️ steady | Design and training of VLA models for robotic control, including action decoding, memory, and data efficiency. |
| **World Model Theory and Foundations** | 91 | ➡️ steady | Formal definitions, theoretical analyses, and structural foundations for world models. |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **8.23** | Flash-WAM: Modality-Aware Distillation for World Action Models | 2026-06-03 | spd 9 · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.05254) · [pdf](https://arxiv.org/pdf/2606.05254v1) |
| **7.79** | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models | 2026-06-24 | spd 8 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.25473) · [pdf](https://arxiv.org/pdf/2606.25473v1) · [code](https://github.com/NVlabs/rcm) |
| **7.73** | BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving | 2026-06-07 | spd 8 · gen 3 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2606.08684) · [pdf](https://arxiv.org/pdf/2606.08684v1) · [code](https://github.com/George-Ling3/BLUE) |
| **7.72** | Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model | 2026-07-13 | spd – · gen 7 · spec 8 · cost 2 | [abs](https://arxiv.org/abs/2607.11643) · [pdf](https://arxiv.org/pdf/2607.11643v1) |
| **7.71** | LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies | 2026-06-14 | spd 7 · gen 7 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15768) · [pdf](https://arxiv.org/pdf/2606.15768v1) |
| **7.67** | vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models | 2026-06-06 | spd 8 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.08094) · [pdf](https://arxiv.org/pdf/2606.08094v1) · [code](https://github.com/ggml-org/llama.cpp) |
| **7.67** | Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models | 2026-06-16 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.17846) · [pdf](https://arxiv.org/pdf/2606.17846v1) · [code](https://github.com/QwenLM/Qwen-RobotManip) |
| **7.66** | Cosmos 3: Omnimodal World Models for Physical AI | 2026-06-01 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02800) · [pdf](https://arxiv.org/pdf/2606.02800v1) · [code](https://github.com/nvidia/cosmos) |
| **7.66** | Multiplayer Interactive World Models with Representation Autoencoders | 2026-07-06 | spd 7 · gen 2 · spec 8 · cost 2 | [abs](https://arxiv.org/abs/2607.05352) · [pdf](https://arxiv.org/pdf/2607.05352v1) · [code](https://github.com/mira-wm/mira) |
| **7.61** | AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing | 2026-06-08 | spd 8 · gen 3 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.09811) · [pdf](https://arxiv.org/pdf/2606.09811v1) |
| **7.61** | GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation | 2026-06-07 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.08530) · [pdf](https://arxiv.org/pdf/2606.08530v1) · [code](https://github.com/babynabeauty/GEAR-VLA) |
| **7.58** | Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation | 2026-06-02 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.03784) · [pdf](https://arxiv.org/pdf/2606.03784v2) |
| **7.58** | FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation | 2026-06-18 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.20867) · [pdf](https://arxiv.org/pdf/2606.20867v1) |
| **7.57** | SANTS: A State-Adaptive Scheduler for World Action Models | 2026-05-27 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2605.27947) · [pdf](https://arxiv.org/pdf/2605.27947v1) |
| **7.57** | Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think | 2026-06-18 | spd 7 · gen 7 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.20246) · [pdf](https://arxiv.org/pdf/2606.20246v1) |
| **7.54** | Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference | 2026-07-14 | spd 8 · gen 4 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2607.12659) · [pdf](https://arxiv.org/pdf/2607.12659v1) · [code](https://github.com/PKU-SEC-Lab/Jetson-PI) |
| **7.53** | SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour | 2026-06-18 | spd – · gen 4 · spec 9 · cost – | [abs](https://arxiv.org/abs/2606.19928) · [pdf](https://arxiv.org/pdf/2606.19928v1) |
| **7.53** | Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies | 2026-07-10 | spd – · gen 7 · spec 8 · cost – | [abs](https://openreview.net/forum?id=h3hJmhiWJ7) · [pdf](https://openreview.net/pdf?id=h3hJmhiWJ7) |
| **7.52** | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis | 2026-06-04 | spd 8 · gen 7 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.05979) · [pdf](https://arxiv.org/pdf/2606.05979v1) · [code](https://github.com/SJTU-DENG-Lab/WLA) |
| **7.51** | FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation | 2026-06-11 | spd – · gen 8 · spec 6 · cost – | [abs](https://arxiv.org/abs/2606.13102) · [pdf](https://arxiv.org/pdf/2606.13102v1) |
| **7.49** | 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training | 2026-06-03 | spd – · gen 6 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.04436) · [pdf](https://arxiv.org/pdf/2606.04436v1) |
| **7.49** | $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation | 2026-06-11 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.13672) · [pdf](https://arxiv.org/pdf/2606.13672v1) · [code](https://github.com/mseitzer/pytorch-fid) |
| **7.48** | LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World | 2026-05-31 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458v1) |
| **7.47** | DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model | 2026-06-10 | spd 8 · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.12105) · [pdf](https://arxiv.org/pdf/2606.12105v1) |
| **7.46** | Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning | 2026-05-29 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.30795) · [pdf](https://arxiv.org/pdf/2605.30795v1) |
| **7.46** | Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments | 2026-05-28 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.30280) · [pdf](https://arxiv.org/pdf/2605.30280v2) · [code](https://github.com/QwenLM/Qwen-VLA) |
| **7.46** | Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance | 2026-05-22 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.24203) · [pdf](https://arxiv.org/pdf/2605.24203v1) |
| **7.46** | WALA Learning Executable Latent Actions from Action-Labeled Demonstrations and Action-Free Videos | 2026-07-13 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2607.11397) · [pdf](https://arxiv.org/pdf/2607.11397v1) |
| **7.45** | QPILOTS: Efficient Test-Time Q-Steering for Flow Policies | 2026-06-11 | spd – · gen 6 · spec 8 · cost 4 | [abs](https://arxiv.org/abs/2606.14801) · [pdf](https://arxiv.org/pdf/2606.14801v1) |
| **7.44** | VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies | 2026-05-28 | spd 8 · gen 7 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2605.30011) · [pdf](https://arxiv.org/pdf/2605.30011v1) · [code](https://github.com/DCDmllm/VisualThink-VLA) |
| **7.44** | Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination | 2026-06-08 | spd 8 · gen 5 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2606.10040) · [pdf](https://arxiv.org/pdf/2606.10040v1) |
| **7.44** | Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation | 2026-06-22 | spd 8 · gen 6 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.23090) · [pdf](https://arxiv.org/pdf/2606.23090v1) |
| **7.44** | ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies | 2026-06-30 | spd 8 · gen 4 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.31132) · [pdf](https://arxiv.org/pdf/2606.31132v1) |
| **7.44** | Learning 4D Geometric Priors for Inference-Efficient World Action Models | 2026-07-06 | spd 5 · gen 6 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2607.05468) · [pdf](https://arxiv.org/pdf/2607.05468v1) |
| **7.41** | Qantara: Bridge-Flow Training for Multi-Paradigm JEPA Control | 2026-07-06 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2607.04978) · [pdf](https://arxiv.org/pdf/2607.04978v1) |
| **7.39** | NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation | 2026-07-07 | spd 6 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2607.06678) · [pdf](https://arxiv.org/pdf/2607.06678v1) |
| **7.38** | Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation | 2026-06-01 | spd 5 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.02486) · [pdf](https://arxiv.org/pdf/2606.02486v1) |
| **7.38** | Wall-OSS-0.5 Technical Report | 2026-05-29 | spd – · gen 8 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.30877) · [pdf](https://arxiv.org/pdf/2605.30877v2) · [code](https://github.com/X-Square-Robot/wall-x) |
| **7.37** | EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies | 2026-06-18 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.20092) · [pdf](https://arxiv.org/pdf/2606.20092v1) |
| **7.36** | SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models | 2026-05-30 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.00664) · [pdf](https://arxiv.org/pdf/2606.00664v1) |
| **7.36** | ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? | 2026-06-17 | spd 7 · gen 6 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.19531) · [pdf](https://arxiv.org/pdf/2606.19531v1) · [code](https://github.com/yuyangalin/ImageWAM) |
| **7.35** | Colosseum V2: Benchmarking Generalization for Vision Language Action Models | 2026-05-26 | spd – · gen 8 · spec – · cost – | [abs](https://arxiv.org/abs/2605.27759) · [pdf](https://arxiv.org/pdf/2605.27759v1) |
| **7.35** | FlowWAM: Optical Flow as a Unified Action Representation for World Action Models | 2026-07-14 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2607.13017) · [pdf](https://arxiv.org/pdf/2607.13017v1) |
| **7.33** | DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World | 2026-06-10 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.11901) · [pdf](https://arxiv.org/pdf/2606.11901v1) · [code](https://github.com/isaac-sim/IsaacSim) |
| **7.33** | dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models | 2026-06-22 | spd – · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.23623) · [pdf](https://arxiv.org/pdf/2606.23623v1) |
| **7.33** | Long-term Traffic Simulation via Structured Autoregressive Modeling | 2026-06-30 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.31209) · [pdf](https://arxiv.org/pdf/2606.31209v1) |
| **7.33** | GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation | 2026-07-02 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2607.02642) · [pdf](https://arxiv.org/pdf/2607.02642v1) |
| **7.31** | CausalDrive: Real-time Causal World Models for Autonomous Driving | 2026-06-13 | spd 6 · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.15341) · [pdf](https://arxiv.org/pdf/2606.15341v1) |
| **7.31** | Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation | 2026-06-17 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2606.19194) · [pdf](https://arxiv.org/pdf/2606.19194v1) |
| **7.31** | RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation | 2026-07-07 | spd 8 · gen 6 · spec 6 · cost 4 | [abs](https://arxiv.org/abs/2607.06558) · [pdf](https://arxiv.org/pdf/2607.06558v1) · [code](https://github.com/alibaba-damo-academy/RynnWorld-Teleop) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _1645 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| KV baseline (growing cache) | — | inference state size at 100k steps | 25600000.0 | authors |
| OpenVLA-7B _(LIBERO)_ | — | I(X; X~) (attack channel capacity) | 5000.0 | authors |
| AURA-Mem | — | inference state size | 4224.0 | authors |
| Wan 2.2 (chunked) _(LIBERO-90)_ | — | FVD | 4177.0 | 3rd-party |
| SimpleVLA-RL _(LIBERO)_ | Long | iterations to 90% success rate | 2450.0 | authors |
| vla.cpp | — | peak RSS | 2031.0 | authors |
| vla.cpp | — | VRAM usage | 1312.0 | authors |
| CoT-VLA | — | Mean Latency | 892.0 | 3rd-party |
| ConfidenceVLA | — | avg inference time | 712.9 | 3rd-party |
| Agentic-VLA _(LIBERO)_ | Long | iterations to 90% success rate | 700.0 | authors |

#### CALVIN  ·  _108 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 99.5 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (1 task) | 99.3 | authors |
| MPCoT _(LIBERO, CALVIN ABC→D)_ | — | 3-step success rate | 96.8 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (2 tasks) | 96.6 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (2 tasks) | 95.9 | authors |
| SAPS (Cosine) _(CALVIN)_ | long-horizon chains (5 subtasks) | subtask success rate (ST-SR) | 94.85 | authors |
| VLM4VLA + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 94.4 | authors |
| MPCoT _(LIBERO, CALVIN ABC→D)_ | — | 4-step success rate | 93.7 | authors |
| VLM4VLA _(CALVIN ABC)_ | — | success rate (1 task) | 93.4 | authors |
| SAPS (Cosine) _(CALVIN)_ | 11 single subtasks | average success rate | 93.0 | authors |

#### RoboTwin  ·  _365 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LingBot-VA | — | per-chunk latency | 8100.0 | authors |
| WAM4D _(RoboTwin 2.0)_ | — | inference latency | 525.43 | authors |
| Fast-WAM _(RoboTwin 2.0)_ | — | inference latency | 425.53 | 3rd-party |
| Flash-WAM _(LingBot-VA)_ | — | per-chunk latency | 348.0 | authors |
| HALO-WA _(online task-specific)_ | Beat Block Hammer | episode length | 213.7 | authors |
| IRASim _(RoboTwin 2.0)_ | Overall | FVD | 126.2 | authors |
| HY-VLA | place_empty_cup | success rate | 100.0 | authors |
| π0.5 _(RoboTwin2.0)_ | Grab Roller | success rate | 98.6 | authors |
| Ours _(RoboTwin 2.0 demonstration data (50 per task, easy setting))_ | S3 (Lift Pot) | success rate | 97.0 | authors |
| HALO-WA _(online task-specific)_ | Click Bell | success rate | 97.0 | authors |

#### SimplerEnv  ·  _172 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GeoAlign _(robot-domain RGB-D + Dpol (SimplerEnv-Fractal demonstrations))_ | Pick Coke Can | success rate | 100.0 | authors |
| S2-VLA | Eggplant in Basket | success rate | 100.0 | authors |
| OpenVLA-7b | Pick up | failure rate (FR) | 97.5 | authors |
| GR00T-N1.6 | Pick up | failed object coverage (FOC) | 97.1 | authors |
| Afford-VLA _(LIBERO + Affordance dataset)_ | Put Eggplant | Success rate | 96.8 | authors |
| Reflective VLA _(π0.5 training data)_ | Spoon | success rate | 95.8 | authors |
| Embodied-R1.5-VLA | — | success rate | 92.4 | authors |
| TBD-VLA _(Fractal)_ | Visual Matching | success rate | 91.0 | authors |
| GeoAlign _(robot-domain RGB-D + Dpol (SimplerEnv-Fractal demonstrations))_ | — | unweighted average success rate | 85.3 | authors |
| EO-1 | Pick up | trajectory coverage (TC) | 84.0 | authors |

#### RLBench  ·  _46 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PointACT _(RLBench (10 tasks))_ | Close laptop lid | success rate | 99.0 | authors |
| EO1 (reproduced) _(RLBench (10 tasks))_ | Mean | success rate | 73.2 | 3rd-party |
| GR00T(arch) + Point _(LIBERO-Spatial / RLBench-10Tasks)_ | Mean | success rate | 69.7 | authors |
| GR00T(arch) + Point (final layer) _(RLBench-10Tasks)_ | Mean | success rate | 69.7 | authors |
| GR00T(arch) + Point (multi-scale, K=128) _(RLBench-10Tasks)_ | Mean | success rate | 65.6 | authors |
| GR00T(arch) + Point (multi-scale, K=64) _(RLBench-10Tasks)_ | Mean | success rate | 65.2 | authors |
| π0 + CamVLA | Mean | success rate | 51.4 | authors |
| GR00T(arch) _(LIBERO-Spatial / RLBench-10Tasks)_ | Mean | success rate | 50.8 | authors |
| HARP-SRPD | — | average success rate | 46.59 | authors |
| HARP-SR | 18 tasks | average success rate | 43.41 | authors |

#### Meta-World  ·  _55 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | push | return | 1641.0 | authors |
| VICX _(Meta-World (drawer-open, reach, basketball))_ | coffee-button | success rate | 100.0 | authors |
| SUREFlow _(LIBERO, Meta-World, LIBERO-PRO)_ | Easy | Success Rate | 97.8 | authors |
| FabriVLA _(Evo-1 Meta-World demonstration dataset)_ | easy | success rate | 95.0 | authors |
| FabriVLA _(Evo-1 Meta-World demonstration dataset)_ | — | overall episode-level success rate | 92.0 | authors |
| FabriVLA _(Evo-1 Meta-World demonstration dataset)_ | — | tier-average success rate | 90.0 | authors |
| SUREFlow _(LIBERO, Meta-World, LIBERO-PRO)_ | — | Average Success Rate | 88.32 | authors |
| LA4VLA-1B _(LA4-33K + LA-33K-V (MixPT))_ | — | success rate | 87.53 | authors |
| LA4VLA | — | tier-average success rate | 87.5 | 3rd-party |
| Evo-Depth | — | tier-average success rate | 84.4 | 3rd-party |

#### ManiSkill  ·  _56 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.99)_ | lift-cube | return | 175.0 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | pick-cube | return | 147.0 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 98.68 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 97.44 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 95.78 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 93.14 | authors |
| π0.5 | — | success rate | 89.8 | authors |
| FORCE (π0) _(ManiSkill (offline + online))_ | — | success rate | 86.9 | authors |
| OpenVLA-OFT + Feat2Go | — | success rate | 82.9 | authors |
| FORCE (Octo) _(ManiSkill (offline + online))_ | — | success rate | 82.3 | authors |

#### RoboCasa  ·  _156 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Cosmos-Policy | Turn Off Microwave | success rate | 100.0 | authors |
| Z-1 RL _(RoboCasa demonstrations)_ | Door | success rate | 97.0 | authors |
| Z-1 SFT _(RoboCasa demonstrations)_ | Door | success rate | 93.2 | authors |
| X-WAM | — | success rate | 79.2 | 3rd-party |
| WALA _(RoboCasa-GR1-Tabletop)_ | — | average success rate | 75.2 | authors |
| ACE-EGO-0 _(Mixed robot demonstrations and egocentric human videos (6.0K+ hours))_ | — | average success | 72.8 | authors |
| GR00T-N1.5 _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.7 | authors |
| Late Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.0 | authors |
| DIAL _(RoboCasa-GR1-Tabletop)_ | — | average success rate | 70.2 | 3rd-party |
| Early Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 69.7 | authors |

#### Open-X / RT  ·  _50 results_

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

#### ALFWorld  ·  _15 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GIGPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 90.4 | authors |
| GRPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 77.9 | authors |
| Expel | — | Success Rate | 60.1 | 3rd-party |
| OCM | — | Success Rate | 41.7 | authors |
| AWM | — | Success Rate | 37.3 | 3rd-party |
| OCM | — | Steps | 34.5 | authors |
| Reflexion | — | Success Rate | 30.6 | 3rd-party |
| ReAct | — | Success Rate | 29.9 | 3rd-party |
| Wall-E | — | Success Rate | 27.6 | 3rd-party |
| WorldCoder | — | Success Rate | 25.4 | 3rd-party |

#### VBench  ·  _790 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| HunyuanVideo (no caching) | 33 prompts from VBench | Latency | 1359.0 | authors |
| Wan-I2V | Cut & Drag | Flow-Err | 181.1 | 3rd-party |
| GWTF | Cut & Drag | Flow-Err | 152.81 | 3rd-party |
| PTQ4DiT | — | FVD-FP | 124.2 | authors |
| Q-ARVD | — | FVD-FP | 116.26 | authors |
| Wan-T2V | T2V Motion Transfer | Flow-Err | 103.26 | 3rd-party |
| TTM | Cut & Drag | Flow-Err | 102.39 | 3rd-party |
| ϕ-Noise | Cut & Drag | Flow-Err | 101.49 | authors |
| LongLive (Vanilla) | — | KV Cache | 100.0 | authors |
| Reward (Vanilla) | — | KV Cache | 100.0 | authors |

#### AgiBot / GENIE  ·  _33 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Egocentric (ours) _(HumanNet (egocentric portion, 5000h subset))_ | Seen tasks (in-distribution) | success rate | 92.5 | authors |
| Reward as an Agent | — | Overall Accuracy | 91.0 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | Scene Consistency | 90.41 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | EWMScore | 82.45 | authors |
| Wan2.2 (no pretraining) | Seen tasks (in-distribution) | success rate | 40.0 | authors |
| DreamDojo (14B) | target-action transfer do(ut=utar) | FDCE | 24.82 | 3rd-party |
| DreamDojo (2B) | target-action transfer do(ut=utar) | FDCE | 24.36 | 3rd-party |
| CD-LAM (2B) _(EgoDex (100h), AgiBot)_ | target-action transfer do(ut=utar) | FDCE | 22.55 | authors |
| CD-LAM (14B) _(EgoDex (100h), AgiBot)_ | target-action transfer do(ut=utar) | FDCE | 21.11 | authors |
| ViPSim(DiT) _(AgiBotWorld-Beta)_ | — | PSNR | 20.35 | authors |

#### Habitat  ·  _19 results_

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

#### BEHAVIOR  ·  _48 results_

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

#### nuScenes  ·  _221 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SparseWorld-S _(nuScenes)_ | Inference memory | Inference Memory (IM) | 4397.0 | authors |
| DriveGAN | video generation | FVD | 502.3 | 3rd-party |
| DriveDreamer | video generation | FVD | 452.0 | 3rd-party |
| Direct Regression (AnchoredVAEDiT) | future frame prediction | FID | 370.8 | authors |
| Vanilla Flow _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 304.1 | 3rd-party |
| REPA w/ DINOv2 _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 295.9 | 3rd-party |
| Self-Flow _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 283.3 | 3rd-party |
| ReWorld _(nuScenes (from scratch))_ | video generation (from scratch) | FVD | 270.4 | authors |
| Diffusion (calibrated) - AnchoredVAEDiT | future frame prediction | FID | 162.5 | authors |
| DrivingGPT | video generation | FVD | 142.6 | 3rd-party |

#### SafeSora  ·  _99 results_

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

#### Open-Domain S2V  ·  _99 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| DomainShuttle (Wan2.2-14B) _(200K image-personalization dataset + 750K video-personalization dataset (Phantom-Data, OpenS2V, Ditto-1M))_ | Overall | MS | 0.987 | authors |
| VACE-Wan2.1-14B | Overall | MS | 0.985 | 3rd-party |
| HuMo | Overall | MS | 0.981 | 3rd-party |
| DomainShuttle (Wan2.1-14B) _(200K image-personalization dataset + 750K video-personalization dataset (Phantom-Data, OpenS2V, Ditto-1M))_ | Overall | MS | 0.977 | authors |
| VACE-Wan2.2-14B | Overall | MS | 0.974 | 3rd-party |
| Phantom | Overall | MS | 0.972 | 3rd-party |
| Kling 1.6 | Overall | MS | 0.965 | 3rd-party |
| MAGREF | Overall | MS | 0.964 | 3rd-party |
| BindWeave | Overall | MS | 0.963 | 3rd-party |
| FFGO-Wan2.2-14B | Overall | MS | 0.945 | 3rd-party |

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

#### Bench2Drive  ·  _88 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| BLUE _(SimLingo training set (~400 routes))_ | — | latency | 549.5 | authors |
| CLEAR (InternVL3-1B) _(SimLingo dataset (~3.1M samples))_ | — | Efficiency | 275.4 | authors |
| VLGA _(Bench2Drive train routes)_ | — | Efficiency | 194.63 | authors |
| LinkVLA _(PDM-Lite)_ | — | Driving Score | 91.01 | 3rd-party |
| BLUE _(SimLingo training set (~400 routes))_ | — | driving score | 90.58 | authors |
| BLUE (CriticVLA) _(CriticVLA training set)_ | — | driving score | 90.37 | authors |
| AnchorVLA _(PDM-Lite)_ | — | Driving Score | 89.92 | authors |
| TakeVLA _(PDM-Lite)_ | — | driving score | 89.72 | 3rd-party |
| PersonaDrive | — | Driving Score | 88.95 | authors |
| BevAD _(PDM-Lite)_ | — | driving score | 88.11 | 3rd-party |

#### NAVSIM  ·  _86 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ours† _(OpenScene (NAVSIM train split))_ | planning | Comf. | 100.0 | authors |
| WCog-VLA-2B _(NAVSIM + 158k open-source driving VQA samples + 170k NAVSIM-tailored samples (85k trajectory-specific VQA + 85k Game-CoT))_ | — | NC (no at-fault collision) | 99.4 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | NC | 98.7 | authors |
| SafeAlign-VLA _(NAVSIM navtrain)_ | trajectory planning | NC | 98.6 | authors |
| WCog-VLA-2B _(NAVSIM + 158k open-source driving VQA samples + 170k NAVSIM-tailored samples (85k trajectory-specific VQA + 85k Game-CoT))_ | — | TTC (time-to-collision) | 98.5 | authors |
| S2-VLA _(ReCogDrive VQA + NAVSIM)_ | — | NC | 98.4 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | DAC | 98.2 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | TTC | 95.9 | authors |
| ForgeDrive _(NAVSIM/nuPlan)_ | — | Driving Command Accuracy | 94.7 | authors |
| RAP _(NAVSIM trainval)_ | — | PDMS | 93.8 | 3rd-party |

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

#### DAVIS  ·  _63 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ours VAE _(in-house synthetic dataset)_ | reconstruction | VBench Total | 82.93 | authors |
| LightX2V VAE | reconstruction | VBench Total | 82.44 | authors |
| TrajectoryCrafter | 10 ReCamMaster camera trajectory types | RotErr | 10.434 | 3rd-party |
| CogNVS | 10 ReCamMaster camera trajectory types | RotErr | 6.9499 | 3rd-party |
| Recammaster _(synthetic (Unreal Engine))_ | 10 ReCamMaster camera trajectory types | RotErr | 2.3175 | 3rd-party |
| Redirector _(synthetic)_ | 10 ReCamMaster camera trajectory types, speed=2.0 | RotErr | 1.9246 | 3rd-party |
| Ours _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types, speed=2.0 | RotErr | 1.8821 | authors |
| MVTrack4Gen ReCamMaster _(Kubric + MultiCamVideo)_ | — | mRotErr | 1.858 | authors |
| MVTrack4Gen Redirector _(Kubric + MultiCamVideo)_ | — | mRotErr | 1.718 | authors |
| Full reward (Geo-Align) _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types | RotErr | 1.3895 | authors |

#### OGBench  ·  _62 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| CoFi | PointMaze-Giant | success rate | 96.0 | authors |
| QPILOTS-M _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 90.0 | authors |
| QPILOTS-U _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 89.0 | authors |
| QAM-E _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 85.0 | 3rd-party |
| CDGS | AntMaze-Giant | success rate | 84.0 | 3rd-party |
| FQL _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 82.0 | 3rd-party |
| FEdit _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 79.0 | 3rd-party |
| QAM _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 70.0 | 3rd-party |
| CD | PointMaze-Giant | success rate | 68.0 | 3rd-party |
| CGQL _(OGBench dataset)_ | all 50 tasks | aggregate success rate (offline → online) | 67.0 | 3rd-party |

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

#### PushT  ·  _54 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LeWM + AITS | — | success rate | 100.0 | authors |
| FF-JEPA (DM) _(PushT filtered successful demonstrations)_ | Short-horizon (t=25) | success rate | 96.09 | authors |
| LeWM | — | success rate | 96.0 | authors |
| Le-WM | — | success rate | 96.0 | authors |
| LeWM _(PushT)_ | Short-horizon (t=25) | success rate | 94.53 | authors |
| VLWM _(expert episodes (PushT, OGBench-Cube, TwoRoom))_ | goal offset 25 | success rate | 94.0 | authors |
| AdaJEPA (WM w/ Temporal Straightening spatial) _(PushT)_ | goal-reaching | success rate | 92.0 | authors |
| Frozen (WM w/ Temporal Straightening spatial) _(PushT)_ | goal-reaching | success rate | 91.3 | authors |
| LeWM _(expert episodes (PushT, OGBench-Cube, TwoRoom))_ | goal offset 25 | success rate | 90.0 | 3rd-party |
| DINO (Hierarchy) | Short-horizon (t=25) | success rate | 89.0 | 3rd-party |

#### HDTF  ·  _51 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| FantasyTalking | — | FID | 16.488 | 3rd-party |
| Hallo3 | — | FID | 14.656 | 3rd-party |
| Sonic | — | FID | 13.242 | 3rd-party |
| ReFree-S2V (w/o RL) _(Hallo3, CelebV-HQ, Seamless Interaction)_ | — | FID | 12.319 | authors |
| ReFree-S2V _(Hallo3, CelebV-HQ, Seamless Interaction)_ | — | FID | 11.643 | authors |
| StableAvatar-1.3B | — | Sync-D | 11.18 | 3rd-party |
| FantasyTalking | — | Sync-D | 11.072 | 3rd-party |
| OmniAvatar | — | Sync-D | 9.242 | 3rd-party |
| Hallo3 | — | Sync-D | 9.181 | 3rd-party |
| LiveAvatar | — | Sync-D | 8.447 | 3rd-party |

## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
- **ActionMap: Robot Policy Learning via Voxel Action Heatmap** — ActionMap replaces the unstructured single-point action decoder in VLA models with a voxel heatmap action head that predicts a probability distribution over a discretized 3D action space, explicitly exploiting the geometric proximity of neighboring actions rather than treating the action space as unstructured… _(→ WAM: In World Action Models, the action conditioning mechanism is critical for predicting how actions transform world states. The voxel heatmap representation can transfer in two ways: (1) as a structured action encoding input to the world model—replacing flat…)_ [abs](https://arxiv.org/abs/2606.06904) · [pdf](https://arxiv.org/pdf/2606.06904v1) · [code](https://github.com/showlab/ActionMap)
- **Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs** — ST-Merge is a plug-and-play, training-free spatio-temporal visual token merging framework that reduces inference latency by fusing redundant visual tokens during the visual encoding phase. It constructs 3D spatiotemporal coordinates for multi-queue parallel matching and weighted aggregation across frames, and… _(→ WAM: World Action Models must process long video histories to predict future world states and generate actions, making visual token count a critical computational bottleneck. ST-Merge's spatio-temporal token merging could be directly applied to the visual encoder…)_ [abs](https://arxiv.org/abs/2606.29350) · [pdf](https://arxiv.org/pdf/2606.29350v1) · [code](https://github.com/Junzhou-Chen/ST_Merge)
- **WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models** — A multi-dimensional, long-horizon evaluation framework for interactive world models that introduces novel metrics: per-frame action metrics to bypass semantic scale disparity, segment-based drift metrics to capture mid-sequence visual collapse, controllability-gated physics evaluation to isolate physical plausibility… _(→ WAM: World Action Models (WAMs) inherently suffer from compounding errors over long horizons, leading to visual drift, physical inconsistencies, and memory loss. The benchmark's metrics—particularly the controllability-gated physics evaluation and action-decoupled…)_ [abs](https://arxiv.org/abs/2606.31672) · [pdf](https://arxiv.org/pdf/2606.31672v1)
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
- **WireCraft: A Simulation Benchmark for Industrial DLO Manipulation** — A modular simulation benchmark for industrial Deformable Linear Object (DLO) manipulation featuring dual physics models (articulated and deformable), configurable task families (connector insertion, clip routing, channel seating), and standardized evaluation protocols bridging simulation and real-world data. _(→ WAM: World Action Models must predict future states given actions, but currently lack benchmarks for complex, infinite-dimensional deformable dynamics. WireCraft provides the exact training data and evaluation protocols needed to develop WAMs capable of modeling…)_ [abs](https://arxiv.org/abs/2606.18097) · [pdf](https://arxiv.org/pdf/2606.18097v1) · [code](https://github.com/isaac-sim/IsaacSim)
- **ROBOSHACKLES: A Safety Dataset for Human-Injury Prevention in Embodied Foundation Models** — A scalable pipeline for constructing safety-critical robotic video data without real-world harm: starting from real robot observations (DROID), applying hazard-aware image editing to inject dangerous states, generating temporal prompts specifying expected scene evolution, and using a video generation model (Wan2.7) to… _(→ WAM: World Action Models must predict future world states conditioned on actions, making safety-critical anticipation essential. The hazard-aware editing + temporal-prompt + rollout-synthesis pipeline can be directly repurposed to generate safety-critical training…)_ [abs](https://arxiv.org/abs/2606.18632) · [pdf](https://arxiv.org/pdf/2606.18632v1)
- **Current World Models Lack a Persistent State Core** — Current world models lack a persistent state core—an internal world state that continuously evolves over time, decoupled from observation. When the camera looks away and returns, models simply resume the scene from the state at which it was last observed rather than advancing the event during the unobserved period… _(→ WAM: A World Action Model must predict the consequences of actions over time, including delayed and indirect effects. Without a persistent state core, a WAM cannot reason about what happens to objects or events when they leave the agent's observation—yet…)_ [abs](https://arxiv.org/abs/2606.20545) · [pdf](https://arxiv.org/pdf/2606.20545v1) · [code](https://github.com/JinPLu/WRBench)
- **Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models** — Mix-QVLA introduces task-evidence-aware mixed-precision quantization that computes gradient-weighted task-evidence maps from VLA functional boundary activations, measures both evidence-mass and attribution-distribution distortion between full-precision and quantized models, and critically models sensitivity as… _(→ WAM: World Action Models share VLA's need for efficient deployment and exhibit similar phase-dependent processing (e.g., world state encoding vs. action-conditioned prediction vs. planning/rollout). The time-aware sensitivity insight transfers directly: different…)_ [abs](https://arxiv.org/abs/2606.19565) · [pdf](https://arxiv.org/pdf/2606.19565v1)
- **GEOPHYS: The Geometry of Physical Plausibility** — Physical plausibility in videos can be detected by analyzing the emergent geometric properties of temporal embeddings from frozen image encoders, providing a highly efficient, training-free alternative to expensive LLM judges or specialized video models. _(→ WAM: WAMs require generating physically plausible future states. GEOPHYS can be used as a lightweight, training-free verifier to filter WAM rollouts (best-of-N sampling) at a fraction of the compute/memory cost of large world model verifiers. Additionally, these…)_ [abs](https://arxiv.org/abs/2606.20707) · [pdf](https://arxiv.org/pdf/2606.20707v1) · [code](https://github.com/ChristianInterno/GeoPhys)
- **Improving Vision-Language-Action Model Fine-Tuning with Structured Stage and Keyframe Supervision** — StaKe introduces plug-in auxiliary supervision for VLA fine-tuning by automatically deriving two complementary signals from demonstration gripper states (without manual annotation): a stage classifier identifying the current manipulation stage, and a keyframe predictor estimating the target joint action at the next… _(→ WAM: World Action Models must predict future world states conditioned on actions, and they struggle most at critical transition boundaries (e.g., contact, grasp, release) where prediction errors compound over long horizons. StaKe's structured supervision transfers…)_ [abs](https://arxiv.org/abs/2606.26801) · [pdf](https://arxiv.org/pdf/2606.26801v1)
- **From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond** — LLMs are a degenerate special case of world models (state space = token sequences, action = append token), and there exists a continuous spectrum from next-token prediction to JEPA-style latent world models, with identifiable intermediate stations—multi-token prediction, future-summary prediction, and next-latent… _(→ WAM: WAMs can explicitly position themselves on this spectrum rather than treating token prediction and world simulation as incompatible paradigms. The intermediate stations offer concrete architectural and objective choices for WAM design: multi-token prediction…)_ [abs](https://arxiv.org/abs/2606.28127) · [pdf](https://arxiv.org/pdf/2606.28127v1)
- **Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?** — The paper introduces Drop-Then-Recovery (DTR), a protocol for measuring architectural redundancy in VLA models by removing transformer blocks and fine-tuning to assess recoverability, along with GateProbe, a one-shot virtual-gate sensitivity metric that ranks blocks by their contribution to the downstream action loss… _(→ WAM: World Action Models similarly integrate language, vision, and action components for predicting action consequences and generating actions. The DTR protocol and GateProbe metric can be directly applied to identify which components of a WAM are redundant versus…)_ [abs](https://arxiv.org/abs/2606.27755) · [pdf](https://arxiv.org/pdf/2606.27755v1) · [code](https://github.com/s1ghhh/VLADrop)
- **The Speedup Paradox: Rethinking Inference Speed-Quality Trade-off in Embodied Tasks** — TISED (Task-level Inference Speedup Effect Decomposition), an analytical framework that decomposes how lossy inference optimizations (quantization, pruning, asynchronous inference) affect closed-loop embodied task performance, revealing paradoxical effects: (1) on static tasks, per-step speedup can increase total task… _(→ WAM: World Action Models operate in closed-loop settings where predicted world states feed back into action selection, making them subject to the same speedup paradox. TISED's decomposition directly applies: moderate quantization or pruning of a WAM's world…)_ [abs](https://arxiv.org/abs/2606.28529) · [pdf](https://arxiv.org/pdf/2606.28529v1)
- **Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning** — Decomposing VLA policies into semantic mapping and physical action decision components, and proposing evaluation designs with controlled variation that causally disentangle whether performance gains stem from semantic matching/distributional overlap versus genuine physical generalization — without requiring access to… _(→ WAM: World Action Models face the identical identifiability problem: when a WAM predicts future world states and actions accurately, it is unclear whether this reflects learned physical dynamics (genuine world modeling) or semantic pattern matching from…)_ [abs](https://arxiv.org/abs/2606.30686) · [pdf](https://arxiv.org/pdf/2606.30686v1)
- **RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation** — Step Forcing: A technique for autoregressive video world models that combines anchored (ground-truth) contexts with one-step self-forwarded (model-predicted) contexts during rollouts to reduce train-test mismatch (exposure bias) and error accumulation, while preserving action-observation dynamics. _(→ WAM: World Action Models suffer heavily from compounding errors during long-horizon, action-conditioned autoregressive rollouts, which causes state drift and out-of-distribution failures. By adopting Step Forcing, WAMs can mitigate this exposure bias by…)_ [abs](https://arxiv.org/abs/2607.01060) · [pdf](https://arxiv.org/pdf/2607.01060v1)
- **Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies** — A real-time, segmentation-based visual grounding method that overlays semantic traversability information onto input observations—green for traversable, red for non-traversable—using SegFormer, serving as a lightweight input preprocessing step that requires no model retraining and acts primarily as a trajectory length… _(→ WAM: World Action Models predict future world states conditioned on actions, and they can suffer from generating physically implausible predictions (e.g., agents moving through obstacles). The segmentation-based visual grounding overlay can be directly applied as…)_ [abs](https://arxiv.org/abs/2607.05122) · [pdf](https://arxiv.org/pdf/2607.05122v1)
- **VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models** — Treating language as an optimizable variable for frozen Vision-Language-Action (VLA) models by training a separate language-conditioning space policy using reinforcement learning. This policy translates human instructions into VLA-grounded commands (incorporating object appearance, spatial relations, and… _(→ WAM: World Action Models (WAMs) similarly rely on conditioning inputs (like language goals or action tokens) to generate future states or action trajectories. Transferring this concept, one could optimize the input conditioning space (language prompts or latent…)_ [abs](https://arxiv.org/abs/2607.04517) · [pdf](https://arxiv.org/pdf/2607.04517v1)

## 👥 Influential Authors & Groups
- **[Xiaofeng Wang](https://www.semanticscholar.org/author/2242976725)** (7 papers) — Xiaofeng Wang's research focuses on embodied world models and unified action-motion representations for robotic control, including visual navigation, manipulation, and aerial embodied question answering. Key contributions include redefining actions as visual…
- **[Yao Mu](https://www.semanticscholar.org/author/2348161293)** (7 papers) — Research focuses on advancing visuomotor and world action models for robotic manipulation, including reinforcement learning with human interventions, open-source VLA systems for bimanual dexterity, equilibrium matching for closed-loop control, compositional…
- **[Xiaozhu Ju](https://www.semanticscholar.org/author/2392718853)** (6 papers) — Xiaozhu Ju's research focuses on developing world models and embodied agents with persistent internal states, manifold-aware cross-modal alignment, hybrid kinematic-physical dynamics, and safe reinforcement learning for vision-language-action policies, aiming…
- **[Jingjing Gong](https://www.semanticscholar.org/author/2371292918)** (6 papers) — Jingjing Gong's research focuses on improving vision-language-action (VLA) models for robotic control, particularly through hierarchical planning, robust action generation under sensor variability, efficient one-step action generation, task-agnostic…
- **[A. T. Le](https://www.semanticscholar.org/author/2282564821)** (6 papers) — A. T. Le's research focuses on improving Vision-Language-Action (VLA) models for robotic manipulation, including developing efficient inference runtimes, reducing model redundancy, incorporating equivariant inductive biases, enhancing robustness, and enabling…
- **[D. M. H. Nguyen](https://www.semanticscholar.org/author/2374196339)** (6 papers) — Research focuses on improving efficiency, robustness, and data efficiency of Vision-Language-Action (VLA) models for robot manipulation, including evaluation frameworks, inference runtimes, equivariant models, and few-shot adaptation.
- **[Xiaowei Chi](https://www.semanticscholar.org/author/2192825554)** (6 papers) — Xiaowei Chi's research focuses on developing World-Action Models (WAMs) that integrate world modeling and action prediction for robotic manipulation, with contributions in reinforcement learning, 4D geometry, tactile sensing, and safe RL.
- **[Shanghang Zhang](https://www.semanticscholar.org/author/2346116279)** (6 papers) — Shanghang Zhang's research focuses on developing world-action models (WAMs) and reinforcement learning frameworks for robotic manipulation, including manifold-aware cross-modal alignment, value-augmented rollback, interactive world models integrating…
- **[Andrea V. Bajcsy](https://www.semanticscholar.org/author/47370841)** (5 papers) — Andrea V. Bajcsy's research focuses on improving the robustness, efficiency, and safety of robot policies through world models and inference-time steering. Key directions include using diffusion-based video world models for policy evaluation and improvement…
- **[Xintao Wang](https://www.semanticscholar.org/author/2305033532)** (5 papers) — Research focuses on egocentric video generation and world models, with emphasis on disentangled camera and hand control, long-horizon consistency via decoupled memory architectures, and geometry-aware implicit memory for 3D scene understanding.
- **[Yann LeCun](https://www.semanticscholar.org/author/2270469816)** (5 papers) — Yann LeCun's WAM research centers on the Joint Embedding Predictive Architecture (JEPA) for learning latent world models. His work spans theoretical foundations (LeJEPA), open-source platforms (stable-worldmodel), and applications in robotics, including…
- **[Xuelong Li](https://www.semanticscholar.org/author/2336880377)** (5 papers) — Xuelong Li's research focuses on video generation with geometric consistency, photorealistic insertion, physics-grounded scene generation, real-time avatar interaction, and compositional human-camera control.
- **[Enze Xie](https://www.semanticscholar.org/author/41020000)** (5 papers) — Enze Xie's research focuses on accelerating video generation and inference through training-free adaptive computation and agent-based frameworks, enhancing physical consistency in video world models for robotic manipulation, and leveraging filtered egocentric…
- **[Zheng Zhu](https://www.semanticscholar.org/author/2265968976)** (5 papers) — Research focuses on embodied world models, including translating actions into visual representations, sparse keyframe interpolation for efficiency, unified latent world-action modeling for navigation, and training-free acceleration of video generation. The…
- **[Hangjun Ye](https://www.semanticscholar.org/author/2384401186)** (5 papers) — Hangjun Ye's research focuses on unified world-action modeling for embodied AI, including autonomous driving and vision-and-language navigation, by integrating vision, language, and action tokens with diffusion-based generation and latent scene prediction.
- **[Junke Wang](https://www.semanticscholar.org/author/2124919221)** (5 papers · Fudan University) — Junke Wang's research focuses on world action modeling, video-action pretraining, and autoregressive generation for robotics and image synthesis, with an emphasis on discrete tokenization, causal reasoning, and few-shot generalization in manipulation tasks.
- **[Nan Duan](https://www.semanticscholar.org/author/2360369479)** (5 papers) — Nan Duan's research focuses on advancing world models and generative AI through memory mechanisms, simulation-enabled data interconversion, and efficient streaming video generation, with applications in embodied AI and real-time high-resolution video…
- **[Fan Feng](https://www.semanticscholar.org/author/2293287494)** (5 papers) — Fan Feng's research focuses on constructing task-sufficient world models for embodied agents, combining structured latent space learning, agentic exploration, and causal debiasing to improve sample efficiency, generalization, and real-time inference in…
- **[Hangjun Ye](https://www.semanticscholar.org/author/2367554550)** (5 papers) — Hangjun Ye's research focuses on developing world action models (WAMs) that unify perception, prediction, and action generation for embodied agents, with applications in navigation and autonomous driving. Key contributions include spatial-perceiving models…
- **[Xinyuan Song](https://www.semanticscholar.org/author/2384121658)** (5 papers) — Xinyuan Song's research focuses on improving world models for long-horizon language agents, addressing issues like hallucination propagation, rollout error, and world-model collapse through techniques such as grounded iterative planning, error-aware…
- **[Z. Cai](https://www.semanticscholar.org/author/48569716)** (5 papers) — Research on world models for language agents, focusing on reducing hallucination propagation, understanding and mitigating rollout error, analyzing world-model collapse as a phase transition, and developing budgeted environment probing and stable correction…
- **[Yujun Shen](https://www.semanticscholar.org/author/2392945842)** (5 papers) — Research on video-action pretraining for robot control, causal world modeling with multi-chunk prediction, controllable world simulators with dynamic memory, infinite interactive world models, and mixture-of-experts video pretraining for embodied intelligence.
- **[Haoqi Yuan](https://www.semanticscholar.org/author/1429192914)** (5 papers) — Haoqi Yuan's research focuses on developing unified foundation models for embodied AI, particularly vision-language-action (VLA) models, tactile pre-training, and world models, with an emphasis on cross-embodiment generalization and scaling with heterogeneous…
- **[Peidong Jia](https://www.semanticscholar.org/author/101105478)** (5 papers) — Peidong Jia's research focuses on world action models (WAM) for robotic manipulation, emphasizing manifold-aware cross-modal alignment, integration of analytical kinematic priors with learned dynamics, unified vision-tactile modeling, world-ego decomposition…
- **[Yinghao Xu](https://www.semanticscholar.org/author/121983635)** (5 papers) — Yinghao Xu's research focuses on world action modeling (WAM) for embodied intelligence, including video-action pretraining, causal world modeling with multi-chunk prediction, and developing scalable world models with mixture-of-experts and semantic…

## 📰 Embodied / Physical-AI News
- [Xpanner rolls out X1 Panel Lift for automated solar panel installation](https://www.therobotreport.com/xpanner-rolls-out-x1-panel-lift-automated-solar-panel-installation/) — _The Robot Report_
- [Lockheed Martin taps Machina’s robots for mission-critical missile parts](https://www.therobotreport.com/lockheed-martin-taps-machinas-robots-for-mission-critical-missile-parts/) — _The Robot Report_
- [Newer Models, Same Advantage](https://huggingface.co/blog/Dharma-AI/newer-models-same-advantages) — _Hugging Face - Blog_
- [Security incident disclosure — July 2026](https://huggingface.co/blog/security-incident-july-2026) — _Hugging Face - Blog_
- [Introducing Real World VoiceEQ: Measuring the human quality of voice AI](https://huggingface.co/blog/real-world-voiceeq) — _Hugging Face - Blog_
- [Walden Robotics launches at $1.1B valuation for general-purpose robots](https://www.therobotreport.com/walden-robotics-launches-1-1b-valuation-general-purpose-robots/) — _The Robot Report_
- [Agility outlines six recommendations for U.S. humanoid robot policies](https://www.therobotreport.com/agility-outlines-six-recommendations-for-u-s-humanoid-robot-policies/) — _The Robot Report_
- [Vicarious Surgical board seeks to dissolve company](https://www.therobotreport.com/vicarious-surgical-board-seeks-to-dissolve-company/) — _The Robot Report_
- [Icarus Robotics uses KULR technology to power JOY free-flying space robot](https://www.therobotreport.com/icarus-robotics-uses-kulr-technology-to-power-joy-free-flying-space-robot/) — _The Robot Report_
- [What building Shippy taught us about building agents](https://huggingface.co/blog/allenai/shippy-tech-blog) — _Hugging Face - Blog_
- [Model Routing Is Simple. Until It Isn’t.](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt) — _Hugging Face - Blog_
- [Welcome Inkling by Thinking Machines](https://huggingface.co/blog/thinkingmachines-inkling) — _Hugging Face - Blog_
- [Key to Humanoid Progress: Managing the Power Behind the Robots](https://www.therobotreport.com/key-to-humanoid-progress-managing-the-power-behind-the-robots/) — _The Robot Report_
- [NVIDIA shares how to evaluate general-purpose robot policies for real-world deployment](https://www.therobotreport.com/nvidia-shares-how-evaluate-general-purpose-robot-policies-real-world-deployment/) — _The Robot Report_
- [The Robot Report parent company, WTWH Media, rebrands as Arrowfly](https://www.therobotreport.com/the-robot-report-parent-company-wtwh-media-rebrands-as-arrowfly/) — _The Robot Report_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
