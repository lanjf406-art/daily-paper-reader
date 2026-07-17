---
title: Coupled Cell-Intrinsic and Microenvironmental Heterogeneity Drives Divergent Trajectories in Castration-Resistant Prostate Cancer
title_zh: 耦合的细胞内源性与微环境异质性驱动去势抵抗性前列腺癌的分化轨迹
authors: "Kemkar, S., Tao, M., Ghosh, A., Ramamurthy, A., Radhakrishnan, R."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.16.738502v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 机器学习代理模型预测前列腺癌治疗耐药
tldr: 去势抵抗性前列腺癌由细胞内在异质性与微环境约束耦合驱动。本研究集成多尺度模型（MHS+ABM）和机器学习SHAP分析，发现PTEN、MDM4、AR为关键内在驱动因子，并揭示微环境影响选择结果。临床验证确认其预后价值。该框架实现了从基因组数据到个性化ADT耐药风险预测的模型化路径。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1371, \"height\": 3189, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1379, \"height\": 3045, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1547, \"height\": 1167, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 590, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1870, \"height\": 2525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1837, \"height\": 1768, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1808, \"height\": 3007, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1836, \"height\": 2682, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1560, \"height\": 3381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1775, \"height\": 2360, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1284, \"height\": 2105, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1260, \"height\": 2120, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1361, \"height\": 1046, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1320, \"height\": 856, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1715, \"height\": 1068, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-16-738502-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1737, \"height\": 468, \"label\": \"Table\"}]"
motivation: 系统解析细胞内在异质性与微环境约束的耦合如何驱动去势抵抗性前列腺癌的不同发展轨迹。
method: 集成细胞信号模型（MHS）与空间代理模型（ABM），结合SHAP特征排序和临床验证，分析内在与外在因素。
result: PTEN缺失、MDM4扩增、AR变异独立预测不良总生存期，且微环境物理约束改变了相同遗传变异的选择结果。
conclusion: CRPC出现是内在-外在耦合的突现属性，必须整合机制模型才能准确预测患者分层。
---

## 摘要
去势抵抗性前列腺癌源于细胞内源性异质性与微环境约束之间的耦合。从机制上剖析这种耦合（而非孤立地研究任一因素）是本研究的核心目标。为系统研究内源性与外源性空间轴对疾病轨迹的影响，我们开发了一个整合的多尺度框架：一个细胞信号模型（MHS），该模型使用来自对照组、生化复发（BR）和治疗抵抗（TR）队列的TCGA基因组数据进行参数化，并与一个基于空间智能体模型（ABM）相耦合。在MHS模型上训练的机器学习代理通过基于SHAP的特征排序，识别出PTEN、MDM4和AR为主要的细胞内源性驱动因子。通过cBioPortal队列的Kaplan-Meier和Cox回归进行的临床验证证实了这些排序：AR改变（中位总生存期20个月对比86个月）、PTEN缺失（54个月对比77个月）和MDM4扩增（33个月对比75个月）独立预测较差的总生存结局。在组织尺度上，运行ABM模拟以研究微环境（细胞外源性）因素（如物理约束、雄激素摄取动力学和粘附-运动强度）对疾病进展的影响。这种时空分析揭示，相同的遗传改变根据微环境背景产生不同的选择结果。将这种耦合逻辑扩展到个体患者层面，我们使用来自EUREKA1前瞻性登记中14名患者的基因表达谱对MHS模型进行参数化。患者特异性雄激素敏感性比率（高睾酮与低睾酮下净细胞生长的比率）根据模型预测的雄激素依赖性对患者进行分层，无需纵向PSA观察，并显示PTEN缺失将增殖反应转向雄激素非依赖性，其幅度由更广泛的表达背景设定为患者特异性。这提供了一条从诊断时的基因组数据到ADT抵抗风险个性化预测的基于模型的路径。总之，这些发现确立了CRPC的出现是内源性-外源性耦合的涌现特性，单独的分子或空间分析均无法预测临床轨迹，并且需要两者的机制整合才能实现准确的患者分层。

