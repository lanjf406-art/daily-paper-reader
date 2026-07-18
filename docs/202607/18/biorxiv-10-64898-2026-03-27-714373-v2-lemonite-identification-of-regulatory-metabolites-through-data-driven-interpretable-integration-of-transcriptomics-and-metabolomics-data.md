---
title: "Lemonite: identification of regulatory metabolites through data-driven, interpretable integration of transcriptomics and metabolomics data"
title_zh: Lemonite：通过数据驱动、可解释的转录组学和代谢组学数据整合鉴定调控代谢物
authors: "Vandemoortele, B., Devlies, H., Michoel, T., Vanhaecke, L., Vandenbroucke, R. E., Laukens, D., Vermeirssen, V."
date: 2026-07-15
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.27.714373v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 数据驱动的转录组与代谢组整合方法用于调控代谢物鉴定
tldr: 现有整合转录组和代谢组的方法受限于可解释性差或先验知识不完整，难以系统性发现调控代谢物。Lemonite提出一种数据驱动且可解释的框架，通过扩展模块网络推断，联合转录因子和代谢物关联基因程序，并构建大规模知识图谱。在胶质母细胞瘤和炎症性肠病队列中，它识别了超过50个功能一致的基因模块，揭示了已知和新的代谢物-基因调控关系，例如肌醇和磷脂酰胆碱调控免疫程序。该工作为探索代谢组调控潜力、生成可实验验证假说提供了原则性方法。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-27-714373-v2/fig-001.webp\", \"caption\": \"\", \"page\": 13, \"index\": 1, \"width\": 1222, \"height\": 1798}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-27-714373-v2/fig-002.webp\", \"caption\": \"\", \"page\": 16, \"index\": 2, \"width\": 1293, \"height\": 1502}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-27-714373-v2/fig-003.webp\", \"caption\": \"\", \"page\": 22, \"index\": 3, \"width\": 1278, \"height\": 1798}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-27-714373-v2/fig-004.webp\", \"caption\": \"\", \"page\": 27, \"index\": 4, \"width\": 1274, \"height\": 1797}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-27-714373-v2/fig-005.webp\", \"caption\": \"\", \"page\": 30, \"index\": 5, \"width\": 1298, \"height\": 1467}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-27-714373-v2/fig-006.webp\", \"caption\": \"\", \"page\": 37, \"index\": 6, \"width\": 1285, \"height\": 1797}]"
motivation: 克服现有方法可解释性差或依赖不完整先验知识的局限，实现从多组学数据中系统识别调控代谢物。
method: Lemonite扩展模块网络推断，联合关联转录因子和代谢物与基因程序，并整合37万代谢物-基因/蛋白和210万蛋白互作知识图谱。
result: 在胶质母细胞瘤和炎症性肠病中识别超50个基因模块，发现肌醇、磷脂酰胆碱等调控免疫程序的已知和新关系，并经体外实验验证。
conclusion: 提供了一个数据驱动、可解释的框架，用于探索代谢组全基因组调控潜力，生成可测试的生物学假说。
---

## 摘要
目前的转录组-代谢组整合方法要么可解释性差，要么受限于不完整的先验知识，阻碍了调控代谢物的系统性鉴定。本文提出Lemonite，一个数据驱动且可解释的框架，用于整合批量转录组和代谢组数据，以发现作用于基因模块的调控代谢物。Lemonite扩展了模块网络推理，将转录因子和代谢物与基因程序联合关联，无需先验差异分析或完整的代谢物组注释。为了将预测置于上下文中，我们构建了一个全面的基因/蛋白质-代谢物知识图谱，整合了超过37万条代谢物-基因/蛋白质相互作用和210万条蛋白质-蛋白质相互作用。将该方法应用于胶质母细胞瘤（n=99）和炎症性肠病（n=75）队列，Lemonite在每个疾病中鉴定出超过50个功能连贯的基因模块，揭示了已知和之前未表征的代谢物-基因调控关系。在胶质母细胞瘤中，肌醇和磷脂酰胆碱与IRF6共同调控间充质样免疫程序，这些程序在整合单细胞转录组后主要表达于肿瘤相关巨噬细胞和单核细胞中。在炎症性肠病中，优先考虑了那些在体外改变结肠上皮细胞中预测靶基因表达的调控代谢物。总体而言，Lemonite提供了一个原则性框架，用于探索代谢物组的全基因组调控潜力，并从多组学数据生成生物学可解释、实验可检验的假设。

## Abstract
Current transcriptomics-metabolomics integration approaches are either limited by poor interpretability or constrained by incomplete prior knowledge, preventing the systematic identification of regulatory metabolites. Here, we present Lemonite, a data-driven and interpretable framework for integrating bulk transcriptomics and metabolomics data to uncover regulatory metabolites acting on gene modules. Lemonite extends module network inference to jointly associate transcription factors and metabolites with gene programs, without requiring prior differential analysis or complete metabolome annotation. To contextualize predictions, we constructed a comprehensive gene/protein-metabolite knowledge graph integrating over 370 000 metabolite-gene/protein and 2.1 million protein-protein interactions. Applied to glioblastoma (n=99) and inflammatory bowel disease (n=75) cohorts, Lemonite identified over 50 functionally coherent gene modules per disease, revealing established and previously uncharacterized metabolite-gene regulatory relationships. In glioblastoma, myo-inositol and phosphatidylcholines, together with IRF6, regulate mesenchymal-like immune programs, which upon integration with single-cell transcriptomics are primarily expressed in tumor-associated macrophages and monocytes. In inflammatory bowel disease, regulatory metabolites were prioritized that change the expression of their predicted target genes in colonic epithelial cells in vitro. Overall, Lemonite provides a principled framework to explore the genome-wide regulatory potential of the metabolome and to generate biologically interpretable, experimentally testable hypotheses from multi-omics data.