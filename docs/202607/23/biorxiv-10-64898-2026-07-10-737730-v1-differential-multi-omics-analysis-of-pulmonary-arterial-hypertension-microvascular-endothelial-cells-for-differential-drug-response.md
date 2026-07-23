---
title: Differential multi-omics analysis of pulmonary arterial hypertension microvascular endothelial cells for differential drug response
title_zh: 肺动脉高压微血管内皮细胞的差异多组学分析用于差异药物反应
authors: "Hiort, P., Weiss, A., Krentz, J., Schermuly, R. T., Bogaard, H.-J., Conrad, T., Szulcek, R., Baum, K."
date: 2026-07-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.10.737730v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 多组学网络框架可迁移至肿瘤耐药研究
tldr: 肺动脉高压（PAH）是一种异质性疾病，单组学分析难以捕捉其复杂分子失调。本研究应用DrDimont多组学网络分析框架，整合转录组、蛋白质组、磷酸化组和激酶筛选数据，构建条件特异性网络并引入激酶-激酶相互作用。结果发现以MAPK信号通路激酶（如MAPK13、MAP2K、IRAK1）为中心的差异，以及ACADSB、GPX7等高差异节点。药物优先化揭示他克莫司和MAPK抑制剂（如司美替尼、曲美替尼）等候选药物。该工作整合激酶活性筛选，揭示了激酶中心改变并提出了PAH的治疗假设。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1327, \"height\": 818, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1326, \"height\": 762, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1319, \"height\": 973, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1665, \"height\": 1416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1673, \"height\": 1226, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1341, \"height\": 431, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1334, \"height\": 666, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1155, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1159, \"height\": 585, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1563, \"height\": 353, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1507, \"height\": 349, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-10-737730-v1/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1625, \"height\": 2067, \"label\": \"Table\"}]"
motivation: PAH涉及多层面分子失调，单组学分析不全面，需多组学整合以揭示关键机制。
method: 应用DrDimont框架，整合多组学数据并引入激酶-激酶相互作用，构建条件特异性差异网络。
result: 识别以MAPK激酶为中心的差异网络，优先化他克莫司和MAPK抑制剂等药物。
conclusion: 多组学网络分析揭示激酶中心改变，为PAH提供可解释的治疗假设。
---

## 摘要
肺动脉高压（PAH）是一组异质性疾病，涉及复杂的分子失调，单组学分析无法完全捕捉这些失调。我们将基于网络的多组学分析框架DrDimont应用于来自PAH患者和对照组的肺微血管内皮细胞的转录组、蛋白质组、磷酸化蛋白质组和激酶筛选数据。因此，我们在构建条件特异性多组学网络时扩展了DrDimont的功能，加入了激酶-激酶相互作用。激酶相互作用是从筛选底物的磷酸化中推断出来的，这些磷酸化通过激酶-底物预测进行加权。基于网络的PAH与对照之间的差异相互作用分数揭示了以激酶为中心的改变，特别是与MAPK信号传导相关的顶级命中，例如MAPK13、MAP2K或上游IRAK1以及其他MAPK/MAP2K家族成员。进一步高度差异的节点是ACADSB、GPX7、DSE（对于蛋白质）和AIM1、LY96、CHSY3（对于mRNA）。在通过将药物靶点映射到差异网络上来对候选药物进行优先级排序时，我们发现药物他克莫司（FK506）和几种抗肿瘤MAPK抑制剂（例如，司美替尼、曲美替尼）以及通过（线粒体）DNA转录作用于一般增殖的药物（例如，表柔比星、拓扑替康）得分很高。将激酶活性筛选整合到我们可解释的基于多组学网络的分析中，揭示了PAH中激酶中心的改变和治疗假说，补充了单层经典差异表达分析。

## Abstract
Pulmonary arterial hypertension (PAH) represents a heterogeneous group of disorders that involves complex molecular dysregulations, which are not fully captured by single-omics analyses. We apply our network-based multi-omics analysis framework, DrDimont, to transcriptomic, proteomic, phosphoproteomic, and kinase screening data from lung microvascular endothelial cells of PAH patients and controls.

Thereby, we extend the functionality of DrDimont to incorporate kinase-kinase interactions during the construction of condition-specific multi-omics networks. Kinase interactions are inferred from phosphorylations of screened substrates that are weighted by kinase-substrate predictions. Differential interaction scores from the network-based analysis between PAH and control uncover alterations centered on kinases, in particular top hits relating to MAPK signaling, such as MAPK13, MAP2K, or upstream IRAK1, and other MAPK/MAP2K family members. Further highly differential nodes were ACADSB, GPX7, DSE (for proteins), and AIM1, LY96, CHSY3 (for mRNAs). When prioritizing drug candidates by mapping drug targets onto the differential network, we find high scores for the drug tacrolimus (FK506) and several anti-neoplastic MAPK inhibitors (e.g., selumetinib, trametinib), as well as agents acting on general proliferation via (mitochondrial) DNA transcription (e.g., epirubicin, topotecan).

Integrating kinase activity screens into our explainable multi-omics network-based analyses reveals kinase-centered alterations and therapeutic hypotheses in PAH that complement single-layer classical differential expression analyses.