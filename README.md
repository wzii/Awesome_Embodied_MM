# Awesome-Embodied&MM

> Daily-updated intelligence on **World Action Models** — world models, vision-language-action
> (VLA) models, action-conditioned video/world generation, robot foundation models, and
> embodied/physical AI. Auto-generated; do not edit by hand.

**Last updated:** 2026-06-04 · **Tracked:** 124 core · 154 adjacent ·
74 news · **599** benchmark rows across **257** model
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
| **7.48** | LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World | 2026-05-31 | spd – · gen 4 · spec 8 · cost – | [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458v1) |
| **7.38** | Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation | 2026-06-01 | spd 5 · gen 6 · spec 8 · cost 5 | [abs](https://arxiv.org/abs/2606.02486) · [pdf](https://arxiv.org/pdf/2606.02486v1) |
| **7.38** | Wall-OSS-0.5 Technical Report | 2026-05-29 | spd – · gen 8 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.30877) · [pdf](https://arxiv.org/pdf/2605.30877v2) · [code](https://github.com/X-Square-Robot/wall-x) |
| **7.09** | World-Task Factorization for Robot Learning | 2026-06-01 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02027) · [pdf](https://arxiv.org/pdf/2606.02027v1) |
| **6.87** | DEFLECT: Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning for VLA Policies | 2026-05-19 | spd 7 · gen 5 · spec 6 · cost – | [abs](https://arxiv.org/abs/2605.19294) · [pdf](https://arxiv.org/pdf/2605.19294v1) |
| **6.76** | LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model | 2026-05-21 | spd 3 · gen 2 · spec 8 · cost – | [abs](https://arxiv.org/abs/2605.22089) · [pdf](https://arxiv.org/pdf/2605.22089v1) · [code](https://github.com/Thinklab-SJTU/Bench2Drive) |
| **6.75** | OneVLA: A Unified Framework for Embodied Tasks | 2026-05-31 | spd – · gen 7 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.01241) · [pdf](https://arxiv.org/pdf/2606.01241v1) · [code](https://github.com/linglingxiansen/OneVLA) |
| **6.58** | RoboDream: Compositional World Models for Scalable Robot Data Synthesis | 2026-06-01 | spd – · gen 6 · spec 6 · cost – | [abs](https://arxiv.org/abs/2606.02577) · [pdf](https://arxiv.org/pdf/2606.02577v1) |
| **6.48** | Point Tracking Improves World Action Models | 2026-05-22 | spd – · gen 6 · spec 7 · cost – | [abs](https://arxiv.org/abs/2605.23856) · [pdf](https://arxiv.org/pdf/2605.23856v1) |
| **6.41** | minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models | 2026-05-28 | spd 6 · gen 5 · spec 5 · cost 5 | [abs](https://arxiv.org/abs/2605.30263) · [pdf](https://arxiv.org/pdf/2605.30263v1) · [code](https://github.com/shengshu-ai/minWM) |
| **6.33** | LEIA: Learned Environment for Interactive Architected Materials | 2026-05-27 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2605.28368) · [pdf](https://arxiv.org/pdf/2605.28368v2) · [code](https://github.com/HaiqianYang-MechE/leia) |
| **6.29** | DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving | 2026-05-27 | spd – · gen 3 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.28544) · [pdf](https://arxiv.org/pdf/2605.28544v1) · [code](https://github.com/OpenDriveLab/OpenScene) |
| **6.25** | Towards Precise Intent-Aligned VLA Aerial Navigation via Expert-Guided GRPO | 2026-06-01 | spd 3 · gen 3 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.02313) · [pdf](https://arxiv.org/pdf/2606.02313v1) |
| **6.19** | IMWM: Intuition Models Complement World Models for Latent Planning | 2026-06-01 | spd – · gen 3 · spec 7 · cost – | [abs](https://arxiv.org/abs/2606.01626) · [pdf](https://arxiv.org/pdf/2606.01626v1) |
| **6.02** | Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models | 2026-05-29 | spd – · gen 3 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2605.31111) · [pdf](https://arxiv.org/pdf/2605.31111v1) · [code](https://github.com/LucasStill/SD-JEPA) |
| **6.0** | Policy and World Modeling Co-Training for Language Agents | 2026-06-01 | spd – · gen – · spec – · cost – | [abs](https://arxiv.org/abs/2606.02388) · [pdf](https://arxiv.org/pdf/2606.02388v1) |
| **5.83** | RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models | 2026-06-01 | spd – · gen 4 · spec – · cost – | [abs](https://arxiv.org/abs/2606.02277) · [pdf](https://arxiv.org/pdf/2606.02277v1) · [code](https://github.com/ZGC-EmbodyAI/RoboSemanticBench) |
| **5.82** | Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action | 2026-05-21 | spd – · gen 5 · spec 6 · cost – | [abs](https://arxiv.org/abs/2605.22283) · [pdf](https://arxiv.org/pdf/2605.22283v1) |
| **5.74** | The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space | 2026-06-01 | spd – · gen 4 · spec 6 · cost – | [abs](https://arxiv.org/abs/2606.01847) · [pdf](https://arxiv.org/pdf/2606.01847v1) |
| **5.69** | Geometry-Aware Implicit Memory for Video World Models | 2026-06-01 | spd – · gen 2 · spec 6 · cost 5 | [abs](https://arxiv.org/abs/2606.02436) · [pdf](https://arxiv.org/pdf/2606.02436v1) |
| **5.69** | QuoVLA: Quotient Space for Vision-Language-Action Models | 2026-05-24 | spd – · gen 6 · spec 5 · cost – | [abs](https://arxiv.org/abs/2605.24890) · [pdf](https://arxiv.org/pdf/2605.24890v1) |
| **5.69** | $π_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control | 2026-05-22 | spd 2 · gen 6 · spec 5 · cost 2 | [abs](https://arxiv.org/abs/2605.23128) · [pdf](https://arxiv.org/pdf/2605.23128v1) |
| **5.45** | WALL-WM: Carving World Action Modeling at the Event Joints | 2026-06-01 | spd – · gen 5 · spec – · cost – | [abs](https://arxiv.org/abs/2606.01955) · [pdf](https://arxiv.org/pdf/2606.01955v1) · [code](https://github.com/X-Square-Robot/wall-x) |
| **5.37** | COMAP: Co-Evolving World Models and Agent Policies for LLM Agents | 2026-06-01 | spd – · gen 3 · spec 5 · cost – | [abs](https://arxiv.org/abs/2606.02372) · [pdf](https://arxiv.org/pdf/2606.02372v1) · [code](https://github.com/loyiv/CoMAP) |

## 📊 Benchmark Leaderboard
_Model identity = (name, training dataset); the same name on different data is a distinct row.
Numbers are as reported; `authors` = self-reported, `3rd-party` = quoted comparison._
_Model identity = (model, training data); same name on different data is a distinct row. `authors` = self-reported, `3rd-party` = quoted. Higher is better for success-rate-style metrics._


#### LIBERO  ·  _62 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| π0.5 | — | success rate | 99.5 | authors |
| ELAN4D(π0.5) _(LIBERO (original, ~2K demos))_ | — | Overall success rate | 97.0 | authors |
| π0.5 _(Open X-Embodiment)_ | — | Overall success rate | 96.9 | 3rd-party |
| π0.5 | — | success rate (SR) | 96.6 | authors |
| GeoPredict | — | Overall success rate | 96.6 | 3rd-party |
| Pri4R | — | Overall success rate | 96.3 | 3rd-party |
| Cosmos-Policy-2B | — | success rate (SR) | 95.3 | authors |
| ELAN4D(π0) _(LIBERO (original, ~2K demos))_ | — | Overall success rate | 95.0 | authors |
| GR00T-N1.7 | — | success rate (SR) | 94.3 | authors |
| π0 _(Open X-Embodiment)_ | — | Overall success rate | 94.2 | 3rd-party |

#### RoboTwin  ·  _11 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| π0.5 _(RoboTwin2.0)_ | Grab Roller | success rate | 98.6 | authors |
| ELAN4D(π0.5) _(RoboTwin2.0 (100 expert episodes per task under clean setting))_ | — | Overall success rate | 37.0 | authors |
| π0.5 _(Open X-Embodiment)_ | — | Overall success rate | 32.0 | 3rd-party |
| ELAN4D(π0) _(RoboTwin2.0 (100 expert episodes per task under clean setting))_ | — | Overall success rate | 15.0 | authors |
| π0 _(Open X-Embodiment)_ | — | Overall success rate | 12.0 | 3rd-party |

#### RoboCasa  ·  _16 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| RLDX-1-FT-RC365 | — | success rate (SR) | 58.4 | authors |
| π0.5 | — | safety | 55.7 | authors |
| RLDX-1-FT-RC365 | — | safety | 54.1 | authors |
| GR00T-N1.5 | — | success rate (SR) | 47.2 | authors |
| π0 | — | safety | 44.6 | authors |
| π0.5 | — | success rate (SR) | 42.3 | authors |
| GR00T-N1.5 | — | safety | 40.7 | authors |
| π0 | — | success rate (SR) | 32.4 | authors |
| GR00T-N1.5 | — | SBU | 26.3 | authors |
| RLDX-1-FT-RC365 | — | SBU | 23.1 | authors |

#### Open-X / RT  ·  _6 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| OpenVLA + RL | speed steering | success rate | 48.9 | authors |
| OpenVLA + PID | height steering | success rate | 46.0 | authors |
| OpenVLA | height steering | success rate | 40.0 | authors |

#### VBench  ·  _71 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| CogVideoX-2B | — | Subject consistency | 95.91 | 3rd-party |
| CoFi | — | Subject consistency | 94.11 | authors |
| CDGS | — | Subject consistency | 91.67 | 3rd-party |
| SlotMemory _(VidProM)_ | single-prompt 30s | Quality Score | 85.23 | authors |
| Lumos-Nexus | — | Quality | 85.03 | authors |
| InfinityStar + VPG | — | Overall | 84.35 | authors |
| SlotMemory _(VidProM)_ | single-prompt 30s | Total Score | 84.28 | authors |
| Lumos-Nexus | — | Total | 84.12 | authors |
| InfinityStar | — | Overall | 83.86 | authors |
| Omni-Video | — | Total | 83.82 | 3rd-party |

#### RealEstate10K  ·  _27 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| DFoT _(RealEstate10K)_ | loop-closing | FVD | 265.03 | 3rd-party |
| WorldMem _(RealEstate10K)_ | loop-closing | FVD | 242.36 | 3rd-party |
| VMem _(RealEstate10K)_ | loop-closing | FVD | 231.77 | 3rd-party |
| COVRAG _(RealEstate10K)_ | loop-closing | FVD | 226.4 | authors |
| VMem _(RealEstate10K)_ | — | average latency | 45.4 | 3rd-party |
| DFoT _(RealEstate10K)_ | loop-closing | FID | 29.88 | 3rd-party |
| WorldMem _(RealEstate10K)_ | loop-closing | FID | 24.77 | 3rd-party |
| VMem _(RealEstate10K)_ | loop-closing | FID | 24.05 | 3rd-party |
| COVRAG _(RealEstate10K)_ | loop-closing | FID | 23.0 | authors |
| COVRAG _(RealEstate10K)_ | loop-closing | PSNR | 18.9 | authors |

#### CARLA-AIR  ·  _27 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| AerialVLN | Cooperative Occlusion-Recovery Escort | RAT (s) | 7.2 | authors |
| SPF | Cooperative Occlusion-Recovery Escort | RAT (s) | 6.5 | authors |
| OpenUAV | Cooperative Occlusion-Recovery Escort | RAT (s) | 6.2 | authors |
| AerialVLA | Cooperative Occlusion-Recovery Escort | Re-acquisition Time (RAT) (s) | 4.8 | authors |
| OpenFly | Cooperative Occlusion-Recovery Escort | RAT (s) | 4.5 | authors |
| Rule-Coop-State | Cooperative Occlusion-Recovery Escort | RAT (s) | 1.8 | authors |
| Rule-Coop-State | Cooperative Occlusion-Recovery Escort | RSR | 0.86 | authors |
| Rule-Coop-State | Cooperative Moving-Platform Landing | TSR | 0.84 | authors |
| OpenFly | Cooperative Moving-Platform Landing | TSR | 0.81 | authors |
| AerialVLA | Cooperative Moving-Platform Landing | Tracking Success Rate (TSR) | 0.78 | authors |

#### Controlled Diagnostic Benchmark  ·  _26 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LAMP | — | Out-Rate | 41.0 | 3rd-party |
| PulpMotion (DiT) | — | Out-Rate | 36.2 | 3rd-party |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | Out-Rate | 5.45 | authors |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | F-Ori | 0.969 | authors |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | F-Tilt | 0.964 | authors |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | F-Roll | 0.937 | authors |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | Auteur-Score | 0.91 | authors |
| Baseline | — | F-Roll | 0.88 | 3rd-party |
| Baseline | — | F-Tilt | 0.875 | 3rd-party |
| PulpMotion (DiT) | — | F-Tilt | 0.873 | 3rd-party |

#### Meve  ·  _26 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| TunerDiT | — | Q4 | 3.34 | authors |
| TunerDiT | — | Q1 | 3.16 | authors |
| TunerDiT | — | Q2 | 3.03 | authors |
| TunerDiT | — | Q3 | 3.03 | authors |
| TunerDiT | — | TVA | 1.533 | authors |
| TunerDiT | — | CSCV | 0.854 | authors |
| DiTCtrl | — | CSCV | 0.803 | 3rd-party |
| FreeNoise | — | CSCV | 0.748 | 3rd-party |
| MEVG | — | CSCV | 0.707 | 3rd-party |
| TunerDiT | — | EI | 0.572 | authors |

#### DL3DV10K  ·  _24 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| DFoT _(DL3DV10K)_ | — | FVD | 706.7 | 3rd-party |
| WorldMem _(DL3DV10K)_ | — | FVD | 428.49 | 3rd-party |
| VMem _(DL3DV10K)_ | — | FVD | 394.79 | 3rd-party |
| COVRAG _(DL3DV10K)_ | — | FVD | 321.81 | authors |
| DFoT _(DL3DV10K)_ | — | FID | 88.01 | 3rd-party |
| WorldMem _(DL3DV10K)_ | — | FID | 58.24 | 3rd-party |
| VMem _(DL3DV10K)_ | — | FID | 57.61 | 3rd-party |
| COVRAG _(DL3DV10K)_ | — | FID | 46.92 | authors |
| COVRAG _(DL3DV10K)_ | — | PSNR | 17.9 | authors |
| VMem _(DL3DV10K)_ | — | PSNR | 16.3 | 3rd-party |

#### VIP-200K  ·  _24 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| ST-DRC (Ours) _(VIP-200K)_ | — | CLIP-Score | 33.04 | authors |
| VACE | — | CLIP-Score | 32.61 | 3rd-party |
| IPVG-STD | — | CLIP-Score | 31.82 | 3rd-party |
| Phantom | — | CLIP-Score | 31.55 | 3rd-party |
| ConsisID | — | CLIP-Score | 31.47 | 3rd-party |
| ST-DRC (Ours) _(VIP-200K)_ | — | MS | 0.992 | authors |
| ConsisID | — | MS | 0.982 | 3rd-party |
| ST-DRC (Ours) _(VIP-200K)_ | — | DD | 0.93 | authors |
| VACE | — | IQ | 0.688 | 3rd-party |
| ST-DRC (Ours) _(VIP-200K)_ | — | IQ | 0.682 | authors |

#### PulpMotion  ·  _16 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| LAMP | — | Cam F1 | 99.7 | 3rd-party |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | Cam F1 | 83.6 | authors |
| Auteur _(Auteur dataset (procedural + CondensedMovies))_ | — | CLaTr | 71.1 | authors |
| LAMP | — | CLaTr | 69.5 | 3rd-party |
| PulpMotion (MAR) | — | Cam F1 | 64.8 | 3rd-party |
| PulpMotion (DiT) | — | Cam F1 | 52.9 | 3rd-party |
| PulpMotion (MAR) | — | CLaTr | 49.3 | 3rd-party |
| PulpMotion (DiT) | — | CLaTr | 39.7 | 3rd-party |
| LAMP | — | FDframe | 35.5 | 3rd-party |
| PulpMotion (MAR) | — | Out-rate | 29.1 | 3rd-party |

#### WorldMem (Minecraft)  ·  _16 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| DecMem _(WorldMem dataset (Minecraft))_ | — | Spatio-temporal Consistency (STC) | 42.12 | authors |
| MineWorld _(Minecraft dataset)_ | — | FID | 41.9661 | 3rd-party |
| DecMem _(WorldMem dataset (Minecraft))_ | — | Visual Quality (VQ) | 39.77 | authors |
| DecMem _(WorldMem dataset (Minecraft))_ | — | Action Controllability (AC) | 37.81 | authors |
| DecMem _(WorldMem dataset (Minecraft))_ | — | PSNR | 30.0785 | authors |
| WorldMem _(Minecraft dataset)_ | — | PSNR | 26.5414 | 3rd-party |
| Oasis _(Minecraft dataset)_ | — | PSNR | 24.1293 | 3rd-party |
| MineWorld _(Minecraft dataset)_ | — | PSNR | 20.2989 | 3rd-party |
| Oasis _(Minecraft dataset)_ | — | FID | 15.9163 | 3rd-party |
| WorldMem _(Minecraft dataset)_ | — | FID | 11.7379 | 3rd-party |

#### MNIST modular arithmetic  ·  _15 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| JEPA + additive embedding (ResNet-18) _(MNIST)_ | digit classification after arithmetic operation | seen operation accuracy | 0.9946 | authors |
| BRo-JEPA (ResNet + MFR) _(MNIST)_ | digit classification after arithmetic operation | zero-shot operation accuracy | 0.9946 | authors |
| BRo-JEPA (ResNet + MFR) _(MNIST)_ | digit classification after arithmetic operation | unseen operation rollout accuracy | 0.9946 | authors |
| BRo-JEPA (ResNet + SFR) _(MNIST)_ | digit classification after arithmetic operation | zero-shot operation accuracy | 0.9893 | authors |
| Supervised ResNet-18 + additive embedding _(MNIST)_ | digit classification after arithmetic operation | seen operation accuracy | 0.9844 | authors |
| JEPA + additive embedding (MLP) _(MNIST)_ | digit classification after arithmetic operation | seen operation accuracy | 0.9794 | authors |
| JEPA + additive embedding (MLP) _(MNIST)_ | digit classification after arithmetic operation | unseen operation rollout accuracy | 0.9793 | authors |
| JEPA + additive embedding (MLP w/ compositional consistency loss) _(MNIST)_ | digit classification after arithmetic operation | zero-shot operation accuracy | 0.9777 | authors |
| Supervised MLP + additive embedding _(MNIST)_ | digit classification after arithmetic operation | seen operation accuracy | 0.9737 | authors |
| BRo-JEPA (MLP + MFR) _(MNIST)_ | digit classification after arithmetic operation | zero-shot operation accuracy | 0.9724 | authors |

#### RoboTrustBench  ·  _14 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Kling-v2.6 | Normal | Overall Average (GPT-5.4 automatic evaluation, normalized to [0,1]) | 0.886 | authors |
| Kling-v2.6 | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.776 | authors |
| LingBot-World | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.681 | authors |
| Cosmos-14B | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.673 | authors |
| Wan2.2 | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.661 | authors |
| Veo-3.1-Fast | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.658 | authors |
| Cosmos-2B | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.651 | authors |
| HunyuanVideo-1.5 | Normal | Overall Average (human evaluation, normalized to [0,1]) | 0.579 | authors |

#### AgentGym  ·  _14 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| PatchWorld-Simple _(AgentGym trajectories)_ | — | macro success rate | 76.4 | authors |
| LLM-Direct | — | macro success rate | 75.8 | 3rd-party |
| ReAct | — | macro success rate | 74.4 | 3rd-party |
| PatchWorld-Residual _(AgentGym trajectories)_ | — | macro success rate | 72.9 | authors |
| PoE-World _(AgentGym trajectories)_ | — | macro success rate | 69.3 | 3rd-party |
| WorldCoder _(AgentGym trajectories)_ | — | macro success rate | 64.4 | 3rd-party |
| Word2World _(AgentGym trajectories)_ | — | macro success rate | 63.5 | 3rd-party |
| Word2World _(AgentGym trajectories)_ | — | macro Token F1 | 0.85 | 3rd-party |
| PatchWorld-Residual _(AgentGym trajectories)_ | — | macro Token F1 | 0.69 | authors |
| LLM-Direct | — | macro Token F1 | 0.64 | 3rd-party |

#### SafeGen-Bench  ·  _13 results_

| Model (training data) | Task | Metric | Value | Source |
|-----------------------|------|--------|------:|:------:|
| Llama-Guard | — | Failure Rate Across 7 Categories | 80.0 | authors |
| LLaVA-Guard | — | Failure Rate Across 7 Categories | 80.0 | authors |
| CogVideoX | — | Average Quality Score | 66.8 | authors |
| Open-Sora-Plan v1.2.0 | — | Average Quality Score | 63.2 | authors |
| Kling V1.0 | — | Average Quality Score | 59.8 | authors |
| I2VGen-XL | — | Average Quality Score | 50.1 | authors |
| Gen3-turbo | — | Average Quality Score | 46.9 | authors |
| CogVideoX | — | Average Unsafety Score | 44.5 | authors |
| Open-Sora-Plan v1.2.0 | — | Average Unsafety Score | 33.6 | authors |
| I2VGen-XL | — | Average Unsafety Score | 31.0 | authors |

## 🔬 Innovation Watch — adjacent fields (VLA / world models / video generation)
_Not scored; surfaced for techniques transferable to WAM._
- **Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends** — The paper systematically identifies and categorizes three crucial technical challenges for interactive world modeling: action-conditioned controllability, long-horizon interactions and memory, and action-following responsiveness for real-time interactivity. _(→ WAM: World Action Models fundamentally rely on action-conditioned state transitions. Addressing these three identified challenges—ensuring actions reliably control state evolution, maintaining coherent long-term memory across extended action sequences, and…)_ [abs](https://arxiv.org/abs/2606.01164) · [pdf](https://arxiv.org/pdf/2606.01164v1) · [code](https://github.com/liujiuming123/Awesome-Interactive-World-Model)
- **Coarse-to-Fine Compositional Diffusion for Long-Horizon Planning** — Coarse-to-Fine Compositional Diffusion (CoFi) separates global structure formation from local detail refinement during inference-time compositional generation. It first aligns local denoised estimates around a shared coarse scaffold capturing long-range task-level arrangement, then diffuses this scaffold to an… _(→ WAM: World Action Models must generate long-horizon action sequences or world-state trajectories that are both globally coherent (the overall plan makes sense) and locally precise (each step's actions are physically valid). CoFi's coarse-to-fine composition…)_ [abs](https://arxiv.org/abs/2606.00837) · [pdf](https://arxiv.org/pdf/2606.00837v1) · [code](https://github.com/KAIST-Visual-AI-Group/SyncDiffusion)
- **MBench: A Comprehensive Benchmark on Memory Capability for Video World Models** — A systematic decomposition of world model memory capability into three hierarchical and complementary dimensions—entity consistency, environment consistency, and causal consistency—further refined into 12 quantifiable sub-dimensions, enabling objective evaluation of long-term state retention in video world models… _(→ WAM: World Action Models must maintain coherent internal world states over extended action sequences, making memory capability critical. The three-dimensional decomposition transfers directly: (1) Entity consistency ensures WAMs track object identities and…)_ [abs](https://arxiv.org/abs/2606.00793) · [pdf](https://arxiv.org/pdf/2606.00793v1) · [code](https://github.com/study-overflow/MBench)
- **SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models** — Formalizing task-aware safety requirements as Signal Temporal Logic (STL) specifications and introducing metrics that expose the success-safety gap: Succ-But-Unsafe (SBU) rate measuring successful-yet-unsafe episodes, and Violation Severity Index (VSI) quantifying worst-case violation depth, revealing that high task… _(→ WAM: World Action Models generate action sequences and predict world states; they could inherit this STL-based safety specification framework to formally constrain their generated trajectories during planning. Currently, WAMs optimizing solely for task-completion…)_ [abs](https://arxiv.org/abs/2606.00773) · [pdf](https://arxiv.org/pdf/2606.00773v1)
- **Closed-Loop Neural Activation Control in Vision-Language-Action Models** — CTRL-STEER decouples representation from regulation in test-time steering of VLA models: rather than applying a fixed steering coefficient along an internal activation direction (open-loop), it uses a closed-loop feedback controller (PID or RL-based) that adaptively adjusts intervention magnitude online based on the… _(→ WAM: World Action Models face the same fundamental problem when being steered at test time: fixed-coefficient interventions on internal representations cause overcorrection and oscillation, especially for temporal/action concepts (speed, smoothness, force). The…)_ [abs](https://arxiv.org/abs/2606.00269) · [pdf](https://arxiv.org/pdf/2606.00269v1)
- **StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement** — Steering diffusion-based world model imaginations toward high-impact yet plausible outcomes at inference time by optimizing the initial noise with two complementary objectives: a semantic objective (using a VLM to provide gradients toward user-specified target events) and a plausibility objective (preventing the… _(→ WAM: World Action Models must evaluate and improve policies by imagining futures conditioned on actions. StressDream's inference-time noise optimization directly transfers: WAMs could stress-test action policies by steering their imaginations toward plausible but…)_ [abs](https://arxiv.org/abs/2606.00267) · [pdf](https://arxiv.org/pdf/2606.00267v1) · [code](https://github.com/CMU-IntentLab/StressDream)
- **SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning** — Using an internal world model for look-ahead reasoning to proactively predict future safety risks from agent actions, enabling a two-tier defense: proactive tool/capability filtering to constrain hazardous power expansion before execution, and immediate intervention as a fail-safe. The world model is trained via a… _(→ WAM: World Action Models inherently simulate environment dynamics and action consequences, making them a natural substrate for SafeMCP's look-ahead safety reasoning. A WAM could roll out hypothetical action trajectories, evaluate them for safety risks before…)_ [abs](https://arxiv.org/abs/2606.01991) · [pdf](https://arxiv.org/pdf/2606.01991v1)
- **TERRA: Task-Embedded Reasoning and Representation Architecture for Cross-Domain Applications** — TERRA provides a formal theory of cross-domain transfer for action-conditioned latent world models by factoring each domain into thin domain adapters and a shared domain-invariant core, then characterizing transfer quality through approximate MDP homomorphisms measured by lax bisimulation discrepancy and… _(→ WAM: World Action Models are inherently action-conditioned latent predictors, so TERRA's factorization into a shared domain-invariant core plus thin domain adapters offers a direct architectural blueprint: train one WAM core across multiple structured-state…)_ [abs](https://arxiv.org/abs/2606.01520) · [pdf](https://arxiv.org/pdf/2606.01520v1)
- **OptiWorld: Optimal Control for Video World Generation under Physical Constraints** — OptiWorld introduces an inference-time optimal control layer between world state extraction and video rendering: it extracts a compact task-relevant state, plans an optimal trajectory on a continuous manifold that unifies 3D geometry and physical constraints into a single planning geometry, then conditions video… _(→ WAM: WAMs must generate actions that produce physically plausible and optimal world trajectories, but currently lack an explicit mechanism to enforce physical constraints or optimality during action generation. OptiWorld's manifold-based optimal control layer can…)_ [abs](https://arxiv.org/abs/2606.00499) · [pdf](https://arxiv.org/pdf/2606.00499v1)
- **From Zero to Hero: Training-Free Custom Concept Spawning in World Models** — SPAWN exploits a structural property of autoregressive image-to-video backbones where the first slot of context memory is pinned to the reference frame and serves as a foundational anchor for every generated chunk. By swapping this anchor with an external concept latent over a short injection window and then letting… _(→ WAM: World Action Models must simulate environments where specific entities persist coherently across long-horizon, action-conditioned rollouts. The SPAWN anchor-swapping technique could be directly applied to WAMs to ensure that user-specified objects…)_ [abs](https://arxiv.org/abs/2606.02575) · [pdf](https://arxiv.org/pdf/2606.02575v1)
- **VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization** — Using a VLM as a 'teacher' that extracts task-specific rules to formulate differentiable rewards, which then guide a Video Generation Model via test-time online optimization of a lightweight LoRA module—shifting from VLM-as-solver (providing textual plans/instructions) to VLM-as-teacher (providing reward signals for… _(→ WAM: World Action Models face the same core problem as VGMs: they often struggle to faithfully follow task-specific rules and constraints despite generating plausible trajectories. The VLM-as-teacher paradigm transfers directly: a VLM can evaluate whether a WAM's…)_ [abs](https://arxiv.org/abs/2606.02564) · [pdf](https://arxiv.org/pdf/2606.02564v1)
- **RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation** — A structured trustworthiness evaluation framework for video world models that goes beyond normal/feasible scenarios, systematically testing under four scenarios (Normal, Constraint-Sensitive, Counterfactual, Adversarial) with a six-dimensional protocol and 13 fine-grained criteria, revealing that visual coherence and… _(→ WAM: World Action Models must be trustworthy when deployed for real-world decision-making. This benchmark's insight—that models can produce visually plausible outputs while failing on constraint reasoning, counterfactual grounding, and safety—directly applies to…)_ [abs](https://arxiv.org/abs/2606.01600) · [pdf](https://arxiv.org/pdf/2606.01600v1)
- **BRo-JEPA: Learning Modular Arithmetic in Latent Space** — A block-rotation predictor that imposes the circular group structure of modulo-10 arithmetic directly into the latent dynamics of a JEPA-style world model, replacing generic additive operation embeddings with a structured predictor that mirrors the algebraic properties of the action space, enabling zero-shot… _(→ WAM: The core principle—encoding known structural priors of the action/state space into the latent predictor architecture rather than relying on generic function approximators—directly applies to World Action Models. If a WAM's latent dynamics module is designed…)_ [abs](https://arxiv.org/abs/2606.01372) · [pdf](https://arxiv.org/pdf/2606.01372v1) · [code](https://github.com/DL-World-Models/mnist-math)
- **PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking** — PACE is a training-free, test-time method that adaptively selects the execution horizon of action chunks by detecting low-speed transition points in the predicted speed profile, using these as natural replanning boundaries. This exploits the phase-dependent kinematic structure of manipulation trajectories—shortening… _(→ WAM: World Action Models generate sequences of predicted future states/actions, and like action-chunking policies, must decide when to stop open-loop rollout and re-observe the real world. PACE's insight—that the predicted trajectory itself contains phase…)_ [abs](https://arxiv.org/abs/2606.00537) · [pdf](https://arxiv.org/pdf/2606.00537v1)
- **LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation** — Formulating long-horizon autoregressive generation as a retrieval-augmented generation (RAG) problem: instead of conditioning only on the recent sliding window of generated latents (which causes irreversible error accumulation and identity drift), treat the entire history of previously generated latents as a dynamic… _(→ WAM: World Action Models face the same core problem of error accumulation and identity drift during long-horizon action-conditioned rollout prediction — sliding-window attention over recent frames causes irreversible trajectory degradation. The…)_ [abs](https://arxiv.org/abs/2606.02553) · [pdf](https://arxiv.org/pdf/2606.02553v1) · [code](https://github.com/qixinhu11/LongLive-RAG)
- **Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation** — COVRAG introduces a depth-based memory retrieval framework for long-horizon autoregressive generation that uses pretrained 3D priors to construct lightweight target-view coverage maps as 3D memory evidence, and selects memory frames by maximizing residual coverage gain—iteratively retrieving frames that explain… _(→ WAM: World Action Models must maintain consistent world state predictions over long action sequences, facing the same long-horizon drift problem. COVRAG's coverage-maximizing retrieval directly transfers: a WAM can maintain a depth-cached memory of past predicted…)_ [abs](https://arxiv.org/abs/2606.02479) · [pdf](https://arxiv.org/pdf/2606.02479v1)
- **Spatial-Temporal Decoupled Reference Conditioning for Identity-Preserving Text-to-Video Generation** — Spatial-Temporal Decoupled Reference Conditioning (ST-DRC): encoding a reference image into the video VAE latent space and concatenating it with noisy video latents for in-context feature injection, then using TASS-RoPE (Temporal-Adjacent Spatial-Shifted RoPE) to place reference tokens temporally near the video… _(→ WAM: World Action Models must condition on a reference observation (current state) to generate future video/action trajectories. The spatial-temporal decoupling principle directly addresses a key WAM challenge: using the current frame as conditioning without the…)_ [abs](https://arxiv.org/abs/2606.02441) · [pdf](https://arxiv.org/pdf/2606.02441v1) · [code](https://github.com/AliothChen/ST-DRC)
- **Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation** — A human-centric camera parameterization expressed through a Domain-Specific Language (DSL), where camera trajectories are defined relative to the actor's pose and motion (encoding shot size, angle, composition) rather than in absolute world-space coordinates. A multimodal LLM maps natural language + coarse human… _(→ WAM: The core transferable insight is defining actions relative to an agent/actor rather than in absolute world coordinates, creating a more compositional, interpretable, and controllable action space. For WAMs, this suggests parameterizing actions (not just…)_ [abs](https://arxiv.org/abs/2606.01900) · [pdf](https://arxiv.org/pdf/2606.01900v1)
- **Behavior-Invariant Task Representation Learning with Transformer-based World Models for Offline Meta-Reinforcement Learning** — Behavior-invariant task representation learning that extracts task-defining latent variables invariant to the behavior policy that generated the offline data, combined with a conservative value penalty on imagination-based rollouts from a Transformer-based stochastic world model to prevent exploitation of model… _(→ WAM: Two key components transfer directly: (1) The behavior-invariant representation mechanism is crucial for WAMs trained on heterogeneous demonstration data from diverse agents/policies—by explicitly disentangling task identity from behavior patterns, the world…)_ [abs](https://arxiv.org/abs/2606.00780) · [pdf](https://arxiv.org/pdf/2606.00780v1) · [code](https://github.com/QianFY/MetaSTAR)
- **Lumos-Nexus: Efficient Frequency Bridging with Homogeneous Latent Space for Video Unified Models** — A two-stage training-inference decoupling framework where only a lightweight generator is trained end-to-end with the reasoning/understanding block to learn semantic control, while at inference time, Unified Progressive Frequency Bridging (UPFB) progressively hands off generation to a high-capacity pretrained… _(→ WAM: World Action Models require both action-grounded reasoning (understanding how actions affect world states) and high-fidelity visual prediction. Lumos-Nexus's frequency bridging in a homogeneous latent space directly transfers: a WAM could train only a…)_ [abs](https://arxiv.org/abs/2605.31603) · [pdf](https://arxiv.org/pdf/2605.31603v1) · [code](https://github.com/black-forest-labs/flux)
- **TunerDiT: Training-free Progressive Steering of Diffusion Transformer for Multi-Event Video Generation** — Discovery of intrinsic turning points in the DiT denoising trajectory where text conditioning shifts from governing global layout to fine-grained details, enabling training-free progressive steering via two handles: (1) Event-Partitioned Masking that enforces event boundaries while allowing cross-event transition… _(→ WAM: World Action Models must plan and execute long-horizon, multi-action sequences. The insight that diffusion denoising has distinct temporal phases (global trajectory → local refinement) means WAMs could progressively steer action-conditioned generation: early…)_ [abs](https://arxiv.org/abs/2605.31590) · [pdf](https://arxiv.org/pdf/2605.31590v1)
- **AlbedoEdit: Unified Instance-Level Video Editing with Albedo Guidance** — Using intrinsic albedo maps as a disentangled intermediate representation for video editing—albedo is invariant to lighting and free of specular highlights, shadows, and inter-reflections—allowing a single unified model to handle object insertion, removal, and texture editing by conditioning on a user-edited… _(→ WAM: WAMs need to predict world state changes under actions, which requires disentangling intrinsic object properties (material, identity) from transient appearance effects (shadows, reflections, shading). AlbedoEdit's albedo-as-intermediate-representation…)_ [abs](https://arxiv.org/abs/2606.01362) · [pdf](https://arxiv.org/pdf/2606.01362v1)
- **Towards 3D-Aware Video Diffusion Models: Render-Free Human Motion Control with Mesh Tokenization** — A render-free framework that conditions video generation directly on compressed 3D human mesh tokens rather than rendered 2D guidance, preserving full 3D geometric information and enabling joint processing of mesh tokens and video tokens within a unified DiT architecture, forcing the model to reason jointly about… _(→ WAM: World Action Models require precise 3D spatial reasoning to predict action outcomes in physical environments. Mesh tokenization provides a direct pathway to inject structured 3D state representations into the world model without the information loss and…)_ [abs](https://arxiv.org/abs/2606.02000) · [pdf](https://arxiv.org/pdf/2606.02000v1)
- **SafeGen-Bench: Benchmarking Safety in Image-Conditioned Text-to-Video Generation** — SafeGen-Bench identifies and benchmarks the combinatorial safety risk in conditional video generation: individually safe text prompts and safe initial images can combine to produce harmful video content. The benchmark reveals that unimodal guardrails (text-only or image-only safety filters) fail with an 80% failure… _(→ WAM: World Action Models take current world states and actions as inputs to predict future world states. The same combinatorial safety risk applies: a safe action and a safe state individually could combine to produce a harmful predicted future (e.g., a benign…)_ [abs](https://arxiv.org/abs/2606.01481) · [pdf](https://arxiv.org/pdf/2606.01481v1)
- **Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence** — A category-theoretic framework for self-revising agentic systems where discovery is formalized as a verified regime transition u: S_b → S_b' between schema categories. Old artifacts are preserved via left Kan extension (Lan_u I_t) along the transition functor, and genuine novelty is identified as residual content… _(→ WAM: World Action Models must maintain and update internal world models, but currently lack principled mechanisms for restructuring their representational schema when encountering out-of-distribution or structurally novel situations. The regime transition…)_ [abs](https://arxiv.org/abs/2606.01444) · [pdf](https://arxiv.org/pdf/2606.01444v1) · [code](https://github.com/lamm-mit/scienceclaw)

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
