---
title: The Fas-FADD-caspase-8 axis is a cancer cell-intrinsic determinant of cytotoxic lymphocyte-mediated killing
title_zh: Fas-FADD-caspase-8轴是癌症细胞内在的细胞毒性淋巴细胞杀伤决定因子
authors: "Solli, E., Wang, S., Wei, Q., Saidu, N. E. B., Tasken, K., Li, Y."
date: 2026-06-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.14.732110v1.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 发现Fas-FADD-caspase-8轴是细胞毒性淋巴细胞杀伤的癌细胞内在决定因素，直接相关免疫抵抗机制
tldr: 通常认为细胞毒性淋巴细胞通过死亡受体和穿孔素-颗粒酶途径激活执行caspase诱导癌细胞凋亡。本研究系统敲除关键细胞死亡介质发现，执行caspase缺失仅导致有限抵抗。全基因组CRISPR筛选揭示Fas-FADD-caspase-8轴是癌细胞内在决定因子，其功能不依赖经典凋亡或非凋亡通路，提示caspase-8通过其他底物或机制促进杀伤。
source: biorxiv
selection_source: fresh_fetch
motivation: 探究癌细胞内在决定其对细胞毒性淋巴细胞杀伤敏感性的关键因子，超越已知的执行caspase。
method: 在细胞毒性淋巴细胞杀伤体系中系统性敲除关键死亡介质，并在执行caspase缺陷细胞中进行全基因组CRISPR筛选。
result: 发现Fas-FADD-CASP8轴的破坏赋予显著杀伤抵抗，即使缺失执行caspase仍存在。
conclusion: Fas-FADD-CASP8轴是癌细胞杀伤敏感性的核心决定因素，其功能不能完全被经典凋亡或非凋亡通路解释。
---

## 摘要
细胞毒性淋巴细胞通过死亡受体-配体相互作用和穿孔素-颗粒酶途径诱导癌细胞死亡。这些途径通常被认为汇聚于执行者半胱天冬酶的激活以驱动凋亡。在这里，我们采用还原论方法系统性地破坏细胞毒性淋巴细胞杀伤系统中的关键细胞死亡介质，以定义它们在决定癌细胞命运中的作用。我们发现，执行者半胱天冬酶的缺失仅赋予对细胞毒性淋巴细胞介导的杀伤的有限抵抗。为了识别在超越执行者半胱天冬酶功能之外的癌细胞内在调节因子，我们在执行者半胱天冬酶缺陷细胞中进行了无偏的全基因组CRISPR筛选。出乎意料的是，即使在缺乏执行者半胱天冬酶的情况下，破坏Fas或FADD——死亡受体途径的核心组分——也能赋予对细胞毒性淋巴细胞介导的杀伤的显著抵抗。这种抵抗在进一步破坏Fas-FADD-caspase-8（CASP8）信号传导的已知下游介质后仍然存在。总之，这些发现将Fas-FADD-CASP8轴确定为对细胞毒性淋巴细胞介导的杀伤易感性的核心癌细胞内在决定因子，其功能不能完全由经典的凋亡或非凋亡效应途径解释。我们的结果进一步表明，CASP8参与额外的下游底物或机制来促进细胞毒性淋巴细胞诱导的癌细胞死亡。

