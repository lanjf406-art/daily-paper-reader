---
title: Spatial co-expression and cell-cell communication inference from spatially resolved transcriptomics with CONCISE
title_zh: CONCISE：基于空间分辨转录组学的空间共表达和细胞间通讯推断
authors: "Zhao, J., Shan, X., Wang, G., Chu, T., Lin, C., Chang, R., Zhao, H."
date: 2026-06-28
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.22.733860v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间细胞间通讯推断，与肿瘤微环境和耐药相关
tldr: 细胞间通信对组织功能至关重要，空间转录组学为研究配体-受体相互作用提供了机遇，但现有方法因忽略空间自相关、分子计数变异和测量误差等混杂因素而假阳性率高。本文提出CONCISE，一种联合建模上述因素及空间邻近约束的统计方法，通过矩估计和解析假设检验实现快速、稳健的推断。模拟和真实数据验证表明，CONCISE能有效控制假阳性并提高检测效能。应用于肠炎和肺癌的高分辨率空间数据，揭示了炎症相关成纤维细胞特异性互作及肿瘤微环境中的复杂信号网络。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有空间转录组学推断细胞通信的方法因忽略空间自相关等混杂因素导致假阳性率高，亟需稳健的统计方法。
method: CONCISE联合建模空间自相关、总分子计数变异、测量误差和空间邻近约束，采用矩估计和解析假设检验实现高效统计推断。
result: 在模拟和真实数据中假阳性率显著低于现有方法，检测效能提升；应用于肠炎和肺癌数据发现炎症相关成纤维细胞特异性互作及肿瘤微环境信号网络。
conclusion: CONCISE提供了校准的空间共表达和配体-受体推断，有助于可靠解析组织微环境中的细胞通信。
---

## 摘要
细胞间通讯是组织形成、稳态维持和疾病进展的基础。空间转录组学的最新进展为直接在完整组织中系统地表征配体-受体相互作用提供了前所未有的机会。然而，空间转录组数据的固有特征，包括空间自相关、总分子计数变异和测量误差，可能引发伪空间共表达并导致假阳性结果膨胀，使得稳健的空间配体-受体相互作用推断仍具挑战性。现有方法大多未能充分考虑这些混杂因素，从而限制了推断细胞通讯的可靠性。本文提出CONCISE，一种用于空间约束共表达和配体-受体相互作用推断的统计方法，该方法联合建模了空间自相关、总分子计数变异、测量误差和空间邻近性约束。CONCISE将高效的基于矩的参数估计与解析假设检验相结合，能够在无严格分布假设下实现快速且统计严格的推断。通过在不同空间转录组平台上的广泛模拟、真实数据置换实验和生物学动机的阴性对照分析，我们显示大多数现有方法具有膨胀的假阳性率，而CONCISE实现了校准良好的推断、稳健的假阳性控制以及改进的检测能力。将CONCISE应用于来自肠道炎症和非小细胞肺癌的高分辨率MERFISH和CosMx数据集，进一步凸显了其在疾病背景下的生物学实用性。CONCISE揭示了肠道炎症期间炎症相关成纤维细胞特异性相互作用，并描绘了肿瘤微环境中复杂的肿瘤-免疫和肿瘤-基质信号网络。

## Abstract
Cell-cell communication is fundamental to tissue organization, homeostasis, and disease progression. Recent advances in spatial transcriptomics provide unprecedented opportunities to systematically characterize ligand-receptor interactions directly within intact tissues. However, robust inference of spatial ligand-receptor interactions remains challenging because intrinsic features of spatial transcriptomics data, including spatial autocorrelation, variation in total molecular counts, and measurement errors, can induce spurious spatial co-expression and lead to inflated false-positive results. Most existing methods do not adequately account for these confounding factors, limiting the reliability of inferred cellular communication. Here, we present CONCISE, a statistical method for spatially constrained co-expression and ligand-receptor interaction inference that jointly models spatial autocorrelation, variation in total molecular counts, measurement errors, and spatial proximity constraints. CONCISE combines efficient moment-based parameter estimation with analytical hypothesis testing, enabling fast and statistically rigorous inference without restrictive distributional assumptions. Through extensive simulations, real-data permutation experiments, and biologically motivated negative-control analyses across different spatial transcriptomics platforms, we show that most existing methods presented inflated false-positive rates, whereas CONCISE achieved well-calibrated inference, robust false-positive control, and improved detection power. Application of CONCISE to high-resolution MERFISH and CosMx datasets from intestinal inflammation and non-small cell lung cancer further highlights its biological utility in disease contexts. CONCISE uncovered inflammation-associated fibroblast-specific interactions during intestinal inflammation and delineated complex tumor-immune and tumor-stromal signaling networks within the tumor microenvironment.