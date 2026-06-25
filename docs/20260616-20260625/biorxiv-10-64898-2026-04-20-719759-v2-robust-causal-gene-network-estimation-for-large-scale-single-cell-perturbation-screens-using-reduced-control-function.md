---
title: Robust causal gene network estimation for large-scale single-cell perturbation screens using reduced control function
title_zh: 基于简约控制函数的大规模单细胞扰动筛选稳健因果基因网络估计
authors: "Ge, C., Li, H."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.04.20.719759v2.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 用于耐药机制发现的单细胞CRISPR筛选因果基因网络估计
tldr: 单细胞CRISPR扰动筛选中的因果网络推断面临潜变量混杂、计数型表达数据和高感染复数设计三大挑战。RICE框架通过重新表述控制函数克服了排除限制违反问题，结合约束负二项模型和可微无环惩罚，在GPU上高效扩展。合成实验和真实CRISPRi数据中，RICE均优于现有方法，并成功重构黑色素瘤细胞中IFN-γ信号通路，发现常规检验遗漏的稳健调控候选。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有因果推断方法难以同时处理潜变量混杂、计数数据和高MOI设计中的约束违反问题。
method: 提出RICE框架，核心是重新表述的控制函数，配对约束负二项模型与可微无环惩罚，支持硬/软干预和高MOI。
result: 在合成基准和CRISPRi实验中持续最优，在保留数据上因果发现更强，重构IFN-γ通路并识别稳健候选。
conclusion: RICE为单细胞扰动基因组学提供了稳健、可扩展的因果发现工具，克服了关键实际挑战。
---

## 摘要
单细胞CRISPR扰动筛选为基因调控网络中的因果发现提供了基础，但现有方法在处理潜在混杂、计数值表达数据和高多重感染（高MOI）设计方面存在困难。我们提出RICE，一个统一框架来解决所有这三个挑战。其核心是针对网络估计场景重新制定的控制函数，该函数恢复了对排除限制违反的稳健性，这种违反在真实CRISPR筛选中普遍存在，并导致标准控制函数方法失效。RICE将该估计器与约束负二项模型和可微无环性惩罚配对，容纳硬干预和软干预，并在单个GPU可扩展模型中原生支持高MOI设计。在广泛的合成基准测试中，RICE持续优于现有方法，并在强混杂、排除违反和高MOI条件下保持稳定。应用于CRISPRi筛选时，RICE在保留数据上实现了更强的因果发现性能。RICE进一步在免疫刺激下重建了黑色素瘤细胞中的经典干扰素（IFN）-γ信号通路，并提名了由于统计功效有限而被常规显著性检验可能忽略的稳定调控候选因子。总之，这些结果使RICE成为单细胞扰动基因组学中因果发现的稳健且可扩展的框架。

## Abstract
Single-cell CRISPR perturbation screens provide a foundation for causal discovery in gene regulatory networks, but existing methods struggle with latent confounding, count-valued expression data, and high-multiplicity-of-infection (high-MOI) designs. We introduce RICE, a unified framework that addresses all three challenges. At its core is a reformulated control function tailored to the network-estimation setting, which restores robustness to exclusion-restriction violations that are pervasive in real CRISPR screens and that cause standard control function approaches to fail. RICE pairs this estimator with a constrained negative binomial model and a differentiable acyclicity penalty, accommodating hard and soft interventions and natively supporting high-MOI designs within a single, GPU-scalable model. Across extensive synthetic benchmarks, RICE consistently outperforms existing methods and remains stable under strong confounding, exclusion violations, and high-MOI conditions. Applied to CRISPRi screens, RICE achieves stronger causal-discovery performance on held-out data. RICE further reconstructs the canonical interferon (IFN)-{gamma} signaling pathway in melanoma cells upon immune stimulation, and nominates stable regulatory candidates that conventional significance tests may overlook due to limited statistical power. Together, these results establish RICE as a robust and scalable framework for causal discovery in single-cell perturbation genomics.