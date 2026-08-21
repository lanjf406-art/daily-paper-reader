---
title: "An open multimodal spatial resource integrating same-tissue transcriptomics, proteomics, and histology"
title_zh: 整合同一组织转录组学、蛋白质组学和组织学的开放多模态空间资源
authors: "Duchini, E., Tsao, C., Madore, J., Ashhurst, T. M., De Almeida Silva, J., Shin, J.-S., Gupta, R., McCaughan, G., Palendira, U., Liu, K., Ferguson, A., Marsh-Wakefield, F."
date: 2026-08-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.17.742355v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 空间多组学整合方法可用于肿瘤表征
tldr: "空间转录组和蛋白组技术互补，但同组织切片整合困难，且缺乏公开多模态数据。本文提出在福尔马林固定石蜡包埋切片上依次进行Xenium、COMET和H&E染色的流程，并应用于多种人类组织。通过图像配准和细胞分割，生成单细胞转录组-蛋白组整合数据，公开四个对齐组织核心及工具UnumLocalia，为多模态空间生物学提供可复用资源。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有空间多模态整合流程技术难度大，且缺乏适合计算方法开发的公开多模态数据集。
method: "在相同FFPE组织切片上依次执行Xenium空间转录组、COMET循环免疫荧光和H&E染色，配准后应用Xenium分割生成单细胞多模态数据。"
result: 成功在扁桃体、肝细胞腺瘤及肝癌配对组织中验证，公开对齐图像、分割和整合单细胞数据，并发布交互式可视化工具UnumLocalia。
conclusion: 该协议、软件和数据集为多模态空间分析提供标准化资源，促进生物发现和计算方法开发。
---

## 摘要
空间转录组学和蛋白质组学技术为组织组织、细胞表型和功能提供互补的见解，但在同一组织切片上整合这些模态在技术上仍具挑战性。顺序工作流必须保持RNA完整性、抗原性和组织形态，同时保持准确的空间配准。目前，适合计算方法开发的公开多模态数据集仍然有限。在此，我们提出了一种在同一福尔马林固定石蜡包埋组织切片上进行顺序10x Genomics Xenium空间转录组学、COMET循环免疫荧光和苏木精-伊红（H&E）组织学染色的工作流。我们在多种生物学上不同的人类组织中展示了该方法，包括扁桃体、肝细胞腺瘤以及匹配的肿瘤和非肿瘤肝细胞癌，说明了该工作流在单一组织类型之外的广泛适用性。在图像配准后，Xenium衍生的细胞分割被应用于蛋白质图像，以生成用于下游分析的整合单细胞转录组和蛋白质组测量。为促进社区复用，我们公开发布了四个代表性的配准组织芯，连同转录本坐标、多重蛋白质图像、H&E图像、细胞分割和整合的单细胞数据集。我们还引入了UnumLocalia，一个开源的视觉化和数据提取工具，能够交互式探索配准的多模态图像，支持用户定义的细胞分割，并允许导出整合的单细胞数据用于下游分析。总之，这份技术方案、工作流、软件和公开可用的数据集为多模态空间生物学提供了可复用的资源，支持生物学发现、计算方法开发、多模态数据整合以及新兴分析方法在互补空间技术中的验证。

## Abstract
Spatial transcriptomic and proteomic technologies provide complementary insights into tissue organisation, cellular phenotype and function, yet integrating these modalities on the same tissue section remains technically challenging. Sequential workflows must preserve RNA integrity, antigenicity and tissue morphology while maintaining accurate spatial registration. At present, publicly available multimodal datasets suitable for computational method development remain limited. Here, we present a workflow for sequential 10x Genomics Xenium spatial transcriptomics, COMET cyclic immunofluorescence, and haematoxylin and eosin (H&E) histological staining on the same formalin-fixed paraffin-embedded tissue section. We demonstrate this approach across multiple biologically distinct human tissues, including tonsil, hepatocellular adenoma, and matched tumour and non-tumour hepatocellular carcinoma, illustrating the widespread applicability of the workflow beyond a single tissue type. Following image registration, Xenium-derived cell segmentations were applied to protein images to generate integrated single-cell transcriptomic and proteomic measurements for downstream analyses. To facilitate community reuse, we publicly release four representative aligned tissue cores together with transcript coordinates, multiplex protein images, H&E images, cell segmentations, and integrated single-cell datasets. We additionally introduce UnumLocalia, an open-source visualisation and data extraction tool that enables interactive exploration of aligned multimodal images, supports user-defined cell segmentation, and allows export of integrated single-cell data for downstream analyses. Together, this technical protocol, workflow, software, and openly available dataset provide a reusable resource for multimodal spatial biology, supporting advances in biological discovery, computational method development, multimodal data integration, and validation of emerging analytical approaches across complementary spatial technologies.