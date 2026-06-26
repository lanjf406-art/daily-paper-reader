---
title: Learning Perturbation Effects Through Contrastive Alignment of Multimodal Biological Embeddings
title_zh: 通过多模态生物嵌入的对比对齐学习扰动效应
authors: "Long, W., Liu, T., Szalata, A., Theis, F. J., Xue, L., Zhao, H."
date: 2026-06-26
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.23.734145v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞扰动学习
tldr: 现有单细胞扰动表示学习方法针对单一模态，未能利用外部语义知识，限制了跨数据集和扰动类型的泛化。本文提出PertOmni，一种CLIP风格的多模态表示学习框架，通过掩码对比学习对齐转录组、文本和图像嵌入。在双向检索、药物-基因交互推断等任务上，该方法优于基线。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法局限于单一模态且缺乏外部知识，难以泛化到不同扰动数据集。
method: PertOmni采用CLIP风格框架，以掩码对比目标联合训练共享转录组编码器和数据集特定文本编码器，强调细胞内区分并消除细胞类型混杂。
result: 在小分子和CRISPRi扰动数据集上，PertOmni在双向检索、药物-基因交互推断等任务中均优于强基线。
conclusion: PertOmni通过多模态对齐有效提升了扰动效应表示的泛化性和任务性能。
---

## 摘要
多模态单细胞扰动筛选为表征遗传和化学干预对细胞状态的影响提供了一种可扩展的方法。然而，大多数现有的表示学习方法仅针对单一扰动模态，未能明确整合外部语义知识，这限制了它们在数据集和扰动类型之间的泛化能力。在此，我们提出PertOmni，一个CLIP风格的多模态表示学习框架，它将转录组扰动特征与来自精选基因和化合物描述的文本导出嵌入，以及来自细胞染色的图像导出嵌入对齐。PertOmni使用掩码对比目标联合训练一个共享的转录组编码器和特定数据集的文本编码器，该目标强调细胞类型内区分，同时减轻由细胞类型异质性引起的混杂效应。我们在小分子和CRISPRi扰动数据集上评估生成的联合嵌入空间在双向检索、药物-基因相互作用推断和扰动预测方面的表现，并展示出相对于强基线方法的一致改进。

## Abstract
Multimodal single cell perturbation screens offer a scalable approach for characterizing the effects of genetic and chemical interventions on cellular state. However, most existing representation learning methods are tailored to a single perturbation modality and fail to explicitly incorporate external semantic knowledge, which limits their ability to generalize across datasets and perturbation types. Here, we introduce PertOmni, a CLIP style multimodal representation learning framework that aligns transcriptomic perturbation signatures with text derived embeddings of curated genes and compound descriptions, as well as image derived embeddings from cell paintings. PertOmni jointly trains a shared transcriptomic encoder and dataset specific text encoders using a masked contrastive objective that emphasizes within cell type discrimination while mitigating confounding effects arising from cell type heterogeneity. We evaluate the produced joint embedding space on bidirectional retrieval, drug gene interaction inference, and perturbation prediction across both small molecule and CRISPRi perturbation datasets, and demonstrate consistent improvements over strong baseline methods.