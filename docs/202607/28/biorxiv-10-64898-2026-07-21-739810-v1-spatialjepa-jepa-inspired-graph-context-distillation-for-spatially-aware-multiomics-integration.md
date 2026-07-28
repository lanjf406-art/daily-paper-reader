---
title: "SpatialJEPA: JEPA-inspired graph-context distillation for spatially aware multiomics integration"
title_zh: SpatialJEPA：受JEPA启发的图上下文蒸馏实现空间感知的多组学整合
authors: "Mann-Krzisnik, D., Li, Y."
date: 2026-07-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.21.739810v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 提供一种可用于表征肿瘤耐药的多组学整合方法
tldr: 空间多组学数据整合面临多数RNA-ATAC数据缺乏空间坐标的难题。SpatialJEPA提出一种JEPA启发的教师-学生框架，通过遮蔽空间邻域图迫使学生学习无空间上下文下的表征匹配，从而将空间知识迁移至非空间数据。在鼠脑多组学中，该方法实现了跨模态对齐并恢复空间转录组和染色质程序。其贡献在于首次将教师-学生蒸馏用于空间上下文迁移，拓展了非空间数据的空间分析能力。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-21-739810-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1649, \"height\": 835, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-21-739810-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1659, \"height\": 1621, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-21-739810-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1640, \"height\": 1257, \"label\": \"Figure\"}]"
motivation: 现有空间多组学整合方法依赖空间坐标，但大量RNA-ATAC数据是解离的非空间数据，无法直接利用空间信息。
method: SpatialJEPA采用JEPA式教师-学生框架，学生输入将教师的空间邻域图替换为自恒等图以遮蔽空间上下文，学习匹配教师嵌入。
result: 在鼠脑多组学中，表征支持源-目标对齐，恢复空间组织转录组和染色质可及性程序，与配体-受体通路结构一致。
conclusion: SpatialJEPA有效将空间上下文从空间数据蒸馏至非空间数据，提升解离多组学数据的空间感知能力。
---

## 摘要
用于整合空间基因组学模态的计算框架扩展了跨分子层的基于细胞的表示学习，但许多配对的RNA-ATAC数据集是解离的且缺乏空间坐标。我们提出SpatialJEPA，一种受JEPA启发的教师-学生框架，用于将空间多组学数据的空间上下文迁移到非空间多组学数据。与掩码补丁或特征的策略不同，SpatialJEPA通过在学生训练期间将教师的空间邻接图替换为仅自我的恒等图来掩盖空间上下文，使得空间样本在学生看来如同解离的。学生从这种图上下文受限的视角学习匹配教师嵌入，从而可以在推理时应用于解离的RNA-ATAC数据。在小鼠脑多组学中，所得表示支持源-目标对齐，恢复空间组织的转录组和染色质可及性程序，并且与空间参考相比，显示出与配体-受体通路结构的一致性。已被CIBB 2026会议接收（https://cibb2026.teralab.ai/）

## Abstract
Computational frameworks for integrating spatial genomics modalities extend cell-based representation learning across molecular layers, but many paired RNA-ATAC datasets are dissociated and lack spatial coordinates. We introduce SpatialJEPA, a JEPA-inspired teacher-student framework for transferring spatial context from spatial multiomics data to non-spatial multiome data. In contrast to patch- or feature-masking objectives, SpatialJEPA masks spatial context by replacing the teacher's spatial neighborhood graph with a self-only identity graph during student training, making the spatial sample appear dissociated to the student. The student learns to match teacher embeddings from this graph-context-restricted view and can therefore be applied to dissociated RNA-ATAC data at inference time. In mouse brain multiomics, the resulting representation supports source-target alignment, recovers spatially organized transcriptomic and chromatin-accessibility programs, and shows concordance with ligand-receptor pathway structure compared with non-spatial references. Accepted at the CIBB 2026 conference (https://cibb2026.teralab.ai/)