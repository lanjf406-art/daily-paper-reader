---
title: Systematic elucidation and pharmacologic targeting of non-oncogene dependencies in imatinib-resistant gastrointestinal stromal tumor
title_zh: 伊马替尼耐药胃肠道间质瘤中非癌基因依赖性的系统阐明与药理学靶向
authors: "Mundi, P. S., Grunn, A., Kojadinovic, A., Pampou, S., Karan, C., Realubit, R., Caescu, C. I., Hibshoosh, H., Aburi, M., Alvarez, M. J., Ingham, M., Evans, D., Rothschild, S., Schwartz, G. K., Califano, A."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.1101/2025.10.12.681609v2.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 通过网络方法和单细胞分析阐明GIST伊马替尼耐药机制
tldr: 伊马替尼耐药是晚期胃肠道间质瘤（GIST）治疗的主要挑战。本研究开发了突变无关的网络方法，系统鉴定主调节因子（MR）作为非癌基因依赖性。通过无监督MR聚类分析34个患者样本，发现耐药肿瘤形成独立簇；单细胞RNA分析显示耐药相关MR活性在进展肿瘤中富集。高通量药物筛选识别出6种候选药物逆转耐药MR活性，在两种PDX模型中linifanib、selinexor和selumetinib显著抑制肿瘤生长。该策略为克服GIST耐药提供了新途径。
source: biorxiv
selection_source: fresh_fetch
motivation: 伊马替尼耐药后缺乏有效疗法，需系统发现非癌基因依赖性作为新靶点。
method: 结合MR聚类分析患者肿瘤和单细胞RNA谱，通过高通量药物转录响应筛选候选药，并在PDX模型中验证。
result: 发现linifanib、selinexor和selumetinib能逆转耐药GIST的MR活性并显著抑制PDX肿瘤生长。
conclusion: 该网络方法可系统发现并靶向非癌基因依赖性，为克服GIST耐药提供新策略。
---

## 摘要
使用伊马替尼和其他KIT靶向药物治疗胃肠道间质瘤（GIST）显著改善了患者的预后。然而，大多数晚期GIST患者最终会产生伊马替尼耐药并死于该疾病。我们开发了不依赖突变、基于网络的方法，系统性地阐明并药理学靶向癌细胞中的主调控因子（MR）蛋白——即关键的非癌基因依赖性。对34例GIST患者肿瘤样本进行无监督的基于MR的聚类分析，得到了两个聚类，其中一个包含了所有伊马替尼耐药肿瘤。对9例高风险GIST的单细胞RNA图谱分析显示，在伊马替尼治疗中发生临床进展的肿瘤含有大量富集伊马替尼耐药肿瘤MR活性特征的亚群，而具有耐药相关突变但无明显进展的肿瘤则显示出较小且大小可变的富集亚群。通过两种GIST细胞系对FDA批准和后期实验药物进行转录反应的高通量分析，确定了六种候选药物，这些药物能够逆转伊马替尼耐药GIST的MR活性。预测结果在两个伊马替尼耐药的患者来源异种移植（PDX）模型中得到了验证。最佳预测药物利尼法尼在两种PDX模型中、在宽剂量范围内均诱导了显著的肿瘤生长抑制；塞利尼索和司美替尼与伊马替尼相比也有效。我们确认了这些药物在体内逆转了MR活性，而无效药物则没有此作用。

## Abstract
Treatment of gastrointestinal stromal tumor (GIST) with imatinib and other KIT-targeting drugs has improved outcomes significantly. However, most patients with advanced GIST eventually develop imatinib resistance and succumb to disease. We have developed mutation-agnostic, network-based methodologies to systematically elucidate and pharmacologically target Master Regulator (MR) proteins--critical non-oncogene dependencies--in cancer cells. Unsupervised, MR-based clustering of 34 GIST patient tumor samples produced two clusters, one of which contained all imatinib-resistant tumors. Analysis of 9 single-cell RNA profiles of high-risk GIST revealed that tumors with clinical progression on imatinib harbored large subpopulations enriched for the MR-activity signature of imatinib-resistant tumors, while tumors with resistance-associated mutations but without overt progression showed smaller, variably sized enriched subpopulations. High-throughput profiling of transcriptional responses by two GIST cell lines to FDA-approved and late-stage experimental drugs identified six candidate drugs that reversed the MR activity of imatinib-resistant GIST. Predictions were validated in two imatinib-resistant, patient-derived xenograft (PDX) models. The top prediction, linifanib, induced marked tumor growth inhibition in both PDXs across a wide dose range; selinexor and selumetinib were also effective compared to imatinib. We confirmed in vivo MR-activity reversal by these drugs, but not by ineffective drugs.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义

