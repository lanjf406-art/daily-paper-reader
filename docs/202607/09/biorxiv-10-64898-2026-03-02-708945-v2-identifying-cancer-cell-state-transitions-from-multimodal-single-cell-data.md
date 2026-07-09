---
title: Identifying cancer cell-state transitions from multimodal single-cell data
title_zh: 从多模态单细胞数据中识别癌细胞状态转变
authors: "Baselli, G. A., Alekseenko, A., Liano-Pons, J., Sinanis, L., Rrapaj, E., Arsenian-Henriksson, M., Pelechano, V."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.02.708945v2.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 捕获表型可塑性的单细胞框架与治疗逃逸
tldr: 癌细胞表型可塑性导致治疗抵抗，但其瞬时状态转换难以直接捕获。本文提出一种单细胞框架，利用mRNA与蛋白积累的时间延迟，在多模态数据中识别不一致的转录-蛋白水平作为转换标志。在K562白血病模型中，该框架定位转换细胞并导出与细胞周期和线粒体相关的可塑性特征。全基因组CRISPR筛选验证了BCR-ABL1和线粒体稳态基因等关键调控因子。该框架衍生出可塑性评分，预测CML药物反应、分层AML预后并在31种癌症中具预后价值，同时空间转录组学揭示实体瘤中可塑性热点。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-02-708945-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1714, \"height\": 1982, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-02-708945-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1775, \"height\": 2509, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-02-708945-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1744, \"height\": 2380, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-02-708945-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1743, \"height\": 2207, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-03-02-708945-v2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1639, \"height\": 1932, \"label\": \"Figure\"}]"
motivation: 癌细胞状态转换的瞬时性使得其分子驱动因素难以通过常规方法解析。
method: 利用多模态单细胞数据中mRNA与蛋白积累的时间延迟，检测不一致的转录-蛋白水平以捕获转换细胞。
result: 在K562等模型中识别转换细胞，导出可塑性特征评分，预测药物反应、分层预后，并在多种肿瘤中验证。
conclusion: 该框架揭示了癌症可塑性的分子基础，并提供了跨肿瘤的量化工具。
---

## 摘要
表型可塑性使癌细胞能够逃逸治疗，然而状态转变的瞬态特性使其分子驱动因素难以确定。在此，我们提出一个单细胞框架，利用mRNA和蛋白质积累之间的时间延迟，直接捕获经历表型转换的细胞。我们证明，在多模态单细胞数据中，转录本与蛋白质积累之间的分化相关延迟可作为mRNA与表面蛋白水平的不一致被检测到。将此策略应用于在分化的CD24-与祖细胞样CD24+状态之间切换的K562白血病模型，我们识别出转变中的细胞，并推导出一个将细胞周期进程和线粒体重塑与可塑性联系起来的转录特征。全基因组CRISPR筛选确认了可塑性的关键调控因子，包括BCR-ABL1和线粒体稳态基因。我们将转变相关程序总结为一个评分，该评分可预测慢性髓系白血病对伊马替尼的反应，对急性髓系白血病的生存进行分层，并在31种TCGA肿瘤类型中保持预后价值。空间转录组学揭示了实体肿瘤中的局部可塑性热点。总之，该框架揭示了癌症可塑性的分子基础，并使其能够在不同肿瘤中进行量化。

## Abstract
Phenotypic plasticity allows cancer cells to evade therapy, yet the transient nature of state transitions has made their molecular drivers difficult to define. Here, we present a single-cell framework that leverages the temporal delays between mRNA and protein accumulation to directly capture cells undergoing phenotypic switching. We show that differentiation-associated delays between transcript and protein accumulation are detectable in multimodal single-cell data as discordant mRNA and surface-protein levels. Applying this strategy to the K562 leukemia model, which alternates between differentiated CD24- and progenitor-like CD24+ states, we identify transitioning cells and derive a transcriptional signature linking cell-cycle progression and mitochondrial remodeling to plasticity. Genome-wide CRISPR screening confirms key regulators of plasticity, including BCR-ABL1 and mitochondrial homeostasis genes. We summarize the transition-associated program into a score that predicts imatinib response in chronic myeloid leukemia, stratifies survival in acute myeloid leukemia, and retains prognostic value across 31 TCGA tumor types. Spatial transcriptomics reveals localized plasticity hotspots in solid tumors. Together, this framework exposes the molecular basis of cancer plasticity and enables its quantification across tumors.