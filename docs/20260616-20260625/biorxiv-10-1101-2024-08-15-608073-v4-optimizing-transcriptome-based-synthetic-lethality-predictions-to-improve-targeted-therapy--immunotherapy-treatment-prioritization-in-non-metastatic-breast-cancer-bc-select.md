---
title: "Optimizing transcriptome-based synthetic lethality predictions to improve targeted therapy / immunotherapy treatment prioritization in non-metastatic breast cancer: BC-SELECT"
title_zh: 优化基于转录组的合成致死性预测以改善非转移性乳腺癌的靶向治疗/免疫治疗优先排序：BC-SELECT
authors: "Kim, Y., Nagy, M., Pollard, B., Rajagopal, P. S."
date: 2026-06-23
pdf: "https://www.biorxiv.org/content/10.1101/2024.08.15.608073v4.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 利用转录组和合成致死性预测乳腺癌新辅助治疗反应
tldr: 早期三阴性或HER2阳性乳腺癌缺乏治疗前预测工具。BC-SELECT通过合成致死/救援关系从转录组数据预测靶向/免疫治疗反应。在9个临床试验中验证，对PARP抑制剂和免疫治疗的ROC-AUC达0.6-0.8，优于现有工具。可作为非转移性乳腺癌治疗优先排序的决策支持。
source: biorxiv
selection_source: fresh_fetch
motivation: 早期TNBC/HER2+乳腺癌无治疗前预测指标，需开发基于基因表达的治疗响应预测工具。
method: 利用合成致死/救援相互作用，结合体内外数据识别药物靶点伙伴基因，并在早期乳腺癌临床试验中训练参数以生成预测评分。
result: 在9个早期试验中，6个显著预测反应（PARP抑制剂AUC 0.6-0.8，免疫治疗AUC 0.7-0.8），8个区分应答者，优于SELECT和ENLIGHT。
conclusion: BC-SELECT有望成为辅助临床决策、优先选择早期乳腺癌批准治疗的预测工具。
---

## 摘要
早期三阴性（TNBC）或HER2阳性（HER2+）乳腺癌患者在治疗前缺乏预测响应的工具。病理学完全缓解（pCR）仍需要新辅助治疗作为替代指标。BC-SELECT是一个临床导向的计算工具，利用遗传相互作用（如合成致死性SL或救援SR）从基因表达数据预测治疗响应。BC-SELECT基于现有相关工具（SELECT, ENLIGHT）构建，以导航竞争性治疗选项。BC-SELECT包含两个主要步骤：（1）“基因对识别”步骤，利用体内和体外数据集为药物靶点识别临床相关伙伴基因；（2）使用早期乳腺癌临床试验进行“训练/参数调优”，以开发预测治疗响应评分。我们通过训练三项包含86名患者的试验，并在九项包含722名患者的试验中验证，评估了BC-SELECT预测曲妥珠单抗、聚（ADP-核糖）聚合酶（PARP）抑制剂和免疫治疗响应者的能力。BC-SELECT在6/9的早期试验中显著预测了治疗响应，包括所有PARP抑制剂（ROC-AUC 0.6-0.8；比值比OR: 1.9-3.5）和免疫治疗（ROC-AUC 0.7-0.8；OR: 3.2-7.1）。BC-SELECT在8/9的试验中区分了响应者和非响应者（FDR校正的Wilcoxon秩和检验p值<0.1）。BC-SELECT在预测免疫治疗响应方面优于SELECT和ENLIGHT。特异性在各亚型中相当，HER2+为0.64，TNBC为0.66，激素受体阳性（HR+）为0.76。TNBC和HER2+乳腺癌缺乏治疗前的标准响应预测因子。我们的研究结果将BC-SELECT定位为最终决策支持工具，用于优先排序针对早期乳腺癌患者批准的疗法。

