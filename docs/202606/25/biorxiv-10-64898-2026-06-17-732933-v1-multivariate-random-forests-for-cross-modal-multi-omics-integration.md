---
title: Multivariate Random Forests for Cross-Modal Multi-Omics Integration
title_zh: 多变量随机森林用于跨模态多组学整合
authors: "Zhang, W., Wang, L., Franzmann, E. J., Chen, X. S."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.17.732933v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 多变量随机森林用于跨模态多组学整合
tldr: 多组学整合中，现有方法难以同时捕捉跨模态共享信号和单模态特异性结构。提出基于多元随机森林的MULTIC方法，从各组学层学习样本相似性并分离共享与模态特异性信号。模拟实验表明，在非线性结构下能更好恢复聚类；在TCGA头颈癌中共享成分对齐主流亚型，特异性成分揭示免疫和发育信号；在ADNI队列中共享信号预测认知衰退。该方法为多组学数据提供灵活的非线性整合工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法融合数据时易模糊单层强信号或依赖线性假设，需要能处理非线性关系并分离共享与特异性结构的方法。
method: 使用多元随机森林学习各组学层样本相似性，跨模态整合后估计算层可预测部分，残差作为模态特异性信号，分别聚类。
result: 模拟中恢复共享聚类优于或持平现有方法，并可靠分离非线性特异性信号；真实数据中共享成分对齐已知亚型，特异性成分补充生物学信息。
conclusion: MULTIC能够同时捕捉共病轴和具有生物学意义的单模态特异性信号，提供非线性、可解释的多组学整合框架。
---

## 摘要
多组学研究广泛应用于生物医学研究的许多领域。在许多疾病中，某些信号在不同数据类型之间共享，而其他信号则在单个组学层中最强。当前的多组学聚类方法通常要么将所有数据类型合并为单一表示，这可能会模糊在某一层中较强的生物学信息，要么依赖于可能遗漏跨数据类型更复杂关系的线性结构。我们引入了O_SCPLOWMULTIC_SCPLOWRF，一种基于随机森林的方法，用于处理复杂数据类型并分离多组学数据中的共享和模态特异性结构。O_SCPLOWMULTIC_SCPLOWRF从多元随机森林中学习跨组学层的样本相似性，将其跨数据类型组合，并利用所得权重估计每个组学层中可被其他层预测的部分。剩余残差被视为模态特异性信号，允许共享和模态特异性相似性分别进行聚类。在模拟中，O_SCPLOWMULTIC_SCPLOWRF恢复共享聚类的效果与已建立的整合方法相当或更好，同时在非线性数据结构下更可靠地分离模态特异性信号。在TCGA头颈部鳞状细胞癌中，共享成分与既定参考分类中的主要亚型结构一致，而基因和miRNA特异性成分揭示了额外的免疫和发育生物学。在匹配血液DNA甲基化和结构MRI的ADNI队列中，共享的跨模态衰老信号与未来转化为轻度认知障碍或阿尔茨海默病相关，而DNAm特异性残差信号显示了探索性的额外信息。这些结果表明，O_SCPLOWMULTIC_SCPLOWRF能够恢复共同的疾病轴，同时保留特定于一种数据类型的生物学有意义信号。O_SCPLOWMULTIC_SCPLOWRF作为开源R包可在https://github.com/novawz/multiRF获取。

## Abstract
Multi-omics studies are widely used across many areas of biomedical research. In many diseases, some signals are shared across data types, while others are strongest in a single omics layer. Current multi-omics clustering methods often either merge all data types into a single representation, which can blur biology that is strong in one layer, or rely on linear structure that may miss more complex relationships across data types. We introduce O_SCPLOWMULTIC_SCPLOWRF, a random-forest-based method that handles complex data types and separates shared and modality-specific structure for multi-omics data. O_SCPLOWMULTIC_SCPLOWRF learns sample similarities across omics layers from multivariate random forests, combines them across data types, and uses the resulting weights to estimate the part of each omics layer that is predictable from the others. The remaining residual is treated as modality-specific signal, allowing shared and modality-specific similarities to be clustered separately. In simulations, O_SCPLOWMULTIC_SCPLOWRF recovered shared clusters as well as or better than established integrative methods while more reliably separating modality-specific signal under nonlinear data structures. In TCGA head and neck squamous cell carcinoma, the shared component aligned with the main subtype structure across established reference classifications, while gene- and miRNA-specific components revealed additional immune and developmental biology. In the ADNI cohort with matched blood DNA methylation and structural MRI, the shared cross-modal aging signal was associated with future conversion to mild cognitive impairment or Alzheimers disease, and a DNAm-specific residual signal showed exploratory additional information. These results show that O_SCPLOWMULTIC_SCPLOWRF can recover a common disease axis while retaining biologically meaningful signals specific to one data type. O_SCPLOWMULTIC_SCPLOWRF is available as an open-source R package at https://github.com/novawz/multiRF.