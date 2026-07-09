---
title: Driver-associated transcriptional rewiring reveals conditional genetic vulnerabilities in cancer
title_zh: 驱动基因相关的转录重编程揭示癌症中的条件性遗传脆弱性
authors: "Geraghty, S., Boyer, J. A., Fazel-Zarandi, M., Arzouni, N., Ryseck, R.-P., McBride, M. J., Parsons, L. R., Rabinowitz, J. D., Singh, M."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.1101/2024.11.20.624509v2.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 整合计算框架解析癌症驱动突变导致的转录重编程
tldr: 癌症驱动基因突变引发广泛转录变化，但识别其下游条件性脆弱性困难。Dyscovr框架整合原发肿瘤多组学数据，鉴定驱动相关转录改变，并结合细胞系数据优先排序特异性或协同杀伤基因。在泛癌和19种肿瘤类型中发现数百个脆弱性，实验验证KBTBD2抑制可增强PI3K抑制剂在PIK3CA突变乳腺癌中的疗效。该平台为连接驱动突变与治疗靶点提供资源。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-20-624509-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1894, \"height\": 1580, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-20-624509-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1927, \"height\": 1806, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-20-624509-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1717, \"height\": 1301, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-20-624509-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1956, \"height\": 1525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-1101-2024-11-20-624509-v2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1727, \"height\": 2104, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-1101-2024-11-20-624509-v2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1713, \"height\": 577, \"label\": \"Table\"}]"
motivation: 现有方法难以从驱动基因突变引发的转录变化中识别有治疗潜力的条件性遗传脆弱性。
method: Dyscovr整合原发肿瘤的突变、表达、拷贝数、甲基化和临床数据，结合细胞系数据优先排序在驱动突变背景下的脆弱基因。
result: 在泛癌和19种肿瘤类型中发现数百个条件性脆弱基因，并实验验证KBTBD2是PIK3CA突变乳腺癌中PI3K抑制剂的协同靶点。
conclusion: Dyscovr提供计算平台和资源，连接驱动突变与条件性脆弱性，指导实验和临床治疗研究。
---

## 摘要
癌症驱动基因的突变会引发广泛的转录变化，这些变化反映了细胞状态的改变，并可能揭示相关的遗传脆弱性。然而，要确定哪些基因因癌症改变而失调，以及其中哪些代表治疗机会，仍然具有挑战性。在此，我们提出Dyscovr，一个整合的计算框架，它利用原发肿瘤的体细胞突变、基因表达、拷贝数改变、甲基化和临床数据，识别与驱动基因相关的转录变化。然后，Dyscovr将这些转录变化作为生物学依据的起点，与癌细胞系数据整合，优先考虑那些在驱动基因突变特定背景下或与驱动抑制联合使用时，其抑制被预测可降低活力的基因。Dyscovr在泛癌和19种肿瘤类型中应用，揭示了数百种这样的条件性脆弱性。作为案例研究，我们新发现并实验验证了KBTBD2，其抑制可增强PI3K抑制剂在PIK3CA突变乳腺癌细胞系中的疗效。Dyscovr软件（github.com/Singh-Lab/Dyscovr）和预测结果（dyscovr.princeton.edu）为将突变的驱动基因与条件性遗传脆弱性联系起来，并优先考虑这些关系以进行实验和治疗研究提供了平台和资源。

