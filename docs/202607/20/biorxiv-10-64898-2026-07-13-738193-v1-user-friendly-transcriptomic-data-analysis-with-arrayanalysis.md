---
title: User-friendly transcriptomic data analysis with ArrayAnalysis
title_zh: 利用ArrayAnalysis进行用户友好的转录组数据分析
authors: "Koetsier, J., Cinar, O., Willighagen, E. L., Ammar, A., Karthik, V., Jennen, D., Evelo, C. T., Curfs, L. M. G., Reutelingsperger, C. P., Bahram Sangani, N., Eijssen, L. M. T."
date: 2026-07-18
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.13.738193v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 用户友好的转录组分析工具，支持耐药研究
tldr: 转录组数据分析已成为生物医学研究核心，但非生物信息学专家常面临技术门槛。ArrayAnalysis更新为交互式平台，支持微阵列和RNA-seq数据的预处理、差异表达和基因集分析，通过逐步工作流和动态可视化辅助用户。关键结果包括可定制出版级图表输出、本地部署选项（桌面应用、Docker或R包），既为新手提供指导，也为专家提供高效流程。该平台降低了转录组数据分析门槛，赋能广泛研究者。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1439, \"height\": 709, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1219, \"height\": 1090, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 1864, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1643, \"height\": 1146, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1513, \"height\": 1713, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1655, \"height\": 940, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-13-738193-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1661, \"height\": 934, \"label\": \"Table\"}]"
motivation: 让转录组数据分析更易用，尤其面向缺乏生物信息学经验的研究人员。
method: 开发交互式网络应用，提供逐步工作流和动态可视化，支持微阵列和RNA-seq全流程分析。
result: 支持数据预处理、差异表达和基因集分析，可导出出版级矢量或高分辨率图表，并支持本地部署。
conclusion: ArrayAnalysis使广泛的生物医学研究者能充分利用转录组数据，兼顾易用性与灵活性。
---

## 摘要
转录组分析已成为现代生物医学研究的基石。为了使转录组分析惠及更广泛的科学界，特别是包括生物信息学专业知识有限的研究人员，我们于2013年推出了ArrayAnalysis，这是一个用户友好的基于网络的微阵列数据分析应用程序。现在我们推出了一次重大更新（https://arrayanalysis.org），引入了一个强交互式平台，便于专门探索和分析微阵列及RNA-seq数据，并允许生成可供发表的输出结果。用户可以通过顺序的、交互式的工作流程执行关键分析步骤，包括数据预处理和质量控制、差异表达分析和基因集分析。在每个步骤中，应用程序都提供交互式可视化效果以及信息页面来支持解读。用户可以动态调整图形布局和调色板，并将图形导出为矢量图形和高分辨率光栅图像。对于非专业用户，ArrayAnalysis提供逐步指导以支持正确使用并促进学习，而对于经验丰富的生物信息学家，它则提供了一种简化且灵活的工作流程，非常适合需要高效和一致处理的大规模分析。ArrayAnalysis既可作为网络应用程序使用，也可作为桌面应用程序、Docker镜像或R包进行本地部署，因此适用于不同的计算环境、用户群体和分析目的。总之，ArrayAnalysis使广大生物医学研究人员能够充分挖掘转录组数据的潜力。

## Abstract
Transcriptomic profiling has become a cornerstone of modern biomedical research. To make transcriptomic analyses accessible to a broader scientific community, specifically including researchers with limited bioinformatics expertise, we introduced ArrayAnalysis in 2013 as a user-friendly web-based application for microarray data analysis. We now present a major update (https://arrayanalysis.org), introducing a strongly interactive platform that facilitates the dedicated exploration and analysis of both microarray and RNA-seq data, and allows for the generation of publication-ready outputs. Users can perform key analysis steps, including data pre-processing and quality control, differential expression analysis, and gene set analysis, via a sequential, interactive workflow. At each step, the application provides interactive visualizations accompanied by information pages to support interpretation. Users can dynamically adjust figure layouts and colour palettes and export figures as vector graphics and high-resolution raster images. For non-expert users, ArrayAnalysis offers step-by-step guidance to support correct usage and facilitate learning, while for experienced bioinformaticians, it provides a streamlined and flexible workflow ideal for large-scale analyses requiring efficient and consistent processing. ArrayAnalysis is available both as a web application and for local deployment as a desktop application, Docker image, or R package, making it suitable for diverse computational environments, user groups, and analytical purposes. Together, ArrayAnalysis empowers a broad community of biomedical researchers to unlock the full potential of transcriptomic data.