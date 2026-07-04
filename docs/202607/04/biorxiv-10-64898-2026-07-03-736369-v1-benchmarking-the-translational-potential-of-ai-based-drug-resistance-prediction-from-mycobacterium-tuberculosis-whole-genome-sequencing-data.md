---
title: Benchmarking the translational potential of AI-based drug-resistance prediction from Mycobacterium tuberculosis whole-genome sequencing data
title_zh: 基于人工智能的结核分枝杆菌全基因组测序数据耐药性预测的转化潜力基准测试
authors: "Liu, C., Zhu, H., Zhou, P., Thanh, N. T., Dat, N. Q., Atmosukarto, I., Cheong, I. H., Kozlakidis, Z., Adisasmito, W., Zheng, X., Wang, H., Yang, Y."
date: 2026-07-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.03.736369v1.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 基于全基因组测序数据的AI耐药预测基准测试，直接针对机器学习耐药预测
tldr: 结核病耐药预测方法因数据集和评价标准不统一难以公平比较。本文构建了包含54364对全基因组测序-药敏试验的大规模统一基准，评估7种模型在18种药物及6种临床耐药类别上的表现。XGBoost在精确率-召回率上最佳，随机森林特异性高，逻辑回归召回率高；床奎、德拉马尼等新药和广泛耐药预测仍是瓶颈。该基准为社区提供标准评估平台，加速WGS耐药预测临床转化。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有结核耐药预测方法因数据集异质无法公平比较，缺乏统一基准阻碍临床转化。
method: 整合三个来源构建54364对WGS-表型药敏记录的统一基准，评估7种模型在18种药物和6种临床耐药类别上的性能。
result: XGBoost平均AUPRC和F1最优，WDNN在AUROC最优；床奎、德拉马尼等新药和XDR预测困难。
conclusion: 提供了最大统一基准，经典ML方法整体最优，新药和XDR是未来关键瓶颈。
---

## 摘要
背景：结核病，尤其是耐药结核病（DR-TB），包括耐多药（MDR）和广泛耐药（XDR）菌株，仍是全球感染性死亡的主要原因之一。全基因组测序（WGS）数据的快速积累推动了大量预测结核分枝杆菌抗菌药物耐药性的计算方法。然而，异构数据集、预处理流程和评估协议使得公平比较无法进行，并阻碍了临床转化。目前急需一种大规模、统一的基准测试，以系统评估和比较现有方法。方法：我们从三个来源整合了MTB WGS-表型药敏试验（pDST）数据集：CRyPTIC数据集（结核病综合耐药性预测国际联盟）、已发表的多研究汇编以及新整理文献来源的数据集。最终基准包含54,364条配对的WGS-pDST记录，具有广泛的地理分布、谱系和药物覆盖范围。在统一表型并生成标准化变异特征后，我们评估了七种模型（包括经典机器学习和深度学习架构），涉及18种药物水平和六种临床耐药类别预测任务。结果：XGBoost在药物水平上获得了平均AUPRC（0.674）和F1分数（0.620）的最高值，并在18种药物中的11种中AUPRC排名第一，而WDNN获得了平均AUROC的最高值。随机森林获得了平均特异性（0.956）和准确率（0.933）的最高值，而逻辑回归获得了平均召回率（0.774）的最高值，突显了不同的临床权衡。药物水平难度高度异质：利福平和异烟肼预测稳健，而贝达喹啉、德拉马尼、利奈唑胺和氯法齐明仍然持续困难。在临床耐药类别评估中，利福平耐药结核病（RR-TB）、耐多药结核病（MDR-TB）和全敏感结核病预测良好，但广泛耐药结核病（XDR-TB）和其他耐药类别构成了主要瓶颈。结论：在迄今为止最大的统一基准测试下，经典机器学习方法，特别是XGBoost，整体上提供了最强的精确率-召回率和F1性能，而神经网络模型在AUROC方面仍具竞争力。新兴药物（贝达喹啉、德拉马尼、利奈唑胺、氯法齐明）和XDR病例仍然难以预测，这指出了未来方法开发的关键瓶颈。该基准可作为评估MTB耐药性预测的社区标准，所提供的评估流程为监管认证和临床决策支持系统验证提供了可操作的基线，从而加速基于WGS的耐药性预测向实践的转化。

