---
title: "SHINE: Decoding transcriptional-metabolic microenvironments through higher-order spatial integration"
title_zh: "SHINE: 通过高阶空间整合解码转录-代谢微环境"
authors: "Du, B., Wong, J. W. H., Huang, Y."
date: 2026-07-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.10.737648v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 整合空间转录组和代谢组的生物信息学框架
tldr: 空间组学技术虽能共谱转录组和代谢组，但整合面临空间错位、分辨率差异和跨模态交互挑战。SHINE提出基于超图的计算框架，通过表示学习和跨模态交互联合分析空间基因表达和代谢网络。在帕金森病和多种癌症中，SHINE准确描绘区域并识别空间组织基因-代谢程序，性能优于现有方法。该框架为代谢-转录微环境提供可解释见解，实现跨生物系统的可扩展空间多组学整合。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737648-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1509, \"height\": 1746, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737648-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1505, \"height\": 2019, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737648-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1502, \"height\": 2169, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737648-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1512, \"height\": 1643, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-10-737648-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1522, \"height\": 1979, \"label\": \"Figure\"}]"
motivation: 解决空间转录组和代谢组整合中的空间错位、分辨率差异及高阶跨模态交互挑战。
method: 提出基于超图的计算框架SHINE，联合分析空间基因表达和代谢网络，实现表示学习和跨模态交互。
result: 在帕金森病和肿瘤数据上，SHINE准确描绘疾病区域，识别空间组织基因-代谢程序，性能优于现有方法。
conclusion: SHINE提供可解释的代谢-转录微环境见解，实现跨系统的可扩展空间多组学整合。
---

## 摘要
空间组学技术正在扩展，能够在同一组织切片上联合分析转录组和代谢组，提供基因表达和生化活性的互补视角，揭示天然组织微环境中的分子程序。然而，由于空间错位、分辨率差异和高阶跨模态相互作用，整合转录组和代谢组在技术上仍然具有挑战性。在此，我们提出SHINE，一个基于超图的计算框架，用于联合分析来自共分析切片的空间基因表达和代谢网络，重点关注表示学习和跨模态相互作用。在多个数据集中，SHINE在领域分割和生物标志物共定位方面持续优于现有方法，并为代谢-转录微环境提供可解释的见解。具体而言，在帕金森病小鼠模型中，SHINE精确描绘了多巴胺能神经元耗竭区域，并重建了连贯的多巴胺相关轴。在人类肺癌和乳腺癌中，SHINE解析了肿瘤相关空间区域，并识别了与肿瘤微环境相关的空间组织基因-代谢物程序。SHINE使得跨不同生物系统的可扩展空间多组学整合成为可能。

## Abstract
Spatial omics technologies are expanding to co-profile transcriptomics and metabolomics on the same tissue slide, providing complementary views of gene expression and biochemical activity to reveal molecular programs within native tissue microenvironments. However, integrating the transcriptome and metabolome remains technically challenging due to spatial misalignment, resolution disparity, and higher-order cross-modality interactions. Here, we present SHINE, a hypergraph-based computational framework for the joint analysis of spatial gene expression and metabolic networks derived from the co-profiling slide, focusing on representation learning and cross-modality interaction. Across multiple datasets, SHINE consistently outperformed existing methods for domain segmentation and biomarker co-localization and provided interpretable insights into metabolic-transcriptional microenvironments. Specifically, in Parkinson's disease mouse models, SHINE accurately delineates dopaminergic neuron-depleted regions and reconstructs coherent dopamine-associated axes. In human lung and breast cancers, SHINE resolves tumor-associated spatial regions and identifies spatially organized gene-metabolite programs associated with the tumor microenvironment. SHINE enables scalable spatial multi-omics integration across diverse biological systems.