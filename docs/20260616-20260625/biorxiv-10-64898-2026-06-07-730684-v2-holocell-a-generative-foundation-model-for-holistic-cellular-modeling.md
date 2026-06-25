---
title: "HoloCell: A Generative Foundation Model for Holistic Cellular Modeling"
title_zh: HoloCell：面向整体细胞建模的生成式基础模型
authors: "Jiang, Q., Li, Z., Hu, B., Bie, Y., Li, K., Li, Q., Jin, P., He, Y., Deng, P., Wang, Z., Chen, X., Qin, T., Liu, H., Jiang, R., Yin, Q."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.07.730684v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞多组学生成基础模型，可用于肿瘤耐药的多组学表征
tldr: 单细胞多组学技术可同时测量表观基因组、转录组和蛋白质组，但现有方法难以统一整合并处理模态缺失。HoloCell是首个覆盖三大组学的生成式基础模型，含8.6亿参数，在4.68亿细胞预训练数据上学习。该模型在表示学习、多组学整合和跨模态生成任务中均优于现有方法，并支持灵活的非自回归生成顺序。HoloCell为构建虚拟细胞提供了统一框架，实现了细胞状态的系统表征和生成模拟。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有单细胞多组学方法通常针对特定模态设计，难以灵活整合多种组学并处理模态缺失问题。
method: 提出HoloCell，采用层次化标记化策略编码顺式调控元件、基因和蛋白质，基于扩散与重掩码的迭代生成框架。
result: 在单组学表示、配/非配对多组学整合及跨模态生成任务中性能领先，支持灵活生成顺序。
conclusion: HoloCell作为统一基础模型，实现了多组学细胞状态的联合表征与生成模拟，推进虚拟细胞概念。
---

## 摘要
单细胞多组学技术近年来取得了进展，使得能够在单个细胞内分析表观基因组、转录组和蛋白质组层面，为将细胞状态表征为整合的生物系统提供了新机遇。然而，开发一个能够无缝整合不同组学模态且对异构模态缺失保持鲁棒性的统一框架仍然具有挑战性。现有方法通常针对特定模态或模态对设计，依赖于数据集特定的训练或配对测量。在这里，我们提出了HoloCell，据我们所知，这是首个用于跨三个主要单细胞组学模态（即表观基因组学、转录组学和蛋白质组学）的联合表征学习和生成建模的生成式基础模型。HoloCell包含超过8.6亿个参数，并在人类多组学语料库（Human-Multi-Omics-Corpus）上进行了预训练，该语料库包含约4.68亿个跨这三个组学层面的单细胞谱，对应超过4250亿个token。HoloCell引入了一种简单但具有生物学动机的分层token化策略，将顺式调控元件、基因和蛋白质编码为共享建模框架内的结构化token。我们通过单组学表征学习、配对多组学整合、未配对多组学对齐以及通过迭代扩散和重新掩码的跨模态生成来评估HoloCell，展示了其在不同组学任务中的卓越性能和灵活性。从表征角度来看，HoloCell提供了跨多个组学层面的细胞状态统一数字映射，将细胞异质性作为一个整合系统来捕捉。从生成角度来看，其迭代扩散和重新掩码框架允许超越固定从左到右因果性的灵活生成顺序，实现了多组学信息流的计算机模拟。总之，这些能力使HoloCell成为迈向虚拟细胞这一新兴概念的通用基础模型，在统一框架内提供细胞系统的系统表征和生成模拟。

## Abstract
Single-cell multi-omics technologies have recently advanced to enable the profiling of epigenomic, transcriptomic, and proteomic layers within individual cells, offering new opportunities to characterize cellular states as integrated biological systems. However, developing a unified framework that can seamlessly integrate diverse omics modalities and remain robust to heterogeneous modality missingness remains challenging. Existing methods are often designed for specific modalities or modality pairs, relying on dataset-specific training or paired measurements. Here we present HoloCell, to our knowledge the first generative foundation model for joint representation learning and generative modeling across all three major single-cell omics modalities, i.e., epigenomics, transcriptomics, and proteomics. HoloCell contains over 860 million parameters and is pretrained on the Human-Multi-Omics-Corpus, which comprises approximately 468 million single-cell profiles across these three omics layers, corresponding to over 425 billion tokens. HoloCell introduces a simple yet biologically motivated hierarchical tokenization strategy that encodes cis-regulatory elements, genes, and proteins as structured tokens within a shared modeling framework. We evaluated HoloCell across single-omics representation learning, paired multi-omics integration, unpaired multi-omics alignment, and cross-modal generation via iterative diffusion and remasking, demonstrating its superior performance and flexibility across diverse omics tasks. From a representation perspective, HoloCell provides a unified digital mapping of cellular states across multiple omics layers, capturing cell heterogeneity as an integrated system. From a generation perspective, its iterative diffusion and remasking framework permits flexible generation orders beyond fixed left-to-right causality, enabling in silico simulation of multi-omics information flow. Together, these capabilities position HoloCell as a versatile foundation model toward the emerging concept of a virtual cell, offering both systematic characterization and generative simulation of cellular systems within a unified framework.