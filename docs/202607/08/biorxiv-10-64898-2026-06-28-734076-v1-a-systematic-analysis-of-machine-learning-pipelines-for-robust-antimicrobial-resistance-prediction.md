---
title: A systematic analysis of machine learning pipelines for robust antimicrobial resistance prediction
title_zh: 用于稳健抗菌药物耐药性预测的机器学习流水线的系统分析
authors: "Aselstyne, A., Karthik, E. N., El Azami, M., Pogorelcnik, R., Fournier, Q., Chandar, S."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.28.734076v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 机器学习管道用于药物耐药预测，可转移到肿瘤耐药场景
tldr: "抗菌素耐药性(AMR)是全球公共卫生威胁，从全基因组测序数据准确预测表型可加速临床决策。本研究系统分析了机器学习管道，针对9种病原体-抗生素组合，重新标记当前CLSI折点实现高达56%数据扩充，优化k-mer长度使F1分数提升20+点。随机交叉验证可很好地代理下游临床性能，且超过95%的k-mer与可识别基因组特征相关。"
source: biorxiv
selection_source: fresh_fetch
motivation: AMR是重大全球公共卫生威胁，准确预测耐药表型对于临床决策和减缓耐药传播至关重要。
method: 分析了9种物种-抗生素组合的ML管道，涉及重新标记、k-mer长度选择、特征矩阵截断、模型比较以及不同交叉验证策略。
result: "重新标记实现19%标签交换和56%数据扩充；优化k-mer长度提升F1超20点；随机交叉验证与临床性能接近。"
conclusion: 特征设计、评估协议和生物学分析对基因组AMR预测很重要，树模型是鲁棒且可解释的方法。
---

## 摘要
动机：抗菌药物耐药性（AMR）已被确定为全球公共卫生的主要威胁。从全基因组测序数据中准确预测AMR表型是加速临床决策和减缓耐药性传播的重要工具。尽管许多先前的研究已经探索了使用基于树的机器学习（ML）模型来预测耐药性，但该领域缺乏对不同病原体物种和抗生素的训练流水线的系统评估。结果：利用NCBI抗菌药物敏感性测试数据库中的九种临床相关的物种-抗生素组合，我们详细分析了ML流水线，并确定了影响模型性能和评估的关键因素。我们首先使用当前的CLSI最低抑菌浓度折点对所有分离株进行重新标记，以解决不一致性并增加可用数据，导致每个物种-抗生素组合的标签交换率高达19%，数据扩展率高达56%。我们确定了几个关键的训练参数，包括k-mer长度（与常用k值相比，可将分类F1分数提高20分以上）、特征矩阵截断（可导致多项式时间减少，性能降低有限）以及ML模型类别。通过比较5折交叉验证与在未见过的临床数据集上的评估，我们表明随机交叉验证分割（经常被批评为过于乐观）可以作为下游临床性能的强代理，在所有情况下都产生比系统发育感知分割更接近的F1分数。最后，我们呈现了一项可解释性研究，表明我们的模型使用的超过95%的k-mer与可识别的基因组特征相关。我们的结果强调了特征设计、评估协议和生物学分析在基因组AMR预测中的重要性，并支持基于树的模型作为一种稳健且可解释的方法。

## Abstract
Motivation: Antimicrobial resistance (AMR) has been identified as a top global public health threat. Accurate AMR phenotype prediction from whole-genome sequencing data is an essential tool for accelerating clinical decision-making and mitigating resistance spread. Although many previous works have explored the use of tree-based machine learning (ML) models to predict resistance, the field lacks a systematic evaluation of the training pipeline across a variety of pathogenic species and antibiotics. Results: Using nine clinically relevant species-antibiotic combinations from the NCBI antimicrobial susceptibility testing database, we present a detailed analysis of the ML pipeline and identify key factors affecting model performance and evaluation. We begin by relabelling all isolates using current CLSI minimum inhibitory concentration breakpoints to resolve inconsistencies and increase available data, resulting in up to a 19% label swap and 56% data enlargement per species-antibiotic combination. We identify several key training parameters including k-mer length, which can increase classification F1 scores by over 20 points compared to commonly used k-values, feature matrix truncation, which can induce polynomial time reductions with limited performance reduction, and ML model class. By comparing 5-fold cross-validation with evaluation on an unseen clinical dataset, we show that random cross-validation splits--often criticized as overly optimistic--can act as a strong proxy for downstream clinical performance, yielding closer F1 scores than phylogeny-aware splits in all cases. We finally present an interpretability study which shows that over 95% of k-mers used by our models are associated with identifiable genomic features. Our results highlight the importance of feature design, evaluation protocol, and biological analysis in genomic AMR prediction, and support tree-based models as a robust and interpretable method.