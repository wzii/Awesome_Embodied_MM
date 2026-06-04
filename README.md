# Awesome-Embodied&MM

> Daily-updated intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-06-04 · **Tracked:** 124 core · 154 adjacent ·
74 news · **3871** benchmark rows across **1612** model
variants · **25** authors

> Scoring: two layers — general (novelty/soundness/impact) + WAM-specific. Top-4 WAM metrics
> (inference **speed**, **gen**eralist, **spec**ialist, inference **cost**) are weighted 2×.
> `–` means the paper does not address that metric (we never fabricate a score).

## 📈 Trends & Popular Directions
| Direction | Papers | Momentum | Summary |
|-----------|-------:|----------|---------|
| **Miscellaneous** | 94 | 📈 rising | Papers that do not fit neatly into the other clusters, covering diverse topics such as affective computing, medical… |
| **Embedded and Interactive World Models for Agents** | 39 | 📈 rising | Focuses on world models that enable interactive, multi-modal agent behavior, including navigation, exploration, and… |
| **Safety and Robustness of VLA Models** | 28 | 📈 rising | Addresses safety, robustness, and trustworthiness of Vision-Language-Action models through benchmarks, defense… |
| **Benchmarking and Evaluation of World Models and VLAs** | 28 | 📈 rising | Develops benchmarks, diagnostic frameworks, and evaluation protocols for assessing world model and VLA capabilities… |
| **Reinforcement Learning and Planning with World Models** | 21 | 📈 rising | Combines world models with reinforcement learning, planning, and optimal control for decision-making in embodied and… |
| **Long-Horizon Video Generation and Memory Management** | 15 | 📈 rising | Focuses on generating long, consistent videos by addressing memory, retrieval, and context management across extended… |
| **Training-Free Video Editing and Control** | 15 | 📈 rising | Investigates training-free methods for controlled video generation, editing, and steering, often using latent… |
| **VLA Model Integration and Multimodal Interaction** | 15 | 📈 rising | Unifies vision, language, and action across embodiments and tasks, often through modular architectures, cross-task… |
| **Efficient and Scalable Video Generation** | 14 | 📈 rising | Explores methods to improve the efficiency, scalability, and speed of video generation, including pruning… |
| **Theory and Foundations of World Models** | 13 | 📈 rising | Develops theoretical foundations, architectural principles, and abstractions for world models, including causal… |
| **World Models for Robotics and Manipulation** | 12 | 📈 rising | Develops world models for robotic manipulation, including synthesis, planning, and evaluation of action-conditioned… |
| **World Models for Autonomous Driving** | 11 | 📈 rising | Applies world models to autonomous driving tasks, including planning, reasoning, and action-conditioned visual… |

