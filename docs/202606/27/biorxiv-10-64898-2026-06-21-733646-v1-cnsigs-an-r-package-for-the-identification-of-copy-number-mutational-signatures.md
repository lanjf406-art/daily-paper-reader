---
title: "CNSigs: An R Package for the Identification of Copy Number Mutational Signatures"
title_zh: CNSigs：用于识别拷贝数突变特征的R包
authors: "Tallman, D., Striker, S., Byappanahalli, A. M., Stockard, S., Jenison, J., Collier, K. A., Blige, E., Vater, M., Stover, D. G."
date: 2026-06-25
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.21.733646v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 拷贝数突变签名识别工具，可用于肿瘤耐药的多组学表征
tldr: 拷贝数变异（CNA）在癌症中普遍存在，但其模式和机制尚不明确。该研究开发了R包CNSigs，从DNA测序分段数据中提取六种CNA特征，利用混合模型和非负矩阵分解（NMF）推导CNA签名。在乳腺癌数据中验证了5种高重现性签名，并在TCGA泛癌数据中识别出13种与生存显著相关的签名。CNSigs在ctDNA中可检测，并与治疗反应和免疫表型关联，为研究CNA形成机制提供了便捷工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 拷贝数变异在癌症中普遍存在，但其潜在过程和特征模式尚不清晰，缺乏类似SNV突变签名的计算工具。
method: 从DNA测序分段数据中提取六种拷贝数特征，采用混合模型和非负矩阵分解（NMF）推导CNA签名，并封装为R包CNSigs。
result: 在乳腺癌数据中重现5种签名（余弦相似度0.89），在TCGA中识别13种泛癌签名与生存显著相关；在ctDNA中可检测，并发现与化疗疗效和免疫表型的关联。
conclusion: CNSigs包使研究者能方便地分析样本获得CNA签名并评估临床关联，为揭示CNA形成机制和临床应用提供了新工具。
---

## 摘要
背景：拷贝数畸变（CNA）是大多数癌症类型中存在的大规模基因组片段的获得和丢失，是癌症基因组改变的一个标志。然而，CNA背后的过程以及CNA的特征模式尚不明确。生物信息学进展已经识别出由不同突变过程产生的单核苷酸变异（SNV）突变特征，但能够揭示CNA类似特征的算法开发仍相对滞后。

方法：利用DNA测序的分段数据文件，提取六个拷贝数特征用于特征确定：片段大小、每10兆碱基的断点数、拷贝数振荡事件、平均变化点大小、平均拷贝数以及每条染色体臂的断点数，同时包括倍性。采用混合模型方法和非负矩阵分解（NMF）来推导跨癌症类型的CNA特征。完整的方法被封装在一个稳健的R包中，命名为CNSigs，该包已公开可用。

结果：为了验证特征的可重复性，我们从两个独立的乳腺癌数据集（总样本量>3000）中推导出五个特征，显示出高准确性（平均余弦相似度=0.89）。CNSigs在TCGA数据集中的泛癌应用产生了13个泛癌特征，这些特征与疾病特异性生存显著相关。将CNSigs与TCGA中的其他两种CNA特征方法进行基准测试，显示出非重叠的特征和有利的计算速度。我们评估了n=24对同时获取的肿瘤和循环肿瘤DNA（ctDNA），并证明CNSig可通过ctDNA检测且可重复，其中CNSig11与转移性三阴性乳腺癌在紫杉烷化疗下的无进展生存期显著相关，但与铂类或卡培他滨化疗无关。在低级别胶质瘤（LGG）中评估了CNSigs与免疫表型的关联，发现CNSig3对LGG具有高度预后价值，但与免疫特征互补。

结论：CNSigs R包允许研究人员轻松分析自己的样本，以推导拷贝数特征并评估临床关联。我们展示了在ctDNA中的潜在应用以及与治疗反应的关联。该包的开发有助于进一步研究可能负责这些CNA指纹的潜在过程。

## Abstract
BackgroundCopy number aberrations (CNAs) are gains and losses of large genomic segments present across most cancer types and are a hallmark of cancer genomic alterations. However, the processes underlying CNAs and characteristic patterns of CNAs are poorly understood. Bioinformatic advances have identified underlying single nucleotide variant (SNV) mutational signatures resulting from distinct mutational processes, yet development of algorithms able to uncover similar signatures for CNAs remains less advanced.

MethodsUsing segmented data files from DNA sequencing, six copy number features are extracted for signature determination: segment size, breakpoints per 10 megabases, copy number oscillation events, average changepoint size, average copy number, and breakpoints per chromosome arm, along with ploidy. Mixed model approaches and non-negative matrix factorization (NMF) are utilized to derive CNA signatures across cancer types. The full methodology was packaged in a robust R package, termed  CNSigs that is publicly available.

ResultsTo verify the reproducibility of the signatures, we derived five signatures from two independent breast cancer datasets (total n>3000), demonstrating high accuracy (average cosine similarity = 0.89). Pan-cancer application of CNSigs in the TCGA dataset resulted in derivation of 13 pan-cancer signatures which were significantly associated with disease-specific survival. Benchmarking CNSigs to two other CNA signature approaches within TCGA demonstrated non-overlapping signatures and favorable compute speed for CNSigs. We evaluated n=24 pairs of tumor and circulating tumor DNA (ctDNA) acquired at the same time and demonstrated that CNSigs are detectable and reproducible via ctDNA, with significant association of CNSig11 with metastatic triple-negative breast cancer progression-free survival for taxane but not platinum or capecitabine chemotherapy. CNSigs association with immunophenotype was evaluated in low-grade glioma (LGG) and CNSig 3 was found to be highly prognostic for LGG yet complementary to immune features.

ConclusionsThe CNSigs R package allows researchers to easily analyze their own samples to derive copy number signatures and evaluate clinical associations. We demonstrate potential application in ctDNA and association with treatment response. The development of this package allows further investigation of underlying processes that may be responsible for these CNA fingerprints.