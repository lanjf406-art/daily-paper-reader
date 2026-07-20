---
title: "SMART: A Somatic Mutation Annotation and Reporting Tool for cancer genomics"
title_zh: SMART：一种用于癌症基因组学的体细胞突变注释和报告工具
authors: "Dominguez, M., Reddin, I. G., Gibson, J., Rudraraju, M., Veal, K., Kipps, C., Williams, A., Ennis, S."
date: 2026-07-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.15.738659v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 用于耐药突变注释的生物信息学工具
tldr: 针对癌症基因组学中体细胞变异注释因转录本优先级不一致和缺乏可重复流程而受阻的问题，SMART工具构建了一个Docker化流程，整合OncoKB API注释与VEP、CIViC等多数据源，采用统一的三级转录本优先级策略，生成适用于计算、生物信息和研究解读的三级输出。验证显示与参考API在804项字段检查中完全一致，为研究提供可靠、可复现的变异注释与报告方案。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738659-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1687, \"height\": 995, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-15-738659-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1886, \"height\": 412, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-15-738659-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1884, \"height\": 854, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-15-738659-v1/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1869, \"height\": 1057, \"label\": \"Table\"}]"
motivation: 解决体细胞变异注释中转录本优先级不一致和缺乏可重复、整合OncoKB证据的研究级流程的问题。
method: "SMART是Docker化流程，嵌入OncoKB API注释并联合VEP、CIViC、ClinVar等，采用白名单>MANE Select>VEP三级转录本优先级，输出三级报告。"
result: 在804个字段级检查中，SMART与参考API完全一致，验证了其注释的准确性。
conclusion: SMART为癌症基因组学研究提供了可复现、集成多源的体细胞变异注释和报告管道，但仅限研究用途。
---

## 摘要
动机：来自靶向肿瘤 panel 的体细胞变异的转化解读受到不一致的转录本优先级排序以及缺乏原生整合 OncoKB 衍生证据用于研究目的的可重复管道的阻碍。结果：我们提出了 SMART（体细胞突变注释和报告工具），一个 Dockerised 管道，它将 OncoKB API 衍生注释（包括治疗性 L1-4、耐药性 R1-R3、诊断性 Dx1-3、预后性 Px1-3 和 FDA 级别）直接嵌入到基于 VCF 的工作流程中。SMART 将此与 VEP、CIViC、Cancer Hotspots、ClinVar、SpliceAI、REVEL、LOEUF 和 gnomAD 相结合，应用统一的三层转录本优先级排序（白名单 > MANE Select > VEP 回退），并产生面向计算、生物信息学和研究人员的三层输出。针对参考 API 的验证显示，在 804 个字段级别的检查中完全一致。可用性和实现：源代码和 Docker 镜像在 https://github.com/WeTGI-colab/SMART 上以 MIT 许可证免费提供。SMART 仅供研究使用；将 SMART 输出用于患者特定的临床报告、临床决策或其他面向患者的目的需要适当的治理和所有必要的第三方许可，包括患者报告生成所需的任何 OncoKB 许可。

## Abstract
Motivation: Translational interpretation of somatic variants from targeted oncology panels is hampered by inconsistent transcript prioritisation and by the need for reproducible pipelines that natively integrate OncoKB-derived evidence for research purposes. Results: We present SMART (Somatic Mutation Annotation and Reporting Tool), a Dockerised pipeline that embeds OncoKB API-derived annotations, including therapeutic (L1-4), resistance (R1-R3), diagnostic (Dx1-3), prognostic (Px1-3) and FDA levels, directly into a VCF-based workflow. SMART combines this with VEP, CIViC, Cancer Hotspots, ClinVar, SpliceAI, REVEL, LOEUF and gnomAD, applies a unified three-tier transcript prioritisation (whitelist > MANE Select > VEP fallback), and produces three-tiered outputs for computational, bioinformatic and research interpretation. Validation against reference APIs showed full concordance across 804 field-level checks. Availability and Implementation: Source code and Docker image are freely available at https://github.com/WeTGI-colab/SMART under the MIT License. SMART is provided for research use only; use of SMART outputs for patient specific clinical reports, clinical decision-making, or other patient-facing purposes requires appropriate governance and all required third-party licensing, including any OncoKB licence required for patient report generation.