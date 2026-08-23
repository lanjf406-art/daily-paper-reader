---
title: "Signature Recontextualization: Mapping perturbational signatures across biological contexts"
title_zh: 签名重构：跨生物学背景映射扰动签名
authors: "Chen, A. D., Girke, T., Monti, S."
date: 2026-08-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.14.744937v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 跨情境扰动特征预测，可迁移至药物应答与耐药建模
tldr: 跨上下文扰动签名预测缺乏统一基准。提出签名重语境化框架，定义三种目标数据覆盖模式及恢复评估指标。评估投影、网络、深度学习等方法于多数据集。结果显示简单方法不逊于复杂模型，可预测性与通路保守性等相关，并发布R包。
source: biorxiv
selection_source: fresh_fetch
motivation: 跨上下文预测扰动效应是重要问题，但现有基准评估任务、指标和数据集不一致，缺乏系统性比较。
method: 构建包含三种目标数据覆盖模式（仅对照、低覆盖、高覆盖）的基准框架，评估projectCor、netProp、scGPT、STACK及统计基线。
result: projection和network方法在多种扰动类型中表现强健，部分情况下匹敌或超越深度学习方法；预测性能与保守性、响应强度及基线相似性相关。
conclusion: 模型复杂度不必然提升跨上下文泛化，发布开源R包sigRecon以支持可复现基准与后续开发。
---

## 摘要
扰动转录组学是理解基因功能和药物效应的有力工具，然而预测扰动在不同生物学背景中的表现仍然是一个核心挑战，限制了从模型系统向临床相关组织的转化。尽管对该问题的兴趣日益增长，但基准测试工作一直受到评估任务不一致、指标异构以及跨扰动类型和生物系统评估有限等问题的阻碍。在此，我们引入了一个用于跨背景扰动签名预测的基准框架（我们将此任务定义为签名重构），该框架基于预测任务、目标数据可用性和以签名恢复为中心的评估指标的明确定义。该框架评估了三种目标背景数据模式下的预测性能：（1）仅对照，即仅测量目标背景中的对照谱；（2）低覆盖度，即测量目标背景中一个有限的扰动子集；（3）高覆盖度，即测量目标背景中的大多数扰动。这种设计能够系统评估预测性能如何依赖于目标背景的样本量，同时为比较方法提供标准化基础。我们评估了新开发的基于投影（projectCor）和基于网络（netProp）的方法，以及基于深度学习的基础模型（scGPT、STACK）和统计基线。该基准覆盖了四个不同的扰动数据集：细胞系中的CRISPR敲除和药物扰动，以及来自DrugMatrix的大鼠组织体内化学扰动，将评估从孤立的细胞系模型扩展到组织水平反应。在各项任务中，投影和网络传播方法在不同扰动类型和生物学背景下表现出很强的灵活性，并且在多种情况下达到或超过了深度学习和基础模型的性能，这表明模型复杂性并不固有地改善跨背景泛化能力。我们进一步表明，扰动可预测性随通路保守性、转录反应强度以及源背景与目标背景之间的基线相似性而有显著变化。所有数据集、方法和评估工具均以开源R包（sigRecon）的形式发布，为可重复基准测试和未来方法开发提供了基础。

## Abstract
Perturbational transcriptomics is a powerful tool for understanding gene function and drug effects, yet predicting how perturbations manifest across different biological contexts remains a central challenge, limiting translation from model systems to clinically relevant tissues. Despite growing interest in this problem, benchmarking efforts have been hindered by inconsistent evaluation tasks, heterogeneous metrics, and limited assessment across perturbation types and biological systems. Here, we introduce a benchmarking framework for cross-context perturbation-signature prediction (a task we define as signature recontextualization), grounded in explicit definitions of the prediction task, target-data availability, and evaluation metrics centered on signature recovery. The framework evaluates prediction performance across three target-context data regimes: (1) control only, where only control profiles from the target context are measured; (2) low coverage, where a limited subset of perturbations in the target context are measured; and (3) high coverage, where most perturbations in the target context are measured. This design enables systematic assessment of how prediction performance depends on target-context sample size while providing a standardized basis for comparing methods. We evaluate newly developed projection-based (projectCor) and network-based (netProp) methods alongside deep learning-based foundation models (scGPT, STACK) and statistical baselines. The benchmark spans four diverse perturbational datasets: CRISPR knockdowns and drug perturbations in cell lines, plus in vivo chemical perturbations in rat tissues from DrugMatrix, extending evaluation beyond isolated cell-line models to tissue-level responses. Across tasks, projection and network propagation approaches show strong flexibility across perturbation types and biological contexts, and in several cases match or exceed the performance of deep learning and foundation models, suggesting that model complexity does not inherently improve cross-context generalization. We further show that perturbation predictability varies substantially with pathway conservation, transcriptional response strength, and baseline similarity between source and target contexts. All datasets, methods, and evaluation utilities are released as an open-source R package (sigRecon), providing a foundation for reproducible benchmarking and future method development.