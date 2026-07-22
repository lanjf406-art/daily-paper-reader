---
title: Absolute quantitative proteomics guides patient-stratified drug repurposing in clear cell and papillary renal cell carcinoma.
title_zh: 绝对定量蛋白质组学指导透明细胞和乳头状肾细胞癌中患者分层药物重定位
authors: "Figueiredo, A. Q., Domingos, I. F., Lodeiro, C., Dhir, R., Carvalho, L. B., Mercolini, L., Wisniewski, J. R., Moroncini, G., Medeiros, M., Pinheiro, L. C., Mansinho, H., Santos, H. M., Korentzelos, D., Capelo, J. L."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.17.738718v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 蛋白质组学指导肾癌药物重定位，生物信息学用于药物反应分析
tldr: 肾细胞癌高度异质性，不同亚型及患者间治疗反应差异大。本研究采用基于总蛋白方法的绝对定量蛋白质组学，结合药物靶点数据库，分析透明细胞和乳头状肾癌组织，识别患者特异性上调蛋白并提名FDA批准药物作为重定位候选。结果显示两亚型具有不同治疗脆弱性，ACLY是跨亚型共享靶点。该框架为肾癌个体化治疗分层提供了可扩展的蛋白质组学方法。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1511, \"height\": 1313, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1491, \"height\": 1832, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1520, \"height\": 1565, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1507, \"height\": 896, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 3476, \"height\": 3688, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 2933, \"height\": 6294, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 8463, \"height\": 6162, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 8775, \"height\": 4719, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 6829, \"height\": 1652, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-17-738718-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 6838, \"height\": 1574, \"label\": \"Table\"}]"
motivation: 肾癌亚型内高度异质性导致疗效差异，需基于蛋白质组学的个体化药物重定位策略。
method: TPA绝对定量蛋白质组学分析17例肾组织，差异蛋白与TTD数据库交叉，提名FDA批准药物。
result: 为ccRCC和pRCC分别鉴定出患者分层候选药物（如bempedoic acid、auranofin），ACLY为共同代谢脆弱点。
conclusion: 建立了绝对定量蛋白质组学指导的药物重定位框架，可用于肾癌患者分层和个性化决策。
---

## 摘要
背景：肾细胞癌（RCC）是一种高度异质性疾病，其不同的分子亚型表现出特征性的基因组、代谢和微环境特征，影响治疗反应。即使在同一组织学类别的肿瘤中，每个亚型内的患者间也存在显著差异，导致临床结局截然不同。蛋白质组学可直接反映肿瘤生物学和通路活性，补充基因组信息，并能够识别患者特异性的可干预弱点。我们应用基于总蛋白方法（TPA）的处方组学框架，将绝对定量蛋白质组学与经过整理的药物-靶点知识相结合，以提名患者特异性的药物重定位选项，作为当前标准治疗的辅助手段。

方法：从公开的PRIDE数据库（PXD023296）中获取了17个人肾组织标本，包括7例透明细胞RCC（ccRCC）、5例乳头状RCC（pRCC）和5例正常邻近组织（NAT），并基于已有的无标记LC-MS/MS数据，采用TPA绝对定量方法重新分析。通过肿瘤亚型与NAT之间的差异表达分析，鉴定出亚型特异性上调蛋白，并与治疗靶点数据库（TTD）交叉比对，提名靶向失调蛋白的FDA批准药物作为候选重定位策略。

结果：ccRCC和pRCC产生不同的全蛋白质组上调谱，与其已知的生物学驱动因素一致。TPA指数分层提名bempedoic acid（ACLY抑制剂）和tipiracil hydrochloride（TYMP抑制剂）作为ccRCC的患者分层候选药物，而auranofin（TXNRD1抑制剂）、bempedoic acid和mipomersen（APOB导向的反义寡核苷酸）则用于pRCC。ACLY是两种亚型共同拥有的唯一高优先级靶点，提示存在跨亚型的候选代谢弱点。在两种亚型中，通过蛋白质-蛋白质相互作用网络分析发现了次要候选靶点。

结论：本研究提出了一种定量蛋白质组学框架，用于将个体患者的蛋白质组学失调转化为主要RCC亚型中的辅助药物重定位假说。通过将TPA用于绝对蛋白质定量与处方组学指导的药物-靶点映射相结合，我们证明ccRCC和pRCC具有不同的、可个体分层的治疗弱点。这些发现为基于蛋白质组学的RCC治疗分层提供了概念验证，并建立了一个可扩展的框架，在功能验证后，可为RCC亚型的个性化治疗决策提供信息。

## Abstract
BackgroundRenal cell carcinoma (RCC) is a highly heterogeneous disease in which distinct molecular subtypes exhibit characteristic genomic, metabolic, and microenvironmental features that influence therapeutic response. Substantial inter-patient variability exists within each subtype, resulting in markedly different clinical outcomes even among tumours of the same histological category. Proteomics provides a direct readout of tumour biology and pathway activity, complementing genomic information and enabling the identification of patient-specific actionable vulnerabilities. We applied a Total Protein Approach (TPA)-based prescriptomics framework that integrates absolute quantitative proteomics with curated drug-target knowledge to nominate patient-specific drug-repurposing options, positioned as coadjuvants to the prevailing standard of care.

MethodsSeventeen human kidney tissue specimens, seven clear cell RCC (ccRCC), five papillary RCC (pRCC), and five normal adjacent tissues (NAT), were retrieved from the publicly available PRIDE repository (PXD023296) and reanalysed by TPA-based absolute quantification applied to previously acquired label-free LC-MS/MS data. Differential expression analysis between each tumour subtype and NAT identified subtype-specific upregulated proteins, wich were intersected with Therapeutic Target Database (TTD) to nominate FDA-approved drugs targeting dysregulated proteins as candidate repurposing strategies.

ResultsccRCC and pRCC produced distinct proteome-wide upregulation profiles consistent with their known biological drivers. TPA index stratification nominated bempedoic acid (ACLY inhibitor) and tipiracil hydrochloride (TYMP inhibitor) as patient-stratified candidates for ccRCC, and auranofin (TXNRD1 inhibitor), bempedoic acid, and mipomersen (APOB-directed antisense oligonucleotide) for pRCC. ACLY was the only top-priority target shared across both subtypes, pointing to a candidate cross-subtype metabolic vulnerability. Secondary candidates emerged from protein-protein interaction network analysis in both subtypes..

ConclusionsThis study presents a quantitative proteomics framework for translating individual-patient proteomic dysregulation into coadjuvant drug-repurposing hypotheses across the principal RCC subtypes. By combining the TPA for absolute protein quantification with prescriptomics-guided drug-target mapping, we show that ccRCC and pRCC harbour distinct, individually stratifiable therapeutic vulnerabilities. These findings provide a proof-of-concept for proteomics-based treatment stratification in RCC and establish a scalable framework that, pending functional validation, could inform personalised therapeutic decision-making across RCC subtypes.