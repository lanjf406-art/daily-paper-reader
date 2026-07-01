---
title: Droplet single-cell CRISPR screens identify regulators of T cell-mediated target-cell killing
title_zh: 液滴单细胞CRISPR筛选鉴定T细胞介导的靶细胞杀伤调控因子
authors: "Saronio, G., Antonini, G., Jain, A., Vogel, I., Teneggi, R., Neumann, J., Zoppi, G., Ding, Y., Pecoraro, M., Langner, M., Mirtschink, P., Stavrakis, S., deMello, A., Geiger, R."
date: 2026-06-29
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.23.734054v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 单细胞CRISPR筛选鉴定T细胞杀伤的负调控因子，揭示耐药机制
tldr: 细胞毒性T细胞通过短暂接触杀伤靶细胞，但混池筛选无法关联单细胞扰动与靶细胞命运。本文开发液滴单细胞CRISPR筛选，实现单T细胞与癌细胞配对并测量杀伤。鉴定出PTEN、RASA2及mTORC1组分等负调控因子，发现抑制mTORC1可增强快速杀伤。该策略提供交互解析遗传图谱，揭示代谢调节可提升抗肿瘤活性。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有混池筛选无法关联单T细胞扰动与靶细胞杀伤命运，需开发可解析细胞间交互的高通量方法。
method: 开发液滴单细胞CRISPR筛选平台，配对单T细胞与癌细胞，快速测量靶细胞死亡并回收sgRNA。
result: 鉴定出TCR信号、突触形成等正调控因子及PTEN、RASA2、mTORC1组分等负调控因子，抑制RPTOR或RHEB增强杀伤而降低mTORC1活性。
conclusion: 该策略实现扰动-表型直接关联，表明短暂mTORC1抑制可转变T细胞从合成代谢转向快速杀伤，增强抗肿瘤效果。
---

## 摘要
细胞毒性CD8 T细胞通过短暂的细胞间接触杀死靶细胞，但混合遗传筛选无法轻易地将单个T细胞中的扰动与其所攻击的靶细胞的命运联系起来。我们开发了液滴单细胞CRISPR筛选，用于配对单个原代人CD8 T细胞与癌细胞，测量快速靶细胞死亡，并从表型定义的液滴中回收sgRNA。将该平台应用于来自多个供体的原代T细胞，恢复了T细胞受体信号传导、突触形成、颗粒胞吐和细胞毒性分化的调控因子，并鉴定出杀伤的负调控因子，包括已知的抑制节点如PTEN、RASA2和FOXO1，以及AFAP1L2和mTORC1通路的组分。在双特异性接合子和TCR工程化环境中的验证表明，选中的阳性调控因子可跨识别模式和肿瘤模型调节靶细胞杀伤。出乎意料的是，扰动RPTOR或RHEB增强了细胞毒性执行，同时降低了mTORC1输出、增加了AKT磷酸化并减弱了合成代谢程序。短暂药理性mTORC1抑制重现了这种快速杀伤状态，并改善了过继转移后的抗肿瘤活性。这些结果建立了一种相互作用解析的混合遗传策略用于绘制细胞毒性调控因子图谱，并揭示mTORC1的短暂调节可将T细胞从合成代谢生长转向快速细胞毒性执行，从而增强抗肿瘤活性。

## Abstract
Cytotoxic CD8 T cells kill target cells through brief cell-cell encounters, but pooled genetic screens cannot readily link perturbations in individual T cells to the fate of the target cells they engage. We developed droplet single-cell CRISPR screening to pair individual primary human CD8 T cells with cancer cells, measure rapid target-cell death, and recover sgRNAs from phenotype-defined droplets. Applied across primary T cells from multiple donors, the platform recovered regulators of T cell receptor signaling, synapse formation, granule exocytosis and cytotoxic differentiation, and identified negative regulators of killing, including established inhibitory nodes such as PTEN, RASA2 and FOXO1, together with AFAP1L2 and components of the mTORC1 pathway. Validation across bispecific engager and TCR-engineered settings showed that selected hits modulate target-cell killing across recognition modalities and tumor models. Unexpectedly, perturbation of RPTOR or RHEB enhanced cytotoxic execution while reducing mTORC1 output, increasing AKT phosphorylation, and attenuating anabolic programs. Transient pharmacologic mTORC1 inhibition reproduced this rapid-killing state and improved antitumor activity after adoptive transfer. These results establish an interaction-resolved pooled genetic strategy for mapping cytotoxicity regulators and reveal that transient modulation of mTORC1 can shift T cells from anabolic growth toward rapid cytotoxic execution to enhance antitumor activity.