## Abstract
Mutations within cancer driver genes induce widespread transcriptional changes that reflect altered cellular states and can reveal associated genetic vulnerabilities. However, it remains challenging to determine which genes are dysregulated as a consequence of cancer alterations, and of these, which represent therapeutic opportunities. Here, we present Dyscovr, an integrative computational framework that leverages somatic mutation, gene expression, copy number alteration, methylation, and clinical data from primary tumors to identify driver-associated transcriptional changes. Dyscovr then uses these transcriptional changes as a biologically grounded starting point, integrating them with cancer cell line data to prioritize genes whose inhibition is predicted to reduce viability either specifically in driver-mutant contexts or in combination with driver inhibition. Applied both pan-cancer and across 19 tumor types, Dyscovr uncovers hundreds of such conditional vulnerabilities. As a case study, we newly implicate--and experimentally validate--KBTBD2 as a gene whose inhibition enhances the efficacy of PI3K inhibitors in PIK3CA-mutant breast cancer cell lines. The Dyscovr software (github.com/Singh-Lab/Dyscovr) and predictions (dyscovr.princeton.edu) provide a platform and resource for linking mutated driver genes to conditional genetic vulnerabilities and for prioritizing these relationships for experimental and therapeutic investigation.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

癌症治疗中的个性化医疗策略主要聚焦于靶向个体突变的驱动基因，但并非所有具有可靶向突变的患者都响应相应疗法，且肿瘤常通过同一通路的重激活产生耐药性。因此，需要额外的策略来增强治疗的持久性和有效性。驱动基因突变不仅影响该基因本身，还会引发瀑布式的分子事件，在全基因组范围内重编程转录程序。这些转录变化可能揭示在驱动突变背景下功能上相关的失调基因，这些基因可能构成候选治疗靶点。然而，如何从这些转录变化中区分出具有治疗潜力的条件性遗传脆弱性（即抑制该基因在突变背景下选择性杀伤肿瘤，或与驱动抑制协同杀伤）是一个关键挑战。现有方法要么仅局限于已知网络邻近基因，要么未考虑关键的混杂因素（如拷贝数、甲基化、免疫浸润等），且难以同时捕捉驱动突变与全转录组的关联以及后续的遗传相互作用。

## 2. 论文提出的方法论：核心思想、关键技术细节

**核心思想**：Dyscovr是一个两阶段的计算框架，旨在将癌症驱动基因突变与下游转录失调联系起来，进而识别条件性遗传脆弱性。

**第一阶段：识别驱动相关的转录变化**
- 整合TCGA原发肿瘤的多组学数据（突变、表达、拷贝数CNA、甲基化、临床）。
- 对于每个候选靶基因t，构建多元线性回归模型：
  - 因变量：靶基因的表达水平E(t)
  - 自变量：所有频繁突变驱动基因d的突变状态(𝑈_d)（二元）、CNA(𝐶_d)、甲基化(𝑌_d)；靶基因自身的突变、CNA、甲基化；以及样本级协变量（年龄、性别、治疗史、肿瘤亚型、免疫浸润分数、基因型主成分、肿瘤纯度、非同义突变负荷等）。
  - 目标：获取每个驱动基因突变系数α_d的显著性，经多重假设校正后得到驱动-靶基因关联对（q<0.2，泛癌使用q<0.01）。
- 该方法与eQTL类似但针对体细胞突变进行了关键改编：聚合基因内非同义突变、在同一模型中纳入多个突变基因、整合癌症特异性分子和临床混杂因素。

**第二阶段：识别条件性遗传脆弱性**
- 对于第一阶段中在泛癌和至少一个癌种中均显著的驱动-靶基因对，利用DepMap（Cancer Dependency Map）的CRISPR敲除筛选数据。
- 对于每个驱动基因d和靶基因t，拟合回归模型：
  - 因变量：敲除t后的细胞活力(V_t)
  - 自变量：驱动基因d的突变状态(U_d)、表达水平(E_d)，以及癌种类别作为协变量。
- 通过经验布朗方法合并U_d和E_d的显著性，得到组合p值，校正后q<0.2作为遗传相互作用候选。
- 根据驱动基因类型（肿瘤抑制因子/癌基因）和系数方向进一步分类：
  - 肿瘤抑制因子（如TP53）：仅关注“获得性脆弱性”（突变状态与活力负相关，表达与活力正相关）。
  - 癌基因（如PIK3CA, KRAS）：分为“获得性脆弱性”（突变/高表达与活力负相关）和“共靶向脆弱性”（突变/高表达与活力正相关，即联合抑制更有效）。

