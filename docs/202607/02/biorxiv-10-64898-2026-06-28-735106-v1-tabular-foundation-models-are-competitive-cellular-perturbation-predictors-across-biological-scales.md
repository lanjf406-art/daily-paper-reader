---
title: Tabular Foundation Models Are Competitive Cellular Perturbation Predictors Across Biological Scales
title_zh: 表格基础模型在不同生物尺度上是具有竞争力的细胞扰动预测器
authors: "Palla, G., Hillsley, A., Kim, Y.-J., Royer, L. A."
date: 2026-07-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.28.735106v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 表格基础模型用于预测细胞扰动响应，与耐药预测相关
tldr: 细胞扰动预测是药物发现的关键挑战，现有专业基础模型性能是否优于通用模型尚不明确。本研究系统比较了Tabular Foundation Models（如TabICL和TabPFN）与scGPT等专业模型在四种实验设置下的表现。结果显示，通用模型在交叉细胞类型、伪批量、CRISPR筛选及胚胎发育等任务中均与专业模型持平或更优。这表明通用表格上下文学习可作为可扩展的替代方案。
source: biorxiv
selection_source: fresh_fetch
motivation: 评估通用表格基础模型与领域特定模型在细胞扰动预测中的实际优势。
method: 在细胞级、伪批量、CRISPR筛选和胚胎发育四种设置下，比较TabICL/TabPFN与scGPT等模型的性能。
result: Tabular Foundation Models在所有设置中与专业模型相当或更优，尤其在伪批量预测中一致超越专业基线。
conclusion: 通用表格上下文学习为跨细胞系统和尺度的扰动响应建模提供了强大且可扩展的替代方案。
---

## 摘要
预测细胞如何响应遗传和化学扰动是药物发现和功能基因组学中的一个核心挑战。针对这一问题，越来越多的专用单细胞基础模型被开发出来，但它们相对于领域无关方法的实际优势仍不清楚。在此，我们在四个互补的评估场景中评估了表格基础模型（如TabICL和TabPFN，通用预训练回归模型）与领域特定架构（包括PRESAGE、scGPT、scLAMBDA、STACK和Prophet）的性能：细胞水平的上下文跨细胞类型预测、基于五个细胞系Perturb-seq数据集的伪批量扰动预测、原代人CD4+ T细胞的全基因组CRISPR筛选，以及斑马鱼发育扰动图谱中的胚胎水平细胞类型组成预测。在细胞水平的跨细胞类型扰动预测中，表格基础模型的表现与专用模型相当或更优。在伪批量扰动预测中，表格基础模型在多个评估指标和数据集上始终优于专用基线。在整个胚胎细胞类型组成预测中，表格基础模型与专用基线具有竞争力。这些结果表明，通用的表格上下文学习为跨细胞系统和尺度的扰动响应建模提供了强大且可扩展的替代方案，超越了定制化的生物架构。

## Abstract
Predicting how cells respond to genetic and chemical perturbations is a central challenge in drug discovery and functional genomics. A growing ecosystem of specialized single-cell foundation models has been developed to address this problem, yet their practical advantage over domain-agnostic approaches remains unclear. Here we evaluate the power of Tabular Foundation Models such as TabICL and TabPFN, general-purpose pre-trained regression models, against domain-specific architectures including PRESAGE, scGPT, scLAMBDA, STACK and Prophet across four complementary evaluation settings: cell-level in-context cross-cell-type prediction, pseudobulk perturbation prediction on five Perturb-seq datasets of cell-lines, a genome-wide CRISPR screen in primary human CD4+ T cells, and embryo-level cell-type composition prediction in a zebrafish developmental perturbation atlas. In the cell-level cross-cell type perturbation prediction, Tabular Foundation Models perform on par or better than specialized models. On pseudobulk perturbation prediction, Tabular Foundation Models consistently outperform specialized baselines across multiple evaluation metrics and datasets. On whole-emrbryo cell-type composition prediction, Tabular Foundation Models are competitive with specialized baselines. These results demonstrate that general-purpose tabular in-context learning provides a strong and scalable alternative to bespoke biological architectures for perturbation response modeling across cell systems and scales.