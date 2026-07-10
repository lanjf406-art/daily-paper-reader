---
title: Single-cell multi-omics analysis reveals heterogeneity and plasticity of neutrophil states in response to immunotherapies
title_zh: 单细胞多组学分析揭示免疫治疗诱导的中性粒细胞状态的异质性和可塑性
authors: "Gao, A., Shyamkumar, S., Winn, N. B., Erbe, A. K., Davis, S., Zaborek, J., Heimstreet, K., Boyenga, S., Matthews, J., Tzu-Ming Tsao, S., Sondel, P. M., Dinh, H. Q."
date: 2026-07-09
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.02.735691v1.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 免疫治疗耐药中中性粒细胞状态的单细胞多组学分析
tldr: 肿瘤相关中性粒细胞在冷肿瘤中与不良预后及免疫治疗抵抗相关，其异质性和可塑性机制尚不清楚。本研究通过单细胞多组学分析M2h小鼠头颈癌模型，鉴定出五种中性粒细胞状态（N0-N4），发现抗肿瘤的ISG+ N1和CCR3+ N3在抗CD40、TNF及组合NAT治疗中显著扩增并增强与CD8+ T细胞互作，而免疫抑制性N0减少。ICAM1（CD54）作为激活标志物，在N1/N2/N3中高表达，其在HNSCC患者中与免疫检查点抑制反应趋势相关且改善总生存。在神经母细胞瘤模型中验证了NAT减少N0但未诱导抗肿瘤状态。该研究揭示了免疫治疗重塑中性粒细胞状态的新机制，为冷肿瘤治疗提供了ICAM1作为潜在生物标志物。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1542, \"height\": 2101, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1631, \"height\": 2169, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1622, \"height\": 2067, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1681, \"height\": 2072, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1684, \"height\": 1497, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1631, \"height\": 2044, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-735691-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1614, \"height\": 1141, \"label\": \"Figure\"}]"
motivation: 冷肿瘤中中性粒细胞状态与ICI抵抗相关，但不同免疫疗法能否诱导抗肿瘤状态及其与疗效关系尚不清楚。
method: 使用M2h小鼠头颈癌模型，通过单细胞多组学测序与流式验证，分析抗CD40、TNF及组合NAT治疗下的中性粒细胞状态，并在神经母细胞瘤模型中验证。
result: 鉴定出N0-N4五种状态，有效治疗中ISG+ N1和CCR3+ N3扩增，N0减少，ICAM1标记激活状态并与ICI反应相关。
conclusion: 免疫治疗可重塑中性粒细胞状态，ICAM1是潜在生物标志物，支持联合aCD40/TNF疗法。
---

