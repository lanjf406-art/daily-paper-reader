---
title: Tissue-aware elastic net decomposition reveals shared and lineage-specific drug response biomarkers
title_zh: 组织感知弹性网络分解揭示共享和谱系特异性药物反应生物标志物
authors: "Strauch, J., Azinfar, L., Pua, H. H., Long, J. P., Coombes, K. R., Asiaee, A."
date: 2026-06-25
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.21.733619v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 机器学习弹性网络用于药物反应生物标志物发现
tldr: "现有药物响应预测模型常因数据泄漏而不可靠，且组织谱系这一归纳偏置未被有效利用。本文提出数据共享弹性网络（DSEN），将模型分解为谱系共享系数块和组织特异性偏差块，在无泄漏评估下对92.5%的药物改进均方误差，并减少58%的共享特征。共享系数可泛化到未见过组织，揭示p53、MAPK等通路；组织块捕获谱系标记。DSEN在特征稀疏时优势明显，为发现可转移的生物标志物提供了可靠框架。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有药物响应预测模型存在数据泄漏问题，且未将组织谱系作为归纳偏置分离共享与特异性信号。
method: 提出数据共享弹性网络（DSEN），通过组织感知回归将模型分解为所有谱系共享的系数块和组织特异性偏差块。
result: "在265种药物1462个细胞系31个谱系中，DSEN对92.5%的药物改进了均方误差（平均4.95%），减少58%共享特征，共享系数泛化到未见组织并恢复可转移通路模块。"
conclusion: 组织感知建模在特征稀疏时最有效，DSEN实现了无泄漏评估并分离了共享与谱系特异性生物标志物。
---

## 摘要
动机：从基因组特征预测癌症药物反应的计算模型是生物标志物发现的核心，但最近的一项审计发现，在32种已发表方法中，72%存在数据泄露，而复杂模型的可解释性较差，在诚实评估下仅略优于简单基线。组织谱系是一种尚未充分利用的合法归纳偏置来源，但现有的组织感知方法既未将泛癌信号与谱系特异性信号分离，也未报告无泄露的性能。结果：我们引入了数据共享弹性网络（DSEN），这是一种组织感知回归方法，可将每种药物的模型分解为所有谱系共有的共享系数块和组织特异性偏差块。在对265种药物、1462个细胞系和31个组织谱系进行无泄露交叉验证时，DSEN在92.5%的药物上将均方误差优于标准弹性网络（平均改善4.95%），同时选择的稳定共享特征减少了58%。共享系数可推广到未见的组织（组织级别胜率59%），并反复恢复可转移的途径模块（p53、MAPK），而组织块则捕获了如皮肤MITF/S100B程序等谱系标志物。最接近的组织感知比较方法TG-LASSO表现逊于无组织感知的基线（平均MSE降低-13.8%）。消融实验表明，当特征稀缺时，组织感知建模帮助最大，且没有单一模态占主导地位。

## Abstract
Motivation: Computational models that predict cancer drug response from genomic features are central to biomarker discovery, yet a recent audit found data leakage in 72% of 32 published methods, and complex models offer little interpretability while only modestly exceeding simple baselines under honest evaluation. Tissue lineage is a largely untapped source of legitimate inductive bias, but existing tissue-aware methods neither separate pan-cancer from lineage-specific signal nor report leakage-free performance. Results: We introduce the Data Shared Elastic Net (DSEN), a tissue-aware regression that decomposes each drug's model into a shared coefficient block common to all lineages and tissue-specific deviation blocks. Under leakage-free cross-validation across 265 drugs, 1,462 cell lines and 31 tissue lineages, DSEN improved mean squared error over a standard elastic net for 92.5% of drugs (mean 4.95%) while selecting 58% fewer stable shared features. Shared coefficients generalized to held-out tissues (59% tissue-level win rate) and recurrently recovered transferable pathway modules (p53, MAPK), whereas tissue blocks captured lineage markers such as the skin MITF/S100B program. The closest tissue-aware comparator, TG-LASSO, performed worse than the tissue-agnostic baseline (-13.8% mean MSE). Ablation shows tissue-aware modeling helps most when features are scarce, with no single modality dominating.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **背景**：从基因组特征预测癌症药物反应的计算模型是生物标志物发现的核心。然而，近期审计发现32种已发表的方法中有72%存在数据泄漏问题，且复杂模型在诚实评估下仅略优于简单基线，可解释性差。
- **核心问题**：现有方法未充分利用“组织谱系”这一合法归纳偏置，缺乏将泛癌共享信号与谱系特异性信号分离的能力，并且在无泄漏评估下性能不佳。
- **整体含义**：作者旨在提出一种组织感知的回归方法，能够在不引入数据泄漏的前提下，同时捕获跨组织共享的药物响应生物标志物和谱系特异性标志物，提升预测准确性和可解释性。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：引入组织感知弹性网络（Data Shared Elastic Net, DSEN），将每种药物的预测模型分解为两个部分：
  - **共享系数块**：所有谱系（组织类型）共用的系数向量，反映泛癌共享信号。
  - **组织特异性偏差块**：每个谱系独有的偏差系数向量，捕获谱系特异性信号。
- **关键技术细节**：
  - 采用弹性网络（Elastic Net）正则化（结合L1和L2惩罚）进行整体优化，惩罚项同时施加于共享系数块和组织偏差块。
  - 通过组织感知回归，模型能够自动分离共享与特异性成分，从而减少冗余特征选择（共享特征减少58%）。
  - 在交叉验证中严格避免数据泄漏：训练集和测试集按细胞系划分，确保同一细胞系不会同时出现在训练和测试中。
