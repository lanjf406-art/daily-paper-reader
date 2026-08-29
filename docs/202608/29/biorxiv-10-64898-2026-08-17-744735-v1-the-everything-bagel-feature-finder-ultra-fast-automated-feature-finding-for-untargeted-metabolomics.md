---
title: "The Everything Bagel Feature Finder: Ultra-fast automated feature finding for untargeted metabolomics"
title_zh: Everything Bagel 特征查找器：用于非靶向代谢组学的超快速自动化特征查找
authors: "Shin, Y., El Abiead, Y., Jarmusch, A. K., Strobel, M., Abraham, P. E., Thurmon, S., Acharya, D. D., Aron, A., Bilbao, A., Bowen, B. P., Broeckling, C. D., Brown, C. J., Charron-Lamoureux, V., Chen, X., Damiani, T., Doty, A., Du, X., Garg, N., Papadopoulos Lambidis, S., McCall, L.-I., Kirkwood-Donelson, K. I., Northen, T., Prenni, J., Rennie, E. E., Vining, O. B., Wang, C. X., Xiong, Q., Zhao, H. N., Dorrestein, P. C., Petras, D., Phelan, V. V., Wang, M."
date: 2026-08-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.17.744735v1.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 超快速非靶向代谢组学自动特征发现工具
tldr: 代谢组学数据规模激增，现有特征查找工具计算开销大且需手动调参。本文提出Everything Bagel特征查找器，集成特征检测、保留时间对齐与补缺，在八个基准数据集上对比两种自动化方法，性能相当或更优，同时CPU时间最高降低150倍，墙钟时间最高降低113倍。重分析已发表生物标志物数据验证了其生物学有效性，有望支撑数千至数万样本的自动分析。
source: biorxiv
selection_source: fresh_fetch
motivation: 大规模代谢组学数据处理面临特征查找计算瓶颈，现有方法速度慢且需手动参数优化。
method: 设计Everything Bagel超快速自动化特征查找工具，融合特征检测、保留时间对齐与gap filling，优化运行时间和内存效率。
result: 在八个数据集上性能优于或媲美现有方法，CPU时间最高降150倍，墙钟时间最高降113倍，并复现已发表生物标志物发现结果。
conclusion: EB工具可大幅加速大规模非靶向代谢组学数据处理，支持数千至数万样本的自动化分析。
---

## 摘要
代谢组学研究日益应用于数百至数千甚至数万个样本，这要求在保持分析灵敏度或定量准确性的同时，进行快速、自动化的数据处理。一个主要的计算瓶颈是特征查找，即将 LC-MS 和 LC-MS/MS 数据转换为跨样本对齐和定量的分析物信号集合。特征查找可能计算密集，并且通常需要手动迭代参数优化。为了加速这一过程，我们提出了 Everything Bagel (EB) 特征查找器，这是一种超快速的自动化特征查找工具，集成了特征检测、保留时间对齐和间隙填充，专为运行时间和内存效率而设计。我们在八个基准数据集上将 EB 与两种自动化特征查找方法进行了对比。具体来说，我们通过测量加标标准品检测覆盖率、稀释系列定量准确性和酵母 12C/13C 可信特征来评估这三种特征查找方法。在该评估中，EB 特征查找器实现了与现有方法相当甚至常常超越的性能，同时所需 CPU 时间最多降低 150 倍，墙钟时间最多降低 113 倍。我们通过重新分析已发表的用于生物标志物发现的数据集，进一步证明了 EB 的生物分析有效性，并复现了与已发表发现相匹配的生物学显著特征，且无需手动调整特征查找设置。结合速度提升，我们预计 EB 将增强社区自动分析数千至数万样本数据集的能力。

## Abstract
Metabolomics studies are increasingly being applied with hundreds to thousands, even tens of thousands of samples that demand rapid, automated data processing while maintaining analytical sensitivity or quantitative accuracy. A major computational bottleneck is feature finding, which is the transformation of LC-MS and LC-MS/MS data into a set of analyte signals aligned and quantified across samples. Feature finding can be computationally intensive and often requires manual iterative parameter optimization. To accelerate this process, we present the Everything Bagel (EB) feature finder, an ultra-fast automated feature finding tool that integrates feature detection, retention-time alignment, and gap filling designed for run-time and memory efficiency. We benchmarked EB against two automated feature finding methods on eight benchmarking datasets. Specifically, we evaluated these three feature finding methods by measuring spike-in standard detection coverage, dilution series quantification accuracy, and yeast 12C/13C credentialed features. In this evaluation, the EB feature finder achieved performance comparable to, and often exceeding, existing methods while requiring up to 150-fold lower CPU hours and up to 113-fold lower wall time. We further demonstrated the bioanalytical validity of EB by reanalyzing published datasets used for biomarker discovery and reproduced biologically significant features that matched the published findings using manually tuned feature finding settings. Taken along with the speed improvements, we anticipate EB will enhance the ability to automatically analyze datasets with thousands to tens of thousands of samples for the community.