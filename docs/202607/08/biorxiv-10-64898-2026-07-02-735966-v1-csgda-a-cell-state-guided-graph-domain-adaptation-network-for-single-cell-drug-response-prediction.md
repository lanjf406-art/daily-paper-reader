---
title: "CSGDA: A Cell State-Guided Graph Domain Adaptation Network for Single-Cell Drug Response Prediction"
title_zh: CSGDA：一种细胞状态引导的图域自适应网络用于单细胞药物反应预测
authors: "Yan, F., Cao, X., Mao, F., You, Z., Chen, Y., Du, Z., Huang, Y.-A."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.02.735966v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 单细胞药物反应预测结合域自适应推断耐药性
tldr: "肿瘤内异质性导致复发和转移，单细胞药物响应预测面临跨域分布偏移挑战。提出CSGDA，利用细胞状态引导图域适应，将基因表达映射为功能状态并构建细胞拓扑，结合图域适应与重叠惩罚机制。在5个scRNA-seq数据集上平均ACC和AUPR提升约6%，并在跨转移顺铂数据中识别耐药关键基因。展现了解决单细胞异质性和精准医学的潜力。"
source: biorxiv
selection_source: fresh_fetch
motivation: 解决单细胞药物响应预测中因测序平台、微环境和转移进化导致的分布偏移问题。
method: CSGDA利用生物先验映射基因表达为功能细胞状态，指导结构学习构建细胞拓扑，通过图域适应和重叠惩罚机制实现跨域预测。
result: "在5个scRNA-seq数据集上平均ACC和AUPR提升约6%，并在跨转移顺铂数据中识别出耐药关键基因。"
conclusion: CSGDA有效解决单细胞异质性导致的分布偏移，提升预测准确性，助力精准医学。
---

## 摘要
瘤内异质性驱动癌症复发和转移，然而单细胞药物反应预测面临着严峻的“跨域”挑战，例如将体外模型应用于体内组织，或从原发肿瘤推断转移性耐药性。这些场景引发了由异质性测序平台、不同的组织微环境和转移性进化引起的分布偏移——现有方法很少解决这些问题。我们提出了CSGDA，一种细胞状态引导的图域自适应框架，旨在跨这些生物异质性预测药物反应。CSGDA整合生物先验知识，将基因表达映射到功能性细胞状态，指导一个结构学习模块构建稳健的细胞拓扑。为了克服分布偏移，模型采用图域自适应结合一种新颖的重叠惩罚机制。在五个scRNA-seq数据集上的广泛基准测试表明，CSGDA优于最先进的方法，在ACC和AUPR上平均提升约6%。除了预测准确性，我们还利用积分梯度有效地定位了一个具有挑战性的跨转移顺铂数据集中与耐药性相关的关键基因。这些发现突显了CSGDA在单细胞药物反应预测中的优越性能及其在解决单细胞异质性方面的潜力，为精准医学铺平了道路。

## Abstract
Intratumoral heterogeneity drives cancer recurrence and metastasis, yet single-cell drug response prediction faces severe "cross-domain" challenges, such as applying in vitro models to in vivo tissues or inferring metastatic resistance from primary tumors. These scenarios trigger distribution shifts arising from heterogeneous sequencing platforms, distinct tissue microenvironments, and metastatic evolution - problems rarely addressed by existing methods. We introduce CSGDA, a cell state-guided graph domain adaptation framework designed to predict drug responses across these biological heterogeneities. CSGDA incorporates biological priors to map gene expression into functional cell states, guiding a structure learning module to construct robust cell topology. To conquer distribution shifts, the model employs graph domain adaptation combined with a novel overlap penalty mechanism. Extensive benchmarks on five scRNA-seq datasets demonstrate that CSGDA outperforms state-of-the-art methods, achieving an average gain of ~6% in ACC and AUPR. Beyond prediction accuracy, we employed integrated gradients to effectively pinpoint key genes involved in drug resistance within a challenging cross-metastasis cisplatin dataset. These findings underscore CSGDA's superior performance in single-cell drug response prediction and its potential in resolving single-cell heterogeneity, paving the way for precision medicine.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

肿瘤内异质性（intratumoral heterogeneity）是导致癌症复发和转移的分子基础，但传统的 Bulk RNA-seq 平均化谱会掩盖关键耐药亚群。单细胞 RNA-seq（scRNA-seq）虽能提供单细胞视角，但依赖湿实验构建完整的药物反应图谱成本高昂、难以规模化。现有的单细胞药物反应预测方法（如 SCAD、scDEAL 等）主要采用“Bulk-to-Single-Cell”跨模态迁移学习范式，然而该范式面临两大挑战：

