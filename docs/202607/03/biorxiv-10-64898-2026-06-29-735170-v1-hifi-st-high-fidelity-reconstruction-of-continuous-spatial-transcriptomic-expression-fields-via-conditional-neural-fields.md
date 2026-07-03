---
title: "HiFi-ST: High-Fidelity Reconstruction of Continuous Spatial Transcriptomic Expression Fields via Conditional Neural Fields"
title_zh: HiFi-ST：基于条件神经场的高保真连续空间转录组表达场重建
authors: "Li, H., Tang, L., Han, W., Yang, X., Chen, X."
date: 2026-07-02
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.29.735170v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间转录组重建方法，可应用于肿瘤耐药研究
tldr: "空间转录组数据是离散的稀疏样本，难以捕捉连续表达场。HiFi-ST利用条件神经场框架，将每个点视为区域观测，通过蒙特卡洛采样近似局部积分，结合多尺度组织特征提取和FiLM调制，实现连续表达场高保真重建。在三个数据集上，平均PCC提升65.1%、10.2%、80.0%，MSE降低40.9%、51.2%、16.3%。该方法为解析肿瘤微环境和免疫结构提供了统一框架。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法将空间转录组学视为点回归，忽略了表达的连续性和观测的区域性，导致信息丢失。
method: 提出HiFi-ST条件神经场模型，将空间表达预测建模为连续场学习，通过蒙特卡洛采样模拟区域观测，并用FiLM调制整合多尺度特征。
result: "在HER2+、cSCC、Alex_NatGen上，PCC分别提升65.1%、10.2%、80.0%，MSE分别降低40.9%、51.2%、16.3%。"
conclusion: HiFi-ST统一了离散测量与连续表达场重建，支持下游免疫分析，为肿瘤微环境研究提供新工具。
---

## 摘要
空间转录组学刻画了组织尺度的基因表达模式，但其观测数据是底层连续分子场的稀疏离散样本，导致空间混叠和亚分辨率信息丢失。现有方法通常将该任务建模为斑点级点回归，难以同时捕捉表达连续性和观测的区域性。为此，我们提出HiFi-ST，一种用于连续空间转录组建模的条件神经场框架。HiFi-ST将空间基因表达预测建模为连续表达场学习，将每个斑点视为有限支撑域上的区域观测，通过蒙特卡洛采样近似局部积分，并整合多尺度组织特征提取与基于FiLM的条件调制，以改进对复杂空间异质性的建模以及与底层测量过程的一致性。在三个独立数据集（HER2+、cSCC和Alex_NatGen）上的系统评估显示，HiFi-ST在关键指标上优于mclSTExp、BLEEP、THItoGene、His2ST和HisToGene。在HER2+上，HiFi-ST的平均PCC提高了65.1%，平均MSE降低了40.9%；在cSCC上，PCC提高了10.2%，MSE降低了51.2%；在Alex_NatGen上，PCC提高了80.0%，MSE降低了16.3%。此外，学习到的多尺度组织表征支持下游空间免疫分析，包括辅助识别候选TLS区域。总体而言，HiFi-ST提供了一个统一框架，桥接离散测量与连续表达场重建，用于肿瘤微环境分析和空间免疫结构表征。

## Abstract
Spatial transcriptomics characterizes tissue-scale gene expression patterns, yet its observations are sparse discrete samples of an underlying continuous molecular field, leading to spatial aliasing and sub-resolution information loss. Existing methods usually formulate this task as spot-level point regression, making it difficult to capture both expression continuity and the regional nature of observation. Here, we propose HiFi-ST, a conditional neural field framework for continuous spatial transcriptomics modeling. HiFi-ST formulates spatial gene expression prediction as continuous expression field learning, models each spot as a regional observation over a finite support domain, approximates local integration through Monte Carlo sampling, and integrates multiscale tissue feature extraction with FiLM-based conditional modulation to improve modeling of complex spatial heterogeneity and consistency with the underlying measurement process. Systematic evaluation on three independent datasets (HER2+, cSCC, and Alex_NatGen) showed that HiFi-ST outperformed mclSTExp, BLEEP, THItoGene, His2ST, and HisToGene on key metrics. On HER2+, HiFi-ST achieved an average PCC improvement of 65.1% and an average MSE reduction of 40.9%; on cSCC, PCC improved by 10.2% and MSE decreased by 51.2%; on Alex_NatGen, PCC improved by 80.0% and MSE decreased by 16.3%. In addition, the learned multiscale tissue representations supported downstream spatial immunoanalysis, including assisted identification of candidate TLS regions. Overall, HiFi-ST provides a unified framework bridging discrete measurements and continuous expression field reconstruction for tumor microenvironment analysis and spatial immune structure characterization.