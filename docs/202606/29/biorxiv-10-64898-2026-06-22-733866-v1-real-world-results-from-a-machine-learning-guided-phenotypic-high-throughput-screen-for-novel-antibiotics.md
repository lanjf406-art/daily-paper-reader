---
title: "Real-world results from a Machine Learning-guided, phenotypic High-Throughput Screen for novel antibiotics"
title_zh: 基于机器学习指导的表型高通量筛选新型抗生素的真实世界结果
authors: "Lukacs, P., Hare, K. C., George, S., Hone, G., Gollapudi, G., Wang Jarantow, L., Pellegrino, J., Miller, A., Thorn, K. S."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.22.733866v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 机器学习引导的抗生素高通量筛选，与耐药预测框架相关
tldr: 抗生素耐药性威胁全球健康，机器学习（ML）可提升高通量筛选（HTS）效率。本研究利用大规模Learning-to-Rank模型，基于公开和私有数据训练，针对E. coli的lptD-突变体进行表型抑制筛选，同时最小化人细胞毒性。结果发现，ML引导的筛选使命中率翻倍、毒性命中减少3倍，且对结构新颖化合物预测稳健。该研究结合大规模HTS、ML创新及文库选择和精选策略，为抗生素发现提供了新范式。
source: biorxiv
selection_source: fresh_fetch
motivation: 抗生素耐药性日益严重，传统HTS效率低且毒性高，需ML提升筛选精准度，加速发现新型抗生素。
method: 训练Learning-to-Rank模型，基于公开和私有数据优化抑制与毒性；筛选预平板库和精选结构新颖化合物，针对E. coli lptD-突变体，进行命中确认、毒性反筛及MOA确定。
result: ML引导筛选使命中率翻倍，毒性命中减少3倍；对野生型和突变体活性均提升；模型对结构不相似化合物预测能力强。
conclusion: ML引导的高通量筛选结合文库与精选策略，显著提高抗生素发现效率，为应对耐药性提供有效工具。
---

## 摘要
抗菌素耐药性是一个紧迫的全球健康威胁，在美国每年有超过280万例多重耐药感染导致超过3.5万人死亡。机器学习已成为提高抗生素高通量筛选效率的潜在解决方案。我们报告了针对大肠杆菌的机器学习指导的高通量筛选。利用大规模学习排序模型，在公共和专有数据集上训练，以最大化表型抑制并最小化人类细胞毒性。我们评估了几个预铺板的化合物库和一组“精心挑选”的结构新颖的化合物。我们针对高渗透性lptD-突变体进行筛选，随后进行命中确认、分析、细胞毒性反筛选和作用机制测定。结果表明，命中率翻倍，毒性命中减少3倍。此外，对野生型大肠杆菌和lptD-突变体的活性均有所提高。机器学习模型对结构不相似的化合物展现出强大的预测能力。大规模高通量筛选、机器学习创新以及文库选择和精心挑选策略的结合，使这项研究在抗生素发现领域中脱颖而出。

## Abstract
Antimicrobial resistance is an urgent global health threat, with over 2.8 million multidrug-resistant infections killing over 35,000 annually in the US. Machine Learning (ML) has emerged as a potential solution to improve efficiency of antibiotic high-throughput screens (HTS). We report ML-guided high-throughput screening against E. coli. Large-scale Learning-to-Rank models were trained on public and proprietary datasets to maximize phenotypic inhibition and minimize human cell cytotoxicity. We evaluated several pre-plated compound libraries and a set of "cherry-picked", structurally novel compounds. We screened against a hyperpermeable lptD- mutant, followed by hit confirmation, profiling, cytotoxicity counter-screening, and MOA determination. Results demonstrated a doubled hit rate and 3X fewer toxic hits. Additionally, activity improved against both Wild Type E. coli and the lptD- mutant. ML models showed robust predictive power on structurally dissimilar compounds. The combination of large-scale HTS, ML innovation, and both library-wise selection and cherry-picking strategies distinguishes this study in the antibiotic discovery field.