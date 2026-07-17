---
title: CAR T cell foundation model predicts immunotherapy response
title_zh: CAR T细胞基础模型预测免疫治疗反应
authors: "Li, Y., Fang, D., Mao, C., Wu, X., Luo, Y."
date: 2026-07-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.11.737994v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 利用单细胞转录组和超图注意力机制的基础模型预测免疫治疗反应，可用于耐药预测
tldr: 单细胞转录组学解析CAR T细胞状态，但将异质性细胞信号转化为患者治疗反应预测仍具挑战。现有研究主要识别反应相关基因或细胞群，缺乏整合基因结构与临床结局的预测框架。本文提出gANCHOR，一个基于分层超图注意力框架的T细胞基础模型，结合生物信息表示学习与患者反应预测，在161名患者中实现0.87的F1分数，并鉴定了可重复的反应/非反应基因程序。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1463, \"height\": 1455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1520, \"height\": 1832, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1517, \"height\": 1331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1515, \"height\": 1315, \"label\": \"Figure\"}]"
motivation: 现有方法难以将单细胞异质性信号转化为患者水平的免疫治疗效果预测。
method: 提出gANCHOR，采用分层超图注意力框架，学习通路感知的细胞嵌入并通过细胞到患者注意力聚合推断反应。
result: 在161名CAR T患者中F1达0.87，优于基线单细胞基础模型；生物学保存和批次校正评估最优。
conclusion: gANCHOR实现了精准免疫治疗反应预测并提供可解释的生物学见解。
---

## 摘要
单细胞转录组学解析了CAR T细胞的状态，然而将异质性细胞信号转化为患者水平的治疗反应仍然具有挑战性。现有研究主要通过实验和统计分析识别反应相关基因或细胞群，但很少有预测框架将基因水平结构与临床结果整合。在此，我们提出gANCHOR，一个基于层次化超图注意力框架的T细胞基础模型，结合了生物学信息表示学习与患者水平反应预测。通过编码基因-通路关系，gANCHOR学习通路感知的细胞嵌入，从而改善生物学保守性和批次鲁棒性。随后，一个细胞到患者的注意力模块聚合细胞信息以推断治疗反应。在基准数据集上，gANCHOR在生物学保守性和批次校正评估中取得了最强的整体性能。在来自五项CAR T细胞研究的161名患者的反应预测中，gANCHOR达到了0.87的F1分数，优于基准的单细胞基础模型。gANCHOR还识别了可复现的反应相关和非反应相关基因程序，为CAR T细胞的疗效和耐药性提供了可解释的生物学见解。

## Abstract
Single-cell transcriptomics resolves CAR T-cell states, yet translating heterogeneous cellular signals into patient-level therapeutic response remains challenging. Existing studies primarily identify response-associated genes or cell populations through experimental and statistical analyses, but few predictive frameworks integrate gene-level structure with clinical outcomes. Here, we present gANCHOR, a T-cell foundation model built on a hierarchical hypergraph attention framework combining biologically informed representation learning with patient-level response prediction. By encoding gene-pathway relationships, gANCHOR learns pathway-aware cell embeddings that improve biological conservation and batch robustness. A cell-to-patient attention module then aggregates cellular information to infer therapeutic response. Across benchmark datasets, gANCHOR achieved the strongest overall performance in biological conservation and batch-correction assessments. In response prediction across 161 patients from five CAR T-cell studies, gANCHOR achieved an F1 score of 0.87, outperforming benchmarked single-cell foundation models. gANCHOR also identified reproducible response- and non-response-associated gene programs, providing interpretable biological insights into CAR T-cell efficacy and resistance.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：单细胞RNA测序（scRNA-seq）能够精细解析CAR T细胞的状态异质性，但如何将这些单细胞水平的分子信号转化为患者水平的免疫治疗效果预测，仍然是一个重大挑战。
- **现有方法局限**：以往研究主要依赖实验和统计方法识别与反应相关的基因或细胞亚群，缺乏能够整合基因网络结构、细胞异质性与临床结局的综合性预测框架。
- **研究意义**：构建一个能够从单细胞转录组数据中学习可迁移表示，并直接预测CAR T治疗反应的深度模型，有助于实现个性化免疫治疗、揭示反应与耐药的分子机制。

