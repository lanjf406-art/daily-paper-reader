---
title: "Reproducible-by-design: Romics Processor, a FAIR ecosystem for multi-omics and spatial-omics analysis"
title_zh: 可重复性设计：Romics Processor，一个用于多组学和空间组学分析的FAIR生态系统
authors: "Gorman, B. L., Bhotika, H., Jehrio, M., Purkerson, J. M., Carlin, F., Nakayasu, E. S., Misra, R. S., Adkins, J. N., Anderton, C. R., Pryhuber, G., Clair, G. C."
date: 2026-07-15
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.09.737600v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 生信多组学FAIR工具
tldr: 多组学与空间组学数据日益复杂，现有工具未能完全遵循FAIR原则，导致计算可重复性问题。RomicsProcessor采用可重复性设计范式，其核心Romics_object自包含数据制品，封装完整处理历史与依赖，确保工作流可移植可重复。在蛋白质组学、多重免疫荧光和质谱成像等数据集上验证了其计算能力与可扩展性。该框架为基于FAIR原则的下一代可重复生物信息学工具提供了蓝图，可加速AI时代的多组学发现。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737600-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1703, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737600-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1356, \"height\": 1717, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737600-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1504, \"height\": 1535, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737600-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1682, \"height\": 1159, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737600-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1051, \"height\": 2358, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737600-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1310, \"height\": 1852, \"label\": \"Figure\"}]"
motivation: 现有组学分析工具对FAIR原则支持不足，计算可重复性问题严峻，亟需可重复性设计范式。
method: 构建以Romics_object为核心的RomicsProcessor，通过自包含数字制品封装完整数据处理历史与依赖。
result: 在批量蛋白质组学、多重免疫荧光和多批次质谱成像数据集上验证了工作流的可移植性与可重复性。
conclusion: RomicsProcessor为遵循FAIR原则的可重复分析提供蓝图，可加速AI时代多组学发现。
---

## 摘要
多组学和空间组学技术的应用正在爆炸式增长，产生了日益复杂的数据集。现有的生物信息学工具发展迅速，但未能完全遵循FAIR原则，使得该领域容易受到计算可重复性问题升级的影响。在此，我们介绍一种可重复性设计范式，该范式体现于组学数据处理包RomicsProcessor中。其核心是“Romics_object”，这是一种自包含的数字制品，封装了从原始数据到完全处理状态的数据全历史，捕捉了转换步骤及所需依赖关系的详细信息。这种架构确保了计算工作流完全可移植和可重复。在本文中，我们展示了RomicsProcessor在多种数据集上的计算能力和可扩展性，包括批量蛋白质组学、大规模多重免疫荧光和多批次质谱成像。RomicsProcessor为真正基于FAIR数据原则的分析提供了一个稳健的框架，是下一代可重复生物信息学工具的蓝图，可以在人工智能时代极大地加速多组学生物学中的发现。

## Abstract
Multi-omics and spatial-omics technologies are exploding in use, producing increasingly complex datasets. Existing bioinformatics tools are developing rapidly but fail to fully enforce the FAIR principles, leaving the field vulnerable to escalating issues in computational reproducibility. Here, we introduce a reproducible-by-design paradigm represented in an omics data processing package, RomicsProcessor. At its core, the "Romics_object", which is a self-contained digital artifact that encapsulates the full history of the data from the original data to the fully processed state, capturing the details of the transformative steps and the required dependencies. This architecture ensures that computational workflows are fully portable and reproducible. In this manuscript, we demonstrate RomicProcessors computational capabilities and scalability on diverse datasets, including bulk proteomics, large-scale multiplexed immunofluorescence, and multi-batch mass spectrometry imaging. Providing a robust framework for truly FAIR Data Principles-based analysis, RomicsProcessor is a blueprint for the next generation of reproducible bioinformatics tools that can dramatically accelerate discovery in multi-omics biology in the era of artificial intelligence.