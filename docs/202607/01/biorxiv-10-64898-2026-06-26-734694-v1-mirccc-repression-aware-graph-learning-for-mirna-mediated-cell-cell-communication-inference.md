---
title: "mirCCC: Repression-aware graph learning for miRNA-mediated cell-cell communication inference"
title_zh: "mirCCC: 用于miRNA介导的细胞-细胞通讯推断的抑制感知图学习"
authors: "Chen, Y., Cui, J., Zhang, S., Liu, E., Xie, L., Feng, C., Chen, M."
date: 2026-07-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.26.734694v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 从单细胞RNA测序推断miRNA介导的细胞间通讯，可用于肿瘤微环境耐药机制研究
tldr: 细胞间通讯分析通常关注蛋白配体-受体，忽略了细胞外囊泡介导的microRNA转移这一重要信号途径。本文提出mirCCC框架，从单细胞转录组数据推断microRNA介导的通讯。它通过检测验证的miRNA靶基因表达协调下降来估计细胞特异性miRNA活性，建模细胞外囊泡的发送和接收能力，并学习miRNA解析的通讯图。在合成基准测试中，mirCCC在强混淆信号下表现优于其他方法；应用于结直肠癌数据集，恢复了已知癌症相关miRNA，并揭示了基质和髓系细胞向上皮细胞的通讯，汇聚于TGF-β和Wnt/β-catenin信号相关的可塑性程序。该工作为在现有单细胞图谱中研究细胞外囊泡介导的通讯提供了实用途径。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有细胞通讯分析方法忽略细胞外囊泡介导的miRNA通讯，而miRNA在癌症信号中起重要作用。
method: 提出mirCCC框架，通过检测miRNA靶基因的协调下调估计细胞特异性miRNA活性，并建模细胞外囊泡的发送/接收能力。
result: 在合成基准中优于其他方法；在结直肠癌数据中恢复已知miRNA，并发现基质-髓系向上皮通讯可塑性程序。
conclusion: mirCCC为从现有单细胞图谱中研究细胞外囊泡介导的细胞通讯提供了实用途径。
---

## 摘要
细胞-细胞通讯分析通常关注蛋白质配体和受体，因此忽略了细胞外囊泡介导的microRNA转移，这是癌症中重要的信号传递途径。在这里，我们展示了通过检测已验证的miRNA靶基因表达中的协调下降，可以从标准的单细胞RNA测序中推断出miRNA介导的通讯。我们开发了mirCCC，一个计算框架，它估计细胞特异性miRNA活性，模拟细胞外囊泡转移的细胞发送和接收能力，并从转录组数据中学习miRNA解析的通讯图。在具有强混杂信号的合成基准测试中，mirCCC表现提升，而所有比较方法均下降。应用于人类结直肠癌图谱，mirCCC恢复了已知的结直肠癌相关miRNA，并识别了基质细胞和髓系细胞到上皮细胞的通讯，这些通讯汇聚到一个与TGF-β和Wnt/β-catenin信号相关的可塑性程序。这些结果为在现有单细胞图谱中研究细胞外囊泡介导的通讯提供了实用途径。

## Abstract
Cell-cell communication analyses usually focus on protein ligands and receptors and therefore miss the extracellular vesicle-mediated transfer of microRNAs, an important route of signalling in cancer. Here, we show that microRNA-mediated communication can be inferred from standard single-cell RNA sequencing by detecting coordinated decreases in the expression of validated miRNA target genes. We developed mirCCC, a computational framework that estimates cell-specific microRNA activity, models cellular sending and receiving capacities for extracellular vesicle transfer, and learns microRNA-resolved communication graphs from transcriptomic data. In synthetic benchmarks with strong confounding signals, mirCCC improved, whereas all comparison methods declined. Applied to a human colorectal cancer atlas, mirCCC recovered known colorectal cancer-associated microRNAs and identified stromal- and myeloid-to-epithelial communication converging on a plasticity program linked to TGF-{beta} and Wnt/{beta}-catenin signalling. These results provide a practical route for studying extracellular vesicle-mediated communication in existing single-cell atlases.