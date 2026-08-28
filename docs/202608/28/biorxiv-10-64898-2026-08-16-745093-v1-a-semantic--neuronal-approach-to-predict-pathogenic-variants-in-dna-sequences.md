---
title: A Semantic + Neuronal Approach to Predict Pathogenic Variants in DNA Sequences
title_zh: 一种语义+神经元方法预测DNA序列中的致病变异
authors: "Motta, J. A., Motta, M. d. M., Fernandez, C."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.16.745093v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 用CRF和BiLSTM预测致病性变异，方法可迁移至耐药突变预测
tldr: 致病性基因变异预测是精准医学的重要任务，但现有方法依赖传统特征，性能有限。本文提出一种结合语义模型与深度学习的混合方法：从ClinVar数据库提取正常与致病序列，将DNA转换为符合语法的肽序列并应用词性标注，然后利用条件随机场与双向长短期记忆网络进行序列建模。在105个基因约27000个致病变异上的实验表明，该方法在精度、PR、ROC和AUC等指标上显著优于五种已有方法，达到当前最佳水平，为致病性变异预测提供了新途径。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有致病性变异预测方法依赖传统特征，准确率有限，需要结合语义与上下文信息的新模型。
method: 从ClinVar数据库提取序列，将DNA转为肽序列并进行词性标注，采用条件随机场与双向长短期记忆网络建模。
result: 在105个基因约27000个变异上评估，精度、PR、ROC和AUC等指标均超过五种现有方法。
conclusion: 结合语义模型与神经网络能有效提升致病性变异预测能力，为精准医疗提供新工具。
---

## 摘要
在本工作中，我们提出了一种用于识别致病变异DNA的机器学习模型。该模型通过分析从ClinVar数据库（由NCBI支持）中提取的正常和致病序列学习得到。该分析基于DNA序列的概念语义模型，该模型将DNA序列转换为由明确语法控制的肽序列（氨基酸序列），从而使我们能够应用NLP技术，特别是词性标注（POS tagging）。我们的预测模型通过结合两种技术构建：CRF（来自马尔可夫模型家族），负责序列建模，以及BiLSTM（一种深度学习模型），捕获序列的过去和未来内容。训练空间由与约27,000个致病变异相关的105个基因的序列创建。使用精确率、P-R曲线和ROC曲线、AUC以及混淆矩阵等指标对模型进行了评估。其性能还与五种已知的致病变异预测方法进行了比较。结果显示，该方法的卓越性能超出了预期，使这种新方法在预测致病DNA序列方面达到了最新技术水平。

## Abstract
In this work, we present a machine learning model for identifying pathogenic DNA variants. The model was learned from the analysis of normal and pathogenic sequences extracted from the ClinVar database (supported by NCBI). This analysis was based on a conceptual semantic model of DNA sequences converted to peptide sequences (amino acid sequences) governed by a well-defined grammar, which allowed us to apply NLP techniques, specifically Part of Speech tagging (POS tagging). Our predictive model was built by combining two techniques: CRF (from the Markov model family), which performs the sequencing, and BiLSTM (a deep learning model) which captures the past and future content of the sequences. The training space was created with the sequences of 105 genes associated with approximately 27,000 pathogenic variants. The model was evaluated using the metrics precision, P-R and ROC curves, AUC, and confusion matrices. Its performance was also compared against five known methods for predicting pathogenic variants. The results show exceptional performance that exceeds expectations and places this new method at the state of the art for predicting pathogenic DNA sequences.