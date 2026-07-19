---
title: "replicateFest: An R Package and Shiny App for Analysis of T Cell Receptor Repertoire Data from the Functional Expansion"
title_zh: replicateFest：用于分析功能性扩增的T细胞受体库数据的R包和Shiny应用程序
authors: "Danilova, L., Favorov, A., Smith, K. N., Cope, L."
date: 2026-07-13
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.18.733036v3.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: TCR库分析工具，用于评估免疫反应，与耐药机制相关
tldr: 基于功能的特异性T细胞扩增（FEST）实验结合短肽刺激与TCR测序，但生物学和技术重复引入变异性，现有工具缺乏重复样本层面分析。我们开发了replicateFest R包和Shiny应用，采用Fisher精确检验（无重复）和负二项模型（有重复）识别抗原刺激下显著扩增的克隆型，区分FEST扩增和FEST阳性克隆型。在合成数据和HIV-1表位刺激数据中验证了准确性，重现原始发现，并提供质量控制与可重复性评估。工具免费开源，可直接用于FEST数据分析。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-06-18-733036-v3/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1301, \"height\": 999, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-06-18-733036-v3/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1272, \"height\": 934, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-06-18-733036-v3/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1764, \"height\": 608, \"label\": \"Table\"}]"
motivation: FEST分析中重复样本的变异性影响结果可重复性，现有工具未提供针对重复样本的专门统计方法。
method: 采用Fisher精确检验（无重复）和负二项模型（有重复），计算校正p值和比值比，区分FEST扩增克隆型与FEST阳性克隆型。
result: 在合成数据中准确检测抗原特异性克隆型；在HIV-1数据中重现原始结果，并验证了可重复性评估和质控功能。
conclusion: replicateFest填补了FEST数据重复样本分析的空白，提供易用的R包和Shiny界面，推动免疫组库研究的可重复性。
---

## 摘要
动机：基于特异性T细胞功能性扩增（FEST）的检测方法将短期肽刺激与TCR测序相结合，以识别响应特定抗原而扩增的克隆型。这些方法已被证明在检测新抗原特异性T细胞反应、指导疫苗开发和评估检查点阻断疗效方面具有不可估量的价值。然而，生物学和技术重复引入的变异对可重复性和解读构成了挑战，现有的计算工具未能解决这些检测中的重复水平分析。

结果：我们开发了replicateFest，这是一个以R包和Shiny Web应用程序形式实现的计算框架，用于分析有或无重复的基于FEST的TCR-seq数据。replicateFest对非重复数据集应用Fisher精确检验，对重复实验应用负二项模型，返回调整后的p值和优势比，以识别在抗原刺激条件下显著扩增的克隆型。该框架区分了FEST扩增的克隆型（相对于无抗原对照）和FEST阳性的克隆型（相对于所有其他条件扩增）。使用合成数据集进行的验证确认了对抗原特异性克隆型的准确检测。应用于已发表的HIV-1表位刺激数据重现了原始发现，并证明了replicateFest在可重复性评估和质量控制方面的实用性。

可用性和实现：replicateFest在Apache-2.0许可证下免费提供，作为R包位于https://github.com/OncologyQS/replicateFest，并作为交互式Shiny应用程序位于http://www.stat-apps.onc.jhmi.edu/FEST/。

## Abstract
MotivationThe Functional Expansion of Specific T cell (FEST)-based assays combine short-term peptide stimulation with TCR sequencing to identify clonotypes that expand in response to specific antigens. These approaches have proven invaluable for detecting neoantigen-specific T cell responses, guiding vaccine development, and assessing checkpoint blockade efficacy. However, variability introduced by biological and technical replicates poses challenges for reproducibility and interpretation, and existing computational tools do not address replicate-level analysis in these assays.

ResultsWe developed replicateFest, a computational framework implemented as an R package and Shiny web application, to analyze FEST-based TCR-seq data with and without replicates. replicateFest applies Fishers exact test for non-replicate datasets and negative binomial modeling for replicate experiments, returning adjusted p-values and odds ratios to identify clonotypes significantly expanded in antigen-stimulated conditions. The framework distinguishes FEST-expanded clonotypes (relative to a no-antigen control) and FEST-positive clonotypes (expanded compared to all other conditions). Validation using synthetic datasets confirmed accurate detection of antigen-specific clonotypes. Application to published HIV-1 epitope stimulation data reproduced original findings and demonstrated replicateFests utility for reproducibility assessment and quality control.

Availability and ImplementationreplicateFest is freely available under the Apache-2.0 license as an R package at https://github.com/OncologyQS/replicateFest and as an interactive Shiny application at http://www.stat-apps.onc.jhmi.edu/FEST/.