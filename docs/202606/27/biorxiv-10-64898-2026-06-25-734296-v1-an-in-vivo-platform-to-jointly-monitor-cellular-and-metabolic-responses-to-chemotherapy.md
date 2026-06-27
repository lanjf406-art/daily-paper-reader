---
title: An in vivo platform to jointly monitor cellular and metabolic responses to chemotherapy.
title_zh: 一个用于联合监测细胞和代谢对化疗反应的体内平台
authors: "Pister, V., Tatarova, Z., Park, N., Gaidhani, G., Jakubik, J., Heiser, L., Blum, J., Palmiotti, A., Maloney, E., Fraenkel, E., Davidson, S., Jonas, O."
date: 2026-06-26
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.25.734296v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 监测肿瘤微环境中的免疫和代谢反应
tldr: 现有方法难以同时监测肿瘤内药物暴露引起的免疫和代谢重塑。本文构建空间药理学平台，利用微装置实现单肿瘤内多药物局部递送，结合CyCIF-MALDI成像获取大规模配对数据。代谢特征可预测蛋白质空间邻域，揭示CSF1R+巨噬细胞与MPO+髓系细胞间的极化轴，并在耐药区发现脂质相关巨噬细胞样群体。该平台首次实现肿瘤内药物-免疫-代谢的多重原位关联分析，为精准药理学提供新工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有技术无法在完整肿瘤内同时追踪化疗引起的免疫和代谢动态变化，需要开发原位多模态分析方法。
method: 开发空间药理学微装置，在单肿瘤内局部递送多种药物，结合CyCIF-MALDI成像生成1.5百万细胞的空间代谢-蛋白组配对数据。
result: 代谢特征可预测蛋白邻域；识别CSF1R+巨噬细胞与MPO+髓系细胞极化轴；耐药区出现脂质相关巨噬细胞样群体。
conclusion: 该平台实现了肿瘤内药物暴露、免疫表型与代谢重塑的多重原位监测，揭示了代谢作为肿瘤组织关键组织者的作用。
---

## 摘要
药物处理如何重塑完整肿瘤内的免疫和代谢状态，现有方法难以研究。我们介绍了一种空间药理学平台，能够在一个肿瘤内并行分析多种药物，将局部药物暴露与免疫和代谢重塑联系起来。通过使用用于局部药物递送的微装置，我们创建了一个大规模配对CyCIF-MALDI数据集，涵盖27个MMTV-PyMT肿瘤切片和9种治疗方案中的150万个细胞，实现了前所未有的规模集成空间药理学。代谢特征稳健地预测蛋白质组空间邻域，将代谢确立为肿瘤组织和免疫表型的有力预测因子。在此框架内，我们识别出一个由CSF1R+肿瘤相关巨噬细胞与靠近药物诱导肿瘤细胞死亡区域的MPO+浸润髓系细胞之间的髓系极化所定义的主导代谢轴。最后，我们在耐药治疗区域检测到推定的脂质相关巨噬细胞（LAM）样群体。

## Abstract
How drug treatments reshape immune and metabolic states within intact tumors remains difficult to study with existing methods. We introduce a spatial pharmacology platform that enables parallel analysis of multiple agents within a single tumor, linking local drug exposure to immune and metabolic remodeling. Using a microdevice for localized drug delivery, we created a large-scale paired CyCIF-MALDI dataset spanning 1.5 million cells across 27 MMTV-PyMT tumor sections and nine treatment programs, enabling integrated spatial pharmacology at unprecedented scale. Metabolic signatures robustly predict proteomic spatial neighborhoods establishing metabolism as a powerful predictor of tumor organization and immune phenotype. Within this framework, we identify a dominant metabolic axis defined by the myeloid polarization between CSF1R+ tumor-associated macrophages and MPO+ infiltrating myeloid cells localized near regions of drug-induced tumor cell death. Finally, we detect putative lipid-associated macrophage (LAM)-like populations within drug-resistant treatment regions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：当前缺乏能够同时追踪化疗药物在完整肿瘤内引起的免疫重塑和代谢重塑的技术。传统方法往往只能独立分析免疫或代谢，难以在空间原位层面揭示药物暴露、免疫表型与代谢状态的动态关联。
- **整体含义**：作者开发了一种空间药理学平台，通过微装置在一个肿瘤内并行递送多种药物，结合高维成像技术（CyCIF-MALDI）生成大规模配对数据，首次实现了肿瘤内药物-免疫-代谢的多重原位关联分析。该方法为精准药理学提供了新工具，并揭示了代谢作为肿瘤组织关键组织者的作用。

## 2. 论文提出的方法论