## 2. 论文提出的方法论

### 核心思想
- 提出**gANCHOR**（graph Attention Network for CAR-T Hierarchical Outcome Reasoning），一个基于**分层超图注意力框架**的T细胞基础模型。
- 通过引入**通路先验知识**（MSigDB基因-通路关系）构建超图，使模型能够学习**通路感知的基因嵌入**，进而生成生物学保留更好、批次效应更小的细胞嵌入。
- 采用**细胞到患者注意力模块**，自适应聚合单细胞信息以推断患者水平的治疗反应。

### 关键技术细节
- **模块I（基础模型）**：
  - **基因编码器**：利用MSigDB构建基因-通路二部超图，通过双注意力超图消息传递（从基因到通路，再从通路到基因）生成通路感知的基因嵌入。
  - **细胞编码器**：将基因嵌入与单细胞表达谱结合（元素级相乘），并经过6层层次化超图注意力块处理，得到最终的基因级细胞表示。
  - **多任务训练目标**：细胞类型分类损失、基因表达重建损失、以及通过梯度反转层实现的批次对抗损失（消除数据集间技术变异）。
- **模块II（患者级预测）**：
  - 固定模块I的编码器，将细胞嵌入作为输入，通过**细胞到患者注意力机制**（加权聚合）生成统一的患者表示，再由MLP进行分类。
  - 使用加权交叉熵损失应对类别不平衡（响应:非响应=3:1权重）。

### 公式/算法流程（文字描述）
1. **基因-通路超图构造**：根据MSigDB C2基因集构建二部图。
2. **基因嵌入初始化**：通过双注意力超图层（两跳）获得结构基因嵌入。
3. **融合表达值**：基因嵌入与归一化表达值经MLP后元素级相乘。
4. **层次化超图注意力编码**（每层）：
   - 基因→通路消息传递（计算通路注意力权重，聚合基因信息到通路）。
   - 通路→基因消息传递（计算基因注意力权重，将通路信息重新分布回基因）。
   - 残差连接与层归一化。
5. **细胞级池化**：仅对表达非零的基因进行注意力加权求和。
6. **多任务学习**：细胞类型分类、表达重建、批次对抗（梯度反转）。
7. **患者级预测**：固定细胞嵌入，计算细胞到患者注意力权重，加权得患者表示，MLP分类。

## 3. 实验设计

### 数据集
- **训练数据**：约180万T细胞和CAR T细胞（来自12项已发表研究，包括7个参考T细胞数据集和5个CAR T细胞数据集）。
- **患者验证数据**：161名患者（5项独立CAR T研究），其中120名响应者、41名非响应者。
- **细胞类型**：统一为12种T细胞亚型（如CD4+辅助、CD8+细胞毒性、记忆、调节性T细胞等）。

### Benchmark (对比方法)
- **批次校正方法**：Combat、MNN、scVI、Scanorama。
- **单细胞基础模型**：Geneformer、scGPT、scMulan、scFoundation、GenePT。
- **基线**：原始基因表达直接作为输入、细胞级平均表达（伪bulk）加逻辑回归。

### 评估指标
- **细胞嵌入质量**：生物学保守性（孤立标签分数、NMI、ARI、ASW、cLISI）和批次校正（批次ASW、iLISI、kBET、图连接性、PCR比较）。
- **患者级预测**：F1分数（主要指标），同时报告精确率、召回率、AUROC、AUPRC。
- **消融实验**：随机打乱基因-通路分配（破坏通路结构）、比较DAEG与DEG等。

## 4. 资源与算力

