---
title: A self-supervised DNA foundation model with collapse-resistant multimodal fusion
title_zh: 一种具有抗坍缩多模态融合的自监督DNA基础模型
authors: "Chen, Y."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.19.745697v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 结合多模态融合的DNA基础模型，适用于多组学耐药研究
tldr: 现有基因组基础模型仅用DNA序列，无法充分捕捉调控信息。本文提出自监督DNA多模态基础模型，将序列嵌入与局部/全局染色质可及性融合，并通过全局归一化解决异质性模态对齐坍塌。在调控功能预测任务上显著优于仅序列基线，峰值检测AUPRC提升4.6倍，外部数据集验证有效，且框架可扩展至更多调控模态。
source: biorxiv
selection_source: fresh_fetch
motivation: 序列表示不足，多模态模型常为任务定制，直接融合稀疏峰值与密集序列信号易导致表示坍塌。
method: 设计共享多模态编码器，融合序列嵌入与局部/全局染色质可及性，预训练用掩码重建，并用全局归一化防坍塌。
result: 在调控活性、信号排序和峰值检测上均超DNA-only基线，峰值检测AUPRC提升4.6倍，ClinVar等外部验证有效。
conclusion: 提供可扩展的多模态DNA基础模型框架，为联合建模异构调控信号奠定方法论基础。
---

## 摘要
在DNA序列上预训练的基因组基础模型在一系列任务中取得了强劲表现，但仅基于序列的表征无法完全捕捉由额外以DNA为中心的多模态所反映的调控信息。现有的多模态基因组模型通常针对特定预测任务进行优化，而非学习可跨下游分析复用的共享嵌入。然而，直接融合异质基因组模态颇具挑战，因为稀疏的峰形调控信号与稠密的序列表征在统计结构上存在显著差异，使得朴素的多模态对齐容易退化为接近零的解。我们提出了一种自监督的以DNA为中心的多模态基础模型来解决这一问题，该模型在共享的多模态编码器中整合DNA序列嵌入与局部及全局染色质可及性，以生成可复用的窗口级嵌入，这些嵌入同时支持预训练期间的掩码重建和下游预测任务。我们诊断了这一异质模态对齐失败的原因，并表明全局归一化能显著缓解坍缩，从而实现跨模态的有效联合学习。由此产生的嵌入改善了对调控功能的多个下游评估，包括调控活性预测、调控信号排序和染色质可及性峰检测，在峰检测中相较于仅使用DNA的基线实现了4.6倍的AUPRC提升，并进一步在ClinVar、GTEx eQTL和PBMC caQTL数据集上提升了外部验证效果。该框架可扩展至更多调控模态，为多模态DNA基础模型提供了方法论基础。

## Abstract
Genomic foundation models pretrained on DNA sequence have achieved strong performance across a range of tasks, but sequence-only representations cannot fully capture regulatory information reflected by additional DNA-centric modalities. Existing multimodal genomic models are often optimized for specific prediction tasks rather than for learning reusable embeddings shared across downstream analyses. However, directly fusing heterogeneous genomic modalities is challenging because sparse, peak-shaped regulatory signals and dense sequence representations have markedly different statistical structures, making naive multimodal alignment prone to degenerate near-zero solutions. We present a self-supervised DNA-centric multimodal foundation model that addresses this gap, integrating DNA sequence embeddings with local and global chromatin accessibility in a shared multimodal encoder to produce reusable window-level embeddings that support both masked reconstruction during pre-training and downstream prediction tasks. We diagnose this heterogeneous-modality alignment failure and show that global normalization substantially alleviates collapse, enabling effective joint learning across modalities. The resulting embeddings improve multiple downstream evaluations of regulatory function, including regulatory activity prediction, regulatory signal ranking and chromatin accessibility peak detection, achieving a 4.6-fold AUPRC improvement over the DNA-only baseline in peak detection, and further improving external validation on ClinVar, GTEx eQTL and PBMC caQTL datasets. The framework is extensible to additional regulatory modalities, providing a methodological basis for multimodal DNA foundation models.