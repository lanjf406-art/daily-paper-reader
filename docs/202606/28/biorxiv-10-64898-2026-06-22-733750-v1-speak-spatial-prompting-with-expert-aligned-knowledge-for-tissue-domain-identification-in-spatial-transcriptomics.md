---
title: "SPEAK: Spatial Prompting with Expert Aligned Knowledge for Tissue Domain Identification in Spatial Transcriptomics"
title_zh: "SPEAK: 基于专家对齐知识的空间提示在空间转录组学组织区域识别中的应用"
authors: "Wei, H., Luo, X., Yu, H., Liang, J., Yang, L., Sauler, M., Kaminski, N., Popa, A., Yan, X."
date: 2026-06-26
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.22.733750v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间域识别方法可用于肿瘤微环境耐药分析
tldr: 空间转录组学数据需要识别组织区域。SPEAK利用大语言模型和专家知识，构建空间上下文提示实现零样本推断和专家引导微调。在STARmap等多个数据集上，SPEAK在精度、鲁棒性和可解释性上优于现有方法。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法在空间域识别中依赖手工特征，难以利用先验知识，且泛化性差。
method: 构造包含细胞类型和标记基因的空间上下文提示，通过两阶段提示实现零样本、微调和原型更新。
result: 在STARmap、Visium等数据上，SPEAK的域预测准确率显著高于现有方法，且对有限先验知识鲁棒。
conclusion: SPEAK有效融合LLM和专家知识，提升了空间域识别的准确性与可解释性，并能泛化至其他组织切片。
---

## 摘要
空间分辨转录组学（SRT）数据需要空间区域识别，以实现组织微环境特异性的下游分析。本文提出SPEAK（基于专家对齐知识的空间提示），一种基于大语言模型（LLM）的方法，通过利用LLM和人类专家的先验知识，从SRT数据中识别空间区域。SPEAK根据每个细胞/点的邻近细胞的细胞类型和标记基因构建空间上下文提示，通过两阶段提示实现零样本推理、专家引导微调和原型更新。在STARmap、Visium、MERFISH和Xenium数据集上的应用表明，SPEAK在区域预测准确性、对有限先验知识的鲁棒性、生物学可解释性以及高效专家引导微调及泛化到其他组织切片的能力方面优于现有空间区域识别方法。

## Abstract
Spatially resolved transcriptomic (SRT) data requires spatial domain identification to enable tissue microenvironment-specific downstream analyses. Here we present SPEAK (Spatial Prompting with Expert-Aligned Knowledge), a large language model (LLM) -based method to identify spatial domains from SRT data by taking advantage of the prior knowledge from both LLM and human experts. SPEAK constructs a spatial context prompt for each cell/spot based on cell types and marker genes of its neighboring cells, enabling zero-shot inference, expert-guided fine-tuning, and prototype updating through two-stage prompting. Applications to STARmap, Visium, MERFISH and Xenium datasets showed advantages of SPEAK over existing spatial domain identification methods in domain prediction accuracy, robustness to limited prior knowledge, biological interpretability, and capacity for efficient expert-guided fine-tuning with generalizability to other tissue sections.