## 摘要
背景肿瘤相关中性粒细胞（TANs）是肿瘤微环境中功能异质性和可塑性细胞的新兴角色。在免疫学冷肿瘤中，中性粒细胞丰度升高与预后不良和免疫检查点抑制（ICI）耐药相关。不同的免疫疗法是否能诱导不同的抗肿瘤中性粒细胞状态，以及它们与治疗效果的关系尚不清楚。
方法利用头颈部鳞状细胞癌（HNSCC）的同系MOC2-huEGFR（M2h）小鼠模型，我们用激动性抗CD40单克隆抗体（mAb）（aCD40）、TNF、西妥昔单抗或其三者组合（称为中性粒细胞激活疗法NAT）治疗荷瘤小鼠。除评估抗肿瘤疗效外，我们还进行了单细胞多组学RNA和蛋白质测序，随后进行生物信息学分析和流式细胞术验证。NAT诱导的抗肿瘤功效和相关中性粒细胞状态也在另一个冷肿瘤模型9464D-GD2神经母细胞瘤中进行了评估。然后利用HNSCC患者的临床、蛋白质组学和转录组学数据评估了鼠源性治疗诱导的中性粒细胞基因特征。
结果使用M2h模型鉴定了五种转录上不同的中性粒细胞状态（N0-N4），包括前体状态CD49d+ N4。N0中性粒细胞（免疫抑制/静止）主导未治疗肿瘤，但在成功治疗中不占主导。ISG+ N1中性粒细胞和CCR3+ N3中性粒细胞在aCD40、TNF和NAT治疗中扩增，具有抗肿瘤基因特征，并且通过生物信息学分析发现与CD8+ T细胞有更多相互作用。N2中性粒细胞反映了在所有治疗中发现的一种最近确定的缺氧适应状态。ICAM1（CD54）成为治疗诱导的中性粒细胞激活的标志物，区分N1、N2和N3中性粒细胞与N0中性粒细胞，并经流式细胞术验证。在9464D-GD2神经母细胞瘤模型中，NAT治疗也减少了HNSCC模型中未治疗肿瘤中见到的N0主导地位，但未能诱导抗肿瘤中性粒细胞状态。在23名接受ICI治疗的HNSCC患者中，中性粒细胞中的ICAM1蛋白表达与应答者状态呈趋势性关联（TMA水平p=0.029），并且ICAM1中性粒细胞基因表达也与TCGA数据中改善的总生存期呈趋势性关联（HR=0.75，p=0.059）。
结论不同的免疫疗法诱导的中性粒细胞状态由富含不同功能通路的转录谱定义，既与抗肿瘤特征相关，也与促肿瘤特征相关。ICAM1识别激活的中性粒细胞，并可能作为HNSCC中ICI反应的生物标志物，需要进一步的临床验证。
关于这个主题已经知道的内容中性粒细胞异质性越来越受到关注，研究识别出基线或治疗诱导的抗肿瘤中性粒细胞群体。几种有效的治疗方案涉及抗CD40激动剂（aCD40）抗体，其中包括中性粒细胞激活疗法（NAT），该疗法结合aCD40、TNF和一种旨在重编程中性粒细胞的肿瘤抗原结合抗体。因此，NAT可能在富含髓系细胞的冷肿瘤中特别有效，这些肿瘤对传统免疫疗法如检查点阻断基本无反应，通过相似和不同的机制发挥这些抗肿瘤作用；然而，这一点尚未得到测试。
这项研究增加了什么这项研究增加了一个单细胞多组学框架，用于定义MOC2-huEGFR和9464D-GD2肿瘤（两种免疫学冷模型）中治疗诱导的中性粒细胞异质性。它突出了ICAM1/CD54和干扰素刺激基因作为主导抗肿瘤中性粒细胞状态的标志物，同时表明中性粒细胞状态组成在不同肿瘤模型中有所变化。
这项研究可能如何影响研究、实践或政策这些结果支持在冷鼠头颈癌模型中围绕aCD40和TNF构建的髓系调节疗法的疗效，并在较小程度上支持冷鼠神经母细胞瘤模型中的疗效。中性粒细胞中ICAM1/CD54的表达也被确定为抗肿瘤活性和治疗反应的有前景的标志物。更广泛地说，这项工作表明将aCD40和/或TNF纳入现有治疗方案可以改善结果，而ICAM1/CD54高表达的中性粒细胞可能作为有用的治疗读数。

## Abstract
BackgroundTumor-associated neutrophils (TANs) are emerging as functionally heterogeneous and plastic cells in the tumor microenvironment. In immunologically cold tumors, elevated neutrophil abundance correlates with poor prognosis and resistance to immune checkpoint inhibition (ICI). Whether distinct anti-tumoral neutrophil states can be induced by different immunotherapies and how they relate to treatment efficacy remains unclear.

MethodsUsing the syngeneic MOC2-huEGFR (M2h) mouse model of head and neck squamous cell cancer (HNSCC), we treated tumor-bearing mice with agonistic anti-CD40 monoclonal antibody (mAb) (aCD40), TNF, Cetuximab, or a combination of all three, designated Neutrophil Activating Therapy (NAT). In addition to evaluating anti-tumor efficacy, we performed single-cell multiomics RNA and protein sequencing, followed by bioinformatics analyses and flow cytometry validation. NAT-induced anti-tumor efficacy and related neutrophil states were also assessed in another cold tumor model, 9464D-GD2 neuroblastoma. Murine treatment-induced neutrophil gene signatures were then evaluated using clinical, proteomic, and transcriptomic data from HNSCC patients.

