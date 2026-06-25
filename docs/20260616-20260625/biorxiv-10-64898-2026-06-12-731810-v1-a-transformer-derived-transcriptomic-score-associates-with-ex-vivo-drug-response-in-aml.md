---
title: A Transformer-derived transcriptomic score associates with ex-vivo drug response in AML
title_zh: 一种基于Transformer的转录组评分与AML体外药物反应相关
authors: "Barman, J., Adhikari, S., Heckman, C., Vaha-Koskela, M."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.12.731810v1.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 基于Transformer的转录组评分预测药物耐受状态，使用机器学习方法
tldr: 针对急性髓系白血病（AML）药物耐受持久细胞（DTP）状态缺乏有效计算评分的问题，提出基于Transformer的知识蒸馏模型，从scRNA-seq训练教师网络并蒸馏至1000基因学生网络，输出概率评分（阈值0.31）。交叉验证AUROC达0.94，在452例BeatAML队列中评分与体外药物反应AUC显著相关（汇总r=0.482），候选靶点列表恢复FLT3和CD33。该工具可用于研究排序，但阈值需跨队列校准，不直接用于临床决策。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法依赖固定基因签名或通用分类器，缺乏针对AML药物耐受持久状态的深度学习评分及体外药效验证。
method: 基于9个样本的scRNA-seq数据训练Transformer教师模型，通过知识蒸馏得到1000基因学生模型，输出概率评分，预设阈值0.31，并在BeatAML等外部队列评估。
result: 交叉验证AUROC 0.936，学生与教师相关系数0.96；在BeatAML中评分与7种药物AUC的Spearman相关系数0.41-0.53，汇总r=0.482。
conclusion: 该评分可作为研究用转录组排序工具，关联AML体外药物反应，但阈值需跨队列校准，未验证临床决策或生存预测。
---

## 摘要
背景：药物耐受持久性（DTP）细胞状态被认为与多种癌症（包括急性髓系白血病[AML]）的复发有关[1,2]。能够从转录组数据中评估这种状态、泛化到未见过样本、提供校准的概率输出并将预测与候选生物学联系起来的方法，有助于优先安排后续实验工作。现有的评估药物耐受或持久性样状态的转录组方法主要依赖于固定的基因标志或事后调整的通用细胞类型分类器（scPred, scANVI, scClassify）；据我们所知，专门为AML药物耐受持久性评分开发的深度学习方法（具有校准的概率输出、预设阈值以及针对体外药物反应数据的透明外部验证）尚缺乏。我们的方法通过结合Transformer教师模型和知识蒸馏的1000基因学生模型、预设阈值τ=0.31以及直接针对BeatAML药物AUC进行评估来填补这一空白。我们的计算机方法旨在填补识别和标记DTP细胞的分析方法缺失的空白。

方法：我们在一个由9个样本混合的scRNA-seq数据集（其中6个来自GSE123902——肺腺癌转移、正常组织和原发肿瘤[4]，加上3个原发AML样本；共32,342个细胞，13,369个常见基因）上训练了一个Transformer分类器，使用分层5折交叉验证（细胞级别）、20%的保留测试集，并在折外预测上选择预设概率阈值。通过知识蒸馏训练了一个1000基因的学生模型[5]。对于每个输入细胞，学生模型输出一个介于0和1之间的概率（以下简称“评分”），表示预测的正训练类成员身份。训练后的模型未经调整直接应用于五个外部或独立应用队列：39个原发AML供体（内部）；GSE74246[6]；BeatAML（n=452，有链接的体外药物AUC；n=405，有总生存期元数据）[7]；TCGA-LAML（n=149）[8]；以及一个内部n=10的scRNA-seq队列（有链接的生存数据）。生存和药物反应数据未用于训练、阈值选择或调优。该评分通过CRISPR/DepMap必需性[9]、通路富集以及正常组织过滤的表面蛋白候选列表（HPA[11]，GTEx[12]）进行机制锚定。

