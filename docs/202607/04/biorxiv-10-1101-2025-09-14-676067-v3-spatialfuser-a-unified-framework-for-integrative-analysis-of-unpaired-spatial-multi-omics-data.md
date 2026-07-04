---
title: "SpatialFuser: a unified framework for integrative analysis of unpaired spatial multi-omics data"
title_zh: SpatialFuser：一个用于非配对空间多组学数据整合分析的统一框架
authors: "Cai, W., Li, W."
date: 2026-07-02
pdf: "https://www.biorxiv.org/content/10.1101/2025.09.14.676067v3.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间多组学整合分析肿瘤微环境
tldr: 空间多组学数据整合面临未配对和异构挑战。SpatialFuser深度学习框架通过多尺度图自编码器、几何预匹配和迭代匹配融合模块，实现跨模态对齐与整合。在空间域识别、跨切片对齐和多组学整合上超越现有方法，解析精细空间模式并揭示互补信号。该框架通用且可扩展，适用于新兴组学。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法难以整合未配对的空间多组学数据，需要统一框架解决跨模态对齐和融合。
method: SpatialFuser包含MCGATE多尺度图自编码器、几何预匹配和迭代匹配融合模块，利用最优传输和对比学习。
result: 在多种基准测试中优于现有方法，成功解析空间分子模式、发育动态并恢复弱相关模态间的生物变异。
conclusion: SpatialFuser是通用且可扩展的框架，适用于多种空间组学整合分析场景。
---

## 摘要
空间多组学技术的最新进展为解读组织微环境中的分子特征提供了前所未有的机遇，但跨异构数据集的整合分析仍然具有挑战性。在此，我们提出SpatialFuser，一个深度学习框架，用于跨表观组学、转录组学、蛋白质组学和代谢组学的非配对空间多组学数据的整合分析。SpatialFuser包含三个协同模块：MCGATE，一种多头协作图注意力自编码器，学习多尺度空间表示以解析超出预定义空间邻域的精细空间异质性；一个可选的几何预匹配模块，在组织几何不匹配情况下提供粗初始化；以及一个迭代匹配-融合模块，将几何约束的最优传输匹配与对比学习引导的模态融合相结合，用于跨切片对齐与整合。系统性基准测试表明，在空间域识别、跨切片对齐和多组学整合方面，SpatialFuser与现有最先进方法相比展现出优越的性能和可靠性。在真实数据集上的应用表明，SpatialFuser能够解析精确的空间分子模式，揭示发育动态，并恢复跨模态的互补信号。我们的方法对弱相关模态进行跨分辨率整合，进一步揭示了先前被掩盖的生物学变异。我们框架的通用性和多功能性使得能够定制分析场景，并有望拓展至新兴组学。

## Abstract
Recent advances in spatial multi-omics technologies provide unprecedented opportunities to interpret molecular features in tissue microenvironments, but integrative analysis across heterogeneous datasets remains challenging. Here we present SpatialFuser, a deep learning framework for integrative analysis of unpaired spatial multi-omics data across epigenomics, transcriptomics, proteomics, and metabolomics. SpatialFuser consists of three coordinated modules: MCGATE, a Multi-head Collaborative Graph Attention auToEncoder that learns multi-scale spatial representations to decipher fine-grained spatial heterogeneity beyond predefined spatial neighbourhoods; an optional geometric pre-matching module that provides coarse initialization under tissue geometry mismatch; and an iterative matching-fusion module that couples geometry-constrained optimal transport matching with contrastive-learning-guided modality fusion for cross-slice alignment and integration. Systematic benchmarks demonstrate superior performance and reliability compared with existing state-of-the-art methods in spatial domain identification, cross-slice alignment, and multi-omics integration. Applications to real datasets illustrate that SpatialFuser resolves precise spatial molecular patterns, reveals developmental dynamics, and recovers complementary signals across modalities. Cross-resolution integration of weakly correlated modalities by our method further uncovers previously obscured biological variation. The generalizability and versatility of our framework enable customized analytical scenarios and potential extension for emerging omics.