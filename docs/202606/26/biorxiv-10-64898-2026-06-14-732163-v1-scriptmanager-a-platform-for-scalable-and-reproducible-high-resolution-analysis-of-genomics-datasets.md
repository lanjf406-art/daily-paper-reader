---
title: "ScriptManager: a platform for scalable and reproducible high-resolution analysis of genomics datasets"
title_zh: ScriptManager：一个用于基因组数据集可扩展和可重复高分辨率分析的平台
authors: "Lang, O. W., Beer, B., Zhang, D., LeSon, C., Deen, A., Pugh, F., Lai, W. K."
date: 2026-06-18
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.14.732163v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 可扩展基因组学分析平台
tldr: 现有基因组学分析工具多针对特定检测类型，互操作性和可重复性不足。ScriptManager v1.0是基于Java的模块化框架，统一跨检测分析流程，支持GUI会话记录、自动化测试和容器化部署。其TagPileup分析可从本地单核扩展至OSG上10305个任务并行执行，总耗时不足2小时。该平台增强了高分辨率基因组分析的可移植性和可重复性，连接探索性分析与出版级图形生成。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有工具缺乏跨检测类型的统一框架，限制了互操作性和可重复性。
method: ScriptManager采用模块化设计，集成GUI日志、自动化测试、Singularity容器、Anaconda包和Galaxy包装。
result: TagPileup分析在Open Science Grid上完成10305个并行任务，总耗时<2小时。
conclusion: ScriptManager支持多样化基因组分析，提升工作流可移植性和可重复性。
---

## 摘要
背景：基因组和表观基因组检测方法的日益多样化驱动了数据格式、分析工作流程和图表生成工具的并行增长。然而，用于分析数据和组装出版质量图表的工具通常针对特定检测方法，极大地限制了它们的互操作性和可重复性。

结果：我们发布了ScriptManager v1.0版本，这是一个基于Java的框架，用于基因组和表观基因组数据的模块化、可重复分析和可视化工作流程。与针对单个检测方法的现有工具不同，ScriptManager提供了一个统一且可扩展的框架，用于跨检测方法可视化和工作流程可重复性。v1.0版本新增了分析模块、GUI会话记录、自动单元和集成测试、教程以及扩展文档。它还通过Singularity容器、Anaconda打包和Galaxy XML包装器与更广泛的可重复性生态系统集成。我们展示了ScriptManager的TagPileup从本地单核执行扩展到分布在开放科学网格（OSG）上的10,305个作业分析，整个工作负载在不到2小时的时钟时间内完成。

结论：ScriptManager v1.0增强了跨多种高分辨率基因组检测的工作流程可移植性、透明性和可重复性。通过将灵活的模块设计与现代可重复性标准相结合，ScriptManager为探索性数据分析和正式的、可发表的图表生成之间搭建了桥梁。这些改进使研究人员能够在各种计算基础设施上以最少的配置构建、共享和重复基因组分析。

## Abstract
BackgroundThe growing diversity of genomic and epigenomic assays has driven a parallel expansion in data formats, analysis workflows, and figure-generation tools. However, tools for analyzing data and assembling publication-quality figures are often specialized to a specific assay, dramatically limiting their interoperability and reproducibility.

ResultsWe present the v1.0 release of ScriptManager, a Java-based framework for modular and reproducible analysis and visualization workflows of genomics and epigenomics data. Unlike existing tools specialized for individual assay types, ScriptManager provides a unified and extensible framework for cross-assay visualization and workflow reproducibility. The v1.0 release adds novel analytical modules, GUI session logging, automated unit and integration testing, tutorials, and expanded documentation. It also integrates with the broader reproducibility ecosystem through Singularity containers, Anaconda packaging, and Galaxy XML wrappers. We demonstrate ScriptManagers TagPileup scaling from local single-core execution to a 10,305-job analysis distributed across the Open Science Grid (OSG), with the full workload completing in <2 hours of wall-clock time.

ConclusionsScriptManager v1.0 enhances workflow portability, transparency, and reproducibility across a diverse range of high-resolution genomic assays. By coupling a flexible module design with modern reproducibility standards, ScriptManager provides a bridge between exploratory data analysis and formal, publication-ready figure generation. These improvements enable researchers to build, share, and reproduce genomic analyses across diverse computational infrastructures with minimal configuration.