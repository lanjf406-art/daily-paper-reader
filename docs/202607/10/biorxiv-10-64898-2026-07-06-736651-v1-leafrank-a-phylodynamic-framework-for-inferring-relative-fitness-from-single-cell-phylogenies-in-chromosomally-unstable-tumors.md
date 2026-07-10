---
title: "LeafRank: A phylodynamic framework for inferring relative fitness from single-cell phylogenies in chromosomally unstable tumors"
title_zh: LeafRank：一种从染色体不稳定肿瘤的单细胞系统发育推断相对适应度的系统动力学框架
authors: "Wu, C., Leder, K., Wang, Z., Sun, R."
date: 2026-07-09
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.06.736651v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 单细胞系统发育推断相对适应度，可用于耐药进化研究
tldr: 染色体不稳定肿瘤中细胞适应度异质性难以量化。LeafRank利用单细胞DNA-seq系统发育树，通过多类型分支过程模型整合拓扑结构与分支长度，估计细胞相对适应度。模拟和卵巢癌数据分析显示其高准确性，并揭示WGD肿瘤中定向和并行选择，以及高适应度谱系中富集的重复拷贝数事件。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1594, \"height\": 1401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1581, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1569, \"height\": 1801, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1249, \"height\": 1920, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1661, \"height\": 1115, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1661, \"height\": 1359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1642, \"height\": 898, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736651-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1585, \"height\": 470, \"label\": \"Table\"}]"
motivation: 现有方法难以量化染色体不稳定肿瘤中单个细胞的相对适应度，尤其在全基因组加倍后。
method: 基于多类型分支过程模型，整合系统发育树全拓扑与分支长度，并引入WGD后树缩放策略调整基因组不稳定性差异。
result: 模拟和卵巢癌数据验证高精度，发现WGD谱系无直接生长优势，但通过后续改变获得适应度。
conclusion: LeafRank提供了一个灵活、准确的框架，用于从单细胞系统发育推断肿瘤细胞适应度异质性。
---

## 摘要
肿瘤包含具有不同生长潜力的癌细胞，这些潜力塑造了进化轨迹，然而在全基因组复制（WGD）和染色体不稳定性情况下，这种适应性多样性仍难以量化。我们提出了LeafRank，一个利用单细胞DNA-seq系统发育推断单个细胞相对适应度的数学框架。使用多类型分支过程模型，LeafRank整合了完整的树拓扑结构，包括分支长度和分叉模式，以估计在罕见驱动事件驱动的点断进化模式下的边际适应度概率。为了解释WGD后升高的畸变率，我们引入了一种树重缩放策略，调整谱系特异性基因组不稳定性。与专注于预定义亚克隆的方法不同，LeafRank对所有采样细胞进行排序，实现了对生长异质性的灵活评估。模拟实验表明，该方法在空间和非空间虚拟肿瘤中均具有高准确性。应用于卵巢癌时，LeafRank揭示了WGD肿瘤中的定向选择和并行选择，并识别出在高适应性谱系中富集的重复拷贝数事件。WGD谱系并未立即显示出生长优势，而是通过后续改变获得适应性。

## Abstract
Tumors contain cancer cells with diverse growth potentials that shape evolutionary trajectories, yet this fitness diversity remains difficult to quantify in cases of whole-genome duplication (WGD) and chromosomal instability. We present LeafRank, a mathematical framework that leverages single-cell DNA-seq phylogenies to infer the relative fitness of individual cells. Using a multi-type branching process model, LeafRank integrates full tree topology, including branch lengths and bifurcation patterns, to estimate marginal fitness probabilities under punctuated evolutionary regimes driven by rare driver events. To account for elevated aberration rates following WGD, we introduce a tree-rescaling strategy that adjusts for lineage-specific genomic instability. Unlike methods focused on predefined subclones, LeafRank ranks all sampled cells, enabling flexible assessment of growth heterogeneity. Simulations demonstrate high accuracy across spatial and non-spatial virtual tumors. Applied to ovarian cancer, LeafRank reveals directional and parallel selection in WGD tumors and identifies recurrent copy number events enriched in high-fitness lineages. WGD lineages do not show immediate growth advantages but acquire fitness through subsequent alterations.