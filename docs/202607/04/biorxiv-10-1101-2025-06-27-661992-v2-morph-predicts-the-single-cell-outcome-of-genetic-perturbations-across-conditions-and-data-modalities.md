---
title: MORPH Predicts the Single-Cell Outcome of Genetic Perturbations Across Conditions and Data Modalities
title_zh: MORPH预测遗传扰动在不同条件和数据模态下的单细胞结果
authors: "He, C., Zhang, J., Dahleh, M. A., Uhler, C."
date: 2026-07-01
pdf: "https://www.biorxiv.org/content/10.1101/2025.06.27.661992v2.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 机器学习模型预测单细胞扰动结果，可应用于药物耐药预测
tldr: 建模细胞对遗传扰动的响应是计算生物学难题。MORPH框架结合差异变分自编码器与注意力机制，预测单细胞转录组和成像输出对扰动的响应。能够泛化到未见扰动、组合扰动及新细胞上下文，并推断基因相互作用网络。为扰动实验优化提供灵活工具，助力细胞程序研究和治疗应用。
source: biorxiv
selection_source: fresh_fetch
motivation: 测量所有基因扰动及组合跨细胞类型条件实验困难，需预测模型泛化数据类型。
method: 采用差异变分自编码器结合注意力机制，支持单细胞转录组和成像输出。
result: 可预测未见扰动、组合扰动及新细胞上下文响应，推断基因调控网络。
conclusion: 提供优化扰动实验的灵活工具，高效探索扰动空间，助力基础和医学研究。
---

## 摘要
建模细胞对遗传扰动的响应是计算生物学中的一个重大挑战。测量所有基因扰动及其在细胞类型和条件下的组合在实验上具有挑战性，这凸显了对能够在数据类型间泛化的预测模型的需求，以支持此任务。在此，我们提出MORPH，一个用于预测扰动变化的模块化框架。MORPH结合了基于差异的变分自编码器与注意力机制，以预测细胞对未见扰动的响应。它支持单细胞转录组学和成像输出，并能泛化到未见扰动、扰动组合以及新细胞环境中的扰动。基于注意力的框架能够推断基因相互作用和调控网络，同时学习的基因嵌入可以指导信息性扰动的设计，这在两个应用中得到了展示。总体而言，MORPH是一个用于优化扰动实验的灵活工具，能够有效探索扰动空间，以增进对细胞程序的理解，为基础研究和治疗应用提供支持。

## Abstract
Modeling cellular responses to genetic perturbations is a significant challenge in computational biology. Measuring all gene perturbations and their combinations across cell types and conditions is experimentally challenging, highlighting the need for predictive models that generalize across data types to support this task. Here we present MORPH, a MOdular framework for predicting Responses to Perturbational cHanges. MORPH combines a discrepancy-based variational autoencoder with an attention mechanism to predict cellular responses to unseen perturbations. It supports both single-cell transcriptomics and imaging outputs and can generalize to unseen perturbations, combinations of perturbations, and perturbations in new cellular contexts. The attention-based framework enables inference of gene interactions and regulatory networks, while the learned gene embeddings can guide the design of informative perturbations, as demonstrated in two applications. Overall, MORPH is a flexible tool for optimizing perturbation experiments, enabling efficient exploration of the perturbation space to advance understanding of cellular programs for fundamental research and therapeutic applications.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：在单细胞水平上，测量所有基因扰动及其组合在所有细胞类型、状态和疾病背景下的效应在实验上不可行。因此需要计算模型，能够从有限的扰动数据中泛化预测未见扰动、组合扰动以及跨细胞环境的效应。
- **整体含义**：MORPH 是一个模块化框架，旨在预测遗传扰动后的单细胞结果（转录组或成像表型），从而有效探索庞大的扰动空间、指导实验设计，并揭示基因调控网络。该工作直接回应了细胞扰动预测挑战赛（Cell Perturbation Prediction Challenge）和虚拟细胞挑战赛（Virtual Cell Challenge）等社区需求。