- **核心思想**：利用一种微装置（microdevice）实现单肿瘤内多药物的局部递送，从而在同一个肿瘤切片上同时产生多个药物处理区域（包括对照）。随后对切片进行**CyCIF（循环免疫荧光）** 和**MALDI（基质辅助激光解吸电离）成像**，分别获取蛋白质组和代谢组的空间信息，并通过图像配准生成配对数据。
- **关键技术细节**：
  - 微装置：可局部释放不同化疗药物（如多柔比星、紫杉醇等），每个微孔对应一种药物条件，覆盖肿瘤不同区域。
  - 成像：CyCIF用于标记免疫细胞标志物（如CSF1R、MPO）、肿瘤细胞及细胞死亡标志物；MALDI-MS成像用于检测代谢物（如脂质、核苷酸等）。
  - 数据分析：对配对的CyCIF-MALDI数据进行空间邻域分析、代谢特征预测蛋白邻域、聚类分析（识别细胞群体），以及极化轴分析等。
- **公式或算法流程**（文字说明）：
  - 数据采集 → 图像配准 → 单细胞分割 → 提取每个细胞的蛋白质标志物表达和代谢物丰度 → 构建空间邻域图（如K近邻图） → 基于代谢特征训练模型预测蛋白质空间邻域 → 识别代谢-免疫关联轴 → 空间聚类发现耐药区域的特殊细胞群体。

## 3. 实验设计

- **使用的数据集**：
  - 27个MMTV-PyMT小鼠乳腺癌肿瘤切片。
  - 9种治疗方案（包括多种化疗药物及组合），每个切片内包含多个局部药物处理点和对照。
  - 总分析细胞数：约150万个细胞。
- **Benchmark**：未明确提及外部基准数据集或标准方法。主要采用内部对照（肿瘤内未处理区域）作为比较基准。
- **对比的方法**：文中未进行与传统方法的系统性对比（如单独CyCIF或单独MALDI），而是强调该平台能生成前所未有的配对数据规模。但通过空间预测分析（代谢特征预测蛋白邻域）验证了代谢信息的预测能力。

## 4. 资源与算力

- 论文摘要及元数据**未明确说明**使用的GPU型号、数量、训练时长等计算资源信息。仅提及生成了大规模配对数据集（150万细胞），数据处理和成像分析可能依赖常规工作站或HPC，但细节缺失。

## 5. 实验数量与充分性

- **实验数量**：覆盖27个肿瘤切片、9种治疗方案，单细胞数量达150万，属于大规模体内实验。但未报告重复肿瘤数量（每个条件是否有多只小鼠重复）、是否进行了独立的验证队列。
- **充分性与客观性**：
  - 优点：在同一肿瘤内设置多个局部药物处理，减少个体间差异；配对CyCIF-MALDI数据确保空间一致性。
  - 不足：缺乏与传统方法（如流式细胞术、质谱流式）的定量对比；结果仅来自MMTV-PyMT单一乳腺癌模型，泛化性有限；未进行消融实验或控制实验（如无药物对照组仅依赖微装置空白区域）。

## 6. 论文的主要结论与发现

- **主要结论**：该空间药理学平台成功实现了肿瘤内药物暴露、免疫表型与代谢重塑的多重原位监测。
- **具体发现**：
  1. 代谢特征可稳健预测蛋白质组空间邻域，表明代谢是肿瘤组织和免疫表型的有力预测因子。
  2. 识别出一个主导代谢轴：由CSF1R+肿瘤相关巨噬细胞与MPO+浸润髓系细胞之间的髓系极化所定义，且该极化轴靠近药物诱导肿瘤细胞死亡区域。
  3. 在耐药治疗区域检测到推定的脂质相关巨噬细胞（LAM）样群体，提示代谢适应在耐药性中发挥作用。

## 7. 优点

- **技术创新**：将局部药物递送微装置与双模态成像（CyCIF + MALDI）结合，首次在单个肿瘤内实现药物、免疫、代谢三重空间图谱的同步获取。
- **数据规模**：150万细胞的大规模配对数据，超越了以往的空间药理学研究。
- **分析深度**：通过代谢特征预测蛋白邻域，揭示了代谢作为肿瘤组织组织者的新视角。
- **生物学发现**：识别了CSF1R-MPO极化轴和抵抗区域LAM样群体，为化疗耐药机制提供了新线索。

## 8. 不足与局限

- **实验覆盖**：仅使用单一乳腺癌小鼠模型（MMTV-PyMT），未在人源样本或不同肿瘤类型中验证。
- **偏差风险**：微装置物理插入可能引起局部组织损伤和炎症反应，影响药物反应的真实性；局部药物递送浓度与全身给药不一致，结果外推受限。
- **方法对比缺失**：未与标准药理学方法（如全身给药后活检）进行系统性比较，难以评估该平台的额外价值。
- **算力与可重复性**：论文未提供计算资源细节，影响实验可重复性评估。
- **验证不足**：未通过功能实验（如基因敲除）验证所识别代谢轴和LAM群体的因果作用。

（完）
