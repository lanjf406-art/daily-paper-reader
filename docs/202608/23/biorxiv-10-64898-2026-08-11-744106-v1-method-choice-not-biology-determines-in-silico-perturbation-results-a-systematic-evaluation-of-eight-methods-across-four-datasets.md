---
title: "Method Choice, Not Biology, Determines In Silico Perturbation Results: A Systematic Evaluation of Eight Methods Across Four Datasets"
title_zh: 方法选择，而非生物学特性，决定计算扰动结果：对四种数据集上八种方法的系统评估
authors: "Wenjie, G., Wu, S., Hu, G., Yang, Z., Wang, Z., Cai, J., Mao, J."
date: 2026-08-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.11.744106v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 系统评估八种单细胞转录组扰动预测方法，与机器学习药物耐药预测直接相关。
tldr: "大多数单细胞计算机扰动方法仅经单数据集验证，可靠性与泛化性未知。本文系统基准八种方法、四个数据集，发现仅CellOracle与DDIM稳定检出TF-糖酵解方向性调控；VAE、张量分解等六种方法均产生不可检测信号，并存在潜空间竞争、相关噪声、图非特异性等失败模式。方法选择可显著逆转结论（DDIM与scTenifoldKnk排名负相关），且预测方向与CRISPRi实验仅40.9%一致。研究提供跨通路验证、方向感知基准及≥500细胞、≥1000高变基因的最小数据要求，为扰动方法选择提供初步指南。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有in silico扰动方法缺乏跨数据集系统验证，可靠性与泛化能力未知，导致应用时难以选择合适方法。
method: 对八种扰动方法（涵盖六种数学框架）在四个数据集上系统交叉基准，采用VAE潜空间剖析、相关分布比较、基因-基因图诊断，并以CRISPRi Perturb-seq实验验证预测方向。
result: "仅CellOracle和DDIM稳定检测到TF-通路信号；六种方法失效并存在不同失败模式。方法选择可逆转结论（排名负相关ρ=-0.811），CellOracle预测方向与实验仅40.9%一致。"
conclusion: 性能差异由多因素造成，建议采用跨通路验证和方向感知基准，并满足最小数据量（≥500细胞、≥1000高变基因）以提升扰动分析可靠性。
---

## 摘要
大多数单细胞转录组学的计算扰动方法仅在单一数据集上得到验证，因此其可靠性和泛化能力未知。通过对四种数据集上涵盖六种数学框架的八种方法进行系统的跨方法、跨数据集基准测试，我们发现八种方法中有六种（包括广泛使用的基于VAE和张量分解的方法）未能产生可检测的转录因子(TF)到通路的信号。只有CellOracle和DDIM一致地检测到了TF到糖酵解的方向性调控。在PBMC单核细胞中的跨通路分析揭示了除糖酵解之外生物学上一致的TF-通路关联（SPI1[->]糖酵解富集4.4倍，FOS[->]AP-1靶标富集4.4倍），其中SOX9作为生物学特异性对照（无通路富集）。仅方法选择就可能逆转生物学结论：DDIM和scTenifoldKnk的排名显著负相关（rho=-0.811, p=0.027）。在K562细胞中的CRISPRi Pert-seq验证证实TF敲低抑制糖酵解基因表达（JUN delta=-1.72, CEBPB delta=-1.59, SPI1 delta=-1.57, FOS delta=-0.70），但CellOracle预测的扰动方向与实验方向不匹配（一致性40.9%，与随机无异），揭示了稳态相关与因果扰动之间的根本差距。使用VAE潜在空间分析、相关性分布比较和基因-基因图分析的诊断性分析识别了不成功方法的不同失败模式：VAE潜在空间竞争（STAT3信噪比0.44 vs. SPI1 4.25）、相关性噪声（TF-糖酵解|r|=0.038与背景|r|=0.047无法区分）和图非特异性（富集0.84倍）。一项受控消融实验表明，在DDIM中添加GRN先验并未改善靶标召回率（所有TF的delta=0），证实性能差异是多因素的。这些发现为方法选择提供了初步指导，包括跨通路验证、方向感知基准测试以及最低数据要求（>=500个细胞，>=1,000个HVG）。

## Abstract
Most in silico perturbation methods for single-cell transcriptomics have been validated only on individual datasets, leaving their reliability and generalizability unknown. Through systematic cross-method, cross-dataset benchmarking of eight methods spanning six mathematical frameworks across four datasets, we find that six of eight methods--including widely used VAE-based and tensor decomposition approaches--fail to produce detectable transcription factor (TF)-to-pathway signals. Only CellOracle and DDIM consistently detected TF-to-glycolysis directional regulation. Cross-pathway analysis in PBMC monocytes revealed biologically coherent TF-pathway associations beyond glycolysis (SPI1[-&gt;]glycolysis 4.4x enrichment, FOS[-&gt;]AP-1 targets 4.4x), with SOX9 serving as a biological specificity control (no pathway enrichment). Method choice alone could reverse biological conclusions: DDIM and scTenifoldKnk rankings were significantly anti-correlated ({rho}=-0.811, p=0.027). CRISPRi Perturb-seq validation in K562 cells confirmed TF knockdown suppresses glycolysis gene expression (JUN {delta}=-1.72, CEBPB {delta}=-1.59, SPI1 {delta}=-1.57, FOS {delta}=-0.70), but CellOracle-predicted perturbation directions did not match experimental directions (40.9% agreement, not different from chance), revealing a fundamental gap between steady-state correlation and causal perturbation. Diagnostic analyses using VAE latent space profiling, correlation distribution comparison, and gene-gene graph analysis identified distinct failure modes in unsuccessful methods: VAE latent space competition (STAT3 signal-to-noise 0.44 vs. SPI1 4.25), correlation noise (TF-glycolysis |r|=0.038 indistinguishable from background |r|=0.047), and graph non-specificity (0.84x enrichment). A controlled ablation experiment showed that adding a GRN prior to DDIM did not improve target recall (delta=0 for all TFs), confirming that performance differences are multi-factorial. These findings establish preliminary guidance for method selection, including cross-pathway validation, direction-aware benchmarking, and minimum data requirements ([&ge;]500 cells, [&ge;]1,000 HVGs).