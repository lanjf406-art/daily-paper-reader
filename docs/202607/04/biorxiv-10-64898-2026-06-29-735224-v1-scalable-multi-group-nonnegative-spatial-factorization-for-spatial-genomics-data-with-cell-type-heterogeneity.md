---
title: Scalable multi-group nonnegative spatial factorization for spatial genomics data with cell-type heterogeneity
title_zh: 可扩展的多组非负空间分解用于具有细胞类型异质性的空间基因组学数据
authors: "Chumpitaz-Diaz, L., Shrestha, P., Engelhardt, B. E."
date: 2026-07-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.29.735224v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间转录组学方法可用于肿瘤微环境耐药研究
tldr: 空间转录组学数据中现有方法难以区分空间基因模式和细胞类型差异。本文提出可扩展的多组非负空间分解（smNSF），通过多组高斯过程先验结合细胞类型标签，实现细胞类型特定的空间变异捕获。在7个数据集上，smNSF恢复稀疏可解释的空间因子，并通过条件后验组织为细胞类型富集、特异和通用程序。该方法提升了空间数据分解的可解释性，支持细胞类型感知的空间分析。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有维度缩减方法忽略空间信息或混淆细胞类型差异与空间模式，影响生物学可解释性。
method: 提出smNSF，使用多组高斯过程先验集成空间坐标和细胞类型标签，结合非负性约束，并通过变分推理实现可扩展优化。
result: 在7个跨技术跨组织数据集中，smNSF恢复稀疏可解释因子，并通过条件后验揭示细胞类型富集、特异及通用空间程序。
conclusion: smNSF实现了细胞类型感知的空间分解，支持基于细胞类型条件后验的空间模式与细胞身份关系探索。
---

## 摘要
空间转录组学（ST）技术能够研究组织空间背景下的基因表达，从而揭示组织结构、细胞相互作用和疾病进展。然而，现有的降维方法常常忽视空间信息，或者难以区分空间基因模式与由细胞类型差异驱动的模式，从而限制了生物学可解释性，因为基因表达模式的差异与细胞类型比例的差异被混在一起。为了解决这些挑战，我们引入了可扩展的多组非负空间分解（smNSF），这是一个计算上可行的概率框架，将空间坐标和细胞类型标签整合到一个统一的矩阵分解模型中。通过使用多组高斯过程（MGGPs）作为先验，我们的模型以细胞类型特异的方式捕获复杂的空间变异，同时强制非负性以增强可解释性。我们为MGGPs开发了一个变分推断框架，支持可扩展优化并提高smNSF的数值稳定性。在涵盖不同技术和组织的七个空间转录组学数据集中，smNSF恢复了稀疏、可解释的空间因子，并通过其细胞类型条件后验，将它们组织成细胞类型富集、细胞类型特异和通用的空间程序，而这些仅从边缘因子中并不明显。给定ST数据中的细胞类型标签，smNSF能够实现细胞类型感知的空间分解，并支持细胞类型条件后验，用于在计算机上探索空间模式与细胞身份之间的关系。

## Abstract
Spatial transcriptomics (ST) technologies enable the study of gene expression within the spatial context of tissues, providing insights into tissue structure, cellular interactions, and disease progression. However, existing dimension reduction methods often overlook spatial information or struggle to distinguish spatial gene patterns from those driven by cell-type differences, limiting biological interpretability by convolving differences in gene expression patterns with differences in cell-type proportions. To address these challenges, we introduce the scalable multi-group nonnegative spatial factorization (smNSF), a computationally-tractable probabilistic framework that integrates spatial coordinates and cell-type labels into a unified matrix factorization model. By using multi-group Gaussian processes (MGGPs) as priors, our model captures complex spatial variation in a cell-type specific way while enforcing nonnegativity to enhance interpretability. We develop a variational inference framework for MGGPs that supports scalable optimization and improves the numerical stability of smNSF. Across seven spatial transcriptomics datasets spanning diverse technologies and tissues, smNSF recovers sparse, interpretable spatial factors and, through its cell-type conditional posteriors, organizes them into cell-type enriched, cell-type specific, and universal spatial programs that are not apparent from marginal factors alone. Given cell-type labels in ST data, smNSF enables cell-type aware spatial decompositions and supports cell-type conditional posteriors for in silico exploration of relationships between spatial patterns and cellular identity.