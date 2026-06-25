---
title: "CellTosg2Sequence: A Unified Text-Omics-Signaling-Graph Large Language Model for Single-Cell Analysis"
title_zh: CellTosg2Sequence：面向单细胞分析的统一文本-组学-信号-图大语言模型
authors: "chen, w., Ye, M., Xu, T., Huang, D., Zhang, H., Li, H., Li, W., Chen, Y., Payne, P. R., Li, F."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.16.732397v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 单细胞分析大语言模型可用于耐药机制研究
tldr: "现有单细胞大语言模型仅依赖基因名作为文本信号，忽略了细胞定位、功能、疾病关联及信号交互等丰富生物先验。为此，CellTosg2Sequence将62,507节点生物知识图谱经轻量异构图编码器转化为虚拟token，拼接到细胞句子中，并通过自回归预训练、InfoNCE监督微调和GRPO本体层级奖励三阶段训练。在多个基准上显著超越强基线，仅需LoRA微调和单一统一检查点。该工作首次系统地将结构化生物先验融入单细胞语言模型，增强了细胞注释与可解释性。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有scLLM缺乏细胞定位、基因功能、疾病关联和信号图先验，限制了注释与假设生成能力。
method: 轻量图编码器将62K节点知识图谱映射为虚拟token，三阶段训练：自回归预训练、InfoNCE监督微调、GRPO本体奖励。
result: 在多个基准和消融实验中优于强基线，LoRA微调单一检查点即达最优性能。
conclusion: 首次将结构化生物先验融入单细胞语言模型，显著提升细胞注释与可解释性。
---

## 摘要
在基于单细胞的科学发现中，文本形式的生物医学先验知识和信号图对于注释和解释数值型单细胞组学数据以及生成新颖可检验假设至关重要。现有单细胞大语言模型（scLLMs）的一个主要局限是，它们仅依赖以基因名为唯一文本信号的数值表达数据，而全面的生物医学先验（细胞定位、基因功能、疾病关联和信号相互作用模式）在模型输入中缺失。我们提出CellTosg2Sequence，一种增强文本先验和信号图的细胞-组学-句子语言模型。

一个轻量级异构图表征器将精选的62,507节点生物医学知识图谱（KG）映射为紧凑的虚拟标记，这些标记被前置到每个细胞句子前，使得语言模型能够在最小序列长度开销下基于生物结构进行条件化。我们采用三阶段目标训练CellTosg2Sequence：第一阶段在自回归语言模型预训练下锚定KG通道，利用Qwen2.5-32B自身的语言推理能力进行快速KG对齐；第二阶段通过基于KG锚定InfoNCE的监督微调对齐标签；第三阶段应用带本体层次奖励的组相对策略优化（GRPO），实现能够泛化到封闭训练词汇之外的自由生成细胞类型预测。

在多个基准测试和消融实验中，CellTosg2Sequence优于强基线。所有结果均通过轻量级LoRA训练和单个统一检查点获得。

数据伦理：本工作使用来自人类细胞图谱（https://www.humancellatlas.org）和Tahoe-100M联盟的公开单细胞数据集。所有HCA组成研究均在适当的捐赠者同意和机构监督下收集，如其原始出版物所述；我们仅进行计算重分析，不引入新的人类受试者数据。HCA数据访问遵循HCA数据门户使用条款。本研究未收集新的患者数据；此二次计算分析无需额外的IRB批准。

## Abstract
In single-cell (sc)-based scientific discovery, text-formatted biomedical prior knowledge and signaling graphs are essential for annotating and interpreting numeric sc-omics data and for generating novel testable hypotheses. A major limitation of existing single-cell large language models (scLLMs) is that they rely on numeric expression data with gene names as the only textual signal, while comprehensive biomedical priors -- cellular localization, gene function, disease associations, and signaling interaction patterns -- remain absent from the model input. We introduce CellTosg2Sequence, a textual-prior- and signaling-graph-augmented cell-omics-sentence language model.

A lightweight heterogeneous graph encoder maps a curated 62,507-node biomedical knowledge graph (KG) into compact virtual tokens that are prepended to each cell sentence, allowing the language model to condition on biological structure with minimal sequence-length overhead. We train CellTosg2Sequence with a three-stage objective: Stage I anchors the KG channel under autoregressive language-model pretraining, leveraging Qwen2.5-32Bs own language reasoning for rapid KG alignment; Stage II aligns labels via supervised fine-tuning with KG-anchored InfoNCE; Stage III applies Group Relative Policy Optimization (GRPO) with an ontology-hierarchy reward, enabling free-generation cell-type prediction that generalizes beyond the closed training vocabulary.

Across multiple benchmarks and ablation experiments, CellTosg2Sequence outperforms strong baselines. All results are achieved with lightweight LoRA training and a single unified checkpoint.

Data ethicsThis work uses publicly available single-cell datasets from the Human Cell Atlas (https://www.humancellatlas.org) and the Tahoe-100M consortium. All HCA constituent studies were collected under appropriate donor consent and institutional oversight as described in their original publications; we perform computational re-analysis only and introduce no new human subjects data. HCA data access follows the HCA Data Portal terms of use. No new patient data are collected in this study; no additional IRB approval is required for this secondary computational analysis.