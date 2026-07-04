---
title: Phenotypic inference from sparse tumor genomes informs an explainable deep-learning model for cancer prognosis
title_zh: 从稀疏肿瘤基因组进行表型推断为癌症预后提供可解释的深度学习模型
authors: "Grant, S., Nath, A."
date: 2026-07-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.26.734894v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 基于肿瘤基因组的机器学习表型推断框架，可应用于耐药预测
tldr: "体细胞基因组变异在癌症中广泛应用，但临床效用有限且现有AI模型可解释性差。本文开发PhenoMap框架，从稀疏肿瘤基因组推断表型状态，结合PhenoSurv深度生存模型，整合表型重建和生存损失进行学习。在9,000例泛癌数据中准确重建通路活性和癌症表型，捕获乳腺癌、肺癌、脑癌的分子亚型和耐药通路，预后性能优于现有方法。该框架提供从基因到表型的可解释预后标志，发现NOTCH1信号和SMARCA4突变等新预后因子，推动精准肿瘤学临床转化。"
source: biorxiv
selection_source: fresh_fetch
motivation: 体细胞变异临床效用受限，现有AI模型忽略表型相互作用且可解释性不足，需整合表型信息提升预后预测。
method: 提出PhenoMap从基因组变异推断表型特征，并构建PhenoSurv深度生存模型，联合表型重建、KL散度和生存损失进行训练。
result: 在乳腺癌、肺癌、脑癌中准确捕获分子亚型和耐药通路，预后性能超越现有模型，并识别NOTCH1、SMARCA4等预后因子。
conclusion: PhenoMap与PhenoSurv提供准确、可解释的预后模型，为精准肿瘤学提供临床可行的生物学见解。
---

## 摘要
体细胞基因组改变在癌症中被广泛检测，并且仍然是个性化治疗的主要依据，但其临床实用性仅限于少数可靶向位点。AI/ML模型为捕获全基因组复杂性提供了机会，但临床转化受到可解释性差的阻碍，通常仅限于单基因效应，忽略了更高阶的表型相互作用。为了解决这个问题，我们开发了PhenoMap，这是一个从体细胞变异推断肿瘤表型状态的机器学习框架。在9000个泛癌基因组和转录组上训练后，PhenoMap能够准确重建基于表达的通路富集分数和整合的标志性癌症表型，从而在表型、通路和基因尺度上实现多层次解释。PhenoMap捕获了乳腺癌、肺癌和脑癌的分子亚型和关键耐药通路。我们在PhenoSurv中利用这些特征，这是一个深度生存模型，整合了表型重建损失、Kullback-Leibler散度和生存损失，以学习具有生物学基础的预测因子。PhenoSurv在性能上优于最先进的生存模型，同时提供了稳健的机制解释。NOTCH1信号和SMARCA4突变成为激素受体阳性乳腺癌的主要预后因素。TGF-β信号和炎症小体（可能由FAT1调节）预测了肺腺癌的结局，而肌醇代谢和PI3K信号是脑癌的关键驱动因素。总之，PhenoMap和PhenoSurv为精准肿瘤学提供了准确、可解释且临床可用的模型。

## Abstract
Somatic genomic alterations are widely profiled in cancer and remain the primary source for personalized therapy, yet their clinical utility is limited to few actionable targets. AI/ML models offer opportunities to capture genome-wide complexities, but clinical translation is hindered by poor interpretability, often limited to single-gene effects, and overlooks higher-order phenotypic interactions. To address this, we developed PhenoMap, a machine-learning framework that infers tumor phenotypic states from somatic variants. Trained on 9,000 pan-cancer genomes and transcriptomes, PhenoMap accurately reconstructs expression-based pathway enrichment scores and consolidated hallmark cancer phenotypes, enabling multilevel interpretation at phenotype, pathway, and gene scales. PhenoMap captured molecular subtypes and key resistance pathways across breast, lung, and brain cancers. We leveraged these features in PhenoSurv, a deep survival model integrating phenotypic reconstruction loss, Kullback-Leibler divergence, and survival loss to learn biologically-grounded predictors. PhenoSurv outperformed state-of-the-art survival models while providing robust mechanistic explanations. NOTCH1 signaling and SMARCA4 mutations emerged as a major prognostic factor in hormone receptor-positive breast cancer. TGF-{beta} signaling and inflammasomes, potentially modulated by FAT1, predicted lung adenocarcinoma outcomes, while inositol metabolism and PI3K signaling were key drivers in brain cancer. Together, PhenoMap and PhenoSurv provide accurate, interpretable, and clinically actionable models for precision oncology.

Graphical Abstract

O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=191 SRC="FIGDIR/small/734894v1_ufig1.gif" ALT="Figure 1">
View larger version (37K):
org.highwire.dtl.DTLVardef@10101f1org.highwire.dtl.DTLVardef@1269ec3org.highwire.dtl.DTLVardef@81211borg.highwire.dtl.DTLVardef@1a48f91_HPS_FORMAT_FIGEXP  M_FIG C_FIG PhenoMap framework leverages genomic data and explainable deep learning to identify phenotype, pathway, and gene-level prognostic markers for precision oncology.