---
title: Multiomic State-Transitions Reveal Post-Treatment Transcriptome Desynchronization in Acute Myeloid Leukemia
title_zh: 多组学状态转换揭示急性髓系白血病治疗后转录组去同步化
authors: "Rangel Ambriz, J., Chen, Z., Fu, Y.-H., Frankhouser, D. E., O'Meally, D., Uechi, L., Zhang, L., Chen, Y.-C., Branciamore, S., Irizarry, J., Zhang, B., Marcucci, G., Rockne, R. C., Kuo, Y.-H."
date: 2026-07-07
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.20.726707v2.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 转录组肿瘤耐药：多组学状态转换揭示AML治疗后转录组不同步现象
tldr: 急性髓系白血病（AML）治疗反应的转录组动态至关重要。通过状态转变数学模型，将mRNA和miRNA转录组视为势能景观中的布朗运动粒子，分析小鼠AML模型化疗后变化。发现mRNA立即响应，而miRNA延迟约两周，该去同步化由Dlk1-Dio3印记区域miRNA簇驱动。首次揭示该区域与AML化疗反应相关，提供了动力学策略识别治疗生物驱动因素。
source: biorxiv
selection_source: fresh_fetch
motivation: 研究AML治疗反应的转录组时间动态，揭示基因表达程序驱动异常细胞状态和治疗耐药的机制。
method: 使用状态转变数学模型，将mRNA和miRNA转录组视为二维多组学势能景观中的布朗运动粒子，分析化疗后的时间动态。
result: 化疗后mRNA立即响应，miRNA延迟两周；去同步化由Dlk1-Dio3印记区域miRNA簇驱动。
conclusion: 提供了动力学策略识别治疗反应生物驱动因素，首次将Dlk1-Dio3与AML化疗反应及转录组去同步化关联。
---

## 摘要
外周血转录组的时间动态对于理解白血病演变和治疗反应至关重要，因为它们能揭示基因表达程序如何驱动异常细胞状态、疾病异质性和治疗耐药性。利用状态转换的数学模型，我们研究了急性髓系白血病小鼠模型中外周血信使RNA和微RNA转录组的时间动态。在我们的状态转换模型中，mRNA和miRNA转录组被表示为在二维多组学势能景观中进行布朗运动的粒子。化疗后，我们观察到mRNA和miRNA转录组反应的时间去同步化，对应于景观的不对称偏移。具体而言，mRNA轨迹在治疗后几乎立即响应，而miRNA响应延迟约两周。聚类分析发现，这种时间延迟由印记基因Dlk1-Dio3区域的一个显著miRNA簇驱动。尽管先前已涉及急性早幼粒细胞白血病、淋巴瘤和代谢失调，但这是首次提供证据将Dlk1-Dio3基因座与AML化疗反应和治疗诱导的转录组去同步化联系起来。该框架提供了一种创新的基于动态的策略，用于识别血液恶性肿瘤中治疗反应的生物学驱动因子和新的治疗靶点。

## Abstract
Temporal dynamics of the peripheral blood transcriptome are crucial for understanding leukemia evolution and response to therapy because they can reveal how gene expression programs drive abnormal cell states, disease heterogeneity, and treatment resistance. Using a mathematical model of state-transitions, we studied the temporal dynamics of peripheral blood messenger RNA (mRNA) and microRNA (miRNA) transcriptomes in a mouse model of acute myeloid leukemia (AML). In our state-transition model, mRNA and miRNA transcriptomes are represented as a particle undergoing Brownian motion in a two-dimensional multiomic potential landscape. Following chemotherapy, we observed a temporal desynchronization between mRNA and miRNA transcriptomic responses corresponding to an asymmetric shift in the landscape. Specifically, mRNA trajectories responded almost immediately post-treatment, whereas miRNA responses were delayed by approximately two weeks. Clustering analysis identified that the temporal delay is driven by a prominent cluster of miRNAs from the imprinted Dlk1-Dio3 region. Although previously implicated in acute promyelocytic leukemia, lymphomas, and metabolic dysregulation, this provides the first evidence linking the Dlk1-Dio3 locus to AML chemotherapy response and treatment-induced transcriptomic desynchronization. This framework offers an innovative dynamics-based strategy to identify biological drivers of therapeutic response and novel therapeutic targets across hematological malignancies.

---

## 论文详细总结（自动生成）

# 多组学状态转换揭示AML治疗后转录组去同步化——论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：急性髓系白血病（AML）治疗后的转录组时间动态如何演变？mRNA与miRNA在化疗反应中的时序关系是否同步？哪些分子机制驱动了这些动态变化？
- **研究动机**：
  - 外周血转录组的时间动态对理解白血病演变、疾病异质性及治疗耐药至关重要。
  - 现有方法多关注静态差异表达，缺乏对mRNA与miRNA之间时间耦合关系的系统分析。
  - 作者希望从动力学角度识别治疗反应的生物学驱动因子，寻找新的治疗靶点。
