---
title: Systematic benchmarking of multi-modal approaches for tumor-naive ctDNA detection and quantification
title_zh: 无肿瘤先验信息的ctDNA检测与定量多模态方法的系统基准测试
authors: "Qi, T., Odinokov, D., Lakshmanan, L. N., Grachet, N. G., Lou, M., Saelee, S., Garcia-Montoya, G., Mun, W. P., Rahman, R. C., Asgharian, H., Yi, A. T. X., Pyone, N. H. Y., Wang, L. Y., Tan, G. T., Carrie, H., Lim, A., Ting, L. Y., Hsia, A. G. H., Yean, P. P. S., Ngo, S., Snyder, J., Kaur, H., Tan, A., Yap, Y. S., Tan, D. S., Tan, I. B. H., Penkler, J.-A., Utiramerur, S., Kumar, D., Skanderup, A. J."
date: 2026-06-24
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.19.733293v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 多模态ctDNA检测方法基准测试，可用于肿瘤耐药监测
tldr: "循环肿瘤DNA（ctDNA）纵向监测可表征癌症治疗反应，但肿瘤未知的ctDNA检测方法（如全基因组测序WGS和DNA甲基化谱）的系统比较尚缺。本研究对150例结直肠癌、肺癌和乳腺癌患者血浆进行高深度WGS和EM-seq，生成40,000个计算机模拟样本，在0.1x-30x测序深度下评估检测准确性、检测限（LoD）和定量限（LoQ）。结果发现多模态集成方法在特定条件下比单一模态提升检测和量化性能，且性能受癌症类型和测序深度影响。该基准确立了关键性能权衡，为ctDNA生物标志物研究提供了方法选择和开发的实用框架。"
source: biorxiv
selection_source: fresh_fetch
motivation: 肿瘤未知的ctDNA定量方法（WGS和甲基化）的比较性能和互补整合潜力尚未系统评估。
method: "对150例癌症患者血浆进行高深度WGS和EM-seq，生成40,000个计算机样本，系统评估不同测序深度下的LoD和LoQ。"
result: 多模态集成方法在特定条件下提升检测和量化性能，性能受癌症类型和测序深度影响。
conclusion: 该基准为基于ctDNA的生物标志物研究提供了方法选择和开发的实用框架，明确了关键性能权衡。
---

## 摘要
长期监测循环肿瘤DNA已成为表征癌症治疗反应动态的有前景框架。用于定量ctDNA的可扩展的无肿瘤先验信息方法通常涉及全基因组测序或DNA甲基化分析，但它们的比较性能和互补整合的能力仍知之甚少。在这里，我们使用来自150名结直肠癌、肺癌和乳腺癌患者的血浆，系统地基准测试了基于无肿瘤先验信息的全基因组测序和甲基化的ctDNA定量方法。利用配对的高深度WGS和EM-seq数据，我们生成了40,000个计算机模拟样本，并评估了检测准确性、检测限和定量限，涵盖癌症类型和测序深度（0.1倍到30倍）。我们进一步评估了单模态和多模态方法组合，确定了整合方法相对于单一模态在检测和定量方面提升分析性能的条件。该基准测试描绘了关键性能权衡，并提供了一个实用框架，以支持方法开发并指导基于ctDNA的生物标志物研究的未来应用。

## Abstract
Longitudinal monitoring of circulating tumor DNA (ctDNA) has emerged as a promising framework for characterizing treatment response dynamics in cancer. Scalable tumor-naive approaches for quantifying ctDNA often involve whole-genome sequencing (WGS) or DNA methylation profiling, but their comparative performance and capacity for complementary integration remain poorly understood. Here we systematically benchmarked tumor-naive WGS- and methylation-based ctDNA quantification methods using plasma from 150 patients with colorectal, lung and breast cancer. Using paired high-depth WGS and EM-seq data, we generated 40,000 in silico samples and evaluated detection accuracy, limits of detection (LoD) and quantification (LoQ) across cancer types and sequencing depths (0.1x-30x). We further assessed single- and multimodal method combinations, identifying conditions under which integrated approaches enhance analytical performance for detection and quantification relative to single modalities. This benchmark delineates key performance trade-offs and provides a practical framework to support method development and guide future research applications in ctDNA-based biomarker studies.