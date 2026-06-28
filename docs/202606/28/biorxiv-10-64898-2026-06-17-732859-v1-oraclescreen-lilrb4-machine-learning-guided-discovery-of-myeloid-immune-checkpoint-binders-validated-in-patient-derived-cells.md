---
title: "OracleScreen-LILRB4: Machine Learning-Guided Discovery of Myeloid Immune Checkpoint Binders Validated in Patient-Derived Cells"
title_zh: OracleScreen-LILRB4：机器学习引导发现髓系免疫检查点结合物并在患者来源细胞中验证
authors: "Abdel-Rahman, S., Gabr, M."
date: 2026-06-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.17.732859v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 机器学习发现髓系免疫检查点结合剂直接应对免疫治疗耐药
tldr: "免疫检查点小分子发现因蛋白界面平坦、常规筛选命中率低而困难。本文提出OracleScreen-LILRB4集成机器学习框架，基于定量生物物理数据训练回归模型，前瞻筛选45760个化合物，实验验证命中率28.5%，富集15倍，获得16个纳摩尔级先导化合物。ORS-22和ORS-14在患者来源癌细胞共培养中恢复抗肿瘤免疫活性。该框架有效加速非酶促免疫检查点小分子发现。"
source: biorxiv
selection_source: fresh_fetch
motivation: 克服免疫检查点小分子发现中蛋白相互作用界面平坦、常规筛选命中率低的挑战。
method: 构建集成机器学习框架，基于两个化合物库的定量ΔFnorm数据训练回归模型，预测结合亲和力。
result: "前瞻虚拟筛选命中率28.5%，富集15倍，16个化合物达纳摩尔级亲和力，先导化合物ORS-22/ORS-14在患者来源细胞中恢复免疫活性。"
conclusion: OracleScreen-LILRB4有效加速非酶促免疫检查点小分子发现，为类似靶点提供通用框架。
---

## 摘要
鉴定免疫检查点蛋白的小分子调节剂仍然是药物发现中的重大挑战，因为蛋白质-蛋白质相互作用界面平坦且无特征，并且传统高通量筛选活动中观察到的命中率通常较低。在此，我们报告了OracleScreen-LILRB4，这是一个集成机器学习框架，基于两个结构多样的化合物库（总共19,800种化合物）针对髓系免疫检查点白细胞免疫球蛋白样受体B4（LILRB4/ILT3）进行定量生物物理筛选数据训练。通过将结合预测制定为回归任务，针对连续的ΔFnorm值而非二元命中分类，OracleScreen-LILRB4在骨架感知交叉验证下实现了平均Spearman R为0.61和ROC-AUC为0.86。对包含45,760种化合物的库进行前瞻性虚拟筛选，并对排名前200的预测进行实验验证，获得了28.5%的命中率，比基线富集了15.0倍，其中16种化合物显示出纳摩尔亲和力的LILRB4 (ILT3)结合。先导化合物ORS-22和ORS-14在患者来源的结直肠癌和急性髓系白血病共培养系统中恢复了抗肿瘤免疫活性，逆转了SCG2介导的免疫抑制并恢复了细胞毒性T细胞功能。这些发现确立了OracleScreen-LILRB4作为加速针对非酶免疫检查点靶点的小分子发现的有效计算框架。

## Abstract
The identification of small molecule modulators of immune checkpoint proteins remains a significant challenge in drug discovery due to the flat, featureless nature of protein-protein interaction interfaces and the characteristically low hit rates observed in conventional high-throughput screening campaigns. Here we report OracleScreen-LILRB4, an ensemble machine learning framework trained on quantitative biophysical screening data from two structurally diverse compound libraries (19,800 compounds total) screened against the myeloid immune checkpoint leukocyte immunoglobulin-like receptor B4 (LILRB4/ILT3). By formulating binding prediction as a regression task targeting continuous {Delta}Fnorm values rather than binary hit classifications, OracleScreen-LILRB4 achieved a mean Spearman R of 0.61 and ROC-AUC of 0.86 under scaffold-aware cross-validation. Prospective virtual screening of a 45,760-member compound library and experimental validation of the top 200 predictions yielded a 28.5% hit rate, representing a 15.0-fold enrichment over baseline, with 16 compounds demonstrating nanomolar-affinity LILRB4 (ILT3) engagement. Lead compounds ORS-22 and ORS-14 restored anti-tumor immune activity across patient-derived colorectal cancer and acute myeloid leukemia co-culture systems, reversing SCG2-mediated immunosuppression and recovering cytotoxic T-cell function. These findings establish OracleScreen-LILRB4 as an effective computational framework for accelerating small molecule discovery against non-enzymatic immune checkpoint targets.

