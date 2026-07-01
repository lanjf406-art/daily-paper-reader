---
title: Genetically informed single-cell and spatial mapping of metabolic programs in human health and disease
title_zh: 基于遗传信息的单细胞和空间映射揭示人类健康与疾病中的代谢程序
authors: "Xu, H., Huang, G., Zhang, L., Liu, W., Wu, Q., Chen, M., Zhao, D., Zhang, Y., Xu, A."
date: 2026-06-29
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.25.734643v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 整合GWAS与单细胞/空间转录组的多组学代谢图谱，可用于耐药研究
tldr: 现有转录组代谢模型无法直接评估单个代谢物与细胞状态关联，尤其是外源信号分子。本文提出gmMAP框架，整合代谢物GWAS统计与单细胞和空间转录组，结合约束代谢通量模型，实现细胞和空间分辨率的代谢程序映射。在人类肾脏发育中验证准确性，重建17小鼠器官及24人体组织的空间代谢图谱，揭示29泛癌代谢重编程及结肠炎基质代谢重塑。gmMAP连接遗传代谢特征与细胞状态、组织空间及疾病病理，提供多尺度代谢图谱。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法无法直接评估单个代谢物（尤其是外源信号分子）与细胞状态的关联。
method: gmMAP整合代谢物GWAS统计与单细胞/空间转录组，结合约束代谢通量模型，预测内源代谢过程和外源代谢物关联。
result: 在肾脏发育、17小鼠器官、24人体组织、29泛癌及结肠炎中验证，重建空间代谢分布并揭示代谢重编程。
conclusion: gmMAP统一连接遗传代谢特征与细胞状态、组织空间及疾病病理，提供多尺度代谢图谱。
---

## 摘要
定义细胞类型特异的内源性代谢特征、细胞水平代谢状态的空间分布以及细胞对外源代谢物的反应，对于理解疾病机制至关重要。现有的基于转录组的代谢模型主要推断细胞内反应或通路水平活性，因此无法直接评估单个代谢物水平与细胞状态之间的关联，特别是对于那些作为信号分子在细胞外作用而非作为代谢底物进入细胞的代谢物。在此，我们介绍了gmMAP，这是一个将代谢物GWAS汇总统计与单细胞和空间转录组整合，以细胞和空间分辨率绘制代谢程序的框架。值得注意的是，gmMAP能够预测内源性代谢过程的激活，同时揭示外源代谢物与多种细胞功能状态之间的内在关联。为了进一步捕捉细胞代谢网络的连通性，我们纳入了一个基于约束的代谢通量模型来评估全局代谢活性。为了评估gmMAP的准确性和稳健性，我们将其应用于涵盖人类发育、生理稳态、炎症和癌症的代表性生物学背景中。在人类肾脏发育中，gmMAP捕捉了动态代谢程序，并通过配对转录组和代谢组参考数据集进行了验证，支持其在代谢物识别和代谢流推断中的可靠性。在器官水平上，gmMAP重建了稳态和自身免疫炎症条件下17个小鼠器官的空间代谢物分布模式，并进一步扩展到24种正常人类组织，生成多尺度的器官和细胞分辨率代谢图谱。在疾病背景下，gmMAP揭示了29种泛癌种细胞群中的代谢重编程，并识别了溃疡性结肠炎中外源代谢物与炎症相关基质代谢重塑之间的潜在联系。总之，gmMAP能够一致地将遗传信息相关的代谢物特征与细胞状态、空间组织结构和疾病病理联系起来。

## Abstract
Defining cell-type-specific endogenous metabolic features, the spatial distribution of cell-level metabolic states and cellular responses to exogenous metabolites is essential for understanding disease mechanisms. Existing transcriptome-based metabolic models primarily infer intracellular reaction or pathway-level activities, and therefore cannot directly assess associations between individual metabolite levels and cellular states, particularly for metabolites that act extracellularly as signalling molecules rather than entering cells as metabolic substrates. Here we introduce gmMAP, a framework that integrates metabolite GWAS summary statistics with single-cell and spatial transcriptomes to map metabolic programmes at cellular and spatial resolution. Notably, gmMAP enables the prediction of endogenous metabolic process activation while also revealing intrinsic associations between exogenous metabolites and diverse cellular functional states. To further capture the connectivity of cellular metabolic networks, we incorporated a constraint-based metabolic flux model to evaluate global metabolic activity. To evaluate the accuracy and robustness of gmMAP, we applied the framework across representative biological contexts spanning human development, physiological homeostasis, inflammation and cancer. In human kidney development, gmMAP captured dynamic metabolic programmes and was validated using paired transcriptomic and metabolomic reference datasets, supporting its reliability in metabolite identification and metabolic-flow inference. At the organ level, gmMAP reconstructed spatial metabolite distribution patterns across 17 mouse organs under homeostatic and autoimmune inflammatory conditions, and further extension to 24 normal human tissues generated a multi-scale metabolic atlas at both organ and cellular resolutions. In disease settings, gmMAP revealed metabolic reprogramming across 29 pan-cancer cell populations and identified potential links between exogenous metabolites and inflammation-associated stromal metabolic remodelling in ulcerative colitis. Together, gmMAP can consistently connect genetically informed metabolite traits with cell states, spatial tissue organization and disease pathology.