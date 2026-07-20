---
title: "LeafRank: A phylodynamic framework for inferring relative fitness from single-cell phylogenies in chromosomally unstable tumors"
title_zh: LeafRank：一种从染色体不稳定肿瘤的单细胞系统发育推断相对适应性的系统动力学框架
authors: "Wu, C., Leder, K., Wang, Z., Sun, R."
date: 2026-07-18
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.06.736651v3.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞系统发育框架推断肿瘤适合度，可应用于耐药机制研究
tldr: 肿瘤内细胞生长潜力多样但难以量化，尤其在全基因组加倍(WGD)和染色体不稳定情况下。本文提出LeafRank，基于单细胞DNA-seq系统发育树，采用多类型分支过程模型和树重缩放策略，推断单个细胞的相对适应性。模拟显示高精度；在卵巢癌中，LeafRank揭示了WGD后的方向性和平行选择，识别出高适应谱系中富集的重复拷贝数事件。该框架可对单个细胞排序，灵活评估生长异质性。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1594, \"height\": 1401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1581, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1569, \"height\": 1801, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1249, \"height\": 1921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1661, \"height\": 1115, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1661, \"height\": 1359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1642, \"height\": 898, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736651-v3/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1585, \"height\": 470, \"label\": \"Table\"}]"
motivation: 肿瘤内细胞生长潜力多样难以量化，尤其在全基因组加倍和染色体不稳定情况下。
method: 基于单细胞DNA-seq系统发育树，采用多类型分支过程模型和树重缩放策略推断相对适应性。
result: 模拟验证高精度；在卵巢癌中识别WGD后方向性和平行选择，发现高适应谱系富集的重复拷贝数事件。
conclusion: LeafRank可对单个细胞排序，揭示WGD后适应性通过后续基因组改变获得。
---

## 摘要
肿瘤包含具有不同生长潜力的癌细胞，这些细胞塑造了进化轨迹，然而，在全基因组加倍（WGD）和染色体不稳定的情况下，这种适应性多样性仍然难以量化。我们提出了LeafRank，一个利用单细胞DNA-seq系统发育来推断单个细胞相对适应性的数学框架。使用多类型分支过程模型，LeafRank整合了完整的树拓扑结构，包括分支长度和分叉模式，以估计由罕见驱动事件驱动的间断进化模式下的边际适应性概率。为了解释WGD后异常率的升高，我们引入了一种树重缩放策略，调整谱系特异性基因组不稳定性。与专注于预定义亚克隆的方法不同，LeafRank对所有采样细胞进行排序，从而能够灵活评估生长异质性。模拟表明，在空间和非空间虚拟肿瘤中均具有高准确性。应用于卵巢癌时，LeafRank揭示了WGD肿瘤中的定向和并行选择，并识别出在高适应性谱系中富集的反复拷贝数事件。WGD谱系并未立即显示出生长优势，而是通过后续改变获得适应性。

## Abstract
Tumors contain cancer cells with diverse growth potentials that shape evolutionary trajectories, yet this fitness diversity remains difficult to quantify in cases of whole-genome duplication (WGD) and chromosomal instability. We present LeafRank, a mathematical framework that leverages single-cell DNA-seq phylogenies to infer the relative fitness of individual cells. Using a multi-type branching process model, LeafRank integrates full tree topology, including branch lengths and bifurcation patterns, to estimate marginal fitness probabilities under punctuated evolutionary regimes driven by rare driver events. To account for elevated aberration rates following WGD, we introduce a tree-rescaling strategy that adjusts for lineage-specific genomic instability. Unlike methods focused on predefined subclones, LeafRank ranks all sampled cells, enabling flexible assessment of growth heterogeneity. Simulations demonstrate high accuracy across spatial and non-spatial virtual tumors. Applied to ovarian cancer, LeafRank reveals directional and parallel selection in WGD tumors and identifies recurrent copy number events enriched in high-fitness lineages. WGD lineages do not show immediate growth advantages but acquire fitness through subsequent alterations.