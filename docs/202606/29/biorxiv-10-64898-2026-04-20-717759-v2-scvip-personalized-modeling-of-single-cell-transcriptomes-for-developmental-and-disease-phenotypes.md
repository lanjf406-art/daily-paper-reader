---
title: "scVIP: personalized modeling of single-cell transcriptomes for developmental and disease phenotypes"
title_zh: "scVIP: 单细胞转录组的个性化建模用于发育和疾病表型"
authors: "Lai, H.-Y., Yoo, Y., Tjaernberg, A., Li, R., He, Z., Travaglini, K. J., Qiao, Q., Agrawal, A., Kana, O., van Velthoven, C., Carroll, J. B., Gillespie, M., Mukherjee, S., Fardo, D. W., Li, X.-j., Lein, E., Gabitto, M. I."
date: 2026-06-27
pdf: "https://www.biorxiv.org/content/10.64898/2026.04.20.717759v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 单细胞转录组生成模型用于表型预测，可应用于耐药机制研究
tldr: 单细胞转录组学虽能解析细胞内异质性，但难以将分子状态与个体表型直接关联。scVIP提出一种生成模型，通过细胞类型感知的多实例学习架构，将基因表达、细胞类型组成和表型测量统一在同一概率框架内。该方法在皮层发育年龄预测中达到Pearson r=0.95，亨廷顿病进展建模CCC=0.90，并成功整合阿尔茨海默病队列、区分类风湿关节炎早期个体。scVIP为从细胞状态到机体表型的跨尺度分析提供了原则性工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有单细胞分析方法无法明确连接细胞分子状态与个体水平表型，亟需桥接这一跨尺度鸿沟的建模框架。
method: scVIP采用细胞类型感知的多实例学习架构，构建联合建模基因表达、细胞组成和表型的概率生成模型，学习隐含的供体嵌入。
result: 准确预测皮层发育年龄（r=0.95）、亨廷顿病进展（CCC=0.90），整合阿尔茨海默病队列并识别疾病相关小胶质细胞程序，区分早期RA进展状态。
conclusion: scVIP实现了从单细胞状态到个体表型的合理解析，能够定位表型关联信号的特定细胞群，支持发育与疾病研究。
---

## 摘要
单细胞转录组学解析个体内的细胞异质性，但将分子状态与个体水平表型联系起来需要明确桥接这些尺度的框架。我们提出scVIP，一个生成模型，在单一概率模型中连接基因表达、细胞类型组成和表型测量，从而实现准确的表型预测和可解释的轨迹推断。一种细胞类型感知的多实例学习架构学习捕获进展的供体嵌入，同时将表型相关信号定位到特定细胞群体。在四个场景中应用，scVIP准确预测皮层发育年龄（Pearson r = 0.95），表征亨廷顿病进展（一致性相关系数 = 0.90），整合两个阿尔茨海默病队列，恢复疾病相关的小胶质细胞和星形胶质细胞程序，并区分健康人与ACPA阳性个体以及非进展者与早期RA个体，识别与疾病相关的炎症T细胞程序。scVIP实现了对细胞状态如何共同塑造发育和疾病中个体水平表型的原理性分析。

## Abstract
Single-cell transcriptomics resolves cellular heterogeneity within individuals, but connecting molecular states to individual-level phenotypes requires frameworks that explicitly bridge these scales. We present scVIP, a generative model that links gene expression, cell-type composition, and phenotypic measurements within a single probabilistic model, which enables accurate phenotype prediction and interpretable trajectory inference. A cell-type-aware multi-instance learning architecture learns donor embeddings that capture progression while localizing phenotype-associated signals to specific cell populations. Applied across four settings, scVIP accurately predicts cortical developmental age (Pearson r = 0.95), characterizes Huntington's disease progression (concordance correlation coefficient = 0.90), integrates two Alzheimer's disease cohorts recovering disease-relevant microglial and astrocytic programs, and distinguishes healthy from ACPA-positive individuals and non-progressors from early RA individuals, identifying inflammatory T cell programs associated with disease. scVIP enables principled analysis of how cellular states collectively shape organism-level phenotypes across development and disease.