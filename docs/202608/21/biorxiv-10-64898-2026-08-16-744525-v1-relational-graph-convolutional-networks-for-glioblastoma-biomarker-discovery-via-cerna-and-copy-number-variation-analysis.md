---
title: Relational Graph Convolutional Networks for Glioblastoma Biomarker Discovery via ceRNA and Copy Number Variation Analysis
title_zh: 基于ceRNA和拷贝数变异分析的关系图卷积网络用于胶质母细胞瘤生物标志物发现
authors: "Khandelwal, S., Jarvis, N., Zhan, J."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.16.744525v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 胶质母细胞瘤机器学习生物标志物发现，可迁移至耐药预测。
tldr: 胶质母细胞瘤预后极差且缺乏可靠生物标志物，现有方法未能整合多种调控机制。本文提出基于关系图卷积网络（RGCN）的晚期融合集成架构，联合ceRNA与拷贝数变异知识图谱进行生物标志物发现。该方法识别出5个新型生物标志物，包括hsa-miR-196a和hsa-miR-224，并通过生存分析验证其预后价值。该框架为GBM生物标志物发现提供了新思路。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有ceRNA和CNV分析未整合多种调控机制，限制了生物标志物发现的准确性。
method: 使用RGCN分别建模ceRNA和CNV知识图谱，通过晚期融合集成架构进行生物标志物预测。
result: 模型优于基线，识别出5个新生物标志物，生存分析显示其具有显著预后能力。
conclusion: 晚期融合RGCN集成能有效捕获复杂基因互作，为GBM生物标志物发现提供新框架和潜在治疗靶点。
---

## 摘要
胶质母细胞瘤（GBM）是一种高度侵袭性的脑肿瘤，其5年生存率极低，仅为6.9%，这主要归因于缺乏可靠的生物标志物。虽然竞争性内源RNA（ceRNA）和拷贝数变异（CNV）分析提供了独特的生物标志物识别潜力，但当前的方法忽视了整合多种调控机制进行生物标志物检测。为解决这一局限性，我们通过一种新颖的后期融合集成架构，将关系图卷积网络（RGCN）应用于ceRNA和CNV知识图谱。所提出的架构优于基线模型，并鉴定出五个新型生物标志物，包括hsa-miR-196a和hsa-miR-224。Kaplan-Meier生存分析和Cox回归表明，所鉴定的基因具有显著的预后和诊断价值。Kaplan-Meier曲线的早期分层表明这些基因在患者生存预测方面具有潜力。结果表明，后期融合RGCN集成能够有效捕获复杂的基因相互作用，克服现有模型的局限性，并为生物标志物发现提供了一个框架。这些新型生物标志物可作为未来GBM治疗开发的潜在靶点以及非侵入性诊断检测的候选对象。

## Abstract
Glioblastoma (GBM) is a highly aggressive brain tumor with an extremely poor 5-year survival rate of 6.9%, largely attributable to the lack of reliable biomarkers. While competing endogenous RNA (ceRNA) and copy number variation (CNV) analyses offer unique biomarker identification potential, current approaches neglect the integration of multiple regulatory mechanisms for biomarker detection. To address this limitation, we applied relational graph convolutional networks (RGCNs) to ceRNA and CNV knowledge graphs through a novel late fusion ensemble architecture. The proposed architecture outperformed baseline models and identified five novel biomarkers, including hsa-miR-196a and hsa-miR-224. Kaplan-Meier survival analysis and Cox regression indicated that the identified genes hold significant prognostic and diagnostic power. The early stratification of the Kaplan-Meier curves indicates the potential these genes hold for patient survival prediction. The results illustrate that a late fusion RGCN ensemble effectively captures complex gene interactions, overcoming limitations of existing models and providing a framework for biomarker discovery. The novel biomarkers serve as prospective targets for future GBM therapeutic development and candidates for non-invasive diagnostic assays.