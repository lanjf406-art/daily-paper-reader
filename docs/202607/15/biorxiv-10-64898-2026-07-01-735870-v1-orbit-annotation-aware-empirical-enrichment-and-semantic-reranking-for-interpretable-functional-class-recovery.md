---
title: "ORBIT: Annotation-Aware Empirical Enrichment and Semantic Reranking for Interpretable Functional-Class Recovery"
title_zh: ORBIT：面向可解释功能类别恢复的注释感知经验富集与语义重排序
authors: "Kidder, B. L."
date: 2026-07-07
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.01.735870v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: ORBIT基因集富集工具可用于耐药转录组分析
tldr: 标准基因集富集工具输出冗长冗余结果表，需人工整合。ORBIT提出注释感知工作流，结合经验富集、语义重排序和冗余感知代表项选择，优先排序解释性功能摘要。在45个核心基准测试中，ORBIT的期望类别恢复率（平均倒数排名0.916，top-1恢复0.889）优于Enrichr和PANTHER。通过GPCR和多项转录组案例验证，ORBIT将冗余富集项压缩为结构化语义邻域，并链接基因、细胞类型和注释类，实现从排名项到可审查生物学摘要的转化。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1145, \"height\": 735, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1333, \"height\": 601, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1212, \"height\": 714, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1244, \"height\": 1628, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1182, \"height\": 740, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1558, \"height\": 2195, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1572, \"height\": 2560, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1869, \"height\": 1561, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 768, \"height\": 675, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 813, \"height\": 669, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 987, \"height\": 736, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-01-735870-v1/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 757, \"height\": 640, \"label\": \"Figure\"}]"
motivation: 现有富集工具输出冗余结果，需要大量手动整理，缺乏自动化解释方法。
method: 结合经验富集、语义重排序和冗余感知代表项选择，优先排序功能摘要。
result: 在45个核心基准测试中，ORBIT平均倒数排名0.916，top-1恢复0.889，优于Enrichr和PANTHER。
conclusion: ORBIT将冗余富集结果压缩为结构化生物学摘要，保留从输入基因到功能摘要的证据链。
---

## 摘要
基因集解读工作流被广泛用于总结转录组和蛋白质组实验，然而标准富集工具通常会返回冗长且存在冗余的结果表，需要大量手动整合。我们开发了ORBIT（本体排序生物学解读工具），这是一种注释感知的解读工作流，结合了经验富集、语义重排序和冗余感知的代表性术语选择，以从基因集中优先提取可解释的功能摘要。

我们在一个经过精心构建的分层基准上评估了ORBIT，该基准包含人类功能类别基因集，涵盖纯净参考集、大小阶梯变体和混合难度案例。在45个基因集的核心基准测试中，ORBIT语义方法在预期类别恢复方面优于Enrichr和PANTHER基因本体分子功能基线，平均倒数排名为0.916，前1恢复率为0.889。自助法置信区间和配对置换检验支持了这一优势的稳健性，补充分析还将比较扩展到了g:Profiler。在一个GPCR混合功能案例研究中，ORBIT将冗余富集术语压缩为语义代表性邻域，展示了如何将冗长的富集输出转化为可审查的生物学摘要。

我们将ORBIT应用于互补的转录组分析，涵盖单细胞免疫细胞标记、干扰素-β刺激和乳腺癌亚型生物学。在这些场景中，ORBIT将标记和差异表达特征压缩为优先排序的功能摘要，并明确链接到支持每个结果的基因、细胞类型和注释类别。这些应用共同展示了ORBIT如何从排序的富集术语转向结构化的生物学解读，并保留从输入基因到功能摘要的证据链。

## Abstract
Gene-set interpretation workflows are widely used to summarize transcriptomic and proteomic experiments, yet standard enrichment tools often return long, redundant result tables that require substantial manual consolidation. We developed ORBIT (Ontology-Ranked Biological Interpretation Tool), an annotation-aware interpretation workflow that combines empirical enrichment, semantic reranking, and redundancy-aware representative-term selection to prioritize interpretable functional summaries from gene sets.

We evaluated ORBIT on a curated tiered benchmark of human functional-class gene sets spanning clean reference sets, size-ladder variants, and mixed-difficulty cases. On the 45-set core benchmark, ORBIT semantic achieved higher expected-class recovery than Enrichr and PANTHER Gene Ontology molecular-function baselines, with a mean reciprocal rank of 0.916 and top-1 recovery of 0.889. Bootstrap confidence intervals and paired permutation testing supported the robustness of this advantage, and supplemental analyses extended the comparison to g:Profiler. In a GPCR mixed-function case study, ORBIT compressed redundant enriched terms into semantic representative neighborhoods, illustrating how long enrichment outputs can be converted into reviewable biological summaries.

We applied ORBIT across complementary transcriptomic analyses spanning single-cell immune-cell markers, interferon-beta stimulation, and breast-cancer subtype biology. In these settings, ORBIT condensed marker and differential-expression signatures into prioritized functional summaries with explicit links to the genes, cell types, and annotation classes supporting each result. Together, these applications show how ORBIT can move from ranked enrichment terms to structured biological interpretation, preserving the evidence trail from input genes to functional summaries.