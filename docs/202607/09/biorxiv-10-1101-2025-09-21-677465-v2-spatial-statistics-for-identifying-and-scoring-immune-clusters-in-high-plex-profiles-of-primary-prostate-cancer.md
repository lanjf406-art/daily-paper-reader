---
title: Spatial statistics for identifying and scoring immune clusters in high-plex profiles of primary prostate cancer
title_zh: 用于识别和评分原发性前列腺癌高plex图谱中免疫簇的空间统计方法
authors: "Amiryousefi, A., Wala, J., Lin, J.-R., Labadie, B. W., Atmakuri, A., Maliga, Z., Toye, E., Chaudagar, K., Torcasso, M. S., Coy, S., Fanelli, G. N., Kobs, B., Socciarelli, F., Gagne, A., Van Allen, E. M., Patnaik, A., Sorger, P."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.1101/2025.09.21.677465v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 肿瘤微环境中免疫簇的空间统计方法
tldr: 肿瘤微环境中免疫细胞的空间分布多样，但缺乏客观参数化方法。本研究提出R包tlsR，利用空间统计识别和评分免疫细胞簇。应用于29例前列腺癌样本，发现高Gleason分级肿瘤中淋巴细胞浸润显著增多，存在B/T细胞富集簇及类似三级淋巴结构，并含前体耗竭T细胞和增殖B细胞。结果表明高分级前列腺癌并非免疫冷肿瘤，具有活跃免疫监视特征，为免疫治疗提供新见解。
source: biorxiv
selection_source: fresh_fetch
motivation: 缺乏客观参数化肿瘤微环境中免疫细胞空间模式的方法，难以评估肿瘤免疫状态。
method: 开发R包tlsR，利用空间统计对多重成像数据中的免疫细胞簇进行识别和评分。
result: 高Gleason前列腺癌中淋巴细胞浸润显著增多，存在B/T细胞富集簇、TLS特征及前体耗竭T细胞。
conclusion: 高分级前列腺癌并非免疫冷，而具有活跃免疫监视，对免疫治疗有重要意义。
---

## 摘要
肿瘤微环境（TME）中免疫细胞的空间排列差异很大，从分散到聚集，从肿瘤排除到浸润。多重空间分析是描述TME中肿瘤浸润淋巴细胞（TILs）和三级淋巴结构（TLS）等免疫复合物的有效手段。然而，很少有方法能够客观参数化免疫组织模式并评估其与生物学或临床变量的关联，这使得评估一组肿瘤相对免疫“冷”或“热”变得困难。本文描述了一套直观的统计工具（包含在R包tlsR中），用于表征实体癌TME中的淋巴细胞模式。我们将tlsR应用于原发性前列腺癌（PCa），它通常被描述为免疫“冷”。使用一组29例根治性前列腺切除标本，按低Gleason分级（LGG；n=15）和高Gleason分级（HGG；n=14）分层，我们发现HGG PCa的淋巴细胞浸润显著高于LGG PCa，这些淋巴细胞组织成B细胞或T细胞富集的免疫簇（BIC和TIC）。这些IC中的一部分具有真正的TLS特征，即B细胞和T细胞区域化以及滤泡树突状细胞。HGG还富含含有前体耗竭T细胞（Tpex）和增殖B细胞的IC，其肿瘤区室中存在与癌细胞接触的颗粒酶B+细胞毒性T细胞。因此，一部分HGG PCa远非免疫“冷”，而是具有与活跃免疫监视相关的特征，这一发现对新兴的PCa免疫疗法具有重要意义。

## Abstract
The spatial arrangement of immune cells in the tumor microenvironment (TME) varies widely, from dispersed to clustered and tumor excluded to infiltrating. Multiplexed spatial profiling is an effective means of characterizing tumor-infiltrating lymphocytes (TILs) and immune complexes such as tertiary lymphoid structures (TLS) in the TME. However, few approaches have been described for objectively parametrizing patterns of immune organization and assessing their association with biological or clinical variables. This makes it difficult to evaluate whether a set of tumors is relatively immunologically cold or hot. Here we describe an intuitive set of statistical tools (available in the R package, tlsR) for characterizing lymphocyte patterns in the TME of solid cancers. We apply tlsR to primary prostate cancer (PCa), which is often described as immunologically  cold. Using a cohort of 29 radical prostatectomy specimens stratified into low Gleason-grade (LGG; n=15) and high Gleason-grades (HGG; n =14) we show that HGG PCa is significantly more infiltrated than LGG PCa with lymphocytes organized into B cell or T cell enriched immune clusters (BICs and TICs). A subset of these ICs have the B and T cell zonation and follicular dendritic cells characteristic of a bona fide TLS. HGGs are also enriched with ICs containing precursor exhausted T cells (Tpex) and proliferating B cells and their tumor compartments harbor granzyme-B+ cytotoxic T cells in contact with cancer cells. Thus, far from being cold, a subset of HGG PCa has features associated with active immune surveillance, a finding with implications for emerging PCa immunotherapies.