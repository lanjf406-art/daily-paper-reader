---
title: "Pillbox: A Leakage-Aware Foundation-Model Predictor and Lineage-Ceiling Diagnostic for Cancer Drug Response"
title_zh: "Pillbox: 一种针对癌症药物反应的泄露感知基础模型预测器及谱系上限诊断方法"
authors: "Hill, J. J. K., Jiao, E., Singh, S., Ghanta, A., Anders, D., Jeong, J., Ryoo, H. J."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.08.725572v2.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 预测癌症药物反应，与耐药生物标志物相关
tldr: 药物反应预测面临数据泄露和谱系主导问题。本文提出Pillbox，结合CpGPT甲基化嵌入、CLAMP药物嵌入和基因表达主成分，通过FiLM条件图注意力融合并集成梯度提升回归器。在GDSC数据集上，随机、组织盲和位点盲分割测试R²达0.78、0.77、0.76，细胞感知提升超过药物均值基线。此外，提出跨架构残差相关诊断量化特征堆饱和度，发现组织谱系主导地位，且基础模型嵌入已饱和，额外通道不提升性能。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有预测器存在数据泄露和谱系主导问题，需泄漏感知模型和特征饱和诊断方法。
method: Pillbox融合CpGPT甲基化嵌入、CLAMP药物嵌入和基因表达主成分，经FiLM图注意力处理并与梯度提升回归器集成。
result: GDSC上随机、组织盲和位点盲测试R²为0.78、0.77、0.76，细胞感知提升0.054、0.060、0.037。
conclusion: 跨架构残差相关诊断显示组织谱系主导，基础模型嵌入饱和，额外通道无效，交叉验证接近重复性上限。
---

## 摘要
我们提出了Pillbox，这是一个预测器，其流程针对六种Asiaee泄露模式进行了审计，并保留了一条残差路径（通过逐折消融实验证明在硬分割上不承担重要负荷）。我们的模型结合了CpGPT甲基化嵌入、CLAMP药物嵌入以及每折拟合的基因表达主成分，通过特征线性调制（FiLM）条件化的图注意力在STRING v12蛋白-蛋白相互作用图上进行融合。然后我们将模型与基于直方图的梯度提升回归基线进行集成。在GDSC GSE68379（987种细胞系，375种药物）上，使用种子42、7和123，集成模型在随机、组织学盲和部位盲分割上分别达到测试R²为0.78、0.77和0.76，细胞感知提升相对于药物平均基线分别为+0.054、+0.060和+0.037。作为特征堆栈饱和度的定量诊断，我们提出了跨架构残差相关性，并针对相同架构不同初始化进行了校准。在组织学盲分割上，跨架构残差相关性值为0.939，低于相同架构上限0.974约0.03，我们将这一差距解释为在当前基础模型表示之上架构选择可用的余量，并且与长期观察到的组织谱系主导细胞系药物反应的结论一致。我们整合了筛选后的突变、甲基化和药物-靶点-表达通道，但一旦基础模型嵌入到位，这些并不会改善预测。针对PRISM的跨筛选验证在Spearman相关系数0.01内匹配了GDSC-to-PRISM测量可重复性上限。

