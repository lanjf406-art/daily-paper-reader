---
title: From hotspot dependence to distributed robustness in resistance-aware lead optimization
title_zh: 从热点依赖性到分布式鲁棒性：耐药感知的先导优化
authors: "Wang, Y., Xiao, B., Kang, J., Cui, H., Fu, Y., Li, W., Perea, S. E., Han, W."
date: 2026-06-22
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.16.732538v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 耐药感知的先导药物优化框架，针对靶向癌症治疗
tldr: 药物耐药性是靶向治疗失败的常见原因，传统方法多在化合物选择后才考虑耐药证据。ResistAgent框架通过位点与组合感知的耐药图谱、确定性机制诊断和鲁棒反设计，将突变易损性转化为设计目标。在EGFR-Erlotinib和HIV-RT-Rilpivirine案例中，该方法分离了残留级易损性，优先鲁棒性使支持从热点接触转向分布式网络。该策略提供了补充物理总结和排名基准，保持前瞻性验证边界。
source: biorxiv
selection_source: fresh_fetch
motivation: 将后验的耐药证据转化为先验的设计目标，避免化合物选择后才考虑耐药性。
method: 提出ResistAgent框架，包括位点与组合感知耐药图谱、机制诊断和鲁棒反设计。
result: 在EGFR和HIV案例中，鲁棒优化优先尾部分布，减少热点依赖，转向分布式网络。
conclusion: 实现抗药性先导优化，提供物理总结和排名基准，保留验证边界。
---

## 摘要
耐药性仍然是靶向抗癌和抗病毒治疗中常见的失败模式，而耐药证据往往仅在化合物选择之后才出现。ResistAgent是一个证据约束框架，通过位点感知和组合感知的耐药性映射、确定性机制诊断以及鲁棒性反向设计，将突变风险转化为设计目标。在EGFR-Erlotinib和HIV-RT-Rilpivirine案例中，该框架将残基水平的风险与观察到的HIV联合治疗风险区分开来，并将优先突变与锚点丢失、口袋重排、静电偏移和接触重新分布相关联。在相同预算下的配对搜索表明，鲁棒性目标改变了低尾突变面板行为和相互作用依赖性谱，同时优先考虑鲁棒性而非平均亲和力行为。在预定义的风险面板下，选定的鲁棒最优轨迹将支持从易突变热点接触转向更分布式的相互作用网络。补充的物理摘要和排名优先基准支持了这一耐药感知设计策略的范围，同时为前瞻性验证保留了清晰的边界。

## Abstract
Drug resistance remains a recurrent failure mode in targeted anticancer and antiviral therapy, and resistance evidence often enters only after compound selection. ResistAgent is an evidence-constrained framework that converts mutational liabilities into design-time objectives through site- and combo-aware resistance mapping, deterministic mechanism diagnosis and robust counter-design. In EGFR-Erlotinib and HIV-RT-Rilpivirine, the framework separated residue-level liabilities from observed HIV combination liabilities and linked prioritized mutations to anchor loss, pocket rearrangement, electrostatic shifts and contact redistribution. Same-budget paired searches showed that robust objectives changed lower-tail mutant-panel behavior and interaction-dependence profiles while prioritizing robustness over average-affinity behavior. Under predefined liability panels, selected robust-best trajectories shifted support away from mutable hotspot contacts toward more distributed interaction networks. Supplementary physical summaries and ranking-first benchmarks support the scope of this resistance-aware design strategy while preserving clear boundaries for prospective validation.