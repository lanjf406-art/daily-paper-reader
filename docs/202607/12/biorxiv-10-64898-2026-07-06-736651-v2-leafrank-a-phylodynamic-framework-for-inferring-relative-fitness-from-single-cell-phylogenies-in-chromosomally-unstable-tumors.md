---
title: "LeafRank: A phylodynamic framework for inferring relative fitness from single-cell phylogenies in chromosomally unstable tumors"
title_zh: "LeafRank: 一种从染色体不稳定肿瘤的单细胞系统发育推断相对适应度的系统动力学框架"
authors: "Wu, C., Leder, K., Wang, Z., Sun, R."
date: 2026-07-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.06.736651v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 利用单细胞系统发育推断染色体不稳定肿瘤的适应性
tldr: 染色体不稳定肿瘤中癌细胞生长潜能的异质性难以量化。LeafRank基于单细胞DNA-seq系统发育树，通过多类型分支过程模型整合树拓扑与分支长度，估计细胞相对适应度，并针对全基因组复制后高畸变率采用树重缩放调整谱系特异性不稳定性。模拟实验在虚拟肿瘤中取得高精度。在卵巢癌应用中，LeafRank揭示全基因组复制谱系不具即时生长优势，而是通过后续拷贝数改变获得高适应度，并识别出定向与平行选择信号。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1594, \"height\": 1401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1581, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1569, \"height\": 1801, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1249, \"height\": 1921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1661, \"height\": 1115, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1661, \"height\": 1359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1642, \"height\": 898, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736651-v2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1585, \"height\": 470, \"label\": \"Table\"}]"
motivation: 现有方法难以量化全基因组复制和染色体不稳定肿瘤中单个细胞的适应度差异，需更精细的推断手段。
method: 基于多类型分支过程模型，整合系统发育树拓扑与分支长度，并采用树重缩放策略校正谱系特异性基因组不稳定性。
result: 模拟显示高精度；卵巢癌分析中识别出高适应度谱系富集的拷贝数事件，揭示全基因组复制后通过后续改变获得优势。
conclusion: LeafRank可有效评估肿瘤生长异质性，为理解染色体不稳定肿瘤的进化动力学提供新工具。
---

## 摘要
肿瘤包含具有不同生长潜力的癌细胞，这些潜力塑造了进化轨迹，然而在全基因组复制(WGD)和染色体不稳定的情况下，这种适应度多样性仍难以量化。我们提出LeafRank，一个利用单细胞DNA-seq系统发育树推断单个细胞相对适应度的数学框架。使用多类型分支过程模型，LeafRank整合完整的树拓扑结构，包括分支长度和分叉模式，以估计在由罕见驱动事件驱动的间断进化模式下边缘适应度概率。为了解释WGD后异常率升高，我们引入了一种树缩放策略，调整谱系特异性基因组不稳定性。与关注预定义亚克隆的方法不同，LeafRank对所有采样细胞进行排序，从而能够灵活评估生长异质性。模拟显示在空间和非空间虚拟肿瘤中具有高准确性。应用于卵巢癌，LeafRank揭示了WGD肿瘤中的定向选择和并行选择，并识别出在高适应度谱系中富集的复发拷贝数事件。WGD谱系并未立即显示生长优势，而是通过后续改变获得适应度。

## Abstract
Tumors contain cancer cells with diverse growth potentials that shape evolutionary trajectories, yet this fitness diversity remains difficult to quantify in cases of whole-genome duplication (WGD) and chromosomal instability. We present LeafRank, a mathematical framework that leverages single-cell DNA-seq phylogenies to infer the relative fitness of individual cells. Using a multi-type branching process model, LeafRank integrates full tree topology, including branch lengths and bifurcation patterns, to estimate marginal fitness probabilities under punctuated evolutionary regimes driven by rare driver events. To account for elevated aberration rates following WGD, we introduce a tree-rescaling strategy that adjusts for lineage-specific genomic instability. Unlike methods focused on predefined subclones, LeafRank ranks all sampled cells, enabling flexible assessment of growth heterogeneity. Simulations demonstrate high accuracy across spatial and non-spatial virtual tumors. Applied to ovarian cancer, LeafRank reveals directional and parallel selection in WGD tumors and identifies recurrent copy number events enriched in high-fitness lineages. WGD lineages do not show immediate growth advantages but acquire fitness through subsequent alterations.