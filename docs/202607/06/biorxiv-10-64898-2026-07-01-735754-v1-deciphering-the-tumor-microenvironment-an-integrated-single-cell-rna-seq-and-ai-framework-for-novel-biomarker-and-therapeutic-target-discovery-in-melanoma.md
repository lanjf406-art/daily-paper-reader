---
title: "Deciphering the Tumor Microenvironment: An Integrated Single-Cell RNA-Seq and AI Framework for Novel Biomarker and Therapeutic Target Discovery in Melanoma"
title_zh: 解析肿瘤微环境：整合单细胞RNA测序与人工智能框架用于黑色素瘤新型生物标志物及治疗靶点发现
authors: "Ostwal, R., Natarajan, E."
date: 2026-07-05
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.01.735754v1.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 单细胞肿瘤微环境AI框架研究治疗抵抗
tldr: 黑色素瘤微环境高度异质，传统测序难以解析其免疫逃逸机制。本研究构建可解释机器学习与网络生物学框架，对单细胞RNA-seq数据进行Leiden聚类，XGBoost筛选标志物，SHAP解释模型，并利用LIANA分析细胞通信。发现CD79A、MLANA等跨区室生物标志物，SERPINE1信号轴驱动免疫-基质互作，SPARC为共表达枢纽。临床验证显示CD79A高表达显著延长患者生存（44.8 vs 26.7个月），为免疫治疗分层提供新策略。
source: biorxiv
selection_source: fresh_fetch
motivation: 传统方法无法解析黑色素瘤微环境单细胞异质性及细胞互作，亟需新框架发现生物标志物与治疗靶点。
method: scRNA-seq数据经Leiden聚类、XGBoost分类器、SHAP解释、自动编码器增强及LIANA通信分析，跨队列与TCGA临床验证。
result: 鉴定CD79A、MLANA等标志物，SERPINE1-LRP1/PLAUR信号轴及SPARC枢纽；CD79A高表达显著提升总生存期。
conclusion: 可解释框架将单细胞网络与临床预后关联，为黑色素瘤免疫治疗分层提供可复现路线图。
---

## 摘要
背景：黑色素瘤是一种高度免疫原性且治疗极具挑战性的恶性肿瘤。肿瘤微环境（TME）中复杂的细胞生态系统是免疫逃逸、患者预后和治疗耐药的关键驱动因素。传统的批量测序往往无法解析这些高分辨率的细胞间动态。本研究提出了一种端到端的可解释机器学习与网络生物学框架，旨在解构TME单细胞异质性、发现新型候选生物标志物并绘制可操作的细胞间通讯网络。方法：采用多阶段计算工作流程处理来自黑色素瘤病变（GSE115978）的高质量单细胞RNA测序（scRNA-seq）表达数据。经过细胞过滤、文库大小归一化和高变基因（HVG）选择后，使用无监督Leiden聚类对细胞进行分群，并通过特征基因评分矩阵方法进行注释（Wolf等，2018；Traag等，2019）。构建了最优梯度提升树集成分类器（XGBoost）用于跨区室生物标志物筛选（Chen & Guestrin, 2016），使用SHAP（SHapley Additive exPlanations）值进行解释（Lundberg & Lee, 2017），并辅以PyTorch深度自编码器。下游系统分析包括通过gseapy（Kuleshov等，2016）进行生物学通路富集、通过LIANA（Efremova等，2020；Dimitrov等，2022）进行配体-受体通讯映射以及Pearson共表达网络分析。在独立黑色素瘤队列（GSE72056）（Tirosh等，2016b）上进行跨队列验证，并使用TCGA-SKCM队列（TCGA研究网络，2015；Davidson-Pilon, 2019）的经验患者生存数据进行预后效用的临床验证。结果：无监督Leiden聚类将细胞图谱划分为七个主要结构和免疫区室：黑色素瘤/肿瘤细胞、T细胞、B细胞、巨噬细胞、NK细胞、内皮细胞和癌症相关成纤维细胞（CAF）。训练后的XGBoost模型将CD79A、MLANA、LYZ、MFAP4和CDH5优先列为不同微环境生态位中的候选生物标志物。SHAP可解释性分析确认MLANA和S100B是肿瘤细胞身份的关键正向预测因子，同时揭示了与抗原呈递下调相关的B2M的双向分布。功能富集将凝血和上皮-间充质转化（EMT）映射为驱动恶性状态的高度失调通路。细胞间通讯分析推断出高度显著的SERPINE1信号轴指向LRP1和PLAUR受体。SPARC被识别为中枢共表达枢纽调控因子。GSE72056中的跨队列筛选证实了生物标志物在不同患者图谱中的稳定性。TCGA-SKCM队列（n=314）中的经验临床生存验证显示，CD79A的高表达与统计学显著的生存优势相关（Log-Rank p = 4.4202 × 10⁻³），中位总生存期从26.7个月延长至44.8个月。结论：本计算流程系统性地解析了TME异质性，揭示了以CD79A和MLANA为核心的稳健生物标志物特征，以及SERPINE1驱动的免疫-基质互作。CD79A保护性预后作用的发现将单细胞免疫网络直接与临床患者结局联系起来，为抗肿瘤免疫参与和免疫治疗分层提供了可复现的路线图。关键词：黑色素瘤，肿瘤微环境，单细胞RNA测序，scRNA-seq，XGBoost，SHAP，LIANA，TCGA-SKCM，CD79A，SPARC，SERPINE1，生物标志物发现，Leiden聚类

