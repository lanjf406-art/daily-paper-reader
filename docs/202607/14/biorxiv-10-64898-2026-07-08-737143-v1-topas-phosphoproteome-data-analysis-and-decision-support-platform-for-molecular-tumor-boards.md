---
title: "TOPAS: phosphoproteome data analysis and decision support platform for molecular tumor boards"
title_zh: TOPAS：面向分子肿瘤委员会的磷酸化蛋白质组数据分析与决策支持平台
authors: "Jensen, C. B., Sakhteman, A., Hamood, F., Schneider, A., Woortman, J., Teleanu, M.-V., Horak, P., Bayer, F. P., Stange, C., Huellein, J., Hübschmann, D., Henssen, A. G., Fröhling, S., Kuster, B., The, M."
date: 2026-07-13
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.08.737143v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 生物信息学平台可用于耐药分析
tldr: 肿瘤分子委员会依赖基因组学常缺乏可操作靶点，磷酸化蛋白质组学可填补缺口。为此开发了TOPAS平台，一个端到端分析管道，整合1998个肿瘤样本数据，计算TOPAS评分并生成患者特异性报告。该平台支持质量控制和交互分析，识别肿瘤抗原和免疫检查点。最终，TOPAS作为开源工具促进了磷酸化蛋白质组学在精准肿瘤学中的临床采纳。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737143-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1699, \"height\": 1614, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737143-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 866, \"height\": 1645, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737143-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1669, \"height\": 1445, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737143-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1700, \"height\": 1794, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737143-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1709, \"height\": 1075, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737143-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1702, \"height\": 1615, \"label\": \"Figure\"}]"
motivation: 基因组学在肿瘤分子委员会中常无法识别临床可操作靶点，磷酸化蛋白质组学可提供补充信息。
method: 开发TOPAS平台，集成1998个肿瘤样本的磷酸化蛋白质组数据，通过端到端管道计算评分并生成报告。
result: 平台支持质量控制、差异丰度分析、异常值检测，并识别肿瘤抗原和免疫检查点。
conclusion: TOPAS是开源平台，解决了磷酸化蛋白质组学在精准肿瘤学中临床应用的迫切需求。
---

## 摘要
分子肿瘤委员会（MTB）是精准肿瘤学的核心，基于患者肿瘤的分子特征提供个性化治疗建议。基因组学对MTB至关重要，但常常无法识别临床可操作的靶点，而磷酸化蛋白质组学可以填补这一空白。我们提出了肿瘤蛋白质组活性状态（TOPAS）平台，这是一个端到端分析流程，将数TB的磷酸化蛋白质组数据转化为用于MTB讨论的患者特定报告，重点关注与致癌机制和治疗靶点相关的临床相关信号。该平台设计用于随队列增长而扩展，整合了1,998份肿瘤样本的数据，以支持患者和队列层面的假说生成。一个门户网站负责质量控制、计算TOPAS评分、识别肿瘤抗原和免疫检查点，并提供差异蛋白丰度和异常检测的交互式分析。TOPAS平台是开源的，解决了关键未满足的需求，并促进未来磷酸化蛋白质组学在精准肿瘤学中的更广泛应用。

## Abstract
The molecular tumor board (MTB) is central to precision oncology, providing personalized treatment recommendations based on molecular profiles of patient tumors. Genomics is instrumental for MTBs but often fails to identify clinically actionable targets, a gap that phosphoproteomics can fill. We present the tumor proteome activity status (TOPAS) platform, an end to end analysis pipeline that converts terabytes of phosphoproteomic data into patient-specific reports for MTB discussions, focusing on clinically relevant signaling linked to oncogenic mechanisms and therapeutic targets. Designed to scale with growing cohorts, the platform integrates data from 1,998 tumor samples to support patient- and cohort-level hypothesis generation. A web portal handles quality control, calculates TOPAS scores, identifies tumor antigens and immune checkpoints, and offers interactive analyses of differential protein abundance and outlier detection. The TOPAS platform is open source, addresses a critical unmet need and facilitates broader adoption of phosphoproteomics in precision oncology in the future.