## Abstract
Cytotoxic lymphocytes induce cancer cell death through death receptor-ligand interactions and the perforin-granzyme pathway. These pathways are generally thought to converge on the activation of executioner caspases to drive apoptosis. Here, we employed a reductionist approach to systematically disrupt key cell death mediators in a cytotoxic lymphocyte killing system to define their roles in determining cancer cell fate. We found that loss of executioner caspases conferred only limited resistance to cytotoxic lymphocyte-mediated killing. To identify cancer cell-intrinsic regulators that function beyond executioner caspases, we performed unbiased genome-wide CRISPR screens in executioner caspase-deficient cells. Unexpectedly, disruption of Fas or FADD--core components of the death receptor pathway--conferred substantial resistance to cytotoxic lymphocyte-mediated killing even in the absence of executioner caspases. This resistance persisted following additional disruption of known downstream mediators of Fas-FADD-caspase-8 (CASP8) signaling. Together, these findings identify the Fas-FADD-CASP8 axis as a central cancer cell-intrinsic determinant of susceptibility to cytotoxic lymphocyte-mediated killing whose function is not fully explained by canonical apoptotic or non-apoptotic effector pathways. Our results further suggest that CASP8 engages additional downstream substrates or mechanisms to promote cytotoxic lymphocyte-induced cancer cell death.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：细胞毒性淋巴细胞（CTL和NK细胞）通过死亡受体-配体相互作用（如FasL-Fas）和穿孔素-颗粒酶途径杀死癌细胞。传统观点认为这些途径最终通过激活执行者半胱天冬酶（如caspase-3, caspase-7）导致凋亡。但作者发现，即使缺失执行者半胱天冬酶，癌细胞仍能被有效杀伤。因此，需要明确：除了执行者半胱天冬酶，还有哪些癌细胞内在因子决定其对杀伤的敏感性？哪些细胞死亡机制真正重要？
- **背景意义**：理解癌细胞免疫逃逸的内在机制对于改进免疫治疗（如CAR-T、TCR-T、NK细胞治疗）至关重要。如果癌细胞通过灭活Fas-FADD-CASP8轴来抵抗杀伤，这可能是肿瘤耐药的新机制。

### 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：采用还原论策略，系统性地敲除已知的死亡相关基因，构建多重基因敲除细胞系，然后进行无偏的全基因组CRISPR筛选，以发现执行者半胱天冬酶之外的关键死亡调节因子。
- **关键技术细节**：
  - **细胞系统**：使用小鼠P815肥大细胞瘤细胞（表达FcγR，可通过抗CD3抗体桥接原发性人CD8+ CTL进行杀伤）和人HeLa细胞（与NK-92细胞共培养）。
  - **遗传敲除**：利用CRISPR-Cas9技术逐一或组合敲除目标基因（如Casp3, Casp7, Mlkl, Bid, Gsdme, Fas, Fadd, Casp8, Sec62），通过Western blot和流式验证。
  - **全基因组CRISPR筛选**：在Casp3-/-和Casp3-/-Mlkl-/-Bid-/-背景的P815细胞中转入Brie文库（4 gRNA/基因），与CTL共培养选择存活细胞，进行NGS测序，用MAGeCK-VISPR分析富集gRNA。
  - **杀伤活性定量**：癌细胞稳定表达ZsGreen1或EGFP，通过活细胞成像系统（Incucyte）实时监测绿色荧光面积的变化来反映细胞存活/死亡，避免了传统凋亡/坏死检测方法的局限性。
  - **TCGA数据挖掘**：从GDC数据库提取简单体细胞突变（SSM）频率，比较CASPs、BID、MLKL等基因的突变频率。

### 3. 实验设计：数据集/场景、基准、对比方法
- **数据集/场景**：
  - **场景1**：小鼠P815细胞 + 原代人CD8+ CTL（抗CD3桥接）。
  - **场景2**：人HeLa细胞 + NK-92细胞。
  - **临床数据**：TCGA pan-cancer数据集（18,289例），分析简单体细胞突变频率。
- **基准**：WT细胞（或Casp3-/-背景）对CTL/NK杀伤的敏感性作为基准。
- **对比方法**：
  - 对比基因敲除细胞系（单敲、双敲、三敲、四敲）与对照的存活曲线。
  - 利用CRISPR筛选获得富集基因（如Fas, Fadd, Casp8, Sec62）并与已知FcγR相关正对照比较。
  - 药理学抑制：使用ferrostatin-1抑制ferroptosis。

### 4. 资源与算力
- 文中未明确说明使用的GPU型号、数量或训练时长。仅提到NGS测序在NovaSeq X平台进行（每个样品2000-3000万reads）。CRISPR筛选数据分析采用MAGeCK-VISPR，无需大量GPU算力。活细胞成像使用Incucyte S3或S5系统。未提及深度学习或大模型训练。

