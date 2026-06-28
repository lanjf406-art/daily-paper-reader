---
title: "IntegrateRigor: annotation-free integration optimization for cell identity recovery reveals cancer-immune interface niches"
title_zh: IntegrateRigor：无标注整合优化实现细胞身份恢复，揭示癌症-免疫界面微环境
authors: "Zhai, Z., Wang, C., Jiang, C., Rong, Z., Li, J. J."
date: 2026-06-27
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.14.725078v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 整合优化癌细胞-免疫交界区域有助于单细胞耐药机制研究
tldr: 单细胞及空间转录组数据跨批次整合时，批次去除与细胞身份保留存在冲突，现有方法易出现过整合或欠整合。IntegrateRigor通过基因批次稳定性评分和数据集级整合评分，无标注地自动优化整合配置。在结直肠癌数据中揭示被默认欠整合和以往过整合掩盖的癌-免疫界面微环境，并在多数据集上提升五种方法的细胞身份恢复。将整合从启发式预处理转变为统计原则的数据自适应过程，提高大规模分析的可重复性和生物学发现能力。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有整合方法因依赖通用基因选择和缺乏无标注调参指标，常导致过/欠整合，影响细胞身份恢复。
method: 提出IntegrateRigor，通过基因批次稳定性评分和数据集级整合评分，无标注地自动选择稳定基因并优化整合参数。
result: 在结直肠癌数据中发现被掩盖的癌-免疫界面微环境，并在多样本上缓解过/欠整合，提升五种方法的细胞身份恢复。
conclusion: 将整合从启发式预处理转变为统计原则的数据自适应流程，提高大规模分析的可重复性和生物学发现能力。
---

## 摘要
整合不同批次的单细胞和空间转录组数据对于恢复可比较的细胞身份（包括细胞类型、亚型和状态）至关重要，这是多条件和大规模研究中下游分析的前提。这一任务仍然具有挑战性，因为批次间变异去除常常与细胞身份保持相冲突，且当前方法通常依赖于通用的高度可变基因选择，并在缺乏细胞身份注释时缺乏超参数调整的原则性指标。这些限制共同导致过度整合（合并生物学上不同的细胞身份）或欠整合（细胞按批次而非身份分离）。在此，我们提出IntegrateRigor，一种数据驱动、无注释、方法无关的框架，它专门针对跨批次可靠恢复细胞身份进行优化整合。IntegrateRigor首先使用基于基因的似然批次稳定性评分选择表达模式跨批次稳定的基因，排除可能偏差细胞身份对齐的批次敏感基因。然后，通过定义一个数据集级别的整合评分，该评分明确平衡批次间变异去除与细胞身份保持，而无需先验注释，从而跨方法和超参数确定最佳整合配置。在结直肠癌单细胞和空间转录组数据集中，IntegrateRigor揭示了肿瘤微环境中先前未表征的癌症-免疫界面微环境，这些微环境在默认设置下被欠整合掩盖，并在先前文献中被过度整合。在跨多个批次变异来源的不同数据集中，IntegrateRigor通过缓解五种最先进方法中的过度整合和欠整合，持续改进了细胞身份恢复。通过将整合从启发式预处理步骤转变为用于细胞身份恢复的统计原则性、数据集自适应程序，IntegrateRigor提高了大规模单细胞和空间转录组分析的可重复性和生物学发现能力。

## Abstract
Integrating single-cell and spatial transcriptomics data across batches is essential for recovering comparable cell identities (including cell types, subtypes, and states) as a prerequisite for downstream analyses in multi-condition and large-scale studies. This task remains challenging because between-batch variation removal often conflicts with cell identity preservation, and current methods typically rely on generic highly variable gene selection and lack principled metrics for hyperparameter tuning when cell identity annotations are unavailable. Together, these limitations often lead to over-integration, which merges biologically distinct cell identities, or under-integration, which leaves cells separated by batch rather than identity. Here we introduce IntegrateRigor, a data-driven, annotation-free, method-agnostic framework that optimizes integration specifically for reliable cell identity recovery across batches. IntegrateRigor first selects genes whose expression patterns are stable across batches using a gene-wise likelihood- based batch stability score, excluding batch-sensitive genes that can bias cell identity alignment during integration. It then identifies the optimal integration configuration across methods and hyperparameters by defining a dataset-level integration score that explicitly balances between-batch variation removal against cell identity preservation, without requiring prior annotations. In a colorectal cancer single-cell and spatial transcriptomics dataset, IntegrateRigor revealed previously uncharacterized cancer-immune interface niches in the tumor microenvironment that were masked by under-integration under default settings and by over-integration in previous literature. Across diverse datasets spanning multiple sources of between-batch variation, IntegrateRigor consistently improved cell identity recovery by mitigating both over-integration and under-integration across five state-of-the-art methods. By transforming integration from a heuristic preprocessing step into a statistically principled, dataset-adaptive procedure for cell identity recovery, IntegrateRigor improves the reproducibility and biological discovery power of large-scale single-cell and spatial transcriptomics analyses.