## Abstract
Background: Tuberculosis, especially drug-resistant tuberculosis (DR-TB) including multidrug-resistant (MDR) and extensively drug-resistant (XDR) strains, remains a leading cause of infectious death worldwide. The rapid accumulation of whole-genome sequencing (WGS) data had spurred numerous computational methods for predicting antimicrobial resistance in Mycobacterium tuberculosis. However, heterogeneous datasets, preprocessing pipelines, and evaluation protocols have made fair comparisons impossible and have hindered clinical translation. A critical yet missing resource is a large-scale, unified benchmark to systematically assess and compare existing methods. Methods: We curated an integrated MTB WGS--phenotypic drug susceptibility testing (pDST) dataset from three sources: the CRyPTIC dataset (Comprehensive Resistance Prediction for Tuberculosis: an International Consortium), a published multi-study compilation, and newly curated literature-derived datasets. The final benchmark contains 54,364 paired WGS-pDST records with broad geographic, lineage, and drug coverage. After harmonizing phenotypes and generating standardized variant features, we evaluated seven models (including classical machine learning and deep learning architectures) across 18 drug-level and six clinical resistance category prediction tasks. Results: XGBoost achieved the highest mean drug-level AUPRC (0.674) and F1-score (0.620) and ranked first in AUPRC for 11 of 18 drugs, whereas WDNN achieved the highest mean AUROC. Random forest yielded the highest mean specificity (0.956) and accuracy (0.933), whereas logistic regression achieved the highest mean recall (0.774), highlighting distinct clinical trade-offs. Drug-level difficulty was highly heterogeneous: rifampicin and isoniazid were predicted robustly, whereas bedaquiline, delamanid, linezolid, and clofazimine remained persistently difficult. In clinical resistance category evaluation, RR-TB, MDR-TB, and pan-susceptibility were well predicted, but XDR-TB and other resistance categories constituted major bottlenecks. Conclusions: Under the largest unified benchmark to date, classical machine-learning methods, particularly XGBoost, provided the strongest precision--recall and F1 performance overall, while neural models remained competitive by AUROC. Emerging drugs (bedaquiline, delamanid, linezolid, clofazimine) and XDR cases remain persistently difficult to predict, identifying key bottlenecks for future method development. This benchmark can serve as a community standard for evaluating MTB resistance prediction and the provided evaluation pipeline offers an actionable baseline for regulatory qualification and clinical decision support system validation, accelerating the translation of WGS-based resistance prediction into practice.

---

## 论文详细总结（自动生成）

# 1. 论文的核心问题与整体含义
- **研究动机**：结核病（TB）尤其是耐药结核（DR-TB）仍是全球主要致死传染病之一。全基因组测序（WGS）数据快速增长，催生了大量基于AI的耐药预测方法，但由于数据集、预处理流程和评估协议高度异构，方法之间无法公平比较，严重阻碍了临床转化。
- **整体含义**：本文构建了目前规模最大的统一基准（54364对WGS-表型记录），通过标准化评估7种模型在18种药物和6种临床耐药类别上的性能，旨在为社区提供可复用的评价平台，加速基于WGS的耐药预测从研究走向临床应用。

# 2. 论文提出的方法论
- **核心思想**：整合多源异构数据，统一表型定义（pDST）和变异特征（如SNP/indel），在标准化条件下横向比较不同机器学习和深度学习模型的预测能力。
- **关键技术细节**：
  - 数据来源：CRyPTIC数据集、已发表的多研究汇编、新整理的文献数据集。
  - 特征工程：统一生成标准化变异特征（具体方法未在摘要中详述，通常依赖比对和变异检测流程）。
  - 模型集合：共7种，包括经典ML（逻辑回归、随机森林、XGBoost等）和深度学习架构（如WDNN）。
  - 评估指标：AUPRC、AUROC、F1分数、特异性、准确率、召回率。
- **流程说明**：数据收集 → 统一表型→生成变异特征 → 划分训练/测试集 → 训练/调优7种模型 → 在18个药物水平和6个临床类别任务上计算上述指标 → 汇总排名和分析。

