---
title: "FloREN: Decoding Immune Regulatory Networks through Interpretable Graph Transformer Patient Representations."
title_zh: FloREN：通过可解释的图Transformer患者表示解码免疫调控网络
authors: "Clemente-Larramendi, I., Hillion, S., Cornec, D., Jamin, C., Foulquier, N."
date: 2026-07-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.12.738088v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 可解释图变换器从scRNA-seq构建患者水平免疫调控网络
tldr: 单细胞RNA测序能刻画细胞异质性，但理解复杂组织的调控环境仍困难。现有样本表示方法多依赖无监督学习，可解释性差。本文提出FloREN，一种有监督可解释的样本表示方法，将单细胞数据建模为异质网络，整合细胞、基因、调控和细胞间通信关系，利用条件感知嵌入和可解释注意力网络。在免疫介导炎症性疾病中，FloREN实现了更好的样本分层和生物标志物发现，揭示了特定免疫网络机制。该框架为免疫调控网络解码提供了新工具。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-738088-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1689, \"height\": 455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-738088-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1632, \"height\": 659, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-738088-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1848, \"height\": 2082, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-738088-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1737, \"height\": 2048, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-738088-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1831, \"height\": 2696, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-738088-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1622, \"height\": 2915, \"label\": \"Figure\"}]"
motivation: 现有单细胞样本表示方法可解释性差，难以揭示免疫网络机制。
method: FloREN将单细胞数据建模为异质网络，通过条件感知嵌入和可解释注意力网络学习患者表示。
result: 在免疫介导炎症性疾病中，FloREN改进了样本分层和生物标志物发现，识别出关键免疫网络机制。
conclusion: FloREN提供了有监督可解释的样本表示框架，增强了对免疫调控网络的理解。
---

## 摘要
单细胞RNA测序（scRNA-seq）能够详细描述细胞异质性，但理解复杂组织的完整细胞和调控环境仍然具有挑战性。在大型单细胞图谱时代，这项技术变得越来越可及，数据集在规模和统计效力上不断增长。因此，样本表示方法已成为总结患者水平生物变异的有前景策略。然而，大多数现有方法依赖于无监督学习框架，其生物学可解释性模糊。在这里，我们提出了一个调控嵌入网络学习框架（FloREN），这是一种有监督且可解释的样本表示方法。FloREN将单细胞数据建模为异质网络，整合细胞和基因以及基因调控和细胞-细胞通信关系。通过条件感知嵌入和可解释的注意力网络，FloREN实现了改进的样本分层和生物标志物发现。此外，该框架支持下游分析，在免疫介导的炎症性疾病（IMIDs）中发现了特定的免疫网络机制。

## Abstract
Single-cell RNA sequencing (scRNA-seq) enables detailed characterization of cellular heterogeneity, yet understanding the full cellular and regulatory environment of complex tissues remains challenging. In the era of large single-cell atlases, this technology has become increasingly accessible, and datasets have grown in scale and statistical power. As a result, sample representation methods have emerged as a promising strategy to summarize patient-level biological variation. However, most existing approaches rely on unsupervised learning frameworks with ambiguous biological interpretability. Here we present a Framework for Learning Over REgulatory-Embedding Networks (FloREN), a supervised and interpretable sample representation method. FloREN models single-cell data as a heterogeneous network integrating cells and genes together with gene regulatory and cell-cell communication relationships. Through condition-aware embeddings and interpretable attention networks, FloREN enables improved sample stratification and biomarker discovery. In addition, the framework supports downstream analyses that found specific immune network mechanisms in immune-mediated inflammatory diseases (IMIDs).