ResultsFive transcriptionally distinct neutrophil states (N0-N4), including precursor state CD49d+ N4, were identified using the M2h model. N0 neutrophils (immunosuppressive/quiescent) dominated untreated tumors, but not in successful treatments. ISG+ N1 neutrophils and CCR3+ N3 neutrophils expanded by aCD40, TNF, and NAT treatment with anti-tumoral gene signatures and found more interacting with CD8+ T cells from bioinformatics analysis. N2 neutrophils reflected a recently established hypoxia-adapted state found in all treatments. ICAM1 (CD54) emerged as a marker of treatment-induced neutrophil activation, discriminating N1, N2, and N3 neutrophils from N0 neutrophils, validated by flow cytometry. In the 9464D-GD2 neuroblastoma model, NAT treatment also reduced the N0 dominance seen in untreated tumors in the HNSCC model but failed to induce anti-tumoral neutrophil states. In 23 HNSCC patients who received ICI therapy, ICAM1 protein expression in neutrophils trended toward association with responder status (TMA-level p=0.029), and ICAM1 neutrophil gene expression also trended toward association with improved overall survival in TCGA data (HR=0.75, p=0.059).

ConclusionsDistinct immunotherapy-induced neutrophil states are defined by transcriptional profiles enriched in different functional pathways, associated with both anti-tumor and pro-tumor signatures. ICAM1 identifies activated neutrophils and potentially serves as a biomarker of ICI response in HNSCC, warranting further clinical validation.

WHAT IS ALREADY KNOWN ON THIS TOPICNeutrophil heterogeneity has received increasing attention, with studies identifying antitumoral neutrophil populations, either at baseline or induced by treatment. Several effective treatment regimens involve an anti-CD40 agonist (aCD40) antibody, among them Neutrophil Activating Therapy (NAT), which combines aCD40, TNF, and a tumor antigen binding antibody designed to reprogram neutrophils. NAT could thus be particularly effective in cold, myeloid-rich tumors that are largely unresponsive to conventional immunotherapies such as checkpoint blockade, enacting these anti-tumoral effects through similar and different mechanisms; however, this has not been tested.

WHAT THIS STUDY ADDSThis study adds a single-cell multi-omics framework for defining treatment-induced neutrophil heterogeneity in MOC2-huEGFR and 9464D-GD2 tumors, two immunologically cold models. It highlights ICAM1/CD54 and interferon-stimulated genes as markers of a dominant antitumor neutrophil state, while showing that neutrophil state composition variy across tumor models.

HOW THIS STUDY MIGHT AFFECT RESEARCH, PRACTICE, OR POLICYThese results support the efficacy of a myeloid-modulating therapy built around aCD40 and TNF in a cold murine head and neck cancer model, and to a lesser extent in a cold murine neuroblastoma model. ICAM1/CD54 expression in neutrophils was also identified as a promising marker of antitumor activity and treatment response. More broadly, this work suggests that incorporating aCD40 and/or TNF into existing treatment regimens could improve outcomes, while ICAM1/CD54-high neutrophils may serve as a useful therapeutic readout.

---

## 论文详细总结（自动生成）