## 🏆 Top World Action Model Papers
| Score | Paper | Published | Top-4 (spd·gen·spec·cost) | Links |
|------:|-------|-----------|---------------------------|-------|
| **7.57** | SANTS: A State-Adaptive Scheduler for World Action Models | 2026-05-27 | spd 8 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2605.27947) · [pdf](https://arxiv.org/pdf/2605.27947v1) |
| **7.48** | LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World | 2026-05-31 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458v1) |
| **7.46** | Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning | 2026-05-29 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.30795) · [pdf](https://arxiv.org/pdf/2605.30795v1) |
| **7.46** | Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments | 2026-05-28 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.30280) · [pdf](https://arxiv.org/pdf/2605.30280v2) · [code](https://github.com/QwenLM/Qwen-VLA) |
| **7.46** | Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance | 2026-05-22 | spd – · gen 7 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.24203) · [pdf](https://arxiv.org/pdf/2605.24203v1) |
| **7.44** | VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies | 2026-05-28 | spd 8 · gen 7 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2605.30011) · [pdf](https://arxiv.org/pdf/2605.30011v1) · [code](https://github.com/DCDmllm/VisualThink-VLA) |
| **7.38** | Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation | 2026-06-01 | spd 5 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.02486) · [pdf](https://arxiv.org/pdf/2606.02486v1) |
| **7.38** | Wall-OSS-0.5 Technical Report | 2026-05-29 | spd – · gen 8 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.30877) · [pdf](https://arxiv.org/pdf/2605.30877v2) · [code](https://github.com/X-Square-Robot/wall-x) |
| **7.36** | SKIP: Sparse Keyframe Interpolation Paradigm for Efficient Embodied World Models | 2026-05-30 | spd 7 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2606.00664) · [pdf](https://arxiv.org/pdf/2606.00664v1) |
| **7.35** | Colosseum V2: Benchmarking Generalization for Vision Language Action Models | 2026-05-26 | spd – · gen 8 · spec – · cost – | [abs](https://arxiv.org/abs/2605.27759) · [pdf](https://arxiv.org/pdf/2605.27759v1) |
| **7.25** | SparseWorld: Enhancing End-to-End Autonomous Driving via World Models with Sparse Scene Representation | 2026-05-23 | spd – · gen 2 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2605.24354) · [pdf](https://arxiv.org/pdf/2605.24354v1) |
| **7.25** | DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions | 2026-05-20 | spd 5 · gen 4 · spec 8 · cost 6 | [abs](https://arxiv.org/abs/2605.21273) · [pdf](https://arxiv.org/pdf/2605.21273v2) |
| **7.24** | Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR | 2026-05-19 | spd – · gen 5 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.19282) · [pdf](https://arxiv.org/pdf/2605.19282v1) |
| **7.23** | ProgVLA: Progress-Aware Robot Manipulation Skill Learning | 2026-05-27 | spd – · gen 6 · spec 7 · cost 8 | [abs](https://arxiv.org/abs/2605.28231) · [pdf](https://arxiv.org/pdf/2605.28231v1) |
| **7.22** | DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions | 2026-05-29 | spd – · gen 3 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2605.31271) · [pdf](https://arxiv.org/pdf/2605.31271v1) |
| **7.21** | ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models | 2026-05-28 | spd 8 · gen 6 · spec – · cost 8 | [abs](https://arxiv.org/abs/2605.29438) · [pdf](https://arxiv.org/pdf/2605.29438v1) |
| **7.18** | From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model | 2026-05-21 | spd – · gen 6 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.22671) · [pdf](https://arxiv.org/pdf/2605.22671v2) |
| **7.15** | Dexora: Open-source VLA for High-DoF Bimanual Dexterity | 2026-05-18 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.18722) · [pdf](https://arxiv.org/pdf/2605.18722v1) |
| **7.14** | FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies | 2026-05-26 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.27284) · [pdf](https://arxiv.org/pdf/2605.27284v1) · [code](https://github.com/NVIDIA/Isaac-GR00T) |
| **7.09** | World-Task Factorization for Robot Learning | 2026-06-01 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02027) · [pdf](https://arxiv.org/pdf/2606.02027v1) |
| **7.09** | EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models | 2026-05-25 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.25477) · [pdf](https://arxiv.org/pdf/2605.25477v1) |
| **7.08** | PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation | 2026-05-30 | spd – · gen 2 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.00515) · [pdf](https://arxiv.org/pdf/2606.00515v1) |
| **7.06** | MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models | 2026-05-28 | spd – · gen 5 · spec – · cost – | [abs](https://arxiv.org/abs/2605.29360) · [pdf](https://arxiv.org/pdf/2605.29360v1) |
| **7.02** | Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics | 2026-05-21 | spd – · gen 2 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.22164) · [pdf](https://arxiv.org/pdf/2605.22164v1) |
| **7.0** | Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation | 2026-05-26 | spd – · gen 8 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.27582) · [pdf](https://arxiv.org/pdf/2605.27582v1) |
| **6.96** | Primitive Subspaces Mediate Few-Shot Transfer in VLAs | 2026-05-29 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.30695) · [pdf](https://arxiv.org/pdf/2605.30695v1) |
| **6.89** | Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation | 2026-05-20 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.20811) · [pdf](https://arxiv.org/pdf/2605.20811v1) |
| **6.87** | $τ_0$-WM: A Unified Video-Action World Model for Robotic Manipulation | 2026-05-31 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.01027) · [pdf](https://arxiv.org/pdf/2606.01027v1) |
| **6.87** | GEM: Generative Supervision Helps Embodied Intelligence | 2026-05-27 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.28548) · [pdf](https://arxiv.org/pdf/2605.28548v1) · [code](https://github.com/starVLA/starVLA) |
| **6.87** | DEFLECT: Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning for VLA Policies | 2026-05-19 | spd 7 · gen 5 · spec 6 · cost – | [abs](https://arxiv.org/abs/2605.19294) · [pdf](https://arxiv.org/pdf/2605.19294v1) |
| **6.87** | Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models | 2026-05-18 | spd 7 · gen 6 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.18601) · [pdf](https://arxiv.org/pdf/2605.18601v1) · [code](https://github.com/zhushangwen/Incantation) |
| **6.81** | Turning Video Models into Generalist Robot Policies | 2026-05-27 | spd – · gen 7 · spec 6 · cost – | [abs](https://arxiv.org/abs/2605.27817) · [pdf](https://arxiv.org/pdf/2605.27817v1) |
| **6.79** | Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models | 2026-05-29 | spd 7 · gen 4 · spec 6 · cost 7 | [abs](https://arxiv.org/abs/2605.31158) · [pdf](https://arxiv.org/pdf/2605.31158v1) |
| **6.79** | GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation | 2026-05-20 | spd 6 · gen 6 · spec 7 · cost 7 | [abs](https://arxiv.org/abs/2605.20752) · [pdf](https://arxiv.org/pdf/2605.20752v2) · [code](https://github.com/TuojingAI/GaussianDream) |
| **6.78** | Theoretical Foundations and Effective Algorithms for Policy-Aware Simulator Learning | 2026-05-27 | spd – · gen 3 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.29032) · [pdf](https://arxiv.org/pdf/2605.29032v1) |
| **6.78** | World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks | 2026-05-19 | spd – · gen 5 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.19957) · [pdf](https://arxiv.org/pdf/2605.19957v1) · [code](https://github.com/ZGCA-HMI-Lab/WEM) |
| **6.76** | Lagrangian Perturbation Diffusion Steering: Latent Reinforcement Learning for Generative Policies | 2026-05-31 | spd – · gen 5 · spec 7 · cost 6 | [abs](https://arxiv.org/abs/2606.01151) · [pdf](https://arxiv.org/pdf/2606.01151v1) |
| **6.76** | LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model | 2026-05-21 | spd 3 · gen 2 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.22089) · [pdf](https://arxiv.org/pdf/2605.22089v1) · [code](https://github.com/Thinklab-SJTU/Bench2Drive) |
| **6.75** | OneVLA: A Unified Framework for Embodied Tasks | 2026-05-31 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.01241) · [pdf](https://arxiv.org/pdf/2606.01241v1) · [code](https://github.com/linglingxiansen/OneVLA) |
| **6.71** | SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation | 2026-05-28 | spd 7 · gen 4 · spec 6 · cost 6 | [abs](https://arxiv.org/abs/2605.29662) · [pdf](https://arxiv.org/pdf/2605.29662v1) |
| **6.71** | E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control | 2026-05-25 | spd – · gen 2 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.26316) · [pdf](https://arxiv.org/pdf/2605.26316v1) · [code](https://github.com/facebookresearch/nwm) |
| **6.71** | SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models | 2026-05-22 | spd – · gen 5 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.23345) · [pdf](https://arxiv.org/pdf/2605.23345v2) |
| **6.67** | World Models for Robotic Manipulation: A Survey | 2026-05-27 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.00113) · [pdf](https://arxiv.org/pdf/2606.00113v1) |
| **6.65** | GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation | 2026-05-20 | spd – · gen 3 · spec 7 · cost 4 | [abs](https://arxiv.org/abs/2605.22882) · [pdf](https://arxiv.org/pdf/2605.22882v2) |
| **6.61** | Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models | 2026-05-21 | spd – · gen 7 · spec 6 · cost – | [abs](https://arxiv.org/abs/2605.22896) · [pdf](https://arxiv.org/pdf/2605.22896v1) |
| **6.61** | PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction | 2026-05-20 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.21414) · [pdf](https://arxiv.org/pdf/2605.21414v1) |
| **6.61** | RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models | 2026-05-19 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.19678) · [pdf](https://arxiv.org/pdf/2605.19678v1) · [code](https://github.com/HCPLab-SYSU/RoVLA) |
| **6.59** | Back to Parsimonious Latents: Learning Task-Centric World Models from Visual Foundations | 2026-05-25 | spd – · gen 5 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.25620) · [pdf](https://arxiv.org/pdf/2605.25620v1) |
| **6.59** | Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving | 2026-05-20 | spd – · gen 3 · spec 7 · cost 5 | [abs](https://arxiv.org/abs/2605.21139) · [pdf](https://arxiv.org/pdf/2605.21139v2) · [code](https://github.com/OpenDriveLab/OpenScene) |
| **6.58** | RoboDream: Compositional World Models for Scalable Robot Data Synthesis | 2026-06-01 | spd – · gen 6 · spec 6 · cost – | [abs](https://arxiv.org/abs/2606.02577) · [pdf](https://arxiv.org/pdf/2606.02577v1) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _405 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| OpenVLA-7B _(LIBERO)_ | — | I(X; X~) (attack channel capacity) | 5000.0 | authors |
| Wan 2.2 (chunked) _(LIBERO-90)_ | — | FVD | 4177.0 | 3rd-party |
| SimpleVLA-RL _(LIBERO)_ | Long | iterations to 90% success rate | 2450.0 | authors |
| ConfidenceVLA | — | avg inference time | 712.9 | 3rd-party |
| Agentic-VLA _(LIBERO)_ | Long | iterations to 90% success rate | 700.0 | authors |
| SKIP _(LIBERO-90)_ | — | FVD | 458.0 | authors |
| Pre-VLA _(PPO rollout trajectories from LIBERO with Critic-derived labels)_ | Overall (forward verification time per action chunk) | average forward verification time | 183.9 | authors |
| Omega-QVLA | Goal | success rate | 100.0 | authors |
| VLA-Hijack | Spatial | Failure Rate | 100.0 | authors |
| π0.5 _(LIBERO (per-suite finetuned))_ | — | success rate | 100.0 | authors |

#### CALVIN  ·  _52 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 99.5 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (1 task) | 99.3 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (2 tasks) | 96.6 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (2 tasks) | 95.9 | authors |
| VLM4VLA + Ours _(CALVIN ABC)_ | — | success rate (1 task) | 94.4 | authors |
| VLM4VLA _(CALVIN ABC)_ | — | success rate (1 task) | 93.4 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (3 tasks) | 91.2 | authors |
| FLOWER _(CALVIN ABC)_ | — | success rate (3 tasks) | 90.5 | authors |
| FLOWER + Ours _(CALVIN ABC)_ | — | success rate (4 tasks) | 86.9 | authors |
| VLM4VLA + Ours _(CALVIN ABC)_ | — | success rate (2 tasks) | 86.7 | authors |

#### RoboTwin  ·  _65 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| π0.5 _(RoboTwin2.0)_ | Grab Roller | success rate | 98.6 | authors |
| SANTS _(RoboTwin 2.0 + real-robot data)_ | — | success rate | 94.4 | authors |
| LingBot-VA | — | success rate | 92.2 | 3rd-party |
| Fast-WAM | — | success rate | 91.8 | 3rd-party |
| EvoScene-VLA _(RoboTwin)_ | 31 tasks | success rate | 89.1 | authors |
| π0.5-Key-Gram | Avg. 50 Tasks | success rate | 89.0 | authors |
| OpenVLA-OFT + Feat2Go | — | success rate | 88.8 | authors |
| DeMaVLA _(~5000 hours real-world dual-arm demonstrations)_ | — | average success rate | 88.42 | authors |
| Motus | — | success rate | 87.8 | 3rd-party |
| Qwen-VLA-Instruct _(Qwen-VLA pretraining mixture + SFT on multi-task and real-robot + RL on SimplerEnv)_ | — | success rate | 87.2 | authors |

#### SimplerEnv  ·  _58 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| OpenVLA-7b | Pick up | failure rate (FR) | 97.5 | authors |
| GR00T-N1.6 | Pick up | failed object coverage (FOC) | 97.1 | authors |
| Afford-VLA _(LIBERO + Affordance dataset)_ | Put Eggplant | Success rate | 96.8 | authors |
| EO-1 | Pick up | trajectory coverage (TC) | 84.0 | authors |
| GR00T-N1.6 | Pick up | trajectory coverage under failure (TCF) | 83.0 | authors |
| ElegantVLA _(CogACT)_ | Visual Matching | success rate | 77.59 | authors |
| SpatialVLA + Ours _(Bridge)_ | Eggplant | success rate | 75.0 | authors |
| ElegantVLA _(GR00T)_ | Google Robot | success rate | 75.0 | authors |
| CogACT | Visual Matching | success rate | 74.8 | 3rd-party |
| SAFE-Pruner | — | success rate | 74.5 | authors |

#### RLBench  ·  _25 results_

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

#### Meta-World  ·  _2 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ProgVLA (0.1B) _(Meta-World MT50)_ | — | success rate | 78.5 | authors |
| SmolVLA (2.25B) | — | success rate | 68.24 | 3rd-party |

#### ManiSkill  ·  _7 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| OpenVLA-OFT + Feat2Go | — | success rate | 82.9 | authors |
| OpenVLA-OFT + Steps-To-Go | — | success rate | 79.0 | 3rd-party |
| OpenVLA-OFT + PPO | — | success rate | 76.8 | 3rd-party |
| OpenVLA-OFT + GRPO | — | success rate | 58.3 | 3rd-party |
| π0.5 + SFT | — | success rate | 26.4 | 3rd-party |
| π0 + SFT | — | success rate | 18.1 | 3rd-party |
| OpenVLA-OFT + SFT | — | success rate | 17.5 | 3rd-party |

#### RoboCasa  ·  _49 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GR00T-N1.5 _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.7 | authors |
| Late Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 71.0 | authors |
| Early Fusion _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 69.7 | authors |
| Spatial Forcing _(RoboCasa demonstrations)_ | average over 8 tasks | success rate | 68.3 | authors |
| X-DiffVLA _(GR00T dataset (RoboCasa tasks))_ | — | Success Rate | 64.5 | authors |
| RLDX-1-FT-RC365 | — | success rate (SR) | 58.4 | authors |
| π0.5 | — | safety | 55.7 | authors |
| Qwen3-VL-4B _(G+E then AgiBot-World-Beta (LoRA r64))_ | — | Success Rate | 55.2 | authors |
| GaussianDream | — | Success rate | 54.8 | authors |
| RLDX-1-FT-RC365 | — | safety | 54.1 | authors |

#### Open-X / RT  ·  _10 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| VisualThink-VLA _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 89.49 | authors |
| FullSoft _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 88.45 | authors |
| ECoT | — | success rate | 85.09 | 3rd-party |
| BaseVLA _(Open X-Embodiment (BridgeData V2, Fractal, RoboTurk, LIBERO, UT Austin MUTEX))_ | — | success rate | 75.37 | authors |
| OpenVLA + RL | speed steering | success rate | 48.9 | authors |
| OpenVLA + PID | height steering | success rate | 46.0 | authors |
| OpenVLA | height steering | success rate | 40.0 | authors |

#### ALFWorld  ·  _2 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| GIGPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 90.4 | authors |
| GRPO w/ PaW _(on-policy RL rollouts)_ | — | success rate | 77.9 | authors |

#### VBench  ·  _335 results_

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

#### Habitat  ·  _4 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ViewCrafter | sparse views-to-video | FVD | 778.207 | 3rd-party |
| TrajectoryCrafter | sparse views-to-video | FVD | 690.322 | 3rd-party |
| GEN3C | sparse views-to-video | FVD | 511.039 | 3rd-party |
| Pantheon360 _(360-1M (filtered))_ | sparse views-to-video | FVD | 450.696 | authors |

#### BEHAVIOR  ·  _2 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| MPVI _(none (no additional training))_ | — | Q-score improvement | 113.0 | authors |
| openpi-comet _(BEHAVIOR-1K 2025 Challenge teleoperation data + motion-planner-synthesized trajectories)_ | — | success rate | 11.4 | 3rd-party |

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

#### NAVSIM  ·  _39 results_

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

#### DAVIS  ·  _37 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| TrajectoryCrafter | 10 ReCamMaster camera trajectory types | RotErr | 10.434 | 3rd-party |
| CogNVS | 10 ReCamMaster camera trajectory types | RotErr | 6.9499 | 3rd-party |
| Recammaster _(synthetic (Unreal Engine))_ | 10 ReCamMaster camera trajectory types | RotErr | 2.3175 | 3rd-party |
| Redirector _(synthetic)_ | 10 ReCamMaster camera trajectory types, speed=2.0 | RotErr | 1.9246 | 3rd-party |
| Ours _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types, speed=2.0 | RotErr | 1.8821 | authors |
| Full reward (Geo-Align) _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types | RotErr | 1.3895 | authors |
| Ours _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types | Dyn-MEt3R | 0.8573 | authors |
| Geo-Align _(CityWalk (conditioning) + OmniWorld (target trajectories, rescaled))_ | 10 ReCamMaster camera trajectory types | Dyn-MEt3R | 0.8573 | authors |
| Redirector _(synthetic)_ | 10 ReCamMaster camera trajectory types | Dyn-MEt3R | 0.8497 | 3rd-party |
| TrajectoryCrafter | 10 ReCamMaster camera trajectory types | Dyn-MEt3R | 0.8244 | 3rd-party |

#### 3DEditBench  ·  _36 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| 3WM | 3D object manipulation | PSNR | 22.73 | authors |
| LightningDrag | 3D object manipulation | PSNR | 19.52 | 3rd-party |
| DiffusionHandles | 3D object manipulation | PSNR | 17.82 | 3rd-party |
| DragAnything | 3D object manipulation | PSNR | 15.13 | 3rd-party |
| 3WM | 3D object manipulation | Edit Adherence (EA) | 0.797 | authors |
| PSI _(3 million real-world RGB video clips)_ | object manipulation (PSI segment, PSI editing model) | EA | 0.776 | authors |
| PSI _(3 million real-world RGB video clips)_ | object manipulation (PSI segment, PSI editing model) | SSIM | 0.736 | authors |
| LightningDrag | 3D object manipulation | Edit Adherence (EA) | 0.722 | 3rd-party |
| DasS | object manipulation (PSI segment, DasS editing model) | SSIM | 0.707 | authors |
| PasC | object manipulation (PSI segment, PasC editing model) | EA | 0.679 | authors |

#### Verse-Bench  ·  _35 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ovi 1.1 | — | Sync-D | 7.979 | 3rd-party |
| daVinci-MagiHuman | — | Sync-D | 7.816 | 3rd-party |
| MoVA | — | Sync-D | 7.808 | 3rd-party |
| NAVA | — | Sync-C | 7.791 | authors |
| LTX 2.3 | — | Sync-D | 7.69 | 3rd-party |
| NAVA | — | Sync-D | 7.566 | authors |
| Ovi 1.1 | — | Sync-C | 7.484 | 3rd-party |
| MoVA | — | Sync-C | 7.289 | 3rd-party |
| LTX 2.3 | — | Sync-C | 7.248 | 3rd-party |
| MoVA | — | PQ | 7.233 | 3rd-party |

#### Trajectory100  ·  _35 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Wan-2.1-I2V | — | FVD | 1421.87 | 3rd-party |
| Tora | — | FVD | 957.81 | 3rd-party |
| RealisDance-DiT | — | FVD | 758.08 | 3rd-party |
| MeshToken _(internal 300K video clips)_ | — | FVD | 695.62 | authors |
| RealisMotion | — | FVD | 314.59 | 3rd-party |
| Wan-2.1-I2V | — | FID | 33.06 | 3rd-party |
| RealisDance-DiT | — | FID | 23.02 | 3rd-party |
| RealisMotion | — | PSNR | 22.57 | 3rd-party |
| MeshToken _(internal 300K video clips)_ | — | FID | 22.13 | authors |
| Tora | — | FID | 21.51 | 3rd-party |

#### CrossFPS  ·  _32 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| HY-World 1.5 | — | FVD | 1131.7 | 3rd-party |
| Matrix-Game 3.0 | — | FVD | 1022.7 | 3rd-party |
| LingBot-World (Act) | — | FVD | 954.4 | 3rd-party |
| SCOPE _(CrossFPS)_ | — | FVD | 690.3 | authors |
| SCOPE _(CrossFPS)_ | — | Flow Score | 18.24 | authors |
| LingBot-World (Act) | — | Flow Score | 15.5 | 3rd-party |
| Matrix-Game 3.0 | — | Flow Score | 13.36 | 3rd-party |
| HY-World 1.5 | — | Photometric Smoothness | 2.523 | 3rd-party |
| Matrix-Game 3.0 | — | Motion Smoothness | 2.502 | 3rd-party |
| SCOPE _(CrossFPS)_ | — | Motion Smoothness | 2.383 | authors |

#### Minecraft VLA benchmark  ·  _30 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| CaB (When+How) _(VPT Demonstration Dataset)_ | smelt | E1: F1 per group | 94.2 | authors |
| CaB (When+How) _(VPT Demonstration Dataset)_ | — | E1: F1↑ | 90.5 | authors |
| CaB-When _(VPT Demonstration Dataset)_ | — | E1: F1↑ | 90.3 | authors |
| Signed-distance regression _(VPT Demonstration Dataset)_ | — | E1: F1↑ | 79.5 | authors |
| Hazard-style completion _(VPT Demonstration Dataset)_ | — | E1: F1↑ | 77.8 | authors |
| Progress regression (STG) _(VPT Demonstration Dataset)_ | — | E1: F1↑ | 74.6 | authors |
| Binary completion (+dwell) _(VPT Demonstration Dataset)_ | — | E1: F1 | 73.8 | authors |
| CaB (When+How) _(VPT Demonstration Dataset)_ | — | E2: Single↑ | 61.1 | authors |
| Binary completion (+dwell) _(VPT Demonstration Dataset)_ | — | E2: Single↑ | 52.4 | authors |
| Signed-distance regression _(VPT Demonstration Dataset)_ | — | E2: Single↑ | 52.1 | authors |

#### custom benchmark  ·  _29 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| TeleOmni | — | FVD | 2.202 | 3rd-party |
| W/O Dual-RoPE _(curated dataset (text-to-video corpora + existing video editing datasets))_ | — | FVD | 1.837 | authors |
| UniVideo | — | FVD | 1.687 | 3rd-party |
| UniVideo-Q | — | FVD | 1.389 | 3rd-party |
| Single-Stream _(curated dataset (text-to-video corpora + existing video editing datasets))_ | — | FVD | 1.364 | authors |
| VACE | — | FVD | 1.302 | 3rd-party |
| W/O Feedback _(curated dataset (text-to-video corpora + existing video editing datasets))_ | — | FVD | 1.074 | authors |
| Smart-Insertion-V _(curated dataset (text-to-video corpora + existing video editing datasets))_ | — | FVD | 1.055 | authors |
| Smart-Insertion-V _(curated dataset (text-to-video corpora + existing video editing datasets))_ | — | Harmonic Score | 0.842 | authors |
| W/O Feedback _(curated dataset (text-to-video corpora + existing video editing datasets))_ | — | DINO-Similarity-V | 0.749 | authors |

#### DeepMind Control Suite  ·  _29 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Ours (PH-RSSM) _(DeepMind Control Suite)_ | Reacher Easy | return | 985.1 | authors |
| R2Dreamer _(DeepMind Control Suite)_ | Average (Cheetah Run, Walker Stand, Reacher Easy, Hopper Hop, Walker Walk, Walker Run) | return | 762.5 | 3rd-party |
| Ours (PH-RSSM) _(DeepMind Control Suite)_ | Average (6 tasks) | imagined reward | 738.9 | authors |
| R2Dreamer _(DeepMind Control Suite)_ | Average (6 tasks) | imagined reward | 702.5 | 3rd-party |
| DreamerV3 _(DeepMind Control Suite)_ | Cheetah Run | return | 689.9 | 3rd-party |
| Ours (PH-RSSM) _(DeepMind Control Suite)_ | Cheetah Run | imagined reward (mean ± std) | 687.1 | authors |
| TC-WM | Cheetah | episode return | 292.0 | authors |
| R2Dreamer _(DeepMind Control Suite)_ | — | Total Energy Consumption (absolute proxy) | 122.1 | 3rd-party |
| Ours (PH-RSSM) _(DeepMind Control Suite)_ | — | Total Energy Consumption (absolute proxy) | 112.58 | authors |
| R2Dreamer _(DeepMind Control Suite)_ | — | Mean Squared Jerk (absolute proxy) | 44.05 | 3rd-party |

#### RoboSemanticBench  ·  _28 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| OpenVLA-OFT _(RSB expert demonstrations)_ | RSB-HardMath-4 | TSR | 20.5 | authors |
| TinyVLA _(RSB expert demonstrations)_ | RSB-General-4 | TSR | 14.8 | authors |
| DexVLA _(RSB expert demonstrations)_ | RSB-Math-4 | TSR | 13.6 | authors |
| OpenVLA-OFT _(RSB expert demonstrations)_ | Average | TSR Avg | 11.1 | authors |
| TinyVLA _(RSB expert demonstrations)_ | Average | TSR Avg | 8.6 | authors |
| DexVLA _(RSB expert demonstrations)_ | Average | TSR Avg | 6.5 | authors |
| GO1 _(RSB expert demonstrations)_ | RSB-Math-4 | TSR | 3.8 | authors |
| GO1 _(RSB expert demonstrations)_ | Average | TSR Avg | 2.0 | authors |

## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
- **World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications** — A unifying multi-axis taxonomy for world models that integrates architecture, methodological families, reasoning strategies (particularly the convergence of chain-of-thought reasoning with world-model imagination), and applications, providing a structured framework to map the fragmented landscape of world model… _(→ WAM: The taxonomy's explicit categorization of reasoning strategies (imagination-based planning, latent policy learning, counterfactual reasoning) directly informs how WAMs can be architected to generate actions rather than just passive predictions. Specifically…)_ [abs](https://arxiv.org/abs/2606.00133) · [pdf](https://arxiv.org/pdf/2606.00133v1)
- **PhAIL: A Real-Robot VLA Benchmark and Distributional Methodology** — Replacing binary success rate metrics with a distributional evaluation methodology based on the time-to-success cumulative distribution function (CDF), scored via Human-Relative Throughput (HRT) and compared using macro-averaged Kolmogorov-Smirnov significance tests to resolve close model comparisons with small sample… _(→ WAM: Evaluating World Action Models often relies on binary task completion metrics, which fail to capture the speed-efficiency trade-offs of different policies. By adopting the time-to-success CDF and HRT scoring, WAM evaluations can distinguish between models…)_ [abs](https://arxiv.org/abs/2605.29710) · [pdf](https://arxiv.org/pdf/2605.29710v1) · [code](https://github.com/Positronic-Robotics/phail-paper)
- **VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models** — A lightweight, one-class discriminative confidence head that leverages frozen pretrained VLA internal representations and step-conditioned modeling to estimate step-wise anomaly scores in a single forward pass, avoiding the computational overhead of resampling and generalizing to continuous action spaces. _(→ WAM: World Action Models (WAMs) often suffer from compounding errors over long horizons and need to know when their world state predictions become unreliable. VLAConf's lightweight confidence head can be directly attached to a WAM's internal representations to…)_ [abs](https://arxiv.org/abs/2605.29605) · [pdf](https://arxiv.org/pdf/2605.29605v1)
- **When Does LeJEPA Learn a World Model?** — LeJEPA (alignment plus Gaussian regularization) provably achieves linear identifiability—linearly recovering the world's true latent variables from nonlinear observations—and Gaussian is the unique latent distribution for which this guarantee holds. Alignment strictly penalizes each degree of nonlinearity via a… _(→ WAM: World Action Models require latent spaces that faithfully preserve the world's true degrees of freedom to support reliable action-conditioned planning and compositional generalization. If the representation scrambles these degrees of freedom, planning becomes…)_ [abs](https://arxiv.org/abs/2605.26379) · [pdf](https://arxiv.org/pdf/2605.26379v1) · [code](https://github.com/klindtlab/lejepa-identifiability)
- **Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts** — A preemptive runtime verification architecture (Pre-VLA) that assesses candidate action chunks before physical execution or world-model imagination, using a lightweight dual-branch head predicting safety confidence and critic-derived advantage scores, trained with a multi-task objective (Focal classification +… _(→ WAM: World Action Models inherently couple world-model rollouts with action generation, making them vulnerable to error accumulation when low-quality actions corrupt the imagined future state. Pre-VLA's preemptive verification layer transfers directly: before a…)_ [abs](https://arxiv.org/abs/2605.22446) · [pdf](https://arxiv.org/pdf/2605.22446v1)
- **Key-Gram: Extensible World Knowledge for Embodied Manipulation** — Key-Gram introduces a conditional-memory framework that decouples language-derived world knowledge from visual-state reasoning in embodied control models. It decomposes language instructions into task-specific 'key-grams', retrieves static linguistic priors via deterministic hashed lookup (O(1) complexity) from an… _(→ WAM: World Action Models (WAMs) inherently rely on language instructions to guide future world state predictions and action generation. By adopting Key-Gram's externalized linguistic memory, WAMs could decouple static language semantics from the heavy…)_ [abs](https://arxiv.org/abs/2605.18556) · [pdf](https://arxiv.org/pdf/2605.18556v1)
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
- **Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling** — A training-free post-training quantization framework (Omega-QVLA) that enables uniform W4A4 quantization of both the LLM backbone and the diffusion-based action head in VLAs. It uses a composite SVD-Hadamard rotation to equalize per-channel weight energy and diffuse activation outliers, alongside a per-step DiT… _(→ WAM: World Action Models share the same architectural bottlenecks as VLAs, relying on large LLM backbones and DiT-based diffusion heads for generating future states or actions. The per-step DiT activation scaling directly transfers to the WAM's generative head…)_ [abs](https://arxiv.org/abs/2605.28803) · [pdf](https://arxiv.org/pdf/2605.28803v1) · [code](https://github.com/UCMP13753/Omega-QVLA)
- **OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning** — OSP-Next introduces a hybrid full-sparse attention architecture (Skiparse-2D Attention) that applies fixed-pattern token-wise and group-wise sparsity along spatial dimensions while remaining natively compatible with FlashAttention kernels, paired with Sparse Sequence Parallelism (SSP) that partitions subsequences… _(→ WAM: World Action Models must process long sequences of observations and actions in real-time, making the quadratic cost of full attention prohibitive. Skiparse-2D's fixed sparse pattern—leveraging spatial locality while preserving FlashAttention…)_ [abs](https://arxiv.org/abs/2605.28691) · [pdf](https://arxiv.org/pdf/2605.28691v1) · [code](https://github.com/PKU-YuanGroup/OSP-Next)
- **Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation** — Proprio introduces a training-free, self-scoring mechanism for video generators by measuring flow residuals under controlled latent perturbations. The core insight is that a frozen generative model's own internal dynamics encode implicit physical knowledge: samples that are better explained by the generator's learned… _(→ WAM: World Action Models (WAMs) must predict physically plausible future states conditioned on actions, but like video generators, they often produce violations of physical laws. Proprio's self-scoring mechanism transfers directly: a WAM's flow residuals under…)_ [abs](https://arxiv.org/abs/2605.28230) · [pdf](https://arxiv.org/pdf/2605.28230v1)
- **VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking** — The core innovation is the 'VLA-Hijack' framework, which exploits the universal mechanism of visual proprioception (visual self-localization of the agent's embodiment) in VLA models to achieve highly transferable adversarial attacks. It concurrently optimizes Attention-Guided Proprioceptive Suppression to hide the… _(→ WAM: World Action Models (WAMs) inherently rely on visual proprioception to predict future world states conditioned on actions; if the model cannot locate the agent in the current frame, its action-conditioned predictions will fail. The 'visual proprioception…)_ [abs](https://arxiv.org/abs/2605.28083) · [pdf](https://arxiv.org/pdf/2605.28083v1)
- **What-If World: A Causal Benchmark for General World Models in Embodied Scenarios** — A causal evaluation methodology for world simulators that tests whether models respond to controlled physical interventions by evaluating paired prompts (same scene, one variable changed) rather than scoring videos individually. The benchmark uses a four-part rubric (APEO: Adherence, Physics, Environment, Outcome) to… _(→ WAM: This paired-intervention evaluation paradigm transfers directly to World Action Models because their core purpose is predicting how the world changes under different actions. A WAM that produces visually plausible futures but fails to change its predictions…)_ [abs](https://arxiv.org/abs/2605.27589) · [pdf](https://arxiv.org/pdf/2605.27589v1)
- **PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs** — A planner-executor architecture that decouples high-level LLM task planning from low-level control execution via a structured tool-calling interface, augmented with an explicit constraint enforcement layer (altitude limits, geofencing) and bounded replanning for recovery from action failures, while constructing a… _(→ WAM: The decoupling of planning from execution with an explicit constraint enforcement layer transfers directly to WAMs: a WAM generates predicted future world states conditioned on actions, but those predictions must respect physical and safety constraints (e.g…)_ [abs](https://arxiv.org/abs/2606.00104) · [pdf](https://arxiv.org/pdf/2606.00104v1) · [code](https://github.com/erdemuysalx/PEACE)
- **Scaling World-Model Reinforcement Learning Through Diffusion Policy Optimization** — Reformulating policy optimization as a diffusion process over searched trajectories in latent world models (Model-Based Diffusion Policy Optimization, or MBDPO) to unify search and policy optimization, using an implicit energy function extracted from the dataset to anchor the policy and resolve the structural… _(→ WAM: World Action Models (WAMs) inherently combine world prediction and action generation, making them susceptible to misalignment between planning/search and policy execution. By adopting MBDPO's approach, a WAM can unify its trajectory prediction and action…)_ [abs](https://arxiv.org/abs/2605.26282) · [pdf](https://arxiv.org/pdf/2605.26282v1) · [code](https://github.com/Edmond1Cheng/MBDPO)
- **Drift-Resistant Navigation World Model with Anchored Epipolar Guidance** — Anchor-guided rollout with bidirectional epipolar geometric constraints: instead of sequentially predicting every frame, first predict sparse future anchor frames as stable long-range targets, then generate intermediate frames conditioned on both past context and future anchors, where the anchors additionally provide… _(→ WAM: World Action Models suffer from the same compounding error problem (perceptual/geometric drift) during long-horizon action-conditioned rollouts. The anchor-guided rollout paradigm transfers directly: WAMs could first predict sparse anchor states at future…)_ [abs](https://arxiv.org/abs/2605.24761) · [pdf](https://arxiv.org/pdf/2605.24761v1)
- **Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems** — The formulation of 'silent physical-action failure' in black-box Physical AI and the proposal of a runtime authorization boundary, including a taxonomy of runtime guardrail functions and evaluation requirements, to prevent plausible but physically invalid or dangerous actions from being executed. _(→ WAM: World Action Models (WAMs) generate action sequences that can suffer from hallucinated affordances or distribution shift, leading to outputs that appear semantically aligned but are physically dangerous. The concept of a runtime authorization boundary can be…)_ [abs](https://arxiv.org/abs/2606.00090) · [pdf](https://arxiv.org/pdf/2606.00090v1)

## 👥 Influential Authors & Groups
- **[Ye Li](https://www.semanticscholar.org/author/2310388004)** (3 papers · Zhejiang University) — Ye Li's research focuses on long video generation and world simulation, including multi-shot video extrapolation with recursive context allocation and closed-loop video world simulators for robotic manipulation, as well as efficient vision-language-action…
- **[Shanghang Zhang](https://www.semanticscholar.org/author/2376781333)** (3 papers · Peking University) — Shanghang Zhang's research focuses on vision-language-action (VLA) models for dexterous manipulation, one-shot cross-embodiment imitation via joint-embedding predictive architectures, and world-ego modeling for long-horizon hybrid embodied tasks.
- **[Pinar Yanardag](https://www.semanticscholar.org/author/3137679)** (2 papers · Virginia Tech) — Pinar Yanardag's research focuses on autoregressive video diffusion and world models, specifically improving temporal dynamics and controllability by manipulating the anchor (reference frame) mechanism—e.g., replacing static anchors with self-evolving latent…
- **[Pengfei Wan](https://www.semanticscholar.org/author/2363570130)** (2 papers · Kuaishou Technology) — Pengfei Wan's research focuses on video generation models, particularly on improving video reasoning through adaptive test-time optimization with VLMs as teachers, and on achieving long-horizon, consistent world generation via decoupled memory architectures.
- **[Kun Gai](https://www.semanticscholar.org/author/2385564054)** (2 papers · The University of Hong Kong) — DecMem introduces a decoupled memory architecture with Sparse Global Memory and Anchored Local Memory to achieve minute-long, consistent world generation by overcoming computational inefficiency and attention dispersion in long-horizon video extrapolation…
- **[Minseok Joo](https://www.semanticscholar.org/author/2313642518)** (2 papers · Korea University) — Minseok Joo's research focuses on improving consistency and reducing ambiguity in vision-based models, specifically through inverse dynamics learning to mitigate state aliasing in Vision-Language-Action models for robot manipulation, and through…
- **[Kyujin Lee](https://www.semanticscholar.org/author/2439353694)** (2 papers · KAIST) — Kyujin Lee's WAM research focuses on improving visual representation learning in Vision-Language-Action (VLA) models for robot manipulation by using inverse dynamics as an auxiliary objective to mitigate state aliasing, and enhancing long-horizon geometric…
- **[Weihua Chen](https://www.semanticscholar.org/author/2365043710)** (2 papers · DAMO Academy, Alibaba Group) — Weihua Chen's research focuses on human motion control in video generation using 3D-aware mesh tokenization without rendering, and efficient video unified models that bridge frequency domains for high-fidelity generation with reduced computational cost.
- **[Fan Wang](https://www.semanticscholar.org/author/2320184479)** (2 papers · DAMO Academy, Alibaba Group) — Fan Wang's research focuses on enhancing video diffusion models with 3D awareness, particularly through mesh tokenization for human motion control, and on interactive world modeling for action-conditioned video generation with long-horizon consistency.
- **[Tianzhuo Yang](https://www.semanticscholar.org/author/2367280829)** (2 papers · Institute for Artificial Intelligence, Peking University) — Developing defense mechanisms for LLM agents via proactive power regulation and environment-grounded look-ahead reasoning, and evaluating action-conditioned reliability in robotic world models through hierarchical benchmarks.
- **[Jiaming Ji](https://www.semanticscholar.org/author/2273548793)** (2 papers · Institute for Artificial Intelligence, Peking University) — Jiaming Ji's research focuses on safety and reliability in AI systems, particularly in LLM agents and robotic world models. This includes proactive defense mechanisms for LLM agents via environment-grounded look-ahead reasoning (SafeMCP) and evaluating…
- **[Juntao Dai](https://www.semanticscholar.org/author/2368404298)** (2 papers · Physis Lab, Institute for Artificial Intelligence, Peking University) — Juntao Dai's research focuses on improving the safety and reliability of AI agents, particularly through proactive defense mechanisms for LLM agents (SafeMCP) and evaluating the action-conditioned reliability of robotic world models (MiraBench).
- **[Chensheng Peng](https://www.semanticscholar.org/author/2160952549)** (2 papers · Applied Intuition) — Chensheng Peng's research focuses on interactive video world modeling, including action-conditioned video generation, long-horizon consistency, and memory mechanisms for out-of-sight state evolution, as demonstrated by work on dynamic memory for video…
- **[Jun Nie](https://www.semanticscholar.org/author/2315126639)** (2 papers · Peking University) — Jun Nie's research focuses on extracting value-like information from frozen vision-language-action (VLA) policies to improve action selection, and on developing training-free methods to dynamically adjust execution horizons for action-chunking robot policies…
- **[Jiachen Zhang](https://www.semanticscholar.org/author/2376800622)** (2 papers · Peking University) — The author's research focuses on improving robot imitation learning policies by extracting value-like information about task success from frozen vision-language-action (VLA) representations for test-time action selection (probing study), and developing…
- **[Junying Lao](https://www.semanticscholar.org/author/2176256865)** (2 papers · Peking University) — Junying Lao's primary WAM research directions focus on improving robot policy performance at test time without retraining. This includes probing frozen Vision-Language-Action (VLA) representations for value-like information about task success to guide action…
- **[Songfang Huang Peking University](https://www.semanticscholar.org/author/2438923144)** (2 papers · Peking University) — Research on improving robot policy performance by extracting value-like information about task success from frozen VLA representations and by dynamically selecting execution horizons for action-chunking policies to enhance success rates.
- **[Haibao Yu](https://www.semanticscholar.org/author/2162290793)** (2 papers · The University of Hong Kong) — Haibao Yu's research focuses on developing world models for robotic manipulation and navigation, particularly through feed-forward 3D Gaussian representations for manipulation and autoregressive training strategies for long-horizon navigation prediction.
- **[Li Jiang](https://www.semanticscholar.org/author/2292670885)** (2 papers · The Chinese University of Hong Kong, Shenzhen) — Li Jiang's research focuses on world-action modeling for autonomous driving and robotic manipulation, leveraging video generative priors and 4D supervision to enhance planning and policy robustness.
- **[Jie-Ying Lee](https://www.semanticscholar.org/author/2311274155)** (2 papers · National Yang Ming Chiao Tung University) — Jie-Ying Lee's research focuses on video generation models, particularly evaluating causal understanding in video diffusion models and developing 3D-aware 360° video generation for digital twin applications.
- **[Yu-Lun Liu](https://www.semanticscholar.org/author/2309657159)** (2 papers · National Yang Ming Chiao Tung University) — Research focuses on advancing video generation models for digital twins and world models, developing benchmarks and frameworks that enforce geometric consistency (e.g., 360° video generation via 3D Cache) and evaluate causal reasoning capabilities of video…
- **[Xiancong Ren](https://www.semanticscholar.org/author/2392686023)** (2 papers · X-Humanoid) — Xiancong Ren's research focuses on developing self-evolving embodied agents that autonomously induce navigation heuristics and refine cognitive strategies through continuous reflection-adaptation loops, as well as diagnosing Vision-Language-Action (VLA)…
- **[Yong Dai](https://www.semanticscholar.org/author/2439566558)** (2 papers · X-Humanoid) — Yong Dai focuses on building self-evolving embodied agents that autonomously induce navigation heuristics and refine cognitive strategies through continuous reflection-adaptation loops, as well as diagnosing Vision-Language-Action (VLA) models by tracing…
- **[Xiaozhu Ju](https://www.semanticscholar.org/author/2392718853)** (2 papers · X-Humanoid) — Research on embodied AI, focusing on self-evolving navigation agents with dual-grain cognitive memory and autonomous knowledge induction, as well as diagnostic methods for Vision-Language-Action models through representation and behavior tracing.
- **[Jiayi Luo](https://www.semanticscholar.org/author/2319302828)** (2 papers · BUAA) — Jiayi Luo's main WAM-related research directions are developing closed-loop video world simulators for robotic manipulation (GE-Sim 2.0) and designing training-free KV cache policies for autoregressive video generation to improve long-video consistency under…

## 📰 Embodied / Physical-AI News
- [2026 Robotics Summit & Expo Recap](https://www.therobotreport.com/2026-robotics-summit-expo-recap/) — _The Robot Report_
- [Petal Surgical adds more funding for incisionless surgical robot](https://www.therobotreport.com/petal-surgical-adds-more-funding-for-incisionless-surgical-robot/) — _The Robot Report_
- [FORT Robotics acquires Mapless AI to expand teleop capabilities](https://www.therobotreport.com/fort-robotics-acquires-mapless-ai-to-expand-teleop-capabilities/) — _The Robot Report_
- [Holo3.1: Fast & Local Computer Use Agents](https://huggingface.co/blog/Hcompany/holo31) — _Hugging Face - Blog_
- [NVIDIA releases new and updated tools for physical AI developers](https://www.therobotreport.com/nvidia-releases-new-updated-tools-physical-ai-gtc-taipei-computex/) — _The Robot Report_
- [ANSCER Robotics closes Series A round for industrial material handling](https://www.therobotreport.com/anscer-robotics-closes-series-a-round-industrial-material-handling/) — _The Robot Report_
- [Top 10 robotics stories of May 2026](https://www.therobotreport.com/top-10-robotics-stories-of-may-2026/) — _The Robot Report_
- [Learn about advances in robotic case and each picking](https://www.therobotreport.com/learn-about-advances-robotic-case-each-picking-webinar/) — _The Robot Report_
- [Introducing Mellum2: A 12B Mixture-of-Experts Model by JetBrains](https://huggingface.co/blog/JetBrains/mellum2-launch) — _Hugging Face - Blog_
- [Beyond LLMs: Why Scalable Enterprise AI Adoption Depends on Agent Logic](https://huggingface.co/blog/ibm-research/agent-logic-and-scalable-ai-adoption) — _Hugging Face - Blog_
- [Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) — _Hugging Face - Blog_
- [Why robotic arms are now being integrated with CNC machines](https://www.therobotreport.com/why-robotic-arms-are-now-being-integrated-cnc-machines/) — _The Robot Report_
- [This DIY Bipedal Robot Used Pneumatic “Air-Muscles” Instead of Motors](https://spectrum.ieee.org/shadow-walker-biped-humanoid-robot) — _IEEE Spectrum_
- [MISUMI Group invests $1B in Americas, global AI and digital manufacturing](https://www.therobotreport.com/misumi-group-invests-1b-americas-global-ai-digital-manufacturing/) — _The Robot Report_
- [Software becoming the biggest bottleneck to physical AI innovation, finds QNX research](https://www.therobotreport.com/software-becoming-biggest-bottleneck-physical-ai-innovation-finds-qnx/) — _The Robot Report_

---
_Generated by [Awesome-Embodied&MM](https://github.com/wzii/Awesome_Embodied_MM)._
