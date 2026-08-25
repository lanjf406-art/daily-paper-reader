---
title: Decoding Tumour-Specific Rewiring and Synthetic Lethality Through Genome-Scale Metabolic Models
title_zh: 解析肿瘤特异性代谢重连与合成致死：基于全基因组规模代谢模型
authors: "Ibrahim, M., Bhoite, R., Lakshmanan, M., Raman, K."
date: 2026-08-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.21.746174v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 肿瘤转录组分析代谢重编程与合成致死
tldr: 癌症细胞通过代谢重编程支持失控增殖，但跨癌种的系统性代谢改变尚不清楚。本文利用TCGA表达数据构建八种组织的上下文特异性基因组规模代谢模型，通过通量富集分析揭示组织特异性重编程，如乳腺癌中支链氨基酸代谢受抑。进一步提出模型驱动流程识别代谢合成致死反应对，并通过DepMap验证部分基因对。该框架为解码癌症代谢重编程和合成致死脆弱性提供了系统方法。
source: biorxiv
selection_source: fresh_fetch
motivation: 癌症代谢重编程是治疗靶点的重要来源，但缺乏跨癌种的系统级代谢变化图谱和脆弱性鉴定方法。
method: 基于TCGA数据构建八种组织上下文特异性代谢模型，用通量富集分析识别差异通路，并设计流程预测合成致死反应对。
result: 发现多种组织特异性代谢重编程模式，预测并验证了CMPK1-AK、ALDOA-PGD等致癌代谢基因对。
conclusion: 建立了系统解码代谢重编程与合成致死脆弱性的框架，为癌症治疗提供潜在靶点。
---

## 摘要
癌细胞迅速重塑其代谢，从高效的能量产生转向合成代谢过程，以维持不受控制的生长。解析这种代谢转变对于发现新的治疗靶点至关重要。为了描绘跨癌症类型的系统级代谢变化，我们利用癌症基因组图谱（TCGA）的基因表达数据，为八种组织（肺、甲状腺、胃、前列腺、肝、肾、结肠和乳腺）构建了组织特异性的全基因组规模代谢模型。应用基于约束的建模，我们随后通过通量富集分析识别差异调控的通路，揭示了组织特异性的重连：支链氨基酸代谢在乳腺癌中受到抑制；鞘脂代谢在结肠、肾和甲状腺中下调，但在乳腺中上调。我们进一步提出一个模型驱动的流程来识别和表征代谢脆弱性。我们首先识别正常组织中的合成致死反应及其在癌症中对应的单致死对应物，从而能够识别每种癌症的代谢“附带致死”反应对。模型预测的附带致死基因对，包括结肠中的CMPK1-AK、前列腺中的ALDOA-PGD和肝脏模型中的SLC25A26-UQCRB，通过使用DepMap基因必需性数据的计算验证得到了支持。随后，我们展示了如何解释癌症组织中的代谢重连，同时考虑任何附带致死对。总之，我们的结果建立了一个系统性框架，用于解析癌症中的代谢重连和合成致死脆弱性。

## Abstract
Cancer cells rapidly rewire their metabolism, from efficient energy production toward anabolic processes, to sustain uncontrolled growth. Decoding such metabolic shifts is essential for uncovering novel therapeutic targets. To map systems-level metabolic changes across cancer types, we built context-specific genome-scale metabolic models for eight tissues (lung, thyroid, stomach, prostate, liver, kidney, colon, and breast) using gene expression data from The Cancer Genome Atlas (TCGA). Applying constraint-based modelling, we then identified differentially regulated pathways through flux enrichment analysis, revealing tissue-specific rewiring: branched chain amino acid metabolism was suppressed in breast cancer; sphingolipid metabolism was downregulated in colon, kidney, and thyroid but upregulated in breast. We further propose a model-driven pipeline to identify and characterise metabolic vulnerabilities. We first identify synthetic lethal reactions in normal tissues and their corresponding single lethal counterparts in cancers, thereby enabling the identification of metabolic "collateral lethal" reaction pairs for each cancer. Model-predicted collateral lethal gene pairs, including CMPK1-AK in colon, ALDOA-PGD in prostate, and SLC25A26-UQCRB in liver models, were supported through computational validation using DepMap data on gene essentiality. Subsequently, we show how to interpret metabolic rewiring in cancer tissues while accounting for any collateral lethal pairs. In summary, our results establish a systemic framework for decoding metabolic rewiring and synthetic lethal vulnerabilities in cancer.