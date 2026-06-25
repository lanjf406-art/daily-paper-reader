---
title: A unified analysis of cell-type and trajectory-associated pathways in single-cell data using Phoenix
title_zh: 使用Phoenix对单细胞数据中细胞类型和轨迹相关通路进行统一分析
authors: "Halperin, Y., Nachmani, D., Rabani, M."
date: 2026-06-19
pdf: "https://www.biorxiv.org/content/10.1101/2025.09.29.679361v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞通路分析框架，可用于耐药性研究
tldr: 单细胞RNA测序能解析细胞异质性，但识别反映细胞类型或连续轨迹的生物学通路面临挑战，传统方法常遗漏非线性或小通路活动。Phoenix框架利用随机森林和非参数显著性检验评估功能基因集的相关性。在人类和小鼠造血及斑马鱼胚胎发生中，Phoenix识别了细胞类型特异和轨迹相关通路，包括管家、发育和谱系特异程序，优于现有工具，尤其在小通路捕捉上。该框架灵敏可解释，揭示复杂单细胞数据集中的生物学通路及其交互作用。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法难以捕捉非线性或小通路的细胞类型或轨迹特异性活动，限制生物学解释。
method: 利用随机森林模型和非参数显著性检验评估通路区分细胞类型和拟时间轨迹的能力。
result: 在造血和胚胎发育数据中识别多种特异通路，优于现有工具，尤其在小通路上。
conclusion: Phoenix为单细胞数据提供灵敏可解释的通路分析框架，揭示动态基因调控。
---

## 摘要
单细胞RNA测序已经改变了我们在分子水平上解析生物样本中复杂细胞异质性的能力。然而，识别哪些生物学通路准确反映了不同的细胞类型或连续的细胞轨迹仍然是一个主要挑战。传统方法常常遗漏微妙或非线性的通路活动，限制了生物学的可解释性和洞察力。为了解决这个问题，我们开发了Phoenix，一个通路分析框架，它利用随机森林模型和非参数显著性检验来评估功能基因集在区分细胞类型和沿着伪时间细胞轨迹组织细胞方面的相关性。Phoenix揭示了上调和下调的过程，包括那些由复杂的非线性基因相互作用形成的过程，并量化了它们的影响大小。应用于人类和小鼠的造血作用以及斑马鱼的胚胎发生，Phoenix识别了细胞类型特异性和轨迹相关的通路，涵盖了持家、发育和谱系特异性程序。它在捕捉小型通路的细胞类型特异性活动方面优于现有工具，并揭示了跨物种通路活动的更大重叠。最终，Phoenix提供了一个敏感且可解释的框架，用于发现具有生物学意义的通路，并引发其组件在复杂单细胞数据集中的相互作用，为探索跨生物系统的动态基因调控开辟了新的机会。

## Abstract
Single-cell RNA sequencing has transformed our ability to resolve complex cellular heterogeneity within biospecimens at the molecular level. However, identifying which biological pathways accurately reflect distinct cell types or continuous cellular trajectories remains a major challenge. Traditional methods often miss subtle or non-linear pathway activities, limiting biological interpretability and insights. To address this, we develop Phoenix, a pathway analysis framework that leverages random forest models and non-parametric significance testing to evaluate the relevance of functional gene sets for distinguishing between cell-types and organizing cells along pseudotemporal cellular trajectories. Phoenix reveals both up- and downregulated processes, including those shaped by complex non-linear gene interactions, and quantifies their effect sizes. Applied to human and mouse hematopoiesis as well as zebrafish embryogenesis, Phoenix identifies both cell-type-specific and trajectory-associated pathways, spanning housekeeping, developmental, and lineage-specific programs. It outperforms existing tools in capturing cell-type-specific activities of small pathways and reveals greater overlap in pathway activities across species. Ultimately, Phoenix provides a sensitive and interpretable framework for uncovering biologically meaningful pathways and eliciting the interactions between their components in complex single-cell datasets, opening new opportunities to explore dynamic gene regulation across biological systems.