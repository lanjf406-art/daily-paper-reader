---
title: AI-enabled reconstruction of 3D spatial multi-omics at single-cell resolution
title_zh: 基于AI的单细胞分辨率三维空间多组学重建
authors: "Wang, Z., Yan, Y., Yang, X., Zhang, D., Han, C., Zou, Q., Du, Y., Hu, Z., Yuan, Z."
date: 2026-07-14
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.09.737490v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: AI驱动的3D空间多组学方法，可用于肿瘤耐药多组学表征
tldr: "三维空间多组学提供独特生物学洞察，但技术存在瓶颈。Histo3D-MO集成了稀疏空间组学测量与H&E染色图像，通过SPONGE模型实现从组织学图像预测多组学，并结合细胞类型传播与组织域注释算法，构建单细胞分辨率的三维图谱。验证表明SPONGE显著优于现有预测方法。应用于肝细胞癌，揭示了翻译效率的空间组织、恶性细胞与单核细胞的空间解耦及深度依赖性分化轨迹。Histo3D-MO为复杂组织三维空间多组学研究提供了可扩展的通用框架。"
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737490-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 2109, \"height\": 2642, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-09-737490-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 2143, \"height\": 1432, \"label\": \"Figure\"}]"
motivation: 现有技术难以实现单细胞分辨率的3D空间多组学重建，亟需可扩展的混合实验计算方法。
method: "提出Histo3D-MO流程，整合稀疏空间组学与H&E组织学，利用SPONGE预测多组学，结合3D细胞类型传播和组织域注释算法。"
result: SPONGE优于现有预测方法；在肝细胞癌中揭示翻译效率空间差异、恶性细胞与单核细胞解耦及深度分化轨迹。
conclusion: 建立了单细胞分辨率3D空间多组学重建的可扩展框架，为复杂组织微环境研究提供新工具。
---

## 摘要
三维空间多组学为生物活动提供了无与伦比的见解，但在技术上仍然难以实现。在此，我们介绍Histo3D-MO，一种混合实验-计算管道，用于重建单细胞分辨率的3D空间多组学图谱。值得注意的是，Histo3D-MO通过基于H&E图像的空间多组学（SPONGE）将稀疏的、组学不重叠的空间测量与密集的苏木精和伊红（H&E）组织学相结合，实现了跨多个组学层的细胞级3D映射。使用保留切片进行验证，SPONGE显著优于现有的组学预测方法。我们进一步开发了一套用于3D细胞类型传播和组织域注释的算法套件，实现了肿瘤微环境的全容积表征。应用于内部肝细胞癌数据，Histo3D-MO揭示了翻译效率的空间组织模式、恶性细胞与单核细胞之间的体积解耦以及深度相关的单核细胞分化轨迹。总之，这些结果确立了Histo3D-MO作为一个可扩展的框架，用于重建单细胞分辨率的3D空间多组学，并探究复杂生物系统中的组织组织。

## Abstract
Three-dimensional (3D) spatial multi-omics provides unparalleled insights into biological activities, yet remains technically prohibitive. Here, we introduce Histo3D-MO, a hybrid experimental-computational pipeline for reconstructing single-cell-resolution 3D spatial multi-omics maps. Notably, Histo3D-MO integrates sparse, omics-disjoint spatial measurements with dense Hematoxylin and Eosin (H&E) histology through SPatial multi-Omics from h&E imaGEs (SPONGE), achieving cell-level 3D mapping across multiple omics layers. Validated using held-out slices, SPONGE substantially outperforms existing omics prediction methods. We further developed an algorithmic suite for 3D cell-type propagation and tissue-domain annotation, enabling whole-volume characterization of the tumor microenvironment. Applied to the in-house hepatocellular carcinoma data, Histo3D-MO revealed spatially organized patterns of translation efficiency, volumetric decoupling between malignant cells and monocytes, and depth-associated monocyte differentiation trajectories. Together, these results establish Histo3D-MO as a scalable framework for reconstructing single-cell-resolution 3D spatial multi-omics and interrogating tissue organization across complex biological systems.