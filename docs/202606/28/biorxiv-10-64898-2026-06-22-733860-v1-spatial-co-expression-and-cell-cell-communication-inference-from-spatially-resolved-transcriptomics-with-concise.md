---
title: Spatial co-expression and cell-cell communication inference from spatially resolved transcriptomics with CONCISE
title_zh: 使用CONCISE从空间分辨转录组学推断空间共表达和细胞间通信
authors: "Zhao, J., Shan, X., Wang, G., Chu, T., Lin, C., Chang, R., Zhao, H."
date: 2026-06-28
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.22.733860v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间细胞间通讯推断方法，可用于肿瘤微环境耐药研究
tldr: 空间转录组学数据中的空间自相关、分子计数变异和测量误差会导致伪空间共表达，使现有细胞通讯推断方法假阳性率高。CONCISE通过联合建模这些混杂因素，采用矩估计与解析假设检验，实现快速且统计严谨的推断。模拟和真实数据表明CONCISE具有校准的推断、稳健的假阳性控制和更高的检测效能。在肠炎和非小细胞肺癌数据中揭示了炎症相关成纤维细胞互作和肿瘤-免疫/基质信号网络。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有空间配体-受体互作推断方法未充分处理空间自相关、分子计数变异和测量误差，导致假阳性率高。
method: CONCISE联合建模空间自相关、分子计数变异、测量误差和空间邻近约束，结合矩估计与解析假设检验进行统计推断。
result: 模拟和真实数据表明CONCISE假阳性率低、推断校准、检测效能高，优于现有方法。
conclusion: CONCISE能可靠推断细胞间通讯，在疾病微环境研究中具有重要应用价值。
---

## 摘要
细胞间通信是组织构建、稳态维持和疾病进展的基础。空间转录组学的最新进展为直接在完整组织中系统地表征配体-受体相互作用提供了前所未有的机会。然而，空间转录组学数据的内在特征，包括空间自相关、总分子计数变异和测量误差，可能诱导虚假的空间共表达并导致假阳性结果膨胀，从而使得稳健的空间配体-受体相互作用推断仍然具有挑战性。大多数现有方法未能充分考虑这些混杂因素，限制了推断细胞通信的可靠性。本文提出CONCISE，一种用于空间约束共表达和配体-受体相互作用推断的统计方法，它联合建模了空间自相关、总分子计数变异、测量误差和空间邻近约束。CONCISE将高效的矩估计与解析假设检验相结合，无需限制性分布假设即可实现快速且统计严谨的推断。通过广泛的模拟、真实数据置换实验以及跨不同空间转录组学平台的生物学动机阴性对照分析，我们表明大多数现有方法呈现了膨胀的假阳性率，而CONCISE实现了良好校准的推断、稳健的假阳性控制和更高的检测效能。将CONCISE应用于来自肠道炎症和非小细胞肺癌的高分辨率MERFISH和CosMx数据集，进一步突显了其在疾病情境中的生物学实用性。CONCISE揭示了肠道炎症期间炎症相关的成纤维细胞特异性相互作用，并描绘了肿瘤微环境内复杂的肿瘤-免疫和肿瘤-基质信号网络。

## Abstract
Cell-cell communication is fundamental to tissue organization, homeostasis, and disease progression. Recent advances in spatial transcriptomics provide unprecedented opportunities to systematically characterize ligand-receptor interactions directly within intact tissues. However, robust inference of spatial ligand-receptor interactions remains challenging because intrinsic features of spatial transcriptomics data, including spatial autocorrelation, variation in total molecular counts, and measurement errors, can induce spurious spatial co-expression and lead to inflated false-positive results. Most existing methods do not adequately account for these confounding factors, limiting the reliability of inferred cellular communication. Here, we present CONCISE, a statistical method for spatially constrained co-expression and ligand-receptor interaction inference that jointly models spatial autocorrelation, variation in total molecular counts, measurement errors, and spatial proximity constraints. CONCISE combines efficient moment-based parameter estimation with analytical hypothesis testing, enabling fast and statistically rigorous inference without restrictive distributional assumptions. Through extensive simulations, real-data permutation experiments, and biologically motivated negative-control analyses across different spatial transcriptomics platforms, we show that most existing methods presented inflated false-positive rates, whereas CONCISE achieved well-calibrated inference, robust false-positive control, and improved detection power. Application of CONCISE to high-resolution MERFISH and CosMx datasets from intestinal inflammation and non-small cell lung cancer further highlights its biological utility in disease contexts. CONCISE uncovered inflammation-associated fibroblast-specific interactions during intestinal inflammation and delineated complex tumor-immune and tumor-stromal signaling networks within the tumor microenvironment.