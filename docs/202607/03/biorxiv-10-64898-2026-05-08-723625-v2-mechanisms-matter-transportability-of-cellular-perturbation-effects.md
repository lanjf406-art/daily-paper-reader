---
title: "Mechanisms Matter: Transportability of Cellular Perturbation Effects"
title_zh: 机制重要：细胞扰动效应的可迁移性
authors: "Qi, S.-a., Chapfuwa, P."
date: 2026-07-02
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.08.723625v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 因果可迁移性框架，与药物耐药预测相关
tldr: 预测细胞扰动效应跨上下文泛化对药物开发至关重要，但深度学习模型常不敌简单基线。本研究基于因果可迁移性理论，指出跨上下文泛化依赖于共享因果机制，并开发因果模拟器生成半合成Perturb-seq数据，同时改进Vendi多样性分数以诊断模式崩溃。实验揭示明显跨上下文泛化差距：模型在因果机制不同的上下文间几乎无法迁移，表现降至基线水平。该工作强调需采用跨上下文评估、多样性感知指标及机械性归纳偏置来提升模型泛化能力。
source: biorxiv
selection_source: fresh_fetch
motivation: 深度学习模型在跨上下文预测细胞扰动效应时表现不佳，现有评估忽视因果机制差异，亟需理解泛化失效根源。
method: 基于因果可迁移性理论，构建可调机制差异的因果模拟器生成半合成Perturb-seq数据，并设计Vendi多样性分数检测模式崩溃。
result: 四种深度学习模型在跨上下文分裂下性能骤降至简单基线水平，且均无法泛化至因果机制不同的上下文。
conclusion: 跨上下文泛化由因果机制共享性决定，需引入机械性归纳偏置和多样性度量以推动模型进步。
---

## 摘要
预测细胞对不同生物背景下遗传或化学扰动的响应是药物开发和疾病理解的核心。尽管数据和模型规模不断增加，深度学习模型并未持续优于简单基线。利用因果可迁移性理论，我们表明跨背景泛化由共享因果机制主导，而不仅仅是分布相似性。为了实现受控评估，我们开发了一个因果模拟器，生成具有可调机制差异的真实半合成Perturb-seq数据集，并提供已知真实因果结构的基准。此外，我们将Vendi多样性分数适应于扰动设置，作为模式崩溃的诊断工具——这是标准每扰动指标无法发现的失败模式。在四个深度学习模型和六个简单基线上，对半合成和真实Perturb-seq数据集进行的大量实验揭示了跨背景泛化差距：跨背景分割下的性能大幅下降，通常降至简单基线水平。值得注意的是，即使在具有完全指定因果结构的合成数据上，也没有模型能泛化到具有不同因果机制的背景。这些结果强调了跨背景评估、多样性感知指标和基于机制的归纳偏见的必要性。

## Abstract
Predicting cellular responses to genetic or chemical perturbations across biological contexts is central to drug development and disease understanding. Despite increases in data and model scale, deep learning models have not consistently outperformed simple baselines. Leveraging causal transportability theory, we show that cross-context generalization is governed by shared causal mechanisms, not merely distributional similarity. To enable controlled evaluation, we develop a causal simulator that generates realistic semi-synthetic Perturb-seq datasets with tunable mechanistic divergence, providing benchmarks with known ground-truth causal structure. Further, we adapt the Vendi diversity score to the perturbation setting as a diagnostic for mode collapse, a failure mode invisible to standard per-perturbation metrics. Extensive experiments across four deep learning models and six simple baselines on semi-synthetic and real Perturb-seq datasets reveal a cross-context generalization gap: performance under cross-context splits drops substantially, often to simple baseline levels. Notably, even on synthetic data with fully specified causal structure, no model generalized across contexts with different causal mechanisms. These results underscore the need for cross-context evaluation, diversity-aware metrics, and mechanistically grounded inductive biases.