**关键技术细节**：
- 处理多重共线性：去除与驱动突变高度相关的亚型变量，并使用方差膨胀因子（VIF）剔除其他共线变量。
- 数据预处理：表达数据量化归一化；突变仅保留非同义突变并排除超突变样本；CNA做log2归一化；甲基化转换为M值。
- 基准测试：与muTarget（Mann-Whitney U检验）和xseq（层次贝叶斯方法）比较。

## 3. 实验设计：数据集、Benchmark、对比方法

**数据集**：
- 第一阶段：TCGA（癌症基因组图谱），共6378个原发肿瘤样本，涵盖32种癌症类型，具有匹配的突变、表达、CNA、甲基化和临床数据。在19种样本量≥75的癌种中分别进行癌种特异性分析。
- 验证数据集：METABRIC乳腺癌队列（854个样本），用于跨队列复现TCGA-BRCA结果。
- 第二阶段：DepMap（v23Q2）的693个癌细胞系，包含CRISPR基因依赖性、突变和表达数据。

**基准测试（Benchmark）**：
- 富集分析：检验Dyscovr识别的靶基因是否富集于已知转录靶标（DoRothEA）、TP53靶标（Fischer数据集）、癌症基因目录（CGC）、已知通路（KEGG, Reactome）。
- 与muTarget对比：发现muTarget产生严重偏斜的p值（70.3%的基因对TTN显著），且未校正免疫细胞浸润导致大量假阳性。
- 与xseq对比：在限定为xseq可测试基因集后，Dyscovr在富集已知TP53靶标方面优于xseq。

**对比方法**：
- muTarget：基于Mann-Whitney U检验的简单方法。
- xseq：利用基因交互网络作为先验的层次贝叶斯方法。
- 控制实验：使用TTN（高频突变但非驱动基因）和随机化表达数据，验证Dyscovr的特异性。

**遗传相互作用验证**：
- 使用BioGRID和手工筛选的文献遗传交互数据集作为金标准，检验Dyscovr预测的遗传相互作用是否富集已知交互。
- 使用SynLethDB数据库中的合成致死关系进行富集分析。
- 实验验证：针对PIK3CA-KBTBD2对，在MCF7乳腺癌细胞系中通过siRNA敲低KBTBD2，结合PI3Kα抑制剂（alpelisib和RLY-2608），测量细胞生长和通路信号变化。

## 4. 资源与算力

论文未明确说明使用何种GPU或训练时长。计算主要基于R语言和Python，使用了线性回归（speedglm包）、基因集富集分析（fgsea）等标准统计方法。所有代码开源（github.com/Singh-Lab/Dyscovr），结果可通过网站（dyscovr.princeton.edu）交互查询。未提供具体算力需求信息。

## 5. 实验数量与充分性

**实验组别**：
- 第一阶段：泛癌层面检测了16,447个靶基因×4个驱动基因；19个癌种各自检测了相应驱动基因组合。总共产生大量关联对，仅报道显著关联。
- 控制实验：TTN（仅3个显著基因）、随机化表达（无显著基因）、突变类型限制（热点/无义突变）结果相似。
- 跨队列验证：TCGA-BRCA与METABRIC的Spearman相关系数：PIK3CA为0.84，TP53为0.62，且超几何检验显著。
- 基准测试：与muTarget和xseq比较，评估富集性能、p值分布、重叠等。
- 第二阶段：对TP53、PIK3CA、KRAS分别筛选了来自第一阶段的显著靶基因（分别为1503、571、237个），在其中检测遗传相互作用（分别有375、54、69个显著遗传相互作用）。富集分析检验金标准遗传交互和SynLethDB。
- 实验验证：仅针对一个候选（KBTBD2）进行了体外验证（siRNA敲低+药物处理），包括qPCR确认敲低效率、细胞生长实验、Western blot检测通路蛋白磷酸化变化。未进行多个候选或多细胞系验证。