## Abstract
Background: Melanoma represents a highly immunogenic and therapeutically challenging malignancy. The complex cellular ecosystem of the tumor microenvironment (TME) acts as a critical driver of immune evasion, patient prognosis, and treatment resistance. Traditional bulk sequencing often fails to resolve these high-resolution intercellular dynamics. This investigation presents an end-to-end explainable machine learning and network biology framework designed to deconstruct TME single-cell heterogeneity, discover novel candidate biomarkers, and map actionable cell-cell communication networks. Methodology: High-quality single-cell RNA sequencing (scRNA-seq) expression data from melanoma lesions (GSE115978) were processed using a multi-phase computational workflow. Following cellular filtration, library size normalisation, and highly variable gene (HVG) selection, cells were partitioned using unsupervised Leiden clustering and annotated via signature gene scoring matrix methods (Wolf et al., 2018; Traag et al., 2019). An optimal gradient-boosted tree ensemble classifier (XGBoost) was constructed for cross-compartment biomarker screening (Chen & Guestrin, 2016), interpreted using SHAP (SHapley Additive exPlanations) values (Lundberg & Lee, 2017), and augmented with a PyTorch deep autoencoder. Downstream systems analyses included biological pathway enrichment via gseapy (Kuleshov et al., 2016), ligand-receptor communication mapping via LIANA (Efremova et al., 2020; Dimitrov et al., 2022), and Pearson co-expression network profiling. Cross-cohort validation was conducted on an independent melanoma cohort (GSE72056) (Tirosh et al., 2016b), and prognostic utility was clinically validated using empirical patient survival data from the TCGA-SKCM cohort (TCGA Research Network, 2015; Davidson-Pilon, 2019). Results: Unsupervised Leiden clustering partitioned the cellular atlas into seven major structural and immunological compartments: Melanoma/Tumor, T-Cells, B-Cells, Macrophages, NK Cells, Endothelial cells, and Cancer-Associated Fibroblasts (CAFs). The trained XGBoost model prioritized CD79A, MLANA, LYZ, MFAP4, and CDH5 as top candidate biomarkers across distinct microenvironmental niches. SHAP explainability analysis confirmed MLANA and S100B as key positive predictors of tumor cell identity, while highlighting a bidirectional distribution for B2M linked to antigen presentation downregulation. Functional enrichment mapped Coagulation and Epithelial-Mesenchymal Transition (EMT) as highly dysregulated pathways driving the malignant state. Cell-cell communication profiling inferred highly significant SERPINE1 signalling axes to LRP1 and PLAUR receptors. SPARC was identified as the central co-expression hub regulator. Cross-cohort screening in GSE72056 confirmed biomarker stability across independent patient profiles. Empirical clinical survival validation within the TCGA-SKCM cohort (n=314) demonstrated that heightened expression of CD79A correlates with a statistically significant survival advantage (Log-Rank p = 4.4202 * 10-3), extending median overall survival from 26.7 months to 44.8 months. Conclusion: This computational pipeline systematically resolves TME heterogeneity, revealing a robust biomarker signature centred on CD79A and MLANA, alongside SERPINE1-driven immune-stromal crosstalk. The discovery of the protective prognostic role of CD79A links single-cell immune networks directly to clinical patient outcomes, providing a reproducible roadmap for anti-tumour immune engagement and immunotherapeutic stratification. Keywords: Melanoma, Tumor Microenvironment, Single-Cell RNA-Seq, scRNA-seq, XGBoost, SHAP, LIANA, TCGA-SKCM, CD79A, SPARC, SERPINE1, Biomarker Discovery, Leiden Clustering

