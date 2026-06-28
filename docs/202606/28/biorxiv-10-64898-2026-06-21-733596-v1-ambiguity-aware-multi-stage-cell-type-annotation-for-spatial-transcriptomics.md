---
title: Ambiguity-Aware Multi-Stage Cell-Type Annotation for Spatial Transcriptomics
title_zh: 面向空间转录组学的模糊感知多阶段细胞类型标注
authors: "Mahmud, M. I., Kochat, V., Anzum, H., Satpati, S., Dwarampudi, J. M. R., Rai, K., Banerjee, T."
date: 2026-06-25
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.21.733596v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间转录组细胞类型注释方法，可用于耐药机制研究
tldr: "空间转录组学存在异质性表达和混合细胞类型导致的注释模糊问题。现有方法强制单标签，忽略生物模糊性。本文提出多阶段框架，结合空间特征聚类与约束语言模型推理，通过置信度评分和局部重聚类处理模糊区域。在胆管癌数据上，簇级模糊度从16.1%降至2.27%，细胞级从18.4%降至0.86%，校准改善。空间消融证实拓扑集成优于特征基线，轻量语言模型保证可扩展性和一致性。该方法强调显式处理模糊性对可靠空间注释的重要性。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法强制单一标签，掩盖了细胞类型的生物模糊性，导致过度自信的注释。
method: 提出结合混合空间特征聚类与约束语言模型的多阶段框架，基于标记覆盖度、候选区分度和熵分配置信度。
result: 在胆管癌Xenium数据集上，簇级模糊度从百分之十六点一降至百分之二点二七，细胞级模糊度从百分之十八点四降至百分之零点八六，校准性能得到改善。
conclusion: 该研究结果强调显式处理模糊性对于异质性肿瘤可靠空间注释的重要性和必要性。
---

## 摘要
空间转录组学能够表征完整组织中的细胞组织，但由于异质性表达谱、混合群体和过渡状态，稳健的细胞类型标注仍然具有挑战性。现有方法通常为每个聚类分配单一标签，掩盖了生物学上有意义的模糊性并产生过度自信的分配。我们提出了一种面向空间细胞类型标注的模糊感知多阶段框架。该方法将混合空间特征聚类与基于精选标签集的约束语言模型推理相结合，并根据标记覆盖度、候选分离度和熵分配置信度分数。通过局部重聚类模糊区域选择性优化低置信度聚类，而未解决的聚类则保留为混合状态而非强行标记。应用于来自胆管癌的10x Genomics Xenium空间转录组学数据，所提出的优化将聚类级模糊度从16.1%降至2.27%，细胞级模糊度从18.4%降至0.86%，同时改善了置信度校准。空间消融实验证实，拓扑整合解决了仅基于特征基线的结构模糊性，而通过轻量级语言模型进行的约束推理确保了可扩展且生物学上连贯的注释。这些结果强调了在异质性肿瘤中，明确处理模糊性对于可靠空间标注的重要性。

## Abstract
Spatial transcriptomics enables characterization of cellular organization in intact tissue, but robust cell type annotation remains challenging due to heterogeneous expression profiles, mixed populations, and transitional states. Existing methods often enforce a single label per cluster, obscuring biologically meaningful ambiguity and producing overconfident assignments. We propose an ambiguity-aware, multi-stage framework for spatial cell-type annotation. The method combines hybrid spatial feature clustering with constrained language-model inference over curated label sets, and assigns confidence scores based on marker coverage, candidate separation, and entropy. Low-confidence clusters are selectively refined via local reclustering of ambiguous regions, while unresolved clusters are preserved as mixed rather than forcibly labeled. Applied to 10x Genomics Xenium spatial transcriptomics data from cholangiocarcinoma, the proposed refinement reduces cluster-level ambiguity from 16.1% to 2.27% and cell-level ambiguity from 18.4% to 0.86%, while improving confidence calibration. Spatial ablation confirms that topological integration resolves structural ambiguity over feature-only baselines, while constrained inference via a lightweight language model ensures scalable and biologically coherent annotations. These results highlight the importance of explicit ambiguity handling for reliable spatial annotation in heterogeneous tumors.