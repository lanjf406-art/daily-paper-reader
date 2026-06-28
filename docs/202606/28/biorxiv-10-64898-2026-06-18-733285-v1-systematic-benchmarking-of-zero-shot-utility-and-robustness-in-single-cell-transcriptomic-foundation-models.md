---
title: Systematic benchmarking of zero-shot utility and robustness in single-cell transcriptomic foundation models
title_zh: 单细胞转录组基础模型中零样本实用性与鲁棒性的系统基准测试
authors: "Liu, T., Feng, T., Pan, X., Chen, Y., Ren, L., Ye, X., Sakurai, T., Lin, H., Zhang, Y."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.18.733285v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞基础模型基准测试有助于肿瘤耐药转录组分析
tldr: 单细胞基础模型虽被广泛提出，但其零样本场景下的实用性和鲁棒性尚未系统评估。本研究对20种方法、6个下游任务、1607个数据集进行大规模基准测试，发现模型实用性与鲁棒性存在解耦，且无单一模型跨任务表现一致，经典统计表示在零样本下仍具竞争力。该工作定义了零样本使用的实际边界，为单细胞转录组表示选择提供决策框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 填补单细胞基础模型在零样本场景下实用性与鲁棒性系统性评估的空白。
method: 在20种方法、6个任务、1607个数据集上测试零样本性能，并分析数据集结构对性能变异的影响。
result: 实用性与鲁棒性解耦，模型在标准基准高排名时对数据集结构变化不稳定；经典统计表示仍具竞争力。
conclusion: 零样本使用需权衡性能与稳定性，本研究提供大规模基准和选择指南。
---

## 摘要
单细胞基础模型（scFMs）被提出作为转录组分析的可重用表示，但其在无任务特定微调情况下的实际效用和鲁棒性尚未完全表征。在此，我们系统评估了20种方法、6个下游任务和1607个数据集（涵盖近2180万个细胞）在零样本设置下的单细胞转录组表示。我们从三个互补维度表征了模型行为：基线效用、结构鲁棒性和性能变异性的数据集级驱动因素。我们的大规模分析揭示了效用与鲁棒性之间的解耦：在标准基准上排名靠前的方法通常在数据集结构变化下表现出明显的不稳定性。此外，没有单一模型在所有任务上表现一致。在若干任务中，基于高度可变基因的经典统计表示在零样本条件下仍具有竞争力。这些结果共同定义了scFMs中零样本使用的实际边界，并为单细胞基因组学中的表示选择提供了大规模基准和决策框架。

## Abstract
Single-cell foundation models (scFMs) have been proposed as reusable representations for transcriptomic analysis, yet their practical utility and robustness when applied without task-specific fine-tuning remain incompletely characterized. Here, we systematically evaluated single-cell transcriptomic representations in zero-shot settings across 20 methods, 6 downstream tasks and 1,607 datasets comprising nearly 21.8 million cells. We characterized model behavior along three complementary dimensions: baseline utility, structural robustness, and dataset-level drivers of performance variability. Our large-scale analysis reveals a decoupling between utility and robustness: methods ranking highly on standard benchmarks often show marked instability under shifts in dataset structure. Furthermore, no single model performs uniformly well across tasks. In several tasks, classical statistical representations based on highly variable genes remain competitive under zero-shot conditions. Together, these results define the practical boundaries of zero-shot use in scFMs and provide a large-scale benchmark and decision framework for representation selection in single-cell genomics.