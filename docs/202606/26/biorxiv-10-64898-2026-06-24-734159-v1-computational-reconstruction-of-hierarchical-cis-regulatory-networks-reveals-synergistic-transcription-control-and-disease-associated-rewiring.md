---
title: Computational reconstruction of hierarchical cis-regulatory networks reveals synergistic transcription control and disease-associated rewiring
title_zh: 层次顺式调控网络的计算机重建揭示协同转录控制与疾病相关的重连
authors: "Zhu, X., Zhou, X., Zhang, Y., Cai, G., Zhao, W., Zhou, B., Zhou, J., Tang, Z., Liu, J., Zhu, Q., Cao, J., Yang, B., Gu, X., Zhou, Z."
date: 2026-06-26
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.24.734159v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 多组学深度学习框架重建调控网络，可用于肿瘤耐药特征刻画
tldr: 基因调控由分散的顺式调控元件协同驱动，但整合机制不明。本文提出ORIGAMI，一种多组学深度学习框架，将顺式调控建模为潜图推理任务，整合DNA序列、表观信号和染色质结构。推断的调控图呈现层次化和模块化，编码细胞状态特异性功能，实现协同转录控制，并在疾病中发生重连。ORIGAMI推进了基因调控的网络视图，为虚拟细胞建模奠定基础。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法难以从分散的顺式元件重建功能性调控网络，缺乏转录约束。
method: ORIGAMI通过潜图推理整合多组学数据，推断受转录输出约束的调控图。
result: 推断的调控图呈现层次化和模块化，编码细胞状态特异性协同控制，并在疾病中重连。
conclusion: ORIGAMI准确预测扰动转录效应，推进基因调控的网络视图，支持虚拟细胞建模。
---

## 摘要
基因调控源于分散的顺式调控元件之间的协调相互作用，但这些元件如何整合成功能性调控网络并共同调控基因转录仍知之甚少。在此，我们提出ORIGAMI，一个多组学、以基因为中心的深度学习框架，用于重建受转录输出约束的功能性顺式调控网络。ORIGAMI将顺式调控建模形式化为一个潜在图推断任务，该任务整合DNA序列、表观基因组信号和三维染色质先验信息，以推断去噪后的调控图，这些图捕获功能性相互作用而不仅仅是结构邻近性。推断出的调控图表现出不同的拓扑结构，其中层次化和模块化组织编码了细胞状态特异性的功能需求，并实现了协同转录控制。此外，我们表明这些调控架构在疾病背景下经历了可测量的状态依赖性重连。最后，ORIGAMI准确预测了顺式和反式调控扰动的转录后果，并将调控架构的重排与扰动响应联系起来。总之，ORIGAMI推进了基于网络的基因调控观点，并为调控动力学的虚拟细胞建模奠定了基础。

## Abstract
Gene regulation emerges from coordinated interactions among dispersed cis-regulatory elements, yet how these elements integrate into functional regulatory networks and collectively regulate gene transcription remains poorly understood. Here, we present ORIGAMI, a multi-omics, gene-centric deep learning framework that reconstructs functional cis-regulatory networks constrained by transcriptional output. ORIGAMI formulates cis-regulatory modeling as a latent graph inference task, which integrates DNA sequence, epigenomic signals, and three-dimensional chromatin priors to infer denoised regulatory graphs that capture functional interactions rather than structural proximity alone. The inferred regulatory graphs exhibit distinct topological regimes, where hierarchical and modular organization encodes cell-state-specific functional demands and enables synergistic transcriptional control. Furthermore, we show that these regulatory architectures undergo measurable state-dependent rewiring across disease contexts. Finally, ORIGAMI accurately predicts the transcriptional consequences of both cis- and trans-regulatory perturbations and links the rearrangement of regulatory architecture to perturbation response. Together, ORIGAMI advances a network-based view of gene regulation and establishes a foundation for virtual cell modeling of regulatory dynamics.