## Abstract
We present Pillbox, a predictor whose pipeline is audited against the six Asiaee leakage modes with the one residual pathway shown by per-fold ablation to be non-load-bearing on hard splits. Our model combines CpGPT methylation embeddings, CLAMP drug embeddings, and per-fold-fit gene-expression principal components which are fused by Feature-wise Linear Modulation (FiLM)-conditioned graph attention on the STRING v12 protein-protein interaction graph. Then we -ensemble the model against a histogram-based gradient boosting regressor baseline. On GDSC GSE68379 (987 cell lines, 375 drugs) across seeds 42, 7, and 123, the ensemble reaches test R2 of 0.78, 0.77, and 0.76 on random, histology-blind, and site-blind splits respectively, with cell-aware lifts above the drug-mean floor of +0.054, +0.060, and +0.037. As a quantitative diagnostic for feature-stack saturation we propose the cross-architecture residual correlation, calibrated against a same-architecture-different-initialization control. On histology-blind splits the cross-architecture value of 0.939 falls short of the same-architecture ceiling of 0.974 by approximately 0.03 in residual correlation, a gap we interpret as the headroom available to architecture choice on top of the current foundation-model representation and consistent with the long-established observation that tissue lineage dominates cell-line drug response. We integrated curated mutation, methylation, and drug-target-expression channels, but these do not improve prediction once foundation-model embeddings are in place. Cross-screen validation against PRISM matches the GDSC-to-PRISM measurement reproducibility ceiling within 0.01 Spearman.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有预测癌症药物反应的模型普遍存在**数据泄露**（如训练集和测试集共用相同细胞系或药物）和**谱系主导**（组织类型主导预测，掩盖了其他生物特征）问题，导致评估结果虚高且缺乏可解释性。
- **核心问题**：如何设计一个**泄露感知**（leakage-aware）的预测器，并开发一种**定量诊断方法**来衡量特征堆栈的饱和程度，从而揭示谱系的上限影响。
- **整体含义**：新模型 **Pillbox** 通过审计六种已知泄露模式、融合基础模型嵌入（CpGPT、CLAMP）和基因表达主成分，在严格分割下达到高预测性能。同时提出的**跨架构残差相关性**诊断表明，组织谱系主导了响应预测，且基础模型嵌入已饱和，添加额外特征不再提升性能。

## 2. 论文提出的方法论：核心思想、关键技术细节与流程

- **核心思想**：构建一个对数据泄露免疫的预测流水线，利用预训练基础模型（DNA甲基化、药物化学）嵌入作为高维特征，通过图注意力交互融合，再与梯度提升集成，最后用残差相关性诊断特征堆栈的饱和度。

- **关键技术细节**：
  1. **泄露审计**：针对 Asiaee 等人的六种泄露模式（如细胞系重叠、药物重叠、组织学盲、位点盲等）逐一审核，保留一条残差通路（经消融证明在硬分割下不承载重要负荷）。
  2. **特征融合**：
     - 细胞系特征：CpGPT 甲基化嵌入
     - 药物特征：CLAMP 化学嵌入
     - 表达特征：每折拟合的基因表达主成分（PCs）
     - 融合方式：在 **STRING v12** 蛋白-蛋白相互作用图上，使用 **FiLM（特征线性调制）** 条件化的**图注意力机制**融合上述特征。
  3. **模型集成**：将图注意力模型的输出与**基于直方图的梯度提升回归器**（如 LightGBM）进行集成。
  4. **诊断方法**：**跨架构残差相关性**：训练两个不同架构的模型（例如图注意力 vs 线性模型），计算它们预测残差的相关性，并与相同架构不同初始化的上限（0.974）比较，差值（约0.03）反映架构选择可用的余量，从而量化特征堆栈的饱和程度。

- **算法流程（文字说明）**：
  - 输入：细胞系 CpGPT 嵌入、CLAMP 药物嵌入、基因表达 PCs → 在 PPI 图上执行 FiLM-图注意力 → 生成融合表示 → 与梯度提升回归器集成 → 输出药物响应预测。
  - 同时，训练基线模型（如仅药物均值）用于计算细胞感知提升（cell-aware lift）。

## 3. 实验设计：数据集、场景、基准与对比方法

- **数据集**：
  - 主要：**GDSC GSE68379**（987 种细胞系，375 种药物）
  - 跨筛选验证：**PRISM**（用于测试 GDSC 到 PRISM 的测量可重复性上限）

- **分割场景（三种硬分割）**：
  1. 随机分割
  2. 组织学盲分割（histology-blind，训练集和测试集不共享组织类型）
  3. 位点盲分割（site-blind，训练集和测试集不共享原发位点）

- **基准（baseline）**：
  - **药物均值基线**（drug-mean floor）：对每个药物取所有细胞系响应的平均值作为预测。细胞感知提升（cell-aware lift）即模型相对于该基线的 R² 提升。

