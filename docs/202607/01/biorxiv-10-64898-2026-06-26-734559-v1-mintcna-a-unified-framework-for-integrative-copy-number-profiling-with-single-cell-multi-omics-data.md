---
title: "MintCNA: A Unified Framework for Integrative Copy Number Profiling with Single-Cell Multi-Omics Data"
title_zh: "MintCNA: 一个用于单细胞多组学数据整合拷贝数分析的统一框架"
authors: "Bao, W., Qin, F., Xiao, F."
date: 2026-07-01
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.26.734559v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 单细胞多组学拷贝数分析框架，直接针对肿瘤治疗耐药进化
tldr: 单细胞拷贝数变异（CNA）检测面临单一组学噪声大、无法利用多模态互补信息的问题。MintCNA框架整合配对scDNA-seq和scRNA-seq数据，通过注意力引导卷积自编码器去噪，并采用滑动窗口筛选与缺失调整CUSUM统计量进行多变量变点检测。在模拟和结直肠癌多组学数据上，MintCNA的CNA检测准确性优于现有单组学方法。该框架为解析肿瘤异质性和进化提供了有效的多组学整合工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有单细胞CNA工具多针对单一组学，易受噪声影响，无法充分利用多组学互补信息，亟需统一框架。
method: MintCNA结合深度学习去噪与统计建模，使用注意力卷积自编码器降噪，并基于滑动窗口和缺失调整CUSUM统计量进行多组学联合变点检测。
result: 在模拟和结直肠癌数据集上，MintCNA的CNA检测精度显著高于现有单组学方法，误差更低。
conclusion: MintCNA为单细胞多组学CNA分析提供了统一框架，有助于揭示肿瘤克隆结构和进化机制。
---

## 摘要
染色体拷贝数变异（CNA）是肿瘤演化、疾病进展和治疗耐药的关键驱动因素，识别CNA是描绘肿瘤克隆结构的重要步骤。然而，从单细胞数据中准确解析CNA图谱仍然具有挑战性。大多数现有工具每次分析一个组学层，且容易受到特定测序方法噪声的影响，限制了它们恢复共享或模态特异性CNA的能力。近年来，单细胞多组学技术能够对同一细胞中的多个分子层进行联合测序，但目前仍缺乏充分利用这种互补多模态数据进行CNA分析的计算方法。在此，我们提出一个单细胞多组学整合框架——MintCNA，一个用于从配对多组学数据中检测CNA的统一框架。MintCNA将传统统计建模与嵌入式深度学习结构相结合，以增强跨多组学的CNA分析。我们使用注意力引导的卷积自编码器进行数据去噪，并利用滑动窗口筛选和排序程序执行多变量变点检测。构建了缺失调整的CUSUM统计量，通过数据自适应投影联合聚合组学特征，以检测全基因组染色体断点。在各种模拟实验以及应用于结直肠癌多组学数据集时，MintCNA在检测准确性上始终优于现有的单一组学CNA检测工具。MintCNA提供了一个整合配对scDNA-seq和scRNA-seq的单细胞CNA工具，支持肿瘤内异质性和肿瘤演化的研究。

