---
title: A unified analysis of cell-type and trajectory-associated pathways in single-cell data using Phoenix
title_zh: 使用Phoenix对单细胞数据中细胞类型和轨迹相关通路进行统一分析
authors: "Halperin, Y., Nachmani, D., Rabani, M."
date: 2026-06-19
pdf: "https://www.biorxiv.org/content/10.1101/2025.09.29.679361v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 单细胞通路分析工具Phoenix可识别耐药相关通路
tldr: 单细胞RNA测序数据中，传统通路分析方法难以捕捉与细胞类型或连续轨迹相关的微妙非线性活动。Phoenix框架利用随机森林模型与非参数显著性检验，评估功能基因集在区分细胞类型和伪时间排序中的相关性。在人类和小鼠造血及斑马鱼胚胎发育数据中，Phoenix识别出管家、发育和谱系特异性通路，且在小通路分析上优于现有工具。该框架为单细胞数据提供敏感且可解释的通路解析，有助于揭示动态基因调控机制。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法难以捕捉细胞类型和轨迹相关的非线性通路活动，限制了对单细胞数据的生物学解释。
method: Phoenix基于随机森林模型与非参数显著性检验，评估通路在分类和伪时间排序中的相关性并量化效应量。
result: 在造血和胚胎发育数据中，Phoenix优于现有工具，识别细胞类型特异和轨迹相关通路，且发现跨物种通路活动重叠更大。
conclusion: Phoenix为单细胞数据提供敏感且可解释的通路分析框架，有助于揭示动态基因调控机制。
---

## 摘要
单细胞RNA测序已极大地提升了我们在分子水平上解析生物样本中复杂细胞异质性的能力。然而，识别哪些生物学通路能准确反映不同的细胞类型或连续的细胞轨迹仍是一项重大挑战。传统方法常常遗漏微妙的或非线性的通路活性，限制了生物学可解释性和洞察力。为此，我们开发了Phoenix，这是一个通路分析框架，它利用随机森林模型和非参数显著性检验来评估功能基因集在区分细胞类型以及沿伪时间细胞轨迹组织细胞方面的相关性。Phoenix揭示了上调和下调的过程，包括由复杂非线性基因相互作用塑造的过程，并量化了它们的效应大小。应用于人类和小鼠的造血作用以及斑马鱼的胚胎发生，Phoenix识别了细胞类型特异性和轨迹相关的通路，涵盖管家、发育和谱系特异性程序。在捕获小通路的细胞类型特异性活性方面，它优于现有工具，并揭示了跨物种通路活性的更大重叠。最终，Phoenix提供了一个灵敏且可解释的框架，用于在复杂单细胞数据集中揭示生物学上有意义的通路并引发其组件之间的相互作用，为探索生物系统中动态基因调控开辟了新机遇。

## Abstract
Single-cell RNA sequencing has transformed our ability to resolve complex cellular heterogeneity within biospecimens at the molecular level. However, identifying which biological pathways accurately reflect distinct cell types or continuous cellular trajectories remains a major challenge. Traditional methods often miss subtle or non-linear pathway activities, limiting biological interpretability and insights. To address this, we develop Phoenix, a pathway analysis framework that leverages random forest models and non-parametric significance testing to evaluate the relevance of functional gene sets for distinguishing between cell-types and organizing cells along pseudotemporal cellular trajectories. Phoenix reveals both up- and downregulated processes, including those shaped by complex non-linear gene interactions, and quantifies their effect sizes. Applied to human and mouse hematopoiesis as well as zebrafish embryogenesis, Phoenix identifies both cell-type-specific and trajectory-associated pathways, spanning housekeeping, developmental, and lineage-specific programs. It outperforms existing tools in capturing cell-type-specific activities of small pathways and reveals greater overlap in pathway activities across species. Ultimately, Phoenix provides a sensitive and interpretable framework for uncovering biologically meaningful pathways and eliciting the interactions between their components in complex single-cell datasets, opening new opportunities to explore dynamic gene regulation across biological systems.