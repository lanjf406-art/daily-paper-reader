---
title: "PhenoBIC: operator-free single-cell spatial phenotyping in multiplex imaging data using deep learning of cell staining patterns"
title_zh: PhenoBIC：利用细胞染色模式的深度学习实现多重成像数据中无操作员单细胞空间表型分析
authors: "Sankaranarayanan, A., Zhao, C., Hernandez, M. G., Clemens, E. A., Smythe, K. S., Kazerouni, A. S., Carr, L. L., Li, C. I., Partridge, S. C., Vinayak, S., Mittal, S."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.11.731702v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 深度学习用于单细胞空间表型分析，与肿瘤微环境研究相关
tldr: 多重成像分析中细胞表型分类通常需要人工干预，效率低且结果依赖操作者。本文提出PhenoBIC，一种预训练深度学习模型，可直接对细胞多重生物标志物染色模式进行图像分类。在多种组织、成像平台和标记物上，PhenoBIC的F1得分约0.88，优于手动门控和其他方法。模型和包含约140万手动标注细胞的数据集已开源，支持QuPath接口，实现无操作者依赖的细胞空间表型分析。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有多重成像细胞表型分析需要手动门控，耗时且结果不一致，限制高通量应用。
method: PhenoBIC使用预训练卷积神经网络，直接对细胞染色图像中的多重生物标志物信号进行端到端分类。
result: 在多种组织和成像平台上，PhenoBIC的F1得分约0.88，优于手动门控和传统机器学习方法。
conclusion: 开源模型和标注数据集使细胞表型分析无需人工干预，可推广至不同多重成像平台和组织类型。
---

## 摘要
多重成像是一种有价值的工具，可在单细胞水平上空间检查组织微环境，以揭示生物学和临床见解。然而，目前大多数多重图像分析工作流程需要手动干预进行细胞表型分析，这减缓了进展，需要人力投入，并产生依赖操作员的输出。在此，我们开发了PhenoBIC，这是一种预训练的深度学习模型，用于对细胞中多重生物标志物信号（细胞的生物标志物印记）进行图像分类，以对细胞表型进行分类。我们展示了PhenoBIC（F1分数约0.88）在细胞标志物表达分类方面优于手动门控（广泛使用）和其他基于机器学习的计算方法。我们在多个生物标志物、组织采样策略（全活检和组织微阵列）、多重面板、成像平台和组织类型上验证了这一点。我们发布了约140万个人工整理细胞表达真实标签的内部训练和验证数据集。我们还开源了PhenoBIC，并通过QuPath接口实现了其在社区范围内的部署。

## Abstract
Multiplex imaging is a valuable tool for spatially examining tissue microenvironments at the single-cell level to uncover biological and clinical insights. However, most multiplex image analysis workflows currently require manual intervention for cell phenotyping, which slows progress, demands human effort, and yields operator-dependent outputs. Here, we developed PhenoBIC, a pre-trained deep learning model for image classification of the multiplexed biomarker signals in a cell (Biomarker Imprint of a Cell) to classify cell phenotypes. We show that PhenoBIC (F1-score [~]0.88) outperforms manual gating (widely used) and other machine learning-based computational approaches for cell marker expression classification. We validated this across multiple biomarkers, tissue sampling strategies (whole biopsies and tissue microarrays), multiplex panels, imaging platforms, and tissue types. We have released our in-house training and validation datasets of [~]1.4 million manually curated cell expression ground truth labels. We have also open-sourced PhenoBIC and enabled its community-wide deployment via the QuPath interface.