## Abstract
Chromosomal copy number alterations (CNAs) are key drivers of tumor evolution, disease progression and therapeutic resistance, and the identification of them is an important step to delineate tumor clonal structure. However, accurately resolving CNA landscapes from single-cell data remains challenging. Most existing tools analyze one omics layer at a time and are susceptible to assay-specific noises, limiting their ability to recover shared or modality-specific CNAs. Recent single-cell multi-omics techniques enable joint sequencing of multiple molecular layers in the same cells, yet in silico methods that fully exploit such complementary multi-modal data for CNA analysis are still missing. Here we present a single-cell multi-omics integration framework, MintCNA, a unified framework for CNA detection from paired multi-omics data. MintCNA integrates traditional statistical modeling with embedded deep learning structure to enhance CNA profiling across multi-omics. We use an attention-guided convolutional autoencoder for data denoising and perform multivariate change-point detection utilizing a sliding-window screening and ranking procedure. Missingness-adjusted CUSUM statistics are constructed which jointly aggregate omics features by a data-adaptive projection to detect genome-wide chromosomal breakpoints. Across various simulations and applications to a colorectal cancer multi-omics dataset, MintCNA consistently outperforms existing single-omics CNA callers in detection accuracy. MintCNA provides a single-cell CNA tool that integrates paired scDNA-seq and scRNA-seq, supporting the study of intra-tumor heterogeneity and tumor evolution.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：单细胞拷贝数变异（CNA）检测是解析肿瘤克隆异质性与演化关键，但现有方法多针对单一组学（如scDNA-seq 或 scRNA-seq），易受各自测序噪声影响，无法充分利用配对多组学（如scDNA-seq + scRNA-seq）的互补信息，导致CNA断点定位不准、假阳性/假阴性偏高。
- **整体含义**：本文提出**MintCNA**，一个统一框架，直接在配对单细胞DNA和RNA数据上联合检测CNA，首次将“缺失调整的多变量变点检测”与“边缘保留的注意力卷积自编码器去噪”结合，显著提升CNA检测精度，为解析肿瘤内异质性和演化提供有力工具。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：分四步：① 质量控制和标准化；② 通过**注意力引导的降噪卷积自编码器（AG-DCAE）** 增强信号质量，同时保留CNA边界（边缘保留损失）；③ 基于**滑动窗口筛选与缺失调整的CUSUM统计量**进行多组学联合变点检测；④ 用**截断高斯混合模型（TGMM）** 分配整数值拷贝数状态。
- **关键技术细节**：
  - **AG-DCAE**：1D卷积自编码器，加入卷积块注意力模块（CBAM），训练时对输入注入高斯噪声（去噪自编码器），损失函数=重建损失（MSE）+ 边缘保留惩罚（梯度差异惩罚，`λ||∇x - ∇x̂||²`），防止断点模糊。
  - **缺失调整CUSUM**：对每个候选断点位置g，以半窗宽h计算每层k的CUSUM统计量`C_{k,g}`，通过仅用观测值计算两侧均值，并用因子`√(L·R/(L+R))`调整缺失导致的方差。
  - **多变量投影**：对每个窗口，构建K×(2h+1)的CUSUM矩阵，通过ℓ₂正则化的秩1分解（交替更新）得到投影向量w（组学权重）和c（位置权重），然后计算诊断得分`D(g) = w^T C_{:,g+h}`。仅DNA时退化为单变量CUSUM。
  - **TGMM**：对片段均值建模为5类截断正态分布（缺失、丢失、中性、增加、扩增），EM算法估计，后验概率分配。
- **公式/算法流程**：见原文公式（1）‑（3）及描述，核心是交替求解`argmax_{w,c} w^T C c + λ||w||₂²`。具体细节在补充材料。

### 3. 实验设计：数据集、Benchmark、对比方法

- **模拟数据**：
  - 使用**CNAsim**生成scDNA-seq读段（不同覆盖度0.05X、0.1X、0.2X；噪声水平0、0.05、0.1；3个子克隆；hg38参考）；用**Splatter**生成配对scRNA-seq，通过CNA剂量效应（乘性因子）修改表达，并引入一致性掩码（比例0.25/0.5/0.75/1）。
  - 共9种覆盖×噪声组合×2种模态（DNA-only vs multi-omics），以及CNA大小分层（大>10Mb、中3‑10Mb、小<3Mb）。
- **真实数据**：
  - 结直肠癌**scTrio-seq2**数据集（患者CRC01），198个细胞来自原发灶（PT）、淋巴结转移（LN）、肝转移（ML）、治疗后肝转移（MP）。配对bulk WGS作为验证参考。
- **基准方法**：DNA-only模式下对比**HMMcopy、SCOPE、SCCNV、SCONCE、rcCAE、SCICoNE**（6种）；多组学模式下对比**MintCNA(DNA)（自对照）**（因为当时没有直接处理配对DNA+RNA的单细胞CNA方法）。
- **评价指标**：模拟数据用事件级F1、断点边界偏差（Mb）、bin级RMSE；真实数据用单细胞CNA与bulk参考的Pearson相关和RMSE。

### 4. 资源与算力

