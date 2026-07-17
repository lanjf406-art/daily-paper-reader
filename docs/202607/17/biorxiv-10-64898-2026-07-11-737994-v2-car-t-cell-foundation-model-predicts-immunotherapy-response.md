---
title: CAR T cell foundation model predicts immunotherapy response
title_zh: CAR T细胞基础模型预测免疫治疗反应
authors: "Li, Y., Fang, D., Mao, C., Wu, X., Luo, Y."
date: 2026-07-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.11.737994v2.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 利用单细胞转录组和超图注意力机制的基础模型预测免疫治疗反应，可用于耐药预测
tldr: 单细胞转录组数据揭示了CAR T细胞状态，但如何将其转化为患者治疗反应预测仍是挑战。本文提出gANCHOR，一种基于层次超图注意力的T细胞基础模型，通过编码基因-通路关系学习通路感知细胞嵌入，并利用细胞到患者注意力模块聚合信息预测免疫治疗反应。在161名患者中预测F1达0.87，优于现有模型，同时识别出可重复的反应相关基因程序，提供了可解释的生物学见解。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1463, \"height\": 1455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1520, \"height\": 1832, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1517, \"height\": 1331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-11-737994-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1515, \"height\": 1315, \"label\": \"Figure\"}]"
motivation: 现有单细胞研究主要识别反应相关基因或细胞群，缺乏整合基因结构与临床结果的预测框架。
method: gANCHOR采用层次超图注意力框架，结合生物学先验编码基因-通路关系，学习通路感知细胞嵌入，并通过注意力聚合推断患者反应。
result: 在五项CAR T研究的161名患者中，gANCHOR的F1分数达0.87，在生物学保守性和批次校正评估中均最优。
conclusion: gANCHOR可有效预测CAR T细胞治疗反应，并揭示响应与耐药相关的可解释基因程序。
---

## 摘要
单细胞转录组学解析了CAR T细胞的状态，然而将异质性细胞信号转化为患者水平的治疗反应仍具挑战。现有研究主要通过实验和统计分析识别反应相关基因或细胞群，但很少有预测框架将基因级结构与临床结果整合。在此，我们提出gANCHOR，一个基于分层超图注意力框架的T细胞基础模型，结合了生物学信息表示学习和患者水平反应预测。通过编码基因-通路关系，gANCHOR学习通路感知的细胞嵌入，提高了生物学保守性和批次鲁棒性。然后，一个细胞到患者的注意力模块聚合细胞信息以推断治疗反应。在基准数据集上，gANCHOR在生物学保守性和批次校正评估中取得了最强的整体性能。在来自五项CAR T细胞研究的161名患者的反应预测中，gANCHOR达到了0.87的F1分数，优于基准的单细胞基础模型。gANCHOR还识别了可重复的反应和非反应相关基因程序，为CAR T细胞疗效和耐药性提供了可解释的生物学见解。

## Abstract
Single-cell transcriptomics resolves CAR T-cell states, yet translating heterogeneous cellular signals into patient-level therapeutic response remains challenging. Existing studies primarily identify response-associated genes or cell populations through experimental and statistical analyses, but few predictive frameworks integrate gene-level structure with clinical outcomes. Here, we present gANCHOR, a T-cell foundation model built on a hierarchical hypergraph attention framework combining biologically informed representation learning with patient-level response prediction. By encoding gene-pathway relationships, gANCHOR learns pathway-aware cell embeddings that improve biological conservation and batch robustness. A cell-to-patient attention module then aggregates cellular information to infer therapeutic response. Across benchmark datasets, gANCHOR achieved the strongest overall performance in biological conservation and batch-correction assessments. In response prediction across 161 patients from five CAR T-cell studies, gANCHOR achieved an F1 score of 0.87, outperforming benchmarked single-cell foundation models. gANCHOR also identified reproducible response- and non-response-associated gene programs, providing interpretable biological insights into CAR T-cell efficacy and resistance.

---

## 论文详细总结（自动生成）

### 论文总结：CAR T细胞基础模型预测免疫治疗反应

