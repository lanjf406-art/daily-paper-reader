---
title: "ATAClone: Cancer Clone Identification and Copy Number Estimation from Single-cell ATAC-seq"
title_zh: ATAClone：基于单细胞ATAC-seq的癌症克隆鉴定和拷贝数估计
authors: "Cain, L. D., Trigos, A. S."
date: 2026-06-24
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.11.710984v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 用于肿瘤克隆鉴定的单细胞ATAC-seq方法，可应用于耐药机制研究
tldr: 单细胞ATAC-seq分析中，DNA拷贝数差异常导致聚类结果误判。ATAClone通过识别共享拷贝数谱的癌细胞克隆并联合估计拷贝数，解决了这一问题。它利用稳定可及区域和总DNA差异推断绝对拷贝数，并通过模拟自动确定最佳聚类分辨率。在细胞混合物和匹配bulk测序实验中，ATAClone准确分离克隆，拷贝数估计与bulk结果高度相关（r=0.75-0.95），为解析肿瘤遗传与非遗传因素提供关键工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 单细胞ATAC-seq分析中，DNA拷贝数差异造成聚类结果偏差，影响肿瘤异质性研究，亟需一种能识别克隆并准确估计拷贝数的方法。
method: 利用稳定可及区域最大化拷贝数信号，通过模拟确定最佳聚类分辨率，并利用细胞总DNA差异推断绝对拷贝数。
result: 在细胞混合物实验中准确分离克隆；与bulk WGS结果相关性0.75-0.95，优于现有方法。
conclusion: ATAClone能有效区分遗传与非遗传因素对基因表达的贡献，揭示肿瘤演化历史。
---

## 摘要
癌症的单细胞分析通常首先通过无监督聚类来识别不同的癌细胞群体。然而，在许多情况下，这种聚类仅由DNA拷贝数的差异解释，这影响了差异表达结果和肿瘤异质性研究的解读。为了检测和估计这些拷贝数差异，我们开发了ATAClone。ATAClone适用于独立的和multiome scATAC-seq实验，首先识别具有共享DNA拷贝数谱（即克隆）的癌细胞，然后联合估计它们的拷贝数。重要的是，ATAClone可以通过模拟自动确定最佳聚类分辨率。通过仅利用稳定可及的染色质区域，ATAClone最大化拷贝数信号，同时最小化无关的生物和技术噪声。此外，通过利用细胞间总DNA的差异，ATAClone可以推断绝对拷贝数，即使存在多倍体。利用癌细胞混合实验，我们验证了ATAClone基于拷贝数差异准确分离克隆的能力。此外，使用匹配的scATAC-seq和批量全基因组测序，我们表明ATAClone的拷贝数估计比现有方法更准确，与其批量估计的Pearson相关系数在0.75-0.95之间。ATAClone是解开癌症中基因表达遗传和非遗传贡献的重要工具，为驱动肿瘤的进化历史和适应力提供了更深入的见解。

## Abstract
Single-cell analyses of cancer typically begin by identifying distinct populations of cancer cells by unsupervised clustering. However, in many cases this clustering is explained simply by differences in DNA copy number, which affects the interpretation of differential expression results and tumour heterogeneity studies. To detect and estimate these differences in copy number, we have developed ATAClone. Applicable to both standalone and multiome scATAC-seq assays, ATAClone first identifies cancer cells with shared DNA copy number profiles (i.e. clones), then estimates their copy number jointly. Importantly, ATAClone can determine an optimal clustering resolution automatically using simulations. By utilising only stably accessible regions, ATAClone maximises copy number signal while minimising unrelated biological and technical noise. Additionally, by leveraging differences in total DNA between cells, ATAClone can infer absolute copy number, even in the presence of polyploidy. Using cancer cell mixture experiments, we verify the ability of ATAClone to accurately separate clones based on copy number differences. Moreover, using matched scATAC-seq and bulk whole genome sequencing, we show that copy number estimates from ATAClone are more accurate than those derived with existing methods, achieving Pearson correlations between 0.75-0.95 with their bulk-derived estimates. ATAClone represents an important tool for disentangling the genetic and non-genetic contributions to gene expression in cancer, providing deeper insight into the evolutionary history and adaptive forces driving a tumour.