为了评估转录组优先排序与蛋白质水平证据之间的一致性，每个排名候选者还额外标注了两个HPA衍生标志：HPA表面蛋白（是/否，源自HPA蛋白质类别和亚细胞定位字段，识别注释为质膜、GPCR、离子通道、转运蛋白、受体或CD标志的基因）和HPA抗体可靠性（增强、支持、批准、不确定或不可用，根据HPA抗体验证等级）。注释按HGNC符号合并；250个候选者中有248个（99.2%）匹配。两个使用较旧CORF命名法的候选者未自动匹配HPA的小写约定，已手动解决。HPA的每个基因RNA-蛋白质数值相关性仅发表在单个基因网页上，未包含在批量下载中；因此我们使用检测水平和抗体可靠性等级作为操作一致性过滤器。

结果：交叉验证的接收者操作特征曲线下面积（AUROC）为0.936±0.014（保留测试集0.941，马修斯相关系数[MCC] 0.696，F1分数0.895）。1000基因学生模型与教师模型的斯皮尔曼ρ≈0.96，在预设阈值下类别一致性超过85%。主要外部结果是BeatAML：该评分与七种AML相关药物的体外药物反应AUC相关，每种药物的一致性斯皮尔曼相关系数（r=0.41-0.53，所有p<0.05）。来自452名患者的3,164个患者-药物对的汇总相关性为r=+0.482，作为总结报告，同时认识到来自同一患者的对并非完全独立。该评分在TCGA-LAML或内部n=10队列中未对总生存期进行分层，部分原因是预测的高评分比例饱和。在GSE74246中，预设阈值下评分未区分细胞类型，表明绝对校准具有队列依赖性。与逻辑回归、随机森林、LSC17干性特征以及同一基因面板的平均表达基线相比，Transformer在等分分组交叉验证下是最稳定的模型，并且是唯一一个与BeatAML药物AUC具有强正相关性的迁移模型。机制性候选目标流程产生了250个候选的表面蛋白排名列表（结果中有详细分解）；FLT3和CD33作为阳性对照从无偏排名中被恢复。

结论：我们提出了一种基于Transformer的转录组评分，解决了缺乏经过验证的计算方法来识别AML中药物耐受持久性样状态的问题。该评分显示出与体外药物反应的外部秩次关联，为优先安排候选持久性相关转录程序进行后续研究提供了研究用途工具。

总之，这些结果支持将该评分作为AML药物反应相关状态的研究用途转录组排名工具。最强大的外部支持来自与BeatAML体外药物反应AUC的一致性关联。固定概率阈值不能可靠地迁移到所有队列，因此基于阈值的分类需要特定队列的重新校准。该评分未经验证用于临床决策，也不作为生存预测指标。候选目标列表是功能后续研究的起点。

## Abstract
BackgroundDrug-tolerant persister (DTP) cell states have been implicated in relapse across multiple cancers, including acute myeloid leukaemia (AML) [1,2]. Methods that score such states from transcriptomic data, generalise to held-out samples, expose calibrated probability outputs, and link predictions to candidate biology are useful for prioritising follow-up experimental work. Existing transcriptomic methods for scoring drug-tolerant or persister-like states largely rely on fixed gene signatures or general-purpose cell-type classifiers adapted post hoc (scPred, scANVI, scClassify); deep-learning approaches developed specifically for AML drug-tolerant persister scoring with calibrated probability outputs, prespecified thresholds, and transparent external validation against ex-vivo drug-response data are, to our knowledge, lacking. Our approach addresses this gap by combining a Transformer teacher with a knowledge-distilled 1,000-gene student, prespecified threshold {tau} = 0.31, and direct evaluation against BeatAML drug-AUC.

Our in silico approach aims to fill this gap of non-existent analytical methods to identify and mark the DTP cells.

