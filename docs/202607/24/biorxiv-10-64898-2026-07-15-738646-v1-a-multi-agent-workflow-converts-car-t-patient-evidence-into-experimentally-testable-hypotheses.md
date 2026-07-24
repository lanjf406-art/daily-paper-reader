---
title: A multi-agent workflow converts CAR-T patient evidence into experimentally testable hypotheses
title_zh: 多智能体工作流将CAR-T患者证据转化为可实验检验的假设
authors: "Wang, S., Li, Y.-R., Wang, Q., Yang, Y., Shen, X., Li, H., Nan, H., Chen, Z., Zhu, Y., Zhang, B., Ding, H., Soto, J., Park, S., Zheng, Y., Huang, X., Yang, L., Li, D., Li, S."
date: 2026-07-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.15.738646v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 基于CAR-T患者scRNA-seq数据的多智能体工作流生成耐药相关假设
tldr: CAR-T细胞研究证据分散且碎片化，难以生成可实验验证的机制假设。BioPathfinder通过多智能体工作流，整合单细胞数据集与文献，构建可追溯的资源，并利用角色专用LLM评审子代理优先排序假设。应用该引擎识别出NK样转变相关基因，其中KLRC1/NKG2A的阻断在体内外模型中改善CAR-T抗肿瘤功能与持久性。该工作证明了结构化临床单细胞证据可被领域专用多智能体系统转化为可操作的CAR-T工程假设。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738646-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1900, \"height\": 1569, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738646-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1893, \"height\": 1436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738646-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1916, \"height\": 1634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738646-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1902, \"height\": 2004, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-15-738646-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1864, \"height\": 1641, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-15-738646-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1903, \"height\": 649, \"label\": \"Table\"}]"
motivation: 解决CAR-T研究证据碎片化、假设生成缺乏系统性和可验证性的问题。
method: 构建追踪来源的论文-数据集资源，结合多智能体规划与角色专用LLM评审，优先排序可实验验证的机制假设。
result: 识别出NK样转变相关基因KLRC1/NKG2A作为耗竭标记，其阻断在慢性刺激模型中改善CAR-T抗肿瘤功能和持久性相关指标。
conclusion: 多智能体系统可将临床单细胞证据转化为可实验验证的CAR-T工程假设，促进精准靶点发现。
---

## 摘要
嵌合抗原受体（CAR）T细胞研究的快速扩张产生了碎片化的证据格局，将出版物、数据库条目、患者元数据和机制观察联系在一起。这里我们提出BioPathfinder，一个用于CAR-T研究证据构建、假设生成和验证规划的多智能体发现引擎。与现有的以预定义CAR-T开发任务为中心的基于LLM和智能体的方法不同，BioPathfinder构建了一个带有溯源追踪的资源，将来自治疗患者的scRNA-seq数据集与其出版物联系起来，并利用它生成多样化、可证伪且数据集感知的机制性假设，这些假设由角色专精的LLM评审子智能体优先进行计算和实验验证。应用于策划的CAR-T治疗患者论文-数据集语料库，BioPathfinder提名了CAR-T持久性、功能障碍和治疗抵抗的候选机制，包括与NK样转换程序相关的基因可能被靶向以减少CAR-T耗竭并促进持久性的假设。患者scRNA-seq分析显示，这种NK样转换相关程序在耗竭的输注后CAR-T细胞状态中富集。虚拟扰动进一步优先考虑了与转换相关的KLR家族受体基因，包括KLRC1、KLRD1和KLRG1。专家评审选择了编码NKG2A的KLRC1进行实验测试。体外和体内慢性刺激模型显示，NKG2A标记了具有激活和耗竭相关表型的CD8+ CAR-T细胞。NKG2A阻断在体内改善了抗肿瘤功能和持久性相关读数。这些结果表明，结构化的临床单细胞证据可以通过领域专精的多智能体系统转化为可实验执行的CAR-T工程假设。

## Abstract
The rapid expansion of chimeric antigen receptor (CAR) T cell studies has produced a fragmented evidence landscape linking publications, repository accessions, patient metadata and mechanistic observations. Here we present BioPathfinder, a multi-agent discovery engine for CAR-T research evidence construction, hypothesis generation and validation planning. Unlike existing LLM-based and agentic approaches centered on predefined CAR-T development tasks, BioPathfinder constructs a provenance-tracked resource linking scRNA-seq datasets from treated patients to their publications and uses it to generate diverse, falsifiable and dataset-aware mechanistic hypotheses prioritized for computational and experimental validation by role-specialized LLM reviewer subagents. Applied to the curated CAR-T-treated patient paper-dataset corpus, BioPathfinder nominated candidate mechanisms of CAR-T persistence, dysfunction and therapeutic resistance, including the hypothesis that genes associated with an NK-like transition program could be targeted to reduce CAR-T exhaustion and promote persistence. Patient scRNA-seq analysis showed that this NK-like transition-associated program was enriched in exhausted post-infusion CAR-T cell states. Virtual perturbation further prioritized transition-associated KLR-family receptor genes, including KLRC1, KLRD1 and KLRG1. Expert review selected KLRC1, encoding NKG2A, for experimental testing. In vitro and in vivo chronic-stimulation models showed that NKG2A marked CD8+ CAR-T cells with activated and exhaustion-associated phenotypes. NKG2A blockade improved antitumour function and persistence-associated readouts in vivo. These results show that structured clinical single-cell evidence can be transformed by domain-specialized multi-agent systems into experimentally actionable CAR-T engineering hypotheses.

HighlightsO_LIBioPathfinder structures fragmented CAR-T patient evidence into a provenance-tracked paper-dataset resource.
C_LIO_LIMulti-agent planning and review prioritize experimentally testable mechanisms of CAR-T dysfunction.
C_LIO_LIExpert selection from BioPathfinder-nominated NK-like transition-associated genes identifies KLRC1/NKG2A blockade as a strategy to promote CAR-T persistence.
C_LI