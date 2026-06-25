---
title: Killer-cell dominance dichotomy governs tumor immune networks and stratifies inflamed cancers
title_zh: 杀伤细胞优势二分法支配肿瘤免疫网络并对炎性癌症进行分层
authors: "Li, A.-N., Yu, Z., Zhang, W., Chang, H., Feng, S., Yang, X., Xiong, K., He, L., Zhao, Z., Shen, L., Tan, Z., Du, W., Zhong, L., Zhang, X., Hu, Y., Su, X., Wang, R., Fu, S., Zhang, L., Hong, S."
date: 2026-06-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.15.732326v1.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 肿瘤微环境中杀伤细胞二分法与免疫治疗耐药相关
tldr: 癌症免疫治疗受益有限，即使“热肿瘤”也存在异质性。本研究基于近5000例泛癌单细胞RNA-seq数据，结合谱流式细胞术和空间转录组学验证，发现终末细胞毒性免疫并非统一由多种杀伤细胞共同浸润，而是呈现两种主导状态：耗竭CD8+ T细胞（Tex）或CD56dimCD16hi NK细胞（NK1）占优。这一二分法主导了肿瘤内在和外在的变异主轴。值得注意的是，NK1偏斜的肿瘤虽具有高细胞溶解活性，但对免疫检查点阻断疗法不敏感。该发现揭示了癌症免疫的基础轴，为NK细胞导向的免疫治疗提供了新靶点。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有“冷热肿瘤”范式无法解释免疫治疗响应差异，需明确杀伤细胞的群体架构。
method: 分析近5000例泛癌单细胞RNA-seq样本，并用谱流式细胞术和空间转录组学进行正交验证。
result: 发现终末细胞毒性免疫分为Tex主导或NK1主导两种状态，主导肿瘤免疫网络方差；NK1偏斜肿瘤对ICB耐药。
conclusion: 杀手细胞二分法定义了癌症免疫基础轴，为NK导向免疫治疗靶点开发提供依据。
---

## 摘要
癌症免疫治疗的获益仍然有限，即使在具有高杀伤淋巴细胞浸润的“热”肿瘤中也是如此。在这里，我们基于近5000个泛癌单细胞RNA测序样本，结合通过光谱流式细胞术和空间转录组学的正交验证，研究了杀伤细胞在群体水平的架构。与主流的“热-冷”范式（假设多种细胞毒性谱系协同浸润）不同，我们揭示了一个保守的框架，其中个体或恶性肿瘤的终末细胞毒性免疫分化为由耗竭的CD8+ T细胞（Tex）或CD56dimCD16hi NK细胞（NK1）主导的状态。尽管肿瘤微环境复杂，Tex-NK1分化主导了肿瘤内在和肿瘤外在变异的主要轴。与NK细胞积极贡献于免疫治疗效果的常规观点不同，NK1偏向的肿瘤虽然具有高细胞溶解活性，但对当前的免疫检查点阻断方案具有抵抗性。这种杀伤细胞分化定义了癌症免疫的基础轴，并为优先考虑NK导向免疫治疗的下一代靶点提供了资源。

## Abstract
Cancer immunotherapy benefits remain limited, even among "hot" tumors with high killer lymphocyte infiltration. Here, we investigated the population-level architecture of killer cells based on nearly 5,000 pan-cancer scRNA-seq samples, together with orthogonal validation by spectral cytometry and spatial transcriptomics. Unlike the prevailing "hot-cold" paradigm, which assumes coordinated infiltration of multiple cytotoxic lineages, we uncovered a conserved framework wherein terminal cytotoxic immunity in individuals or malignancies diverges into states dominated by either exhausted CD8+ T cells (Tex) or CD56dimCD16hi NK (NK1) cells. Despite the complexity of the tumor microenvironment, Tex-NK1 divergence governs the primary axis of tumor-intrinsic and tumor-extrinsic variance. Distinct from the conventional view that NK cells positively contribute to immunotherapy efficacy, NK1-skewed tumors, although highly cytolytic, are refractory to current immune checkpoint blockade regimens. This killer divergence defines a foundational axis of cancer immunity and provides a resource for prioritizing next-generation targets for NK-directed immunotherapy.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：即使在高杀伤淋巴细胞浸润的“热”肿瘤中，免疫治疗获益仍然有限，表明现有“冷热肿瘤”范式无法解释响应差异。需要明确杀伤细胞在群体层面的真实架构。
- **研究动机**：传统观点认为多种细胞毒性谱系（如CD8+ T细胞、NK细胞）协同浸润肿瘤；但作者怀疑存在更保守的主导性分化模式。
- **背景意义**：发现一种全新的免疫分类轴——杀伤细胞优势二分法（Tex vs. NK1），为理解肿瘤免疫网络和指导下一代免疫治疗（尤其NK导向疗法）提供基础资源。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程（文字说明）
- **核心思想**：跳出“混合浸润”范式，证明终末细胞毒性免疫并非均匀混合，而是分化为两种互斥的主导状态——耗竭CD8+ T细胞（Tex）主导或CD56⁴ⁱᵐCD16ʰⁱ NK细胞（NK1）主导。
- **关键技术**：
  - 基于近5000个泛癌单细胞RNA测序（scRNA-seq）样本进行大规模的细胞分群和状态鉴定。
  - 使用光谱流式细胞术（spectral cytometry）和空间转录组学（spatial transcriptomics）进行正交验证，确认Tex-NK1分化的存在和保守性。
