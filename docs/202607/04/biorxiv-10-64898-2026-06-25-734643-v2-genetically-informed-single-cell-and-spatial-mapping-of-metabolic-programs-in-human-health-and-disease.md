---
title: Genetically informed single-cell and spatial mapping of metabolic programs in human health and disease
title_zh: 基于遗传信息的单细胞与空间映射揭示人类健康与疾病中的代谢程序
authors: "Xu, H., Huang, G., Zhang, L., Liu, W., Wu, Q., Chen, M., Zhao, D., Zhang, Y., Xu, A."
date: 2026-06-30
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.25.734643v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞和空间代谢图谱方法，可应用于肿瘤耐药机制研究
tldr: 现有转录组代谢模型难以直接关联代谢物与细胞状态，尤其外源性信号代谢物。为此，提出gmMAP框架，整合代谢物GWAS与单细胞/空间转录组，结合约束代谢通量模型。在发育、免疫、癌症等场景验证，重建多器官代谢图谱，发现代谢重编程及与炎症的关联。实现了遗传信息指导的代谢特征与细胞状态、空间组织、病理的映射。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法无法直接评估代谢物水平与细胞状态关联，尤其外源性信号代谢物。
method: 提出gmMAP，整合代谢物GWAS与单细胞/空间转录组，结合约束代谢通量模型。
result: 在肾发育、小鼠器官、人类组织、癌症和溃疡性结肠炎中验证，重建多尺度代谢图谱。
conclusion: gmMAP可连接遗传代谢特征与细胞状态、空间组织和病理。
---

## 摘要
定义细胞类型特异性的内源性代谢特征、细胞水平代谢状态的空间分布以及细胞对外源代谢物的反应，对于理解疾病机制非常重要。然而，现有的基于转录组的代谢模型主要推断细胞内反应或通路水平的活性，因此无法直接评估单个代谢物水平与细胞状态之间的关联，特别是对于作为信号分子在细胞外发挥作用而非作为代谢底物进入细胞的代谢物。为了解决这一问题，我们引入了gmMAP（基于遗传信息的代谢物特征跨单细胞和空间组织映射），这是一个整合代谢物GWAS汇总统计与单细胞和空间转录组以在细胞和空间分辨率下映射代谢程序的框架。值得注意的是，gmMAP能够预测内源性代谢过程的激活，同时揭示外源代谢物与多种细胞功能状态之间的内在关联。为了进一步捕捉细胞代谢网络的连通性，我们整合了基于约束的代谢通量模型来评估全局代谢活性。为了评估gmMAP的准确性和泛化能力，我们将该框架应用于涵盖人类发育、生理稳态、炎症和癌症的代表性生物学场景。在人类肾脏发育中，gmMAP捕获了动态代谢程序，并通过配对的转录组和代谢组参考数据集进行验证，支持其在代谢物识别和代谢流推断中的可靠性。在器官水平上，gmMAP重建了稳态和自身免疫性炎症条件下17个小鼠器官的空间代谢物分布模式，并进一步将gmMAP扩展到24种正常人类组织，生成了器官和细胞分辨率下的多尺度代谢图谱。在疾病背景下，gmMAP揭示了29种泛癌细胞群体的代谢重编程，并确定了溃疡性结肠炎中外源代谢物与炎症相关基质代谢重塑之间的潜在联系。总之，gmMAP能够一致地将基于遗传信息的代谢物特征与细胞状态、空间组织结构和疾病病理联系起来。

## Abstract
Defining cell-type-specific endogenous metabolic features, the spatial distribution of cell-level metabolic states and cellular responses to exogenous metabolites is very important for understanding disease mechanisms. However, existing transcriptome-based metabolic models primarily infer intracellular reaction or pathway-level activities, and therefore cannot directly assess associations between individual metabolite levels and cellular states, particularly for metabolites that act extracellularly as signalling molecules rather than entering cells as metabolic substrates. To overcome this problem, we introduce the gmMAP (Genetically informed metabolite trait mapping across single-cell and spatial tissues), a framework that integrates metabolite GWAS summary statistics with single-cell and spatial transcriptomes to map metabolic programmes at cellular and spatial resolution. Notably, the gmMAP enables the prediction of endogenous metabolic process activation while also revealing intrinsic associations between exogenous metabolites and diverse cellular functional states. To further capture the connectivity of cellular metabolic networks, we incorporated a constraint-based metabolic flux model to evaluate global metabolic activity. To evaluate the accuracy and generalizability of gmMAP, we applied the framework across representative biological contexts spanning human development, physiological homeostasis, inflammation and cancer. In human kidney development, the gmMAP captured dynamic metabolic programmes, which was validated using paired transcriptomic and metabolomic reference datasets, supporting its reliability in metabolite identification and metabolic-flow inference. At the organ level, the gmMAP reconstructed spatial metabolite distribution patterns across 17 mouse organs under homeostatic and autoimmune inflammatory conditions, and further extension of gmMAP to 24 normal human tissues generated a multi-scale metabolic atlas at both organ and cellular resolutions. In disease settings, gmMAP revealed metabolic reprogramming across 29 pan-cancer cell populations, and identified potential links between exogenous metabolites and inflammation-associated stromal metabolic remodelling in ulcerative colitis. Together, gmMAP can consistently connect genetically informed metabolite traits with cell states, spatial tissue organization and disease pathology.