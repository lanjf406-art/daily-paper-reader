---
title: Stability-driven multi-omics integration for reproducible latent structure
title_zh: 稳定性驱动的多组学整合以实现可重复的潜在结构
authors: "Guan, H., Gerwen, M. v., Kim-Schulze, S., Colicino, E., Dolios, G., Petrick, L."
date: 2026-06-27
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.23.734064v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 稳定性驱动的多组学整合框架与肿瘤耐药生信相关
tldr: 高维多组学数据整合中采样变异性常导致发现不可重复。本文提出稳定性驱动框架，结合稀疏广义典型相关分析与重复交叉验证、样本外投影及稳定性评估。应用于甲状腺癌队列，识别出可重复的代谢组和蛋白质组潜在成分，且疾病关联与时间变化模式一致。该框架提升了多组学潜在结构的可重复性和生物推断的鲁棒性。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有多组学整合方法对采样变异性引起的不可重复性评估不足，需系统性提高潜在结构的稳定性。
method: 提出稳定性驱动框架，使用稀疏广义典型相关分析，结合重复交叉验证、样本外投影和组件级、特征级稳定性评估。
result: 在甲状腺癌队列中（n=162），识别出代谢组和蛋白质组可重复潜在成分，疾病关联与时间序列变化一致。
conclusion: 该框架提供了提高多组学整合可重复性和生物学推断鲁棒性的通用策略。
---

## 摘要
高维多组学数据整合为表征复杂生物系统提供了新的机会。尽管采样变异性经常损害研究结果的可信度，尤其是在小规模队列中，但所得潜在结构的可重复性和泛化性尚未得到充分评估。我们提出了一种稳定性驱动的多组学整合框架，该框架结合了稀疏广义典型相关分析、重复交叉验证、样本外投影以及组件级和特征级稳定性的系统评估。我们将该框架应用于甲状腺癌病例对照队列（n=162）中的非靶向代谢组学和Olink靶向炎症蛋白质组学数据。我们的稳定性驱动整合识别出可重复的代谢组学和蛋白质组学潜在成分，这些成分显示出一致的样本外疾病关联，并追踪了与诊断时间相关的时序结构变化。该框架提供了一种通用策略，用于识别可重复的潜在结构，从而提高多组学研究中生物推断的稳健性。

## Abstract
High-dimensional multi-omics data integration offers novel opportunities to characterize complex biological systems. Even though sampling variability frequently compromises findings, particularly in small cohorts, the reproducibility and generalizability of the derived latent structures are insufficiently evaluated. We propose a Stability-driven framework for multi-omics integration that combines sparse generalized canonical correlation analysis with repeated cross-validation, out-of-sample projection, and systematic evaluation of both component-level and feature-level stability. We apply this framework to untargeted metabolomic and Olink targeted inflammation proteomic profiles in a thyroid cancer case-control cohort (n = 162). Our Stability-driven integration identified reproducible metabolomic and proteomic latent components that showed consistent out-of-sample disease associations and tracked temporally structured changes relative to time to diagnosis. The proposed framework provides a generalizable strategy for identifying reproducible latent structures that improve robustness of biological inference in multi-omics studies.