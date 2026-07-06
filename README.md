# Awesome-Embodied&MM

> Auto-updated (daily) intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-07-06 · **Tracked:** 470 core · 445 adjacent ·
214 news · **12385** benchmark rows across **4822** model
variants · **30** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **Miscellaneous** | 460 | 📈 rising | Covers outlier papers on topics including human-robot interaction, tactile sensing, multi-agent systems, medical… |
| **Controllable Video Generation and World Simulation** | 64 | ➡️ steady | Develops methods for controllable video generation with explicit control over camera, object motion, and scene… |
| **Evaluation Benchmarks and Diagnostics for World Models** | 60 | ➡️ steady | Proposes benchmarks and diagnostic frameworks for evaluating world models, VLAs, and video generation across dimensions… |
| **World Models for Navigation and Autonomous Driving** | 50 | ➡️ steady | Applies world models and VLA frameworks to navigation and autonomous driving, focusing on trajectory planning, safety… |
| **VLA Policy Improvement and Fine-Tuning** | 47 | 📈 rising | Improves VLA policies through reinforcement learning, preference optimization, test-time adaptation, and structured… |
| **Efficient Inference and Deployment of Generative Models** | 47 | ➡️ steady | Focuses on accelerating inference, quantization, and deployment of video generation and world models for real-time or… |
| **Physics-Grounded and Causal World Modeling** | 40 | 📈 rising | Integrates physical principles, causal reasoning, and geometric constraints into world models for more accurate and… |
| **Vision-Language-Action Model Training and Adaptation** | 36 | 📈 rising | Explores training recipes, fine-tuning strategies, and adaptation methods for Vision-Language-Action models, including… |
| **Safety, Robustness, and Verification in Embodied AI** | 36 | ➡️ steady | Addresses safety, robustness, and formal verification of world models and VLA policies, including adversarial attacks… |
| **Memory and Long-Horizon Consistency in World Models** | 33 | ➡️ steady | Addresses memory mechanisms for maintaining consistency over long horizons in world models and video generation… |
| **World Action Models for Robotic Manipulation** | 32 | 📈 rising | Develops world action models that jointly predict future states and actions for robotic manipulation, emphasizing… |
| **Latent World Models and Representation Learning** | 27 | 📈 rising | Studies latent-space world models, representation learning, and predictive architectures for efficient planning and… |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **8.23** | Flash-WAM: Modality-Aware Distillation for World Action Models | 2026-06-03 | spd 9 · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2606.05254) · [pdf](https://arxiv.org/pdf/2606.05254v1) |
| **7.79** | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models | 2026-06-24 | spd 8 · gen 4 · spec 8 · cost 7 | [abs](https://arxiv.org/abs/2606.25473) · [pdf](https://arxiv.org/pdf/2606.25473v1) · [code](https://github.com/NVlabs/rcm) |
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
| **7.44** | ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies | 2026-06-30 | spd 8 · gen 4 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.31132) · [pdf](https://arxiv.org/pdf/2606.31132v1) |
| **7.38** | Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation | 2026-06-01 | spd 5 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.02486) · [pdf](https://arxiv.org/pdf/2606.02486v1) |
| **7.38** | Wall-OSS-0.5 Technical Report | 2026-05-29 | spd – · gen 8 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.30877) · [pdf](https://arxiv.org/pdf/2605.30877v2) · [code](https://github.com/X-Square-Robot/wall-x) |
| **7.37** | EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies | 2026-06-18 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.20092) · [pdf](https://arxiv.org/pdf/2606.20092v1) |
| **7.36** | SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models | 2026-05-30 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.00664) · [pdf](https://arxiv.org/pdf/2606.00664v1) |
| **7.36** | ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? | 2026-06-17 | spd 7 · gen 6 · spec 6 · cost 8 | [abs](https://arxiv.org/abs/2606.19531) · [pdf](https://arxiv.org/pdf/2606.19531v1) · [code](https://github.com/yuyangalin/ImageWAM) |
| **7.35** | Colosseum V2: Benchmarking Generalization for Vision Language Action Models | 2026-05-26 | spd – · gen 8 · spec – · cost – | [abs](https://arxiv.org/abs/2605.27759) · [pdf](https://arxiv.org/pdf/2605.27759v1) |
| **7.33** | DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World | 2026-06-10 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.11901) · [pdf](https://arxiv.org/pdf/2606.11901v1) · [code](https://github.com/isaac-sim/IsaacSim) |
| **7.33** | dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models | 2026-06-22 | spd – · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.23623) · [pdf](https://arxiv.org/pdf/2606.23623v1) |
| **7.33** | Long-term Traffic Simulation via Structured Autoregressive Modeling | 2026-06-30 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.31209) · [pdf](https://arxiv.org/pdf/2606.31209v1) |
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

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _1425 results_

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

#### CALVIN  ·  _89 results_

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

#### RoboTwin  ·  _325 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LingBot-VA | — | per-chunk latency | 8100.0 | authors |
| WAM4D _(RoboTwin 2.0)_ | — | inference latency | 525.43 | authors |
| Fast-WAM _(RoboTwin 2.0)_ | — | inference latency | 425.53 | 3rd-party |
| Flash-WAM _(LingBot-VA)_ | — | per-chunk latency | 348.0 | authors |
| IRASim _(RoboTwin 2.0)_ | Overall | FVD | 126.2 | authors |
| HY-VLA | place_empty_cup | success rate | 100.0 | authors |
| π0.5 _(RoboTwin2.0)_ | Grab Roller | success rate | 98.6 | authors |
| Ours _(RoboTwin 2.0 demonstration data (50 per task, easy setting))_ | S3 (Lift Pot) | success rate | 97.0 | authors |
| StaKe _(RoboTwin 2.0 (50 demos per task))_ | Adjust Bottle | success rate | 96.0 | authors |
| SANTS _(RoboTwin 2.0 + real-robot data)_ | — | success rate | 94.4 | authors |

#### SimplerEnv  ·  _148 results_

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

#### RLBench  ·  _42 results_

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

#### Meta-World  ·  _31 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| SWAAP _(fine-tuned on 5000 transitions with 10% poisoned, α=0.9)_ | push | return | 1641.0 | authors |
| VICX _(Meta-World (drawer-open, reach, basketball))_ | coffee-button | success rate | 100.0 | authors |
| LA4VLA-1B _(LA4-33K + LA-33K-V (MixPT))_ | — | success rate | 87.53 | authors |
| ProgVLA (0.1B) _(Meta-World MT50)_ | — | success rate | 78.5 | authors |
| SmolVLA (2.25B) | — | success rate | 68.24 | 3rd-party |
| SmolVLA + VLA-Corrector _(MetaWorld)_ | — | success rate | 66.65 | authors |
| π0.5 | MT50 | success rate | 65.4 | authors |
| π0.5 + VLA-Corrector _(MetaWorld)_ | — | success rate | 64.35 | authors |
| SmolVLA _(MetaWorld)_ | — | success rate | 61.9 | authors |
| X-VLA + VLA-Corrector _(MetaWorld)_ | — | success rate | 59.6 | authors |

#### ManiSkill  ·  _53 results_

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

#### RoboCasa  ·  _129 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Cosmos-Policy | Turn Off Microwave | success rate | 100.0 | authors |
| Z-1 RL _(RoboCasa demonstrations)_ | Door | success rate | 97.0 | authors |
| Z-1 SFT _(RoboCasa demonstrations)_ | Door | success rate | 93.2 | authors |
| X-WAM | — | success rate | 79.2 | 3rd-party |
| ACE-EGO-0 _(Mixed robot demonstrations and egocentric human videos (6.0K+ hours))_ | — | average success | 72.8 | authors |
| GR00T-N1.5 _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.7 | authors |
| Late Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.0 | authors |
| Early Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 69.7 | authors |
| ZR-0 _(ProcCorpus-60M)_ | — | success rate | 69.3 | authors |
| Spatial Forcing _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 68.3 | authors |

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

#### ALFWorld  ·  _6 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GIGPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 90.4 | authors |
| GRPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 77.9 | authors |
| FQE _(πb trajectories (Llama-3.1-8B-Instr.))_ | iter1 policy | Spearman ρ | 0.82 | 3rd-party |
| ADWM _(πb trajectories (Llama-3.1-8B-Instr.))_ | iter3 policy | Spearman ρ | 0.8 | authors |

#### VBench  ·  _687 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Wan-I2V | Cut & Drag | Flow-Err | 181.1 | 3rd-party |
| GWTF | Cut & Drag | Flow-Err | 152.81 | 3rd-party |
| PTQ4DiT | — | FVD-FP | 124.2 | authors |
| Q-ARVD | — | FVD-FP | 116.26 | authors |
| Wan-T2V | T2V Motion Transfer | Flow-Err | 103.26 | 3rd-party |
| TTM | Cut & Drag | Flow-Err | 102.39 | 3rd-party |
| ϕ-Noise | Cut & Drag | Flow-Err | 101.49 | authors |
| LongLive (Vanilla) | — | KV Cache | 100.0 | authors |
| Reward (Vanilla) | — | KV Cache | 100.0 | authors |
| Krea (Vanilla) | — | KV Cache | 100.0 | authors |

#### AgiBot / GENIE  ·  _21 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Egocentric (ours) _(HumanNet (egocentric portion, 5000h subset))_ | Seen tasks (in-distribution) | success rate | 92.5 | authors |
| Reward as an Agent | — | Overall Accuracy | 91.0 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | Scene Consistency | 90.41 | authors |
| PAIWorld _(AgiBot-World, RoboMIND, Galaxea, RoboTwin, RoboCOIN (2.5M clips))_ | — | EWMScore | 82.45 | authors |
| Wan2.2 (no pretraining) | Seen tasks (in-distribution) | success rate | 40.0 | authors |
| ViPSim(DiT) _(AgiBotWorld-Beta)_ | — | PSNR | 20.35 | authors |
| ViPSim(UNet) _(AgiBotWorld-Beta)_ | — | PSNR | 18.42 | authors |
| EnerVerse-AC | — | PSNR | 17.93 | 3rd-party |
| ViPSim(DiT) _(AgiBotWorld-Beta)_ | — | Overall | 5.5697 | authors |
| ViPSim(UNet) _(AgiBotWorld-Beta)_ | — | Overall | 5.4291 | authors |

#### Habitat  ·  _10 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ViewCrafter | sparse views-to-video | FVD | 778.207 | 3rd-party |
| TrajectoryCrafter | sparse views-to-video | FVD | 690.322 | 3rd-party |
| GEN3C | sparse views-to-video | FVD | 511.039 | 3rd-party |
| Pantheon360 _(360-1M (filtered))_ | sparse views-to-video | FVD | 450.696 | authors |
| multiple (LLaVA-1.6, GPT-4V, Gemini-1.5-Pro, InternVL2, OpenVLA) | — | success rate relative to oracle | 94.2 | authors |
| Gemini-1.5-Pro | — | PIB (bits) | 1.05 | authors |
| CoFL-S _(R2R-CE + RxR-CE training episodes (augmented with instruction-diverse slots from Fine-Grained R2R and Landmark RxR))_ | — | success rate (SR) | 0.43 | authors |
| Action Chunk _(R2R-CE + RxR-CE training episodes (same matched training))_ | — | success rate (SR) | 0.3 | 3rd-party |
| Action Token _(R2R-CE + RxR-CE training episodes (same matched training))_ | — | success rate (SR) | 0.25 | 3rd-party |

#### BEHAVIOR  ·  _31 results_

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

#### nuScenes  ·  _187 results_

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

#### NAVSIM  ·  _64 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ours† _(OpenScene (NAVSIM train split))_ | planning | Comf. | 100.0 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | NC | 98.7 | authors |
| SafeAlign-VLA _(NAVSIM navtrain)_ | trajectory planning | NC | 98.6 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | DAC | 98.2 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | TTC | 95.9 | authors |
| ForgeDrive _(NAVSIM/nuPlan)_ | — | Driving Command Accuracy | 94.7 | authors |
| RAP _(NAVSIM trainval)_ | — | PDMS | 93.8 | 3rd-party |
| LWDrive _(Impromptu dataset (adaptation stage))_ | — | PDMS | 92.0 | authors |
| Ours-Rep+Geo+MCB _(OpenScene (NAVSIM train split))_ | planning (frozen tokenizer + lightweight decoder) | PDMS | 91.8 | authors |
| Ours† _(OpenScene (NAVSIM train split))_ | planning | PDMS | 91.8 | authors |

#### Bench2Drive  ·  _64 results_

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

#### DAVIS  ·  _61 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| TrajectoryCrafter | 10 ReCamMaster camera trajectory types | RotErr | 10.434 | 3rd-party |
| CogNVS | 10 ReCamMaster camera trajectory types | RotErr | 6.9499 | 3rd-party |
| Recammaster _(synthetic (Unreal Engine))_ | 10 ReCamMaster camera trajectory types | RotErr | 2.3175 | 3rd-party |
| Redirector _(synthetic)_ | 10 ReCamMaster camera trajectory types, speed=2.0 | RotErr | 1.9246 | 3rd-party |
| Ours _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types, speed=2.0 | RotErr | 1.8821 | authors |
| MVTrack4Gen ReCamMaster _(Kubric + MultiCamVideo)_ | — | mRotErr | 1.858 | authors |
| MVTrack4Gen Redirector _(Kubric + MultiCamVideo)_ | — | mRotErr | 1.718 | authors |
| Full reward (Geo-Align) _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types | RotErr | 1.3895 | authors |
| MVTrack4Gen Redirector _(Kubric + MultiCamVideo)_ | — | Motion Smoothness | 0.986 | authors |
| MVTrack4Gen ReCamMaster _(Kubric + MultiCamVideo)_ | — | Motion Smoothness | 0.984 | authors |

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

#### Real-world  ·  _49 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| InSight _(50 human scooping demonstrations + acquired lateral-push primitive)_ | sweeping | success rate | 100.0 | authors |
| OASIS | Goal | success rate | 98.6 | authors |
| InSight _(50 human pick-and-place demonstrations + 20 successful pour primitives)_ | pour beans into bowl | success rate | 96.0 | authors |
| 3DThinkVLA (Ours) _(VLA data + 3D reasoning data (co-training))_ | Transparent container placement | success rate | 93.3 | authors |
| InSight _(50 human pick-and-place demonstrations + 20 successful twist primitives)_ | twist cap open | success rate | 92.0 | authors |
| MaskWAM | language-ambiguous tasks (ID + OOD) | success rate | 84.9 | authors |
| π0.5 | Average (Goal, Spatial, Long) | success rate | 81.6 | 3rd-party |
| Afford-VLA _(LIBERO + Affordance dataset)_ | Cup-to-Plate | Success rate | 80.0 | authors |
| VLAJS (zero-shot) | Pick & Place | success rate | 80.0 | authors |
| RepWAM-5B _(AgiBot, RoboMIND, RoboCOIN, InternA1)_ | Push drawer | success rate | 80.0 | authors |

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
- **Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends** — The paper systematically identifies and categorizes three crucial technical challenges for interactive world modeling: action-conditioned controllability, long-horizon interactions and memory, and action-following responsiveness for real-time interactivity. _(→ WAM: World Action Models fundamentally rely on action-conditioned state transitions. Addressing these three identified challenges—ensuring actions reliably control state evolution, maintaining coherent long-term memory across extended action sequences, and…)_ [abs](https://arxiv.org/abs/2606.01164) · [pdf](https://arxiv.org/pdf/2606.01164v1) · [code](https://github.com/liujiuming123/Awesome-Interactive-World-Model)
- **Coarse-to-Fine Compositional Diffusion for Long-Horizon Planning** — Coarse-to-Fine Compositional Diffusion (CoFi) separates global structure formation from local detail refinement during inference-time compositional generation. It first aligns local denoised estimates around a shared coarse scaffold capturing long-range task-level arrangement, then diffuses this scaffold to an… _(→ WAM: World Action Models must generate long-horizon action sequences or world-state trajectories that are both globally coherent (the overall plan makes sense) and locally precise (each step's actions are physically valid). CoFi's coarse-to-fine composition…)_ [abs](https://arxiv.org/abs/2606.00837) · [pdf](https://arxiv.org/pdf/2606.00837v1) · [code](https://github.com/KAIST-Visual-AI-Group/SyncDiffusion)

## 👥 Influential Authors & Groups
- **[Xiaozhu Ju](https://www.semanticscholar.org/author/2392718853)** (6 papers) — Xiaozhu Ju focuses on safe and robust world action models for embodied agents, integrating world models with reinforcement learning and vision-language-action policies to improve safety, generalization, and physical fidelity.
- **[Xiaofeng Wang](https://www.semanticscholar.org/author/2242976725)** (6 papers) — Focuses on embodied world models and visual navigation, developing unified latent world-action models that jointly generate actions and visual foresight, as well as decoupling semantic reasoning from continuous action generation for aerial and robotic…
- **[Yao Mu](https://www.semanticscholar.org/author/2348161293)** (6 papers) — Yao Mu's research focuses on advancing Vision-Language-Action (VLA) models for robotic manipulation, particularly enhancing bimanual dexterity, safety evaluation, humanoid control, and efficient action prediction through diffusion models and equilibrium…
- **[A. T. Le](https://www.semanticscholar.org/author/2282564821)** (6 papers) — Research on Vision-Language-Action (VLA) models, focusing on inference runtime optimization, structured evaluation, robustness via diffusion noise, fine-tuning efficiency through layer redundancy, rotationally equivariant architectures, and data-efficient…
- **[D. M. H. Nguyen](https://www.semanticscholar.org/author/2374196339)** (6 papers) — Research on Vision-Language-Action (VLA) models, including efficient inference, robustness, fine-tuning, equivariance, and few-shot adaptation.
- **[Xiaowei Chi](https://www.semanticscholar.org/author/2192825554)** (6 papers) — Xiaowei Chi focuses on developing world action models (WAMs) for robot manipulation, integrating vision, tactile sensing, and reinforcement learning to improve safety, efficiency, and generalization under distribution shifts.
- **[Shanghang Zhang](https://www.semanticscholar.org/author/2346116279)** (6 papers) — Shanghang Zhang's research focuses on safe reinforcement learning for vision-language-action (VLA) policies, interactive world models that combine kinematic and physical reasoning, and joint optimization of world and action models to improve robot…
- **[Andrea V. Bajcsy](https://www.semanticscholar.org/author/47370841)** (5 papers) — Andrea V. Bajcsy's research focuses on improving robot control policies at inference time through adaptive test-time compute allocation, steering of world models and vision-language-action models, and multi-modal policy steering using vision and touch, with…
- **[Yann LeCun](https://www.semanticscholar.org/author/2270469816)** (5 papers) — Yann LeCun's research focuses on developing world models for planning and control, particularly using self-supervised learning and latent variable models (JEPA) for robotics, sim-to-real transfer, and generalization.
- **[Xuelong Li](https://www.semanticscholar.org/author/2336880377)** (5 papers) — Xuelong Li's research focuses on controllable video generation, including autoregressive video generation with compositional human-camera control, real-time streaming avatar video generation, photorealistic video object insertion, geometric consistency in…
- **[Enze Xie](https://www.semanticscholar.org/author/41020000)** (5 papers) — This author's research focuses on accelerating video generation and world models for robotic manipulation, with an emphasis on training-free inference optimization, physical consistency enhancement, and efficient long-video infrastructure. Key contributions…
- **[Zheng Zhu](https://www.semanticscholar.org/author/2265968976)** (5 papers) — Zheng Zhu's research centers on developing efficient world-action models for embodied AI, focusing on disentangling dynamics learning from visual synthesis, using latent diffusion transformers to jointly generate actions and visual foresight, and accelerating…
- **[Hangjun Ye](https://www.semanticscholar.org/author/2384401186)** (5 papers) — 专注于世界-动作建模（WAM）和视觉-语言-动作（VLA）模型的统一框架，应用于自动驾驶、导航和操纵任务，同时探索社会智能与理论心智推理。
- **[Xinyuan Song](https://www.semanticscholar.org/author/2384121658)** (5 papers) — Research focuses on integrating world models with language agents, including reducing hallucination propagation, repairing world-model planning graphs, budgeted environment probing for calibration, analyzing world-model collapse as a phase transition, and…
- **[Z. Cai](https://www.semanticscholar.org/author/48569716)** (5 papers) — Z. Cai researches grounded language planning and world-model calibration for long-horizon LLM agents, focusing on reducing hallucination propagation, repairing world-model graphs through causal correction, and understanding rollout errors and phase…
- **[Haoqi Yuan](https://www.semanticscholar.org/author/1429192914)** (5 papers) — Haoqi Yuan's research focuses on building foundation models for robotic manipulation, including vision-language-action models (VLA), tactile pre-training, and world models, that can generalize across diverse tasks, environments, and robot embodiments.
- **[Peidong Jia](https://www.semanticscholar.org/author/101105478)** (5 papers) — Peidong Jia's research focuses on world action models (WAMs) for robotics, integrating vision, tactile sensing, and interactive world models to improve safe reinforcement learning, contact-rich manipulation, and long-horizon embodied tasks.
- **[Pengfei Wan](https://www.semanticscholar.org/author/2363570130)** (4 papers · null) — Pengfei Wan's research focuses on video world models and long-horizon video generation, with emphasis on memory architectures, geometric consistency, and adaptive test-time optimization to extend temporal coherence and reasoning in video generation.
- **[Kun Gai](https://www.semanticscholar.org/author/2385564054)** (4 papers) — Kun Gai's research focuses on long-horizon consistent video generation and world modeling, with innovations in memory architectures (DecMem, MemLearner), adaptive test-time optimization for video reasoning (VLMs as teachers), and egocentric world simulation…
- **[Xintao Wang](https://www.semanticscholar.org/author/2305033532)** (4 papers) — Research focuses on long-horizon consistent video world models through advanced memory mechanisms, including decoupled memory (Sparse Global Memory and Anchored Local Memory), geometry-aware implicit memory for 3D scene structure distillation, and…
- **[Sanja Fidler](https://www.semanticscholar.org/author/2261282058)** (4 papers) — Sanja Fidler's research focuses on generative world models for physical AI, including multi-agent simulation, humanoid loco-manipulation, autonomous vehicle simulation, and omnimodal world models that integrate language, image, video, audio, and action…
- **[Bohan Zhuang](https://www.semanticscholar.org/author/3194022)** (4 papers) — Research focuses on advancing long video generation and world models by addressing key challenges such as infinite-length, error-free, and identity-consistent video synthesis, incorporating causal attention, key-value caching, truncated-rectified flow, and…
- **[Randall Balestriero](https://www.semanticscholar.org/author/2378151189)** (4 papers) — Randall Balestriero's WAM research focuses on developing world models for planning and control, including joint embedding predictive architectures (JEPAs) for robotics, sensorimotor representations for action, and open-source platforms for reproducible world…
- **[Jie Huang](https://www.semanticscholar.org/author/2362441710)** (4 papers) — Research on efficient autoregressive video generation, focusing on memory mechanisms (evolving memory, KV cache compression) and real-time streaming at high resolutions.
- **[Jingjing Gong](https://www.semanticscholar.org/author/2371292918)** (4 papers) — Jingjing Gong's research focuses on advancing Vision-Language-Action (VLA) models for robotic control, including in-context world modeling for adaptation, efficient one-step action generation, coarse-to-control planning for long-horizon tasks, and…

## 📰 Embodied / Physical-AI News
- [LeRobot v0.6.0: Imagine, Evaluate, Improve](https://huggingface.co/blog/lerobot-release-v060) — _Hugging Face - Blog_
- [PRX Part 4: Our Data Strategy](https://huggingface.co/blog/Photoroom/prx-part4-data) — _Hugging Face - Blog_
- [🤗 Kernels: Major Updates](https://huggingface.co/blog/revamped-kernels) — _Hugging Face - Blog_
- [Humanoid says KinetIQ Ascend reinforcement learning approaches human-level dexterity](https://www.therobotreport.com/humanoid-announces-kinetiq-ascend-reinforcement-learning-approach/) — _The Robot Report_
- [Context is king: How Avride uses cloud VLMs as a safety net for delivery robots](https://www.therobotreport.com/how-avride-uses-cloud-vlms-safety-net-delivery-robots/) — _The Robot Report_
- [Japan Pioneered Humanoid Robots—Can It Now Catch China?](https://spectrum.ieee.org/humanoid-robots-japan) — _IEEE Spectrum_
- [Quarterhill discusses transport modernization as U.S. marks 70 years of federal highways](https://www.therobotreport.com/quarterhill-discusses-transport-modernization-u-s-marks-70-years-federal-highways/) — _The Robot Report_
- [Video Friday: An Earthbound Mars Rover for the Moon](https://spectrum.ieee.org/video-friday-nasa-lunar-rover) — _IEEE Spectrum_
- [Why you should combine robot dexterity with mechanical positioning for complex assembly operations](https://www.therobotreport.com/why-you-should-combine-robot-dexterity-with-mechanical-positioning-for-complex-assembly-operations/) — _The Robot Report_
- [Luxonis closes Series A round to scale physical AI perception layer](https://www.therobotreport.com/luxonis-closes-series-a-round-to-scale-physical-ai-perception-layer/) — _The Robot Report_
- [Blattner awards Built Robotics $75M contract for physical AI to help meet energy demand](https://www.therobotreport.com/blattner-awards-built-robotics-75m-contract-meet-energy-demands/) — _The Robot Report_
- [Automate 2026 show recap](https://www.therobotreport.com/automate-2026-show-recap/) — _The Robot Report_
- [Apptronik unveils Apollo 2 and a flagship data collection and training facility](https://www.therobotreport.com/apptronik-unveils-apollo-2-flagship-data-collection-training-facility/) — _The Robot Report_
- [Hugging Face and Cerebras bring Gemma 4 to real-time voice AI](https://huggingface.co/blog/cerebras-gemma4-voice-ai) — _Hugging Face - Blog_
- [In Robotics, Ruggedization Is No Longer Optional](https://www.therobotreport.com/in-robotics-ruggedization-is-no-longer-optional/) — _The Robot Report_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
