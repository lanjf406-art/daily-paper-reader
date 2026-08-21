---
title: "Mantpy: a framework for extracellular matrix analysis in spatial proteomics"
title_zh: Mantpy：空间蛋白质组学中细胞外基质分析框架
authors: "Ghafoor, M., Parkinson, J. E., Pham, T., Georgaka, S., Hayley, M. J., Jokl, E., Hanley, K. P., Allen, J. E., Sutherland, T. E., Rattray, M."
date: 2026-08-19
pdf: "https://www.biorxiv.org/content/10.1101/2025.06.04.657781v4.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 用于肿瘤微环境细胞外基质分析的空间蛋白质组学框架
tldr: 空间蛋白质组学可同时原位检测细胞与细胞外基质(ECM)，但现有工具以细胞为中心，忽略ECM。为此提出Mantpy框架，将ECM及细胞-ECM界面构建为空间图，并与细胞图链接，实现联合分析，支持图统计、可解释图深度学习及可视化。在人类肠道、感染小鼠肝脏和小鼠肺数据上，分别恢复组织分层结构、解析疾病相关基质组成与组织、表征细胞-基质关联。Mantpy与scverse生态互操作，将空间分析单元从细胞扩展至周围基质。
source: biorxiv
selection_source: fresh_fetch
motivation: 空间蛋白质组学同时产生细胞与ECM数据，但现有分析工具以细胞为中心，忽视ECM的重要作用。
method: Mantpy从基质标记物构建ECM空间图，并与细胞图链接，形成联合图，支持图统计、可解释图学习与可视化。
result: Mantpy在人类肠道恢复分层结构，在小鼠肝脏解析疾病相关基质，在小鼠肺中表征细胞-基质关联。
conclusion: Mantpy建立细胞-ECM联合分析框架，扩展空间分析单元，并可与scverse生态互操作。
---

## 摘要
空间蛋白质组学技术现已能够原位同时分析细胞和细胞外基质（ECM）。然而，尽管ECM在健康和疾病中发挥着重要作用，现有分析工具仍以细胞为中心。在此，我们提出Mantpy，一个将ECM及其与细胞的界面表示为空间图的框架。Mantpy直接从基质标志物构建ECM图，并将其与细胞图链接以进行细胞-ECM联合分析，支持图统计、可解释图深度学习及可视化。从单一ECM标志物到多重ECM和细胞标志物组合，Mantpy能够恢复人肠道中的分层组织结构，解析感染小鼠肝脏中与疾病相关的基质组成和组织，并表征小鼠肺中的细胞-基质关联。Mantpy随附包含ECM的数据集发布，并与scverse生态系统互操作，将空间分析的单位从细胞扩展到其周围的基质。

## Abstract
Spatial proteomics technologies now profile cells and the extracellular matrix (ECM) together in situ. Yet analysis tools remain cell-centric, despite the ECM playing an essential role in health and disease. Here we present Mantpy, a framework that represents the ECM, and its interface with cells, as spatial graphs. Mantpy builds ECM graphs directly from matrix markers and links them with cell graphs for joint cell-ECM analysis, supporting graph statistics, explainable graph deep learning and visualisation. From a single ECM marker to multiplexed panels of ECM and cellular markers, Mantpy recovers layered tissue architecture in human intestine, resolves disease-associated matrix composition and organisation in infected mouse liver, and characterises cell-matrix associations in mouse lung. Released with ECM-inclusive datasets and interoperating with the scverse ecosystem, Mantpy extends the unit of spatial analysis beyond the cell, to the matrix that surrounds it.