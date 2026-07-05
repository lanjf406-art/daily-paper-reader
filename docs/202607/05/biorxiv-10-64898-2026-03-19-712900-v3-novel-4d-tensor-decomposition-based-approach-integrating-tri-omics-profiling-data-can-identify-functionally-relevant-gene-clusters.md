---
title: Novel 4D tensor decomposition-based approach integrating tri-omics profiling data can identify functionally relevant gene clusters
title_zh: 基于新型四维张量分解整合三组学数据的方法可识别功能相关的基因簇
authors: "Turki, T., Taguchi, Y.-h."
date: 2026-07-04
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.19.712900v3.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 使用张量分解的多组学整合方法
tldr: 整合转录组、翻译组和蛋白质组等多组学数据是理解基因表达调控的关键，但缺乏无监督整合框架。本文提出基于四维张量分解（HOSVD）的无监督特征提取方法，对支链氨基酸饥饿下的三组学数据进行分解，捕获了核糖体堆积和翻译缓冲两种调控模式。基因选择识别出1781个与核糖体堆积相关、227个与翻译缓冲相关的基因，富集分析揭示了它们参与翻译、应激、细胞周期等通路。与MOFA+和mixOmics对比，本方法能更直接提取可解释的生物学成分。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法难以无监督整合转录组、翻译组和蛋白质组数据，识别基因调控的功能模块。
method: 提出四维张量分解（HOSVD）方法，对三组学数据进行高阶奇异值分解，并基于奇异值向量选择基因。
result: 识别出核糖体堆积（1781基因）和翻译缓冲（227基因）两组基因，富集于翻译、应激、细胞周期等通路，且优于对比方法。
conclusion: 张量分解可有效从三组学数据中提取可解释的生物学调控模式，有助于发现功能相关基因簇。
---

## 摘要
理解基因表达需要整合多个调控层次，因为转录本丰度不一定对应于翻译活性或蛋白质丰度。核糖体图谱和蛋白质组学有助于区分翻译增强与核糖体堆积或翻译缓冲，但目前尚无用于无监督整合转录组、翻译组和蛋白质组谱的事实标准框架。本文提出了一种基于四维张量分解的无监督特征提取方法用于三组学整合。我们将高阶奇异值分解应用于支链氨基酸饥饿条件下测量的转录组、Ribo-seq和蛋白质组谱。得到的奇异值向量捕捉了三个组学层之间的关系，包括一个与核糖体堆积一致的组分（其中转录组和翻译组信号增强而蛋白质组信号减弱），以及另一个与翻译缓冲一致的组分（尽管转录组和翻译组发生变化，但蛋白质组变异被抑制）。基因选择鉴定出1,781个与核糖体堆积相关的基因和227个与翻译缓冲相关的基因。富集分析将前者与翻译、翻译后蛋白质修饰、RNA聚合酶II转录、细胞周期调控、内质网蛋白质加工、泛素介导的蛋白水解和应激相关通路联系起来，将后者与核糖体、翻译延伸和终止、剪接体、免疫和应激相关通路以及核糖体病相关疾病联系起来。稳健性分析表明，结果不受重复蛋白质组样本或缺失值处理的显著影响。在测试条件下，与MOFA+和mixOmics的比较表明，我们的方法更直接地提取了可解释为核糖体堆积和翻译缓冲的成分。这些结果证明，基于张量分解的无监督特征提取对于从三组学数据中识别功能相关的基因簇是有用的。

## Abstract
Understanding gene expression requires integrating multiple regulatory layers, because transcript abundance does not necessarily correspond to translational activity or protein abundance. Ribosome profiling and proteomics help distinguish increased translation from ribosome stacking or translational buffering, but no de facto standard framework exists for unsupervised integration of transcriptome, translatome, and proteome profiles. Here, we propose a four-dimensional tensor decomposition-based unsupervised feature extraction approach for tri-omics integration. We applied higher-order singular value decomposition to transcriptome, Ribo-seq, and proteome profiles measured under branched-chain amino acid starvation. The resulting singular value vectors captured relationships among the three omics layers, including a component consistent with ribosome stacking, where transcriptome and translatome signals increased while proteome signals decreased, and another consistent with translational buffering, where proteome variation was suppressed despite transcriptome and translatome changes. Gene selection identified 1,781 genes associated with ribosome stacking and 227 genes associated with translational buffering. Enrichment analyses linked the former to translation, post-translational protein modification, RNA polymerase II transcription, cell cycle regulation, endoplasmic reticulum protein processing, ubiquitin-mediated proteolysis, and stress-related pathways, and the latter to ribosome, translation elongation and termination, spliceosome, immune- and stress-related pathways, and ribosomopathy-associated diseases. Robustness analyses indicated that the results were not substantially affected by the duplicated proteome replicate or missing-value handling. Under the tested settings, comparison with MOFA+ and mixOmics suggested that our approach more directly extracted components interpretable as ribosome stacking and translational buffering. These results demonstrate that tensor decomposition-based unsupervised feature extraction is useful for identifying functionally relevant gene clusters from tri-omics data.