## Abstract
Patients with early-stage triple-negative (TNBC) or HER2-positive (HER2+) breast cancer do not have tools to predict response before treatment. Pathologic complete response (pCR) is a proxy that still requires neoadjuvant treatment. BC-SELECT is a clinically focused computational tool that leverages genetic interactions, such as synthetic lethality (SL) or rescue (SR), to predict treatment response from gene expression data. BC-SELECT builds on existing related tools (SELECT, ENLIGHT) to navigate competing treatment options. BC-SELECT involves two main steps: (1) a "gene pair identification" step that identifies clinically relevant partner genes using in vivo and in vitro datasets for a drug target, and (2) "training/parameter tuning" using early-stage breast cancer clinical trials to develop predicted response scores to treatment. We evaluated BC-SELECT's ability to predict responders to trastuzumab, poly (ADP-ribose) polymerase (PARP) inhibitors, and immunotherapy by training on three trials including 86 patients and validating on nine trials including 722 patients. BC-SELECT significantly predicted treatment response in 6/9 early-stage trials, including in all PARP inhibitors (ROC-AUCs 0.6-0.8; Odds Ratio (OR): 1.9-3.5) and immunotherapy (ROC-AUCs 0.7-0.8; OR: 3.2-7.1). BC-SELECT distinguished between responders and non-responders in 8/9 trials (FDR-corrected Wilcoxon rank-sum test p-value <0.1). BC-SELECT outperformed SELECT and ENLIGHT in predicting immunotherapy response. Specificity was comparable across subtypes, with HER2+ 0.64, TNBC 0.66, and hormone-receptor positive (HR+) 0.76. There are no standard-of-care pre-treatment predictors of response in TNBC and HER2+ breast cancer. Our findings position BC-SELECT as an eventual decision-support tool to prioritize treatments approved for patients with early-stage breast cancer.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：非转移性三阴性乳腺癌（TNBC）和HER2阳性乳腺癌患者在治疗前缺乏可靠的预测工具来判断靶向治疗或免疫治疗的反应。当前，病理学完全缓解（pCR）需通过新辅助治疗后手术才能获得，无法在治疗前指导方案选择。
- **整体含义**：当患者有多个竞争性治疗选项（如PARP抑制剂、免疫治疗、曲妥珠单抗）时，临床缺乏有效的优先排序手段。BC-SELECT旨在利用转录组数据和合成致死性（SL）/合成救援（SR）遗传相互作用，在治疗前预测pCR，从而辅助临床决策，优化治疗顺序，避免不必要的联合用药毒性。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：基于合成致死性/合成救援原理，对于每个药物靶点基因A（如PARP1/2、HER2、PD-1/PD-L1），通过大规模数据分析寻找与其存在SL或SR相互作用的伙伴基因B集合。患者的预测响应评分由靶点基因表达水平与伙伴基因表达比值的乘积生成。
- **关键技术细节**：
  - **基因对识别（Gene-pair identification）**：
    - 使用体外细胞系数据（如DepMap）和体内乳腺癌患者数据（TCGA、METABRIC等）筛选与药物靶点基因A存在显著SL/SDL（靶向治疗）或SR（免疫治疗）的候选伙伴基因B。
    - 通过以下三步骤过滤：
      1. 大规模基因对筛选（基于细胞系或体内数据）
      2. 在乳腺癌数据集中使用Cox比例风险模型，结合临床变量和总生存期，筛选具有临床相关性的基因对。
      3. 基于进化保守性分析，保留相对表达关系保守的基因对。
  - **训练/参数调优（Training/parameter tuning）**：
    - 使用3个临床试验数据（共86例患者）进行网格搜索，优化两个参数：
      - 所需显著基因对的数量（范围10-100）
      - 区分pCR与非pCR的比值比阈值（最终采用0.51）
    - 对于靶向治疗，最终选取前55个SL/SDL基因对；对于免疫治疗，选取前10个SR基因对。
  - **预测响应评分**：最终评分为靶点基因A的表达水平与伙伴基因B表达比值（经过Nanostring基因列表特化处理）的乘积。
- **算法流程**（文字描述）：
  1. 输入患者肿瘤转录组数据、目标药物靶点。
  2. 从预先生成的基因对数据库中选择对应靶点的伙伴基因列表。
  3. 计算每个伙伴基因的表达比值（相对于参照基因集）。
  4. 将伙伴基因比值与靶点基因表达相乘，得到每个基因对的贡献。
  5. 汇总所有选定基因对的贡献，得到最终预测响应评分。
  6. 将评分与阈值0.51比较，输出“pCR”或“非pCR”预测。

### 3. 实验设计：使用了哪些数据集/场景，benchmark，对比方法

- **数据集与场景**：
  - **训练/调优集**：3个临床试验（GSE66399, GSE160568, NCT02489448），共86例患者，覆盖曲妥珠单抗、PARP抑制剂、免疫治疗。
  - **验证集**：9个独立临床试验（共722例患者），包括：
    - 4个曲妥珠单抗试验（HER2+乳腺癌）
    - 3个PARP抑制剂试验（TNBC，药物为奥拉帕利、维利帕利）
    - 2个PD-1/PD-L1免疫治疗试验（帕博利珠单抗、度伐利尤单抗）
    - 部分试验还包含HR+患者（172例）。
  - **场景**：所有试验均为非转移性（I-III期）乳腺癌新辅助治疗。
