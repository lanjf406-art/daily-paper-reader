---
title: "MSstatsBioNet: Integrating Statistical Analyses with Prior Knowledge Biomolecular Networks for Quantitative Proteomics and Phosphoproteomics"
title_zh: MSstatsBioNet：整合统计分析与先验知识生物分子网络用于定量蛋白质组学和磷酸化蛋白质组学
authors: "Wu, A., Kohler, D., Navada, P. P., Robbins, J. E., Boyle, G. E., Boshart, A., Karis, K., Neefjes, J., Konvalinka, A., Sarthy, J., Pino, L., Gyori, B. M., Vitek, O."
date: 2026-07-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.09.737605v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 整合网络的蛋白质组学生物信息学工具，可应用于耐药研究
tldr: 蛋白质组学实验常产生差异蛋白列表，但缺乏机制背景。MSstatsBioNet整合统计分析与先验知识网络，自动从INDRA数据库检索子网络并叠加定量变化。通过三个案例验证，结合文本挖掘证据辅助构建机制假说，为蛋白质组和磷酸化蛋白质组数据提供可解释的生物网络分析。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737605-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1725, \"height\": 1086, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737605-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1705, \"height\": 879, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737605-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1361, \"height\": 790, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737605-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1698, \"height\": 1310, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737605-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1668, \"height\": 1331, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-09-737605-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1722, \"height\": 247, \"label\": \"Table\"}]"
motivation: 解决差异蛋白列表缺乏生物学机制解释的问题，自动化整合先验网络以提升可解释性。
method: 集成MSstats统计分析和INDRA文本挖掘网络，输入差异蛋白列表后检索子网络并映射折叠变化。
result: 三个案例成功展示网络交互与证据链接，辅助构建迭代假设。
conclusion: MSstatsBioNet作为Bioconductor包，为定量蛋白质组和磷酸化蛋白质组提供网络整合与可视化工具。
---

## 摘要
基于定量质谱的蛋白质组学和磷酸化蛋白质组学实验的一个常见结果是获得在不同条件下差异丰度的蛋白质列表。然而，生物学解释需要在生物机制和蛋白质功能的先验知识背景下进行评估。促进机制性生物学解释的一种方法是将这些列表与从手动策划资源和文本挖掘系统构建的生物网络数据库整合。本文通过MSstatsBioNet自动化了这一过程，这是一个Bioconductor包，整合了MSstats（一个用于检测差异丰度蛋白质的开源包家族）和INDRA（一个通过文本挖掘从生物医学文献中提取生物分子网络并将这些网络与策划知识库内容合并的系统）。以来自MSstats的差异丰度蛋白质列表作为输入，MSstatsBioNet从INDRA检索蛋白质子网络，并将实验倍数变化叠加到底层子网络上。然后用户可以交互式地处理网络和叠加的数据，查询原始文献证据以构建用于迭代假设生成的粒度机制叙事。我们通过三个案例研究展示了该方法的实用性，其中两个测量蛋白质丰度的变化，一个测量磷酸化水平的变化。

## Abstract
A common outcome of quantitative mass spectrometry-based proteomic and phosphoproteomic experiments is a list of proteins that are differentially abundant between conditions. However, biological interpretation requires evaluation in the context of prior knowledge of biological mechanisms and protein function. One approach to facilitate mechanistic biological interpretation is to integrate such lists with biological network databases, built from manually curated resources and text mining systems. This manuscript automates this process with MSstatsBioNet, a Bioconductor package that integrates MSstats, a family of open-source packages for detecting differentially abundant proteins, and INDRA, a system that extracts biomolecular networks from biomedical literature using text mining and merges those networks with the content of curated knowledge bases. Taking as input a list of differentially abundant proteins from MSstats, MSstatsBioNet retrieves a protein subnetwork from INDRA and overlays experimental fold changes onto the underlying subnetwork. Users can then interact with the network and overlaid data, interrogating primary literature evidence to construct granular mechanistic narratives for iterative hypothesis generation. We demonstrate the utility of this approach with three case studies, two measuring changes in protein abundance and one measuring changes in phosphorylation.