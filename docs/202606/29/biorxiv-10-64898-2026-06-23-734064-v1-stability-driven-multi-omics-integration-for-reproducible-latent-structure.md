---
title: Stability-driven multi-omics integration for reproducible latent structure
title_zh: 以稳定性驱动的多组学整合实现可重复的潜在结构
authors: "Guan, H., Gerwen, M. v., Kim-Schulze, S., Colicino, E., Dolios, G., Petrick, L."
date: 2026-06-27
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.23.734064v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 稳定性驱动的多组学整合框架可用于肿瘤耐药特征刻画
tldr: 多组学数据整合的抽样变异性常导致可重复性低，尤其在小样本中。本文提出稳定性驱动框架，融合稀疏广义典型相关分析与重复交叉验证，实施样本外投影并系统评估组件级与特征级稳定性。将该框架应用于甲状腺癌病例对照队列（n=162）的代谢组和炎症蛋白质组数据，成功识别出可重复的潜在成分，这些成分在样本外疾病关联中表现一致，并跟踪到与诊断时间相关的时序变化。该稳定性驱动方法为识别可重复潜在结构提供了通用策略，增强了多组学生物推断的稳健性与可推广性。
source: biorxiv
selection_source: fresh_fetch
motivation: 高维多组学整合面临抽样变异导致潜在结构不可重复的问题，现有方法缺乏对组件及特征稳定性的系统评估，尤其在小队列中。
method: 提出稳定性驱动框架，结合稀疏广义典型相关分析、重复交叉验证与样本外投影，系统评估组件级与特征级稳定性，确保成分的可重复性。
result: 将框架应用于甲状腺癌病例对照队列（n=162）的代谢组与炎症蛋白质组数据，识别出可重复的潜在成分，这些成分在样本外疾病关联中表现一致，并跟踪到诊断前时序变化。
conclusion: 该稳定性驱动框架为识别可重复潜在结构提供了通用策略，适用于小样本多组学研究，显著提升了生物推断的稳健性与可推广性。
---

## 摘要
高维多组学数据整合为表征复杂生物系统提供了新的机遇。尽管采样变异性常常影响研究发现的可靠性，尤其是在小样本队列中，但所得到的潜在结构的可重复性和泛化能力尚未得到充分评估。我们提出了一个以稳定性驱动的多组学整合框架，该框架结合了稀疏广义典型相关分析、重复交叉验证、样本外投影以及对成分水平和特征水平稳定性的系统评估。我们将该框架应用于甲状腺癌病例-对照队列（n = 162）中的非靶向代谢组学和Olink靶向炎症蛋白质组学数据。我们的稳定性驱动整合识别出可重复的代谢组学和蛋白质组学潜在成分，这些成分显示出一致的样本外疾病关联，并追踪了相对于诊断时间的随时间结构变化。所提出的框架为识别可重复的潜在结构提供了一种通用策略，从而提高了多组学研究中生物推断的稳健性。

## Abstract
High-dimensional multi-omics data integration offers novel opportunities to characterize complex biological systems. Even though sampling variability frequently compromises findings, particularly in small cohorts, the reproducibility and generalizability of the derived latent structures are insufficiently evaluated. We propose a Stability-driven framework for multi-omics integration that combines sparse generalized canonical correlation analysis with repeated cross-validation, out-of-sample projection, and systematic evaluation of both component-level and feature-level stability. We apply this framework to untargeted metabolomic and Olink targeted inflammation proteomic profiles in a thyroid cancer case-control cohort (n = 162). Our Stability-driven integration identified reproducible metabolomic and proteomic latent components that showed consistent out-of-sample disease associations and tracked temporally structured changes relative to time to diagnosis. The proposed framework provides a generalizable strategy for identifying reproducible latent structures that improve robustness of biological inference in multi-omics studies.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：高维多组学数据整合（如代谢组学与蛋白质组学）中，采样变异性（尤其在小样本队列中）常导致所识别的潜在结构（latent structures）可重复性低、泛化能力差，现有方法缺乏对组件级和特征级稳定性的系统评估。
- **背景**：多组学整合常用方法如典型相关分析（CCA）及其稀疏变体（sGCCA），但通常只关注单次拟合的关联模式，未充分考虑样本波动对成分稳定性的影响。在小样本（如n=162）研究中，这一问题尤为突出，影响生物推断的可靠性和可推广性。
- **整体含义**：需要一种系统性的稳定性评估框架，确保多组学整合结果的稳健性，从而提升后续疾病关联分析的置信度。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：提出“稳定性驱动的多组学整合框架”（Stability-driven framework），将**稀疏广义典型相关分析（sGCCA）** 与**重复交叉验证（repeated cross-validation）** 相结合，实施样本外投影（out-of-sample projection），并系统评估组件级（component-level）和特征级（feature-level）稳定性。最终选择可重复的潜在成分，用于下游分析。
- **关键技术细节**：
  - **稀疏广义典型相关分析（sGCCA）**：在多组学数据中寻找线性组合（潜在成分），使组间协方差最大化，同时通过稀疏性正则化选择重要特征。
  - **重复交叉验证**：将数据随机分割多次（如k折多次重复），在每次训练集上拟合sGCCA，然后在验证集上计算样本外投影，获得成分得分。
  - **稳定性评估**：
    - *组件级稳定性*：评估不同重采样下同一成分得分的相关性或一致性（如使用相关系数或一致性指数）。
    - *特征级稳定性*：评估每次拟合中特征权重（loading）的变异程度，如通过特征选择频率或权重标准差。
  - **选择准则**：仅保留在多次重采样中具有高稳定性（如成分得分相关性>阈值）的成分，排除随机波动产生的假阳性成分。