**充分性与公平性**：
- 总体实验数量充足：涵盖泛癌和多个癌种，控制实验充分证明了方法的特异性。
- 基准测试客观：与当前常用的两种方法进行了系统比较，展示了优势。
- 局限性：实验验证仅聚焦于一个案例，缺乏对更多预测的高通量验证。第二阶段仅对三个泛癌驱动基因进行了分析，癌种特异性驱动基因的遗传相互作用未系统评估。此外，回归模型假设线性关系，可能遗漏非线性模式。

## 6. 论文的主要结论与发现

- Dyscovr在泛癌和19种癌种中识别出数百个驱动突变关联的转录失调靶基因，这些靶基因显著富集于已知癌症基因、转录靶标和功能通路，且优于现有方法。
- 对于TP53、PIK3CA、KRAS，Dyscovr进一步鉴定了数百个候选遗传相互作用，包括获得性脆弱性和共靶向脆弱性，许多预测与已知文献一致或具有潜在药物可及性。
- 实验验证发现：在PIK3CA突变乳腺癌细胞MCF7中，敲低KBTBD2显著增强PI3Kα抑制剂alpelisib的细胞毒性，并将生长抑制转化为细胞死亡；联合处理导致mTORC1下游信号（pS6、p4EBP1、cyclin D1）更深层抑制。KBTBD2被提出作为PI3K-AKT通路的正调控因子，其下调可能是对PIK3CA激活的负反馈破坏的结果。
- Dyscovr提供了一个从驱动突变到可测试治疗假设的系统性框架，其预测可通过网站和开源代码公开获取。

## 7. 优点：方法或实验设计上的亮点

- **全面的混杂控制**：首次在驱动-靶基因关联分析中同时考虑了CNA、甲基化、免疫浸润、肿瘤纯度、基因型背景、亚型等多种混杂因素，大大减少了假阳性。
- **双向治疗策略**：创新地区分了“获得性脆弱性”（单药靶向）和“共靶向脆弱性”（联合靶向），尤其弥补了传统合成致死范式对癌基因靶点识别不足的问题。
- **生物学基础优先**：将转录失调作为起点，而非暴力筛选所有基因，提高了候选基因的生物学相关性和可解释性。
- **跨数据源整合**：连接原发肿瘤转录组学与功能基因组筛选，利用临床相关数据驱动发现。
- **可复现性与易用性**：提供开源代码和交互式网站，使其他研究者可探索和验证预测。
- **实验验证**：以KBTBD2为例，从计算预测到机制验证，展示了完整的转化路径。

## 8. 不足与局限

- **实验验证覆盖有限**：仅验证了一个基因（KBTBD2）和一个细胞系（MCF7），缺乏对多个预测脆弱性的大规模实验筛选，无法评估整体预测的阳性预测率。
- **驱动基因频率限制**：分析局限于≥5%突变频率的驱动基因，罕见驱动突变无法纳入，限制了在特定癌种或亚型中的应用。
- **线性模型假设**：回归模型假设线性关系和独立误差，可能无法捕捉复杂非线性或交互效应。
- **第二阶段的细胞系数据兼容性**：DepMap细胞系与TCGA原发肿瘤在遗传背景、微环境等方面存在差异，可能存在跨平台偏差。
- **癌种特异性分析**：第二阶段仅分析了三个泛癌驱动基因，未对癌种特异性驱动基因进行遗传相互作用分析，部分可能具有重要治疗意义的癌种特异性关系被遗漏。
- **药物敏感性预测的间接性**：Dyscovr基于基因敲除依赖性推断遗传相互作用，并未直接模拟药物抑制效果，从基因到药物的转化需要额外验证。
- **生存分析仅针对一个靶基因**：未对全部分析结果进行生存关联验证，作为预后标志物的潜力尚不完全清楚。

（完）
