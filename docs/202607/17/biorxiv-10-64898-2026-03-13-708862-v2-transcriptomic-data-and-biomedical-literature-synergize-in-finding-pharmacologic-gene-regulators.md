---
title: Transcriptomic data and biomedical literature synergize in finding pharmacologic gene regulators
title_zh: 转录组数据与生物医学文献协同寻找药理基因调控因子
authors: "Deisseroth, C. A., Brazelton, B., Shaik, Z., Sandberg, B. S., Liu, Z., Zoghbi, H. Y."
date: 2026-07-15
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.13.708862v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 整合转录组数据用于药物靶标发现，可应用于耐药研究
tldr: 大多数单基因疾病缺乏靶向治疗，药物可对抗基因扰动导致的转录组变化。现有RNA-Seq研究标签需手动注释，为此提出SNACKKSS框架，自动筛选GEO中的基因干扰和药物处理研究，与统一计算的读取计数结合，直接进行调控关系预测。交叉验证显示其SA4变体在发现蛋白抑制化合物方面有独特贡献。将自动筛选的转录组特征与基于文献和共表达的预测因子集成，可提升药物重定位优先排序效果；同时提醒复杂模型输出受硬件架构影响。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1963, \"height\": 990, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1352, \"height\": 1333, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1971, \"height\": 1983, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1949, \"height\": 991, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1704, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1709, \"height\": 669, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1973, \"height\": 563, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v2/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1897, \"height\": 887, \"label\": \"Table\"}]"
motivation: 自动从GEO中筛选基因干扰和药物处理研究，结合转录组数据预测药物基因调控关系，以避免手动注释瓶颈。
method: 构建SNACKKSS框架，自动筛选GEO研究并计算读取计数，通过调控关系预测模型（如SA4变体）识别潜在药物；集成现有预测工具形成更优组合。
result: SNACKKSS的SA4变体在交叉验证中显著提升蛋白抑制化合物识别能力，多个预测工具集成效果优于单一模型。
conclusion: 自动筛选的RNA-Seq特征与基于文献和共表达的预测因子协同，显著增强药物重定位优先排序；同时需关注硬件架构对复杂模型输出的影响。
---

## 摘要
大多数由单个基因产物缺乏或过量引起的疾病缺乏靶向疗法。由于这些疾病可以通过基因过表达、敲除或敲低来建模，因此能够对抗此类扰动转录组效应的药物可能是有前景的治疗候选药物。RNA测序（RNA-Seq）研究可以促进这种药物优先级排序，但其以纯文本编写的标签必须手动注释。因此，我们引入了基于自动策展敲除、敲低和小分子研究的签名网络（SNACKKSS），该网络自动从基因表达综合数据库中策展基因干扰和药物治疗研究，并与统一计算的读取计数数据集合作，将标签和RNA-Seq数据直接输入调控关系预测中。通过交叉验证，我们表明SNACKKSS的预测（特别是来自一种称为“SA4”的变体）在寻找蛋白质抑制化合物方面做出了独特贡献，即使与现有预测因子一起使用也是如此。我们展示了聚合多种预测工具的好处，并提供了这个强大的集成模型以及SNACKKSS。重要的是，我们建议研究人员在多个设备上测试复杂的机器学习模型，因为硬件架构可能会影响其输出。尽管如此，下游预测能力令人瞩目，我们的研究结果支持将自动策展的RNA-Seq签名与基于文献和共表达的预测因子整合用于药物重定位优先级排序的价值。

## Abstract
Most disorders caused by a deficiency or excess of one gene product lack targeted therapies. Since these disorders can be modeled with a gene overexpression, knockout, or knockdown, drugs that oppose the transcriptomic effects of such perturbations may be promising therapeutic candidates. RNA-Sequencing (RNA-Seq) studies can fuel this drug-prioritization, but their labels, written in plain language, must be annotated manually. Hence, we introduce Signature-based Networks from Automatically Curated Knockout, Knockdown, and Small-molecule Studies (SNACKKSS), which automatically curates gene-disruption and drug-treatment studies from the Gene Expression Omnibus and, in partnership with uniformly computed read count datasets, feeds the labels and RNA-Seq data directly into regulatory relationship predictions. Through cross-validation, we show that SNACKKSS' predictions (specifically, from a variation called "SA4") make a unique contribution to finding protein-inhibiting compounds, even alongside existing predictors. We demonstrate the benefit of aggregating multiple predictive tools, and provide this powerful ensemble alongside SNACKKSS. Importantly, we advise researchers to test complex machine learning models on multiple devices, since the hardware architecture can affect their output. Nonetheless, the downstream predictive ability was striking, and our findings support the value of integrating automatically curated RNA-Seq signatures with literature- and co-expression-based predictors for drug-repurposing prioritization.