MethodsWe trained a Transformer classifier on a pooled scRNA-seq corpus of nine samples (six from GSE123902-lung adenocarcinoma metastasis, normal, and primary tumour [4]-plus three primary AML samples; 32,342 cells, 13,369 common genes), with stratified 5-fold cross-validation at the cell level, a 20% held-out test split, and a prespecified probability threshold selected on out-of-fold predictions. A 1,000-gene student model was trained by knowledge distillation [5]. For every input cell, the student outputs a probability between 0 and 1 (hereafter "the score") representing predicted membership in the positive training class. The trained model was applied without re-tuning to five external or independent application cohorts: 39 primary AML donors[in-house]; GSE74246[6]; BeatAML (n = 452 with linked ex-vivo drug-AUC; n = 405 with overall-survival metadata)[7]; TCGA-LAML (n = 149)[8]; and an in-house n = 10 scRNA-seq cohort with linked survival. Survival and drug-response data were not used during training, threshold selection, or tuning. The score was anchored mechanistically against CRISPR/DepMap essentiality[9], pathway enrichment, and a normal-tissue-filtered surface-protein candidate list (HPA[11], GTEx[12]).

To assess concordance between transcriptomic prioritisation and protein-level evidence, each ranked candidate was additionally annotated with two HPA-derived flags: HPA_surface_protein (Yes/No, derived from HPA Protein class and Subcellular location fields, identifying genes annotated as plasma-membrane, GPCR, ion-channel, transporter, receptor, or CD-marker) and HPA_antibody_reliability (Enhanced, Supported, Approved, Uncertain, or Not available, per HPA antibody validation tier). Annotations were merged on HGNC symbol; 248 of 250 candidates (99.2%) matched. Two candidates using the older CORF nomenclature did not auto-match HPAs lowercase convention and were resolved manually. HPAs per-gene RNA-protein numeric correlation is published only on per-gene web pages and not in the bulk download; we therefore used the detection-level and antibody-reliability tiers as the operational concordance filter.

ResultsCross-validation area under the receiver operating characteristic curve (AUROC) was 0.936 +/- 0.014 (held-out test 0.941, Matthews correlation coefficient (MCC) 0.696, F1-score 0.895). The 1,000-gene student showed Spearman {rho} {approx} 0.96 with the teacher and >85% class agreement at the prespecified threshold. The principal external result was in BeatAML: the score correlated with ex-vivo drug-response AUC across seven AML-relevant drugs, with consistent per-drug Spearman correlations (r = 0.41-0.53, all p < 0.05). The aggregate correlation across 3,164 patient-drug pairs from 452 patients was r = +0.482 and is reported as a summary, recognising that pairs from the same patient are not fully independent. The score did not stratify overall survival in TCGA-LAML or in the in-house n = 10 cohort, in part because predicted high-score fractions saturated. At the prespecified threshold the score did not separate cell types in GSE74246, indicating that absolute calibration is cohort-dependent. Compared against logistic regression, random forest, the LSC17 stemness signature, and a mean-expression baseline on the same gene panel, the Transformer was the most stable model under aliquot-grouped cross-validation and the only one to transfer with strong, positive correlation to BeatAML drug-AUC. The mechanistic candidate-target pipeline produced a 250-candidate ranked surface-protein list (full breakdown in Results); FLT3 and CD33 were recovered from the unbiased ranking as positive controls.

ConclusionWe present a Transformer-derived transcriptomic score that addresses the lack of validated computational methods for identifying drug-tolerant persister-like states in AML. The score shows external rank-order association with ex-vivo drug response, providing a research-use tool for prioritising candidate persister-associated transcriptional programs for follow-up.

Together, these results support the score as a research-use transcriptomic ranking tool for AML drug-response-associated states. The strongest external support comes from the consistent association with BeatAML ex-vivo drug-response AUC. The fixed probability threshold did not transfer reliably across all cohorts, so threshold-based classification should require cohort-specific recalibration. The score is not validated for clinical decision-making and is not proposed as a survival predictor. The candidate-target list is a starting point for functional follow-up.

---

## 论文详细总结（自动生成）

好的，遵照您的要求，以下是对该论文的结构化、深入、客观的中文总结。

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：急性髓系白血病（AML）中，存在一种被称为“药物耐受持久细胞”（DTP）的状态，这种状态被认为是导致疾病复发的重要原因。然而，目前缺乏一种专门为AML设计的、经过充分验证的计算方法，能够从转录组数据中准确识别并量化这种DTP状态。
- **整体含义**：现有的方法要么依赖于固定的基因标志，缺乏泛化能力；要么是事后调整的通用细胞类型分类器，并非专门针对DTP状态设计，且缺乏校准的概率输出、预设阈值以及针对体外药物反应的透明外部验证。本文旨在填补这一分析方法的空白，提供一个可泛化、有校准概率且与药物反应相关的转录组评分工具，以帮助研究人员优先排序后续的实验工作。
- **研究动机**：开发一个能够从转录组数据中评估DTP状态、泛化到新样本、输出校准概率并与候选生物学机制建立联系的深度学习方法。