- **对比方法**：
  - 文中未显式比较其他已有预测器（如 DeepDSC、GraphDRP 等），而是通过消融实验、跨架构对比以及跨筛选验证来评估自身。主要对比的是：
    - 自身集成模型 vs 单一图注意力模型 vs 梯度提升基线
    - 相同架构不同初始化的残差相关性上限（用于诊断）
  - 此外，还对比了是否加入突变、甲基化、药物-靶点-表达通道的性能变化。

- **种子设置**：重复实验使用三个种子（42、7、123），报告平均结果。

## 4. 资源与算力

- **未明确说明**：文中未提及使用的 GPU 型号、数量、训练时长或内存等信息。仅能从模型复杂度推测（CpGPT/CLAMP 嵌入可能依赖预训练，图注意力网络在 PPI 图上训练），但具体算力需求未知。

## 5. 实验数量与充分性

- **实验数量**：
  - 三种分割 × 三个种子 → 9 组主要测试结果
  - 消融实验（逐折消融残留路径）
  - 跨架构残差相关诊断（对比相同架构不同初始化）
  - 通道消融（突变、甲基化、药物-靶点-表达通道加入后的效果）
  - 跨筛选验证（GDSC→PRISM）

- **充分性评价**：
  - **优点**：三种硬分割覆盖了不同泄露模式，消融实验验证了残差路径重要性，诊断方法具有创新性；跨筛选验证增强了结果可信度。
  - **不足**：缺少与现有前沿方法（如 DeepCDR、PaccMann、GNN-DTI 等）的定量对比；未在更多独立数据集（如 CCLE、CTRP）上验证泛化性；没有统计显著性检验（如置信区间）。整体而言，实验设计严谨但对比维度不够广。

## 6. 论文的主要结论与发现

1. **预测性能**：集成模型在随机、组织学盲、位点盲分割上的测试 R² 分别为 **0.78、0.77、0.76**；细胞感知提升分别为 +0.054、+0.060、+0.037。
2. **谱系主导**：组织学盲分割下，跨架构残差相关性为 0.939，低于相同架构上限 0.974 约 0.03，说明组织谱系特征主导了预测，架构选择仅能带来较小改善。
3. **特征饱和**：一旦 CpGPT/CLAMP 基础模型嵌入到位，额外加入突变、甲基化、药物-靶点-表达通道**不会提升预测性能**，表明基础模型嵌入已饱和。
4. **跨筛选一致性**：GDSC 到 PRISM 的跨筛选验证中，Spearman 相关系数与测量可重复性上限的差距在 0.01 以内，说明模型具有良好的泛化能力。

## 7. 优点：方法或实验设计上的亮点

- **泄露感知审计**：首次系统性地针对六种泄露模式设计流水线，确保评估的公正性。
- **定量诊断工具**：提出**跨架构残差相关性**，能定量衡量特征堆栈的饱和度和架构余量，具有方法论创新。
- **基础模型融合**：利用预训练的甲基化（CpGPT）和药物（CLAMP）嵌入，避免从零训练，提高表示质量。
- **集成策略**：图注意力与梯度提升集成，兼顾表示学习和非线性回归。
- **严格的硬分割**：组织学盲和位点盲分割更贴近真实临床场景，避免组织偏好。
- **跨筛选验证**：验证了模型在不同筛选平台间的可迁移性。

## 8. 不足与局限

- **对比不足**：未与主流方法（如 DeepDSC、GraphDRP、SE(3)等）进行公平对比，难以判断相对优势。
- **数据局限**：仅使用了 GDSC 和 PRISM，未在 CCLE、CTRP 等独立数据集上验证，可能有过拟合 GDSC 的风险。
- **未见统计检验**：未报告 R² 的置信区间或显著性水平，无法判断性能差异是否显著。
- **特征选择依赖预设**：选择 CpGPT 和 CLAMP 的理由不够充分，其他基础模型（如 DNABERT、ChemBERTa）未对比。
- **谱系主导结论的泛化性**：虽然谱系主导被广泛认知，但该诊断仅在 GDSC 上进行，其他癌种或药物类型未必适用。
- **资源与可重复性**：未公开代码或模型权重，复现困难；未说明训练耗时和硬件需求。
- **实时性限制**：基础模型嵌入计算可能较慢，不利于临床实时预测。

（完）
