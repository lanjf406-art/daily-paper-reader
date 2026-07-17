---
title: "Mapping Tumor-Microenvironment dependencies with TMEformer: A spatial foundation framework enabling in silico perturbation"
title_zh: 利用TMEformer映射肿瘤-微环境依赖关系：一个支持虚拟扰动的空间基础框架
authors: "Chen, S., Zhu, G., Yang, L., Wei, X., Li, S., Liu, P., Chen, Q., Zhang, Z., Liu, D., Tang, Y., Xu, G., Zhou, M., Luo, J., Huang, L., Chen, B., Ou, S., Jiang, J."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.17.725770v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 肿瘤微环境空间建模
tldr: 现有虚拟扰动模型常忽略空间上下文，而肿瘤进展依赖微环境空间结构。本文提出TMEformer，利用高分辨率空间转录组显式建模肿瘤内在程序与局部微环境信号的联合作用。在多种肿瘤空间转录组数据中验证，TMEformer能进行虚拟扰动并捕捉细胞生态系统的功能依赖，在捕获谱系可塑性和治疗耐药等关键转变上优于大规模预训练基线模型。系统扰动分析优先出驱动疾病进展的转录因子和微环境配体，且其嵌入可改善肿瘤细胞的空间分层，建立了一个可扰动、空间耦合的肿瘤建模通用框架。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-17-725770-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1528, \"height\": 1535, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-17-725770-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1538, \"height\": 2212, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-17-725770-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1532, \"height\": 1813, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-17-725770-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1498, \"height\": 2059, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-17-725770-v2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1518, \"height\": 1991, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-17-725770-v2/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1529, \"height\": 2126, \"label\": \"Figure\"}]"
motivation: 现有虚拟扰动模型忽视空间上下文对肿瘤进展的关键作用，需建立空间感知的计算框架。
method: 提出TMEformer，基于空间转录组显式建模肿瘤细胞程序与局部微环境信号的联合效应，支持虚拟扰动。
result: TMEformer在谱系可塑性和耐药转变上优于大规模预训练模型，并优先出已知及新型驱动转录因子与微环境配体。
conclusion: TMEformer为空间耦合、可扰动的肿瘤生态系统建模提供通用框架，拓展肿瘤虚拟实验的可行性。
---

## 摘要
尽管空间背景在驱动肿瘤进展中起关键作用，但目前大多数用于虚拟扰动的计算模型在很大程度上忽视了其重要性。在此，我们引入TMEformer，一个肿瘤微环境感知的深度学习框架，通过显式结合空间结构，利用高分辨率空间转录组学来联合建模内在肿瘤细胞程序与局部微环境信号。经过多种肿瘤空间转录组学数据集的验证，TMEformer能够实现捕捉局部细胞生态系统中功能依赖关系的虚拟扰动。尽管仅在癌症特异性空间数据集上训练，TMEformer在捕捉关键肿瘤转变（包括谱系可塑性和治疗耐药性的出现）方面优于在大规模语料库上预训练的基线模型。系统性扰动分析优先考虑了驱动疾病进展的肿瘤内在转录因子和TME来源的配体，恢复了已知调控因子并揭示了新的候选因子。此外，TME来源的嵌入改善了肿瘤细胞的空间分层，并与病理结构更加一致。总之，TMEformer建立了一个将肿瘤建模为空间耦合、可扰动生态系统的通用框架。

## Abstract
Despite the fundamental role of spatial context in driving tumor progression, most current computational models for virtual perturbation have largely overlooked its importance. Here, we introduce TMEformer, a tumor microenvironment-aware deep learning framework that leverages high-resolution spatial transcriptomics to jointly model intrinsic tumor cell programs and local microenvironmental signals by explicitly incorporating spatial architecture. Validated across diverse tumor spatial transcriptomic cohorts, TMEformer enables virtual perturbations that capture functional dependencies within local cellular ecosystems. Despite being trained on cancer-specific spatial datasets, TMEformer outperforms baseline models pretrained on large-scale corpora in capturing key tumor transitions, including lineage plasticity and the emergence of therapy resistance. Systematic perturbation analyses prioritize tumor-intrinsic transcription factors and TME-derived ligands that drive disease progression, recovering established regulators and revealing novel candidates. Furthermore, TME-derived embeddings improve the spatial stratification of tumor cells and align more closely with pathological architecture. Together, TMEformer establishes a general framework for modeling tumors as spatially coupled, perturbable ecosystems.