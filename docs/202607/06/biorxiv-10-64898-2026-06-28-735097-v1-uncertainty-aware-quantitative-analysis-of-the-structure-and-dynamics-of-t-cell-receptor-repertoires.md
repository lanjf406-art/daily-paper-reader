---
title: Uncertainty-aware quantitative analysis of the structure and dynamics of T cell receptor repertoires
title_zh: 感知不确定性的T细胞受体库结构与动力学的定量分析
authors: "Kitanovski, S., Wollek, K., Hoffmann, D."
date: 2026-07-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.28.735097v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: T细胞受体库分析用于免疫应答，与免疫治疗耐药相关
tldr: 免疫受体库的多样性和动态难以量化，且测量存在噪声。本文提出ClustIRR框架，通过序列相似性构建联合图并检测社区，实现不确定性感知的贝叶斯差异性分析。该框架整合单细胞数据，成功应用于抗原响应、癌症免疫治疗和种间V(D)J重组偏差分析。ClustIRR作为开源工具提供了免疫组库结构动力学分析的可靠方案。
source: biorxiv
selection_source: fresh_fetch
motivation: 免疫受体库的多样性和动态难以量化，实验噪声影响分析准确性。
method: 提出ClustIRR，基于序列相似性构建联合图、检测社区，进行贝叶斯分析并整合单细胞表达数据。
result: 在抗原挑战、免疫治疗纵向动力学和V(D)J重组偏差中成功应用，揭示定量变化和动力学特征。
conclusion: ClustIRR是一种不确定性感知的开源工具，有效分析免疫受体库结构动力学。
---

## 摘要
免疫细胞受体库（IRR）的多样性和动力学是适应性免疫功能核心的两个因素，两者共同使得IRR难以被全面把握。此外，测量结果受各种实验噪声的影响。本文提出一个计算框架（ClustIRR），用于对IRR结构与动力学进行感知不确定性的定量分析。ClustIRR将多个重复、时间点或条件下的IRR映射到由免疫受体序列相似性诱导的联合图上，然后在联合图上检测群落（CJs）。基于这些CJs作为跨IRR的参考结构，ClustIRR接着对差异CJ占用进行贝叶斯定量分析。此外，ClustIRR整合单细胞基因表达数据，将群落扩增与转录激活特征联系起来。我们通过多个T细胞受体库的联合分析展示了ClustIRR的能力，包括以下示例应用：（1）抗原刺激引起的定量变化，（2）癌症免疫治疗期间的纵向动力学，（3）人类与小鼠库中V(D)J重组偏差，这些偏差预先使IRR适应病原体应答。ClustIRR作为开源软件可从Bioconductor存储库免费获取。

## Abstract
Diversity and dynamics of immune cell receptor repertoires (IRRs) are two factors at the functional heart of adaptive immunity that together make IRRs difficult to grasp. Moreover, measurements are compounded by various sources of experimental noise. Here we propose a computational framework (ClustIRR) for uncertainty-aware quantitative analysis of IRR structure and dynamics. ClustIRR maps multiple IRRs across replicates, time points, or conditions onto a joint graph induced by immune receptor sequence similarity. It then detects communities on the joint graph (CJs). Based on CJs as reference structures across IRRs, ClustIRR then performs quantitative Bayesian analyses of differential CJ occupancy. Additionally, ClustIRR integrates single-cell gene expression data to link community expansion with transcriptional activation signatures. We demonstrate the capabilities of ClustIRR with the joint analysis of multiple T cell receptor repertoires in several example applications: (1) quantitative changes due to antigen challenge, (2) longitudinal dynamics during cancer immunotherapy, (3) V(D)J recombination biases in human vs murine repertoires that pre-adapt IRRs for pathogen responses. ClustIRR is freely available as open source software from the bioconductor repository.