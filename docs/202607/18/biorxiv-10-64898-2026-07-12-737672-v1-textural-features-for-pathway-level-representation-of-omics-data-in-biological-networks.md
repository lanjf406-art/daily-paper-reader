---
title: Textural features for pathway-level representation of omics data in biological networks
title_zh: 用于生物网络中组学数据通路级表示的纹理特征
authors: "Alexeyenko, A."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.12.737672v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 用于药物反应预测的纹理特征
tldr: 针对生物网络稀疏不规则导致纹理特征难以应用的问题，本研究提出网络适配的Haralick纹理分析方法，将基因表达数据转化为通路级特征用于药物响应预测。该方法在保持与网络富集分析（NEA）相似敏感性的同时更简单，且特征在体外和临床数据中一致，为稳健通路级生物标志物提供了新工具。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 746, \"height\": 741, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 873, \"height\": 935, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 683, \"height\": 744, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1734, \"height\": 821, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1668, \"height\": 702, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 815, \"height\": 780, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 840, \"height\": 779, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1805, \"height\": 857, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1673, \"height\": 1122, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1695, \"height\": 858, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1767, \"height\": 1627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1751, \"height\": 1041, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1702, \"height\": 1041, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1625, \"height\": 979, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-12-737672-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1713, \"height\": 865, \"label\": \"Table\"}]"
motivation: 图像纹理特征难以直接用于稀疏不规则的生物网络，需开发适用于网络结构的通路级特征提取方法。
method: 构建网络共现矩阵，计算Haralick纹理特征作为通路级基因表达概括，实现降维和药物响应预测。
result: Haralick特征与网络富集分析敏感性相当，且在体外药物筛选和临床生存分析中特征保持一致性。
conclusion: 网络Haralick特征提供了一种简单有效的通路级表征方法，具有跨平台稳健性。
---

## 摘要
50多年前，Haralick及其合著者提出了一系列灰度共生统计量，即后来众所周知的纹理特征。这些特征广泛应用于图像分析，但由于细胞网络是稀疏、不规则的图，而非规则的像素网格，它们在生物学网络中的应用仍然有限。本研究提出了一种网络自适应版本的Haralick纹理分析，用于从基因级组学图谱生成通路级特征。生成的图谱降低了维度，并可作为抗癌药物反应的候选预测因子。将这些特征的性能与原始基因表达变量以及网络富集分析（NEA）的通路特征进行比较，后者此前已被证明具有稳健性。尽管技术上比NEA简单，但Haralick特征表现出相当的敏感性。更重要的是，选定的Haralick特征在体外药物筛选和临床治疗相关的生存分析之间保持一致，支持其用于优先选择稳健的通路级药物反应相关因素的潜在用途。

## Abstract
More than 50 years ago, Haralick and co-authors proposed a family of gray-level co-occurrence statistics that became known as textural features. These features are widely used in image analysis, but their application to biological networks has remained limited because cellular networks are sparse, irregular graphs rather than regular pixel grids. This work presents a network-adapted version of Haralick texture analysis for generating pathway-level features from gene-level omics profiles. The resulting profiles reduce dimensionality and can be used as candidate predictors of anti-cancer drug response. Performance of these features is compared with original gene expression variables and with pathway features from network enrichment analysis (NEA), whose robustness has been demonstrated previously. Although technically simpler than NEA, Haralick features showed comparable sensitivity. More importantly, selected Haralick features were preserved between in vitro drug screens and clinical treatment-associated survival analyses, supporting their potential use for prioritizing robust pathway-level drug-response correlates.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **背景**：Haralick 纹理特征（基于灰度共生矩阵）在图像分析中非常成功，但生物网络（如蛋白质互作网络）是稀疏、节点度数服从幂律分布的不规则图，无法直接应用规则像素网格上的纹理分析。
- **问题**：现有通路级特征方法如网络富集分析（NEA）虽然稳健，但需要构建样本特异性的“改变基因集”（AGS），参数调优复杂。而原始基因表达特征维度高、噪声大，在跨数据集和体外到临床的迁移中稳健性差。
- **目标**：提出一种网络自适应版本的 Haralick 纹理分析，将基因表达数据转化为通路级特征，用于抗癌药物反应预测，并与 NEA 及原始基因表达进行系统比较。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：将每个通路视为基因节点的子图，把节点上的连续表达值量化为离散等级（2^t 个 bin），然后计算子图中所有边连接的两个节点等级共现的灰度共生矩阵（GLCM），再从中提取 15 种 Haralick 纹理特征（如角二阶矩、对比度、相关性、熵、方差、和平均、差熵等）作为该通路的样本级特征。
- **关键技术细节**：
  - 有两种模式：**HTF**（仅使用通路内部边）和 **HOF**（额外包括通路边界边，即一端在通路内、另一端在外）。
  - 离散化参数 t 通过优化 FDR 选择 t=3（即 8 个等级）。
  - 全局网络来自 STRING v12，取前 999,589 条高置信度边，包含 19,126 个基因节点。
  - 对每个样本、每条通路，分别构建 GLCM 并计算纹理特征，得到通路×样本的特征矩阵。
  - 与 NEA 对比：NEA 计算通路基因与样本 AGS 之间的网络链接富集度，AGS 定义为表达值最异常的基因（例如 top50/100/200 或 FDR 阈值）。

