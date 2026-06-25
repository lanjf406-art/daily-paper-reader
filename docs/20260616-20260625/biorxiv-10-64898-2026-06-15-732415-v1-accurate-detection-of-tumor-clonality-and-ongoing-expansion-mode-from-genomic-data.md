---
title: Accurate detection of tumor clonality and ongoing expansion mode from genomic data
title_zh: 从基因组数据准确检测肿瘤克隆性和持续扩增模式
authors: "Chen, Y., Jaksik, R., Terranova, P., El Baghdadi, S., Koval, A., Kurpas, M. K., Tavare, S., Kimmel, M., Dinh, K. N."
date: 2026-06-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.15.732415v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 检测肿瘤克隆性和扩张模式，与耐药机制相关
tldr: 现有肿瘤内异质性估计算法有限。DECODE方法整合测序覆盖和突变偏差，通过检测位点频率谱中性尾部来推断克隆性和扩增模式。在合成数据上优于现有方法，在急性髓系白血病中给出更简洁克隆分解，在低级别胶质瘤中发现ITH与生存关联。DECODE提供两个互补的预后相关肿瘤进化读数。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有ITH估计算法有限，无法准确检测克隆性和肿瘤扩增模式。
method: DECODE整合样本特异性测序覆盖和突变偏差，通过突变聚类检测SFS中性尾部。
result: 在合成数据上优于现有方法；在AML中给出更简洁克隆分解；在TCGA中揭示低级别胶质瘤ITH与生存关联。
conclusion: DECODE联合推断克隆性和扩增模式，提供互补且预后相关的肿瘤进化读数。
---

## 摘要
最近的证据表明，尽管付出了相当大的努力，目前用于估算肿瘤内异质性（ITH）的算法仍然有限。我们开发了DECODE（从DNA进化解读癌症起源），一种新的突变聚类方法，它整合了样本特异性测序覆盖度和突变调用偏差的影响。在合成数据上，DECODE在多个克隆性指标上优于现有方法，并准确检测和表征了位点频率谱（SFS）中的中性尾部，该尾部编码了肿瘤的持续扩增模式。在急性髓系白血病中，考虑中性尾部使DECODE能够产生更简约的克隆分解，更紧密地匹配驱动复发的已知亚克隆动态。应用于癌症基因组图谱的数据，DECODE不仅在大多数肿瘤类型的样本中检测到中性SFS尾部，还发现了低级别胶质瘤中ITH与生存之间的临床意义关联。通过联合推断克隆性和扩增模式，DECODE从单个肿瘤基因组样本中提供了两种互补且与预后相关的肿瘤进化读数。

## Abstract
Recent evidence shows that despite considerable effort, currently available algorithms for estimating intratumor heterogeneity (ITH) remain limited. We developed DECODE (Deciphering Cancer Origin from DNA Evolution), a novel mutation clustering method that incorporates the impact of sample-specific sequencing coverage and mutation calling biases. On synthetic data, DECODE outperformed existing methods across multiple clonality metrics and accurately detected and characterized the neutral tail in the site frequency spectrum (SFS), which encodes the tumors ongoing expansion mode. In acute myeloid leukemia, accounting for the neutral tail enabled DECODE to yield more parsimonious clonal decompositions that align more closely with known subclonal dynamics that drive relapse. Applied to data from The Cancer Genome Atlas, DECODE not only detected a neutral SFS tail in most samples across tumor types but also uncovered a clinically meaningful link between ITH and survival in low-grade glioma. By jointly inferring clonality and expansion mode, DECODE provides two complementary and prognostically relevant readouts of tumor evolution from single tumor genomic samples.