---

## 论文详细总结（自动生成）

# 论文结构化总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：黑色素瘤肿瘤微环境（TME）具有高度细胞异质性和复杂的免疫逃逸机制，传统批量测序无法解析单细胞水平下细胞间动态互作，导致现有免疫治疗（如抗PD-1）响应率仅30%-40%，缺乏可指导治疗分层的稳健生物标志物。
- **研究动机**：整合单细胞RNA测序（scRNA-seq）的高分辨率优势与可解释人工智能（AI）的预测能力，构建端到端计算框架，系统性地发现新型生物标志物、解析细胞通讯网络，并实现临床预后验证。
- **整体含义**：通过将单细胞图谱构建、机器学习特征筛选、网络生物学分析与真实患者生存数据结合，为黑色素瘤免疫治疗提供可复现的精准分层工具和新治疗靶点。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：利用scRNA-seq解析TME细胞异质性，通过监督/无监督学习联合挖掘跨区室生物标志物，结合网络生物学推断功能模块与细胞间信号，最终通过独立队列和临床生存数据验证。
- **关键技术细节**：
  - **数据预处理**：使用Scanpy进行质量控制（基因数>200、细胞数>3、线粒体比例<20%），保留7,186个细胞；对数归一化（ln(1+x)）；筛选前2,000个高变基因（HVG）。
  - **聚类与注释**：PCA降维（40个主成分），Leiden聚类（分辨率0.5）得到23个子簇；基于7个预设细胞系标志物基因集（如Melanoma: MITF/MLANA；B-Cells: CD19/CD79A等）通过`sc.tl.score_genes()`自动分配细胞类型，合并为7个主要细胞区室。
  - **AI生物标志物发现**：
    - **XGBoost分类器**：多分类任务（7类细胞），参数：n_estimators=150, learning_rate=0.05, max_depth=5，80%训练/20%测试，5折交叉验证，提取全局特征重要性。
    - **SHAP可解释性**：使用TreeExplainer对Melanoma/Tumor类别分析，展示基因正向/负向贡献方向。
    - **深度自编码器**：PyTorch实现，Adam优化器（lr=1e-3, weight decay=1e-5），60轮训练，压缩32维潜在空间。
  - **下游系统分析**：
    - 通路富集：gseapy查询GO BP 2021、KEGG 2021、MSigDB Hallmark 2020。
    - 细胞通讯：LIANA框架调用CellPhoneDB，基于未缩放原始count矩阵，p<0.05过滤。
    - 共表达网络：Pearson相关系数（前200个XGBoost特征），计算绝对均值作为连通性。
  - **临床验证**：TCGA-SKCM（n=314），基于CD79A伪批量表达中位数分为高/低组，Kaplan-Meier曲线+Log-Rank检验，使用lifelines包。

## 3. 实验设计：数据集、基准与对比方法

- **使用数据集**：
  - 发现队列：GSE115978（Tirosh et al., 2016a），包含黑色素瘤单细胞转录组。
  - 外部验证队列：GSE72056（Tirosh et al., 2016b），独立单细胞数据集，用于验证生物标志物表达稳定性。
  - 临床生存队列：TCGA-SKCM（n=314），提供真实总生存期数据。
- **基准/对比方法**：
  - 论文未设置量化对比的基准方法（如与其他机器学习模型比较AUC等），而是与已有文献定性对比：如Tirosh(2016)单细胞图谱、Sade-Feldman(2018)T细胞状态、Helmink(2020)/Cabrita(2020)B细胞/TLS研究等。XGBoost性能通过5折交叉验证ROC-AUC（0.997）自评。
- **对比方法**：无直接定量对比，仅从方法学上指出已有研究未同时整合scRNA-seq、AI、网络生物学与临床验证。

## 4. 资源与算力

- **文中未明确说明**：未提及使用的GPU型号、数量、训练时长或计算集群信息。运行环境为Python（Scanpy、XGBoost、PyTorch等），推测可在标准服务器或Google Colab上完成（作者声明提供10-cell Colab兼容流水线），但具体算力细节缺失。

## 5. 实验数量与充分性

- **实验数量**：主要实验包括：
  - 一次主发现队列聚类与注释（7类细胞）。
  - 一次XGBoost训练与5折交叉验证。
  - SHAP解释（仅对Melanoma/Tumor类别）。
  - 一次通路富集（多数据库）。
  - 一次细胞通讯分析（LIANA）。
  - 一次共表达网络（Pearson）。
  - 一次跨队列验证（GSE72056）。
  - 一次临床生存分析（TCGA-SKCM，仅对CD79A）。
