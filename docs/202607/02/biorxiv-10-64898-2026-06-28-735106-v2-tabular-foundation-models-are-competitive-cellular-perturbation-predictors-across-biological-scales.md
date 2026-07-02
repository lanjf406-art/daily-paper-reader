---
title: Tabular Foundation Models Are Competitive Cellular Perturbation Predictors Across Biological Scales
title_zh: 表格基础模型在跨生物尺度的细胞扰动预测中具有竞争力
authors: "Palla, G., Hillsley, A., Kim, Y.-J., Royer, L. A."
date: 2026-07-02
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.28.735106v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 表格基础模型用于扰动预测；适用于药物耐药预测
tldr: 细胞扰动预测是药物发现与功能基因组学的核心挑战。当前领域特定单细胞基础模型虽多，但其实际优势不明确。本文系统评估了通用表格基础模型（如TabICL、TabPFN）与领域特定模型在四种细胞预测场景中的表现。结果发现，表格基础模型在多个层次上相当或优于专用模型，表明通用上下文学习可作为有力的可扩展替代方案。
source: biorxiv
selection_source: fresh_fetch
motivation: 评估通用表格基础模型在细胞扰动预测中是否比领域特定模型更具优势。
method: 比较TabICL、TabPFN等表格基础模型与PRESAGE、scGPT等专用模型在细胞级、伪批量、全基因组筛选及胚胎发育扰动任务上的性能。
result: 表格基础模型在跨细胞类型预测、伪批量预测及胚胎细胞类型组成预测中均达到或超过专用模型。
conclusion: 通用表格上下文学习为细胞扰动响应建模提供了强大且可扩展的替代方案。
---

## 摘要
预测细胞如何响应遗传和化学扰动是药物发现和功能基因组学中的一个核心挑战。针对这一问题，已开发出一个日益壮大的专业单细胞基础模型生态系统，但它们相对于领域无关方法的实际优势仍不明确。在此，我们评估了表格基础模型（如TabICL和TabPFN，即通用预训练回归模型）与领域特定架构（包括PRESAGE、scGPT、scLAMBDA、STACK和Prophet）在四个互补评估设置中的表现：细胞层面上下文内跨细胞类型预测、基于五个细胞系Perturb-seq数据集的伪批量扰动预测、原代人CD4+ T细胞的全基因组CRISPR筛选，以及斑马鱼发育扰动图谱中的胚胎级细胞类型组成预测。在细胞层面跨细胞类型扰动预测中，表格基础模型的表现与专业模型相当或更优。在伪批量扰动预测中，表格基础模型在多个评估指标和数据集上持续优于专业基线。在全胚胎细胞类型组成预测中，表格基础模型与专业基线具有竞争力。这些结果表明，通用的表格上下文内学习为跨细胞系统和尺度的扰动响应建模提供了强大且可扩展的替代方案，可替代特制的生物学架构。

## Abstract
Predicting how cells respond to genetic and chemical perturbations is a central challenge in drug discovery and functional genomics. A growing ecosystem of specialized single-cell foundation models has been developed to address this problem, yet their practical advantage over domain-agnostic approaches remains unclear. Here we evaluate the power of Tabular Foundation Models such as TabICL and TabPFN, general-purpose pre-trained regression models, against domain-specific architectures including PRESAGE, scGPT, scLAMBDA, STACK and Prophet across four complementary evaluation settings: cell-level in-context cross-cell-type prediction, pseudobulk perturbation prediction on five Perturb-seq datasets of cell-lines, a genome-wide CRISPR screen in primary human CD4+ T cells, and embryo-level cell-type composition prediction in a zebrafish developmental perturbation atlas. In the cell-level cross-cell type perturbation prediction, Tabular Foundation Models perform on par or better than specialized models. On pseudobulk perturbation prediction, Tabular Foundation Models consistently outperform specialized baselines across multiple evaluation metrics and datasets. On whole-emrbryo cell-type composition prediction, Tabular Foundation Models are competitive with specialized baselines. These results demonstrate that general-purpose tabular in-context learning provides a strong and scalable alternative to bespoke biological architectures for perturbation response modeling across cell systems and scales.