- **算法流程（文字说明）**：
  1. 收集泛癌scRNA-seq数据（近5000例样本）并进行质量控制、标准化和聚类。
  2. 重点分析CD8+ T细胞和NK细胞中的终末细胞毒性亚群，识别出Tex（耗竭CD8+ T）和NK1（CD56⁴ⁱᵐCD16ʰⁱ NK）两个主要终末状态。
  3. 计算每个样本或每个肿瘤中Tex和NK1的相对比例，确定主导类型（dominance）。
  4. 分析Tex-NK1分化与肿瘤内在（如突变、通路）和肿瘤外在（如免疫浸润、临床结局）方差的主轴关系。
  5. 通过独立的光谱流式和空间转录组数据验证该分化的可重复性和空间组织模式。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：
  - 主要数据集：近5000个泛癌单细胞RNA-seq样本（涵盖多种癌症类型）。
  - 验证数据集：光谱流式细胞术和空间转录组学数据（具体样本量和癌种未在摘要中详述）。
- **基准（Benchmark）**：未明确设置传统基准；研究本质是发现性（discovery）而非方法对比。隐含地，与“冷热肿瘤”范式进行概念对比，证明后者忽略了Tex-NK1二分法。
- **对比方法**：无直接算法对比，但通过正交实验（不同技术平台）验证结论的鲁棒性。

## 4. 资源与算力：若文中有提及
- **论文未明确说明**：使用的GPU型号、数量、训练时长等信息均未在摘要和元数据中提供。需要查阅全文（目前受限）才能获知。

## 5. 实验数量与充分性
- **实验数量**：基于近5000例scRNA-seq样本，规模较大；此外有两项独立验证实验（光谱流式、空间转录组）。但摘要未列出具体的子实验数量（如消融实验、跨癌种比较等）。
- **充分性评估**：
  - **优点**：样本量足够大，泛癌覆盖增强了一般性；正交验证增加了可信度。
  - **潜在不足**：缺少功能实验（如基因敲除、过继转移）来直接证明Tex-NK1分化的因果关系；未提供临床队列的免疫治疗响应数据（仅在结论中提到NK1偏斜肿瘤对ICB耐药，但未展示详细统计）。
  - **客观性**：基于公开数据和独立验证，方法相对公正，但可能存在构建分析 pipeline 时的偏见。

## 6. 论文的主要结论与发现
- **核心发现**：肿瘤终末细胞毒性免疫呈现保守的二分法：要么由Tex主导，要么由NK1主导，而非多种细胞类型混合主导。
- **关键结论**：
  - Tex-NK1分化是肿瘤内在和肿瘤外在变异的主轴，解释了肿瘤微环境的主要方差。
  - 与传统认知不同，NK1高浸润的肿瘤（虽具有高细胞溶解活性）对当前的免疫检查点阻断（ICB）方案不敏感（即耐药）。
  - 该二分法定义了“癌症免疫的基础轴”，为NK导向的免疫治疗提供了新的潜在靶点和分层依据。

## 7. 优点：方法或实验设计上的亮点
- **大规模数据驱动**：利用近5000例泛癌scRNA-seq，使得发现具有广泛代表性。
- **多平台正交验证**：结合光谱流式（蛋白水平）和空间转录组（空间分布），增强了转录组层面发现的可靠性。
- **颠覆性概念**：挑战了“热肿瘤中所有杀伤细胞协同浸润”的默认假设，提出了更简洁、可操作的分类（Tex vs. NK1）。
- **临床相关性**：明确区分出对现有ICB耐药但高细胞毒的NK1偏斜肿瘤，为开发NK导向疗法提供直接动机。

## 8. 不足与局限
- **实验覆盖**：未涉及功能性体内实验，结论主要基于关联性分析，因果关系未建立。
- **偏差风险**：scRNA-seq分析中细胞分群和状态鉴定存在主观阈值，可能遗漏中间状态或稀有亚群。
- **应用限制**：
  - 当前ICB耐药的结论仅来自转录组特征，缺乏临床生存或治疗响应数据的直接验证。
  - 尚无证据表明NK1偏斜肿瘤是否对其他类型的免疫治疗（如NK细胞过继转移、NK细胞衔接器）敏感。
  - 未覆盖所有癌症类型，可能某些癌种中Tex-NK1分化不显著。
- **资源信息缺失**：未报告计算成本，使可重复性评估受限。

（完）