#### 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：如何从单细胞转录组数据（scRNA-seq）有效预测CAR T细胞免疫治疗的临床反应？现有研究大多为描述性分析，识别与反应相关的基因或细胞群体，但缺乏能够整合基因结构信息与临床结局的预测性框架。
- **背景**：CAR T疗法对部分血液肿瘤有显著疗效，但患者间反应差异大（缓解 vs. 复发/毒性）。单细胞RNA测序虽能高分辨率解析T细胞异质性（如记忆、耗竭状态），但尚未被有效用于构建预测模型，现有单细胞基础模型也主要在细胞类型分类等任务上评估，未直接用于患者水平治疗反应预测。
- **整体含义**：通过构建融合生物学先验（基因-通路关系）与深度学习架构的模型，弥合单细胞分子特征与临床预后之间的鸿沟，实现个性化免疫治疗预测及可解释的生物标志物发现。

#### 2. 方法论：核心思想、关键技术细节与流程
- **核心思想**：gANCHOR（graph Attention Network for CAR-T Hierarchical Outcome Reasoning）采用两模块层次架构，先学习生物学信息丰富的细胞嵌入（模块I），再通过注意力机制聚合细胞信息预测患者反应（模块II）。
- **关键技术细节**：
  - **模块I（基础模型）**：
    - **超图注意力编码**：利用MSigDB C2基因集构建基因-通路二分超图（基因节点，通路超边）。通过双重注意力机制（基因→通路→基因）交换信息，生成通路感知的基因嵌入。
    - **表达融合**：将原始基因表达值与基因嵌入逐元素相乘，输入堆叠的超图注意力块（共6层），得到基因级细胞表示。
    - **细胞池化**：采用表达感知的注意力池化，仅对表达非零的基因加权求和，得到细胞嵌入。
    - **多任务训练**：联合优化细胞类型分类（交叉熵）、基因表达重建（均方误差）、对抗性批次去偏（梯度反转层），损失权重分别为 \( w_1=1, w_2=1, w_3=0.35 \)，梯度反转系数 \(\gamma=1\)。
  - **模块II（患者反应预测）**：
    - 固定模块I的编码器参数，使用细胞嵌入作为输入。
    - **细胞-患者注意力**：可学习的注意力向量 \(w\) 计算每个细胞对患者的贡献权重，加权求和得到患者嵌入 \(Z_{pd}\)。
    - **分类**：患者嵌入输入多层感知机（MLP），输出响应/非响应概率，采用加权交叉熵损失（非响应:响应=3:1）应对类别不平衡。
- **训练流程**：两阶段独立训练。模块I预训练10 epoch，优化器Adam，初始学习率1e-5，权重衰减1e-4，批量大小64，dropout 0.2，嵌入维度128。模块II超参数网格搜索（学习率1e-5~1e-2，权重衰减1e-4~1e-2），根据验证集F1选择最优配置，每个超参数组合运行4次。

#### 3. 实验设计
- **数据集**：
  - **预训练数据**：约180万T细胞和CAR T细胞，来自12个已发表数据集（包括CZ CELLxGENE中的7个参考T细胞图谱+5个CAR T临床研究）。
  - **反应预测数据**：5个独立CAR T研究（Deng 2020, Haradhvala 2022, Wilson 2022, Bai 2022, Bai 2024），共161名患者（120响应，41非响应）。所有样本均为治疗前输注产品单细胞数据。
- **基准（Benchmark）**：
  - 细胞嵌入质量对比方法：4种批次校正方法（Combat, MNN, scVI, Scanorama）+5种单细胞基础模型（Geneformer, scGPT, scMulan, scFoundation, GenePT）。
  - 患者反应预测对比方法：上述所有模型+原始基因表达（作为嵌入基线）+基因表达均值聚合+逻辑回归（细胞层级消除基线）。
- **评估指标**：
  - 细胞嵌入：生物学保守性（孤立标签分数、NMI、ARI、细胞类型ASW、cLISI）和批次校正（批次ASW、iLISI、kBET、图连通性、PCR对比）。
  - 反应预测：主要指标为二分类F1分数，辅以精确率、召回率、AUROC、AUPRC；统计显著性通过置换检验（10,000次）评估。

