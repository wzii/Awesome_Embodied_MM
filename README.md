# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-09-05 · **Tracked:** 1014 core · 828 adjacent ·
465 news · **22653** benchmark rows across **9213** model
variants · **30** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **Miscellaneous** | 622 | ➡️ steady | Papers that do not fit neatly into the other directions, covering diverse topics from theory to applications. |
| **Vision-Language-Action Model Architectures and Training** | 369 | ➡️ steady | Designs and improves Vision-Language-Action (VLA) model architectures, training recipes, and post-training methods for… |
| **World Action Models for Robot Control** | 122 | 📈 rising | Develops world action models (WAMs) that jointly predict future states and generate actions for robotic manipulation… |
| **Efficient Video Generation and Inference** | 106 | ➡️ steady | Develops methods to accelerate video generation and world model inference through caching, sparse attention… |
| **Video Generation and World Model Evaluation** | 91 | 📈 rising | Creates benchmarks, metrics, and evaluation frameworks for video generation models and world models, assessing physical… |
| **World Models for Autonomous Driving** | 87 | ➡️ steady | Develops world models and VLA systems specifically for end-to-end autonomous driving, planning, and simulation. |
| **Latent World Models and Representation Learning** | 80 | 📈 rising | Studies latent-space world models, representation learning objectives (JEPA, contrastive), and their theoretical… |
| **Long-Horizon and Memory-Augmented World Models** | 80 | 📈 rising | Addresses long-horizon prediction, memory, and consistency in world models and VLA policies for extended tasks. |
| **Safety, Security, and Robustness of World Models** | 72 | 📈 rising | Investigates adversarial attacks, defenses, safety guarantees, and failure detection for world models and VLA policies. |
| **Physics-Grounded and Causal World Models** | 68 | 📈 rising | Incorporates physical principles, causal reasoning, and structured dynamics into world models for improved consistency… |
| **Interactive and Multi-Agent World Models** | 42 | 📉 cooling | Develops world models for interactive, multi-agent, and multi-view scenarios, including cooperative and competitive… |
| **Tactile and Multimodal World Models** | 32 | ➡️ steady | Integrates tactile, force, and other sensory modalities into world models and VLA policies for contact-rich… |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **8.23** | Flash-WAM: Modality-Aware Distillation for World Action Models | 2026-06-03 | spd 9 · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.05254) · [pdf](https://arxiv.org/pdf/2606.05254v1) |
| **8.12** | TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM | 2026-07-29 | spd 9 · gen 3 · spec 8 · cost 9 | [abs](https://arxiv.org/abs/2607.27205) · [pdf](https://arxiv.org/pdf/2607.27205v1) · [code](https://github.com/H-EmbodVis/TurboVLA) |
| **8.12** | MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO? | 2026-09-03 | spd 9 · gen 3 · spec 8 · cost 9 | [abs](https://arxiv.org/abs/2609.03715) · [pdf](https://arxiv.org/pdf/2609.03715v1) · [code](https://github.com/k1000dai/MINERVA) |
| **8.11** | Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving | 2026-07-17 | spd 9 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2607.15621) · [pdf](https://arxiv.org/pdf/2607.15621v1) |
| **8.1** | CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators | 2026-08-27 | spd – · gen 9 · spec 7 · cost – | [abs](https://arxiv.org/abs/2608.27406) · [pdf](https://arxiv.org/pdf/2608.27406v1) · [code](https://github.com/omni-CLAP/clap) |
| **8.09** | DriftWorld: Fast World Modeling through Drifting | 2026-07-16 | spd 9 · gen 6 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2607.15065) · [pdf](https://arxiv.org/pdf/2607.15065v1) · [code](https://github.com/Susie-Lu/driftworld) |
| **8.09** | Keep the Future, Drop the Rollout: RIFT for World Action Models | 2026-08-12 | spd 8 · gen 6 · spec 9 · cost 7 | [abs](https://arxiv.org/abs/2608.11521) · [pdf](https://arxiv.org/pdf/2608.11521v1) |
| **7.87** | Reinforced Planning with Latent World Models | 2026-08-19 | spd 8 · gen 6 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2608.18669) · [pdf](https://arxiv.org/pdf/2608.18669v1) |
| **7.83** | Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference | 2026-08-05 | spd 9 · gen – · spec 4 · cost 7 | [abs](https://arxiv.org/abs/2608.04428) · [pdf](https://arxiv.org/pdf/2608.04428v1) |
| **7.79** | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models | 2026-06-24 | spd 8 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.25473) · [pdf](https://arxiv.org/pdf/2606.25473v1) · [code](https://github.com/NVlabs/rcm) |
| **7.73** | BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving | 2026-06-07 | spd 8 · gen 3 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2606.08684) · [pdf](https://arxiv.org/pdf/2606.08684v1) · [code](https://github.com/George-Ling3/BLUE) |
| **7.72** | Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model | 2026-07-13 | spd – · gen 7 · spec 8 · cost 2 | [abs](https://arxiv.org/abs/2607.11643) · [pdf](https://arxiv.org/pdf/2607.11643v1) |
| **7.71** | LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies | 2026-06-14 | spd 7 · gen 7 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15768) · [pdf](https://arxiv.org/pdf/2606.15768v1) |
| **7.71** | StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models | 2026-08-12 | spd 5 · gen 8 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2608.11671) · [pdf](https://arxiv.org/pdf/2608.11671v1) |
| **7.67** | vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models | 2026-06-06 | spd 8 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.08094) · [pdf](https://arxiv.org/pdf/2606.08094v1) · [code](https://github.com/ggml-org/llama.cpp) |
| **7.67** | Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models | 2026-06-16 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.17846) · [pdf](https://arxiv.org/pdf/2606.17846v1) · [code](https://github.com/QwenLM/Qwen-RobotManip) |
| **7.67** | One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation | 2026-08-26 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2608.26058) · [pdf](https://arxiv.org/pdf/2608.26058v1) |
| **7.66** | Cosmos 3: Omnimodal World Models for Physical AI | 2026-06-01 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02800) · [pdf](https://arxiv.org/pdf/2606.02800v1) · [code](https://github.com/nvidia/cosmos) |
| **7.66** | Multiplayer Interactive World Models with Representation Autoencoders | 2026-07-06 | spd 7 · gen 2 · spec 8 · cost 2 | [abs](https://arxiv.org/abs/2607.05352) · [pdf](https://arxiv.org/pdf/2607.05352v1) · [code](https://github.com/mira-wm/mira) |
| **7.66** | GlanceWAM: Sparse Test-Time Imagination for World-Action Models | 2026-08-25 | spd 8 · gen 6 · spec 7 · cost 5 | [abs](https://arxiv.org/abs/2608.23927) · [pdf](https://arxiv.org/pdf/2608.23927v1) · [code](https://github.com/linhanwang/GlanceWAM) |
| **7.65** | ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training | 2026-08-31 | spd 8 · gen 8 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2609.00188) · [pdf](https://arxiv.org/pdf/2609.00188v1) · [code](https://github.com/ZimaBlue-WAM/ZimaBlue) |
| **7.64** | Foresight Without Seeing: Latent Futures for World Action Models | 2026-08-12 | spd 5 · gen 4 · spec 9 · cost 6 | [abs](https://arxiv.org/abs/2608.11605) · [pdf](https://arxiv.org/pdf/2608.11605v1) |
| **7.63** | Latent Action as Intention Enables Efficient Future Imagination for World Action Models | 2026-08-25 | spd 7 · gen 6 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2608.24882) · [pdf](https://arxiv.org/pdf/2608.24882v1) |
| **7.61** | AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing | 2026-06-08 | spd 8 · gen 3 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.09811) · [pdf](https://arxiv.org/pdf/2606.09811v1) |
| **7.61** | GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation | 2026-06-07 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.08530) · [pdf](https://arxiv.org/pdf/2606.08530v1) · [code](https://github.com/babynabeauty/GEAR-VLA) |
| **7.59** | Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories | 2026-07-16 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2607.15330) · [pdf](https://arxiv.org/pdf/2607.15330v1) · [code](https://github.com/Physical-Intelligence/openpi) |
| **7.59** | JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling | 2026-08-10 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2608.09381) · [pdf](https://arxiv.org/pdf/2608.09381v1) |
| **7.58** | Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation | 2026-06-02 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.03784) · [pdf](https://arxiv.org/pdf/2606.03784v2) |
| **7.58** | FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation | 2026-06-18 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.20867) · [pdf](https://arxiv.org/pdf/2606.20867v1) |
| **7.57** | SANTS: A State-Adaptive Scheduler for World Action Models | 2026-05-27 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2605.27947) · [pdf](https://arxiv.org/pdf/2605.27947v1) |
| **7.57** | Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think | 2026-06-18 | spd 7 · gen 7 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.20246) · [pdf](https://arxiv.org/pdf/2606.20246v1) |
| **7.57** | Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking | 2026-08-04 | spd 8 · gen 5 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2608.03231) · [pdf](https://arxiv.org/pdf/2608.03231v1) |
| **7.54** | Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference | 2026-07-14 | spd 8 · gen 4 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2607.12659) · [pdf](https://arxiv.org/pdf/2607.12659v1) · [code](https://github.com/PKU-SEC-Lab/Jetson-PI) |
| **7.54** | CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model | 2026-07-28 | spd – · gen 5 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2607.25487) · [pdf](https://arxiv.org/pdf/2607.25487v1) · [code](https://github.com/BrainJellyPie/CoTinyVLA) |
| **7.53** | SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour | 2026-06-18 | spd – · gen 4 · spec 9 · cost – | [abs](https://arxiv.org/abs/2606.19928) · [pdf](https://arxiv.org/pdf/2606.19928v1) |
| **7.53** | Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies | 2026-07-10 | spd – · gen 7 · spec 8 · cost – | [abs](https://openreview.net/forum?id=h3hJmhiWJ7) · [pdf](https://openreview.net/pdf?id=h3hJmhiWJ7) |
| **7.53** | Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation | 2026-08-14 | spd 8 · gen 4 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2608.14379) · [pdf](https://arxiv.org/pdf/2608.14379v1) |
| **7.52** | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis | 2026-06-04 | spd 8 · gen 7 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.05979) · [pdf](https://arxiv.org/pdf/2606.05979v1) · [code](https://github.com/SJTU-DENG-Lab/WLA) |
| **7.52** | CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation | 2026-08-18 | spd 8 · gen 5 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2608.17717) · [pdf](https://arxiv.org/pdf/2608.17717v1) |
| **7.51** | FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation | 2026-06-11 | spd – · gen 8 · spec 6 · cost – | [abs](https://arxiv.org/abs/2606.13102) · [pdf](https://arxiv.org/pdf/2606.13102v1) |
| **7.49** | 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training | 2026-06-03 | spd – · gen 6 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.04436) · [pdf](https://arxiv.org/pdf/2606.04436v1) |
| **7.49** | $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation | 2026-06-11 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.13672) · [pdf](https://arxiv.org/pdf/2606.13672v1) · [code](https://github.com/mseitzer/pytorch-fid) |
| **7.49** | SimWAM: A Simple World Action Model for End-to-End Autonomous Driving | 2026-08-07 | spd 6 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2608.07468) · [pdf](https://arxiv.org/pdf/2608.07468v1) · [code](https://github.com/H-EmbodVis/SimWAM) |
| **7.49** | SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving | 2026-09-03 | spd 6 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2609.03602) · [pdf](https://arxiv.org/pdf/2609.03602v1) |
| **7.48** | LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World | 2026-05-31 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458v1) |
| **7.48** | hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance | 2026-08-13 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2608.13678) · [pdf](https://arxiv.org/pdf/2608.13678v1) |
| **7.47** | DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model | 2026-06-10 | spd 8 · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.12105) · [pdf](https://arxiv.org/pdf/2606.12105v1) |
| **7.46** | Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning | 2026-05-29 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.30795) · [pdf](https://arxiv.org/pdf/2605.30795v1) |
| **7.46** | Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments | 2026-05-28 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.30280) · [pdf](https://arxiv.org/pdf/2605.30280v2) · [code](https://github.com/QwenLM/Qwen-VLA) |
| **7.46** | Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance | 2026-05-22 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.24203) · [pdf](https://arxiv.org/pdf/2605.24203v1) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _2828 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| KV baseline (growing cache) | — | inference state size at 100k steps | 25600000.0 | authors |
| π0.5 (LeRobot) _(lerobot/libero)_ | — | inference time per chunk | 12781.0 | authors |
| OpenVLA-7B _(LIBERO)_ | — | I(X; X~) (attack channel capacity) | 5000.0 | authors |
| AURA-Mem | — | inference state size | 4224.0 | authors |
| Wan 2.2 (chunked) _(LIBERO-90)_ | — | FVD | 4177.0 | 3rd-party |
| SimpleVLA-RL _(LIBERO)_ | Long | iterations to 90% success rate | 2450.0 | authors |
| vla.cpp | — | peak RSS | 2031.0 | authors |
| vla.cpp | — | VRAM usage | 1312.0 | authors |
| SmolVLA | — | inference time per chunk | 1010.0 | authors |
| π0.5 _(LIBERO)_ | — | latency | 958.54 | 3rd-party |

#### CALVIN  ·  _150 results_

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

#### RoboTwin  ·  _599 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LingBot-VA | — | per-chunk latency | 8100.0 | authors |
| LingBot-VLA + BCP _(RoboTwin 2.0 Clean)_ | all 50 tasks | VLA inference time | 940.13 | authors |
| ST-WAM _(RoboTwin 2.0)_ | — | inference latency | 756.17 | authors |
| Fast-WAM _(RoboTwin 2.0)_ | — | inference latency | 609.3 | authors |
| WAM4D _(RoboTwin 2.0)_ | — | inference latency | 525.43 | authors |
| Flash-WAM _(LingBot-VA)_ | — | per-chunk latency | 348.0 | authors |
| HALO-WA _(online task-specific)_ | Beat Block Hammer | episode length | 213.7 | authors |
| IRASim _(RoboTwin 2.0)_ | Overall | FVD | 126.2 | authors |
| HY-VLA | place_empty_cup | success rate | 100.0 | authors |
| π0.5 _(RoboTwin2.0)_ | Grab Roller | success rate | 98.6 | authors |

#### SimplerEnv  ·  _260 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| dense | pick-coke | serve latency p50 | 102.1 | authors |
| VLA-Pruner | pick-coke | serve latency p50 | 101.2 | authors |
| GeoAlign _(robot-domain RGB-D + Dpol (SimplerEnv-Fractal demonstrations))_ | Pick Coke Can | success rate | 100.0 | authors |
| S2-VLA | Eggplant in Basket | success rate | 100.0 | authors |
| actuation-slack refresh | pick-coke | serve latency p50 | 100.0 | authors |
| OpenVLA-7b | Pick up | failure rate (FR) | 97.5 | authors |
| GR00T-N1.6 | Pick up | failed object coverage (FOC) | 97.1 | authors |
| Afford-VLA _(LIBERO + Affordance dataset)_ | Put Eggplant | Success rate | 96.8 | authors |
| X-VLA + IDR | WidowX | Average success rate | 95.83 | authors |
| Reflective VLA _(π0.5 training data)_ | Spoon | success rate | 95.8 | authors |

#### RLBench  ·  _52 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PointACT _(RLBench (10 tasks))_ | Close laptop lid | success rate | 99.0 | authors |
| EO1 (reproduced) _(RLBench (10 tasks))_ | Mean | success rate | 73.2 | 3rd-party |
| AtlasVLA _(RLBench (100 demos per task))_ | — | success rate | 70.8 | authors |
| GR00T(arch) + Point _(LIBERO-Spatial / RLBench-10Tasks)_ | Mean | success rate | 69.7 | authors |
| GR00T(arch) + Point (final layer) _(RLBench-10Tasks)_ | Mean | success rate | 69.7 | authors |
| GR00T(arch) + Point (multi-scale, K=128) _(RLBench-10Tasks)_ | Mean | success rate | 65.6 | authors |
| GR00T(arch) + Point (multi-scale, K=64) _(RLBench-10Tasks)_ | Mean | success rate | 65.2 | authors |
| MemoryVLA _(RLBench (100 demos per task))_ | — | success rate | 55.0 | 3rd-party |
| π0 + CamVLA | Mean | success rate | 51.4 | authors |
| GR00T(arch) _(LIBERO-Spatial / RLBench-10Tasks)_ | Mean | success rate | 50.8 | authors |

#### Meta-World  ·  _92 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | push | return | 1641.0 | authors |
| Oracle inverse | reach, push, pick-place | mean cumulative reward | 485.5 | authors |
| RLS | reach, push, pick-place | mean cumulative reward | 434.41 | authors |
| Replay | reach, push, pick-place | mean cumulative reward | 428.59 | authors |
| SpikeWorld _(multimodal cache (SHD, SSC, text, image, video) + Meta-World)_ | reach, push, pick-place | mean cumulative reward | 422.58 | authors |
| Full prediction tuning _(same as SpikeWorld (further tuning on Meta-World))_ | reach, push, pick-place | mean cumulative reward | 422.19 | authors |
| VICX _(Meta-World (drawer-open, reach, basketball))_ | coffee-button | success rate | 100.0 | authors |
| GUARD (SmolVLA) | — | ROC-AUC | 99.94 | authors |
| SUREFlow _(LIBERO, Meta-World, LIBERO-PRO)_ | Easy | Success Rate | 97.8 | authors |
| FabriVLA _(Evo-1 Meta-World demonstration dataset)_ | easy | success rate | 95.0 | authors |

#### ManiSkill  ·  _104 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| CompCPZ _(ManiSkill3 (200 synthetic frames for YOLOv8n fine-tune))_ | Pooled 18 families | paired sign test wins | 1900.0 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.99)_ | lift-cube | return | 175.0 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | pick-cube | return | 147.0 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 98.68 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 97.44 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 95.78 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 93.14 | authors |
| π0.5 | — | success rate | 89.8 | authors |
| FORCE (π0) _(ManiSkill (offline + online))_ | — | success rate | 86.9 | authors |
| OpenVLA-OFT + Feat2Go | — | success rate | 82.9 | authors |

#### RoboCasa  ·  _252 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Joint-WAM _(RoboCasa)_ | — | inference latency | 593.1 | authors |
| LAWA _(RoboCasa + egocentric videos)_ | — | inference latency | 338.5 | authors |
| Fast-WAM _(RoboCasa)_ | — | inference latency | 196.5 | authors |
| Cosmos-Policy | Turn Off Microwave | success rate | 100.0 | authors |
| Z-1 RL _(RoboCasa demonstrations)_ | Door | success rate | 97.0 | authors |
| Z-1 SFT _(RoboCasa demonstrations)_ | Door | success rate | 93.2 | authors |
| MiDAS _(1 demonstration)_ | — | success rate | 89.3 | authors |
| GIFT-WAM-Fast | — | success rate | 83.6 | authors |
| GIFT-WAM-IDM | — | success rate | 82.3 | authors |
| X-WAM | Group average | success rate | 80.8 | authors |

#### Open-X / RT  ·  _72 results_

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

#### ALFWorld  ·  _37 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GIGPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 90.4 | authors |
| Online WMSFT _(ALFWorld)_ | — | success rate | 90.4 | authors |
| KnOTS(V) _(ALFWorld)_ | — | success rate | 87.8 | authors |
| WMRL->PRL _(ALFWorld)_ | — | success rate | 87.0 | authors |
| PRL _(ALFWorld)_ | — | success rate | 84.6 | authors |
| GRPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 77.9 | authors |
| WMSFT->PRL _(ALFWorld)_ | — | success rate | 66.4 | authors |
| Qwen3-8B (MEMWM+Skill) | Overall | task success | 65.24 | authors |
| ReflAct + BB-WM | — | SR@1 | 65.2 | authors |
| ReflAct + Belief | — | SR@1 | 63.4 | authors |

#### VBench  ·  _1105 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| HunyuanVideo (no caching) | 33 prompts from VBench | Latency | 1359.0 | authors |
| Wan2.1-14B | — | latency | 948.0 | authors |
| MDD | — | latency | 321.0 | authors |
| EasyAnimateV5.1-12B | — | latency | 246.0 | authors |
| Wan-I2V | Cut & Drag | Flow-Err | 181.1 | 3rd-party |
| GWTF | Cut & Drag | Flow-Err | 152.81 | 3rd-party |
| PTQ4DiT | — | FVD-FP | 124.2 | authors |
| Q-ARVD | — | FVD-FP | 116.26 | authors |
| Wan-T2V | T2V Motion Transfer | Flow-Err | 103.26 | 3rd-party |
| TTM | Cut & Drag | Flow-Err | 102.39 | 3rd-party |

#### AgiBot / GENIE  ·  _68 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| NebulaVLA-Homo | — | avg inference latency | 115.0 | authors |
| V-Link _(AGIBOT A3 Ultra teleoperation data)_ | Autonomous Power-On | success rate | 98.0 | authors |
| Egocentric (ours) _(HumanNet (egocentric portion, 5000h subset))_ | Seen tasks (in-distribution) | success rate | 92.5 | authors |
| NebulaVLA-Heter | Packaging Line Material Feeding | success rate | 92.5 | authors |
| Reward as an Agent | — | Overall Accuracy | 91.0 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | Scene Consistency | 90.41 | authors |
| NebulaVLA-Homo | Packaging Line Material Feeding | success rate | 90.0 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | EWMScore | 82.45 | authors |
| InternVLA-M1 | — | avg inference latency | 81.0 | 3rd-party |
| GR00T-N1.6 _(AGIBOT A3 Ultra teleoperation data)_ | Autonomous Power-On | success rate | 78.0 | authors |

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

#### nuScenes  ·  _305 results_

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

#### DAVIS  ·  _123 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Image Conductor | joint object and camera control | EPE | 91.64 | 3rd-party |
| Ours VAE _(in-house synthetic dataset)_ | reconstruction | VBench Total | 82.93 | authors |
| LightX2V VAE | reconstruction | VBench Total | 82.44 | authors |
| Go-With-The-Flow | joint object and camera control | EPE | 41.99 | 3rd-party |
| Diffusion-As-Shader | joint object and camera control | EPE | 40.23 | 3rd-party |
| 4DStreamCtrl Teacher _(OpenVidHD-Motion3D)_ | streaming efficiency | Latency | 34.92 | authors |
| 4DStreamCtrl Causal _(OpenVidHD-Motion3D)_ | streaming efficiency | Memory | 31.8 | authors |
| 4DStreamCtrl Teacher _(OpenVidHD-Motion3D)_ | streaming efficiency | Memory | 23.9 | authors |
| 4DStreamCtrl Causal _(OpenVidHD-Motion3D)_ | joint object and camera control | FPS | 20.6 | authors |
| 4DStreamCtrl Causal _(OpenVidHD-Motion3D)_ | streaming efficiency | Throughput | 20.6 | authors |

#### PushT  ·  _113 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LeWM + CEM | — | eval time | 198.92 | 3rd-party |
| LeWM + AITS | — | success rate | 100.0 | authors |
| DA-LeWM | — | success rate | 98.7 | authors |
| VIS-WM | — | success rate | 98.0 | authors |
| SA+IDM | — | success rate | 98.0 | authors |
| FF-JEPA (DM) _(PushT filtered successful demonstrations)_ | Short-horizon (t=25) | success rate | 96.09 | authors |
| LeWM | — | success rate | 96.0 | authors |
| Le-WM | — | success rate | 96.0 | authors |
| LeWorldModel | — | success rate | 96.0 | 3rd-party |
| LeFlow _(offline trajectory data from LeWM benchmarks)_ | — | success rate | 95.2 | authors |

#### NAVSIM  ·  _111 results_

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

#### Bench2Drive  ·  _107 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| BLUE _(SimLingo training set (~400 routes))_ | — | latency | 549.5 | authors |
| ORION _(Bench2Drive, Chat-B2D)_ | trajectory prediction | decoder latency | 497.52 | authors |
| CLEAR (InternVL3-1B) _(SimLingo dataset (~3.1M samples))_ | — | Efficiency | 275.4 | authors |
| VLGA _(Bench2Drive train routes)_ | — | Efficiency | 194.63 | authors |
| ORION _(Bench2Drive, Chat-B2D)_ | command probe | command-probe accuracy | 97.7 | authors |
| LinkVLA _(PDM-Lite)_ | — | Driving Score | 91.01 | 3rd-party |
| BLUE _(SimLingo training set (~400 routes))_ | — | driving score | 90.58 | authors |
| BLUE (CriticVLA) _(CriticVLA training set)_ | — | driving score | 90.37 | authors |
| AnchorVLA _(PDM-Lite)_ | — | Driving Score | 89.92 | authors |
| TakeVLA _(PDM-Lite)_ | — | driving score | 89.72 | 3rd-party |

#### DROID  ·  _106 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Wan2.2 TI2V 5B _(DROID 700-sample pick-and-place subset)_ | — | inference time | 400.0 | 3rd-party |
| MiniWorld-3B _(DROID)_ | — | Trajectory Accuracy improvement | 249.0 | authors |
| MiniWorld-3B _(DROID)_ | — | Depth Accuracy improvement | 238.0 | authors |
| MiniWorld-3B _(DROID)_ | — | LPIPS improvement | 216.0 | authors |
| TesserAct | — | FID | 164.54 | 3rd-party |
| MiniWorld-3B _(DROID)_ | — | SSIM improvement | 125.0 | authors |
| π0.5-droid _(DROID)_ | Task Average | task progression rate | 89.3 | 3rd-party |
| Cloak-VLA _(DROID)_ | Task Average | task progression rate | 88.0 | authors |
| LAP-VLA | Task Average | task progression rate | 87.9 | 3rd-party |
| G0.5 _(pretrained on robot datasets + VQA, then post-trained on DROID)_ | — | success rate | 82.5 | authors |

#### NAVSIM v1  ·  _99 results_

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

#### Real-world  ·  _97 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| InSight _(50 human scooping demonstrations + acquired lateral-push primitive)_ | sweeping | success rate | 100.0 | authors |
| SAGE-SFT _(π0.5)_ | Place the green cube on the plate | Success rate | 100.0 | authors |
| OASIS | Goal | success rate | 98.6 | authors |
| InSight _(50 human pick-and-place demonstrations + 20 successful pour primitives)_ | pour beans into bowl | success rate | 96.0 | authors |
| 3DThinkVLA (Ours) _(VLA data + 3D reasoning data (co-training))_ | Transparent container placement | success rate | 93.3 | authors |
| InSight _(50 human pick-and-place demonstrations + 20 successful twist primitives)_ | twist cap open | success rate | 92.0 | authors |
| π0.5 | Place the green cube on the plate | Success rate | 90.0 | 3rd-party |
| OrthoSkillVLA | Flip, Pick, Push, Press | Average success rate (%) | 86.25 | authors |
| MaskWAM | language-ambiguous tasks (ID + OOD) | success rate | 84.9 | authors |
| π0.5 | Average (Goal, Spatial, Long) | success rate | 81.6 | 3rd-party |

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

## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
- **ActionMap: Robot Policy Learning via Voxel Action Heatmap** — ActionMap replaces the unstructured single-point action decoder in VLA models with a voxel heatmap action head that predicts a probability distribution over a discretized 3D action space, explicitly exploiting the geometric proximity of neighboring actions rather than treating the action space as unstructured… _(→ WAM: In World Action Models, the action conditioning mechanism is critical for predicting how actions transform world states. The voxel heatmap representation can transfer in two ways: (1) as a structured action encoding input to the world model—replacing flat…)_ [abs](https://arxiv.org/abs/2606.06904) · [pdf](https://arxiv.org/pdf/2606.06904v1) · [code](https://github.com/showlab/ActionMap)
- **Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs** — ST-Merge is a plug-and-play, training-free spatio-temporal visual token merging framework that reduces inference latency by fusing redundant visual tokens during the visual encoding phase. It constructs 3D spatiotemporal coordinates for multi-queue parallel matching and weighted aggregation across frames, and… _(→ WAM: World Action Models must process long video histories to predict future world states and generate actions, making visual token count a critical computational bottleneck. ST-Merge's spatio-temporal token merging could be directly applied to the visual encoder…)_ [abs](https://arxiv.org/abs/2606.29350) · [pdf](https://arxiv.org/pdf/2606.29350v1) · [code](https://github.com/Junzhou-Chen/ST_Merge)
- **WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models** — A multi-dimensional, long-horizon evaluation framework for interactive world models that introduces novel metrics: per-frame action metrics to bypass semantic scale disparity, segment-based drift metrics to capture mid-sequence visual collapse, controllability-gated physics evaluation to isolate physical plausibility… _(→ WAM: World Action Models (WAMs) inherently suffer from compounding errors over long horizons, leading to visual drift, physical inconsistencies, and memory loss. The benchmark's metrics—particularly the controllability-gated physics evaluation and action-decoupled…)_ [abs](https://arxiv.org/abs/2606.31672) · [pdf](https://arxiv.org/pdf/2606.31672v1)
- **DWM: Separating World Effects from Actions in Latent World Models** — DWM decomposes latent world model transitions into an action-invariant world effect (environment-intrinsic dynamics like gravity, inertia, drift) and a complementary action-driven component, using an auxiliary world head regularized by a normalized world-contrastive objective to be action-invariant, coupled with an… _(→ WAM: World Action Models must predict future states conditioned on actions and then use those predictions to select or generate actions. DWM's decomposition transfers directly: (1) By separating action-invariant dynamics from action-driven effects, a WAM can more…)_ [abs](https://arxiv.org/abs/2607.18715) · [pdf](https://arxiv.org/pdf/2607.18715v1)
- **The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping** — The core innovation is identifying that the provenance of the gate signal—not the token-skipping mechanism itself (reuse vs. deletion)—determines closed-loop reliability in accelerated VLAs. When the gate is 'dirty' (harvested from the model's own accelerated/skipped forwards), compounding visibility errors cause… _(→ WAM: World Action Models operate in closed-loop rollouts where compounding prediction errors are already a central challenge. If WAMs adopt token skipping, caching, or pruning for efficient world-state prediction, the same self-harvested gate collapse will occur…)_ [abs](https://arxiv.org/abs/2608.00391) · [pdf](https://arxiv.org/pdf/2608.00391v1)
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

## 👥 Influential Authors & Groups
- **[Kaipeng Zhang](https://www.semanticscholar.org/author/2313680460)** (12 papers) — Kaipeng Zhang's research focuses on advancing video-based world models for interactive, long-horizon, and physically plausible simulation, including causality evaluation, state management, real-time rendering, and multi-agent consistency.
- **[Shanghang Zhang](https://www.semanticscholar.org/author/2346116279)** (9 papers) — Shanghang Zhang's research focuses on world-action models (WAM) for robotic manipulation and humanoid loco-manipulation, integrating latent physical reasoning, reinforcement learning, safe RL, and simulator fidelity diagnostics to improve action…
- **[Yao Mu](https://www.semanticscholar.org/author/2348161293)** (8 papers) — Yao Mu's research focuses on advancing Vision-Language-Action (VLA) models for robotic manipulation, with contributions in novel action decoding (Equilibrium Matching), efficient world models (ImageWAM, Enfold), reinforcement learning for discrete diffusion…
- **[Junjie He](https://www.semanticscholar.org/author/2316016558)** (8 papers) — Developing World Action Models (WAM) for robotic manipulation, focusing on cross-embodiment learning, mobile manipulation, semantic guidance, spatiotemporal awareness, and robustness. Also explores JEPA world models and real-time audio-visual interaction…
- **[Peiyan Li](https://www.semanticscholar.org/author/2305635155)** (8 papers) — Research focuses on developing and improving Vision-Language-Action (VLA) models for robotic manipulation, including fine-tuning strategies (StaKe), chain-of-thought reasoning (ERVLA), world models, test-time scaling, efficient keyframe interpolation…
- **[Xiaowei Chi](https://www.semanticscholar.org/author/2192825554)** (8 papers) — Xiaowei Chi's research focuses on world action models (WAMs) for robotic manipulation, including efficient video-based future imagination, manifold-aware cross-modal alignment, tactile modeling, reinforcement learning for joint world-action optimization, safe…
- **[Wenxuan Song](https://www.semanticscholar.org/author/2293142288)** (8 papers) — 研究世界动作模型（World Action Models）在移动操作中的应用，包括链式思维、轨迹预测、物理状态基础等，以提升机器人操作的泛化性和性能。
- **[Cong Wang](https://www.semanticscholar.org/author/2269795155)** (7 papers) — Cong Wang's research focuses on advancing video generation models, particularly in achieving long-video consistency, physical plausibility, identity-consistent multi-subject generation, human-object interaction, and controllable embodied manipulation. The…
- **[Enze Xie](https://www.semanticscholar.org/author/41020000)** (7 papers) — Efficient video generation, focusing on hybrid attention mechanisms, inference acceleration, and training acceleration, with applications in world models, embodied AI, and robotic manipulation.
- **[Jingjing Gong](https://www.semanticscholar.org/author/2371292918)** (7 papers) — Developing memory, world modeling, and action planning mechanisms to improve the scalability, robustness, and efficiency of Vision-Language-Action models for long-horizon robotic manipulation tasks.
- **[Xiaofeng Wang](https://www.semanticscholar.org/author/2242976725)** (7 papers) — Xiaofeng Wang's research focuses on developing world-action models and embodied AI systems for robotic manipulation and visual navigation, leveraging latent representations, video generation, and efficient policy learning to achieve spatial generalization and…
- **[Zheng Zhu](https://www.semanticscholar.org/author/2109516240)** (7 papers) — Zheng Zhu's research focuses on world action models (WAMs) for embodied AI, including 3D-aware data augmentation for manipulation policies, whole-body control for humanoids, hybrid-attention online RL for world-action models, and foundation models for robots…
- **[Yuan Xu](https://www.semanticscholar.org/author/2313357459)** (7 papers) — Yuan Xu's research focuses on improving vision-language-action (VLA) models and world-action models for robotic manipulation, particularly through techniques such as structured stage supervision, memory augmentation, test-time scaling, sparse keyframe…
- **[Yixiang Chen](https://www.semanticscholar.org/author/2366155958)** (7 papers) — Research focuses on improving vision-language-action models and world models for robotic manipulation, with emphasis on data efficiency, cross-embodiment generalization, memory augmentation, and efficient action representation.
- **[Hangjun Ye](https://www.semanticscholar.org/author/2367554550)** (7 papers) — Hangjun Ye's research focuses on developing world action models and world foundation models for embodied systems, including autonomous driving and robot navigation, by unifying scene generation, video prediction, and trajectory planning through multimodal…
- **[Chuanhao Li](https://www.semanticscholar.org/author/2294251099)** (7 papers) — Interactive world modeling and long-horizon video generation, focusing on world state management, consistency, and real-time interactive generation.
- **[Yan Huang](https://www.semanticscholar.org/author/2375031786)** (7 papers) — Yan Huang's research focuses on world-action models (WAMs) for embodied AI, including cross-embodiment generalization, unified visual navigation, long-horizon manipulation, test-time scaling, efficient world model rollout, and memory-augmented…
- **[Xintao Wang](https://www.semanticscholar.org/author/2305033532)** (6 papers) — Xintao Wang's research focuses on developing video world models and long-horizon video generation with consistent memory architectures, including decoupled memory, geometry-aware implicit memory, and learning-based adaptive context query. His work also…
- **[Xiaozhu Ju](https://www.semanticscholar.org/author/2392718853)** (6 papers) — Xiaozhu Ju's research focuses on developing world models and embodied agents that integrate persistent internal states, hybrid kinematics-physics dynamics, and safe reinforcement learning to improve action generalization, policy evaluation, and autonomous…
- **[Yann LeCun](https://www.semanticscholar.org/author/2270469816)** (6 papers) — Yann LeCun's research in world models and embodied AI focuses on developing hierarchical frameworks that unify object-centric representations with diffusion policies for robotic tasks, efficient visual representations for robot control, JEPA-based latent…
- **[Xuelong Li](https://www.semanticscholar.org/author/2336880377)** (6 papers) — Xuelong Li's research focuses on video generation with physical grounding, controllability, and real-time interaction, including physics-based scene generation, compositional human-camera control, world action models for embodied intelligence, and interactive…
- **[Yong Li](https://www.semanticscholar.org/author/2300459663)** (6 papers) — Yong Li's research focuses on developing world models for heterogeneous action control, navigation, and biomedical simulation, emphasizing unified frameworks like Mixture-of-Experts and adaptive multi-modal reasoning to improve prediction, planning, and…
- **[Hangjun Ye](https://www.semanticscholar.org/author/2384401186)** (6 papers) — Hangjun Ye's research focuses on integrating world-action modeling with vision-language models for embodied AI, including autonomous driving and mobile manipulation, while also exploring social intelligence through Theory-of-Mind reasoning in digital humans.
- **[M. Shou](https://www.semanticscholar.org/author/2047358650)** (6 papers) — Research focuses on Vision-Language-Action (VLA) models for end-to-end autonomous driving and robot manipulation, including multi-modality interaction, trajectory planning and optimization, action space modeling, and leveraging video generation and…
- **[Nan Duan](https://www.semanticscholar.org/author/2360369479)** (6 papers) — Nan Duan's research focuses on advancing video generation, world models, and generative modeling, particularly for long-duration, real-time, and memory-efficient autoregressive video generation, as well as few-step flow matching and embodied data…

## 📰 Embodied / Physical-AI News
- [ARM Institute gets $90M for 10 projects to modernize military manufacturing](https://www.therobotreport.com/arm-institute-gets-90m-for-10-projects-to-modernize-military-manufacturing/) — _The Robot Report_
- [Enovis to acquire surgical tech provider eCential Robotics for $180M](https://www.therobotreport.com/enovis-to-acquire-ecential-robotics-for-180m/) — _The Robot Report_
- [Cyborg Roaches Can Stab You With Needles](https://spectrum.ieee.org/cyborg-rescue-roach) — _IEEE Spectrum_
- [Calling robotics startups: Apply now to be part of the 2026 Robotics Startup Radar](https://www.therobotreport.com/calling-all-robotics-startups-apply-now-2026-robotics-startup-radar/) — _The Robot Report_
- [Lyte raises $165M to help robots better sense their surroundings](https://www.therobotreport.com/lyte-raises-165m-help-robots-better-sense-their-surroundings/) — _The Robot Report_
- [Robot.com partners with Sodexo to roll out more sidewalk delivery robots](https://www.therobotreport.com/robot-com-partners-sodexo-rolls-out-more-sidewalk-delivery-robots/) — _The Robot Report_
- [How FPGAs become the gatekeepers of physical AI security](https://www.therobotreport.com/how-fpgas-become-the-gatekeepers-of-physical-ai-security/) — _The Robot Report_
- [Video Friday: Digit Redecorates](https://spectrum.ieee.org/video-friday-agility-robotics-digit) — _IEEE Spectrum_
- [NVIDIA plans to acquire Hugging Face and keep AI development platform open](https://www.therobotreport.com/nvidia-to-acquire-hugging-face-and-keep-ai-develpment-platform-open/) — _The Robot Report_
- [PlusAI to take autonomous trucking public via a SPAC deal](https://www.therobotreport.com/plusai-takes-autonomous-trucking-public-via-spac-deal/) — _The Robot Report_
- [Protecting Dynamic Industrial Robot Cable Carriers](https://spectrum.ieee.org/industrial-robot-cable-carrier-protection) — _IEEE Spectrum_
- [The Best Way to Explore Lunar Craters Is a Giant Robot Ball](https://spectrum.ieee.org/moon-ball-robot) — _IEEE Spectrum_
- [NeoMME: an efficient Multimodal-native and Multilingual Encoder](https://huggingface.co/blog/Hcompany/neomme) — _Hugging Face - Blog_
- [Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps](https://huggingface.co/blog/grpo-with-trl-ifstruct) — _Hugging Face - Blog_
- [Give Your Coding Agents a Memory You Own](https://huggingface.co/blog/funes) — _Hugging Face - Blog_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
