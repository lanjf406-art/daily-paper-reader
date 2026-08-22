---
title: A permutation-free family-wise error rate for the moderated top-gene scan under gene correlation
title_zh: 基因相关性下调节的顶部基因扫描的免置换族系错误率
authors: "Dwyer, W. J."
date: 2026-08-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.17.745282v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 免置换的差异表达全基因组家族错误率控制方法，可用于药物耐药转录组分析
tldr: 差异表达扫描报告最大调整t统计量，基因相关性使传统置换法复杂，且经验贝叶斯先验自由度被高估导致错误率膨胀。本文通过误差分解发现相关性主要破坏先验自由度，提出用无调参谱U统计量校正方差扩散，无需置换即可将全族错误率保持在独立基线且功效不降，并给出稳定性指标指导何时必须置换。
source: biorxiv
selection_source: fresh_fetch
motivation: 基因相关性下控制调整t统计量最大值的全族错误率通常依赖置换，且相关性使经验贝叶斯先验失效，需明确其宽松机制。
method: 通过错误预算消融归因，提出谱U统计量估计平均平方相关，并用其校正样本方差离散度，避免置换。
result: 无需置换即可将错误率控制在独立基因小样本基线，同时保持检验功效。
conclusion: 相关性并非独立障碍，校正先验自由度即可；同时提供决策指标以在严重共表达时回退到置换。
---

## 摘要
一个差异表达扫描报告具有最大调节t统计量的基因，因此控制族系错误率意味着控制基因间最大统计量的零分布。在基因相关性下，人们普遍认为这需要置换检验，因为相关性改变了有效多重性，并破坏了调节t统计量背后的经验贝叶斯方差先验。我们通过误差预算消融分解了这种宽松性，并表明在模拟模型类别中，它主要归结为经验贝叶斯先验自由度的膨胀：用真实先验替换后，族系错误率回到独立基因小样本基线，因此一旦先验正确，依赖性不会构成单独的障碍。相关性压缩了对数样本方差的跨基因离散度；因为先验自由度随该离散度减小，所以先验被高估，调节的最大值变得宽松。将观察到的离散度除以一减去平均平方基因相关性（通过具有无偏迹目标的免调谐谱U统计量估计），可逆转该机制，并在无需置换的情况下将族系错误率保持在基线附近，同时保持统计功效。一个可观察的不稳定性指数可标记何时严重的共表达应让位于置换检验。

## Abstract
A differential-expression scan reports the genes with the largest moderated t-statistics, so controlling the family-wise error rate means controlling the null distribution of the maximum statistic over genes. Under gene correlation this is widely believed to require permutation, because correlation changes the effective multiplicity and corrupts the empirical-Bayes variance prior behind the moderated t-statistic. We decompose that liberality by an error-budget ablation and show that, within the simulated model class, it reduces principally to an inflation of the empirical-Bayes prior degrees of freedom: substituting the true prior returns the family-wise error to the independent-gene small-sample baseline, so dependence imposes no separate barrier once the prior is correct. Correlation deflates the cross-gene spread of the log sample variances; because the prior degrees of freedom decreases in that spread, the prior is over-estimated and the moderated maximum turns liberal. Dividing the observed spread by one minus the mean squared gene correlation, estimated by a tuning-free spectral U-statistic with an unbiased trace target, reverses the mechanism and holds the family-wise error near the baseline at retained power without permutation. An observable instability index flags when severe co-expression should defer to permutation.