#### 4. 资源与算力
- 文中仅说明模型使用PyTorch实现，并在NVIDIA GPU上训练，但**未明确给出GPU型号、数量及总训练时长**。模块I预训练10 epoch，模块II训练依赖超参数网格搜索（每配置4次运行），整体训练成本中等，具体算力需求未知。

#### 5. 实验数量与充分性
- **实验数量**：
  - 细胞嵌入质量基准：对比10种方法，使用多维度指标（5个生物学+5个批次校正）。
  - 患者反应预测：对比10种方法（含两种消融基线），每个模型4次重复运行，共计约44组主实验。
  - 消融实验：随机打乱通路分配分析（验证通路先验重要性）、聚合基线（验证细胞层级必要性）、注意力特征空间分析（对比传统差异表达）。
  - 可重复性验证：4次独立运行识别DAEGs，仅保留100%一致的基因（响应组59个，非响应组65个）。
- **充分性与公平性**：所有对比模型使用相同的下游预测框架（模块II）和相同的训练/测试划分（患者级分层，避免信息泄露）；超参数均针对各方法独立优化；消融实验设计合理。实验覆盖了嵌入质量、预测性能、可解释性、鲁棒性等多个维度，充分性较好。

#### 6. 主要结论与发现
- **预测性能**：gANCHOR在患者反应预测中F1分数达0.87，显著优于所有对比模型（置换检验p<0.05），且变异最小；原始基因表达或聚合基线远低于嵌入方法，证明表示学习与细胞层级建模的关键作用。
- **嵌入质量**：gANCHOR在生物学保守性与批次校正综合排名中最高，在保持细胞类型结构的同时有效混合跨数据集样本。
- **生物可解释性**：
  - 响应组DAEGs富集记忆/干细胞相关基因（SELL, IL7R, CD27）、细胞毒性效应基因（KLRK1, FGFBP2）等，提示“功能胜任、记忆丰富”的CAR T状态。
  - 非响应组DAEGs富集耗竭标志（PDCD1, CTLA4, TIGIT）、AP-1转录因子（JUN, JUNB, FOS）、Treg标志（FOXP3），与治疗失败一致。
  - 基因向量空间：同通路基因嵌入距离显著小于随机基因集（Wilcoxon p<0.001），表明模型保留了通路级功能结构。
- **注意力与传统差异表达对比**：在患者反应分析中，注意力富集的基因更聚焦于免疫相关生物学过程，而传统差异表达基因易受批次效应干扰（如管家基因），说明注意力机制能有效抑制技术噪声。

#### 7. 优点
- **方法创新**：
  - 首次将超图注意力与植物学先验（基因-通路关系）引入单细胞基础模型，用于CAR T反应预测。
  - 层次注意力设计（基因→细胞→患者）不仅提升预测性能，还提供从分子到临床结局的完整可解释链条。
  - 对抗性批次去偏嵌入优于传统校正方法，且与下游任务适配。
- **实验设计**：
  - 严格的患者级数据划分（避免信息泄漏），统一下游框架公平比较。
  - 多重消融（通路先验、聚合基线、注意力特征）系统验证各组件贡献。
  - 多数据集整合（12个来源）且涵盖不同测序平台，增强泛化性证据。

#### 8. 不足与局限
- **方法局限**：
  - 通路注释依赖MSigDB，可能不完全或偏向已知机制，限制新功能关系发现。
  - 注意力权重反映相关性而非因果性，需实验验证。
  - 两阶段训练（先预训练模块I再训练模块II）可能未充分对齐表示学习与预测目标，未来可探索端到端或任务自适应微调。
- **实验局限**：
  - 算力资源未公开，复现成本不透明。
  - 仅使用CAR T细胞输注前数据，未纳入动态、多组学或空间信息，可能遗漏关键免疫过程。
  - 患者队列规模（161例）相对有限，且以CD19靶向为主，对其它靶点（如BCMA）或实体瘤的适用性未验证。
- **偏差风险**：
  - 不同研究的临床反应定义合并为二分类可能丢失中间状态（如部分缓解的归属）。
  - 非响应组样本量偏小（41/161），可能影响模型训练和DAEGs检测的统计效力。

（完）