Graphical abstract

O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=99 SRC="FIGDIR/small/732859v1_ufig1.gif" ALT="Figure 1">
View larger version (48K):
org.highwire.dtl.DTLVardef@1ef70a9org.highwire.dtl.DTLVardef@cd976dorg.highwire.dtl.DTLVardef@1907ebforg.highwire.dtl.DTLVardef@1716aec_HPS_FORMAT_FIGEXP  M_FIG C_FIG

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：免疫检查点蛋白（如 LILRB4/ILT3）的小分子调节剂发现面临两大难题：  
  - 蛋白-蛋白相互作用（PPI）界面平坦、缺乏特征，传统高通量筛选（HTS）命中率极低（通常低于 0.3%-2%）。  
  - 髓系免疫检查点 LILRB4 在多种肿瘤（结直肠癌、急性髓系白血病等）中介导免疫抑制，但现有治疗以抗体为主，小分子研究匮乏。  
- **整体意义**：本文提出 **OracleScreen-LILRB4**，一个基于机器学习（ML）的集成框架，通过定量生物物理筛选数据训练回归模型，实现对超大化学库的高效虚拟筛选，以加速发现 LILRB4 小分子结合物，并验证其在患者来源细胞中的免疫恢复功能。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：将结合预测建模为**回归任务**（预测连续 ΔFnorm 值），而非传统的二元分类（命中/非命中），以保留完整的定量结合信号信息，避免阈值截断导致的信息损失。  
- **关键技术细节**：  
  - **分子表征**：扩展连通性 Morgan 指纹（半径=2，1024 bits）+ 10 个理化描述符（分子量、脂溶性 cLogP、氢键供/受体数、拓扑极性表面积、可旋转键数、芳香环数、sp3 碳分数、杂原子数、环数）。  
  - **集成模型**：随机森林（Random Forest）、XGBoost、梯度提升（Gradient Boosting）三个互补算法，预测结果取平均得到共识集成分数。  
  - **训练数据**：两个 Enamine 化合物库（PPI 库 15,000 个、免疫聚焦库 4,800 个），通过 Dianthus 热迁移（TRIC）技术测量 ΔFnorm 值，共 19,800 个化合物（286 个阳性结合物，1.44% 命中率）。  
  - **评估策略**：**骨架感知五折交叉验证**（scaffold-aware cross-validation），确保同一 Murcko 骨架的化合物全部分到同一折，模拟虚拟筛选的新骨架预测场景。  
  - **SHAP 分析**：解释模型特征重要性，发现 cLogP 和芳香环数是最关键的驱动因素。  
- **算法流程**：  
  1. 训练集构建 → 2. 混合特征生成 → 3. 三个模型训练 → 4. 集成预测 → 5. 应用于 45,760 个化合物库 → 6. 选择 top 200 预测化合物 → 7. 实验验证。

### 3. 实验设计：使用了哪些数据集 / 场景，benchmark 是什么，对比了哪些方法

- **数据集**：  
  - **训练集**：Enamine PPI 库（15,000 个）和 Immunology 库（4,800 个），共计 19,800 个化合物。  
  - **虚拟筛选库**：Enamine 另一个 45,760 个化合物的库。  
  - **验证场景**：  
    - 前瞻实验验证 top 200 预测化合物（单剂量 Dianthus 筛选 → 浓度依赖 KD 测定）。  
    - 正交靶标确认：MST/TRIC 结合、细胞热转移分析（CETSA）。  
    - 功能验证：患者来源的结直肠癌（HCT116 + PBMC）和急性髓系白血病（THP-1 + PBMC）共培养体系，通过 SCG2 激活 LILRB4 模拟免疫抑制。  
- **Benchmark**：不直接对比其他方法，而是将前瞻命中率（28.5%）与基线 HTS 命中率（1.44%）比较，计算 15.0 倍富集。  
- **对比方法**：仅比较了集成内的三个子模型（Random Forest、XGBoost、Gradient Boosting）的性能。

### 4. 资源与算力：使用的 GPU 型号、数量、训练时长

- **未明确说明**。文中没有提及 GPU 型号、数量或训练时长。可以推断该模型（随机森林/梯度提升树）不需要大规模 GPU 训练，使用 CPU 即可完成。论文仅提到代码已开源于 GitHub，未提供计算环境细节。

