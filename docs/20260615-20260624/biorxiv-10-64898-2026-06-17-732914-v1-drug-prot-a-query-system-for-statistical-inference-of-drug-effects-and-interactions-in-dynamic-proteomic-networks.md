---
title: "Drug-Prot: A query system for statistical inference of drug effects and interactions in dynamic proteomic networks"
title_zh: Drug-Prot：动态蛋白质组网络中药物效应与相互作用的统计推断查询系统
authors: "Ulmer, M., Sun, R., Qian, L., Aebersold, R., Guo, T., Buehlmann, P."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.17.732914v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 药物效应与相互作用的蛋白质组网络
tldr: 药物效应和药物相互作用对于联合治疗至关重要。Drug-Prot框架利用63种单药和59种组合处理18种乳腺癌细胞系的大规模蛋白质组数据，通过统计推断量化因果药物效应和相互作用，并重建有向时间依赖蛋白质网络。通过交互式Web应用，用户可查询特定蛋白质集，获得校正p值和网络图。该框架将候选蛋白特征与可操作药物组合联系起来，助力联合疗法开发。
source: biorxiv
selection_source: fresh_fetch
motivation: 为理解药物效应和药物-药物相互作用，支持联合治疗方案的开发，该工作提出了Drug-Prot框架。
method: 利用63种单药和59种组合在18种乳腺癌细胞系中的大规模蛋白质组数据，通过统计推断量化效应并构建动态网络。
result: 开发了交互式Web应用，用户可自定义蛋白质集，获得校正p值和有向时间依赖蛋白质网络。
conclusion: 该框架将候选因果蛋白特征与可操作的药物组合联系起来，促进联合疗法的发现。
---

## 摘要
理解药物效应和药物-药物相互作用对于开发联合疗法至关重要。我们提出Drug-Prot，一个利用大规模扰动蛋白质组学来量化因果药物效应、药物-药物相互作用以及动态蛋白质关系的计算框架。使用来自18种乳腺癌细胞系在6、24和48小时时间点施加的63种单药和59种药物组合的数据，Drug-Prot估计药物对蛋白质表达的影响，并重建有向的时间蛋白质依赖网络。该公开可用的软件支持对用户定义的蛋白质集进行靶向分析，显著减轻多重检验负担。通过交互式网络应用程序，用户可获得单药和组合效应的校正p值、有向时间依赖网络以及可下载的结果，无需访问底层蛋白质组数据集。作为用例，我们将不变性正则化随机森林应用于三阴性乳腺癌细胞系，以识别与药物反应相关的蛋白质。在Drug-Prot中查询这些蛋白质揭示了蛋白质网络层面的药物特异性和相互作用效应，展示了该框架如何将候选因果蛋白质特征与可行的药物组合联系起来。

## Abstract
Understanding drug effects and drug-drug interactions is essential for developing combination therapies. We present Drug-Prot, a computational framework that leverages large-scale perturbation proteomics to quantify causal drug effects, drug-drug interactions, and dynamic protein relationships. Using data from 63 single drugs and 59 drug combinations applied to 18 breast cancer cell lines at 6, 24, and 48 hours, Drug-Prot estimates drug effects on protein expression and reconstructs directed temporal protein dependency networks. The publicly available software enables targeted analyses of user-defined protein sets, substantially reducing the multiple-testing burden. Through an interactive web application, users obtain corrected p-values for single-drug and combination effects, directed temporal dependency networks, and downloadable results without requiring access to the underlying proteomic dataset. As a use case, we apply invariance-regularized Random Forests to triple-negative breast cancer cell lines to identify proteins associated with drug response. Querying these proteins in Drug-Prot reveals drug-specific and interaction effects at the protein-network level, illustrating how the framework links candidate causal protein features to actionable drug combinations.