- **Benchmark**：pCR作为金标准（0/1二进制）。
- **对比方法**：
  - BC-SELECT的两个组成部分：单独靶点基因表达（基因A）和单独伙伴基因表达比值（基因B）。
  - 已有工具：SELECT和ENLIGHT（在免疫治疗预测上进行比较）。
  - 无治疗效应验证：通过比较PARP抑制剂治疗组与安慰剂组（BrighTNess试验）的AUC，确保评分不是由治疗本身引起。

### 4. 资源与算力

- **文中未明确说明使用的GPU型号、数量或训练时长**。仅提到“运行时间在大型临床试验中为数小时”，以及使用NIH Biowulf集群（CPU集群）。算法主要基于R语言，计算需求不高，未见大规模深度学习训练。因此无法量化具体算力。

### 5. 实验数量与充分性

- **实验数量**：
  - 训练集：3项试验（86例）
  - 验证集：9项试验（722例）
  - 共9项验证试验，覆盖三种治疗类型（曲妥珠单抗、PARP抑制剂、免疫治疗），且包含多个独立数据集。
  - 亚组分析：针对TNBC、HER2+、HR+亚型分别评估特异性。
  - 跨疗法评分关联分析：在BRCA缺陷（低表达）肿瘤中比较免疫治疗和PARP抑制剂评分的关系（3个独立队列）。
  - 消融实验：对比BC-SELECT完整评分与单独靶点表达、单独伙伴基因比值的AUC。
- **充分性评价**：
  - **优点**：验证集数量较多、来源独立、包含多种治疗类型，且使用了统一的pCR终点。有安慰剂对照验证（排除人为抬高）。对比了SELECT和ENLIGHT。
  - **不足**：曲妥珠单抗预测性能一般（仅2/4试验显著），可能因机制不完全依赖SL。样本量较小（尤其其训练集仅86例）。缺乏长期生存终点（如无复发生存），仅使用pCR。仅验证了三种治疗类型，未覆盖CDK4/6抑制剂、PIK3CA抑制剂等。未进行跨试验的批次效应校正（但作者明确避免以减少偏倚）。
  - **总体**：实验设计客观、公平，数据全部公开，但受限于公开数据的可获得性，覆盖范围有限。

### 6. 论文的主要结论与发现

- BC-SELECT在6/9个验证试验中显著预测pCR（OR>1，95%CI不含1），包括所有PARP抑制剂和所有免疫治疗试验。
- ROC-AUC范围：PARP抑制剂0.6-0.8，免疫治疗0.7-0.8，曲妥珠单抗部分显著但整体较弱。
- BC-SELECT在免疫治疗预测中优于SELECT和ENLIGHT。
- 特异性在各亚型中相当（TNBC 0.66, HER2+ 0.64, HR+ 0.76）。
- 在BRCA缺陷肿瘤中，免疫治疗评分和PARP抑制剂评分呈负相关，提示可帮助优先排序。
- BC-SELECT有潜力作为非转移性乳腺癌治疗优先排序的临床决策支持工具。

### 7. 优点：方法或实验设计上的亮点

- **临床导向**：直接针对当前指南中缺乏预测工具的问题，旨在解决竞争性治疗选项的优先排序。
- **利用遗传相互作用**：不仅考虑单个基因表达，还捕捉基因间SL/SR关系，机制更接近治疗原理。
- **模块化设计**：基因对识别和训练/调优分离，便于未来加入新数据（新的治疗靶点或临床试验）。
- **公开可复现**：代码、数据来源均公开，便于独立验证。
- **多数据源整合**：同时使用细胞系和患者数据，体内外证据互补。
- **鲁棒性验证**：包含安慰剂对照、亚型特异性分析、与现有算法对比。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等

- **样本量有限**：训练集仅86例，验证集总722例，但每个试验样本量较小（部分<25例），可能导致高变异性。
- **仅使用pCR作为终点**：缺乏长期生存数据，pCR与最终生存的相关性虽强，但非完全替代。
- **治疗覆盖不全**：仅验证了曲妥珠单抗、PARP抑制剂、免疫治疗，未涉及CDK4/6抑制剂、内分泌治疗等。
- **依赖特定药物靶点**：仅适用于靶向/免疫治疗，无法预测化疗反应。
- **曲妥珠单抗预测效果有限**：可能因其作用机制不完全依赖SL，算法适用性受限。
- **无法区分同一靶点的不同药物**：如不同PARP抑制剂之间。
- **未进行跨试批次效应标准化**：可能引入技术偏倚，但作者故意避免以保持自然变异。
- **临床转化障碍**：需要治疗前获取肿瘤组织进行转录组测序，成本和组织可用性限制。
- **BRCA状态信息缺乏**：使用表达量代替突变状态，可能不够精确。

（完）