### 2. 论文提出的方法论
- **核心思想**：利用一个条件变分自编码器（VAE）结合交叉注意力机制，将控制细胞与先验基因嵌入联合编码，并通过最大均值差异（MMD）匹配预测的扰动细胞分布与真实扰动细胞分布，从而学习从控制细胞到扰动细胞的映射。
- **关键技术细节**：
  - **输入表示**：控制细胞向量 \( X_\emptyset \)，基因嵌入 \( v_g \)（来自 DepMap、Geneformer、GenePT 等先验知识）。
  - **架构**：
    - 两个分离的编码器（控制细胞编码器 + 基因嵌入编码器）将输入映射到潜在空间。
    - 拼接后的潜在向量作为查询（Query），与一个可学习的基因程序矩阵（Gene Program Matrix，作为 Key 和 Value）进行交叉注意力，输出注意力分数。
    - 注意力输出经残差连接和 MLP 后送入解码器，生成预测的扰动细胞 \( \hat{X}_g \)。
  - **损失函数**：
    - 控制细胞的重建损失：VAE 的 ELBO（l2 重建 + KL 散度）加上控制分布的 MMD 损失。
    - 扰动细胞的分布匹配损失：MMD(\( P(\hat{X}_g), P(X_g) \))，确保分布级对齐而非仅均值。
    - 总损失：\( \alpha L_{\text{discrep}} + \beta L_{\text{KL}} + \gamma L_{\text{hybrid recon}} \)。
  - **处理组合扰动**：通过将单基因嵌入的组合送入相同架构，实现多基因扰动的预测。
  - **可解释性**：注意力权重和基因程序矩阵可直接用于推断“扰动模块–基因程序”的二分调控网络。
- **算法流程**（文字描述）：
  1. 输入一个控制细胞和待预测基因的嵌入向量。
  2. 分别编码获得潜在表示，拼接后经交叉注意力机制，学习基因程序选择。
  3. 解码得到预测的扰动细胞向量。
  4. 训练时通过 MMD 损失（分布级）和 VAE 损失（控制重构）优化参数。
  5. 对新基因或新细胞系，直接推理或仅用控制细胞微调解码器即可迁移。

### 3. 实验设计
- **数据集与场景**：
  - **转录组数据**：Replogle et al. (K562-EG, RPE1-EG, K562-GW)，Norman et al. (K562 双基因扰动)，内部 CD8 T 细胞 Perturb-seq（73 基因 KO）。
  - **成像数据**：Carlson et al. 的光学池化屏幕（Ebola 病毒感染的 HeLa 细胞，4 种感染状态）。
  - **模拟数据**：基于已知二分网络生成基因表达数据，用于验证调控网络推断能力。
- **基准方法**：
  - 基线：控制分布、扰动均值。
  - 现有方法：GEARS、线性模型、SALT/SALT+（处理组合扰动）。
  - 消融：不同先验源（随机、Identitiy、Permuted DepMap）、无控制细胞输入、非注意力架构。
- **评估指标**：
  - 均值指标：RMSE、Pearson 相关性（delta）、Spearman 相关性（delta）、Retrieval rank。
  - 分布指标：MMD（单细胞级）。
  - 成像任务：归一化 L1 损失（状态分布），Chi-squared 检验。
  - 基因交互分类：AUC-ROC、Pearson 相关系数。
- **实验设置**：
  - 5 折交叉验证（扰动级划分）和异常分布拆分（outlier distribution split）。
  - 跨细胞系迁移：训练于 RPE1，仅用 K562 控制细胞微调。
  - 主动学习：比较随机、不确定性、覆盖度、损失预测四种采集策略，并与 GEARS 对比。
  - 消融：先验源比较、注意力必要性、基因掩蔽/库大小鲁棒性、模型容量扫描。

### 4. 资源与算力
- 论文中**未明确说明**使用的 GPU 型号、数量或具体训练时长。仅提及实现基于 PyTorch，超参数搜索细节在补充材料中（Supplemental Note 1）。从实验规模（百万级细胞、数千扰动）推断可能需要 GPU 集群，但无公开量化信息。

