---
title: Novel biologically relevant small RNA-sequencing alignment tool LevenMap for alignment to database of non-coding RNAs
title_zh: 新型生物相关性小RNA测序比对工具LevenMap，用于与非编码RNA数据库进行比对
authors: "Dlugas, H., Dyson, G., Dombkowski, A., Kim, Y., Gurdziel, K., Boerner, J. L., Bock, C."
date: 2026-08-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.14.742100v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: RNA测序比对工具，可支撑肿瘤耐药相关转录组学分析。
tldr: 针对小RNA测序比对到非编码RNA数据库这一特殊任务，现有比对工具多面向基因组长读段，忽略ncRNA与读段长度相近且存在包含关系。新算法LevenMap专为此设计，能完整比对所有精确匹配读段，且读段与参考长度比接近1，显著优于Bowtie、BWA和STAR，提供更生物学相关的计数结果。工具开源可用。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有比对器针对基因组读段设计，不适用于ncRNA数据库比对，导致读段归属错误。
method: LevenMap基于编辑距离动态规划，允许零或一个错配，直接比对到ncRNA参考数据库。
result: "精确匹配读段100%被正确比对，长度比平均为1.0，而其他工具均低于0.51。"
conclusion: LevenMap为小RNA-seq分析提供更准确的ncRNA定量结果，适用于非编码RNA研究。
---

## 摘要
小RNA测序生物信息学工作流程中的一个关键方面是将读数与参考ncRNA数据库进行比对。通常使用的比对算法如Bowtie、Burrows-Wheeler Aligner（BWA）和Spliced Transcripts Alignment to a Reference（STAR）是为将读数比对到参考基因组而设计的。将短RNA测序读数与非编码RNA（ncRNA）数据库进行比对，本质上不同于将较长读数比对到基因组，因为ncRNA（i）与所比对读数的核苷酸数量大致相同，并且（ii）是其他ncRNA的子序列。考虑到这些差异，我们开发了新型比对算法LevenMap。在公开可用的数据集中，所有与参考ncRNA精确匹配的读数中，LevenMap将其100.0%比对到各自的ncRNA，而所有其他比对器将这些读数映射到相应ncRNA的比例不到40%。此外，对于LevenMap，允许零个和一个错配时，所有比对读数的平均比率（读数长度/对应参考ncRNA长度）分别为1.0和0.998；而所有其他比对器的该比率不超过0.51。总体而言，LevenMap旨在考虑将小RNA测序数据比对到参考ncRNA数据库的细微差别，在此背景下比传统比对器产生更多生物学相关的计数。LevenMap免费公开，可在GitHub上获取：https://github.com/hdlugas/LevenMap。

## Abstract
A crucial aspect of the bioinformatics workflow in small RNA-sequencing is the alignment of reads to a database of reference ncRNAs. Alignment algorithms such as Bowtie, Burrows-Wheeler Aligner (BWA), and Spliced Transcripts Alignment to a Reference (STAR) - which are designed for aligning reads to a reference genome - are typically used. Aligning short RNA-sequenced reads to a database of non-coding RNAs (ncRNAs) is fundamentally a different task than aligning longer reads to a genome due to ncRNAs (i) having roughly the same number of nucleotides as the reads being aligned and (ii) being subsequences of other ncRNAs. To account for these differences, we developed the novel alignment algorithm LevenMap. Of all reads which exactly matched a reference ncRNA in a publicly available dataset, LevenMap aligned 100.0% of them to their respective ncRNA while all other aligners mapped less than 40% of these reads to their corresponding ncRNA. Furthermore, the mean ratio (length of read) / (length of corresponding reference ncRNA) of all aligned reads was 1.0 and 0.998 for LevenMap with at most zero and one mismatch(es) allowed, respectively; this ratio was no more than 0.51 for all other aligners. Overall, LevenMap is designed to account for the nuances of aligning small RNA-sequencing data to a database of reference ncRNAs and yields more biologically relevant counts compared to traditional aligners in this context. LevenMap is free and publicly available on GitHub: https://github.com/hdlugas/LevenMap.