# 3. 实验设计
- **数据集**：最终基准包含54,364条配对的WGS-pDST记录，覆盖广泛地理区域、谱系及18种抗菌药物（包括一线、二线及新药）。
- **任务场景**：
  - 药物水平预测：18种药物（如利福平、异烟肼、贝达喹啉、德拉马尼等）的二分类（敏感/耐药）。
  - 临床耐药类别：6种类别（利福平耐药RR-TB、耐多药MDR-TB、广泛耐药XDR-TB、全敏感等）的多类/多标签分类。
- **对比方法**：7种模型（XGBoost、随机森林、逻辑回归、WDNN等），未列出全部具体模型名称，但摘要明确比较了它们在多个指标上的表现。
- **Benchmark**：本文构建的基准本身即为评估标准，所有模型在同一数据集、同一特征和同一评估协议下比较，保证了公平性。

# 4. 资源与算力
- 文中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。仅提及“评估了七种模型”，未提供计算资源细节。这可能是因为预印本未包含附录的实验环境说明，待正式发表时补充。

# 5. 实验数量与充分性
- **实验数量**：共涉及7个模型 × (18个药物任务 + 6个临床类别任务) = 至少168个主要实验（每个任务计算多个指标），加上可能的多折交叉验证或重复实验，总量较大。
- **充分性**：
  - 使用了目前最大统一数据集，覆盖广泛药物和临床类别，实验设计全面。
  - 对比了经典ML和深度学习，并报告了多个互补指标（AUPRC、AUROC、特异性等），能反映不同临床权衡。
  - **不足**：未提及消融实验（如特征选择、模型超参数影响）、未报告统计显著性检验（如配对比较）、未讨论数据不平衡的处理策略。总体而言，基准测试的广度高，但深度稍欠（如缺乏对模型可解释性、失败案例分析）。

# 6. 论文的主要结论与发现
- **整体性能**：XGBoost在平均AUPRC（0.674）和F1（0.620）上最优，在18种药物中11种AUPRC排名第一；WDNN在平均AUROC上最优；随机森林特异性（0.956）和准确率（0.933）最高；逻辑回归召回率（0.774）最高。
- **药物难度差异**：利福平和异烟肼预测稳健；贝达喹啉、德拉马尼、利奈唑胺、氯法齐明等新药预测持续困难。
- **临床类别瓶颈**：RR-TB、MDR-TB和全敏感预测良好；XDR-TB及其他耐药类别仍是主要瓶颈。
- **方法学偏好**：经典ML（特别是XGBoost）在精确率-召回率权衡上整体优于深度学习，而深度学习在AUROC上仍有竞争力。不同模型适合不同临床场景（例如高特异性选随机森林，高召回率选逻辑回归）。

# 7. 优点
- **规模与统一性**：构建了迄今为止最大的MTB耐药预测统一基准，解决了长期困扰该领域的数据异质性比较问题。
- **评估全面性**：覆盖18种药物（包括新药）和6种临床类别，使用多指标综合评价，能指导具体应用场景的模型选择。
- **社区贡献**：提供的评估流程和基线结果可作为监管认证和临床决策支持系统验证的参考标准，加速转化。
- **公正性**：所有模型在同一数据管线、同一划分下训练和测试，避免了先前研究中的评测偏差。

# 8. 不足与局限
- **表型局限性**：仅采用了pDST作为金标准，但pDST本身存在一致性差、阈值不统一等问题，可能引入噪声。
- **新药和XDR数据稀缺**：贝达喹啉、德拉马尼等新药耐药样本量小，导致预测困难，基准可能无法充分评估这些药物上的模型能力。
- **计算资源未报告**：缺少GPU、训练时间等细节，影响可复现性。
- **模型覆盖面有限**：仅评估了7种模型，未纳入最新方法（如Transformer、图神经网络、集成变异调用器），也未进行特征重要性或因果推断分析。
- **缺乏外部验证**：虽然数据整合了多来源，但未设置独立外部验证集（如真实临床队列），临床转化仍需前瞻性验证。
- **统计检验缺失**：未提供模型间性能差异的显著性检验，某些排名可能受随机波动影响。
- **可解释性不足**：未探讨哪些特征（基因、突变）驱动了模型的预测，这对生物学验证和临床解释很重要。

（完）
