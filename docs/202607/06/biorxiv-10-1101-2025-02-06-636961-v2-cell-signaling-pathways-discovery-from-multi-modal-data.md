---
title: Cell signaling pathways discovery from multi-modal data
title_zh: 从多模态数据发现细胞信号通路
authors: "He, C., Simpson, C., Cossentino, I., Zhang, B., Tkachev, S., Eddins, D. J., Kosters, A., Yang, J., Sheth, S., Levy, T., Possemato, A., Huang, L., Tabatsky, E., Lee, S. H., Ghosh, D., George, A., Gregoretti, I., Ariss, M., Dandekar, D., Ausekar, A., Roan, N. R., Ghosn, E. E. B., Colonna, M., Rikova, K., Nie, Q., Orlova, D."
date: 2026-07-06
pdf: "https://www.biorxiv.org/content/10.1101/2025.02.06.636961v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 多模态数据整合发现信号通路，可应用于耐药机制研究
tldr: 细胞信号通路解析对理解疾病机制和药物开发至关重要，但多模态数据高维异构且现有工具局限。本文提出Incytr方法，整合转录组、ATAC-seq、蛋白质组、磷酸化组和激酶组数据，高效发现信号通路。在COVID-19、阿尔茨海默病和癌症中验证，成功恢复已知通路并生成细胞类型特异性新假设，结合药物数据库支持靶点发现。进一步用Incytr通路训练NLP模型，深化细胞通讯理解，助力新治疗靶点识别。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有计算工具难以从高维异构的多组学数据中有效推断细胞信号通路。
method: 提出Incytr方法，整合转录组、ATAC-seq、蛋白质组、磷酸化组和激酶组等多模态数据推断信号通路。
result: 在COVID-19、阿尔茨海默病和癌症中恢复已知通路，生成细胞类型特异性新假设，并支持药物靶点发现。
conclusion: Incytr整合多模态数据发现通路，结合数据库可支持靶点发现，且作为NLP训练数据可深化细胞通讯理解。
---

## 摘要
破译细胞信号通路是理解生物学、疾病机制以及开发新疗法的关键。尽管多组学技术的进步为信号传导提供了更丰富的见解，但数据仍然呈高维、异质性且难以解读，当前用于推断信号通路的计算工具也十分有限。为解决这一问题，我们开发了Incytr，一种通过整合多种数据模态（包括转录组学、ATAC-seq、蛋白质组学、磷酸化蛋白质组学和激酶组学）来高效发现细胞信号通路的方法。我们在COVID-19、阿尔茨海默病和癌症中展示了其应用，该方法成功恢复了已知通路，并生成了由多种数据类型支持的新型细胞类型特异性假设。我们进一步展示了如何将Incytr推导的通路与生物标志物和药物数据库相结合，以支持靶点发现和药物研发。最后，我们表明，将Incytr推导的信号通路作为简单自然语言处理模型的训练数据，可以加深我们对细胞间通讯和免疫细胞动力学的理解，同时帮助识别新的治疗靶点。

## Abstract
Deciphering cell signaling pathways is key to understanding biology, disease mechanisms, and developing new therapies. Although advances in multi-omics technologies provide richer insight into signaling, the data remain high-dimensional, heterogeneous, and difficult to interpret, and current computational tools for inferring signaling pathways are limited. To address this, we developed Incytr, a method for efficient discovery of cell signaling pathways through integration of diverse data modalities, including transcriptomics, ATAC-seq, proteomics, phosphoproteomics, and kinomics. We demonstrate its application in COVID-19, Alzheimer's disease, and cancer, where it successfully recovers known pathways and generates novel, cell-type-specific hypotheses supported by multiple data types. We further show how integrating Incytr-derived pathways with biomarker and drug databases can support target and drug discovery. Finally, we show that using Incytr-derived signaling pathways as training data for simple natural language processing models can deepen our understanding of cell-cell communication and immune cell dynamics, while helping identify new therapeutic targets.