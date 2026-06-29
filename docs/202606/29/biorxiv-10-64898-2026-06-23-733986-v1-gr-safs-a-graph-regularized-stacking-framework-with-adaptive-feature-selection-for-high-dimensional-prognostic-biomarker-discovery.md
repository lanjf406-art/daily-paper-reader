---
title: "GR-SAFS: A Graph-Regularized Stacking Framework with Adaptive Feature Selection for High-Dimensional Prognostic Biomarker Discovery"
title_zh: GR-SAFS：一种用于高维预后生物标志物发现的图正则化堆叠框架与自适应特征选择
authors: "He, J., Guan, J."
date: 2026-06-28
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.23.733986v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 转录组生物标志物发现，可应用于耐药机制
tldr: 高维转录组数据中识别预后生物标志物面临稀疏性、网络拓扑保持和非线性信号整合的三重挑战。提出GR-SAFS框架，包含图Lasso与随机森林并行引擎、ecdf对齐层和多样性惩罚二次规划路由，实现自适应特征选择。在TCGA-LUAD上得到20基因签名，训练C-index 0.700，在独立外部队列中唯一保持显著风险分层。功能富集锚定Wnt/β-catenin轴，开源实现确保可重复。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法忽略基因网络结构、无法捕获非线性交互或缺乏融合异质模型输出的机制，需新框架同时解决稀疏性、网络拓扑和信号整合。
method: GR-SAFS并行运行图Lasso（嵌入基因共表达网络拉普拉斯先验）和随机森林，通过ecdf对齐层统一重要性度量，再用严格凸二次规划路由加权融合。
result: 在TCGA-LUAD中选出20基因签名，训练C-index 0.700；在两组独立微阵列队列中唯一保持显著风险分层，强基线方法在外部队列中失效。
conclusion: GR-SAFS有效整合稀疏与非线性信号，生成跨平台稳定的预后签名，其功能富集与Wnt/β-catenin轴一致，开源实现促进可复现研究。
---

## 摘要
从高维转录组数据中识别预后生物标志物面临三重挑战：实现稀疏性、保留生物网络拓扑以及整合互补的非线性信号。现有方法通常忽略网络结构，错过非线性相互作用，或缺乏融合异构模型输出的原则性机制。我们提出GR-SAFS（图正则化堆叠与自适应特征选择），一个包含三个模块的框架：一个嵌入基因共表达网络拉普拉斯先验的图套索引擎，与随机森林引擎并行运行；一个经验累积分布函数（eCDF）对齐层，将稀疏和密集重要性置于共同百分位尺度上；以及一个多样性惩罚二次规划路由器，其严格凸性产生唯一的全局最优解。在TCGA-LUAD队列上，GR-SAFS识别出一个20基因特征，训练一致性指数为0.700。在两个独立的跨平台微阵列队列中，GR-SAFS是唯一其冻结特征在每一个队列中都保持显著风险分层的方法，而更强C指数基线方法至少在一个外部队列中失去显著性。功能富集将特征锚定到连贯的Wnt/β-连环蛋白轴上。已发布开源实现以确保完全可重复性。

## Abstract
Identifying prognostic biomarkers from high-dimensional transcriptomic data poses a triple challenge: achieving sparsity, preserving biological network topology, and integrating complementary nonlinear signals. Existing methods typically ignore network structure, miss nonlinear interactions, or lack a principled mechanism to fuse heterogeneous model outputs. We introduce GR-SAFS (Graph-Regularized Stacking with Adaptive Feature Selection), a framework with three modules: a Graph-Lasso engine embedding gene co-expression network Laplacian priors, run in parallel with a Random Forest engine; an empirical cumulative distribution function (eCDF) alignment layer that places sparse and dense importances on a common percentile scale; and a diversity-penalized quadratic programming router whose strict convexity yields a unique global optimum. On the TCGA-LUAD cohort, GR-SAFS identifies a 20-gene signature with a training concordance index of 0.700. Across two independent crossplatform microarray cohorts, GR-SAFS is the only method whose frozen signature retains statistically significant risk stratification in every cohort, where stronger-C-index baselines lose significance on at least one external cohort. Functional enrichment anchors the signature to a coherent Wnt/{beta};-catenin axis. An open-source implementation is released for full reproducibility.