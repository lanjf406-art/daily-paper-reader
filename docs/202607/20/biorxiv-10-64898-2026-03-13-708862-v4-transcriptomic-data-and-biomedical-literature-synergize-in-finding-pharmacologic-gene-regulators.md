---
title: Transcriptomic data and biomedical literature synergize in finding pharmacologic gene regulators
title_zh: 转录组数据与生物医学文献协同发现药理基因调控因子
authors: "Deisseroth, C. A., Brazelton, B., Shaik, Z., Sandberg, B. S., Liu, Z., Zoghbi, H. Y."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.13.708862v4.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 转录组数据和文献挖掘用于药物靶点发现
tldr: 大多数单基因疾病因基因产物缺乏或过量而缺乏靶向疗法。本文提出SNACKKSS方法，自动从Gene Expression Omnibus中策展基因敲除/敲低和药物处理研究，结合统一计算的RNA-Seq数据，直接预测药物-基因调控关系。交叉验证表明其SA4变体在发现蛋白抑制化合物方面有独特贡献，且集成多个预测工具效果更佳。结果表明，自动策展的RNA-Seq特征与文献和共表达预测器结合，能有效支持药物重定位优先排序。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1963, \"height\": 990, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1405, \"height\": 1384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1971, \"height\": 1983, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1949, \"height\": 991, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1704, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1709, \"height\": 669, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1973, \"height\": 563, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v4/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1897, \"height\": 887, \"label\": \"Table\"}]"
motivation: 手工标注RNA-Seq研究标签耗时费力，需要自动策展基因干扰和药物研究数据以加速药物靶点发现。
method: SNACKKSS自动从GEO中提取基因敲除/敲低及小分子研究标签，并整合统一计算的RNA-Seq读计数数据，通过构建调控关系网络进行预测。
result: 交叉验证显示SNACKKSS的SA4变体在预测蛋白抑制化合物方面具有独特价值，并且集成多个预测工具可提升整体性能。
conclusion: 自动策展的RNA-Seq签名与文献和共表达预测器结合，为药物重定位提供了有力的优先排序策略。
---

## 摘要
大多数由单个基因产物缺乏或过量引起的疾病缺乏靶向治疗。由于这些疾病可以通过基因过表达、敲除或敲降来模拟，因此能够对抗此类扰动转录组效应的药物可能是有前景的治疗候选药物。RNA测序（RNA-Seq）研究可以促进这种药物优先排序，但其用自然语言编写的标签需要手动注释。因此，我们引入了基于自动筛选的敲除、敲降和小分子研究特征网络（SNACKKSS），该网络自动从基因表达综合库中筛选基因破坏和药物治疗研究，并与统一计算的读数计数数据集合作，直接将标签和RNA-Seq数据输入调控关系预测。通过交叉验证，我们表明SNACKKSS预测（特别是来自一种称为“SA4”的变体）即使在现有预测因子存在的情况下，也为寻找蛋白质抑制化合物做出了独特贡献。我们证明了聚合多种预测工具的好处，并提供了这个强大的集成模型以及SNACKKSS。重要的是，我们建议研究人员在多个设备上测试复杂的机器学习模型，因为硬件架构可能影响其输出。尽管如此，下游预测能力令人瞩目，我们的研究结果支持将自动筛选的RNA-Seq特征与基于文献和共表达的预测因子整合用于药物重定位优先排序的价值。

## Abstract
Most disorders caused by a deficiency or excess of one gene product lack targeted therapies. Since these disorders can be modeled with a gene overexpression, knockout, or knockdown, drugs that oppose the transcriptomic effects of such perturbations may be promising therapeutic candidates. RNA-Sequencing (RNA-Seq) studies can fuel this drug-prioritization, but their labels, written in plain language, must be annotated manually. Hence, we introduce Signature-based Networks from Automatically Curated Knockout, Knockdown, and Small-molecule Studies (SNACKKSS), which automatically curates gene-disruption and drug-treatment studies from the Gene Expression Omnibus and, in partnership with uniformly computed read count datasets, feeds the labels and RNA-Seq data directly into regulatory relationship predictions. Through cross-validation, we show that SNACKKSS predictions (specifically, from a variation called "SA4") make a unique contribution to finding protein-inhibiting compounds, even alongside existing predictors. We demonstrate the benefit of aggregating multiple predictive tools, and provide this powerful ensemble alongside SNACKKSS. Importantly, we advise researchers to test complex machine learning models on multiple devices, since the hardware architecture can affect their output. Nonetheless, the downstream predictive ability was striking, and our findings support the value of integrating automatically curated RNA-Seq signatures with literature- and co-expression-based predictors for drug-repurposing prioritization.