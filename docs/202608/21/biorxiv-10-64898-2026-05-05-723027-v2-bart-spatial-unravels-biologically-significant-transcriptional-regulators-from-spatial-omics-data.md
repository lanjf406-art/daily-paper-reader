---
title: BART-spatial unravels biologically significant transcriptional regulators from spatial omics data
title_zh: BART-spatial从空间组学数据中解析具有生物学意义的转录调控因子
authors: "Wang, J., Zhang, H., Wang, Z., Zang, C."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.05.723027v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间转录组调控因子推断工具，可用于肿瘤耐药转录组研究
tldr: 空间组学数据为研究转录调控因子（TR）活性提供了新机会，但TR表达低且活性与mRNA水平不直接相关，现有非空间方法忽视空间异质性。为此提出BART-spatial，整合空间变异和拟时序信息与公开TR结合谱，从空间组学推断功能性TR。在多个平台（如10x Visium、Visium HD、Atera、空间RNA-ATAC-seq）上优于现有方法，能识别状态特异TR及表达无法揭示的调控因子，且兼容空间表观组学。该工具可稳健解码空间分辨的基因调控程序。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有空间组学工具主要针对非空间单细胞数据，忽视空间异质性，且难以应对TR低表达和活性与mRNA不相关的问题。
method: BART-spatial整合空间变异和拟时序信息，结合公开TR结合位点谱，从空间转录组和表观组数据推断功能性转录调控因子。
result: 在多种空间平台数据上优于现有方法，能识别状态特异TR及表达无法检测的调控因子，并兼容空间表观组学实现交叉验证。
conclusion: BART-spatial提供了稳健高效的工具，可解码空间分辨的基因调控程序，助力理解组织发育和疾病机制。
---

## 摘要
转录调控因子(Transcriptional regulators, TRs)通过激活或抑制谱系特异性基因、整合环境信号与内在调控网络，是细胞命运决定的关键调控者。识别功能性TRs对于理解发育、组织结构和疾病至关重要。新兴的空间转录组学和表观基因组学技术现在能够以接近单细胞的分辨率绘制基因组特征图谱，同时保留每个细胞物理位置及其微环境的信息，而这些因素会影响TR活性。尽管取得了这些进展，但由于TR表达水平低，且TR活性往往与mRNA水平不直接相关，在空间数据中识别活性TRs仍具挑战性。此外，现有工具主要针对非空间单细胞数据设计，忽略了空间异质性。为弥合这一差距，我们开发了BART-spatial(用于空间组学数据转录调控的结合分析)，一种从空间组学数据推断功能性TRs的创新计算方法。BART-spatial整合了空间变异性和伪时间信息以及公开可用的TR结合谱。应用于来自多种平台(包括10x Visium、Visium HD、Atera和空间RNA-ATAC-seq)的多个空间数据集，BART-spatial始终优于现有方法，能够识别状态特异性TRs，并揭示仅凭表达无法检测到的调控因子。它与空间表观基因组数据的兼容性进一步增强了其实用性，并能够进行交叉验证。总之，BART-spatial为解码空间分辨的基因调控程序提供了强大而稳健的工具。

## Abstract
Transcriptional regulators (TRs) are crucial regulators of cell fate decisions by activating or repressing lineage-specific genes and integrating environmental signals with intrinsic networks. Identifying functional TRs is essential for understanding development, tissue organization, and disease. Emerging spatial transcriptomics and epigenomics technologies now provide near-single-cell resolution mapping of genomic features while preserving information of each cell's physical location and microenvironment which influence TR activity. Despite these advances, identifying active TRs in spatial data remains challenging due to low TR expression and the fact that TR activity often does not correlate directly with mRNA levels. Moreover, existing tools mainly designed for non-spatial single-cell data overlook spatial heterogeneity. To bridge this gap, we developed BART-spatial (Binding Analysis for Regulation of Transcription for spatial omics data), an innovative computational method to infer functional TRs from spatial omics data. BART-spatial integrates spatial variability and pseudotemporal information with publicly available TR binding profiles. Applied to multiple spatial datasets from diverse platforms, including 10x Visium, Visium HD, Atera, and spatial RNA-ATAC-seq, BART-spatial consistently outperforms existing methods, identifying state-specific TRs and revealing regulators undetectable by expression alone. Its compatibility with spatial epigenomics data further strengthens its utility and enables cross-validation. Overall, BART-spatial provides a powerful and robust tool for decoding spatially resolved gene regulatory programs.