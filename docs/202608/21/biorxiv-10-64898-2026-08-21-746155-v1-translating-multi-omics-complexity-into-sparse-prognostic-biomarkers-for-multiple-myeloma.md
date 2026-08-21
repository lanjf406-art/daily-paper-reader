---
title: Translating multi-omics complexity into sparse prognostic biomarkers for multiple myeloma
title_zh: 将多组学复杂性转化为多发性骨髓瘤的稀疏预后生物标志物
authors: "Obermayer, B., Benary, M., Kroenke, J., Mertins, P., Beule, D."
date: 2026-08-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.21.746155v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 多组学整合与监督分类方法，可迁移至肿瘤耐药多组学刻画
tldr: 多发性骨髓瘤存在跨组学调控异质性，单一组学难以刻画预后。本研究整合拷贝数、转录组、蛋白组和磷酸化组数据，发现下游蛋白层能更好分类基因组事件，并借助MOFA2识别出独立于R-ISS的连续预后因子。进一步用弹性网络构建RNA稀疏代理，在外部队列中验证了其稳健预后价值，为临床转化提供了桥梁。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有风险分层依赖细胞遗传学或单组学特征，无法捕捉跨层调控复杂性。
method: 整合多组学数据，用监督分类比较各层分类能力，并用MOFA2提取预后因子，弹性网络构建RNA代理。
result: 蛋白层分类更准，MOFA2因子独立预测生存，RNA代理在外部队列中验证有效。
conclusion: 多组学整合可揭示被单组学隐藏的预后轴，稀疏代理能促进临床落地。
---

## 摘要
多发性骨髓瘤（MM）表现出深刻的分子异质性，但当前的风险分层依赖于细胞遗传学或单组学特征，往往无法捕捉跨层级的调控复杂性。我们重新分析了一个整合拷贝数、转录组、蛋白质组和磷酸化蛋白质组数据的多组学数据集，以剖析常见基因组驱动改变如何通过分子级联传播。监督分类表明，下游层级，特别是蛋白质组和磷酸化蛋白质组，比原始基因组或转录组数据更准确地分类基因组事件。有趣的是，仅反式作用特征就足以进行分类，这表明虽然直接剂量效应在RNA水平上显现，但下游网络响应主导了蛋白质组状态。多组学因子分析（MOFA2）确定了一个连续潜在轴，可独立于R-ISS预测无进展生存期和总生存期。该因子捕获了一个由免疫浸润和NSD2表达调节的gain(1q)/del(13q)轴，整合了所有四种模态的方差。为了促进临床转化，我们使用弹性网络回归推导出稀疏的单模态代理。RNA代理忠实地重现了多组学因子，并在已发表的微阵列和RNAseq队列中独立验证，显示出跨治疗时代的稳健预后效用。这些发现表明，多组学整合揭示了被单组学分析掩盖的隐藏预后轴，而稀疏代理可以弥合复杂发现与临床实施之间的鸿沟。

## Abstract
Multiple myeloma (MM) exhibits profound molecular heterogeneity, yet current risk stratification relies on cytogenetics or single-omics signatures that often fail to capture cross-layer regulatory complexity. We re-analyzed a multi-omics dataset integrating copy-number, transcriptomic, proteomic, and phosphoproteomic data to dissect how common genomic driver alterations propagate through the molecular cascade. Supervised classification demonstrated that downstream layers, particularly the proteome and phosphoproteome, classify genomic events more accurately than primary genomic or transcriptomic data. Intriguingly, trans-acting features alone were sufficient for classification, indicating that while direct dosage effects manifest at the RNA level, downstream network responses dominate the proteomic state. Multi-omics factor analysis (MOFA2) identified a continuous latent axis predicting progression-free and overall survival independent of R-ISS. This factor captured a gain(1q)/del(13q) axis modulated by immune infiltration and NSD2 expression, integrating variance across all four modalities. To enable clinical translation, we derived sparse, single-modality proxies using elastic net regression. An RNA proxy faithfully recapitulated the multi-omic factor and validated independently in published microarray and RNAseq cohorts, demonstrating robust prognostic utility across treatment eras. These findings reveal that multi-omics integration uncovers hidden prognostic axes obscured by single-omics analyses, and that sparse proxies can bridge the gap between complex discovery and clinical implementation.