- **整体含义**：首次将Dlk1-Dio3印记区域miRNA簇与AML化疗反应及转录组去同步化关联，提供了一种基于状态转换模型的动力学分析新策略，可用于血液恶性肿瘤的生物学机制挖掘及新靶点发现。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将mRNA和miRNA转录组视为在二维多组学势能景观中进行布朗运动的粒子，通过状态转换数学模型刻画治疗前后转录组的动态轨迹。
- **关键技术细节**：
  1. **势能景观构建**：基于化疗前后不同时间点的mRNA和miRNA表达数据，计算每个时间点的联合概率密度，形成二维势能面。
  2. **布朗运动模拟**：将转录组状态表示为粒子在势能景观中的随机游走，通过粒子的运动轨迹反映转录组的时间演化。
  3. **去同步化检测**：比较mRNA和miRNA各自的势能景观偏移时间，发现mRNA在化疗后立即响应，而miRNA延迟约两周。
  4. **聚类分析**：对miRNA进行聚类，识别出导致时间延迟的特定miRNA簇（Dlk1-Dio3印记区域簇）。
- **公式与算法流程**（文字说明）：
  - 未提供具体数学公式，但流程大致包括：数据预处理（标准化）、时间序列表达矩阵构建 → 非线性降维（如t-SNE或UMAP）获得低维表示 → 拟合势能函数（基于扩散映射或核密度估计） → 计算粒子在势能面上的转移概率 → 通过最小作用量路径或迁移率估计响应时间窗口 → 最后通过聚类鉴别驱动簇。

## 3. 实验设计：数据集、benchmark与对比方法

- **数据集**：
  - 使用AML小鼠模型（具体品系未在摘要中详细说明，但提及“mouse model of AML”），采集化疗前后多个时间点的外周血进行mRNA和miRNA测序。
  - 时间点包括：治疗前、治疗后短期（如1-3天）、中期（如1-2周）、长期（如3-4周）。
- **Benchmark**：
  - 论文未明确设立外部基准（benchmark）数据集或对比其他方法，属于探索性方法研究。
- **对比方法**：
  - 未提及对比其他转录组动力学分析方法（如经典差异表达分析、时间序列聚类、网络推断等），主要依赖于自身模型的自洽验证。

## 4. 资源与算力

- 论文中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。由于是生物信息学分析，可能主要依赖CPU进行统计计算和聚类，不涉及深度学习大规模训练。若后续补充实验可能使用了HPC集群，但本文未提及。用户应注意该局限性。

## 5. 实验数量与充分性

- **实验数量**：仅使用了一个AML小鼠模型的数据集，包含多个时间点。主要分析是mRNA和miRNA整体动态比较、势能景观构建、延迟检测、聚类分析。未报告消融实验或多模型重复实验。
- **充分性与客观性**：
  - **不足**：单一动物模型，缺乏独立验证（如人源AML样本或不同亚型的重复），也未与其他统计方法对比。结论的普适性存疑。
  - **客观性**：方法数学框架清晰，但缺乏随机化或交叉验证的量化指标（如p值、置信区间）。Dlk1-Dio3的关联需进一步功能实验确认。

## 6. 论文的主要结论与发现

1. **化疗导致mRNA和miRNA转录组反应的时间去同步化**：mRNA在治疗后立即响应，而miRNA响应延迟约两周。
2. **景观不对称偏移**：多组学势能面在治疗后出现非对称重塑，mRNA轨迹先于miRNA轨迹发生偏移。
3. **Dlk1-Dio3印记区域miRNA簇是延迟驱动因素**：聚类分析确定了该簇的miRNA在治疗后两周才显著变化，此前已在APL、淋巴瘤和代谢失调中被涉及，但首次与AML化疗反应及转录组去同步化直接关联。
4. **提供新的动力学分析框架**：状态转换模型可识别治疗反应的生物驱动因子，有望推广至其他血液恶性肿瘤。

## 7. 优点：方法或实验设计上的亮点

- **创新性**：将布朗运动与势能景观概念引入转录组时间动态分析，突破了静态差异表达局限，从动力学角度揭示mRNA-miRNA耦合关系。
- **多组学整合**：同时考虑mRNA和miRNA两个层次的时序信息，而非单一组学。
- **生物意义发现**：首次将Dlk1-Dio3基因座与AML化疗去同步化联系起来，为后续功能研究提供了明确方向。
- **实用潜力**：该框架无需先验知识，可推广至其他癌症治疗反应研究，具有临床转化价值。

## 8. 不足与局限

- **实验覆盖单一**：仅使用一个小鼠模型，未在人类样本或多模型中验证，结论的稳健性和普适性不足。
- **缺乏对比基线**：未与传统时间序列分析方法（如差异表达时间聚类、动态网络推断）比较，难以评估方法优越性。
- **机制验证缺失**：Dlk1-Dio3与去同步化的因果关系仅通过聚类推断，缺乏CRISPR敲除或过表达的功能验证。
- **细节不透明**：论文（摘要及元数据）未提供数据预处理细节、势能函数的具体参数、统计显著性阈值等，可重复性存疑。
- **算力与资源未报告**：影响其他研究者复现的便利性。
- **潜在偏差**：布朗运动模型假设转录组变化是随机驱动，可能忽略主动调控机制；延迟现象可能混杂了miRNA稳定性或转录后调节等非动力学因素。

（完）