### 5. 实验数量与充分性：实验组数、消融实验、公平性

- **实验组数**：  
  - 模型验证：5 折交叉验证，每个子模型重复 5 次，计算平均 Spearman R 和 ROC-AUC。  
  - 前瞻验证：1 次单剂量筛选（top 200 → 57 个命中），浓度依赖实验确定 16 个 KD。  
  - 正交靶标确认：MST/TRIC（5 个重复）、CETSA（5 个重复）。  
  - 功能实验：8 个患者供体重复，两组疾病模型（CRC 和 AML），两个化合物（ORS-22 和 ORS-14）加上抗体对照。  
- **消融实验**：无传统消融实验，但通过比较三个子模型性能及集成与单模型的差异，间接体现了集成优势。  
- **充分性与公平性**：  
  - 交叉验证采用了严格的骨架感知划分，避免了信息泄露，比随机分割更公平。  
  - 前瞻实验使用完全独立的化合物库，验证了实际富集能力。  
  - 功能实验使用患者原代细胞，具有临床代表性；同时包含同型对照和抗体阳性对照。  
  - 但缺乏与现有 ML 方法（如 GNN、Transformer 等）的直接比较，也缺少更广泛的化合物库交叉测试。总体而言实验设计较充分，客观性良好。

### 6. 论文的主要结论与发现

- OracleScreen-LILRB4 在骨架感知交叉验证下取得 **Spearman R = 0.61，ROC-AUC = 0.86**。  
- 前瞻虚拟筛选 45,760 个化合物，top 200 的实验命中率 **28.5%**，富集 **15.0 倍**。  
- 发现 **16 个纳摩尔级 KD 的 LILRB4 结合物**，其中 ORS-22（KD = 9.2 nM）和 ORS-14（KD = 85.2 nM）为先导化合物。  
- 在患者来源 CRC 和 AML 共培养体系中，ORS-22 和 ORS-14 恢复 IFN-γ、IL-2 分泌，增加 Granzyme B+ CD8+ T 细胞频率，降低肿瘤细胞活性，效果接近抗 LILRB4 抗体。  
- 结论：将回归型 ML 集成框架应用于生物物理筛选数据，可有效加速非酶免疫检查点的小分子发现，该框架具有通用性。

### 7. 优点：方法或实验设计上的亮点

- **回归任务设计**：使用连续 ΔFnorm 值而非二元标签，保留了更丰富的结合信号强度信息，提高了排序准确性。  
- **混合特征 + 集成学习**：Morgan 指纹结合理化描述符，三个互补模型集成，降低方差，提升鲁棒性。  
- **骨架感知交叉验证**：更严格模拟真实虚拟筛选场景，评估模型对全新骨架的泛化能力。  
- **前瞻实验验证**：不是仅靠回顾性指标，而是实际购买并测试了 top 200 化合物，证明了方法的实用性。  
- **多层级验证**：从生化结合（TRIC）、细胞靶向（CETSA）到功能（共培养）一以贯之，支持机制假设。  
- **临床相关性**：患者来源细胞共培养，直接证明小分子可逆转 LILRB4 介导的免疫抑制，具有转化潜力。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制

- **模型对比局限**：未与深度学习（如 GNN、Transformer）或其他虚拟筛选方法（如对接）比较，难以评估本方法在整体前沿中的相对地位。  
- **训练数据来源单一**：仅使用两个 Enamine 库，且均来自同一供应商，可能存在化学空间偏差，未必能泛化到其他库。  
- **前瞻验证规模有限**：仅测试了 top 200，未评估其他分数段的命中率，也未见负样本验证（预测的非结合物是否真无活性）。  
- **缺乏脱靶验证**：未测试 ORS-22/ORS-14 对其他 LILR 家族蛋白或无关靶点的选择性，有潜在的脱靶风险。  
- **功能实验浓度单一**：功能实验仅使用 1 μM 浓度，未做剂量响应分析，无法确定 EC50 是否与结合亲和力一致。  
- **算力/成本未报告**：未提供训练时间和资源，不利于复现性评价。  
- **样本量**：功能验证仅 8 位供体，虽然统计显著，但更大样本可增强结论稳健性。  
- **应用限制**：框架依赖 Dianthus 等生物物理筛选数据，并非所有靶点都容易获得该类型高质量定量数据。

（完）
