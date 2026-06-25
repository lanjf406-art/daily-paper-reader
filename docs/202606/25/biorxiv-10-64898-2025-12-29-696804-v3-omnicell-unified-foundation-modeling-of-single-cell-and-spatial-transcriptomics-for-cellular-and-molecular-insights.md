---
title: "OmniCell: Unified Foundation Modeling of Single-Cell and Spatial Transcriptomics for Cellular and Molecular Insights"
title_zh: OmniCell：单细胞与空间转录组学的统一基础建模，用于细胞和分子洞察
authors: "Pang, J., Qiu, P., He, Y., Deng, Y., Tang, W., Zhi, H., Yan, J., Li, B., Lin, A., Cao, L., Teng, F., Fang, S., Li, S., Deng, Z., Zhang, Y., Li, Y., Xu, X."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.64898/2025.12.29.696804v3.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 单细胞转录组基础模型，适用于耐药研究
tldr: 细胞转录程序受组织环境调控，但现有单细胞和空间转录组数据各自受限。本文OmniCell在6700万细胞和空间谱上预训练，整合基因身份、表达量和组织环境，跨尺度组织转录组。该模型恢复细胞类型程序、改进空间重建，在肝癌中识别肿瘤-正常过渡区，并通过虚拟扰动映射调控基因。结果表明组织环境是转录组表示的主要轴线。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有模型未充分考虑组织环境对细胞转录程序的影响。
method: 预训练于6700万单细胞与空间转录组数据，整合基因身份、表达量和组织环境。
result: 恢复细胞类型程序，改进空间重建，在肝癌中识别肿瘤过渡区，虚拟扰动映射调控基因。
conclusion: 组织环境是转录组表示的核心轴线，提供研究程序上下文依赖意义的新框架。
---

## 摘要
细胞的转录程序不仅仅由基因表达来完全定义，而且还由该程序所处的组织环境所定义。单细胞RNA测序在解离后解析分子身份，而空间转录组学则保留了组织结构，但仍受限于实验特异性的稀疏性和基因覆盖度。在此，我们提出OmniCell，一个基于组织背景的转录组基础模型，该模型在6700万个解离和空间解析的谱上进行了预训练。通过整合基因身份、表达水平和组织背景，OmniCell将转录程序与其运作的细胞邻域和解剖背景联系起来。OmniCell在分子、细胞和组织尺度上组织了转录组。它恢复了细胞类型特异性程序和与组织对齐的基因模块，跨批次、物种和稀有群体保持了稳健的细胞状态结构，并改进了空间细胞身份、解剖区域和细胞类型组成的重建。在人肝癌Stereo-seq数据中，OmniCell解析了一个以免疫浸润、急性期炎症、凝血/补体活性和金属硫蛋白相关的金属离子解毒为特征的肿瘤-边缘过渡区。背景基因嵌入相似性分析显示，基因关系在肿瘤核心、过渡区和瘤旁/邻近非恶性微环境中存在差异，表明OmniCell捕获了组织依赖的基因功能，而不仅仅是表达相似性。在小鼠大脑发育和猕猴皮层中，空间虚拟扰动将调控基因映射到阶段和区域特异性解剖程序上。总之，这些结果确立了组织背景作为转录组表征的一个主轴，并提供了一个研究细胞程序如何在完整组织中获得背景依赖性生物学意义的框架。

## Abstract
A cells transcriptional programme is not fully defined by gene expression alone, but by the tissue context in which that programme is enacted. Single-cell RNA sequencing resolves molecular identity after dissociation, whereas spatial transcriptomics preserves tissue architecture but remains constrained by assay-specific sparsity and gene coverage. Here we present OmniCell, a tissue-contextual transcriptomic foundation model pretrained on 67 million dissociated and spatially resolved profiles. By integrating gene identity, expression magnitude and tissue context, OmniCell links transcriptional programmes to the cellular neighbourhoods and anatomical contexts in which they operate. OmniCell organised transcriptomes across molecular, cellular and tissue scales. It recovered cell-type-specific programmes and tissue-aligned gene modules, preserved robust cell-state structure across batches, species and rare populations, and improved the reconstruction of spatial cell identity, anatomical domains and cell-type composition. In human liver cancer Stereo-seq data, OmniCell resolved a tumour-margin transition zone characterised by immune infiltration, acute-phase inflammation, coagulation/complement activity and metallothionein-linked metal-ion detoxification. Contextual gene-embedding similarity analysis showed that gene relationships differed across tumour core, transition-zone and paratumour/adjacent non-malignant niches, indicating that OmniCell captures tissue-dependent gene function rather than expression similarity alone. In mouse brain development and macaque cortex, spatial virtual perturbations mapped regulatory genes onto stage- and region-specific anatomical programmes. Together, these results establish tissue context as a primary axis of transcriptomic representation and provide a framework for studying how cellular programmes acquire context-dependent biological meaning in intact tissues.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义
- **研究动机**：单细胞RNA测序（scRNA-seq）在解离后解析分子身份，但丢失了组织结构信息；空间转录组学（ST）保留组织架构，却受限于实验特异性的稀疏性和基因覆盖度。现有基础模型未充分考虑 **组织环境** 对细胞转录程序的调控作用。
- **整体含义**：细胞的转录程序不仅由基因表达决定，还取决于其所在的 **组织邻域和解剖背景**。OmniCell 将组织环境作为转录组表征的主轴，为理解细胞程序如何在完整组织中获得上下文依赖的生物学意义提供了新框架。