- **充分性评价**：
  - **优点**：从发现到验证到临床的完整链条清晰，使用了独立队列，生存分析有统计学显著性。
  - **不足**：
    - 缺乏消融实验（如去除某个模块对最终结果的影响）。
    - 仅对单一生物标志物（CD79A）进行临床验证，其他候选（MLANA、LYZ、SPARC等）未做生存分析。
    - 未与现有已知标志物（如PD-L1、TMB）进行预测性能比较。
    - 细胞通讯仅发现SERPINE1和TFPI两个配体-受体对，可能受数据库限制。
    - 共表达分析仅用线性Pearson相关性，未用非线性或WGCNA进一步验证。
    - 生存分析使用伪批量CD79A表达（非独立IPI匹配的TCGA原始FPKM数据），存在近似误差。
  - 总体实验设计基本充分，但未进行多变量校正或竞争风险分析，结论的稳健性需进一步验证。

## 6. 论文的主要结论与发现

- **细胞图谱**：成功将7,186个细胞划分为7个主要TME区室（Melanoma/Tumor、T细胞、B细胞、巨噬细胞、NK细胞、内皮细胞、CAF）。
- **关键生物标志物**：XGBoost优先级排序前五：CD79A (B细胞)、MLANA (肿瘤)、LYZ (巨噬)、MFAP4 (CAF)、CDH5 (内皮)。SHAP揭示MLANA和S100B正向预测肿瘤身份，B2M低表达指示MHC-I下调（免疫逃逸）。
- **功能性通路**：肿瘤细胞显著富集凝血级联（adj.p=7.32e-12）和EMT通路。
- **细胞通讯**：SERPINE1来自T/B细胞，作用于CAF（LRP1）和巨噬细胞（PLAUR），构成免疫-基质激活回路。
- **共表达枢纽**：SPARC为最高连通性基因（r=0.195），与SERPINE2、CALD1、S100B、TYR形成正相关模块，与CCL5负相关，暗示基质沉积与免疫排斥的拮抗。
- **临床验证**：CD79A高表达组中位总生存期44.8个月 vs 低表达组26.7个月，风险比显著（Log-Rank p=4.42e-3），支持B细胞/TLS的抗肿瘤保护作用。

## 7. 优点

- **端到端集成性**：首次在单一框架内完整融合了scRNA-seq聚类、XGBoost/SHAP可解释AI、LIANA细胞通讯、Pearson共表达网络、跨队列验证与真实患者生存分析，覆盖从数据到临床的全链条。
- **可解释性强**：SHAP分析无需先验生物学知识即可捕获已知免疫逃逸机制（B2M下调）与诊断标志物（MLANA/S100B），验证了模型生物学合理性。
- **临床转化价值**：CD79A关联18.1个月生存获益，为预测免疫治疗疗效提供新的免疫评分候选，与Helmink/Cabrita等人的早期工作一致且具有单细胞精度优势。
- **代码开放**：承诺提供可复现的Colab流水线，增强可复现性。

## 8. 不足与局限

- **实验局限**：
  - 缺乏与现有生物标志物（如PD-L1 TPS、TMB、TLS评分）的直接比较或联合分析。
  - 仅验证了CD79A一个标志物，其他候选未进行生存分析或治疗响应关联。
  - 无任何功能实验（如B细胞耗竭、SERPINE1中和、SPARC敲除等）提供因果关系证据。
  - 共表达网络仅用线性Pearson相关性，未能捕捉非线性调控关系。
  - LIANA仅识别出两个显著的配体-受体对，可能因数据库覆盖不全而低估TME通讯复杂度。
- **方法局限性**：
  - 生存分析中CD79A表达采用伪批量（pseudobulk）近似而非匹配的TCGA原始RNA-seq FPKM值，引入测量误差。
  - 未进行多变量Cox回归校正年龄、性别、分期等混杂因素。
  - 发现队列（GSE115978）样本量较小（7,186个细胞），可能无法代表所有TME亚群。
  - 仅使用一套聚类分辨率（0.5），未评估不同参数对结果稳定性的影响。
- **应用限制**：
  - 结论完全基于计算，尚未在独立前瞻性队列或临床试验中验证。
  - 黑色素瘤仅涵盖皮肤型，未涉及黏膜、肢端等亚型。
  - CD79A作为B细胞标记，无法区分TLS中B细胞亚型（如记忆B细胞、浆细胞等），细化分型可能提供更精准分层。

（完）
