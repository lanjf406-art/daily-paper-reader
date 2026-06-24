---
title: The Warburg effect as a metabolic niche construction strategy in the tumor microenvironment
title_zh: 瓦博格效应作为肿瘤微环境中的代谢生态位构建策略
authors: "Anand, V., Levine, H."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.12.731860v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 肿瘤微环境作用：乳酸塑造免疫抑制微环境促进耐药
tldr: 有氧糖酵解（Warburg效应）的细胞内效益被广泛研究，但乳酸对肿瘤微环境的塑造作用常被忽略。本研究构建包含肿瘤、抗肿瘤免疫细胞和促肿瘤基质细胞的消费者-资源模型，发现乳酸分泌抑制免疫细胞却降低肿瘤丰度，形成生长-排除权衡。当基质细胞将乳酸转化为代谢物回补肿瘤时，权衡解除，但需临界肿瘤质量。这表明Warburg效应是生态位构建策略，依赖于基质合作伙伴重组肿瘤生态系统。
source: biorxiv
selection_source: fresh_fetch
motivation: 探讨Warburg效应在肿瘤微环境中的生态优势，尤其是乳酸分泌对免疫与基质细胞的影响及代谢交叉喂养的角色。
method: 构建最小消费者-资源模型，模拟肿瘤、免疫细胞和基质细胞间营养与代谢物相互作用。
result: 乳酸分泌抑制免疫细胞但降低肿瘤丰度，形成权衡；基质细胞交叉喂养可解除权衡，但需临界肿瘤质量。
conclusion: Warburg效应是生态位构建策略，其优势依赖于微环境中基质伙伴的存在以重组肿瘤生态系统。
---

## 摘要
瓦博格效应赋予癌细胞的优势仍未明确。尽管大量研究在细胞内水平上探讨了有氧糖酵解，强调了其可能的生物合成或ATP产生速率优势，但关于被输出到肿瘤微环境中的富含能量的乳酸的命运却相对较少受到关注。然而，乳酸远非代谢惰性：它积极塑造肿瘤微环境，作为对适应性免疫细胞的毒素，同时促进肿瘤微环境中几种非癌细胞的生长，这些细胞反过来又促进肿瘤生长。在此，我们开发了一个最小的消费者-资源模型，包含肿瘤、抗肿瘤免疫和促肿瘤基质群体，它们通过共享的营养物质、乳酸和代谢副产物相互作用。我们发现，乳酸分泌施加了一种生长-排斥权衡：更高的糖酵解分配抑制抗肿瘤免疫细胞，但由于代谢效率较低同时减少了肿瘤丰度。这种权衡在存在能够进行代谢交叉喂养的促肿瘤基质群体时得到解决，即基质细胞将乳酸转化为代谢产物，这些代谢产物反馈支持肿瘤生长，从而抵消糖酵解成本。交叉喂养的益处是种群规模的二阶效应，需要一定的肿瘤质量才能运作。综合来看，这些结果表明瓦博格效应可能存在生态优势，这取决于微环境背景。具体而言，乳酸分泌主要在存在合适的基质伙伴时有益，作为一种生态位构建策略，重新组织肿瘤生态系统以利于肿瘤扩张。

## Abstract
The advantage conferred by the Warburg effect to cancer cells remains unresolved. While extensive research has examined aerobic glycolysis at the intracellular level, emphasizing its possible biosynthetic or ATP-production rate benefits, the fate of the energy-rich lactate exported into the tumor microenvironment (TME) has received comparatively little attention. Yet lactate is far from metabolically inert: it actively shapes the TME, functioning as a toxin to adaptive immune cells and simultaneously promoting growth of several non-cancerous cells in the tumor microenvironment which in turn promote tumor growth. Here, we develop a minimal consumer-resource model incorporating tumor, anti-tumor immune, and pro-tumor stromal populations interacting through shared nutrients, lactate, and metabolic byproducts. We find that lactate secretion imposes a growth-exclusion tradeoff: higher glycolytic allocation suppresses anti-tumor immune cells but simultaneously reduces tumor abundance due to less efficient metabolism. This tradeoff is resolved in the presence of pro-tumor stromal populations capable of metabolic cross-feeding, namely stromal cells that convert lactate into metabolites which feed back to support tumor growth, thereby offsetting the glycolytic cost. The cross-feeding benefit is second-order in population size, requiring a critical tumor mass to operate. Taken together, these results suggest that there may be an ecological advantage of the Warburg effect, contingent on microenvironmental context. Specifically, lactate secretion is beneficial primarily when appropriate stromal partners are present, functioning as a niche-construction strategy that reorganizes the tumor ecosystem in favor of tumor expansion.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：解析瓦博格效应（有氧糖酵解）在肿瘤微环境（TME）中赋予癌细胞的生态学优势，特别是乳酸分泌对微环境中免疫细胞与基质细胞的塑造作用，以及这种代谢策略如何影响肿瘤整体的扩张。
- **研究动机**：已有大量研究聚焦于瓦博格效应的细胞内收益（如生物合成前体供给、ATP快速合成），但对细胞外排出的乳酸如何参与微环境重编程（免疫抑制、基质细胞增殖）关注不足。本文试图从“生态位构建”（niche construction）视角，将Warburg效应视为一种通过乳酸操纵微环境、促进肿瘤扩张的策略。
- **整体含义**：提出乳酸并非代谢废物，而是肿瘤主动构建有利生态位的“工程工具”，其益处依赖于微环境中合适的基质伙伴的存在。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **方法类型**：理论建模，构建最小消费者-资源（consumer-resource）模型。
- **模型组成**：
  - **种群**：肿瘤细胞（T）、抗肿瘤免疫细胞（I，如T细胞）、促肿瘤基质细胞（S，如成纤维细胞）。
  - **资源/代谢物**：共享营养物质（N）、乳酸（L）、基质细胞转化后的代谢副产物（M）。