## 2. 论文提出的方法论
- **核心思想**：构建一个基于组织背景的转录组基础模型，同时整合 **基因身份（gene identity）**、**表达量（expression magnitude）** 和 **组织环境（tissue context）**，将转录程序与细胞邻域和解剖背景联系起来。
- **关键技术**：
  - 在 **6700 万个解离与空间解析的谱（profiles）** 上进行大规模预训练。
  - 模型能够跨 **分子、细胞和组织** 三个尺度组织转录组，恢复细胞类型特异性程序和组织对齐的基因模块。
  - 通过 **背景基因嵌入相似性分析**（contextual gene-embedding similarity）揭示组织依赖的基因功能关系。
  - 支持 **空间虚拟扰动**（virtual perturbations），将调控基因映射到阶段/区域特异性解剖程序。
- **算法流程**（文字说明）：输入数据包含基因身份、表达量及对应的空间位置/组织区域 → 模型在统一框架下学习基因-细胞-组织的联合表示 → 输出可用于细胞身份重建、空间域识别、组成推断以及扰动效应映射。

> 注意：摘要中未提供具体的模型架构细节（如Transformer、注意力机制等）及损失函数公式。

## 3. 实验设计
- **使用的数据集**：预训练数据包含约 6700 万个解离和空间解析的转录组谱（来源包括多物种、多组织），具体数据集名称未在摘要中列出。下游评估包括：
  - 人肝癌 **Stereo-seq** 空间转录组数据（10x Visium 类似技术）。
  - 小鼠大脑发育数据（可能为小鼠脑发育 scRNA-seq 或 ST）。
  - 猕猴皮层数据（可能为空间转录组学或单细胞数据）。
- **Benchmark 任务**：
  - 跨批次、跨物种、稀有群体的细胞状态结构保持能力。
  - 空间细胞身份、解剖区域、细胞类型组成的重建精度。
  - 基因模块的组织对齐性。
  - 虚拟扰动对解剖程序的映射效果。
- **对比方法**：摘要未明确列出对比的方法名称，但推测应与现有单细胞基础模型（如 scBERT、Geneformer）、空间分析方法（如 SpaGCN、STARmap 处理流程）进行了比较。

## 4. 资源与算力
- **摘要中未明确说明** 使用的 GPU 型号、数量或训练时长。仅提及在 6700 万谱上进行了预训练，计算规模较大但具体细节缺失。

## 5. 实验数量与充分性
- **实验数量**：涉及多个任务场景：
  - 细胞类型程序恢复与基因模块提取。
  - 跨批次/物种/稀有群体鲁棒性验证。
  - 空间重建（细胞身份、区域、组成）。
  - 人肝癌肿瘤-边缘过渡区解析。
  - 两个独立的虚拟扰动案例（小鼠大脑发育、猕猴皮层）。
- **充分性评价**：实验覆盖了分子、细胞、组织三个尺度，并包含实际生物学发现（如肝癌过渡区的免疫-急性期特征），具有一定充分性。但摘要未提及 **消融实验**（如去掉组织背景、不同预训练数据规模的影响），也未给出定量对比表格或统计检验细节，完整性受限。

## 6. 论文的主要结论与发现
- **核心发现**：组织背景是转录组表征的 **主轴**，OmniCell 捕获的是组织依赖的基因功能，而非仅表达相似性。
- **具体生物学结果**：
  - 在人肝癌中成功解析 **肿瘤-边缘过渡区**，特征为免疫浸润、急性期炎症、凝血/补体活性及金属硫蛋白介导的金属离子解毒。
  - 空间虚拟扰动验证了调控基因在发育阶段（小鼠大脑）和脑区（猕猴皮层）的特异性解剖程序映射。
- **方法论结论**：OmniCell 统一了单细胞和空间转录组学，可恢复细胞类型程序、改进空间重建，并提供跨尺度转录组组织能力。

## 7. 优点
- **创新性**：首次将组织环境作为显式输入维度整合到基础模型中，打破单细胞与空间数据各自为政的局面。
- **大规模预训练**：6700 万谱为模型提供了广泛的生物学先验。
- **多任务通用性**：一个模型同时完成细胞身份重建、空间域识别、基因功能关系推断及虚拟扰动预测。
- **生物学可解释性**：背景基因嵌入相似性分析揭示了组织依赖的基因关系，可发现隐藏的生物学机制（如肿瘤过渡区特征）。

## 8. 不足与局限
- **实验覆盖局限**：预训练数据集的物种、组织类型、技术平台的具体分布未交代，可能存在偏倚。
- **对比方法缺失**：未明确列出基线方法名称及详细定量比较，难以直接判断性能提升幅度。
- **消融实验不充分**：缺少对组织背景模块、不同数据融合策略的消融验证。
- **可解释性评估不足**：模型内部表示的可解释性（如注意力权重是否对应生物学通路）未在摘要中讨论。
- **计算资源未报告**：无法评估方法复现的门槛与效率。
- **部署限制**：医疗/临床应用中，模型对特定疾病（如肝癌）的泛化能力仍待更大规模独立验证。

（完）