---

## 论文详细总结（自动生成）

### 论文核心问题与整体含义（研究动机和背景）
- **背景**：细胞毒性CD8⁺ T细胞通过形成免疫突触和释放溶细胞颗粒来快速杀伤靶细胞，这一过程是抗肿瘤免疫和细胞治疗的基础。然而，传统混池CRISPR筛选无法将单个T细胞中的基因扰动直接与它所攻击的靶细胞的命运（死亡或存活）联系起来，因为杀伤表型是非细胞自主的——扰动在T细胞中，而读出在与之物理交互的靶细胞中。
- **核心问题**：缺乏一种能够以高通量、单细胞分辨率方式，在保留效应-靶细胞配对关系的前提下，鉴定调控快速细胞毒性的基因的高通量遗传筛选方法。
- **整体含义**：开发一种新的液滴单细胞CRISPR筛选平台，将单个T细胞与单个癌细胞封装在皮升级液滴中，快速测量靶细胞死亡，并回收对应的sgRNA，从而建立扰动-表型的直接关联。该方法不仅发现了已知的杀伤正负调控因子，还意外识别出mTORC1通路的组分（如RPTOR、RHEB）是快速杀伤的负调控因子，并揭示短暂抑制mTORC1可将T细胞从合成代谢生长转向快速细胞毒执行，增强抗肿瘤活性。

### 论文提出的方法论
- **核心思想**：利用微流控液滴技术将单个CRISPR编辑的原代人类CD8⁺ T细胞与单个癌细胞共封装，在液滴内实现短暂的细胞-细胞接触杀伤，并通过荧光染料（SYTOX Green）快速报告靶细胞死亡状态，随后根据液滴荧光信号分选，恢复对应的sgRNA进行测序分析。
- **关键技术细节**：
  1. **液滴生成**：使用水-油-水双乳液（W/O/W）或水包油（W/O）液滴。T细胞和靶细胞（JeKo-1淋巴瘤细胞）与双特异性抗体Blinatumomab、活/死染料SYTOX Green共封装。
  2. **杀伤测量**：液滴在37℃孵育90分钟（快速杀伤窗口），随后通过流式细胞术（双乳液模式）或荧光激活液滴分选（FADS）分析靶细胞死亡。
  3. **分选与回收**：高速液滴分选器（~0.8 kHz）根据SYTOX Green和细胞荧光标记分选含死靶或活靶的液滴；分选后液滴破乳，回收细胞提取基因组DNA，PCR扩增sgRNA。
  4. **数据分析**：使用MAGeCK进行差异sgRNA富集分析，基因水平统计聚合多个供体结果。
- **算法流程（文字说明）**：T细胞转导sgRNA文库 → Cas9核糖核蛋白电转导 → 扩增14天 → 与靶细胞共封装于液滴 → 孵育90分钟 → FADS分选死靶/活靶液滴 → 破乳、提取gDNA → 两轮PCR添加索引 → 高通量测序 → MAGeCK计算log2倍变化 → z-score标准化 → 基因级z-score中位数 → 与非靶向对照比较，鉴定正/负调控因子。

### 实验设计
- **数据集与场景**：
  - 原代人类CD8⁺ T细胞（来自健康供体，磁珠分选后纯化记忆亚群）。
  - 靶细胞：JeKo-1（CD19阳性淋巴瘤），使用Blinatumomab（CD19×CD3双特异性抗体）介导杀伤。
  - 其他验证系统：抗CD19 CAR-T细胞；1G4 TCR（识别NY-ESO-1/HLA-A*02:01）用于固体肿瘤模型（A375黑色素瘤、Huh7肝癌球体）。
- **基准对比**：
  - 对照组：非靶向对照（NTC）sgRNA；TCR缺失（TRAC/TRBC敲除）作为杀伤缺失对照。
  - 已知正调控因子（如CD3D、LCK、ZAP70等）和已知负调控因子（如PTEN、RASA2、FOXO1）的恢复作为平台验证基准。