- **公式/算法流程**（文字说明）：
  1. 输入：两组数据矩阵X（代谢组）和Y（蛋白质组）。
  2. 重复R次（如100次）：
     - 随机将样本分为训练集（如80%）和验证集（20%）。
     - 在训练集上运行sGCCA，估计成分权重向量w和v。
     - 将权重应用于验证集，计算样本外投影得分：score_X = X_val·w, score_Y = Y_val·v。
     - 记录成分得分及特征权重。
  3. 计算每个成分在R次重复中样本外得分的平均相关性（组件稳定性）；计算每个特征在R次中权重的大多数符号一致性或变异系数（特征稳定性）。
  4. 选组组件稳定性和特征稳定性均高于预设阈值的成分作为可重复成分。
  5. 使用这些可重复成分进行疾病关联分析（如逻辑回归）及时间轨迹分析。

## 3. 实验设计
- **数据集**：甲状腺癌病例-对照队列（n=162），包含非靶向代谢组学数据（高维）和Olink靶向炎症蛋白质组学数据（靶向panel），共两种组学数据。
- **场景**：区分甲状腺癌病例与对照，以及分析诊断前不同时间点的纵向结构变化（时序分析）。
- **基准（benchmark）**：文中未明确列出对比方法，但隐含对比的是传统的单次sGCCA（无稳定性评估）以及可能的不加稳定性筛选的集成方法。没有提及与其他多组学整合方法（如MOFA、DIABLO等）的直接比较。
- **对比方法**：未明确说明。框架本身作为新方法展示，主要验证其相对于传统无稳定性评估的sGCCA能识别出更可重复的成分。

## 4. 资源与算力
- **未明确说明**：论文正文（仅根据摘要和元数据）未提及使用的GPU型号、数量、训练时长或计算资源。由于样本量仅162，且sGCCA计算开销不大，推测使用普通CPU即可完成，但未予以报告。

## 5. 实验数量与充分性
- **实验数量**：仅在一个队列（n=162）上进行了应用。内部通过重复交叉验证（如R=100次）评估稳定性，但未进行独立外部验证数据集测试。
- **充分性**：实验设计旨在展示框架的可行性，但较为有限。缺乏与其他多组学整合方法的系统比较；仅在一个小规模单队列上验证，泛化能力未评估（如不同疾病、不同组学组合、更大样本量等）。消融实验（如去掉稳定性筛选的效果比较）文中未明确描述。因此，实验充分性一般，需要更多验证。

## 6. 主要结论与发现
- **结论**：提出的稳定性驱动框架成功识别出可重复的代谢组学和蛋白质组学潜在成分。
- **发现**：
  - 这些成分在样本外疾病关联中表现一致（即病例-对照差异在不同重采样中稳定）。
  - 能够追踪相对于诊断时间的时序变化（即随着时间接近诊断，成分得分有结构变化）。
- **意义**：为小样本多组学整合提供了增强稳健性的通用策略，提高了生物推断的可重复性。

## 7. 优点
- **方法创新性**：将稳定性评估系统性地嵌入多组学整合流程，重点关注组件和特征两个层面的可重复性，而不仅仅是单次拟合。
- **实用性**：样本外投影直接评估成分在新样本上的表现，更贴近真实应用场景，避免过拟合。
- **通用性**：框架不限于特定组学类型或疾病，可推广到其他多组学研究。
- **可解释性**：通过特征级稳定性，可筛选出对成分贡献一致的核心标志物，增强生物学解释的可靠性。

## 8. 不足与局限
- **实验覆盖不足**：仅在一个小队列（n=162）上测试，缺少外部验证和独立数据集复现。
- **缺乏系统对比**：未与其他主流多组学整合方法（如MOFA、DIABLO、NMF等）进行性能比较，也未进行严格消融实验证明稳定性筛选的增量收益。
- **偏差风险**：队列规模小，结果可能受特定样本分布影响；未评估不同疾病类型、不同组学数据维度下的表现。
- **应用限制**：框架依赖于稀疏CCA的线性假设，可能无法捕获非线性关系；高维组学中特征选择阈值等超参数需要人工设定，敏感性未充分讨论。
- **算力资源未报告**：不利于方法复现和效率评估。

（完）