### 2. 论文提出的方法论：核心思想、关键技术细节、算法流程
- **核心思想**：采用**知识蒸馏**策略，首先训练一个强大的**Transformer教师模型**，然后将其知识迁移到一个更轻量、更实用的**1000基因学生模型**上，该学生模型能够输出一个介于0和1之间的概率评分，用以指示细胞处于DTP状态的可能性。
- **关键技术细节与流程**：
    1.  **数据准备**：使用一个由9个样本（6个肺腺癌样本和3个原发AML样本）混合的scRNA-seq数据集，共32,342个细胞，13,369个共有基因。
    2.  **教师模型训练**：训练一个**Transformer分类器**作为教师模型，其任务是区分“DTP样”细胞（训练数据中被标记为正类的类别）和其他细胞。采用分层5折交叉验证。
    3.  **阈值设定**：在交叉验证的折外预测结果上，预先设定一个**概率阈值τ=0.31**，高于此阈值则判为DTP样状态。
    4.  **学生模型蒸馏**：通过**知识蒸馏**技术，训练一个仅包含1000个基因的轻量级学生模型，使其输出接近教师模型的预测结果。最终，对于每个输入的细胞，学生模型输出一个称为“评分”（score）的概率值。
    5.  **迁移应用**：将训练好的学生模型（未经任何调整）直接应用于五个外部或独立队列，生成每个细胞的评分，并评估其与药物反应和生存数据的关系。

### 3. 实验设计：数据集、基准与对比方法
- **数据集与场景**：
    - **训练集**：9个样本混合的scRNA-seq数据集（GSE123902 + 3个原发AML样本）。
    - **验证/应用场景**：五个独立外部队列，涵盖不同规模和数据类型：
        - 内部39个原发AML供体队列（bulk RNA-seq）。
        - **GSE74246**（bulk RNA-seq）。
        - **BeatAML**（n=452，链接体外药物AUC数据；n=405，生存数据）：**主要的外部验证数据集**。
        - **TCGA-LAML**（n=149）。
        - 内部n=10的scRNA-seq队列（链接生存数据）。
- **基准（Benchmark）**：
    - 与几种基线方法进行了比较，包括：逻辑回归、随机森林、LSC17干性特征签名、以及同一基因面板的平均表达基线。
    - 对比了**scPred, scANVI, scClassify**等通用细胞类型分类器。
- **对比方法与指标**：
    - **主要指标**：交叉验证AUROC、与BeatAML体外药物AUC的Spearman相关系数。还报告了预测性指标（MCC, F1分数）和机制性验证（CRISPR/DepMap必需性、通路富集）。

### 4. 资源与算力
- 文中**未明确说明**训练模型所使用的具体GPU型号、数量、训练时长等算力资源。

### 5. 实验数量与充分性
- **实验数量**：论文做了多组实验，包括：
    - **模型性能验证**：交叉验证AUROC、保留测试集AUROC。
    - **知识蒸馏验证**：学生模型与教师模型的评分相关性（Spearman ρ≈0.96）和类别一致性（>85%）。
    - **主要外部验证**：在BeatAML队列中，针对7种AML相关药物，每个药物与评分的Spearman相关性检验。
    - **生存分析**：在TCGA-LAML和内部n=10队列中评估评分对总生存期的分层能力。
    - **机制验证**：CRISPR/DepMap必需性分析、通路富集分析、生成250个候选表面蛋白排名列表。
    - **对比实验**：与逻辑回归、随机森林等基线方法在交叉验证和BeatAML药物AUC相关性上的比较。