- 论文**未明确说明使用GPU类型、数量以及训练时长**。仅提及计算效率测量：所有方法在8 CPU核、64GB RAM的高性能集群上运行，MintCNA完成时间为28‑80分钟（与rcCAE相当，远快于SCOPE、SCONCE、SCCNV）。
- 由于AG-DCAE是浅层1D卷积网络，支持early stopping，对GPU需求不高，但具体训显卡信息缺失。

### 5. 实验数量与充分性

- **实验数量**：模拟实验涵盖**9种覆盖×噪声条件**（共9组），每组重复？文中未明确复现次数（但F1、RMSE等给出均值或分布）。额外对CNA大小进行了分层分析（3层）、不同拷贝数状态（CN1‑CN5）、一致性比例（4种）进行消融。真实数据**1个患者4个位点**，对比7种方法。
- **充分性判断**：
  - **充分**：模拟条件覆盖广泛（低/中/高覆盖度，无/中等/高噪声），且做了CNA大小、一致性等灵敏度分析，消融实验（DNA-only vs multi-omics）证明了整合RNA的收益。
  - **客观性**：所有对比方法按默认参数运行，并报告了F1、RMSE、边界偏差等多维度指标，无过度调优嫌疑。
  - **局限**：真实数据仅一个患者（CRC01），且其CNA以染色体臂级为主，未能充分测试在多组学优势（如局灶CNA）下的表现；模拟数据中RNA与CNA的关联模型比较简单（乘性因子+随机效应）。

### 6. 论文的主要结论与发现

1. **MintCNA在DNA-only模式下，F1、边界定位精度、全局RMSE全面优于6种现有方法**，尤其对小尺寸CNA（<3Mb）优势更明显。
2. **整合配对scRNA-seq进一步提高了检测准确性**，在低DNA覆盖度和局灶CNA上收益最大，即使仅25%基因反映CNA剂量效应仍有改善。
3. **AG-DCAE的去噪效果优于rcCAE的标准卷积自编码器**，能保留断点结构（如结直肠癌数据中17号染色体渐进性丢失被MintCNA保留，而rcCAE模糊）。
4. **AG-DCAE的潜在表示通过K‑means聚类可准确恢复子克隆结构**（ARI达0.92），远超PCA、t‑SNE、rcCAE。
5. **在结直肠癌真实数据中，MintCNA推断的CNA与bulk WGS高度一致（中位Pearson r=0.84），并揭示17号染色体在转移过程中逐步丢失的演化模式**。

### 7. 优点

- **方法创新**：首次将“缺失调整的多变量CUSUM”与“边缘保留注意力的卷积自编码器”结合用于单细胞多组学CNA检测。
- **框架统一**：支持纯DNA模式和多组学模式，灵活适用不同数据场景。
- **去噪与分段一体设计**：AG-DCAE既降低噪声又保留断点，有利于后续变点检测。
- **计算高效**：浅层架构+滑动窗口，运行时间合理（<80分钟），优于多个对比方法。
- **实验设计全面**：覆盖多种模拟条件、消融分析、分层分析，并在真实数据中与bulk正交验证。
- **子克隆恢复**：利用自编码器潜在表示实现高准确度聚类，提供增值输出。

### 8. 不足与局限

- **每细胞独立分割**：未利用同克隆细胞间共享断点信息，可能损失对弱信号克隆事件的敏感性（作者也指出可扩展为跨细胞联合分割）。
- **真实数据验证有限**：仅一个CRC患者，且以臂级CNA为主，未能充分展示多组学在局灶CNA上的优势。需更多肿瘤类型和更大规模验证。
- **RNA模拟简化**：Splatter+剂量效应模型未考虑RNA-seq dropout的复杂模式及CNA对表达的间接影响（如调控区域失活）。
- **未报告GPU使用细节**：无法复现训练资源需求，对潜在用户部署不够透明。
- **注意力机制的计算成本**：虽然总时间可接受，但注意力模块可能增加参数量，文中未提供消融分析（无注意力版本对比）。
- **缺失调整CUSUM的阈值选择**：依赖经验性零分布，对极端稀疏区域可能不够稳健（需补充模拟验证）。

（完）