好的，以下是根据您提供的论文内容生成的详细中文总结。

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：肿瘤相关中性粒细胞（Tumor-Associated Neutrophils, TANs）在肿瘤微环境（TME）中具有功能异质性和转录可塑性，并非传统认为的单一促肿瘤细胞。在“免疫学冷肿瘤”中（如头颈鳞癌，HNSCC），高中性粒细胞丰度与预后不良和对免疫检查点抑制剂（ICI）的耐药性密切相关。
- **核心问题**：不同的免疫疗法（特别是髓系调节疗法）能否诱导出不同的抗肿瘤中性粒细胞状态？这些状态与治疗效果之间的关系尚不清楚。
- **研究意义**：理解TANs在免疫治疗下的动态变化，有助于开发新的治疗策略（如联合aCD40/TNF）和鉴定预测治疗反应的生物标志物（如ICAM1），以改善冷肿瘤患者的预后。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：利用单细胞多组学技术，在两种冷肿瘤小鼠模型中，系统解析不同免疫疗法（aCD40、TNFα、Cetuximab 及其组合 NAT）诱导的中性粒细胞状态图谱，并将发现与人类临床数据关联。
- **关键技术细节**：
    1.  **动物模型**：使用免疫学冷肿瘤的**MOC2-huEGFR (M2h) 同系小鼠头颈癌模型**进行主要发现和机制研究，并使用**9464D-GD2 神经母细胞瘤模型**进行跨模型验证。
    2.  **单细胞多组学测序**：
        - 对M2h大肿瘤进行 **CITE-seq**，同时检测转录组 (RNA) 和表面蛋白。
        - 对M2h小肿瘤和9464D-GD2肿瘤进行 **scRNA-seq**。
    3.  **生物信息学分析**：
        - **细胞聚类**：使用Seurat和Harmony进行聚类和批次校正。
        - **差异表达基因分析**：MAST。
        - **通路富集分析**：clusterProfiler (GO和KEGG)。
        - **细胞间通讯分析**：CellChat。
        - **分化轨迹推断**：Slingshot。
        - **标签转移**：使用M2h模型鉴定的中性粒细胞状态作为参考，预测其他模型中的中性粒细胞状态。
    4.  **流式细胞术验证**：设计了包含CD54(ICAM1)、DcTRAIL-R1、CD193(CCR3)和CD49d的流式抗体组合，以CITE-seq蛋白数据为指导，验证鉴定的中性粒细胞亚群。

### 3. 实验设计：数据集、基准和方法对比

- **数据集/场景**：
    1.  **M2h HNSCC模型**：主要实验平台，测试了多种治疗组合（包括不同肿瘤大小：小肿瘤35-50mm³，大肿瘤125-150mm³）。
    2.  **9464D-GD2神经母细胞瘤模型**：用于验证NAT治疗效果的普适性和中性粒细胞状态的可转移性。
    3.  **人类HNSCC临床数据**：来自**23名接受ICI治疗患者的68个肿瘤核心**的CosMX SMI空间蛋白组数据，以及**TCGA的500名HNSCC患者**的转录组和生存数据。
- **基准/对照**：
    - 主要对照为**未经治疗的肿瘤**（Untreated/Control）。
    - 在治疗实验中，考察了**NAT组合疗法对比其各个单一组份（aCD40、TNFα、Cetuximab）及双药组合（aCD40+TNFα）**的疗效。
    - 通过**中性粒细胞耗竭实验**（抗Ly6G抗体）验证中性粒细胞的作用。
    - 评估了**联合ICI（抗PD-1/抗CTLA-4）**是否增强疗效。
- **方法对比**：主要对比了不同治疗组（NAT、aCD40、TNFα、Cetuximab等）对中性粒细胞状态组成和功能的影响，以及不同肿瘤模型（M2h vs. 9464D-GD2）在相同治疗下的反应差异。

### 4. 资源与算力

- 论文**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。仅提及使用Illumina NovaSeq X Plus进行测序，并使用Seurat、CellRanger等软件进行数据分析。

### 5. 实验数量与充分性

- **实验数量**：
    - **体内疗效实验**：在M2h和9464D-GD2模型中，进行了小/大肿瘤、不同治疗组、中性粒细胞耗竭、联合ICI等**多个独立实验**，每组通常有多个小鼠（n=15-17等），并评估了肿瘤生长、存活率和肿瘤清除率。
    - **单细胞测序实验**：对**大M2h肿瘤**（每个治疗组2-3个肿瘤混合）进行CITE-seq，对小M2h和9464D-GD2肿瘤进行scRNA-seq。
    - **流式细胞术验证实验**：在两个独立实验中对大M2h肿瘤进行验证。
    - **临床数据分析**：在独立的人HNSCC队列中进行了关联性分析。
- **实验充分性**：
    - **客观**：实验设计基本合理，包含了必要的对照组和关键验证实验（如中性粒细胞耗竭）。
    - **公平**：在比较不同治疗时，使用了相同的动物品系、肿瘤模型和治疗方案。跨模型验证增强了结论的稳健性。
    - **结论**：实验覆盖了从机理（单细胞图谱）到功能（耗竭实验）再到临床关联的多个层面，总体较为充分。但作者也指出，**所有功能推断均基于转录组和蛋白表达，缺乏直接的功能实验**（如体外杀伤实验、T细胞激活实验），这是后续研究需要补足的关键环节。

