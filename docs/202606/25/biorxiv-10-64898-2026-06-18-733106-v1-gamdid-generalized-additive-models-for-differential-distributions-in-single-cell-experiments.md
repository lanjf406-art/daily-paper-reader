---
title: "gamdid: generalized additive models for differential distributions in single cell experiments"
title_zh: "gamdid: 单细胞实验中差异分布的广义可加模型"
authors: "Clement, L., Beerland, L., Martens, L., Vanderaa, C., Vandenbulcke, S."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.18.733106v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞实验差异分布分析方法
tldr: 单细胞蛋白质组学数据中，现有差异分析方法局限于检测均值变化，忽略了细胞间分布形状的生物学差异。论文提出gamdid框架，基于广义加性模型灵活建模蛋白丰度分布，实现差异分布分析。在基准测试中，gamdid有效控制假发现率，检测形状差异的性能显著优于现有方法，并支持多组比较与可视化。该工作为单细胞蛋白组学提供了针对形状差异的全新分析工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法仅检测均值差异，忽略单细胞数据中重要的分布形状差异。
method: 提出gamdid，基于广义加性模型灵活建模分布，进行差异推断与可视化。
result: 半合成基准测试中假发现率控制保守，形状差异检测性能大幅优于竞争方法。
conclusion: gamdid为单细胞蛋白质组学差异分布分析提供了有效工具，支持多组比较。
---

## 摘要
单细胞蛋白质组学（SCP）能够在数百至数千个单细胞中测量蛋白质丰度，为研究细胞异质性提供了前所未有的分辨率。然而，现有的差异丰度（DA）方法仅限于检测均值表达的变化，而忽略了形状上具有生物学意义的差异。事实上，SCP的独特优势在于识别群体中单个细胞之间的差异，这些差异通常表现为形状差异而非均值表达差异。因此，我们在此提出gamdid（面向差异分布的广义可加模型），这是一种新颖的统计框架和R包，用于SCP数据中的差异分布（DD）分析。gamdid基于广义可加模型（GAMs），能够灵活地对异质性分布进行建模、执行推断并提供可解释的可视化。通过在两个SCP数据集上进行的半合成基准测试，gamdid展示了保守的假发现率控制，在形状差异方面显著优于竞争方法，同时在均值偏移方面性能相当。一项加标病例研究进一步证明了gamdid及其可解释可视化的实用性。在DD方法中，gamdid独特地支持超过两个组别的综合检验，并通过逐步检验进行事后两两比较，且专门针对蛋白质组学丰度数据定制。

## Abstract
Single-cell proteomics (SCP) generates protein abundance measurements across hundreds to thousands of individual cells, offering unprecedented resolution to study cellular heterogeneity. However, existing differential abundance (DA) methods are limited to detecting shifts in mean expression, leaving biologically relevant differences in shape undetected. Indeed, the specific power of SCP is to identify differences between individual cells in a population, which are typically only found as shape differences rather than in mean expression. We here therefore present gamdid (generalized additive models for differential distributions), a novel statistical framework and R package for differential distribution (DD) analysis in SCP data. gamdid is based on generalized additive models (GAMs) to flexibly model heterogeneous distributions, perform inference and provide interpretable visualizations. Through semi-synthetic benchmarking on two SCP datasets, gamdid demonstrates conservative false discovery rate control and substantially outperforms competing methods for differences in shape, while achieving comparable performance for mean shifts. A spike-in case study further demonstrates the utility of gamdid and its interpretable visualization. Uniquely among DD methods, gamdid supports omnibus testing across more than two groups, with post-hoc pairwise comparisons via stagewise testing, and is specifically tailored for proteomics abundance data.