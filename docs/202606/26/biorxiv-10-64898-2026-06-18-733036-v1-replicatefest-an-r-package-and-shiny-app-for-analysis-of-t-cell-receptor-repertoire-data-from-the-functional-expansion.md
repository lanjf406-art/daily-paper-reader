---
title: "replicateFest: An R Package and Shiny App for Analysis of T Cell Receptor Repertoire Data from the Functional Expansion"
title_zh: "replicateFest: 用于功能扩增的T细胞受体库数据分析的R包与Shiny应用程序"
authors: "Danilova, L., Favorov, A., Smith, K. N., Cope, L."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.18.733036v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: TCR库分析工具用于评估免疫检查点阻断疗效
tldr: 基于FEST的TCR-seq分析因生物和技术重复引入变异性，影响重现性。replicateFest框架通过Fisher精确检验或负二项模型识别显著扩增的克隆型，区分FEST扩增和阳性克隆型。合成数据验证准确，HIV-1数据重现原结果。提供R包和Shiny应用，支持重复样本分析。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有工具缺乏对FEST试验中重复样本的分析能力，导致重现性挑战。
method: 对无重复数据用Fisher精确检验，有重复用负二项模型，返回调整p值和优势比。
result: 合成及HIV-1数据验证表明能准确识别抗原特异性克隆型，重现原研究结果。
conclusion: replicateFest作为免费R包和Shiny应用，填补了FEST数据重复分析的工具空白。
---

## 摘要
动机基于特异性T细胞功能扩增（FEST）的检测方法结合短期肽刺激与TCR测序，以识别对抗原刺激产生响应的克隆型。这些方法在检测新抗原特异性T细胞反应、指导疫苗开发及评估检查点阻断疗效方面已被证明价值巨大。然而，生物学和技术重复引入的变异性给可重复性和解读带来挑战，现有计算工具并未解决这些检测中的重复级别分析问题。

结果我们开发了replicateFest，一个以R包和Shiny Web应用形式实现的计算框架，用于分析有或没有重复的FEST-based TCR-seq数据。replicateFest对非重复数据集应用Fisher精确检验，对重复实验应用负二项模型，返回校正后的p值和优势比，以识别在抗原刺激条件下显著扩增的克隆型。该框架区分FEST扩增克隆型（相对于无抗原对照）和FEST阳性克隆型（相对于所有其他条件扩增）。使用合成数据集验证确认了对抗原特异性克隆型的准确检测。应用于已发表的HIV-1表位刺激数据重现了原始发现，并展示了replicateFest在可重复性评估和质量控制方面的实用性。

可用性与实现replicateFest在Apache-2.0许可下免费提供，作为R包位于https://github.com/OncologyQS/replicateFest，并作为交互式Shiny应用程序位于http://www.stat-apps.onc.jhmi.edu/FEST/。

## Abstract
MotivationThe Functional Expansion of Specific T cell (FEST)-based assays combine short-term peptide stimulation with TCR sequencing to identify clonotypes that expand in response to specific antigens. These approaches have proven invaluable for detecting neoantigen-specific T cell responses, guiding vaccine development, and assessing checkpoint blockade efficacy. However, variability introduced by biological and technical replicates poses challenges for reproducibility and interpretation, and existing computational tools do not address replicate-level analysis in these assays.

ResultsWe developed replicateFest, a computational framework implemented as an R package and Shiny web application, to analyze FEST-based TCR-seq data with and without replicates. replicateFest applies Fishers exact test for non-replicate datasets and negative binomial modeling for replicate experiments, returning adjusted p-values and odds ratios to identify clonotypes significantly expanded in antigen-stimulated conditions. The framework distinguishes FEST-expanded clonotypes (relative to a no-antigen control) and FEST-positive clonotypes (expanded compared to all other conditions). Validation using synthetic datasets confirmed accurate detection of antigen-specific clonotypes. Application to published HIV-1 epitope stimulation data reproduced original findings and demonstrated replicateFests utility for reproducibility assessment and quality control.

Availability and ImplementationreplicateFest is freely available under the Apache-2.0 license as an R package at https://github.com/OncologyQS/replicateFest and as an interactive Shiny application at http://www.stat-apps.onc.jhmi.edu/FEST/.