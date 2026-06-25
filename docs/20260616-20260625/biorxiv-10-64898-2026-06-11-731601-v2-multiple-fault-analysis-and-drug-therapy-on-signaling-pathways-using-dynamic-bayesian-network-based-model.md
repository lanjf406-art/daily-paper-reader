---
title: Multiple Fault Analysis and Drug Therapy on Signaling Pathways Using Dynamic Bayesian Network-based Model
title_zh: 基于动态贝叶斯网络的信号通路多重故障分析与药物治疗
authors: "Chowdhury, T., Majumder, S., Lodh, E., Maitra, A., Agarwal, A., Sur, A., Sarkar, S."
date: 2026-06-18
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.11.731601v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 动态贝叶斯网络模型用于信号通路多故障分析与药物治疗，可用于耐药研究
tldr: 癌症信号通路常因多分子异常共激活而失调。本文提出基于动态贝叶斯网络的概率模型，用软逻辑规则模拟通路组件激活概率传播，系统评估一至四重故障下的信号输出。在生长因子和MAPK通路中，负担随故障数增加，U0126+LY294002+Temsirolimus组合在低负担下实现高效率，并发现ERK1/2+RPS6KB1等新靶点对。该框架为通路多故障分析与干预排序提供了可解释可扩展的概率方法。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有信号通路模型多处理单一故障，缺乏对多分子同时失调下异常激活及药物干预策略的系统概率分析。
method: 构建动态贝叶斯网络，用软逻辑更新规则传播激活概率，计算编码负担评分与效率评分，结合帕累托分析和双靶点搜索。
result: U0126+LY294002+Temsirolimus是已知最优低负担组合，自定义搜索发现ERK1/2+RPS6KB1与Raf+MEK1为高影响靶点对。
conclusion: 框架可解释性强、扩展性高，能有效量化多故障影响并优先排序药物干预，适用于其他信号通路分析。
---

## 摘要
癌症相关信号通路通常在多个分子组分同时失调时表现出异常激活。本研究提出了一种基于概率时序动态贝叶斯网络（DBN）的框架，用于分析生长因子（GF）和丝裂原活化蛋白激酶（MAPK）信号通路中的多重故障行为及干预响应。与确定性布尔传播不同，该模型通过激活概率表示每个通路组分，并利用软逻辑更新规则在离散时间步长上传播这些概率。在共同的最小负荷输入向量下，系统评估了单故障、双故障、三故障和四故障场景。使用编码的通路负荷分数汇总输出概率，并通过相对于无干预基线的效率分数对已知药物组合进行排序。进一步采用帕累托分析平衡干预效率与药物向量负荷，同时执行自定义双靶点搜索以识别超出预定药物靶点的计算干预假设。结果表明，两条通路中编码负荷随故障阶数增加，MAPK产生的基线负荷高于GF。在已知药物向量中，U0126+LY294002+Temsirolimus始终是最强的低负荷候选方案，其效率接近最大六药物向量。自定义双靶点分析确定GF通路中的ERK1/2+RPS6KB1和MAPK通路中的Raf+MEK1为高影响计算靶点对。运行时基准测试显示，批量向量化NumPy执行显著提高了高阶故障模拟的可扩展性。总体而言，该框架为概率性通路级故障分析和干预优先级排序提供了一种可解释且可扩展的方法。

## Abstract
Cancer-associated signaling pathways often exhibit abnormal activation under simultaneous dysregulation of multiple molecular components. This study presents a probabilistic temporal Dynamic Bayesian Network (DBN)-based framework for analyzing multi-fault behaviour and intervention response in Growth Factor (GF) and Mitogen-Activated Protein Kinase (MAPK) signaling pathways. Unlike deterministic Boolean propagation, the proposed model represents each pathway component through an activation probability and propagates these probabilities over discrete time steps using soft-logic update rules. One-, two-, three-, and four-fault scenarios were systematically evaluated under a common lowest-burden input vector. The resulting output probabilities were summarized using an encoded pathway-burden score, and known-drug combinations were ranked using efficiency scores relative to no-intervention baselines. Pareto analysis was further used to balance intervention efficiency against drug-vector burden, while a custom dual-target search was performed to identify computational intervention hypotheses beyond predefined drug targets. Results showed that encoded burden increased with fault order in both pathways, with MAPK producing a higher baseline burden than GF. Among known-drug vectors, U0126+LY294002+Temsirolimus consistently emerged as the strongest low-burden candidate, achieving efficiency close to the maximum six-drug vector. Custom dual-target analysis identified ERK1/2+RPS6KB1 in GF and Raf+MEK1 in MAPK as high-impact computational target pairs. Runtime benchmarking showed that batched vectorized NumPy execution substantially improved scalability for higher-order fault simulations. Overall, the framework provides an interpretable and scalable approach for probabilistic pathway-level fault analysis and intervention prioritization.