- **对比方法**：未与传统阵列式筛选直接对比，但通过正交试验（bulk共培养、成像流式、体内模型）验证候选基因的效应。

### 资源与算力
- 论文中**未明确提及使用的GPU型号、数量、训练时长**等算力信息。
- 所涉计算资源限于MAGeCK分析、R统计绘图、Illumina MiSeq测序数据预处理，均属常规生物信息学分析，无需深度学习训练。

### 实验数量与充分性
- **数量**：
  - 筛选阶段：14次独立筛选（来自至少5个供体，每批不同供体），每次产生约2000万液滴，其中约75万含效应-靶细胞对的“有效事件”。
  - 验证阶段：包括液滴杀伤实验（多个供体重复）、bulk共培养（多效靶比、多时间点）、肿瘤球成像、流式免疫表型、磷酸化印迹、定量蛋白质组学（4个供体，三重复）、靶向代谢组学、体内小鼠模型（每组10-13只，两个独立实验）。
  - 消融实验：RPTOR、RHEB、AFAP1L2、PTEN、FOXO1、RASA2等基因分别验证。
- **充分性**：实验设计较为全面，覆盖从体外单细胞到体内过继转移，从血液肿瘤到实体瘤，从瞬时表型到长期效果。统计方法合理（Welch t检验、Benjamini-Hochberg校正、MAGeCK）。但筛选文库仅针对791个特定基因（TCR信号、膜运输等），非全基因组，可能遗漏其他关键调控因子。

### 论文的主要结论与发现
- **建立了首个可解析单细胞交互的混合CRISPR筛选平台**，成功应用于原代人类CD8⁺ T细胞，鉴定已知的正调控因子（如TCR组件、钙信号、溶颗粒因子、转录因子EOMES）和负调控因子（PTEN、RASA2、FOXO1、SOCS1）。
- **发现两个新负调控因子**：AFAP1L2（肿瘤浸润T细胞中富集的适配子）和RPTOR（mTORC1核心组分）。
- **揭示mTORC1抑制可增强快速杀伤**：基因敲除RPTOR或RHEB加速早期靶细胞杀伤，同时降低mTORC1信号（p-S6K减少）、增加AKT Ser473磷酸化、减弱合成代谢（氨基酸/脂质合成酶下调、代谢物累积），但降低T细胞增殖能力。
- **瞬态药理抑制优于永久敲除**：短暂rapamycin处理（8天体外扩增）重现快速杀伤表型，并在NSG小鼠A375肿瘤模型中显著抑制肿瘤生长、延长生存，而永久基因敲除因增殖缺陷无益。

### 优点
1. **创新性**：首次将液滴微流控与CRISPR混合筛选结合，解决细胞毒性T细胞杀伤这一非细胞自主过程的单细胞遗传解析难题。
2. **功能性**：实现了扰动与靶细胞命运的物理配对和表型读出，比传统混池筛选更贴近生物过程。
3. **普适性**：平台适用于不同识别模式（双特异性抗体、CAR、TCR）和肿瘤类型（血液、实体瘤）。
4. **机制洞察**：意外发现mTORC1负调控快速杀伤，并阐明其通过解除负反馈上调AKT、抑制合成代谢来实现表型转换，为免疫治疗提供新策略。

### 不足与局限
1. **文库覆盖不全**：只靶向791个候选基因，未进行全基因组筛选，可能遗漏大量调控因子。
2. **体外窗口短**：90分钟杀伤窗口仅捕获早期快速杀伤事件，无法鉴定影响持久杀伤或记忆分化的基因。
3. **体内验证有限**：仅使用一个A375肿瘤模型和一种TCR，且未测试原位或转移模型；rapamycin处理方案未优化（剂量、时序）。
4. **机制不完全**：mTORC1抑制如何通过AKT信号加速早期杀伤的分子细节（如细胞骨架重组、溶胞极性等）未完全阐明；AFAP1L2的作用机制未深入。
5. **潜在偏差**：筛选依赖于Blinatumomab介导的杀伤和JeKo-1细胞，可能引入特定靶细胞或接合子依赖性；原代T细胞供体差异大，但已通过多供体聚合来缓解。
6. **应用限制**：永久基因编辑（如RPTOR KO）因增殖缺陷不利于体内持久，瞬态抑制的转化方案（如CAR-T制造中加rapamycin）需进一步优化和安全性评估。

（完）
