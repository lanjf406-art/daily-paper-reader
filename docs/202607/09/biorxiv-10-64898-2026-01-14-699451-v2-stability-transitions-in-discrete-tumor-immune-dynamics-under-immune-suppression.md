---
title: Stability Transitions in Discrete Tumor-Immune Dynamics under Immune Suppression
title_zh: 免疫抑制下离散肿瘤-免疫动力学的稳定性转变
authors: "Yoon, N., Scott, J. G., Cho, Y.-B."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.01.14.699451v2.full.pdf"
tags: ["query:neo-resist"]
score: 6.0
evidence: 肿瘤-免疫动力学数学模型分析免疫逃逸
tldr: 肿瘤免疫相互作用中，免疫逃逸是治疗失败的关键。本研究通过离散时间模型模拟癌症-免疫循环，引入免疫抑制参数（如PD-1/PD-L1通路）。利用雅可比矩阵的迹和行列式进行局部稳定性分析，发现系统在弱免疫条件下出现鞍结分岔导致平衡态消失；强免疫条件下稳定螺旋平衡变为不稳定螺旋，失去肿瘤控制能力。参数范围内无稳定极限环，强调维持平衡稳定性是实现有效免疫抑制的核心。该工作为区分平衡存在与有效肿瘤控制提供了数学框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 理解肿瘤免疫逃逸的动态机制，为改善免疫治疗策略提供理论基础。
method: 构建离散时间肿瘤-免疫模型，基于雅可比矩阵的迹和行列式进行局部稳定性与分岔分析。
result: 系统出现鞍结分岔和稳定性转变，稳定螺旋平衡变为不稳定螺旋，且无稳定非平衡吸引子。
conclusion: 维持平衡态稳定性对免疫介导的肿瘤控制至关重要，该框架有助于区分平衡存在与有效控制。
---

## 摘要
尽管癌症免疫治疗取得了重大进展，但许多患者仍经历免疫逃逸和疾病进展。因此，理解控制肿瘤控制与免疫逃逸之间转变的动态机制对于改进治疗策略至关重要。分岔理论和稳定性分析提供了数学框架，用于解释逐渐的参数变化如何导致生物系统中的突然定性转变。在肿瘤-免疫相互作用的背景下，这种转变可能对应于分隔免疫限制的肿瘤控制与免疫逃逸行为的关键阈值。

在本研究中，我们研究了癌症-免疫循环的离散时间模型，基于雅可比矩阵的迹和行列式对系统平衡点进行局部稳定性分析。该模型通过一个代表肿瘤介导免疫逃逸的参数来纳入免疫抑制，包括与免疫检查点通路（如PD-1/PD-L1信号）相关的机制。在弱免疫条件下，系统表现出鞍结分岔，与非平凡平衡点的出现和消失相关。此外，在强免疫条件下，模型显示出明显的稳定性转变，其中稳定的螺旋平衡点（螺旋汇）失去稳定性并变为不稳定的螺旋（螺旋源），导致在平衡点消失之前失去稳定的肿瘤控制动力学。

额外的数学分析和数值研究表明，在所考虑的参数范围内，系统不会产生稳定的非平衡吸引子，如极限环。因此，稳定平衡点仍然是模型中唯一的稳定吸引子，强调了维持平衡稳定性对于有效的免疫介导肿瘤抑制的重要性。此外，进一步的参数分析表明，在分岔边界附近，平衡点的存在性和稳定性都非常敏感，反映了肿瘤增殖与免疫激活之间的微妙平衡。

总体而言，这项工作为在离散肿瘤-免疫系统中区分平衡点存在性与有效肿瘤控制提供了数学框架。除了所考虑的具体模型外，结果强调了稳定性分析在理解免疫逃逸中的重要性，并可能有助于未来自适应和个性化免疫治疗建模的方法。

## Abstract
Despite major advances in cancer immunotherapy, many patients still experience immune escape and disease progression. Understanding the dynamical mechanisms governing the transition between tumor control and immune escape is therefore essential for improving therapeutic strategies. Bifurcation theory and stability analysis provide a mathematical framework for explaining how gradual parameter changes can produce sudden qualitative transitions in biological systems. In the context of tumor-immune interactions, such transitions may correspond to critical thresholds separating immune-limited tumor control from immune-escape behavior.

In this study, we investigate a discrete-time model of the cancer-immunity cycle applying the local stability analysis to the system equilibria based on the trace and determinant of the Jacobian matrices. The model incorporates immune suppression through a parameter representing tumor-mediated immune evasion, including mechanisms related to immune checkpoint pathways such as PD-1/PD-L1 signaling. The system exhibits a saddle-node bifurcation associated with the appearance and disappearance of nontrivial equilibria, under weak immune conditions. In addition, under strong immune conditions, the model demonstrates a distinct stability transition in which a stable spiral equilibrium (spiral sink) loses stability and becomes an unstable spiral (spiral source), resulting in the loss of stable tumor-control dynamics before equilibrium disappearance occurs.

Additional mathematical analysis and numerical investigations indicate that the system does not generate stable non-equilibrium attractors such as limit cycles over the parameter ranges considered. Consequently, the stable equilibrium remains the only stable attractor in the model, emphasizing the importance of maintaining equilibrium stability for effective immune-mediated tumor suppression. Also, further parameter analyses reveal that both equilibrium existence and stability are highly sensitive near bifurcation boundaries, reflecting the delicate balance between tumor proliferation and immune activation.

Overall, this work provides a mathematical framework for distinguishing equilibrium existence from effective tumor control in discrete tumor-immune systems. Beyond the specific model considered, the results highlight the importance of stability analysis in understanding immune escape and may contribute to future approaches in adaptive and personalized immunotherapy modeling.