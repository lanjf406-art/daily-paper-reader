---
title: "ATLAS: a scverse-compatible package for multi-omic single-cell trajectory inference integration"
title_zh: ATLAS：一个兼容scverse的多组学单细胞轨迹推断整合包
authors: "Leclercq, A., Martini, L., Bardini, R., Savino, A., Di Carlo, S."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.23.727175v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 多组学单细胞轨迹推断方法，可用于耐药机制研究
tldr: 单细胞轨迹推断多依赖转录组数据，忽略染色质可及性信息。ATLAS通过加权最近邻图整合scRNA-seq和scATAC-seq，构建统一多组学表示以联合推断伪时间和命运概率。在合成和真实数据中重建连贯发育轨迹，揭示跨组学调控程序。该框架兼容scverse，为多组学细胞分化研究提供新工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有轨迹推断方法仅利用转录组数据，无法全面捕获细胞状态转变中的染色质调控过程。
method: 通过加权最近邻图整合scRNA-seq和scATAC-seq，在多组学表示中联合估计伪时间、终点状态和命运概率。
result: 在合成和真实数据上重建发育轨迹，解析谱系结构，并揭示跨组学调控程序（如Lef1在毛囊分化中的作用）。
conclusion: ATLAS提供了一个兼容scverse的多组学轨迹推断框架，能够捕获单模态数据无法发现的跨层调控动态。
---

## 摘要
单细胞轨迹推断广泛用于研究细胞分化和命运决定，但大多数方法仅依赖转录组数据，因此只捕捉了细胞状态转变背后的部分调控过程。这里我们介绍ATLAS（高级多组学单细胞分辨率轨迹学习），一个兼容scverse的Python包，用于从配对的单细胞RNA-seq和ATAC-seq数据中推断轨迹。ATLAS通过加权最近邻图整合转录组和染色质可及性信息，使得两种模态能够在统一的多组学表示中共同指导伪时间估计、终端状态识别和命运概率推断。在合成和真实数据集上，ATLAS重建了连贯的发育轨迹，捕捉了渐进的命运决定，并解析了有生物学意义的谱系结构，突显了多组学整合对于表征细胞发育动态的价值。此外，ATLAS能够沿伪时间联合分析转录因子表达和可及性衍生的靶基因活性，为跨越转录组和表观基因组层的调控程序提供见解，而这些从单模态数据中不易检测。作为概念验证，ATLAS重现了已知的毛囊调控程序，并揭示了连贯的多组学轨迹，其中Lef1相关的调控模式与毛干分化相关联。总之，ATLAS为在单细胞多组学实验中研究细胞分化和调控动态提供了一个可互操作且具有生物学信息的框架。

## Abstract
Single-cell trajectory inference is widely used to study cellular differentiation and fate decisions, yet most methods rely solely on transcriptomic data and therefore capture only part of the regulatory processes underlying cell-state transitions. Here we present ATLAS (Advanced Trajectory Learning from multi-omics At Single-cell resolution), a scverse-compatible Python package for trajectory inference from paired single-cell RNA-seq and ATAC-seq data. ATLAS integrates transcriptomic and chromatin accessibility information through Weighted Nearest Neighbor graphs, enabling both modalities to jointly inform pseudotime estimation, terminal-state identification, and fate probability inference within a unified multi-omic representation. Across synthetic and real datasets, ATLAS reconstructs coherent developmental trajectories, captures progressive fate commitment, and resolves biologically meaningful lineage structures, highlighting the value of multi-omic integration for characterizing cellular developmental dynamics. In addition, ATLAS enables joint analysis of transcription factor expression and accessibility-derived target-gene activity along pseudotime, providing insights into regulatory programs spanning transcriptomic and epigenomic layers that are not readily detectable from unimodal data. As a proof of concept, ATLAS recapitulates known hair follicle regulatory programs and reveals coherent multi-omic trajectories in which Lef1-associated regulatory patterns are linked to hair shaft differentiation. Overall, ATLAS provides an interoperable and biologically informative framework for studying cellular differentiation and regulatory dynamics in single-cell multi-omics experiments.