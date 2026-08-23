---
title: Pheno-MYCN maps the morphological footprint of MYCN amplification in paediatric neuroblastoma
title_zh: Pheno-MYCN 绘制儿童神经母细胞瘤中 MYCN 扩增的形态学足迹
authors: "Chai, B., Fourkioti, O., Naidoo, R., De Vries, M., George, S., Chesler, L., Hutchinson, J. C., Bakal, C."
date: 2026-08-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.20.745848v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 弱监督机器学习框架将切片水平的分子预测与可解释形态表型关联，可迁移至耐药预测
tldr: "MYCN扩增是小儿神经母细胞瘤的关键预后标志，但现有分子检测多为整体水平，难以与病理形态直接对应。作者开发Pheno-MYCN，基于弱监督学习，在常规H&E全切片图像上联合预测切片级MYCN状态与解构形态学子群，并利用细胞级特征刻画扩增的形态学足迹。在189张切片上，该方法仅凭形态特征即可识别MYCN扩增样组织，AUC达0.93-1.00，且能定位其空间梯度分布。该工作提供了一种低成本、可解释的筛查方案，在分子检测受限地区具有重要应用价值。"
source: biorxiv
selection_source: fresh_fetch
motivation: "现有MYCN检测与组织形态脱节，单独使用均无法全面识别高危病例，需在H&E上定位扩增的形态足迹。"
method: "开发Pheno-MYCN，用弱监督方式在H&E全切片上联合预测MYCN状态与形态学子群，并剖析细胞级特征。"
result: 在189张切片上，仅凭形态特征即可识别MYCN扩增样组织，AUC达0.93-1.00，且能定位其空间分布。
conclusion: "MYCN扩增在常规H&E上留下可解释的形态学足迹，为分子检测受限地区提供低成本标记与定位手段。"
---

## 摘要
MYCN 扩增长期以来一直是儿童神经母细胞瘤的预后标志物，但通常是在整体水平上进行检测，与病理学家评估的异质性组织结构并列而非在其内部。这留下了一个空白：仅凭 MYCN 状态无法定位 MYCN 相关的生物学特征，而仅凭形态学无法赋予分子风险。基于我们发现两者结合能识别出任一单独方法遗漏的高危病例，我们开发了 Pheno-MYCN，一种弱监督框架，将切片水平的 MYCN 预测与常规 H&E 全切片图像上可解释的形态学子群联系起来。其目的并非构建更强的分类器：预测探究 MYCN 扩增对组织的影响，其证据可接受病理学审查。在 189 张切片中，Pheno-MYCN 将每张切片解析为表型聚类，专家审查将其映射到神经母细胞瘤形态。细胞水平分析显示，MYCN 扩增在每个子群中都留有“标记”，但每个子群的标记特征不同：细胞密集但无序的肿瘤，具有更稀疏、多样性较低的网络；主要在坏死和出血区域中丰度增加。仅凭这些特征即可在切片水平识别 MYCN 扩增样组织（AUC 0.93-1.00，留一切片交叉验证），并在肿瘤内表现为连续梯度。因此，MYCN 扩增留下了具体、可解释的足迹，可在常规 H&E 上读取和定位，为分子检测受限的环境提供了一种低成本的标记和映射方法。

## Abstract
MYCN amplification has long been a prognostic marker in paediatric neuroblastoma, yet is typically assayed in bulk, alongside rather than within the heterogeneous tissue architecture pathologists assess. This leaves a gap: MYCN status alone cannot localise MYCN-associated biology, while morphology alone cannot assign molecular risk. Motivated by our finding that the two together identify high-risk cases missed by either, we developed Pheno-MYCN, a weakly supervised framework linking slide-level MYCN prediction to interpretable morphological sub-populations on routine H&E whole-slide images. The aim is not a stronger classifier: prediction probes what MYCN amplification does to the tissue, its evidence open to pathological scrutiny. Across 189 slides, Pheno-MYCN resolved each into phenotypic clusters that expert review mapped to neuroblastoma morphologies. Cell-level profiling revealed MYCN amplification "marked" every sub-population, through a different feature in each: densely cellular yet disorganised tumour with sparser, less diverse networks; chiefly abundance in necrotic and haemorrhagic regions. MYCN-amplified-like tissue was identifiable per slide from these features alone (AUC 0.93-1.00, leave-one-slide-out) and traced as a continuous gradient within tumours. Thus MYCN amplification leaves a concrete, interpretable footprint that can be read and localised on routine H&E, offering a low-cost means to flag and map it where molecular testing is limited.