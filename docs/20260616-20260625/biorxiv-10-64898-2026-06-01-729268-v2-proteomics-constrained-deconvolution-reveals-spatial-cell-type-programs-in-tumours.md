---
title: Proteomics-constrained deconvolution reveals spatial cell-type programs in tumours
title_zh: 蛋白质组学约束下的反卷积揭示肿瘤中的空间细胞类型程序
authors: "Isik, E. B., Haley, M. J., Anbaki, A. A., Bere, L., Roncaroli, F., Piper Hanley, K., Couper, K., Wedge, D. C., Sellers, R., Baker, A., Oliveira, P., Ashton, J., Bristow, R. G., Alvarez, M. A., Georgaka, S., Rattray, M."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.01.729268v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 肿瘤微环境解卷积方法
tldr: 空间转录组学中细胞类型混合物精准解析面临挑战，尤其在肿瘤中缺乏高质量单细胞参考。提出了PISTACHIO框架，利用配对成像质谱流式细胞术施加空间约束，基于负二项似然的非负矩阵分解实现去卷积。在合成和真实肿瘤数据上，PISTACHIO相比于Cell2location和STdeconvolve更准确地恢复空间细胞类型分布，对细胞类型标注错误具有鲁棒性，且运行快速。该方法无需外部单细胞参考，为大规模肿瘤空间转录组分析提供了实用工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有空间转录组去卷积方法依赖高质量单细胞参考或缺乏可扩展性，难以应对缺乏参考的肿瘤异质性场景。
method: 提出PISTACHIO，利用成像质谱流式细胞术导出的空间细胞类型约束，在负二项似然下进行约束非负矩阵分解。
result: 在合成和真实肿瘤数据集上，PISTACHIO的细胞类型分布恢复优于Cell2location和STdeconvolve，且在标签噪声下保持高相关性。
conclusion: PISTACHIO实现了无需单细胞参考的稳健、快速空间转录组去卷积，适用于大规模肿瘤研究。
---

## 摘要
在空间转录组学中准确解析细胞类型混合物仍然具有挑战性，尤其是在异质性肿瘤中，细胞群相互混合，且匹配的单细胞参考可能不可用或对齐不良。当前的反卷积方法要么需要高质量的单细胞RNA测序参考，要么存在可扩展性限制，或者缺乏可解释性。我们提出了PISTACHIO，一个基于蛋白质组学信息的空间转录组反卷积框架，该框架基于约束非负矩阵分解和负二项似然。PISTACHIO不使用概率先验，而是整合了来自配对成像质谱流式细胞术的空间细胞类型约束，强制执行生物基础的稀疏性和细胞类型存在的明确空间可行性。与Cell2location和STdeconvolve相比，PISTACHIO在合成和真实肿瘤数据集上提高了空间细胞类型分布的恢复。我们的方法在细胞类型分配错误下保持稳健，在中等噪声下与真实值保持高相关性，并在标准硬件上实现快速运行，从而实现实际的大规模部署。

## Abstract
Accurately resolving cell-type mixtures in spatial transcriptomics remains challenging, particularly in heterogeneous tumours where cell populations are intermixed and matched single-cell references may be unavailable or poorly aligned. Current deconvolution approaches either require high-quality scRNA-seq references, suffer from scalability limitations, or lack interpretability. We introduce PISTACHIO, a proteomics-informed spatial transcriptomics deconvolution framework based on constrained non-negative matrix factorization with a negative-binomial likelihood. Rather than using probabilistic priors, PISTACHIO incorporates spatial cell-type constraints derived from paired Imaging Mass Cytometry, enforcing biologically grounded sparsity and explicit spatial feasibility of cell-type presence. PISTACHIO improved recovery of spatial cell-type distributions compared with Cell2location and STdeconvolve across synthetic and real tumour datasets. Our approach remains robust under cell-type assignment errors, maintaining high correlation with ground-truth under moderate noise, and achieves fast runtime on standard hardware, enabling practical large-scale deployment.