- 论文在方法部分仅说明：“All models were implemented in PyTorch and trained on NVIDIA GPUs”，但**未提供GPU的具体型号、数量、训练时长**等信息。
- 因此无法精确评估其计算资源消耗。

## 5. 实验数量与充分性

- **主要实验**：
  - 细胞嵌入质量benchmark：对比11种方法，在多个指标上评估（图2）。
  - 患者级预测：在统一下游框架下对比8种表示（包括gANCHOR、6个基础模型、原始表达），每个模型在4次不同随机初始化下运行，并做统计显著性检验（置换检验）。
  - 消融实验：通路图随机打乱（评估结构先验贡献）、直接使用基因表达、平均聚合（评估单细胞分辨率的贡献）。
  - 可解释性分析：识别DAEG，并与传统DEG比较；检查通路一致性等。
- **充分性评价**：
  - 数据集覆盖多个研究、多种疾病背景，患者数量（161）在同类研究中属较大规模。
  - 使用了严格的训练/验证/测试集划分（保持患者级独立性），多次独立运行并统计检验。
  - 消融实验设计合理，能够剥离不同组件的贡献。
  - 实验整体**充分、客观、公平**，且采用了统一的下游评估框架，避免因分类器设计差异造成偏差。

## 6. 主要结论与发现

1. **gANCHOR在细胞嵌入质量上综合最优**：在生物学保守性和批次校正的双重评估中取得最高整体得分，优于所有对比方法（包括基础模型和传统批次校正方法）。
2. **患者级反应预测显著提升**：在161名患者中达到F1=0.87，显著高于所有基线模型（置换检验p<0.05），且方差小。
3. **识别可复现的反应/非反应基因程序**：
   - 响应者基因富集于T细胞激活、记忆形成、细胞毒性（如SELL, IL7R, CD27, KLRK1）。
   - 非响应者基因富集于衰竭标志（PDCD1, CTLA4, TIGIT）、AP-1转录因子、调节性T细胞标记（FOXP3）。
4. **学习到的表示具有生物学结构**：基因嵌入中同一通路的基因距离更近；细胞嵌入能准确分类T细胞亚型；注意力得分与已知标志物高度一致。
5. **注意力机制比传统差异表达更具抗批次效应**：在强批次效应的CAR T数据中，DAEG（attention-derived）更倾向于识别生物学相关基因，而传统DEG受批次污染更严重。

## 7. 优点

- **创新性**：首次将超图注意力架构与通路先验结合，用于CAR T疗效预测，实现了从单细胞到患者水平的端到端可解释建模。
- **生物学可解释性**：层次化注意力机制（基因→细胞→患者）能够逐级追溯贡献，识别关键基因和细胞状态。
- **鲁棒性**：通过批次对抗训练和通路引导的表示学习，有效减轻批次效应，提高跨数据集泛化能力。
- **模块化设计**：基础模型与预测模型分离训练，避免过拟合于有限的临床标签，且基础模型可迁移至其他T细胞相关任务。
- **充分消融**：通过打乱通路等实验证明通路先验的重要性，而非仅仅依赖架构。

## 8. 不足与局限

- **通路注释的局限性**：依赖MSigDB现有通路，可能遗漏未知或疾病特异的基因关系，限制新发现的潜力。
- **注意力≠因果**：尽管注意力权重提示基因重要性，但不代表直接因果关系，需要实验验证。
- **两阶段训练**：基础模型与预测模型分开训练，未实现端到端优化，未来可探索任务自适应微调。
- **数据覆盖**：仅使用scRNA-seq数据，未整合多组学、空间转录组或纵向采样数据，可能丢失动态免疫过程信息。
- **样本量**：非响应者样本仅41例，类别不平衡可能影响模型对非响应者的识别鲁棒性，需要在更大、更多样化的队列中验证。
- **计算资源未明确报告**：缺少关于训练成本的可复现细节，不利于社区复现和资源评估。

（完）
