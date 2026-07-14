---
title: A Bayesian Network-Based Framework for Causal Cancer Drug Target Discovery Integrating Patient and Cell Line Data
title_zh: 基于贝叶斯网络的因果癌症药物靶点发现框架，整合患者与细胞系数据
authors: "Yoon, S. H., Park, Y. R., Kim, H. U."
date: 2026-07-13
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.13.736676v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 整合患者数据的贝叶斯网络因果药物靶点发现
tldr: 现有癌症药物靶点发现方法存在细胞系数据难以转化到患者肿瘤、缺乏因果解释的局限。本文提出BayesTx框架，整合患者和细胞系转录组数据，投影至通路与转录因子活性空间，学习域特异因果图并加权合并，通过do-simulation量化转录因子对细胞活力的因果效应。在乳腺癌中排名47个转录因子，经生存分析和药物反应验证。该工作展示了跨域贝叶斯网络建模可桥接细胞系与患者数据，系统发现因果治疗靶点。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-736676-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1579, \"height\": 914, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-736676-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1559, \"height\": 1377, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-736676-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 753, \"height\": 539, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-736676-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1571, \"height\": 995, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-736676-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1632, \"height\": 864, \"label\": \"Figure\"}]"
motivation: 克服细胞系靶点转化差和缺乏因果解释，桥接患者与细胞系数据。
method: 将患者和细胞系数据映射到共享通路/转录因子活性空间，学习因果图并加权合并，执行do-simulation量化因果效应。
result: 在乳腺癌中排名47个转录因子，通过regulon传播得到基因靶点，外部生存分析和药物响应验证支持。
conclusion: 跨域贝叶斯网络建模可系统识别癌症因果治疗靶点，提升临床相关性。
---

## 摘要
当前癌症药物靶点发现方法面临两个关键局限性：从细胞系衍生的靶点向患者肿瘤的转化效果不佳，以及缺乏对靶点优先排序背后调控机制的因果解释。本文提出了BayesTx（贝叶斯治疗靶点发现），一个贝叶斯网络框架，整合患者转录组学数据与细胞系数据，以识别癌症中的因果治疗靶点。BayesTx将两个数据域投影到共享的生物学空间（通路和转录因子活性），学习领域特定的因果图，并通过加权边聚合和自助法共识过滤将其合并。在共识网络上进行do模拟，量化每个转录因子对癌细胞活力的因果效应。使用TCGA-BRCA（癌症基因组图谱乳腺癌队列）和DepMap（癌症依赖性图谱）数据集应用于乳腺癌，该框架按预测的因果影响对47个转录因子进行排序，并通过基于调节子的传播进一步衍生出基因水平的靶点。排名靠前的转录因子（TF）靶点得到外部队列数据中的生存分析和药物基因组药物反应关联的独立支持。总体而言，BayesTx证明了跨领域贝叶斯网络建模可以桥接患者和细胞系数据，从而系统地识别癌症中的因果治疗靶点。

## Abstract
Current approaches to cancer drug target discovery face two key limitations: poor translation of cell line-derived targets to patient tumors, and the lack of causal explanation of the regulatory mechanisms underlying target prioritization. Here we present BayesTx (Bayesian Therapeutics target discovery), a Bayesian network framework that integrates patient transcriptomics data with cell line data to identify causal therapeutic targets in cancer. BayesTx projects both data domains into a shared biological space of pathway and transcription factor activities, learns domain-specific causal graphs, and merges them through weighted edge aggregation with bootstrap consensus filtering. Do-simulation on the consensus network quantifies the causal effect of each transcription factor on cancer cell viability. Applied to breast cancer using TCGA-BRCA (The Cancer Genome Atlas breast cancer cohort) and DepMap (Cancer Dependency Map) datasets, the framework ranked 47 transcription factors by predicted causal impact, with gene-level targets further derived through regulon-based propagation. Top-ranked transcription factor (TF) targets were independently supported by survival analysis in external cohort data and pharmacogenomic drug response associations. Overall, BayesTx demonstrates that cross-domain Bayesian network modeling can bridge patient and cell line data to systematically identify causal therapeutic targets in cancer.