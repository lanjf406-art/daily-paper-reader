---
title: "TIDEST: post-imputation differential expression testing for spatial transcriptomics data"
title_zh: TIDEST：空间转录组数据插补后的差异表达检验
authors: "Roeder, K., Lei, J., Testa, L."
date: 2026-06-24
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.19.733432v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间转录组的差异表达检验方法，可用于肿瘤耐药的转录组学研究
tldr: 空间转录组学高分辨率平台常测量有限基因，深度学习可插补缺失基因，但后续差异表达分析因忽略预测不确定性和空间变异而不可靠。TIDEST利用实测基因校正系统误差并调整潜在空间变异，在模拟中有效控制错误率同时保持统计效力。在鼠脑、人胶质母细胞瘤和乳腺癌数据中，TIDEST恢复了被传统分析遗漏或扭曲的生物差异信号，为插补空间转录组提供了可靠的差异表达分析框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 空间转录组插补后差异表达分析因忽视预测不确定性和空间变异导致假阳性或偏差。
method: TIDEST利用实测基因信息校正插补误差，并调整组织结构和细胞类型等潜在空间变异。
result: 模拟表明TIDEST错误率控制远优于现有方法，真实数据中恢复了传统分析遗漏的差异表达信号。
conclusion: TIDEST为空间转录组插补数据的差异表达分析提供了原则性且可靠的方法。
---

## 摘要
空间转录组学能够原位研究组织结构，但许多高分辨率平台仅测量有限的基因面板，导致大部分转录组未被观测。尽管深度学习方法可以从匹配的单细胞参考中重建缺失基因，但由于预测不确定性和空间结构化变异来源通常被忽略，下游差异表达（DE）分析仍不可靠。这些因素会偏倚效应估计并增加假阳性发现。我们提出了TIDEST，一个用于空间转录组插补后进行DE检验的框架。TIDEST利用测量基因的信息纠正重建表达中的系统误差，并调整潜在的空间变异（如组织结构或细胞类型组成），这些变异可能产生生物学组间的虚假差异。在大量模拟中，TIDEST在保持统计效力的同时，比现有方法具有明显更好的错误控制。应用于小鼠大脑、人胶质母细胞瘤和人乳腺癌数据，TIDEST恢复了被传统分析遗漏或扭曲的具有生物学意义的DE信号。TIDEST为重建空间转录组的DE分析提供了一个有原则的框架。

## Abstract
Spatial transcriptomics enables the study of tissue organization in situ, but many high-resolution platforms measure only a limited gene panel, leaving much of the transcriptome unobserved. Although deep learning methods can reconstruct missing genes from matched single-cell references, downstream differential expression (DE) analysis remains unreliable because prediction uncertainty and spatially structured sources of variation are typically ignored. These factors can bias effect estimates and inflate false discoveries. We present TIDEST, a framework for DE testing after spatial transcriptomic imputation. TIDEST uses information from measured genes to correct systematic errors in reconstructed expression and adjusts for latent spatial variation, such as tissue architecture or cell-type composition, that can create spurious differences between biological groups. Across extensive simulations, TIDEST maintains substantially better error control than existing approaches while preserving power. Applications to mouse brain, human glioblastoma, and human breast cancer data recover biologically meaningful DE signals that are missed or distorted by conventional analyses. TIDEST provides a principled framework for DE analysis on reconstructed spatial transcriptomes.