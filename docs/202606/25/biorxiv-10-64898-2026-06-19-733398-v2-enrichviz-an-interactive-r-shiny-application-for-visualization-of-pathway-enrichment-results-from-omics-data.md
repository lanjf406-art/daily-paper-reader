---
title: "EnrichViz: An Interactive R Shiny Application for Visualization of Pathway Enrichment Results from Omics Data"
title_zh: EnrichViz：用于组学数据通路富集结果可视化的交互式R Shiny应用程序
authors: "Garcia-Milian, R."
date: 2026-06-24
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.19.733398v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 组学通路富集可视化的生信工具
tldr: 通路富集分析是组学数据解读的核心，但结果表格难以直接生成出版级可视化，尤其是对非计算背景研究者。EnrichViz是一个基于R Shiny的交互式应用，接受归一化丰度矩阵、样本注释和富集结果CSV文件，自动检测p值格式，生成条形图、气泡图、弦图、热图、箱线图/小提琴图等六种可调整图形。用户可通过侧边栏实时修改参数，最终以300 dpi PNG导出，无需任何编程技能。该工具免费在线可用，显著降低了可视化门槛，加速了生物学发现。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有富集分析工具输出表格难以直接生成出版级可视化，需要编程技能，阻碍非计算研究者快速获取直观结果。
method: 基于R Shiny框架，接收三个CSV文件，利用ggplot2、pheatmap、circlize等包自动生成六种可视化，支持实时参数调整和p值格式自动检测。
result: 生成条形图、气泡图、弦图、热图、箱线图/小提琴图，所有图形可导出为300 dpi PNG，参数实时可调。
conclusion: EnrichViz提供免代码交互式可视化，简化通路富集结果图表制作，免费开源，增强可重复性和研究效率。
---

## 摘要
通路和功能富集分析是组学数据解释的基石，使研究人员能够将差异表达的蛋白质或基因映射到精选的生物过程、信号级联和分子功能上。虽然诸如Ingenuity Pathway Analysis (IPA)、g:Profiler和Enrichr等工具被广泛用于生成排序的富集结果，但将这些表格输出转换为清晰、可发表的图形仍然是一个耗时的步骤，通常需要自定义脚本并熟悉可视化库，这对没有计算背景的研究人员来说是一个重大障碍。在此，我们提出EnrichViz，一个自包含的、基于浏览器的R Shiny应用程序，能够实现定量蛋白质组学、转录组学和代谢组学实验中通路和功能富集结果的交互式、无需编程的可视化。EnrichViz接受三个标准CSV文件作为输入：归一化丰度矩阵、样本注释或元数据文件，以及来自任何导出表格结果的平台的富集结果，并生成六种互补的、可发表的图形：用于按显著性排序富集项的条形图和气泡图、用于探索通路-分子连接性的弦图、用于显示跨实验组Z-score归一化表达模式的聚类热图，以及用于检查单个蛋白质、基因或代谢物丰度分布的箱线图或小提琴图。该应用程序支持通过自动检测处理原始p值和预转换的-log10(p)值，所有图形参数均可通过图形侧边栏实时调整。每张图可以300 dpi的分辨率导出为高分辨率PNG文件。EnrichViz使用R语言中的Shiny、ggplot2、pheatmap和circlize包实现，并可免费从https://rgmilian.shinyapps.io/EnrichViz/获取。

## Abstract
Pathway and functional enrichment analysis is a cornerstone of omics data interpretation, enabling researchers to map differentially expressed proteins or genes onto curated biological processes, signaling cascades, and molecular functions. While tools such as Ingenuity Pathway Analysis (IPA), g:Profiler, and Enrichr are widely used to generate ranked enrichment results, translating these tabular outputs into clear, publication-ready figures remains a time-consuming step that typically requires custom scripting and familiarity with visualization libraries, a significant barrier for researchers without a computational background. Here we present EnrichViz, a self-contained, browser-based R Shiny application that enables interactive, code-free visualization of pathway and functional enrichment results from quantitative proteomics, transcriptomics, and metabolomics experiments. EnrichViz accepts three standard CSV files as input, a normalized abundance matrix, a sample annotation or metadata file, and enrichment results from any platform that exports tabular output, and produces six complementary, publication-ready visualizations: bar and bubble plots for ranking enriched terms by significance, chord diagrams for exploring pathway-molecule connectivity, clustered heatmaps for displaying Z-score normalized expression patterns across experimental groups, and boxplots or violin plots for examining the abundance distribution of individual proteins, genes, or metabolites. The application supports both raw p-values and pre-transformed -log10(p) values through automatic detection, and all plot parameters are adjustable in real time through a graphical sidebar. Every figure can be exported as a high-resolution PNG file at 300 dpi. EnrichViz is implemented in R using the Shiny, ggplot2, pheatmap, and circlize packages, and is freely available at https://rgmilian.shinyapps.io/EnrichViz/