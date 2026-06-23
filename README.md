# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-06-23 · **Tracked:** 356 core · 356 adjacent ·
164 news · **9613** benchmark rows across **3640** model
variants · **30** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **Vision-Language-Action Models: Policy and Control** | 187 | 📈 rising | Papers developing VLA models for robotic manipulation, navigation, and driving, focusing on action generation… |
| **Video Generation and World Model Simulation** | 135 | 📈 rising | Papers on video generation as world models, including controllable video synthesis, interactive simulation, and… |
| **Miscellaneous** | 60 | 📈 rising | Outlier papers on topics such as LLM reasoning, supply chains, blockchain, music recommendation, and theoretical… |
| **Benchmarks and Evaluation for World Models and VLAs** | 47 | 📈 rising | Papers introducing benchmarks, evaluation metrics, and diagnostic frameworks for world models, VLAs, and video… |
| **Model Efficiency: Compression, Quantization, Distillation** | 41 | 📈 rising | Papers on reducing model size, inference latency, and computational cost through pruning, quantization, knowledge… |
| **Long-Horizon and Temporal Consistency** | 41 | 📈 rising | Papers addressing long-range temporal dependencies, consistency, and planning in video generation and world models. |
| **World Action Models: Architectures and Training** | 37 | 📈 rising | Papers proposing novel world action model architectures, training paradigms, and latent representations for embodied… |
| **Physics and Causal Reasoning in World Models** | 35 | 📈 rising | Papers that incorporate physical principles, causal structure, or domain knowledge into world models for improved… |
| **Memory and State Persistence in World Models** | 32 | 📈 rising | Papers on persistent memory, state tracking, and long-term history management in world models and VLA policies. |
| **Cross-Embodiment and Multimodal Learning** | 29 | 📈 rising | Papers leveraging data from multiple embodiments, humans, or modalities to train generalizable policies and world… |
| **Safety, Robustness, and Adversarial Attacks** | 27 | 📈 rising | Papers on safety alignment, adversarial attacks, robustness to perturbations, and failure detection in world models and… |
| **Human-Robot Interaction and Social Robotics** | 8 | 📈 rising | Papers on collaborative robots, human intent understanding, and social navigation using VLA models. |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **8.23** | Flash-WAM: Modality-Aware Distillation for World Action Models | 2026-06-03 | spd 9 · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.05254) · [pdf](https://arxiv.org/pdf/2606.05254v1) |
| **7.73** | BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving | 2026-06-07 | spd 8 · gen 3 · spec 8 · cost 8 | [abs](https://arxiv.org/abs/2606.08684) · [pdf](https://arxiv.org/pdf/2606.08684v1) · [code](https://github.com/George-Ling3/BLUE) |
| **7.71** | LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies | 2026-06-14 | spd 7 · gen 7 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15768) · [pdf](https://arxiv.org/pdf/2606.15768v1) |
| **7.67** | vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models | 2026-06-06 | spd 8 · gen 5 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.08094) · [pdf](https://arxiv.org/pdf/2606.08094v1) · [code](https://github.com/ggml-org/llama.cpp) |
| **7.67** | Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models | 2026-06-16 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.17846) · [pdf](https://arxiv.org/pdf/2606.17846v1) · [code](https://github.com/QwenLM/Qwen-RobotManip) |
| **7.66** | Cosmos 3: Omnimodal World Models for Physical AI | 2026-06-01 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02800) · [pdf](https://arxiv.org/pdf/2606.02800v1) · [code](https://github.com/nvidia/cosmos) |
| **7.61** | AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing | 2026-06-08 | spd 8 · gen 3 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.09811) · [pdf](https://arxiv.org/pdf/2606.09811v1) |
| **7.61** | GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation | 2026-06-07 | spd – · gen 8 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.08530) · [pdf](https://arxiv.org/pdf/2606.08530v1) · [code](https://github.com/babynabeauty/GEAR-VLA) |
| **7.58** | Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation | 2026-06-02 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.03784) · [pdf](https://arxiv.org/pdf/2606.03784v2) |
| **7.58** | FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation | 2026-06-18 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.20867) · [pdf](https://arxiv.org/pdf/2606.20867v1) |
| **7.57** | SANTS: A State-Adaptive Scheduler for World Action Models | 2026-05-27 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2605.27947) · [pdf](https://arxiv.org/pdf/2605.27947v1) |
| **7.57** | Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think | 2026-06-18 | spd 7 · gen 7 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.20246) · [pdf](https://arxiv.org/pdf/2606.20246v1) |
| **7.53** | SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour | 2026-06-18 | spd – · gen 4 · spec 9 · cost – | [abs](https://arxiv.org/abs/2606.19928) · [pdf](https://arxiv.org/pdf/2606.19928v1) |
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
| **7.44** | Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation | 2026-06-22 | spd 8 · gen 6 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.23090) · [pdf](https://arxiv.org/pdf/2606.23090v1) |
| **7.38** | Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation | 2026-06-01 | spd 5 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.02486) · [pdf](https://arxiv.org/pdf/2606.02486v1) |
| **7.38** | Wall-OSS-0.5 Technical Report | 2026-05-29 | spd – · gen 8 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.30877) · [pdf](https://arxiv.org/pdf/2605.30877v2) · [code](https://github.com/X-Square-Robot/wall-x) |
| **7.37** | EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies | 2026-06-18 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.20092) · [pdf](https://arxiv.org/pdf/2606.20092v1) |
| **7.36** | SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models | 2026-05-30 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.00664) · [pdf](https://arxiv.org/pdf/2606.00664v1) |
| **7.36** | ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? | 2026-06-17 | spd 7 · gen 6 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.19531) · [pdf](https://arxiv.org/pdf/2606.19531v1) · [code](https://github.com/yuyangalin/ImageWAM) |
| **7.35** | Colosseum V2: Benchmarking Generalization for Vision Language Action Models | 2026-05-26 | spd – · gen 8 · spec – · cost – | [abs](https://arxiv.org/abs/2605.27759) · [pdf](https://arxiv.org/pdf/2605.27759v1) |
| **7.33** | DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World | 2026-06-10 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.11901) · [pdf](https://arxiv.org/pdf/2606.11901v1) · [code](https://github.com/isaac-sim/IsaacSim) |
| **7.33** | dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models | 2026-06-22 | spd – · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.23623) · [pdf](https://arxiv.org/pdf/2606.23623v1) |
| **7.31** | CausalDrive: Real-time Causal World Models for Autonomous Driving | 2026-06-13 | spd 6 · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.15341) · [pdf](https://arxiv.org/pdf/2606.15341v1) |
| **7.31** | Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation | 2026-06-17 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2606.19194) · [pdf](https://arxiv.org/pdf/2606.19194v1) |
| **7.28** | Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation | 2026-06-14 | spd 6 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.15869) · [pdf](https://arxiv.org/pdf/2606.15869v1) |
| **7.26** | Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models | 2026-06-09 | spd – · gen 8 · spec 7 · cost 5 | [abs](https://arxiv.org/abs/2606.11324) · [pdf](https://arxiv.org/pdf/2606.11324v1) · [code](https://github.com/pickxiguapi/Embodied-R1.5) |
| **7.25** | SparseWorld: Enhancing End-to-End Autonomous Driving via World Models with Sparse Scene Representation | 2026-05-23 | spd – · gen 2 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2605.24354) · [pdf](https://arxiv.org/pdf/2605.24354v1) |
| **7.25** | DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions | 2026-05-20 | spd 5 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2605.21273) · [pdf](https://arxiv.org/pdf/2605.21273v2) |
| **7.25** | Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models | 2026-06-13 | spd 8 · gen 3 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.15099) · [pdf](https://arxiv.org/pdf/2606.15099v1) |
| **7.24** | Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR | 2026-05-19 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.19282) · [pdf](https://arxiv.org/pdf/2605.19282v1) |
| **7.23** | ProgVLA: Progress-Aware Robot Manipulation Skill Learning | 2026-05-27 | spd – · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2605.28231) · [pdf](https://arxiv.org/pdf/2605.28231v1) |
| **7.23** | ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation | 2026-06-12 | spd 8 · gen 5 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2606.14255) · [pdf](https://arxiv.org/pdf/2606.14255v1) |
| **7.23** | IOI: Decoupling Kinematics and Physics for Interactive World Models | 2026-06-22 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.23296) · [pdf](https://arxiv.org/pdf/2606.23296v1) |
| **7.23** | AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control | 2026-06-22 | spd 7 · gen 6 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.23079) · [pdf](https://arxiv.org/pdf/2606.23079v1) |
| **7.23** | UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models | 2026-06-22 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.22794) · [pdf](https://arxiv.org/pdf/2606.22794v1) · [code](https://github.com/linsun449/UniFS) |
| **7.22** | DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions | 2026-05-29 | spd – · gen 3 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2605.31271) · [pdf](https://arxiv.org/pdf/2605.31271v1) |
| **7.22** | T-Rex: Tactile-Reactive Dexterous Manipulation | 2026-06-15 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.17055) · [pdf](https://arxiv.org/pdf/2606.17055v1) · [code](https://github.com/xiaoxiaoxh/reactive_diffusion_policy) |
| **7.21** | ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models | 2026-05-28 | spd 8 · gen 6 · spec – · cost 8 | [abs](https://arxiv.org/abs/2605.29438) · [pdf](https://arxiv.org/pdf/2605.29438v1) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _1052 results_

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

#### CALVIN  ·  _88 results_

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

#### RoboTwin  ·  _245 results_

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

#### SimplerEnv  ·  _120 results_

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

#### RLBench  ·  _36 results_

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

#### Meta-World  ·  _18 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | push | return | 1641.0 | authors |
| VICX _(Meta-World (drawer-open, reach, basketball))_ | coffee-button | success rate | 100.0 | authors |
| ProgVLA (0.1B) _(Meta-World MT50)_ | — | success rate | 78.5 | authors |
| SmolVLA (2.25B) | — | success rate | 68.24 | 3rd-party |
| AVDC _(Meta-World (11 tasks))_ | — | success rate | 55.0 | 3rd-party |
| π0.5-Finetune _(Meta-World MT50)_ | — | success rate | 26.1 | 3rd-party |
| π0.5-Scratch _(Meta-World MT50)_ | — | success rate | 20.6 | 3rd-party |
| Gemini-1.5-Pro | — | PIB (bits) | 2.65 | authors |

#### ManiSkill  ·  _24 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.99)_ | lift-cube | return | 175.0 | authors |
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | pick-cube | return | 147.0 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 98.68 | authors |
| FlowMPC _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 97.44 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | anytime success rate | 95.78 | authors |
| FM policy _(expert trajectories from SAC policy on PickCube-v1)_ | PickCube-v1 | end success rate | 93.14 | authors |
| OpenVLA-OFT + Feat2Go | — | success rate | 82.9 | authors |
| OpenVLA-OFT + Steps-To-Go | — | success rate | 79.0 | 3rd-party |
| OpenVLA-OFT + PPO | — | success rate | 76.8 | 3rd-party |
| FlowMPC _(expert trajectories from SAC policy on PickSingleYCB-v1)_ | PickSingleYCB-v1 | anytime success rate | 69.78 | authors |

#### RoboCasa  ·  _94 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ACE-EGO-0 _(Mixed robot demonstrations and egocentric human videos (6.0K+ hours))_ | — | average success | 72.8 | authors |
| GR00T-N1.5 _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.7 | authors |
| Late Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.0 | authors |
| Early Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 69.7 | authors |
| Spatial Forcing _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 68.3 | authors |
| World Pilot _(LIBERO)_ | — | success rate | 65.5 | authors |
| X-DiffVLA _(GR00T dataset (RoboCasa tasks))_ | — | Success Rate | 64.5 | authors |
| RLDX-1-FT-RC365 | — | success rate (SR) | 58.4 | authors |
| μ0 _(TraceExtract)_ | SlideToasterOvenRack | success rate | 56.0 | authors |
| π0.5 | — | safety | 55.7 | authors |

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

#### VBench  ·  _568 results_

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

#### AgiBot / GENIE  ·  _13 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Egocentric (ours) _(HumanNet (egocentric portion, 5000h subset))_ | Seen tasks (in-distribution) | success rate | 92.5 | authors |
| Reward as an Agent | — | Overall Accuracy | 91.0 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | Scene Consistency | 90.41 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | EWMScore | 82.45 | authors |
| Wan2.2 (no pretraining) | Seen tasks (in-distribution) | success rate | 40.0 | authors |
| Wan2.2 (no pretraining) | Unseen tasks (out-of-distribution) | action loss (L2) | 0.0273 | authors |
| Robot pretraining _(multi-embodiment real-robot trajectories (5000h))_ | Unseen tasks (out-of-distribution) | action loss (L2) | 0.0254 | authors |
| Egocentric (ours) _(HumanNet (egocentric portion, 5000h subset))_ | Unseen tasks (out-of-distribution) | action loss (L2) | 0.0204 | authors |

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

#### nuScenes  ·  _141 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SparseWorld-S _(nuScenes)_ | Inference memory | Inference Memory (IM) | 4397.0 | authors |
| Direct Regression (AnchoredVAEDiT) | future frame prediction | FID | 370.8 | authors |
| Diffusion (calibrated) - AnchoredVAEDiT | future frame prediction | FID | 162.5 | authors |
| LooseControlVideo (LCV) _(internal stock videos (~10k))_ | — | GOW | 97.32 | authors |
| OMNIDRIVE _(nuScenes)_ | — | TF | 97.0 | authors |
| OMNIDRIVE _(nuScenes)_ | — | BC | 95.5 | authors |
| OMNIDRIVE _(nuScenes)_ | — | SC | 93.1 | authors |
| LooseControlVideo (LCV) _(internal stock videos (~10k))_ | — | OcclAcc | 92.69 | authors |
| Control-free | — | TrajErr | 90.12 | 3rd-party |
| LooseControlVideo (LCV) _(internal stock videos (~10k))_ | — | Contain | 87.93 | authors |

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

#### HunyuanVideo  ·  _50 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SVG | — | Latency (s) | 3459.0 | 3rd-party |
| VGDFR | — | Latency (s) | 3019.0 | 3rd-party |
| Ours | — | Latency (s) | 2939.0 | authors |
| EasyCache | — | Latency (s) | 2850.0 | 3rd-party |
| DiCache | — | Latency (s) | 2814.0 | 3rd-party |
| SAP | — | Latency (s) | 2634.0 | 3rd-party |
| Ours + SAP | — | Latency (s) | 2555.0 | authors |
| ScalingAttention _(HunyuanVideo)_ | — | Density | 55.0 | authors |
| SVG2 | — | Density | 55.0 | 3rd-party |
| SVG | — | Density | 55.0 | 3rd-party |

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
- **WireCraft: A Simulation Benchmark for Industrial DLO Manipulation** — A modular simulation benchmark for industrial Deformable Linear Object (DLO) manipulation featuring dual physics models (articulated and deformable), configurable task families (connector insertion, clip routing, channel seating), and standardized evaluation protocols bridging simulation and real-world data. _(→ WAM: World Action Models must predict future states given actions, but currently lack benchmarks for complex, infinite-dimensional deformable dynamics. WireCraft provides the exact training data and evaluation protocols needed to develop WAMs capable of modeling…)_ [abs](https://arxiv.org/abs/2606.18097) · [pdf](https://arxiv.org/pdf/2606.18097v1) · [code](https://github.com/isaac-sim/IsaacSim)
- **ROBOSHACKLES: A Safety Dataset for Human-Injury Prevention in Embodied Foundation Models** — A scalable pipeline for constructing safety-critical robotic video data without real-world harm: starting from real robot observations (DROID), applying hazard-aware image editing to inject dangerous states, generating temporal prompts specifying expected scene evolution, and using a video generation model (Wan2.7) to… _(→ WAM: World Action Models must predict future world states conditioned on actions, making safety-critical anticipation essential. The hazard-aware editing + temporal-prompt + rollout-synthesis pipeline can be directly repurposed to generate safety-critical training…)_ [abs](https://arxiv.org/abs/2606.18632) · [pdf](https://arxiv.org/pdf/2606.18632v1)
- **Current World Models Lack a Persistent State Core** — Current world models lack a persistent state core—an internal world state that continuously evolves over time, decoupled from observation. When the camera looks away and returns, models simply resume the scene from the state at which it was last observed rather than advancing the event during the unobserved period… _(→ WAM: A World Action Model must predict the consequences of actions over time, including delayed and indirect effects. Without a persistent state core, a WAM cannot reason about what happens to objects or events when they leave the agent's observation—yet…)_ [abs](https://arxiv.org/abs/2606.20545) · [pdf](https://arxiv.org/pdf/2606.20545v1) · [code](https://github.com/JinPLu/WRBench)
- **Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models** — Mix-QVLA introduces task-evidence-aware mixed-precision quantization that computes gradient-weighted task-evidence maps from VLA functional boundary activations, measures both evidence-mass and attribution-distribution distortion between full-precision and quantized models, and critically models sensitivity as… _(→ WAM: World Action Models share VLA's need for efficient deployment and exhibit similar phase-dependent processing (e.g., world state encoding vs. action-conditioned prediction vs. planning/rollout). The time-aware sensitivity insight transfers directly: different…)_ [abs](https://arxiv.org/abs/2606.19565) · [pdf](https://arxiv.org/pdf/2606.19565v1)
- **GEOPHYS: The Geometry of Physical Plausibility** — Physical plausibility in videos can be detected by analyzing the emergent geometric properties of temporal embeddings from frozen image encoders, providing a highly efficient, training-free alternative to expensive LLM judges or specialized video models. _(→ WAM: WAMs require generating physically plausible future states. GEOPHYS can be used as a lightweight, training-free verifier to filter WAM rollouts (best-of-N sampling) at a fraction of the compute/memory cost of large world model verifiers. Additionally, these…)_ [abs](https://arxiv.org/abs/2606.20707) · [pdf](https://arxiv.org/pdf/2606.20707v1) · [code](https://github.com/ChristianInterno/GeoPhys)
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

## 👥 Influential Authors & Groups
- **[Xiaofeng Wang](https://www.semanticscholar.org/author/2242976725)** (5 papers) — 研究具身智能中的世界模型、动作表示与视觉导航，包括将动作转化为视觉图像（iMaC）、稀疏关键帧插值加速（SKIP）、3D感知数据增强（R2RDreamer）、潜空间世界-动作联合建模（WAM-Nav）以及无人机主动感知（ScoutVLA）。
- **[Andrea V. Bajcsy](https://www.semanticscholar.org/author/47370841)** (4 papers) — Andrea V. Bajcsy's research focuses on improving vision-language-action (VLA) and world models for robotic manipulation through interactive steering and test-time policy improvement, including methods to safely steer frozen models and evaluate policies via…
- **[Sanja Fidler](https://www.semanticscholar.org/author/2261282058)** (4 papers) — Sanja Fidler's research focuses on generative world models for physical AI, including real-time simulation for autonomous driving, omnimodal models that integrate language, image, video, audio, and action, multi-agent interactive simulation, and generating…
- **[Jie Huang](https://www.semanticscholar.org/author/2362441710)** (4 papers) — Jie Huang researches real-time video generation and world models, focusing on streaming frameworks for high-resolution video, memory mechanisms for action world models and infinite video generation, and efficient autoregressive video diffusion via…
- **[Zheng Zhu](https://www.semanticscholar.org/author/2265968976)** (4 papers) — Developing efficient embodied world models and video generation methods via keyframe interpolation and asynchronous denoising flow scheduling, and exploring unified latent world-action models for visual navigation.
- **[Hangjun Ye](https://www.semanticscholar.org/author/2384401186)** (4 papers) — Hangjun Ye's research focuses on unifying vision, language, and action (VLA) for embodied tasks and autonomous driving, with contributions including a unified framework for navigation and manipulation, latent future scene prediction for driving, and discrete…
- **[Cewu Lu](https://www.semanticscholar.org/author/2301174899)** (4 papers) — Cewu Lu's research focuses on advancing embodied AI and robotic manipulation by developing vision-language-action (VLA) models with spatial and tactile reasoning, as well as creating open-source hardware-software platforms for real-world deployment. Key…
- **[Pengfei Wan](https://www.semanticscholar.org/author/2363570130)** (3 papers) — Pengfei Wan's research focuses on video world models, long-horizon consistent world generation, and video reasoning, leveraging geometry-aware implicit memory, decoupled memory architectures, and test-time optimization with VLMs.
- **[Kun Gai](https://www.semanticscholar.org/author/2385564054)** (3 papers) — Kun Gai's research focuses on embodied egocentric world simulation using 3D human motion and exogenous viewpoints, long-horizon consistent world generation via decoupled memory architectures, and enhancing video reasoning through adaptive test-time…
- **[Bin Zhu](https://www.semanticscholar.org/author/2337784762)** (3 papers) — Bin Zhu's research focuses on video world-action models for robotic manipulation, including unified frameworks for policy learning, video prediction, and action evaluation, as well as benchmarking trustworthiness and behavioral diagnostics of these models.
- **[Xintao Wang](https://www.semanticscholar.org/author/2305033532)** (3 papers) — Xintao Wang's WAM research focuses on long-horizon, consistent video world generation for embodied agents, developing memory architectures and geometry-aware representations to achieve robust egocentric simulation and customizable world evolution.
- **[Jiayi Luo](https://www.semanticscholar.org/author/2319302828)** (3 papers) — Research on video generation, including training-free KV cache policies for long-video consistency, physics-informed video generation via mixture-of-experts latent alignment, and closed-loop video world simulators for robotic manipulation.
- **[Cong Wang](https://www.semanticscholar.org/author/2269795155)** (3 papers) — Cong Wang's research focuses on advancing video generation, particularly in identity-consistent video generation under large viewpoint changes, improving long-video consistency with training-free KV cache policies, and enhancing physical plausibility through…
- **[Xuanchi Ren](https://www.semanticscholar.org/author/2271992289)** (3 papers) — Xuanchi Ren's research focuses on generative world models for simulation and physical AI, including real-time closed-loop autonomous driving simulation, multi-agent interactive simulation, and omnimodal world models that jointly process vision, language…
- **[Dongxiu Liu](https://www.semanticscholar.org/author/2340937401)** (3 papers) — Dongxiu Liu's research focuses on developing efficient Vision-Language-Action (VLA) models for robotics, including quantization techniques (Ω-QVLA) for memory reduction, pretraining methods for zero-shot real-robot behavior (Wall-OSS-0.5), and multimodal…
- **[Ye Li](https://www.semanticscholar.org/author/2310388004)** (3 papers) — Ye Li focuses on efficient and scalable inference for Vision-Language-Action models and video world simulators for robotic manipulation, as well as long video extrapolation through recursive context management.
- **[Bohan Zhuang](https://www.semanticscholar.org/author/3194022)** (3 papers) — Developing video-based world models with a focus on latent spatial memory for efficient scene representation, comprehensive benchmarking for physical faithfulness and interaction fidelity, and recursive context allocation for long video extrapolation.
- **[Yann LeCun](https://www.semanticscholar.org/author/2270469816)** (3 papers) — Yann LeCun's WAM research focuses on developing and unifying world models for robotics and planning, including object-centric world models with diffusion policies for multi-stage tasks, and theoretical analysis of joint embedding predictive architectures…
- **[Yixiao Chen](https://www.semanticscholar.org/author/2375412354)** (3 papers) — Research on world action models, vision-language-action models, and video-language models, with a focus on model compression and efficiency through distillation and quantization, as well as improving spatial-temporal reasoning.
- **[Xiaotong Zhao](https://www.semanticscholar.org/author/2290452230)** (3 papers) — Xiaotong Zhao's research focuses on controllable and evaluative video generation, including developing frameworks for professional cinematic video evaluation (EvalVerse), interactive video world models with object-level control (WorldCraft), and…
- **[Alan Zhao](https://www.semanticscholar.org/author/2346976453)** (3 papers) — Alan Zhao's research focuses on controllable video generation, evaluation, and interactive control, including pipeline-aware benchmarking for professional cinematic video generation, extending interactive video world models to object-level trajectory control…
- **[Xuelong Li](https://www.semanticscholar.org/author/2336880377)** (3 papers) — Research focuses on video generation and editing, including improving geometric consistency in video generation through joint geometry-video modeling, photorealistic video object insertion with closed-loop feedback, and physics-grounded multi-object scene…
- **[Jiancheng Zhao](https://www.semanticscholar.org/author/2325368986)** (3 papers) — Jiancheng Zhao researches interactive video world models and long video generation, with a focus on FPS games and multi-entity control. Their work includes SCOPE for cross-game generalization in FPS, Incantation for natural-language-driven world models, and…
- **[Arash Akbari](https://www.semanticscholar.org/author/2273976196)** (3 papers) — Arash Akbari's research focuses on improving world-action models (WAM) for Physical AI, including physics-faithful video generation, modality-aware distillation for efficient inference, and sub-4-bit quantization for deploying vision-language-action models.
- **[Arman Akbari](https://www.semanticscholar.org/author/2273976198)** (3 papers) — Arman Akbari's research focuses on improving the efficiency and physical plausibility of world-action models (WAMs) and vision-language-action (VLA) models for Physical AI, including post-training for video generation world models, modality-aware distillation…

## 📰 Embodied / Physical-AI News
- [Why physical AI 2.0 needs a reality check](https://www.therobotreport.com/why-physical-ai-2-0-needs-reality-check/) — _The Robot Report_
- [Build real agentic apps using CUGA: two dozen working examples on a lightweight harness](https://huggingface.co/blog/ibm-research/cuga-apps) — _Hugging Face - Blog_
- [Shipping huggingface_hub every week with AI, open tools, and a human in the loop](https://huggingface.co/blog/huggingface-hub-release-ci) — _Hugging Face - Blog_
- [NVIDIA releases Halos, a full-stack safety system for robotics](https://www.therobotreport.com/nvidia-releases-halos-a-full-stack-safety-system-for-robotics/) — _The Robot Report_
- [Cobot’s Proxie Gen 2 robot adds autotasking, mobile manipulation](https://www.therobotreport.com/cobots-proxie-gen-2-robot-adds-autotasking-mobile-manipulation/) — _The Robot Report_
- [PP-OCRv6 on Hugging Face: 50-Language OCR from 1.5M to 34.5M Parameters](https://huggingface.co/blog/PaddlePaddle/pp-ocrv6) — _Hugging Face - Blog_
- [FORT and NVIDIA launch AI-driven Outside-In Safety blueprint](https://www.therobotreport.com/fort-and-nvidia-launch-ai-driven-outside-in-safety-blueprint/) — _The Robot Report_
- [How Intrinsic eliminates manual robot coding](https://www.therobotreport.com/how-intrinsic-eliminates-manual-robot-coding/) — _The Robot Report_
- [Bear Robotics acquires Kinisi Robotics to boost its physical AI capabilities](https://www.therobotreport.com/bear-robotics-acquires-kinisi-robotics-to-boost-its-physical-ai-capabilities/) — _The Robot Report_
- [Eclipse Automation launches RealitySync simulation platform](https://www.therobotreport.com/eclipse-automation-launches-realitysync-simulation-platform/) — _The Robot Report_
- [We got local models to triage the OpenClaw repo for FREE!*](https://huggingface.co/blog/local-models-pr-triage) — _Hugging Face - Blog_
- [Güdel to show grinding beyond stationary robots with vertical, horizontal motion at Automate 2026](https://www.therobotreport.com/gudel-to-showcase-grinding-beyond-stationary-robots-integrated-vertical-horizontal-motion-automate/) — _The Robot Report_
- [Defense manufacturing readiness hinges on autonomous finishing, says GrayMatter Robotics](https://www.therobotreport.com/defense-manufacturing-readiness-hinges-autonomous-surface-prep-says-graymatter/) — _The Robot Report_
- [U.S. robotics industry saw double-digit growth in 2025, says IFR](https://www.therobotreport.com/u-s-robotics-industry-saw-double-digit-growth-in-2025-says-ifr/) — _The Robot Report_
- [Elmo releases new motion controller and servo drives for industrial applications](https://www.therobotreport.com/elmo-releases-new-motion-controller-servo-drives-industrial-applications/) — _The Robot Report_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