- **研究动机**：胃肠道间质瘤（GIST）是一类对伊马替尼等KIT靶向药物高度依赖的肿瘤。然而，大多数晚期GIST患者最终会因获得性耐药而死亡。现有治疗手段（如舒尼替尼、瑞戈非尼）效果有限，急需新的治疗策略。
- **核心问题**：伊马替尼耐药后，肿瘤细胞是否依赖非癌基因性的主调节因子（Master Regulator, MR）维持恶性状态？能否通过系统性地鉴定这些MR并靶向它们来逆转耐药？
- **整体含义**：该研究提出了一种不依赖驱动基因突变、基于转录组网络分析的方法，能够系统阐明伊马替尼耐药GIST的非癌基因依赖性，并成功预测出多个可逆转耐药状态的候选药物，为克服GIST耐药提供了全新范式。

## 2. 论文提出的方法论

### 核心思想

- 利用VIPER算法及其扩展metaVIPER，从基因表达数据推断蛋白质的调控活性（而非仅仅看mRNA水平）。通过分析肿瘤中异常激活或失活的蛋白质，鉴定出维持肿瘤状态的关键MR。
- 通过OncoTarget和OncoTreat两个互补策略，筛选能够靶向这些MR的药物：
  - **OncoTarget**：识别具有高亲和力抑制剂的MR，直接匹配已知药物。
  - **OncoTreat**：通过药物在体外细胞系中诱导的转录反应，评估药物能否逆转肿瘤特异的MR活性特征（前25个激活+前25个失活MR组成的片段）。

### 关键技术细节

1. **网络构建**：使用ARACNe算法，基于TCGA等多个癌症类型的RNASeq数据（≥100样本）逆向工程转录调控网络。
2. **蛋白质活性推断（VIPER/metaVIPER）**：
   - 对每个样本计算相对于参考组（如数据集质心）的差异基因表达谱（dGES）。
   - 利用VIPER的aREA（analytic-rank based enrichment analysis）检验，计算每个调控蛋白的转录靶点在dGES中的富集程度，得到归一化富集分数（NES）作为活性度量。
   - 因GIST缺乏大样本专属网络，使用metaVIPER整合43个癌症类型的网络，用Stouffer方法合并各网络结果。
3. **聚类分析**：对metaVIPER得到的蛋白质活性谱进行无监督共识聚类（ConsensusClusterPlus），采用PAM（Partition Around Medoids）算法，10,000次迭代，确定最优聚类数k=2。
4. **单细胞分析**：对9例高风险GIST的scRNA-seq数据，先分离恶性细胞（表达DOG1/ANO1，经SingleR注释和InferCNV验证），再对每细胞使用metaVIPER推断蛋白质活性，评估每个细胞对伊马替尼耐药簇（C1）特征（ImResS）的富集程度。
5. **药物扰动实验**：
   - 选择GIST-T1和GIST430两个细胞系，在亚致死浓度（EC20及1/10 EC20）下用46种（后扩展至333种）临床相关药物处理24小时，PLATE-Seq测序。
   - 对每个药物，用VIPER计算药物 vs 对照的差异蛋白质活性，作为药物机制指纹。
6. **OncoTreat预测**：对于每个患者肿瘤，取其前25上调+25下调MR，在药物指纹中测试这些MR是否被逆转（即药物激活的蛋白质是肿瘤失活的MR，药物失活的蛋白质是肿瘤激活的MR），用aREA计算显著性（BH校正p<10⁻⁵）。

### 公式/算法流程

- 核心算法：VIPER的aREA公式：  
  NES = (E - μ)/σ，其中E是靶基因集的平均富集分数，μ和σ基于零假设分布计算。实际使用分析近似而非置换。
- 集成方法与聚类标准：Stouffer Z-score整合、共识聚类基于共识指数和轮廓系数。

## 3. 实验设计

### 使用数据集

- **患者肿瘤数据**：来自Life Raft Group（LRG）的34例GIST患者肿瘤（FFPE样本）的bulk RNASeq，包括10例明确伊马替尼耐药的样本。带有详细的临床注释（KIT/PDGFRA基因型、治疗史、预后等）。
- **PDX模型数据**：Crown Bioscience提供的18个GIST PDX模型的RNASeq。
- **单细胞数据**：公开的9例高风险GIST scRNA-seq数据集（GSE254762），其中3例已临床进展、4例有耐药突变但未进展、2例敏感且未进展。
- **药物扰动数据**：GIST-T1和GIST430细胞系在46种（初始）和333种（扩展）药物处理后的PLATE-Seq转录组。

### Benchmark与对比方法

- 主要对比：使用差异基因表达（dGES）而非蛋白质活性进行聚类和药物预测，结果显示不稳定且无法有效分离耐药肿瘤。
- 阴性对照：伊马替尼（已知对耐药肿瘤无效）。标准治疗瑞戈非尼作为阳性对照（但非OncoTreat预测）。

### 对比的方法

- 使用mRNA表达水平（而非蛋白质活性）进行OncoTarget和OncoTreat预测，结果无一致预测。
- 对比MAPK7 mRNA过表达作为预测linifanib敏感的替代标志，但灵敏性差。

## 4. 资源与算力

论文**未明确提及**具体的GPU型号、数量或训练时长等算力信息。只提到使用STAR、DESeq2、ARACNe、VIPER等软件包，在标准高性能计算环境中完成。

