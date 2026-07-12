---
title: AI-enabled Spatial Profiling of Circulating Tumor-Immune Ecosystems Predicts Patient Outcomes Across Cancers
title_zh: AI驱动的循环肿瘤-免疫生态系统空间谱分析预测多种癌症患者预后
authors: "Squires, J. R., Sun, Y., Hoffmann, A., Zhang, Y., Pan, H., Tong, F., He, Y., Scholten, D., Almubarak, H., Gurley, M., Minor, A., Singh, A., Zhang, J., Ding, H., Mao, C., Platanias, L. C., Yu, J., Hussain, M., Luo, Y., Gradishar, W. J., Cristofanilli, M., Cooper, L. A. D., Zhao, L., Fang, D., Stringer, C., Liu, H."
date: 2026-07-09
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.02.736133v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: AI空间分析预测患者结局，可适配用于耐药预测
tldr: 循环肿瘤细胞与免疫细胞在血液中构成动态多细胞生态系统，但其空间组织及临床意义尚未系统阐明。我们开发了基于AI的CCIP框架，通过分析常规多重免疫荧光扫描，高精度识别CTCs和五种免疫细胞，并量化多细胞簇及其相互作用。在1399名患者的2693份扫描中（超6000万细胞），14特征图像模型预测乳腺癌总生存期，优于传统指标且泛化至前列腺癌。该工作揭示了循环肿瘤-免疫空间结构与全身免疫功能障碍的关联，为液体活检提供新范式。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 2160, \"height\": 2135, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1908, \"height\": 2610, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 2116, \"height\": 2746, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1862, \"height\": 1098, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 2017, \"height\": 2741, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 2207, \"height\": 2795, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1677, \"height\": 403, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1878, \"height\": 969, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-02-736133-v1/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1862, \"height\": 1098, \"label\": \"Table\"}]"
motivation: 循环肿瘤细胞与免疫细胞的空间组织及其临床相关性尚未被系统表征。
method: 开发基于AI的CCIP框架，分析多重免疫荧光扫描，自动识别CTCs、免疫细胞及其多细胞簇。
result: 14特征图像模型预测乳腺癌和前列腺癌总生存期，优于临床病理变量和CTC计数。
conclusion: 循环肿瘤-免疫空间结构成像特征与治疗反应及免疫抑制状态相关，可泛化至多种癌症。
---

## 摘要
循环肿瘤细胞（CTCs）和免疫细胞在血液中形成动态的多细胞生态系统，但它们的空间组织及临床相关性尚未得到系统表征。我们开发了细胞和簇识别程序（CCIP），这是一种基于人工智能的框架，可分析常规多重免疫荧光血液扫描，高精度分割细胞、识别CTCs及五种免疫谱系，并量化多细胞簇和肿瘤-免疫相互作用。将CCIP应用于来自1399名患者的2693份血液扫描，我们分析了超过6000万个细胞（>700万个多细胞簇），并将成像衍生特征与患者预后相关联。与循环肿瘤DNA突变负荷相关的一个14特征图像模型预测了乳腺癌的总生存期，优于临床病理变量和CTC计数，并推广至前列腺癌。预后成像特征还与治疗反应相关的无进展生存期以及单细胞RNA测序衍生的免疫抑制状态相关联，将循环肿瘤-免疫结构与系统性免疫功能障碍联系起来。

## Abstract
Circulating tumor cells (CTCs) and immune cells form dynamic multicellular ecosystems in blood, but their spatial organization and clinical relevance have not been systematically characterized. We developed the Cell and Cluster Identification Program (CCIP), an artificial intelligence-based framework that analyzes routine multiplex immunofluorescence blood scans to segment cells, identify CTCs and five immune lineages with high accuracy, and quantify multicellular clusters and tumor-immune interactions. Applying CCIP to 2,693 blood scans from 1,399 patients, we profiled over 60 million cells (>7 million multi-cell clusters) and linked imaging-derived features to patient outcomes. Correlated with circulating-tumor DNA mutation burdens, a 14-feature image model predicted overall survival in breast cancer, outperformed clinicopathologic variables and CTC enumeration, and generalized to prostate cancer. Prognostic imaging signatures were also associated with therapy response-related progression-free survival as well as with single-cell RNA sequencing-derived immune suppression states, connecting circulating tumor-immune architecture with systemic immune dysfunction.