## 3. 实验设计

- **数据集与场景**：
  - **体外**：CCLE（癌细胞系 RNA-seq 表达，1377 个细胞系）、三个药物敏感性筛选（CTRP v.2、GDSC1、GDSC2），共 138 个共享药物。将细胞系按起源组织分为七个子集（breast、kidney、lung、pancreas、skin、lymphoid、myeloid）。
  - **临床**：TCGA 六大癌症队列（BRCA、LUAD、LUSC、KIRC、KIRP、SKCM、PAAD），包含 RNA-seq rsem z-score、临床分期、治疗记录和生存随访。
- **Benchmark 方法对比**：
  - 原始基因表达（GE）
  - Haralick 纹理特征（HTF/HOF，共 15 种×2 模式）
  - 网络富集分析通路级（NEA，使用不同 AGS 定义如 top50/100/200 和 FDR 阈值）
  - 网络富集分析基因节点级（GNEA，单个基因作为“通路”）
- **评估指标**：
  - **体外灵敏度**：单变量线性模型下药物响应 AUC 与特征的关联显著性（FDR 控制）。
  - **跨屏幕一致性**：对于共享药物，计算两个屏幕间 p 值的 Spearman 秩相关（协变量校正 site 或 site 特异性模型）。
  - **体外到临床保存**：TCGA 中 Cox 比例风险模型，包含“feature”主效应和“drug×feature”交互项；检查效应方向是否在体外与临床中一致（Fisher 精确检验 vs 随机置换）。

## 4. 资源与算力

- 文中**未明确说明**使用的 GPU 型号、数量或训练时长。所有计算基于 R 语言实现（NEArender v2.0 包），并启用并行化。未提及专用硬件资源如 GPU 集群。

## 5. 实验数量与充分性

- **实验规模**：
  - 首先优化离散化参数 t，在 CCLE 三个药物筛选上比较 4 种 t 值。
  - 然后对 CCLE 三个主要肿瘤类型（breast, lung, lymphoid）进行单变量 FDR 分析，每个特征类别产生大量 p 值。
  - 跨屏幕一致性：计算 138 个药物×所有特征类别的 Spearman 相关，并展示不同阈值（R>0.15~0.75）上的保存比例，包含全局（协变量）和 7 个部位特异性模型。
  - 临床分析：6 个 TCGA 队列，每个队列纳入最多 10 个药物，模型包含 stage 等协变量，分别测试 feature 主效应和交互项。
  - 体外-临床方向保存验证：Fisher 精确检验，对比实际数据与随机置换的符号一致率。
- **充分性与公平性**：
  - 覆盖了多种癌症类型、多个独立药物筛选、临床观察数据，比较了多种特征类别，实验设计较为全面。
  - **局限性**：单变量模型未探索多变量组合；未与其他通路状态量化方法（如 SPIA、PARADIGM、PROGENy）直接比较；临床数据为观察性，无法排除混杂因素；无独立外部验证集。

## 6. 主要结论与发现

- **性能相当**：Haralick 纹理特征在检测体外药物响应相关通路方面，其敏感性（FDR 控制下的显著比例）与 NEA/GNEA 相当，且显著优于原始基因表达。
- **跨屏幕稳健性**：通路级特征（HTF/HOF、NEA/GNEA）在跨药物屏幕间的一致性明显高于原始基因表达；HTF/HOF 与 NEA 之间无显著差异。
- **体外-临床保存**：选定的 HTF/HOF 特征（如 con、var、sav）在体外-临床方向保存上与 NEA 相当，而基因级特征（GNEA、GE）保存较差。效应方向一致率比随机置换高 2.2~6 倍。
- **技术优势**：Haralick 方法无需构建 AGS，直接利用连续表达值，技术更简单，且部分特征（如 sav、var）不受通路大小或节点度数影响，而 NEA 特征值与通路大小相关。

## 7. 优点

- **方法简洁**：避免了 NEA 中复杂的 AGS 定义和参数调优，直接利用网络边上的等级共现。
- **可扩展性**：可定义更多图级纹理特征，未来可结合高阶网络结构。
- **生成可解释通路级特征**：降低维度同时保留生物学意义（如“对比度”反映通路内表达异质性）。
- **跨平台稳健性**：在多个体外筛选和临床队列中表现一致，具有实际应用潜力。

## 8. 不足与局限

- **临床数据局限**：TCGA 治疗数据为观察性，可能存在治疗指征混杂（如分期之外未测量的变量），无法进行因果推断；比例风险假设未充分验证。
- **实验覆盖**：仅与 NEA 和原始基因表达比较，未与更广泛的通路活性方法（如 ssGSEA、VIPER、PROGENy 等）对比。未构建多变量预测模型并报告独立验证性能。
- **特征解释性**：部分 Haralick 特征（如 f12、f13）的生物学含义较模糊，且与通路大小存在相关性（如 den、f13），需谨慎使用。
- **跨通路可比性**：HTF/HOF 特征值在不同通路间直接比较缺乏标准化，文中提到未来需要归一化处理。
- **复现性**：所有分析基于单一全局网络（STRING v12）和特定离散化参数，在不同网络或参数下的鲁棒性尚未验证。

（完）