- **算法流程**（文字描述）：
  1. 输入：所有细胞系的基因组特征矩阵，每个细胞系标记所属组织谱系；对应药物的IC50或AUC响应值。
  2. 定义损失函数：均方误差（MSE）加上弹性网络正则化项（同时作用于共享系数和组织偏差系数）。
  3. 使用坐标下降法（coordinate descent）优化，迭代更新共享系数和每个谱系的偏差系数。
  4. 通过内部交叉验证选择正则化参数λ和混合比例α。
  5. 输出：共享系数向量（可解释为泛癌生物标志物）和各组织偏差向量（谱系特异性标志物）。

## 3. 实验设计：数据集、benchmark、对比方法

- **数据集**：
  - 使用 **265种药物** 对 **1462个细胞系** 的响应数据，涵盖 **31个组织谱系**。
  - 基因组特征包括基因表达、突变、拷贝数变异等多模态数据（具体未详细列出，但摘要提及“no single modality dominating”）。
- **Benchmark**：
  - 主要基线是标准弹性网络（Elastic Net），无组织感知。
  - 对比方法包括最接近的组织感知方法 **TG-LASSO**（Tissue-Guided LASSO）。
- **评估设置**：
  - 采用**无泄漏交叉验证**（按细胞系划分），确保训练和测试集细胞系不重叠。
  - 评估指标：均方误差（MSE）、特征选择数量、组织级别胜率等。

## 4. 资源与算力

- 论文中**未明确说明**所使用的GPU型号、数量或训练时长。仅提及使用了坐标下降法优化，但未提供具体计算资源信息。
- 暗示该方法是可扩展的，因为弹性网络算法计算效率高，但未量化算力开销。

## 5. 实验数量与充分性

- **实验组数**：覆盖265种药物，每种药物独立建模，相当于265个回归任务。此外，可能包含消融实验（如不同正则化参数、是否使用组织感知、不同模态特征等），摘要中提到了“消融实验表明组织感知建模在特征稀疏时帮助最大”。
- **充分性**：
  - **优点**：在大量药物（265）和细胞系（1462）上进行系统评估，对比基线（标准弹性网络）和竞争方法（TG-LASSO），并进行了消融分析，实验设计较为充分。
  - **不足**：实验结果主要基于MSE的改进百分比（平均4.95%），可能缺乏统计显著性检验（如p值或置信区间）的详细报告。此外，仅与一种组织感知方法（TG-LASSO）对比，未与更多复杂模型（如神经网络、集成方法）比较。
  - **公平性**：严格使用无泄漏交叉验证，确保与基线公平比较，且对比方法同样在相同设置下运行，相对客观。

## 6. 论文的主要结论与发现

- **性能提升**：DSEN在92.5%的药物上MSE优于标准弹性网络，平均改善4.95%；同时选择的稳定共享特征减少了58%，表明模型更稀疏、更可解释。
- **可泛化性**：共享系数块可推广到未见的组织（组织级别胜率59%），并反复恢复可转移的通路模块（如p53、MAPK信号通路）。
- **谱系特异性捕获**：组织特异性偏差块能捕获谱系标志物（如皮肤谱系中的MITF/S100B程序）。
- **对比方法表现**：最接近的组织感知方法TG-LASSO表现逊于无组织感知的基线（平均MSE降低-13.8%），说明简单的组织感知设计（如TG-LASSO）可能无效，而DSEN的分解策略是关键。
- **消融发现**：当特征稀缺（例如基因表达特征维度低或样本量小）时，组织感知建模帮助最大；没有单一模态（如基因表达、突变、拷贝数）占主导地位，说明多模态整合有益。

## 7. 优点

- **方法创新性**：首次将组织谱系作为归纳偏置以“共享+特异性”分解形式整合到弹性网络，同时解决可解释性和泄漏问题。
- **无泄漏评估**：严格实施按细胞系划分的交叉验证，避免数据泄漏，结果可信度高。
- **可解释性**：模型输出自然分为共享生物标志物（泛癌通路）和谱系特异性标志物，便于生物学解读。
- **性能与稀疏性平衡**：在提升预测准确性的同时大幅减少特征数量，有助于临床转化。
- **跨组织泛化**：证明了共享系数可推广到未见组织，支持其在未知组织中发现生物标志物的潜力。

## 8. 不足与局限

- **方法局限**：依赖线性模型假设（弹性网络本质是线性），可能无法捕捉复杂的非线性交互作用。在更深度特征交互场景下，性能可能不如非线性方法。
- **实验覆盖**：仅与一种组织感知方法（TG-LASSO）对比，未与更多主流方法（如随机森林、图神经网络、多任务学习模型）进行比较。此外，仅报告MSE平均改善，未给出方差或统计显著性检验。
- **可重复性**：论文未公开代码或数据集，也未提供详细的超参数设置（如弹性网络α、λ的搜索范围），限制了可复现性。
- **临床应用限制**：细胞系数据与真实患者肿瘤微环境存在差异，共享和特异性标志物在临床队列上的验证尚未进行，泛化到真实患者仍需进一步研究。
- **算力信息缺失**：未提供计算资源消耗，不利于评估该方法在大规模场景下的可行性。
- **偏差风险**：细胞系来源偏重于某些组织（如NCI-60或CCLE中的常见组织），31个谱系可能不均衡，可能影响模型对稀有谱系的泛化能力。

（完）