- **固有流形结构不匹配**：Bulk 数据是平滑的群体平均，而 scRNA-seq 数据是非线性非凸流形，强制对齐会淹没细微药物反应信号。
- **复杂非 I.I.D. 偏移**：测序平台、组织微环境、转移演化等因素导致多层次分布偏移，使决策边界漂移。

因此，现有方法难以处理实际临床中高度异质的跨域场景（如跨组织适应、跨转移演化）。论文提出 CSGDA（Cell State-Guided Graph Domain Adaptation），旨在从“Bulk-to-SC”转向“Single-Cell to Single-Cell”的端到端迁移范式，以解决单细胞药物反应预测中的跨域泛化瓶颈。

---

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
利用**细胞功能状态**（如 EMT、DNA 修复等）作为跨域不变语义锚，构建稳健的生物学桥梁连接基因型与表型。通过生物先验驱动特征重建、图结构学习及域自适应，实现高噪声 scRNA-seq 数据的鲁棒预测。

### 关键技术细节

1. **细胞状态提取与伪标签分配**
   - 基于 CancerSEA 数据库选取 K=8 个与耐药相关的核心功能状态，构建状态-基因映射字典。
   - 对每个细胞 i 和状态 k，计算状态活性分数 \( x_{i,k} = \frac{1}{|G_k \cap G_{\text{data}}|} \sum_{g \in (G_k \cap G_{\text{data}})} E_{i,g} \)。
   - 采用“赢者通吃”原则分配伪标签：\( y^{(i)}_{\text{pseudo}} = \arg\max_k (x_{i,1},...,x_{i,8}) \)。

2. **CSGDA 整体框架**
   - **Cell State-Aware Graph Structure Learning (CSA-GSL)**：基于状态特征矩阵 X 构建初始 KNN 图（含噪声），再利用 ProGNN 优化框架联合学习干净图结构 G 和 GNN 参数 θ。损失函数 \( L_{\text{GSL}} = \gamma L_{\text{GNN}} + \phi\|G-A\|_F^2 + \alpha\|G\|_1 + \beta\|G\|_* + \lambda \operatorname{tr}(X^T \hat{L}_G X) \)，其中包含稀疏、低秩、特征平滑约束。采用交替优化（梯度下降、奇异值软阈值、L1 软阈值、投影）。
   - **共享图 Transformer 编码器**：对源/目标域采用相同参数，结构约束注意力（仅允许图 G 中边计算 attention），加上残差、批归一化、随机潜在正则化（重参数化技巧）。
   - **图域自适应模块**：
     - 对抗性域对齐：域判别器 D 与共享编码器 E_sh 通过梯度反转层（GRL）进行最小-最大博弈，损失 \( L_{\text{dom}} \)。
     - 目标域信息熵最小化 \( L_{\text{ent}} \)。
     - **重叠惩罚损失（Overlap Penalty）**：\( L_{\text{olp}} = \frac{1}{|S_{\text{pos}}||S_{\text{neg}}|} \sum_{s_a \in S_{\text{pos}}} \sum_{s_u \in S_{\text{neg}}} \max(0, \mu + s_u - s_a) \)，推动敏感/耐药细胞分数分布分离，增大类间间隔。
   - 总损失 \( L_{\text{total}} = L_{\text{cls}} + \lambda_d L_{\text{dom}} + \lambda_e L_{\text{ent}} \)，其中 \( L_{\text{cls}} = \lambda_c L_{\text{ce}} + \lambda_o L_{\text{olp}} \)。

### 算法流程（文字说明）
1. 输入：源域（有标签）和目标域（无标签）的基因表达矩阵。
2. 计算细胞状态特征矩阵 X，分配伪标签。
3. 初始化 KNN 图，通过 CSA-GSL 交替优化得到干净图 G。
4. 共享图 Transformer 编码器提取域不变嵌入 Z_s、Z_t。
5. 计算分类损失（含重叠惩罚）、域对抗损失、目标熵损失，联合优化。
6. 推理时仅使用共享编码器和预测器生成药物反应概率。

---

## 3. 实验设计

### 数据集与场景
使用了 5 个 scRNA-seq 数据集，覆盖：

