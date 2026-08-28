---
title: "PASTRI: Resolving Stage-Specific Cell-State Dynamics from Annotated Cell Lineage Trees"
title_zh: PASTRI：从注释细胞谱系树解析阶段特异性细胞状态动态
authors: "Yang, W., Li, Z., Yu, X., Wu, P., Zhang, X., Ren, C., Liu, K., Chen, J., Chen, F., He, X., Zhang, J., Chen, X., Yang, J."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.16.745065v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 从单细胞谱系推断细胞状态转变的计算框架
tldr: 细胞在表型状态间的转换是发育和疾病的基础，但定量解析其动态过程颇具挑战。现有方法难以同时刻画阶段特异性的转变速率。本文提出PASTRI框架，基于带有末端状态注释的细胞谱系树，利用不同系统发育距离的细胞对推断状态转变速率，并避免发育过程中动态变化的影响。通过模拟数据和线虫胚胎谱系验证，并应用于三种谱系追踪数据集，揭示了肝星状细胞激活和肺祖细胞分化的限速步骤以及支持癌细胞增殖的吸引子状态，为解析细胞状态转变动态提供了新途径。
source: biorxiv
selection_source: fresh_fetch
motivation: 细胞状态转变动态的定量分析困难，现有方法无法解析发育过程中阶段特异性的转变速率。
method: 提出PASTRI框架，利用谱系树上不同系统发育距离的细胞对，推断带末端状态注释的细胞谱系的转变速率。
result: 在模拟和线虫数据中验证，并应用于多类谱系追踪数据，识别出肝星状细胞激活、肺祖细胞分化的限速步骤及癌细胞的吸引子状态。
conclusion: PASTRI可从注释细胞谱系中解析阶段特异的细胞状态转换动态，为发育和疾病研究提供有力工具。
---

## 摘要
细胞在不同表型状态之间的转变是发育和疾病的基础，然而对其动态的定量分析仍然具有挑战性。本文提出了PASTRI（基于系统发育邻接的状态转变率推断），一种从带有末端表型状态（如单细胞转录组）注释的细胞谱系/系统发育中推断转变率的计算框架。我们使用模拟谱系和秀丽隐杆线虫胚胎谱系验证了PASTRI。重要的是，通过利用不同系统发育距离上的细胞对，PASTRI能够准确解析阶段特异性的转变率，避免了动力学发育变化的问题。将PASTRI应用于我们谱系追踪实验中三个细胞系统发育数据集，涵盖不同的发育/疾病模型和追踪系统，PASTRI揭示了肝星状细胞激活和肺原始祖细胞分化中的限速步骤，以及支持癌细胞增殖的吸引子状态。因此，PASTRI为从注释细胞谱系/系统发育中解析细胞状态转变动态开辟了一条新途径。

## Abstract
Cellular transitions between phenotypic states are fundamental to development and disease, yet quantitative analysis of their dynamics remains challenging. Here we present PASTRI (Phylogenetic Adjacency-based State Transition Rate Inference), a computational framework that infers transition rates from cell lineages/phylogenies annotated with terminal phenotypic states, such as single-cell transcriptomes. We validate PASTRI using simulated lineages and the Caenorhabditis elegans embryonic lineage. Importantly, by leveraging cell pairs at varying phylogenetic distances, PASTRI accurately resolves stage-specific transition rates, circumventing the issue of developmental changes in dynamics. Applied to three cell phylogeny datasets from our lineage-tracing experiments spanning diverse developmental/disease models and tracing systems, PASTRI uncovers rate-limiting steps in the activation of hepatic stellate cells and the differentiation of primordial lung progenitors, as well as attractor states that support cancer cell proliferation. PASTRI thus opens up a venue for dissecting cell state transition dynamics from annotated cell lineage/phylogeny.