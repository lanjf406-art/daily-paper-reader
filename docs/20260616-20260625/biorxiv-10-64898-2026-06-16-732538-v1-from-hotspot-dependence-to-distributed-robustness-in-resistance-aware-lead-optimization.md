---
title: From hotspot dependence to distributed robustness in resistance-aware lead optimization
title_zh: 从热点依赖到分布式鲁棒性：耐药感知的先导化合物优化
authors: "Wang, Y., Xiao, B., Kang, J., Cui, H., Fu, Y., Li, W., Perea, S. E., Han, W."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.16.732538v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: ResistAgent框架直接通过生物信息学和机器学习解决耐药问题
tldr: 药物耐药性常在化合物选择后才发现，导致治疗失败。本文提出ResistAgent框架，通过抗药性映射、机制诊断和鲁棒反向设计，将突变风险转化为设计目标。在EGFR和HIV案例中，该框架识别了关键突变机制，优先考虑鲁棒性而非平均活性，将支撑从热点接触转向分布式网络。该策略为抗药性感知的药物设计提供了验证基础。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有方法在化合物选择后才考虑耐药性，导致设计滞后，需要将耐药性风险提前纳入药物设计目标。
method: 提出ResistAgent框架，包含位点感知的耐药性映射、确定性机制诊断和鲁棒反向设计。
result: 在EGFR-Erlotinib和HIV-RT-Rilpivirine中，鲁棒目标改变了突变体行为，将支持从热点接触转向分布式网络。
conclusion: 通过抗药性感知设计，实现了从热点依赖到分布式鲁棒性的转变，提升了先导化合物的耐药鲁棒性。
---

## 摘要
耐药性仍然是靶向抗癌和抗病毒治疗中反复出现的失败模式，且耐药证据往往仅在化合物筛选后才会出现。ResistAgent是一个证据约束框架，通过位点和组合感知的耐药性映射、确定性机制诊断和鲁棒性逆向设计，将突变风险转化为设计阶段目标。在EGFR-Erlotinib和HIV-RT-Rilpivirine案例中，该框架将残基级别的风险与观察到的HIV组合风险分离，并将优先突变与锚点丢失、口袋重排、静电偏移和接触重新分布联系起来。同预算配对搜索表明，鲁棒性目标改变了低尾突变体面板行为和相互作用依赖特征，同时优先考虑鲁棒性而非平均亲和力行为。在预定义风险面板下，鲁棒性目标轨迹将支撑从可突变热点接触转向更分布式的相互作用网络。附加的物理总结和排名优先基准支持了这种耐药感知设计策略的验证范围。

## Abstract
Drug resistance remains a recurrent failure mode in targeted anticancer and antiviral therapy, and resistance evidence often enters only after compound selection. ResistAgent is an evidence-constrained framework that converts mutational liabilities into design-time objectives through site- and combo-aware resistance mapping, deterministic mechanism diagnosis and robust counter-design. In EGFR-Erlotinib and HIV-RT-Rilpivirine, the framework separated residue-level liabilities from observed HIV combination liabilities and linked prioritized mutations to anchor loss, pocket rearrangement, electrostatic shifts and contact redistribution. Same-budget paired searches showed that robust objectives changed lower-tail mutant-panel behavior and interaction-dependence profiles while prioritizing robustness over average-affinity behavior. Under predefined liability panels, robust-objective trajectories shifted support away from mutable hotspot contacts toward more distributed interaction networks. Supplementary physical summaries and ranking-first benchmarks support the validation envelope of this resistance-aware design strategy.