---
title: Transcriptomic data and biomedical literature synergize in finding pharmacologic gene regulators
title_zh: 转录组数据与生物医学文献协同发现药理基因调控因子
authors: "Deisseroth, C. A., Brazelton, B., Shaik, Z., Sandberg, B. S., Liu, Z., Zoghbi, H. Y."
date: 2026-07-15
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.13.708862v3.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 利用转录组数据的生物信息学方法优先排序药物靶点，可应用于耐药研究
tldr: 许多单基因疾病缺乏靶向疗法。为加速药物发现，SNACKKSS自动从GEO中整理基因敲除/敲低和药物处理的RNA-Seq数据，与统一计算的读数结合，直接预测调控关系。交叉验证显示其变体SA4在寻找蛋白质抑制剂方面独特贡献，且集成多个预测工具更优。研究支持自动RNA-Seq特征与文献、共表达预测结合用于药物重定位。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1963, \"height\": 990, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1405, \"height\": 1384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1971, \"height\": 1983, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1949, \"height\": 991, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1704, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1709, \"height\": 669, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1973, \"height\": 563, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-03-13-708862-v3/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1897, \"height\": 887, \"label\": \"Table\"}]"
motivation: 现有方法需手动注释RNA-Seq研究标签，效率低且难以规模化，限制了药物重定位的应用。
method: SNACKKSS自动提取基因表达综合数据库（GEO）中的基因扰动和药物处理研究，与统一计算的read count数据集结合，直接预测基因调控关系。
result: 交叉验证表明，SA4变体在发现蛋白质抑制化合物方面有独特贡献；集成多个预测工具可提升性能，但硬件架构会影响复杂模型的输出。
conclusion: 自动化整理的RNA-Seq签名与基于文献和共表达的预测因子整合，显著增强了药物重定位优先排序的可靠性。
---

## 摘要
大多数由单个基因产物缺乏或过量引起的疾病缺乏靶向治疗。由于这些疾病可以通过基因过表达、敲除或敲低来建模，因此能够对抗此类扰动转录组效应的药物可能是有前途的治疗候选药物。RNA测序（RNA-Seq）研究可以推动这种药物优先排序，但其以通俗语言编写的标签需要手动注释。因此，我们引入了基于自动策展的敲除、敲低和小分子研究的签名网络（SNACKKSS），该网络自动从基因表达综合数据库中策展基因干扰和药物治疗研究，并与统一计算的读数计数数据集合作，将标签和RNA-Seq数据直接输入调控关系预测。通过交叉验证，我们表明SNACKKSS的预测（特别是来自称为“SA4”的变体）在寻找蛋白质抑制化合物方面做出了独特贡献，即使是与现有预测因子一起使用。我们展示了聚合多种预测工具的好处，并提供了这个强大的集成模型以及SNACKKSS。重要的是，我们建议研究者在多种设备上测试复杂的机器学习模型，因为硬件架构可能影响其输出。尽管如此，下游预测能力是显著的，我们的发现支持了将自动策展的RNA-Seq签名与基于文献和共表达的预测因子整合用于药物重定位优先排序的价值。

## Abstract
Most disorders caused by a deficiency or excess of one gene product lack targeted therapies. Since these disorders can be modeled with a gene overexpression, knockout, or knockdown, drugs that oppose the transcriptomic effects of such perturbations may be promising therapeutic candidates. RNA-Sequencing (RNA-Seq) studies can fuel this drug-prioritization, but their labels, written in plain language, must be annotated manually. Hence, we introduce Signature-based Networks from Automatically Curated Knockout, Knockdown, and Small-molecule Studies (SNACKKSS), which automatically curates gene-disruption and drug-treatment studies from the Gene Expression Omnibus and, in partnership with uniformly computed read count datasets, feeds the labels and RNA-Seq data directly into regulatory relationship predictions. Through cross-validation, we show that SNACKKSS' predictions (specifically, from a variation called "SA4") make a unique contribution to finding protein-inhibiting compounds, even alongside existing predictors. We demonstrate the benefit of aggregating multiple predictive tools, and provide this powerful ensemble alongside SNACKKSS. Importantly, we advise researchers to test complex machine learning models on multiple devices, since the hardware architecture can affect their output. Nonetheless, the downstream predictive ability was striking, and our findings support the value of integrating automatically curated RNA-Seq signatures with literature- and co-expression-based predictors for drug-repurposing prioritization.