| 场景 | 描述 |
|------|------|
| 跨平台（Cross-Platform） | 不同测序平台 |
| 跨细胞系（Cross-Cell Line） | 不同细胞系 |
| 跨组织-单药（Cross-Tissue Monotherapy） | 不同组织来源（单药治疗） |
| 跨组织-联合（Cross-Tissue Combination） | 不同组织（联合治疗） |
| 跨转移（Cross-Metastasis） | 原发 vs 转移瘤（顺铂耐药） |

### 基准方法（Baseline）
- SCAD
- scDEAL
- scAdaDrug
- SSDA4Drug（半监督，但 CSGDA 为无监督）
- scGSDR

### 评价指标
AUROC、AUPR、ACC、F1-macro。所有方法在相同预处理数据、相同条件下运行，超参数按官方默认/推荐调优，保证公平。

---

## 4. 资源与算力

论文正文及实验部分**未明确说明**使用的 GPU 型号、数量及训练时长。仅在方法部分提到学习率、迭代次数等超参数，但未提供硬件环境。

---

## 5. 实验数量与充分性

主要实验包括：
- **主实验**（表1）：5 个场景 × 5 个基准方法 + CSGDA，共 30 组对比。
- **消融实验**（图4）：考察生物先验、动态图学习、域自适应、损失函数（L_ce 与 L_olp）的贡献，在 5 个场景中分别进行。
- **生物可解释性分析**：积分梯度识别关键基因，在跨转移顺铂数据集中展示驱动基因（RAD51C 等）和细胞状态（DNA 修复等）的贡献。
- **附加实验**：范式对比（Bulks-to-SC vs SC-to-SC）如图3和表S5。

**充分性评价**：实验设计较全面，覆盖了多种临床相关异质性场景，对比方法均为近年最新。消融实验验证了各模块必要性。可解释性分析深入且与文献一致。但未提及统计显著性检验（如 t 检验或置信区间），也缺少更多样化的药物/癌症类型验证。整体而言，实验充分且客观，但非绝对完备。

---

## 6. 论文的主要结论与发现

1. **CSGDA 在所有场景中均优于现有方法**，尤其在高异质性场景（跨组织、跨转移）提升显著，平均 ACC 和 AUPR 提升约 6%。
2. **从 Bulk-to-SC 转向 SC-to-SC 范式**能有效避免流形不匹配问题，为 CSGDA 提供了更优基础。
3. **消融实验证实**：生物先验、CSA-GSL 图学习、域自适应、重叠惩罚损失均为关键组件，缺一不可。
4. **可解释性分析**成功识别出已知耐药基因（RAD51C、TMEM205）和细胞状态（DNA 修复），并发现缺氧、细胞周期等辅助因素，验证模型学习到真实生物学机制。
5. **模型具备发现未知特征的能力**：在无监督下识别出 NDUFA11、NDUFS6、TMEM205 等未在初始字典中的高贡献基因，TMEM205 作为顺铂外排泵得到文献支持。

---

## 7. 优点

- **创新性**：首次将细胞功能状态作为跨域语义锚，结合图结构学习与域自适应，解决单细胞药物反应预测中的分布偏移问题。
- **方法设计**：重叠惩罚损失明确增大类间间隔，提高对混淆亚群的区分能力；图结构学习引入生物先验（特征平滑），避免纯数据驱动的盲目优化。
- **可解释性强**：集成梯度框架实现“基因→状态→耐药机制”的多层次归因，兼具验证已知和发现新生物标志物能力。
- **实验严谨**：在多种真实临床异质性场景（平台、组织、转移）上评估，对比方法全面，消融实验充分。
- **实用性**：采用无监督域适应（不依赖目标标签），更符合实际应用场景。

---

## 8. 不足与局限

| 不足/局限 | 说明 |
|-----------|------|
| **计算资源未报告** | 未提及 GPU 型号、数量、训练时长，影响可复现性评估。 |
| **数据集多样性有限** | 仅使用 5 个 scRNA-seq 数据集，未涵盖更多癌症类型、更多药物（仅直接测试顺铂解释性）。 |
| **缺乏统计显著性检验** | 未提供标准误差或假设检验，无法判断性能提升是否统计显著。 |
| **依赖先验知识库** | 细胞状态映射依赖 CancerSEA，可能遗漏未知功能状态或在不同癌症中适用性有限。 |
| **仅转录组层面** | 未整合蛋白质组、表观组等多组学数据，无法全面刻画肿瘤微环境复杂性。 |
| **潜在过拟合风险** | 虽然消融实验有效，但未在完全独立的外部验证集上测试泛化能力（如其他机构数据）。 |

---

（完）