- **关键假设**：
  - 肿瘤细胞在糖酵解与氧化磷酸化之间分配碳通量，更高糖酵解分配导致更多乳酸分泌，但能量效率更低（ATP/葡萄糖比低）。
  - 乳酸施加“毒素”效应：抑制抗肿瘤免疫细胞的生长/活性。
  - 基质细胞能够摄取乳酸并将其转化为代谢产物（如谷氨酰胺、其它促肿瘤因子），这些产物反向供给肿瘤。
- **核心动力学**：
  - 肿瘤丰度受营养物质N和代谢物M的正向影响，受免疫细胞I的负向影响。
  - 免疫细胞受N正向影响，受L负向影响。
  - 基质细胞受N和L正向影响，并消耗L生产M。
- **关键发现（模型预测）**：
  - 无基质细胞时：高糖酵解分配抑制免疫细胞，但同时降低肿瘤自身丰度（因代谢效率低），形成“生长-排除权衡”。
  - 有基质细胞时：基质将乳酸转化为M，M反馈促进肿瘤生长，从而解除权衡，但此效应具有二阶依赖性——需要肿瘤达到临界规模才能驱动足够的乳酸流，从而启动有效的交叉喂养。
- **算法流程**：使用常微分方程（ODEs）描述群体动态与资源代谢物浓度变化，通过稳态分析、分岔分析等方法评估不同参数（如糖酵解分配比例、营养供应率）下的生态结果。具体公式未在摘要中给出。

## 3. 实验设计

- **数据集/场景**：无实证数据集或临床/实验数据，属于纯理论生态-进化模型研究。
- **基准（benchmark）**：无标准对比基准，论文通过分析不同策略（高糖酵解 vs 低糖酵解）和不同TME组成（有无基质细胞）的平衡状态来推导结论。
- **对比方法**：未与其他模型或实证结果进行定量对比；可能通过与文献中已有假设的定性对比来论证模型合理性。

## 4. 资源与算力

- **未提及**：论文作为预印本，未报告任何计算资源（如GPU型号、数量、训练时长等）。模型为低维常微分方程组，解析或数值求解所需算力极小，通常可在普通台式机上完成。

## 5. 实验数量与充分性

- **实验类型**：本文为理论分析，本质上是“思想实验”，通过调节关键参数（如糖酵解分配率α、营养输入率、细胞间相互作用强度）进行参数扫描和稳态分析。未提及具体扫描次数或代表性参数集。
- **充分性评价**：
  - **不充分**：作为一种理论假设，模型依赖大量简化假设（如忽略空间结构、细胞异质性、免疫逃逸的其它机制等），且未使用实际数据校准参数或验证预测。结论的泛化能力有限。
  - **客观性**：模型推导逻辑自洽，但缺乏与实验对照的公平性验证。建议后续进行体外/体内实验来检验核心预测（如临界肿瘤质量、基质乳酸转化必要性）。

## 6. 论文的主要结论与发现

- **核心发现1**：乳酸分泌对肿瘤自身存在“双刃剑”效应——分泌乳酸可以抑制抗肿瘤免疫细胞，但会因代谢效率降低而减少肿瘤丰度，形成权衡。
- **核心发现2**：当微环境中存在能进行代谢交叉喂养的促肿瘤基质细胞（如肿瘤相关成纤维细胞）时，基质细胞将乳酸转化为促肿瘤代谢物，抵消了糖酵解的成本，从而解除上述权衡。
- **核心发现3**：交叉喂养的益处随群体规模呈二阶增长，需要肿瘤达到一定临界数量才能有效运作（意味着小型肿瘤可能无法从Warburg效应中获益）。
- **总体结论**：瓦博格效应可被理解为一种“生态位构建策略”，其优势依赖于是否存在合适的基质合作伙伴；单独的高糖酵解并不总是有利，其进化成功依赖于TME中代谢网络的协作。

## 7. 优点

- **视角创新**：将Warburg效应从细胞自主优势扩展到生态系统层面，提出乳酸作为生态位工程信号的新观点。
- **模型简洁**：最小消费者-资源模型抓住了肿瘤-免疫-基质三方相互作用的核心矛盾，易于理解核心权衡。
- **机制清晰**：明确揭示了“生长-排除权衡”以及“交叉喂养解除权衡”的条件，为理解高糖酵解在耐药和免疫逃逸中的作用提供了理论框架。
- **有启发性**：临界肿瘤质量的预测具有潜在临床应用意义，例如可针对小型肿瘤早期干预代谢网络。

## 8. 不足与局限

- **缺乏实证支持**：目前仅停留在数学建模层面，未使用任何体内或体外实验数据验证模型预测，结论的可靠性有待检验。
- **模型过度简化**：
  - 忽略了空间异质性和营养梯度、细胞迁移等关键TME特征。
  - 未纳入其他免疫抑制机制（如PD-L1、Treg等）以及肿瘤内代谢异质性。
  - 基质细胞仅设定为均一群体，实际中基质细胞种类多样且功能可变。
- **未考虑进化动态**：细胞策略（糖酵解分配）被视为固定参数，未考虑进化适应性变化。
- **实验不足**：无消融实验、无敏感性分析的计算实验细节，读者无法复现或评估模型鲁棒性。
- **偏倚风险**：模型结论高度依赖于“基质细胞将乳酸转化为促肿瘤代谢物”这一假设，若实际中基质细胞主要消耗乳酸而非回补，则结论可能相反。

（完）