- **充分性与公平性**：
    - **充分性**：实验设计较为完整，覆盖了模型性能、泛化能力、外部验证和生物学解释。在BeatAML上的药物反应关联分析是其最有力的证据。
    - **客观性与公平性**：
        - **优点**：生存和药物反应数据未用于模型训练和调优，避免了过拟合。使用了多个独立外部队列进行验证。
        - **不足**：生存分析未得到阳性结果（评分未能对生存期进行有效分层），作者客观地报告了这一点，并解释了可能的原因（高评分比例饱和）。同时，也诚实地承认了预设阈值在不同队列间的迁移性不佳，需要重新校准。

### 6. 论文的主要结论与发现
1.  **高性能评分**：基于Transformer的模型（教师模型）在交叉验证中达到了**AUROC 0.936±0.014**的高性能，学生模型与之高度一致（ρ≈0.96）。
2.  **与体外药物反应显著相关**：在**BeatAML**这一最大外部队列中，该评分与多种AML相关药物的**体外AUC值**呈一致的正相关（单药r=0.41-0.53，汇总r=+0.482），表明高评分与更强的药物耐受性相关。
3.  **优于基线方法**：与逻辑回归、随机森林等基线模型相比，Transformer是交叉验证中最稳定的模型，并且是唯一一个在BeatAML药物AUC迁移验证中表现出强正相关性的模型。
4.  **可识别已知靶点**：候选目标分析流程从无偏排名中成功恢复了已知的AML药物靶点**FLT3**和**CD33**，作为阳性对照，验证了评分的生物学相关性。
5.  **局限性**：该评分并不能可靠地分层总生存期，且预设的概率阈值（0.31）在不同队列间的绝对校准性存在差异，不能直接迁移。
6.  **最终结论**：该评分是一个有价值的**研究用途工具**，可用于对AML中与药物反应相关的转录状态进行排序和优先化研究，但**不适用于临床决策或生存预测**。

### 7. 优点：方法或实验设计上的亮点
1.  **新颖性**：将先进的深度学习方法（Transformer、知识蒸馏）专门应用于AML药物耐受性评分领域，解决了现有方法的不足。
2.  **透明性与可复现性**：预设了概率阈值（0.31），并透明地展示了其在跨队列迁移时的局限性，体现了良好的科学诚实性。
3.  **全面的外部验证**：使用了多个独立队列进行验证，特别是包含了与体外药物反应数据（BeatAML）的直接关联，使方法更具说服力。
4.  **可解释性与实用性**：通过知识蒸馏得到一个1000基因的小模型，降低了计算成本，使其更易于被其他研究者应用。同时，生成的候选基因列表为后续的湿实验研究提供了直接起点。
5.  **公平比较**：与多个明确的基线方法（逻辑回归、随机森林、LSC17等）进行了系统比较，并客观地报告了自己模型的优势（强相关且稳定）和劣势（仅模型之一）。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制
1.  **临床验证不足**：模型未能预测总生存期，这是其作为临床工具的重大缺陷。它与体外药物反应的相关性，是否等同于在体内也能预测治疗反应和复发，尚需进一步验证。
2.  **队列校准问题**：预设阈值在不同队列间不可迁移，这意味着如果要将该评分用于特定队列的分类任务，必须重新进行校准，限制了其作为“即插即用”工具的便利性。
3.  **训练数据偏差风险**：训练集包含了肺腺癌数据，虽然扩大了数据量，但可能存在跨癌症类型的偏差。模型对AML的特异性是否会因此受到影响，文中未进行深入讨论。
4.  **计算资源未公开**：未提供训练所需的算力信息，不利于其他团队复现或评估其成本。
5.  **核心假设的验证**：模型训练时使用的DTP细胞定义依赖于作者在数据上的标记。这个标记过程本身是否准确、是否完全代表了DTP状态，可能存在主观性。缺乏独立的数据集来严格验证这个训练标签的可靠性。
6.  **分析粒度**：主要在患者/bulk RNA-seq层面验证了评分与药物AUC的相关性。虽然衍生自scRNA-seq，但学生模型在单细胞上的表现和应用分析相对较少，其在不同细胞亚型间的具体分布和功能关联有待更细化。

（完）