## Abstract
Castration-resistant prostate cancer emerges from coupling between cell-intrinsic heterogeneity and microenvironmental constraints. Mechanistically dissecting this coupling, rather than either factor in isolation, is the central aim of this study. To systematically study the effect of intrinsic and extrinsic spatial axes on disease trajectories, we developed an integrated multiscale framework: a cellular signaling model (MHS) parameterized with TCGA genomic data from control, biochemical recurrence (BR), and treatment-resistant (TR) cohorts, coupled to a spatial agent-based model (ABM). Machine learning surrogates trained on the MHS model identified PTEN, MDM4, and AR as dominant intrinsic drivers, using SHAP-based feature ranking. Clinical validation via Kaplan-Meier and Cox regression across cBioPortal cohorts confirmed these rankings: AR alterations (median OS 20 vs. 86 months), PTEN loss (54 vs. 77 months), and MDM4 amplification (33 vs. 75 months) predicted poor overall survival outcomes independently. At the tissue scale, ABM simulations were run to study the effect of microenvironmental (cell-extrinsic) factors such as physical confinement, androgen uptake kinetics, and adhesion-motility strength, on disease progression. This spatiotemporal analysis revealed that identical genetic alterations produce varied selection outcomes depending on microenvironmental context. Extending this coupling logic to the individual patient level, we parameterized the MHS model using gene expression profiles from 14 patients in the EUREKA1 prospective registry. Patient-specific androgen sensitivity ratios, the ratio of net cell growth under high versus low testosterone, stratified patients by model-predicted androgen dependence without requiring longitudinal PSA observations and showed that PTEN deletion shifts the proliferative response toward androgen independence in a patient-specific magnitude set by the broader expression background. This provides a model-based route from genomic data at diagnosis to personalized prediction of ADT resistance risk. Together, these findings establish that CRPC emergence is an emergent property of the intrinsic-extrinsic coupling, that neither molecular nor spatial analyses in isolation can predict clinical trajectories, and that mechanistic integration of both is required for accurate patient stratification.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：为什么在根治性前列腺切除术后，具有相似临床病理特征（如PSA、Gleason评分、PTEN状态）的前列腺癌患者会走向截然不同的转归轨迹——从惰性的生化复发迅速进展至致命的去势抵抗性前列腺癌（CRPC）？现有的临床风险分层工具（如PSA动力学、Nomogram）无法预测这种差异，其根本原因在于对疾病内在生物学复杂性的认识不足，尤其是细胞内在异质性与微环境约束之间的动态耦合未被充分考虑。
- **整体含义**：CRPC的发生不是由细胞内在遗传变异或微环境压力单独决定的，而是两者耦合作用的涌现属性。本研究通过构建整合的多尺度模型，展示了这种耦合如何导致不同患者队列（对照组、生化复发BR、肿瘤复发TR）在相同压力下出现完全不同的选择结果，并提供了从基因组数据到个性化ADT耐药风险预测的模型化路径。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：将细胞内在信号异质性（PTEN/PI3K/AKT、AR、p53等）与微环境外在因素（物理拥挤、雄激素资源竞争、细胞粘附-运动平衡）在统一的多尺度框架中耦合，使分子层面的遗传信息通过细胞决策“上卷”到组织层面，同时微环境反馈调节细胞表型。
- **关键技术细节**：
  - **MHS（多尺度混合系统）细胞模型**：整合五个子模型——①AR信号与EGFR/Ras-MAPK通路；②PI3K/AKT/PTEN通路；③雄激素合成与受体激活；④TP53介导的细胞周期布尔逻辑模型；⑤双群体PSA动力学模型（敏感S vs 抵抗R）。ODE子模型（4-8小时时间尺度）与布尔模块（24-48小时）通过混合模拟器桥接。ADT通过调控睾酮浓度（1-20 nM）模拟。
  - **ABM（基于智能体的空间模型）**：使用PhysiCell v1.10.4实现2D空间模拟，包含扩散-反应输运（BioFVM）。每个智能体继承MHS定义的增殖/迁移/粘附/死亡倾向，并根据局部微环境（睾酮、生长因子浓度）实时调整。三个轴线被系统变化：
    - 物理拥挤（低/高密度包装）
    - 雄激素摄取速率（SLCO转运蛋白代理）
    - 细胞-细胞粘附强度（EMT状态代理，与运动性呈倒数关系）
  - **机器学习代理与SHAP特征排序**：为解决MHS模型全局敏感性分析计算成本过高的问题，训练了三个分类器（神经网络、随机森林、支持向量机）作为MHS的替代代理。输入特征z-score归一化，类别不平衡通过SMOTE处理，超参数经5折交叉验证优化。最佳二分类阈值（NCG≥0.15为增殖，否则静止）通过平衡准确率选择。SHAP用于计算每个特征对细胞命运预测的边际贡献，PTEN、MDM4、AR在三种架构中均名列前茅。
  - **临床验证**：基于cBioPortal的7个OS队列（~4718患者）进行基因组改变层面的Kaplan-Meier生存分析和多变量Cox回归；4个mRNA队列（TCGA-PRAD、SU2C、MSKCC、MCTP）进行表达分层分析。使用逻辑或定义“改变”状态（截短突变、拷贝数变异≥±2、结构变异），仅保留改变臂≥20患者的结果。
