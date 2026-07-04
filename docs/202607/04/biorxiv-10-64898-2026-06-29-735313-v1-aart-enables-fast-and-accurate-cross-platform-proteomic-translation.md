---
title: AART enables fast and accurate cross-platform proteomic translation
title_zh: AART实现快速准确的跨平台蛋白质组翻译
authors: "chen, y., Zhang, S."
date: 2026-07-03
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.29.735313v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 跨平台蛋白质组翻译方法，可用于耐药生物标志物整合
tldr: "血浆蛋白质组学面临跨平台数据一致性问题，影响可重复性。AART框架整合匹配蛋白质岭回归与残差学习，实现快速准确翻译。在三大平台六种翻译方向中，AART性能相对提升92%，比最强基线cpiVAE高31.6%。下游分析中，2型糖尿病和阿尔茨海默病的关联可重复性分别提升75.5%和370.6%，ALS诊断准确率提升92.6%。AART速度快1-3个数量级，支持大规模应用，促进可重复、可迁移的蛋白质组学研究。"
source: biorxiv
selection_source: fresh_fetch
motivation: 跨平台蛋白质组数据一致性低，严重限制研究可重复性和模型转移性。
method: 提出AART框架，整合匹配蛋白质岭回归与残差学习进行跨平台翻译。
result: "在三大平台六种翻译方向中，AART翻译性能相对提升92%，下游疾病分析可重复性提高75%-370%。"
conclusion: AART是快速准确的跨平台蛋白质组翻译框架，速度快1-3个量级，促进可重复、可迁移研究。
---

## 摘要
血浆蛋白质组分析已被广泛用于生物标志物发现、疾病预测和诊断以及患者分层。然而，不同检测平台之间的技术差异通常导致低至中等的一致性，限制了研究的可重复性、数据整合和模型可迁移性。本文提出了AART，一个跨平台蛋白质组翻译框架，它整合了匹配蛋白岭回归与全蛋白质组残差学习。我们使用三个主要平台（包括Olink、SomaScan和质谱）对三个独立队列进行了AART基准测试。在所有六个翻译方向上，AART在重叠和非重叠蛋白质翻译中均取得了优于基线方法的性能，相比直接映射平均相对提升92.0%，相比最强基线cpiVAE提升高达31.6%。AART准确翻译并改善的蛋白质富集于细胞外、囊泡相关和组织限制的血浆生物学功能。在下游应用中，与直接跨平台比较相比，AART将2型糖尿病蛋白质组关联分析的可重复性提升了75.5%，阿尔茨海默病提升了370.6%。与未整合分析相比，AART支持的队列整合将肌萎缩侧索硬化的诊断准确率提升了92.6%。总体而言，AART比cpiVAE快一到三个数量级，便于生物样本库规模的应用。这些结果共同确立了AART作为一个快速、准确且可扩展的跨平台蛋白质组翻译框架，推动了更具可重复性、可迁移性和整合性的蛋白质组研究。

## Abstract
Plasma proteomic profiling has been widely used for biomarker discovery, disease prediction and diagnosis, and patient stratification. However, technical differences across assay platforms often result in low-to-moderate agreement, limiting study reproducibility, data integration, and model transferability. Here we present AART, a cross-platform proteomic translation framework that integrates matched-protein ridge regression with proteome-wide residual learning. We benchmarked AART spanning three independent cohorts profiled using three major platforms, including Olink, SomaScan, and mass spectrometry. Across all six translation directions, AART achieved the best performance compared with baseline methods for both overlapping and non-overlapping protein translations, with a relative improvement of 92.0% on average over direct mapping and by up to 31.6% over cpiVAE, the strongest baseline. Proteins that were accurately translated and improved by AART were enriched for extracellular, vesicle-associated, and tissue-restricted plasma biology. In downstream applications, AART improved the reproducibility of proteomic association analyses relative to direct cross-platform comparison by 75.5% for type 2 diabetes and 370.6% for Alzheimer's disease. AART-enabled cohort integration enhanced diagnostic accuracy for amyotrophic lateral sclerosis by 92.6% compared with non-integration analysis. AART was overall one to three orders of magnitude faster than cpiVAE, facilitating biobank-scale applications. Together, these results establish AART as a fast, accurate, and scalable framework for cross-platform proteomic translation, enabling more reproducible, transferable, and integrated proteomic research.