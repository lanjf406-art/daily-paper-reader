---
title: Easy-Multiome enables joint profiling of gene expression and chromatin accessibility in single cells
title_zh: Easy-Multiome实现单细胞中基因表达与染色质可及性的联合分析
authors: "ZHANG, X., Minow, M. A. A., Schmitz, R. J."
date: 2026-07-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.15.738754v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞多组学方法联合分析基因表达和染色质可及性
tldr: "植物单细胞中联合分析基因表达与染色质可及性存在流程复杂、性能不稳定及成本高等挑战。本研究提出easy-Multiome方法，通过在标准液滴scATAC-seq流程中整合一步原位反转录，从玉米幼苗超过20000个核中同时获得高质量基因表达和染色质可及性图谱，其中约90%的核兼具两种高质量数据。该方法解析出16个细胞簇对应9种主要细胞类型，并直接表征了同一核的细胞类型特异性染色质开放状态，同时捕获转录因子表达与其DNA结合基序可及性的关联。easy-Multiome以最小修改实现了稳健高效的植物单细胞多组学联合分析，为研究转录调控机制提供了直接工具。"
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738754-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1126, \"height\": 756, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738754-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1019, \"height\": 1700, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738754-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1716, \"height\": 1329, \"label\": \"Figure\"}]"
motivation: 现有植物单细胞联合分析方法流程复杂、性能不稳定且成本高昂，限制了其应用。
method: 在标准液滴scATAC-seq中整合单步原位反转录，实现同一核内同时捕获基因表达和染色质可及性。
result: "从玉米幼苗超过20000个核中获得约90%双高质量数据，解析出16个簇对应9种细胞类型，并直接关联转录因子表达与基序可及性。"
conclusion: easy-Multiome仅需最小修改现有scATAC-seq流程，即可稳健高效地实现植物单细胞多组学联合分析。
---

## 摘要
基因表达和染色质可及性为定义细胞状态的调控机制提供了互补的见解。尽管已有联合分析这些模态的方法，但由于工作流程复杂、性能不稳定以及成本高昂，植物应用仍然有限。在此，我们提出easy-Multiome，一种简化的单细胞多组学工作流程，它将单个原位逆转录步骤整合到标准的基于液滴的scATAC-seq方案中。利用easy-Multiome，我们从玉米幼苗中分析了超过20,000个细胞核，生成了配对基因表达和染色质可及性数据，其中约90%的细胞核同时包含高质量的RNA和染色质可及性图谱。得到的转录组数据解析出对应于九种主要玉米幼苗细胞类型的16个聚类，并能够直接从相同的细胞核中表征细胞类型特异性的染色质可及性。此外，easy-Multiome同时捕获了细胞类型特异性的转录因子表达及其同源DNA结合基序的可及性，从而在转录程序与调控景观之间建立了直接联系。总之，这些结果表明，easy-Multiome能够稳健且高效地联合分析植物基因表达和染色质可及性，同时仅需对现有基于液滴的scATAC-seq工作流程进行极小的修改。

## Abstract
Gene expression and chromatin accessibility provide complementary insights into the regulatory mechanisms that define cell states. Although methods for jointly profiling these modalities exist, plant applications remain limited because of complex workflows, inconsistent performance, and prohibitive costs. Here, we present easy-Multiome, a streamlined single-cell multiomic workflow that integrates a single in situ reverse transcription step into the standard droplet-based scATAC-seq protocol. Using easy-Multiome, we profiled more than 20,000 nuclei from maize seedlings generating paired gene expression and chromatin accessibility data, with approximately 90% of nuclei containing both high-quality RNA and chromatin accessibility profiles. The resulting transcriptome data resolved 16 clusters corresponding to nine major maize seedling cell types and enabled direct characterization of cell-type-specific chromatin accessibility from the same nuclei. Furthermore, easy-Multiome simultaneously captured cell-type-specific transcription factor expression and the accessibility of their cognate DNA-binding motifs, providing direct links between transcriptional programs and regulatory landscapes. Together, these results demonstrate that easy-Multiome enables robust and efficient joint profiling of plant gene expression and chromatin accessibility while requiring only minimal modifications to existing droplet-based scATAC-seq workflows.