### 5. 实验数量与充分性
- **实验组数量**：
  - 基因敲除验证：Western blot确认每个敲除（至少重复）。
  - CRISPR筛选：两个独立筛选（Casp3-/-背景4个生物重复；Casp3-/-Mlkl-/-Bid-/-背景3个生物重复），每个重复进行至少两轮CTL选择。
  - CTL杀伤实验：每个敲除细胞系至少两个独立实验，每个实验含3个技术重复。
  - NK杀伤实验：类似设计。
  - 药理学抑制：ferrostatin-1处理，有对照。
  - TCGA分析：全癌种数据，手动提取。
- **充分性评价**：
  - **充分**：多基因组合敲除（单、双、三、四敲）系统解析了各通路的贡献；CRISPR筛选结果在两种不同基因背景中一致，重复性好；在两种独立杀伤系统（CTL vs NK）中验证，增强了泛化性；TCGA数据支持临床相关性。
  - **客观公平**：杀伤定量基于荧光面积实时监测，避免了传统终点法偏差；但未比较其他量化方法（如LDH释放、ATP法）。
  - **潜在偏差**：仅使用P815和HeLa两种细胞系，可能无法代表所有癌细胞类型；未在体内模型中验证。

### 6. 论文的主要结论与发现
1. **执行者caspase（CASP3/7）的缺失仅赋予微小杀伤抵抗**：Casp3-/- P815细胞几乎被完全杀伤，说明存在CASP3非依赖死亡机制。
2. **全基因组CRISPR筛选鉴定Fas-FADD-CASP8为核心抵抗因子**：即使在Casp3-/-或Casp3-/-Mlkl-/-Bid-/-背景下，Fas/Fadd/Casp8的破坏均导致显著存活优势。
3. **其他死亡途径贡献有限**：Mlkl（necroptosis）部分贡献；Gsdme（pyroptosis）无明显贡献；Ferroptosis抑制剂无效；Bid缺失增加部分抵抗，但不足以完全保护。
4. **Fas-FADD-CASP8的功能超越已知下游通路**：在同时缺失CASP3/7、MLKL、BID后，额外敲除Fas/FADD/CASP8仍大幅提高存活，提示CASP8存在未知底物/机制。
5. **临床相关性**：TCGA数据显示CASP8在癌症中突变频率（1.91%）远高于CASP3、CASP7、BID，支持其作为关键免疫抵抗开关。

### 7. 优点
- **方法创新**：采用还原论+无偏CRISPR筛选的结合，系统解构了多条死亡通路的相对贡献，避免了单一通路研究的偏向性。
- **系统全面**：同时考虑了凋亡、necroptosis、pyroptosis、ferroptosis、MOMP，并且逐步叠加敲除，逻辑严密。
- **定量客观**：利用内源荧光蛋白实时成像，避免依赖于CASP3/7活性的检测方法，适用于多种死亡形式。
- **跨系统验证**：在P815-CTL和HeLa-NK两个独立系统中验证，并观察一致结果，提高结论可靠性。
- **临床数据支撑**：TCGA突变频率分析为研究发现提供了临床意义。

### 8. 不足与局限
- **细胞系局限性**：仅使用了小鼠P815和人HeLa两种癌细胞系，未在更多人类癌细胞（如黑色素瘤、结直肠癌等）中测试，泛化性受限。
- **未鉴定CASP8新底物**：作者推测存在未知底物但未进行底物组学或生化验证，机制仍需深入。
- **缺乏体内实验**：所有数据基于体外共培养，未使用小鼠肿瘤模型验证Fas-FADD-CASP8缺失对免疫治疗抵抗的影响。
- **未排除其他死亡受体**：仅关注Fas，但TNF-R和TRAIL-R也可能参与，且未检测其贡献。
- **CRISPR筛选可能遗漏**：Brie文库覆盖率（4 gRNA/基因）可能无法完全覆盖所有调控因子，且筛选只在特定基因背景进行，可能存在其他关键因子未被发现。
- **对临床解释有限**：虽然CASP8突变频率高，但尚未建立因果关系或功能验证是否直接导致免疫逃逸。

（完）