## 5. 实验数量与充分性

### 实验数量

- **患者样本聚类**：34个bulk样本的无监督聚类。
- **单细胞分析**：9例样本，每例数百至数千个恶性细胞，共分析数千个单细胞蛋白质活性。
- **药物筛选**：初始GIST430中46种药物，后扩展至333种；GIST-T1中46种。每个药物至少测试两个浓度。
- **PDX验证**：两个PDX模型（GS5106和GS5108）各自进行5个部分的治疗实验（每次有独立对照组），每个治疗组5只小鼠，部分多剂量组，另加2只/组用于药效（PD）活检。
- **药效评估**：对每个治疗组（共约16+个药物-剂量组合）进行PD活检及VIPER分析。

### 充分性与公平性

- **充分性**：从患者数据发现、体外筛选到体内验证，流程完整。验证了多个预测药物，包括阳性（linifanib、regorafenib）和阴性（panobinostat）对照。但未对所有预测药物进行多浓度测试（如crizotinib被排除）。
- **公平性**：PDX模型选择是基于OncoMatch分析，完全盲态（不知其已知耐药表型），最终匹配的模型确实耐药，避免了选择偏倚。但是，未设立随机挑选的阴性药物面板作为对照（仅用imatinib）。
- **局限性**：部分治疗组因COVID-19疫情导致小鼠死亡率高、剂量中断，影响统计效力；PD活检样本量小（2只/组），可能不足以反映异质性。

## 6. 论文的主要结论与发现

1. **伊马替尼耐药GIST存在保守的MR活性特征**：无监督聚类将34个样本分成两簇，一簇（C1）包含所有10个耐药肿瘤及6个可能高危但未进展的样本，另一簇（C2）为敏感/初治样本。该特征不依赖于特定突变。
2. **单细胞水平证实耐药特征在进展肿瘤中扩增**：在临床进展的肿瘤中，40%–62%的恶性细胞高度富集C1 MR活性特征；而在有耐药突变但未进展的肿瘤中，该比例较小且可变。
3. **预测的候选药物在PDX中有效**：
   - **Linifanib**（VEGFR2/多激酶抑制剂）：在两个PDX模型中均诱导显著肿瘤退缩（TGI 137%~169%），且在低剂量仍有效（80%~75% TGI）。
   - **Selinexor**（XPO1抑制剂）：在GS5108中TGI 45%~53%，与对照组差异显著。
   - **Selumetinib**（MEK抑制剂）：在GS5108中低剂量（50mg/kg BID）达TGI 54%，但在高剂量（100mg/kg QD）无效。
4. **体内MR活性逆转与疗效相关**：有效药物（linifanib、regorafenib、低剂量selumetinib）在PD活检中显示显著的MR活性逆转；无效药物（imatinib、panobinostat、tamoxifen等）无逆转或反而增强。Spearman ρ = -0.72（p=0.002）。
5. **OncoTarget预测的XPO1靶向药物selinexor**虽然未逆转全局MR活性，但确实抑制了XPO1本身活性，提示其机制可能不同于OncoTreat。

## 7. 优点

- **方法新颖**：不依赖已知驱动突变，而是通过系统生物学解析非癌基因依赖性，适用于耐药肿瘤等突变复杂情况。
- **多层级验证**：从患者bulk RNA到单细胞，从细胞系到PDX，从疗效到药效学，链条完整。
- **临床相关性高**：利用患者倡导组织建立的真实世界肿瘤库（LRG），样本具有详细的临床历史。
- **突变无关性**：即使在KIT野生型或PDGFRA D842V突变等原发耐药剂型中也有效。
- **对比传统方法**：展示了基于蛋白质活性比基于mRNA表达更稳健，突显VIPER的优越性。

## 8. 不足与局限

- **样本量有限**：仅34个bulk肿瘤和9例单细胞，且PDX验证仅两个模型，可能无法完全代表人群异质性。
- **药物筛选不完全**：初始药物panel仅46种，虽然后来扩展到333种，但一些预测药物（如crizotinib、AZD1775）因在PDX中不匹配被排除，说明OncoTreat对模型依赖性较强。
- **体内药效学样本量小**：每组仅2只小鼠用于PD活检，可能无法捕捉个体间差异，且未进行多次时间点分析。
- **未评估组合疗法**：虽然提出与伊马替尼联用的可能性，但未在实验中测试。
- **缺乏充分的阴性对照面板**：仅用伊马替尼作为阴性对照，未随机选取非预测药物集，无法估计假阴性率。
- **剂量问题**：部分药物的MTD与文献报道有差异（如regorafenib 10mg/kg vs 20mg/kg），可能影响疗效可比性。
- **COVID-19干扰**：部分实验因疫情导致小鼠死亡、剂量中断，影响数据质量。
- **转化前景**：linifanib虽有效，但该药因毒性问题已停止临床开发；selinexor、selumetinib有待进一步临床试验验证。
- **未进行体内基因敲除验证**：未直接验证MR在耐药中的因果作用（如CRISPR敲除）。

（完）
