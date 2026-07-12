---
title: "Targeting the Tumor-Stroma Crosstalk: An AI-Based Virtual Screening Strategy for Dual MET/SMO Inhibitors in Pancreatic Cancer"
title_zh: 靶向肿瘤-基质串扰：基于AI的虚拟筛选策略用于胰腺癌中双重MET/SMO抑制剂
authors: "Roggia, M., Chianese, U., Amendola, G., Albanese, V., Vetrei, C., Ierano, C., DAlterio, C., Di Maro, S., Ciardiello, F., Morgillo, F., Scala, S., Altucci, L., Preti, D., Schulte, G., Benedetti, R., Kozielewicz, P., Cosconati, S."
date: 2026-07-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.03.736313v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 基于AI的虚拟筛选靶向肿瘤-基质交互；涉及肿瘤微环境和机器学习
tldr: 胰腺导管腺癌因致密基质导致药物渗透差和免疫逃逸，需要同时靶向肿瘤和基质。基于AI虚拟筛选（PyRMD+分子对接）从900万化合物中鉴定出双靶c-MET/SMO抑制剂化合物21。该化合物能抑制SMO基质支持、c-MET肿瘤驱动，并诱导c-MET降解，在3D异质模型中比单药联合更有效。化合物21克服基质耐药，验证了双靶策略作为单一疗法的潜力。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1643, \"height\": 723, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1623, \"height\": 907, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1581, \"height\": 1487, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1568, \"height\": 2057, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1308, \"height\": 1233, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1859, \"height\": 803, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1628, \"height\": 2071, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1793, \"height\": 2109, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1629, \"height\": 1932, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-03-736313-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1658, \"height\": 1570, \"label\": \"Table\"}]"
motivation: 胰腺癌致密基质导致耐药，需要同时阻断c-MET驱动的肿瘤增殖和SMO介导的基质保护信号。
method: AI虚拟筛选结合机器学习PyRMD和分子对接，从900万化合物中识别出双靶c-MET/SMO抑制剂化合物21。
result: 化合物21选择性结合SMO正构位点（pKi=5.60），抑制GLI信号（pIC50=5.50）和c-MET激酶（pIC50=6.94），并诱导c-MET泛素化降解。
conclusion: 化合物21克服基质耐药，验证双靶c-MET/SMO抑制作为胰腺癌单一治疗策略的可行性。
---

## 摘要
胰腺导管腺癌（PDAC）是一种侵袭性恶性肿瘤，其特征是致密的结缔组织肿瘤微环境（TME），限制了药物渗透并促进免疫逃逸。因此，有效治疗需要同时调节多个信号通路。在此，我们描述了一种定向的多药理学策略，以识别c-MET和Smoothened（SMO）的双重调节剂，旨在通过抑制SMO破坏保护性基质，同时通过靶向c-MET直接抑制肿瘤细胞存活。

我们将基于机器学习平台PyRMD（在已知c-MET和SMO配体上训练）与基于结构的分子对接相结合的人工智能引导虚拟筛选工作流程应用于超过900万个化合物的文库。该方法鉴定了化合物21，一种氨基嘧啶-苯酰胺-苯氧喹啉衍生物，作为双重c-MET/SMO抑制剂。

生化和细胞研究表明，化合物21选择性结合SMO正构位点（pKi = 5.60），抑制激动剂诱导的GLI（胶质瘤相关癌基因）信号传导（pIC50 = 5.50），并有效抑制c-MET激酶活性（pIC50 = 6.94）。Western blot分析进一步显示，化合物21促进c-MET的泛素-蛋白酶体介导的降解，消除受体可用性并限制补偿性耐药信号。在包含MIAPaCa2胰腺癌细胞和CAF154-hTERT成纤维细胞的3D异型模型中，双重抑制SMO介导的基质支持和c-MET驱动的肿瘤进展比选择性抑制剂Sonidegib和PHA-665752的组合产生更大的细胞毒性。总体而言，化合物21克服了基质介导的耐药性，增强了肿瘤细胞死亡，并验证了双重SMO/c-MET靶向作为PDAC的一种有前景的单药治疗策略。

一句话摘要：一种AI鉴定的双重SMO/c-MET抑制剂克服基质耐药性并降解c-MET以抑制胰腺癌。

## Abstract
Pancreatic ductal adenocarcinoma (PDAC) is an aggressive malignancy characterized by a dense desmoplastic tumor microenvironment (TME) that limits drug penetration and promotes immune evasion. Effective treatment, therefore, requires simultaneous modulation of multiple signaling pathways. Here, we describe a directed polypharmacological strategy to identify dual modulators of c-MET and Smoothened (SMO), aiming to disrupt the protective stroma through SMO inhibition while directly suppressing tumor cell survival via c-MET targeting.

An AI-guided virtual screening workflow combining the machine-learning platform PyRMD, trained on known c-MET and SMO ligands, with structure-based molecular docking was applied to a library of over 9 million compounds. This approach led to the identification of compound 21, an aminopyrimidine-benzamide-phenoxyquinoline derivative, as a dual c-MET/SMO inhibitor.

Biochemical and cellular studies demonstrated that compound 21 selectively binds the SMO orthosteric site (pKi = 5.60), inhibits agonist-induced GLI (Glioma-associated oncogene) signaling (pIC50 = 5.50), and potently suppresses c-MET kinase activity (pIC50 = 6.94). Western blot analyses further revealed that compound 21 promotes ubiquitin-proteasome-mediated degradation of c-MET, eliminating receptor availability and limiting compensatory resistance signaling. In 3D heterotypic models comprising MIAPaCa2 pancreatic cancer cells and CAF154-hTERT fibroblasts, dual inhibition of SMO-mediated stromal support and c-MET-driven tumor progression resulted in greater cytotoxicity than the combination of the selective inhibitors Sonidegib and PHA-665752. Overall, compound 21 overcomes stromal-mediated resistance, enhances tumor cell death, and validates dual SMO/c-MET targeting as a promising single-agent therapeutic strategy for PDAC.

One Sentence SummaryAn AI-identified dual SMO/c-MET inhibitor overcomes stromal resistance and degrades c-MET to suppress pancreatic cancer.