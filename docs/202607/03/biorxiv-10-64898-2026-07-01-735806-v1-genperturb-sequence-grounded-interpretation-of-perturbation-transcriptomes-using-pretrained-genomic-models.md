---
title: "GenPerturb: sequence-grounded interpretation of perturbation transcriptomes using pretrained genomic models"
title_zh: GenPerturb：基于预训练基因组模型对扰动转录组的序列层面解释
authors: "Nikaido, I., Shiihashi, T."
date: 2026-07-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.01.735806v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 利用预训练模型解读扰动转录组，可应用于耐药机制研究
tldr: Perturb-seq扰动转录组学缺乏直接解析顺式调控元件或转录因子基序的能力。GenPerturb框架利用预训练序列到表达模型，对比扰动与对照状态，优先排序候选调控区域和基序。在多种扰动中识别出谱系特异性和信号相关基序活动，即使对应转录因子表达变化有限。无需匹配染色质数据即可将基因水平响应转化为扰动特异性顺式调控假说，指导下游实验验证。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有Perturb-seq分析无法直接解析顺式调控元件和转录因子基序，依赖间接分析或外部表观遗传注释。
method: GenPerturb利用预训练序列到表达模型，对比扰动与对照状态，优先排序候选调控区域和转录因子基序。
result: 模型在多种扰动中识别谱系特异性和信号相关基序活动，即使转录因子表达变化有限。
conclusion: GenPerturb将基因表达响应转化为扰动特异性顺式调控假说，无需染色质数据，实现机制解释并指导实验。
---

## 摘要
背景：Perturb-seq捕获数千种遗传和化学扰动下的转录响应，但不能直接解析这些响应背后的顺式调控元件或转录因子基序。现有方法依赖于间接的事后分析或外部表观基因组注释，难以将基因水平的响应与特定调控元件相关联。结果：我们提出GenPerturb框架，利用预训练的序列到表达模型将扰动诱导的表达变化与候选顺式调控元件联系起来。通过对比扰动状态和对照状态，GenPerturb优先识别与每种扰动相关的调控区域和转录因子基序。该模型能够重现扰动依赖的基因表达模式，并在无需匹配染色质数据的情况下实现序列层面的解释。在多种扰动类型中，GenPerturb识别出具有生物学意义的调控程序，包括谱系特异性和信号相关的基序活性，即使相应的转录因子表达变化有限。结论：GenPerturb将Perturb-seq的基因水平表达响应转化为扰动特异、基于序列的顺式调控假设。通过优先识别响应于每种扰动的候选调控元件和转录因子基序，且无需匹配的染色质数据，GenPerturb实现了对转录调控的机制性解释，并指导下游实验验证。

## Abstract
Background: Perturb-seq captures transcriptional responses to thousands of genetic and chemical perturbations, but does not directly resolve the cis-regulatory elements or transcription factor motifs underlying those responses. Existing approaches rely on indirect post hoc analyses or external epigenomic annotations, making it difficult to connect gene-level responses to specific regulatory element Results: We present GenPerturb, a framework that leverages pretrained sequence-to-expression models to link perturbation-induced expression changes to candidate cis-regulatory elements. By contrasting perturbation and control states, GenPerturb prioritizes regulatory regions and transcription factor motifs associated with each perturbation. The model recapitulates perturbation-dependent gene expression patterns and enables sequence-level interpretation without requiring matched chromatin data. Across multiple perturbation types, GenPerturb identifies biologically meaningful regulatory programs, including lineage-specific and signaling-associated motif activities, even when corresponding transcription factor expression changes are limited. Conclusions: GenPerturb converts gene-level expression responses from Perturb-seq into perturbation-specific, sequence-grounded cis-regulatory hypotheses. By prioritizing candidate regulatory elements and transcription factor motifs responsive to each perturbation without requiring matched chromatin data, GenPerturb enables mechanistic interpretation of transcriptional regulation and guides downstream experimental validation.