- **算法流程简述**：①从TCGA提取DEGs并映射到MHS物种初始浓度，生成队列参数化实例；②运行MHS模拟获取NCG输出；③训练ML代理并执行SHAP排序；④在ABM中嵌入MHS双群体子模型，变化微环境参数运行随机模拟；⑤对临床队列进行生存分析验证模型预测。

## 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **数据集**：
  - **TCGA-PRAD**（501患者初始，250分析集）：按PTEN缺失状态和复发类型分为对照组（无复发）、BR（PSA定义）、TR（影像定义）。
  - **cBioPortal**：7个OS队列（TCGA-PRAD、SU2C/PCF CRPC、MCTP、MSK Prostate 2025、MSK PIK3R1 2021、MSK Clin Cancer Res 2024、MSK Metastatic CSPC），共4718患者用于基因组改变生存分析。4个mRNA队列（TCGA-PRAD、SU2C、MSKCC、MCTP）用于表达分析。
  - **EUREKA1**：14个前列腺切除患者，有纵向PSA数据（3例）和基因表达谱，用于个性化ADT响应预测。
- **Benchmark与对比**：
  - 没有与外部预测模型（如Nomogram、PSA动力学模型）进行直接定量对比。验证主要通过：（a）ML代理的内部一致性（跨三种架构共识）；（b）临床生存分析的统计显著性（log-rank p<0.05、Cox HR显著）；（c）ABM与双群体ODE在无空间约束条件下的一致性检查（图S7.3.1）。
  - 方法对比主要是通过SHAP特征排序与临床风险比大小和显著性的正相关性（图3E），但论文指出这种相关性温和，且PTEN的高频率低HR导致一定偏差。
- **场景**：
  - 细胞尺度：PTEN缺失梯度（七级） × 三种队列 × 两种GF水平。
  - 组织尺度：物理拥挤（2水平） × 队列（BR/TR） × 初始R/S比；雄激素摄取速率（多种水平） × 队列；粘附强度（多种水平） × 队列 × 睾酮浓度。
  - 临床尺度：每个基因进行Kaplan-Meier + Cox，并检查基因×PTEN交互作用（仅用TCGA-PRAD）。

## 4. 资源与算力

- **文中明确指出**：所有计算均运行在匹兹堡超级计算中心的Bridges-2集群上。MHS模型在COPASI和Python v2.7中模拟；ABM在PhysiCell v1.10.4中模拟。每个条件运行10个随机重复。机器学习代理的超参数调优和SHAP也在Bridges-2上执行。
- **未明确说明**：未提及使用的GPU型号、数量或具体训练时长。由于MHS基于ODE，ML代理规模不大，推测算力需求中等（CPU密集型而非GPU密集型）。无详细能耗或时间信息。

## 5. 实验数量与充分性

- **实验数量**：
  - MHS细胞模拟：每队列20个实例（2 PTEN × 5睾酮 × 2 GF），共60实例。
  - ABM模拟：每条件10个随机重复，涉及三个轴线（拥挤：2×2队列；摄取：多种速率×2队列；粘附：3-4水平×3队列×2睾酮），估计总模拟次数>1000。
  - 临床生存分析：覆盖7+4个队列，检验基因数量：内在驱动子3个，微环境相关轴基因→拥挤轴27个、AND轴3个、EMT轴10个，每个基因做1或2个终点KM + Cox，并额外检验基因×PTEN交互（37个交互项）。总计约200次独立统计检验。
- **充分性与公平性**：
  - **优点**：跨多个独立队列验证（内在驱动子来自cBioPortal 7个OS队列；mRNA来自4个独立队列），提高了泛化性；ABM模拟大量参数扫描，覆盖了关键范围；三种ML架构共识减少了单一模型偏差。
  - **缺点**：缺乏与现有临床风险模型（如CAPRA、Partin表）的对比；没有进行独立的外部数据集时间验证（EUREKA1的14例仅用于示范性分析，未进行统计验证）；拥挤轴临床分析受限于低事件数（TCGA-PRAD仅有30 DFS事件、93 PFS事件），部分基因的显著性脆弱；多个基因×PTEN交互因小样本被标记为exploratory。结果报告了名义p值，未进行多重比较校正（如Bonferroni），增加了假阳性风险。

## 6. 论文的主要结论与发现

