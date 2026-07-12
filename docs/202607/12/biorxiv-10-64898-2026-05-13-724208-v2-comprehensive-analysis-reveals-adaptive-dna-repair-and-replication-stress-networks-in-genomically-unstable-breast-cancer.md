---
title: Comprehensive Analysis Reveals Adaptive DNA Repair and Replication Stress Networks in Genomically Unstable Breast Cancer
title_zh: 综合分析揭示基因组不稳定乳腺癌中的适应性DNA修复和复制胁迫网络
authors: "Ramadan, F., Zahraeifard, S., Yadav, N., Subedi, U., Shah, S., Panday, A."
date: 2026-07-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.13.724208v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 生物信息学分析DNA修复在耐药中的作用
tldr: 乳腺癌基因组不稳定性是重要特征，但肿瘤如何耐受持续DNA损伤机制不明。该研究通过多队列分析，利用基因组片段改变评估不稳定性，发现BRCA突变肿瘤中DNA损伤应答与复制胁迫耐受通路异常激活，且活性与基因组改变增加正相关，提示损伤耐受而非修复恢复。复制胁迫耐受程序（如叉重塑、保护）也增强肿瘤适应性。这些适应性状态在侵袭性亚型中富集，并随疾病进展而加剧，同时与通路特异性突变负荷相关。共现与互斥分析揭示驱动基因与DDR基因的非随机遗传相互作用，为合成致死治疗提供新靶点。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 4605, \"height\": 2358, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1923, \"height\": 2289, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1903, \"height\": 1408, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 4640, \"height\": 2484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 4680, \"height\": 2488, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 2198, \"height\": 2403, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-13-724208-v2/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 4072, \"height\": 1666, \"label\": \"Figure\"}]"
motivation: 基因组不稳定性是乳腺癌标志，但肿瘤如何适应性耐受DNA损伤以实现生存的机制尚不清晰。
method: 采用多队列分析，以基因组片段改变（FGA）为指标，系统评估BRCA突变肿瘤中DNA损伤应答与复制胁迫耐受通路的表达和遗传相互作用。
result: BRCA突变肿瘤中DDR和RST通路活性升高且与FGA正相关，适应性状态在侵袭性亚型中富集，并发现驱动基因与DDR基因的非随机遗传相互作用。
conclusion: 揭示基因组维护程序代偿性激活驱动肿瘤韧性，并提出针对合成致死脆弱性的治疗策略。
---

## 摘要
基因组不稳定性是乳腺癌的一个标志性特征，然而肿瘤如何耐受持续DNA损伤的机制仍知之甚少。我们对乳腺癌数据集进行了全面的多队列分析，以界定基因组不稳定肿瘤中DNA损伤应答（DDR）和复制胁迫耐受（RST）网络如何被重新编程。使用基因组改变分数（FGA）作为染色体不稳定性指标，我们显示BRCA突变肿瘤表现出升高的基因组不稳定性，同时伴随同源重组、范可尼贫血、错配修复、碱基切除修复和替代末端连接通路的表达增加。引人注目的是，升高的通路活性与增加的基因组改变相关，支持一种损伤耐受而非修复恢复的模型。RST程序，包括叉重塑、保护和单链DNA间隙抑制，进一步促进了在复制胁迫下的肿瘤适应性。这些适应性状态在侵袭性亚型中富集，随着进展而加剧，并与通路特异性突变负荷相关。共现和互斥映射揭示了主要驱动基因和DDR基因之间的非随机亚型相关遗传相互作用状态，提出了情境依赖的合成致死机会。我们的发现确定了补偿性基因组维持程序是肿瘤恢复力的核心驱动因素，并强调了用于靶向治疗干预的通路特异性脆弱性。

## Abstract
Genomic instability is a defining hallmark of breast cancer, yet the mechanisms by which tumors tolerate persistent DNA damage remain poorly understood. We performed a comprehensive, multi-cohort analysis of breast cancer datasets to define how DNA damage response (DDR) and replication stress tolerance (RST) networks are rewired in genomically unstable tumors. Using fraction of genome altered (FGA) as a chromosomal instability metric, we show that BRCA-mutant tumors exhibit elevated genomic instability coupled with increased expression of homologous recombination, Fanconi anemia, mismatch repair, base excision repair, and alternative end-joining pathways. Strikingly, heightened pathway activity correlates with increased genome alteration, supporting a model of damage tolerance rather than repair restoration. RST programs, including fork remodeling, protection, and single strand DNA gap suppression, further contribute to tumor fitness under replication stress. These adaptive states are enriched in aggressive subtypes, intensified with progression, and associate with pathway-specific mutational burden. Co-occurrence and mutual exclusivity mapping uncovered non-random subtype-relevant genetic interactions states among major drivers and DDR genes, nominating context-specific synthetic lethal opportunities. Our findings identify compensatory genome-maintenance programs as central drivers of tumor resilience and highlight pathway-specific vulnerabilities for targeted therapeutic intervention.