### 6. 论文的主要结论与发现

1.  **鉴定了五种中性粒细胞状态 (N0-N4)**：
    - **N0 (免疫抑制/静止型)**：在未治疗肿瘤中占主导，特征为低ICAM1、T细胞抑制基因、基质重塑。成功治疗后显著减少。
    - **N1 (ISG+ / 干扰素刺激型)**：抗肿瘤状态，在所有成功治疗（尤其是aCD40和NAT）中扩增，高表达ICAM1和干扰素刺激基因，与CD8+ T细胞有强相互作用。
    - **N2 (缺氧适应型)**：在所有治疗组中均存在，表达缺氧和应激反应基因，其功能偏向促肿瘤（与已报道的T3状态一致）。
    - **N3 (CCR3+ / 抗菌效应型)**：严格治疗诱导的状态（主要由NAT和TNFα诱导），高表达抗菌和趋化基因，表面蛋白CCR3阳性，ICAM1中等表达。
    - **N4 (CD49d+ / 前体样型)**：少量存在，表达发育和血管生成相关基因，功能惰性。
2.  **NAT (aCD40 + TNFα) 在M2h模型中疗效显著**，且中性粒细胞是其主要效应细胞。在M2h模型中，**aCD40 + TNFα双药组合的疗效与完整的NAT三药组合相当**，表明此模型中无需肿瘤靶向抗体（Cetuximab）。
3.  **ICAM1是治疗诱导的激活中性粒细胞的关键标志物**。它可区分N1/N2/N3与N0，且在小鼠和人数据中均与治疗反应和生存期改善呈趋势性相关。
4.  **中性粒细胞状态在不同肿瘤模型间存在差异**。在9464D-GD2神经母细胞瘤中，NAT降低了N0的比例，但未能有效诱导N1和N3抗肿瘤状态，导致其中性粒细胞对疗效的贡献远小于M2h模型。这揭示了TANs重编程的**肿瘤类型特异性**。

### 7. 优点：方法或实验设计上的亮点

1.  **先进的单细胞多组学方法**：使用CITE-seq同时检测RNA和表面蛋白，为中性粒细胞状态的精细分群和功能预测提供了高分辨率数据，优于单一的转录组分析。
2.  **系统的体内外验证**：从单细胞图谱发现，到流式细胞术验证，再到中性粒细胞耗竭的功能实验，最后到临床数据分析，形成了完整的证据链。
3.  **跨模型比较**：在两种不同的冷肿瘤（HNSCC和神经母细胞瘤）中验证发现，揭示了中性粒细胞状态的可塑性和上下文依赖性，得出的结论更具普适性。
4.  **强临床转化导向**：不仅在小鼠模型中鉴定出新标志物ICAM1，还利用公共和已发表的临床数据验证了其与ICI反应和生存期的关联，为临床转化提供了直接证据。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制

1.  **功能验证不足**：所有中性粒细胞状态的功能判断（如N1的抗肿瘤，N2的促肿瘤）主要基于转录组和蛋白表达推断，**缺乏直接的功能实验**（如共培养杀伤实验、T细胞激活实验、过继转移等）来最终确认。
2.  **轨迹推断的局限性**：Slingshot轨迹分析基于静态单细胞快照，**无法替代实时谱系追踪或时间序列实验**，只能提供发育关系的推测。
3.  **人类数据样本量小且不匹配**：人HNSCC临床数据队列**规模有限（23名患者）**，且分析的是ICI治疗，与小鼠模型中的NAT治疗方案不完全匹配，限制了统计效力、临床普适性和直接可比性。
4.  **实验偏差风险**：作者在文中提到，流式细胞术与CITE-seq之间的定量差异可能源于几个**生物和技术变量**（如小鼠性别、肿瘤接种代次、动物房地点），这在不同批次实验间可能引入偏差。
5.  **应用限制**：研究主要基于免疫缺陷小鼠模型，无法完全反映人类肿瘤的复杂免疫环境。ICAM1作为生物标志物的临床价值需要在**前瞻性、多中心、更大样本量的研究**中进行最终验证。

（完）