1. **细胞内在异质性在双重层面运作**：PTEN缺失剂量依赖性驱动更早、更猛的生化复发，但TR队列的基因组背景使其在相同PTEN缺失下表现出更强的进展潜能，表明除通路剂量外，全基因组信号背景也起放大器作用。
2. **SHAP共识鉴定PTEN、MDM4、AR为关键驱动子**：三种ML架构均将这三个基因列为最高贡献特征。临床验证：AR改变（HR=4.07）、MDM4扩增（HR=2.25）、PTEN缺失（HR=1.51）均显著预测较差总生存（p<0.001）。MDM4的突出地位提示p53-MDM4轴是潜在治疗靶点。
3. **微环境物理拥挤门控内在侵袭潜能**：松散包装中PTEN缺失克隆的增殖优势显著放大，而密集包装通过接触抑制大幅削弱该优势，且此效应在BR和TR中一致。
4. **雄激素资源竞争产生队列特异性选择**：高摄取速率造成局部睾酮耗竭，但在BR中导致抵抗克隆富集（转化为均质抵抗肿瘤），在TR中因敏感细胞本身雄激素非依赖性而维持异质性。这是内在-外在耦合的典型体现。
5. **粘附-运动耦合驱动阈值相变式空间重组**：粘附强度超过临界值后，抵抗细胞从分散状态突变为同型聚类。该阈值在对照组最低、BR次之、TR最高，且受雄激素浓度调节。聚类指数呈S型曲线，表明空间组织是可调的涌现现象。
6. **临床生存分析支持微环境轴**：AKR1C3高表达（雄激素合成）与更差PFS相关（多个队列）；RHOA高表达和CDH1低表达（EMT相关）与更差结局一致；拥挤轴中Cyclin D1（CCND1）在PTEN缺失肿瘤中显著恶化预后（交互HR=5.40），提示PTEN缺失放大了细胞周期驱动的复发风险。
7. **个性化雄激素敏感性比率可分层ADT响应**：对EUREKA1患者，计算高/低睾酮下净细胞生长比率，揭示PTEN缺失将比率降低（趋向雄激素非依赖性），但降低幅度因患者表达背景而异，提供了从基因组数据到个性化风险指数的入口。

## 7. 优点：方法或实验设计上的亮点

- **多尺度整合的架构**：首次将详细的细胞信号模型与空间ABM进行双向耦合，而不是松散连接，使得内在状态（如PTEN缺失）能直接影响微环境重塑（通过粘附/运动），微环境又反馈调节克隆适应度。
- **机器学习代理加速分析**：面对ODE+布尔逻辑混合模型的高计算成本，采用代理模型+SHAP实现了全局敏感性分析，适用于生物复杂系统。
- **从基因组到预后的直接桥梁**：利用TCGA DEGs参数化模型，再通过临床大样本验证，使得计算模型的预测具有可操作的临床关联。
- **严密的内外一致性验证**：ABM在无空间约束下与双群体ODE模型输出一致（PSA曲线吻合），确保空间效应不是数值伪影。
- **临床生存分析的全面覆盖**：同时验证基因组改变和mRNA表达，并检查微环境轴相关基因与PTEN的交互作用，提供了多层面的证据。

## 8. 不足与局限

- **模型简化与覆盖缺失**：
  - 细胞模型仅聚焦PTEN/PI3K/AKT和AR，忽略了TP53突变、AR剪接变体（AR-V7）、糖皮质激素受体旁路、SLCO转运蛋白异质性、雄激素合成等重要的抵抗机制。
  - ABM为2D，未捕捉3D血管、基质（CAF）、免疫细胞（巨噬细胞、T细胞）等关键成分，而它们在前列腺癌进展中作用重大。
  - 无药代动力学-药效学（PK/PD）模块，无法模拟恩杂鲁胺、阿比特龙等一线药物治疗的时序效应。
- **参数化局限**：
  - 依赖TCGA bulk RNA-seq，掩盖了瘤内空间异质性和亚克隆动态。
  - 微环境轴中，SLCO转运蛋白、粘附相关参数仅作代理，未直接定量。
- **验证不足**：
  - ABM空间输出（聚类指数、R/S组成）未与免疫组化、空间转录组学或定量组织学比较，仅为预测。
  - 拥挤轴临床分析因事件数低，上游机械传导基因（如YAP1、PIEZO1）的转录水平可能无法反映活性状态，得到反直觉方向（高YAP1与更好预后相关）且难以解释。
  - 未进行多重比较校正（如FDR），部分名义显著结果可能为假阳性。
- **外部独立性**：
  - EUREKA1仅14例，无足够的统计效力；雄激素敏感性比率未与真实ADT响应进行前瞻性相关验证。
  - 没有与传统临床风险计算器（CAPRA、Partin表）或更复杂的影像组学模型进行比较。
- **结果的推广性**：
  - 所有模拟基于TCGA定义的队列（CNT/BR/TR），其划分依赖复发类型，但实际临床中生物化学复发和治疗抵抗有重叠，边界不清晰。
  - 未纳入转移性、新辅助治疗等更晚期的患者数据，结论可能仅限于根治术后早期复发阶段。

（完）
