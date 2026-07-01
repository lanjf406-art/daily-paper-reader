---
title: "GenoME: a MoE-based generative model for individualized, multimodal prediction and perturbation of genomic profiles"
title_zh: GenoME：基于混合专家模型的生成模型，用于基因组图谱的个性化、多模态预测与扰动
authors: "Wei, J., Xue, Y., Chai, H., Gao, Y. Q."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.64898/2025.12.28.696482v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 基于MoE的多模态基因组预测生成模型，支持多组学表征
tldr: 非编码基因组的调控机制复杂，现有模型难以整合多模态数据。GenoME基于MoE架构，利用DNA序列和细胞类型特异的ATAC-seq信号，预测表观基因组、转录组和染色质架构。该模型可对保留区域进行多尺度预测，并泛化到未见或个性化的细胞类型。通过in silico扰动，它能准确预测遗传变异的多模态后果并识别功能增强子-启动子连接，为多尺度基因组生成与因果机制研究提供统一平台。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有模型难以整合非编码基因组的多模态调控模式，需开发能统一预测表观组、转录组和三维染色质结构的生成模型。
method: 采用混合专家（MoE）生成模型，以DNA序列和细胞类型特异ATAC-seq为输入，输出碱基到千碱基分辨率的统一基因组概况。
result: 模型精准预测保留基因组区域，泛化至未见细胞类型；通过in silico扰动预测遗传变异的多模态效应，优于Activity-by-Contact等模型。
conclusion: GenoME实现了跨细胞类型泛化与因果推断的一体化平台，可用于解析转录因子语法和调控机制。
---

## 摘要
非编码基因组通过一个复杂的多尺度调控系统运作，其中受调控的基因表达与细胞类型特异性组蛋白修饰、转录因子结合和三维构象密切相关。开发能够整合这些模式以预测和解读调控系统的计算模型仍然具有挑战性。在这里，我们提出了GenoME，一个基于混合专家（MoE）的生成模型，它利用DNA序列和细胞类型特异性的ATAC-seq信号，预测从碱基对到千碱基分辨率的多组学图谱，包括表观基因组、转录组和染色质结构。GenoME能够对留出的基因组区域进行多尺度预测，并且关键的是，它能够仅从单个ATAC-seq输入推广到预测未见或个性化细胞类型的完整调控景观。我们为GenoME配备了计算机模拟扰动框架，该框架能准确预测遗传扰动的多模式后果，并识别功能性增强子-启动子连接，其性能优于Activity-by-Contact等专门模型。这些预测还可用于解读细胞类型特异性增强子的转录因子语法。因此，GenoME提供了一个多功能的一体化平台，用于多尺度调控基因组的生成建模、跨细胞类型泛化以及因果机制研究。

## Abstract
The non-coding genome operates through a complex, multiscale regulatory system where regulated gene expressions are closely associated with cell-type-specific histone modifications, transcription factor binding and 3D conformation. Developing computational models that can integrate these patterns to predict and interpret the regulatory system remains challenging. Here, we present GenoME, a Mixture of Experts (MoE)-based generative model that uses DNA sequence and cell-type-specific ATAC-seq signals to predict a unified genomic profile encompassing epigenomics, transcriptomics, and chromatin architecture at base-pair to kilobase resolutions. GenoME enables multiscale predictions for held-out genomic regions and, critically, generalizes to predict the full regulatory landscape of unseen or individualized cell types from a single ATAC-seq input. We equip GenoME with an in silico perturbation framework that accurately forecasts the multimodal consequences of genetic perturbations and identifies functional enhancer-promoter connections, outperforming specialized models like Activity-by-Contact. These predictions can also be used to decipher the transcription factor grammar of cell-type-specific enhancers. GenoME thus provides a versatile, all-in-one platform for generative modeling, cross-cell-type generalization, and causal mechanistic investigation of the multiscale regulatory genome.