### 5. 实验数量与充分性
- **实验数量**：非常充分。涵盖转录组（3 个子数据集，含单/双基因扰动，基因组宽）、成像、模拟数据；涉及预测、迁移、交互、主动学习、调控网络推断等多任务；共设计了**超过 10 组主要实验**（Figure 2-7 及其补充图表）。
- **充分性与公平性**：
  - 消融完整：比较 4 种先验源、注意力 vs 拼接 MLP、不同模型容量、输入扰动等。
  - 鲁棒性测试：基因掩蔽 10%/90%、库大小缩放、随机权重模型比较。
  - 对比方法选择合理：GEARS 作为 SOTA，线性模型、SALT 等作为基线，且已考虑无法应用于成像模型。
  - 潜在偏差：部分对比（如 GEARS 无法用于成像）已说明；基因组宽数据中 MORPH 的均值指标不及简单基线（但分布指标更优），作者已给出解释。总体较客观。

### 6. 论文的主要结论与发现
- **预测能力**：MORPH 在大多数指标上优于现有方法，尤其擅长捕捉单细胞分布异质性（MMD 提升显著），对强效应扰动预测效果最好。
- **先验影响**：DepMap 嵌入（基于功能实验）表现最佳，提示扰动相关先验比大规模文本或表达先验更重要。
- **跨细胞系迁移**：仅用目标细胞系的控制细胞微调解码器即可有效迁移，但迁移难度与通路保守性相关（如代谢通路易迁移，红细胞分化通路难）。
- **组合扰动**：能预测 0/2、1/2、2/2 未见基因的组合，且在“冗余”和“增效”等非加性交互类型上显著优于 GEARS。
- **主动学习**：使用基于预测损失的自适应选择策略（learned representation）优于随机和基于先验的策略，能够更高效覆盖扰动空间。
- **调控网络推断**：注意力机制可恢复模拟数据的二分图；在真实数据中学习到的基因程序与已知标注高度对齐（AUROC ~0.95），且注意力变化能区分上下调程序。
- **应用验证**：
  - 成像数据：成功预测 Ebola 感染状态，提名 TOP10 候选基因（如 RAB7A、CCDC115）与真实数据排名高度一致。
  - T 细胞耗竭：识别出 Batf 可增加前体样 T 细胞比例，并在独立 Perturb-seq 数据中验证其效果优于 72/73 个专家挑选基因。

### 7. 优点
- **模块化与多模态**：支持转录组和成像两种输出，可扩展至其他数据模态。
- **分布级预测**：使用 MMD 匹配整个单细胞分布，而非仅平均效应，更能捕获细胞异质性。
- **可解释性**：注意力机制直接输出基因程序权重，可用于推断调控网络，且经因果理论证明可识别性（Supplemental Note 4）。
- **高效实验设计**：主动学习框架能有效减少实验次数，加速扰动空间覆盖。
- **强迁移能力**：仅需少量控制细胞即可跨细胞系泛化。
- **生物发现验证**：在两种独立应用（Ebola 病毒、T 细胞）中提名并验证了有潜力的靶标，展示实际应用价值。

### 8. 不足与局限
- **计算资源未公开**：缺乏详细的 GPU 使用信息，影响可复现性与效率评估。
- **弱效应扰动预测有限**：当大部分扰动无显著表型变化时，均值预测基线（如扰动均值）表现与 MORPH 相当甚至更优，MORPH 的优势主要体现在强效应扰动和分布指标上。
- **先验依赖**：性能高度依赖于先验知识的选择（DepMap 最佳），但 DepMap 仅覆盖部分基因和细胞系，限制了应用范围。
- **可解释性需特殊处理**：注意力机制的可解释性需移除残差连接，否则调控信号被稀释（如图 5 注释），增加了使用复杂度。
- **成像数据调控网络推断不直观**：输出为形态特征而非基因，推断的边是“扰动→表型特征”，生物意义较转录组弱。
- **跨细胞系迁移受通路差异限制**：对于高度细胞类型特异性的通路（如红细胞分化），迁移性能下降。
- **组合扰动外推上限**：仅验证了双基因组合，更复杂的多基因组合实验未涉及。

（完）
