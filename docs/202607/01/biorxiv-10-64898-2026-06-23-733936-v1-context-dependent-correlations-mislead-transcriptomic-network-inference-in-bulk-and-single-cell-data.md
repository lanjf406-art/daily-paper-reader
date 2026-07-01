---
title: Context-dependent correlations mislead transcriptomic network inference in bulk and single-cell data
title_zh: 背景依赖性相关误导批量与单细胞数据中的转录网络推断
authors: "Asiaee, A., Bombina, P., McGee, R. L., Reed, J., Abrams, Z. B., Abruzzo, L. V., Coombes, K. R."
date: 2026-06-29
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.23.733936v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 转录组网络推断陷阱与肿瘤耐药转录组分析相关
tldr: "转录组网络推断常假设跨样本的Pearson相关系数代表单一生物学意义，但Simpson悖论使得该假设脆弱。本研究系统量化了来自TCGA、GTEx及单细胞数据的数十亿基因对，发现94.8%的miRNA-mRNA对在不同癌症队列中同时存在正负相关，13.3%的高变异汇总相关性符号与多数队列相反。异质性普遍存在（中位I²=0.86），且99.5%对拒绝相关性相等。结果表明单一汇总相关系数可能误导网络推断，建议报告上下文依赖的分布及异质性统计。"
source: biorxiv
selection_source: fresh_fetch
motivation: 系统量化真实转录组数据中因上下文混淆导致的相关性反转发生率。
method: 分析TCGA 31种癌症的8890个肿瘤样本、GTEx多组织数据及单细胞测序数据，使用异质性统计和符号反转诊断。
result: "94.8% miRNA-mRNA对跨队列符号不一致，13.3%汇总相关性反转；单细胞中13-38%对在去除细胞类型均值后反转。"
conclusion: 单一汇总相关系数不可靠，需报告上下文内分布、异质性及均差诊断。
---

## 摘要
背景相关性是共表达模块发现和miRNA靶标推断的主导输入。两者都依赖一个隐含假设：跨异质样本（无论是组织、癌症类型还是细胞类型）汇集的皮尔逊系数估计一个具有生物学意义的量。辛普森悖论原则上使这一假设变得脆弱，因为组间均值偏移可能主导或逆转组内关联。在真实转录组数据中这种情况发生的频率尚未量化。

结果在来自31个癌症队列的8,890个TCGA肿瘤和23,170,038个miRNA-mRNA对中，94.8%的配对同时显示正负的队列内相关性。限制在100万对的高方差区域中，13.3%的|rglobal|≥0.2的整体相关在符号容忍度ε=0.05下相对于队列内多数方向发生逆转。异质性是常态而非例外（中位I2=0.86，IQR 0.80-0.90），99.5%的配对在FDR<0.05下拒绝跨队列等相关性。在可测量的692,770个经实验验证的miRTarBase v10靶标中，仅0.9%跨队列保持一致负相关。该模式在不同模态中重复出现。在GTEx中，21.0%的整体符号与组织多数不一致，23.5%的配对在去除组织均值后符号翻转。在10x PBMC scRNA-seq中，13.1%的基因-基因相关性在去除细胞类型均值后翻转；在CITE-seq中，37.9%的蛋白质-RNA配对在细胞联合WNN分区下翻转。细化背景可减少逆转，但减少程度取决于分区：在BRCA内，5.5%的配对在分子PAM50亚型下逆转，而临床IHC受体状态下降至0.35%；将T细胞细分为转录组定义的亚型使PBMC逆转率从11.8%降至0.13%。

结论单一的汇集相关系数相对于其背景内成分方向发生逆转的比率不可忽略。相关性应随其背景一同报告：背景内分布、异质性统计量以及区分背景间均值偏移与背景内关联的诊断量。我们提供了一个计算这些汇总值的简洁R接口。

## Abstract
BackgroundCorrelation is the dominant input to co-expression module discovery and miRNA-target inference. Both rely on an implicit assumption: a Pearson coefficient pooled across heterogeneous samples, whether tissues, cancer types, or cell types, estimates one biologically meaningful quantity. Simpsons paradox makes this assumption fragile in principle, since between- group mean shifts can dominate or reverse within-group associations. How often this happens in real transcriptomic data has not been quantified.

ResultsAcross 8,890 TCGA tumors from 31 cancer cohorts and 23,170,038 miRNA-mRNA pairs, 94.8% of pairs showed both positive and negative within-cohort correlations. Restricting to the high-variance domain of one million pairs, 13.3% of pooled correlations with |rglobal|[&ge;]0.2 reversed against the within-cohort majority at sign tolerance{varepsilon} = 0.05. Heterogeneity was the rule rather than the exception (median I2 = 0.86, IQR 0.80-0.90), and 99.5% of pairs rejected equal correlation across cohorts at FDR < 0.05. Of 692,770 experimentally validated miRTarBase v10 targets measurable in our data, only 0.9% were uniformly negative across cohorts. The pattern recurred across modalities. In GTEx, 21.0% of pooled signs disagreed with the tissue majority, and 23.5% of pairs flipped sign after tissue-mean removal. In 10x PBMC scRNA-seq, 13.1% of gene-gene correlations flipped after cell-type-mean removal; in CITE-seq, 37.9% of protein-RNA pairs flipped under a joint WNN partition of cells. Refining context reduced reversal, though by how much depended on the partition: within BRCA, 5.5% of pairs reversed under molecular PAM50 subtypes versus 0.35% under clinical IHC receptor status, and refining T cells into transcriptome-defined subtypes cut PBMC reversal from 11.8% to 0.13%.

ConclusionsA single pooled correlation coefficient can invert direction relative to its within-context constituents at rates that are not negligible. Correlations should be reported with their context: the within-context distribution, a heterogeneity statistic, and a diagnostic that separates between-context mean shifts from within-context association. We provide a small R interface that computes these summaries.