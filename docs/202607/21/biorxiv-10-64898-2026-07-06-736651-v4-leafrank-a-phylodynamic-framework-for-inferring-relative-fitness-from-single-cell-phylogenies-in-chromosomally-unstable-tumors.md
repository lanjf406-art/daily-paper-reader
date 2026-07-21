---
title: "LeafRank: A phylodynamic framework for inferring relative fitness from single-cell phylogenies in chromosomally unstable tumors"
title_zh: LeafRank：一种从染色体不稳定肿瘤的单细胞系统发育推断相对适应性的系统动力学框架
authors: "Wu, C., Leder, K., Wang, Z., Sun, R."
date: 2026-07-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.06.736651v4.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 从单细胞系统发育推断相对适应度，支持耐药机制研究
tldr: 染色体不稳定肿瘤中癌细胞适应度异质性难以量化，尤其在WGD后。提出LeafRank框架，基于单细胞DNA-seq系统发育树，采用多类型分支过程模型整合树拓扑与分支长度，通过树重缩放策略校正WGD相关基因组不稳定性，估计单细胞相对适应度。模拟证明高精度；卵巢癌应用揭示WGD肿瘤中的定向和并行选择，发现高适应度谱系富集特定拷贝数改变，且WGD后适应度通过后续突变获得。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1594, \"height\": 1401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1581, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1569, \"height\": 1801, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1249, \"height\": 1921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1660, \"height\": 1115, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1661, \"height\": 1359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1642, \"height\": 898, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736651-v4/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1585, \"height\": 470, \"label\": \"Table\"}]"
motivation: 染色体不稳定肿瘤中细胞适应度难以量化，现有方法局限于预定义亚克隆，无法刻画单细胞级异质性。
method: 基于多类型分支过程模型，整合系统发育树拓扑与分支长度，并引入树重缩放策略校正WGD后谱系特异性变异率。
result: 模拟验证高精度；卵巢癌应用显示WGD肿瘤中的定向和并行选择，识别高适应度谱系中富集的拷贝数改变。
conclusion: LeafRank有效推断单细胞适应度，揭示WGD并非立即赋予优势，适应度通过后续突变积累。
---

## 摘要
肿瘤含有具有不同生长潜力的癌细胞，这些潜力塑造了进化轨迹，但在全基因组加倍（WGD）和染色体不稳定性情况下，这种适应性多样性仍然难以量化。我们提出LeafRank，一个数学框架，利用单细胞DNA-seq系统发育来推断单个细胞的相对适应性。通过多类型分支过程模型，LeafRank整合完整的树拓扑结构，包括分支长度和分叉模式，以估计由罕见驱动事件驱动的间断进化模式下的边际适应性概率。为了解释WGD后异常率的升高，我们引入了一种树重缩放策略，以调整谱系特异性基因组不稳定性。与专注于预定义亚克隆的方法不同，LeafRank对所有采样细胞进行排序，从而灵活评估生长异质性。模拟表明，在空间和非空间虚拟肿瘤中均具有高准确性。应用于卵巢癌，LeafRank揭示了WGD肿瘤中的定向和平行选择，并识别了在高适应性谱系中富集的重复拷贝数事件。WGD谱系并未表现出即时的生长优势，而是通过后续改变获得适应性。

## Abstract
Tumors contain cancer cells with diverse growth potentials that shape evolutionary trajectories, yet this fitness diversity remains difficult to quantify in cases of whole-genome duplication (WGD) and chromosomal instability. We present LeafRank, a mathematical framework that leverages single-cell DNA-seq phylogenies to infer the relative fitness of individual cells. Using a multi-type branching process model, LeafRank integrates full tree topology, including branch lengths and bifurcation patterns, to estimate marginal fitness probabilities under punctuated evolutionary regimes driven by rare driver events. To account for elevated aberration rates following WGD, we introduce a tree-rescaling strategy that adjusts for lineage-specific genomic instability. Unlike methods focused on predefined subclones, LeafRank ranks all sampled cells, enabling flexible assessment of growth heterogeneity. Simulations demonstrate high accuracy across spatial and non-spatial virtual tumors. Applied to ovarian cancer, LeafRank reveals directional and parallel selection in WGD tumors and identifies recurrent copy number events enriched in high-fitness lineages. WGD lineages do not show immediate growth advantages but acquire fitness through subsequent alterations.