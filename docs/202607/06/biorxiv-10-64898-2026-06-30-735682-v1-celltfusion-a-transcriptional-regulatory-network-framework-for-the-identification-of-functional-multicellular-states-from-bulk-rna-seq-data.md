---
title: "CellTFusion: a transcriptional regulatory network framework for the identification of functional multicellular states from bulk RNA-seq data"
title_zh: CellTFusion：一个从批量RNA-seq数据中识别功能性多细胞状态的转录调控网络框架
authors: "Hurtado, M., Pancaldi, V."
date: 2026-07-05
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.30.735682v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 通过bulk RNA-seq转录调控网络解析肿瘤微环境
tldr: 现有大量bulk RNA-seq数据分析方法将细胞类型丰度、通路活性和转录因子活性视为独立信息，忽略协调性调控程序。CellTFusion框架通过整合细胞类型反卷积与转录调控网络分析，从bulk数据中识别功能性的多细胞状态，将患者表征为这些状态的加权组合。在黑色素瘤和膀胱癌队列中，CellTFusion发现了与免疫治疗反应呈相反关联的复发性TME程序，且跨队列迁移性优于现有工具。该框架首次实现了从bulk数据中联合建模多细胞协调程序，提升了TME表征能力。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法将细胞类型、通路和TF活性独立分析，忽略了定义功能性多细胞状态的协调调控程序。
method: 整合细胞类型反卷积与转录调控网络分析，将每个患者表示为多种功能性多细胞状态的加权组合。
result: 在黑色素瘤和膀胱癌数据中，识别出与免疫治疗反应有相反关联的复发性TME程序，跨队列迁移性优于现有工具。
conclusion: CellTFusion通过联合多变量建模揭示了新的TME功能状态，提高了bulk数据对肿瘤微环境的解析能力。
---

## 摘要
批量RNA-seq仍然是肿瘤微环境（TME）表征中最易获取的转录组平台，然而现有的计算方法将细胞类型丰度、通路活性和转录因子（TF）活性视为独立的信息来源，忽略了定义功能性多细胞状态的协调调控程序。在此，我们介绍了CellTFusion，一个将细胞类型反卷积与来自批量RNA-seq数据的转录调控网络分析相结合的框架，用于识别功能性多细胞群体。CellTFusion生成TME的混合表示，其中每个患者被描述为状态的加权组合，每个状态捕获一个独特的协调标志程序。应用于黑色素瘤和膀胱癌队列，CellTFusion识别出与免疫治疗反应具有相反关联的反复出现的TME程序，这些程序仅通过联合多变量建模才出现，并且与已建立的TME表征工具相比，展示了优越的跨队列可迁移性。

## Abstract
Bulk RNA-seq remains the most accessible transcriptomic platform for tumor microenvironment (TME) characterization, yet existing computational approaches treat cell type abundance, pathway activity, and transcription factor (TF) activity as independent sources of information, missing the coordinated regulatory programs that define functional multicellular states. Here we introduce CellTFusion, a framework that integrates cell type deconvolution with transcriptional regulatory network analysis from bulk RNA-seq data to identify functional multicellular groups. CellTFusion produces a mixture representation of the TME in which each patient is described as a weighted combination of states, each capturing a distinct coordinated hallmark program. Applied to melanoma and bladder cancer cohorts, CellTFusion identified recurrent TME programs with opposing associations with immunotherapy responses that only emerged through joint multivariate modeling, and demonstrated superior cross-cohort transferability compared to established TME characterization tools.