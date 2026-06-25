---
title: "Pillbox: A Leakage-Aware Foundation-Model Predictor and Lineage-Ceiling Diagnostic for Cancer Drug Response"
title_zh: Pillbox：一种泄漏感知的基础模型预测器及癌症药物反应谱系上限诊断方法
authors: "Hill, J. J. K., Jiao, E., Singh, S., Ghanta, A., Anders, D., Jeong, J., Ryoo, H. J."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.08.725572v2.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 机器学习预测癌症药物反应，直接相关于耐药预测
tldr: 癌症药物反应预测常受数据泄漏和组织谱系主导效应影响。Pillbox结合CpGPT甲基化嵌入、CLAMP药物嵌入和基因表达主成分，通过FiLM条件图注意力融合在STRING PPI图上，并集成梯度提升回归器。在GDSC数据集上，随机、组织盲和部位盲分割的R²分别达0.78、0.77和0.76，细胞感知提升超过药物均值基线。提出的交叉架构残差相关诊断定量揭示架构选择仍有约0.03的提升空间，跨屏幕验证与PRISM测量重复性上限接近，表明基础模型嵌入已捕获主要信号。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有预测器易受数据泄漏影响，且组织谱系主导细胞系响应，需要泄漏感知和定量诊断架构饱和度的预测器。
method: Pillbox融合CpGPT甲基化嵌入、CLAMP药物嵌入和基因表达PC，通过FiLM条件图注意力在STRING PPI图上，并集成梯度提升回归器；提出交叉架构残差相关诊断。
result: GDSC上随机/组织盲/部位盲分割R²为0.78/0.77/0.76，细胞感知提升≥0.037；跨屏幕验证与PRISM的Spearman相关性达测量重复性上限（相差<0.01）。
conclusion: 基础模型嵌入已饱和大部分预测信号，架构选择仍提供小但可测量的改进空间，谱系效应主导响应，泄漏防控有效。
---

## 摘要
我们提出Pillbox，一个预测器，其流程针对六种Asiaee泄漏模式进行了审计，并通过每折消融实验发现有一条残留通路在硬分割任务中不承担负载。我们的模型结合了CpGPT甲基化嵌入、CLAMP药物嵌入以及每折拟合的基因表达主成分，这些成分通过特征级线性调制（FiLM）条件化的图注意力机制在STRING v12蛋白质-蛋白质相互作用图上融合。然后，我们将该模型与基于直方图的梯度提升回归基线进行集成。在GDSC GSE68379数据集（987个细胞系，375种药物）上，使用种子42、7和123，集成模型在随机、组织学盲和位点盲分割上的测试R²分别为0.78、0.77和0.76，细胞感知提升相对于药物均值基线分别为+0.054、+0.060和+0.037。作为特征堆栈饱和度的定量诊断，我们提出了跨架构残差相关性，并以同架构不同初始化组作为对照进行校准。在组织学盲分割上，跨架构残差相关性值为0.939，低于同架构上限0.974约0.03，我们将这一差距解释为在当前基础模型表示之上架构选择可用的提升空间，并与长期以来的观察一致，即组织谱系主导细胞系药物反应。我们整合了精选的突变、甲基化和药物靶点表达通道，但在基础模型嵌入到位后，这些并未改善预测。针对PRISM的跨屏幕验证与GDSC到PRISM的测量可重复性上限在0.01 Spearman范围内匹配。

## Abstract
We present Pillbox, a predictor whose pipeline is audited against the six Asiaee leakage modes with the one residual pathway shown by per-fold ablation to be non-load-bearing on hard splits. Our model combines CpGPT methylation embeddings, CLAMP drug embeddings, and per-fold-fit gene-expression principal components which are fused by Feature-wise Linear Modulation (FiLM)-conditioned graph attention on the STRING v12 protein-protein interaction graph. Then we -ensemble the model against a histogram-based gradient boosting regressor baseline. On GDSC GSE68379 (987 cell lines, 375 drugs) across seeds 42, 7, and 123, the ensemble reaches test R2 of 0.78, 0.77, and 0.76 on random, histology-blind, and site-blind splits respectively, with cell-aware lifts above the drug-mean floor of +0.054, +0.060, and +0.037. As a quantitative diagnostic for feature-stack saturation we propose the cross-architecture residual correlation, calibrated against a same-architecture-different-initialization control. On histology-blind splits the cross-architecture value of 0.939 falls short of the same-architecture ceiling of 0.974 by approximately 0.03 in residual correlation, a gap we interpret as the headroom available to architecture choice on top of the current foundation-model representation and consistent with the long-established observation that tissue lineage dominates cell-line drug response. We integrated curated mutation, methylation, and drug-target-expression channels, but these do not improve prediction once foundation-model embeddings are in place. Cross-screen validation against PRISM matches the GDSC-to-PRISM measurement reproducibility ceiling within 0.01 Spearman.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：癌症细胞系药物反应预测是一个长期存在的药理学问题，但现有方法普遍存在严重的数据泄漏（data leakage）问题。最近的审计显示，32篇被引超过3000次的方法中有23篇存在数据泄漏，泄漏修复后平均均方误差上升16.6%。此外，组织谱系（tissue lineage）对预测信号的贡献远大于细胞特异性信号，多数方法的绝对性能被药物均值基线（DummyDrugAvg）所掩盖。
- **研究动机**：提供一个泄漏审计清洁（leakage-aware）的预测器，明确验证对六种Asiaee泄漏模式的防控；填补现有清洁方法中缺少同时使用甲基化基础模型和药物基础模型、且在组织盲硬分割下进行多种子验证的空白；提出一个定量诊断指标来衡量特征堆栈（feature stack）的饱和程度；报告一个重要的负结果：在基础模型嵌入已到位后，精心挑选的生物学先验（突变、甲基化、药物靶点表达）不再提升聚合R²。
- **整体含义**：该工作强调，在癌症药物反应预测中，一旦泄漏被控制、基线设为药物均值，细胞感知贡献非常小（约0.04–0.06 R²）。大部分可预测方差由组织谱系编码在基础模型表示中，架构选择仅提供很小的提升空间（约0.03残差相关差距）。这迫使领域重新关注表示质量而非架构复杂度，并提醒审稿人需重视泄漏审计。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：结合两个冻结的基础模型（CpGPT甲基化嵌入和CLAMP药物嵌入）与每折拟合的基因表达主成分（PCA-128），通过特征级线性调制（FiLM）条件化的图注意力网络（GAT）在STRING v12蛋白质相互作用图上融合，再与基于直方图的梯度提升回归器（HGBR）进行α集成。
- **关键技术细节**：
  - **细胞侧编码器**：CpGPT（100M参数，冻结）输出512维细胞嵌入；基因表达经标准化和每折PCA得到128维；两者作为基因节点特征（129维：表达值+PCA载荷），在包含5000个基因节点、21558条高置信度边的STRING v12图上运行3层4头GAT，最后通过20个k-means模块池化得到细胞表示。
  - **药物侧编码器**：CLAMP（冻结）输出768维药物嵌入，经过一个小型MLP（768→256→128），再通过一个γ,β预测头产生与细胞表示匹配的FiLM调制参数γ和β（各1280维），初始化为γ=1, β=0以保持恒等映射。
  - **融合**：调制后的细胞表示 c′ = γ ⊙ c + β，然后经过融合MLP（256维）输出Arch I预测。
  - **α集成**：在每折验证集上通过闭式一维最小二乘拟合标量α，使y_pred = α·y_ArchI + (1−α)·y_HGBR，α落在[0.2,0.8]区间内表明两个模型均有贡献。
  - **泄漏防控**：严格按折预处理（StandardScaler、PCA、RobustScaler均在训练折内拟合）；超参数固定；早期停止仅使用验证MSE；CpGPT预训练语料与GSE68379无交集（作者确认）；报告折均值R²而非合并后算R²；无测试集最优点选择。
  - **相似度增强正则化**：在训练时，将部分细胞输入替换为其表达空间中5个近邻的凸组合（权重0.5），仅作为正则化，推理时不使用。
- **算法流程**：输入（细胞甲基化、基因表达、药物SMILES）→ CpGPT/CLAMP/Gene Expression PCA → GAT + FiLM → Arch I预测；同时HGBR在相同的1,408维特征向量上训练 → α集成 → 最终ln(IC50)预测。

### 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **数据集**：
  - **主要训练/评估**：GDSC1面板，包含987个癌症细胞系、38种GDSC组织学类别、13个解剖原发部位。保留375种至少有100个细胞系IC50测量的化合物。标签矩阵稀疏，有效占87.5%（295,641个细胞-药物对）。
  - **甲基化**：GSE68379（Illumina HumanMethylation450K芯片），保留前10,000个高方差CpG位点（无监督于IC50）。
  - **基因表达**：RMA归一化的GDSC微阵列数据，保留5,000个最可变基因，每折标准化后PCA降维至128。
  - **外部验证**：PRISM Repurposing Secondary Screen（跨屏幕验证）。
  - **精选生物学先验消融**：DepMap 24Q4二元体细胞突变、13个药理学CpG探针、69个药物靶点基因的z-score表达。
- **评估场景**：
  - 三种分割类型：随机5折、组织学盲（38折，留一组织类型）、部位盲（13折，留一解剖部位）。每种分割在三颗初始化种子（42, 7, 123）下重复。
  - 对比方法：
    - **DummyDrugAvg**：药物均值基线（仅知道药物身份，忽略细胞）。
    - **TransCDR-like**：使用相同基础模型输入但采用TransCDR融合机制（交叉注意力）的架构消融。
    - **HGBR on FM stack**：仅用基础模型特征堆栈的直方图梯度提升回归。
    - **Arch I**：本工作提出的图注意力+FiLM架构。
    - **Arch I + HGBR α-ensemble**：最后集成版本。
  - **跨屏幕验证**：将训练好的Arch I（种子42，随机5折折0）冻结，在PRISM 39,682个细胞-药物对上预测，与GDSC-to-PRISM测量可重复性上限比较。
  - **额外消融**：精选生物学先验（突变、甲基化、药物靶点表达）消融；全局PCA泄漏消融；FiLM γ空间可重复性检验；交叉架构残差相关诊断。

### 4. 资源与算力：如果文中有提到，请总结使用了多少算力（GPU 型号、数量、训练时长等）。若未明确说明，也请指出这一点。

- 文中明确提到：训练使用A100 GPU，混合精度bf16自动转换引入约10⁻⁴ R²的非确定性。在数据与代码可用性部分指出，重新生成等价权重大约需要80 A100 GPU小时。
- 未说明具体使用了多少张GPU、训练时长（小时数）以及是否是多卡并行。提到batch size为2048，使用Adam学习率10⁻³，patience-30早停。整体算力消耗中等。

### 5. 实验数量与充分性：大概做了多少组实验（如不同数据集、消融实验等），这些实验是否充分、是否客观、公平。

- **实验数量**：
  - 主要结果：3种分割 × 3颗种子 × 5个模型类（DummyDrugAvg, TransCDR-like, HGBR, Arch I, Arch I+HGBR） → 总计至少45个主要R²报告点（每种子每折平均后有3×3=9个平均值，但种子间有标准差）。
  - 每种子每折详细结果：补充表S7列出206行，涵盖Arch I、Arch I+HGBR、清理的PCA消融、两种生物学先验消融的每折R²、RMSE、Pearson。
  - 消融：
    - 全球PCA泄漏消融：每个分割选一个代表折（共3折）重做，对比∆R²。
    - 生物学先验消融：突变单独和三种组合共2种，每种子5折 → 30个额外实验。
    - 跨架构残差相关：所有折×种子对计算，有同架构控制。
    - FiLM γ空间置换检验：1000次置换。
    - CpGPT线性探测：5折交叉验证逻辑回归对13个组织、38个组织学、17个驱动突变。
  - 额外：TransCDR-like架构控制、跨屏幕PRISM验证（一个冻结模型）。
- **充分性与公平性**：
  - 充分：多种分割（组织盲、部位盲这类硬分割比直接随机分割更真实）；多种子验证确保结果非随机；详尽泄漏审计覆盖六种模式；负结果（生物学先验无效、FiLM解释不通过置换检验）被诚实报告；提供完整代码、数据、预测数组。
  - 客观：所有评估遵循泄漏防控协议，每折预处理独立；与基准DummyDrugAvg比较细胞感知提升而非绝对R²；跨屏幕验证考虑测量不一致性（Spearman而非Pearson）。
  - 公平：对比的TransCDR-like使用相同清洁输入，但原版TransCDR存在泄漏（M2），因此原文明确指出不能宣称超越原版。对比方法选择合理，但缺少与官方清洁清单中其他方法（如UNO/IMPROVE、DeepResponse等）的直接比较，不过论文在Discussion中解释了它们没有同时使用甲基化和药物基础模型。

### 6. 论文的主要结论与发现

1. **泄漏防控有效**：唯一残留的M2泄漏路径（全局PCA+相似度增强k-NN图）在硬分割上每折消融显示∆R²在±0.005以内，非负载承载，因此表1中的性能数据成立。
2. **细胞感知贡献很小**：在组织盲分割上，Arch I+HGBR相对于DummyDrugAvg的细胞感知提升仅为+0.060 R²，类似地，随机和部位盲分别为+0.054和+0.037 R²。大部分绝对性能来自于药物身份和组织谱系。
3. **表示跳变是性能提升的主因**：从平特征（-0.06 R²组织盲）到HGBR on FM stack（0.7625）的提升约+0.82 R²，而架构选择（Arch I vs HGBR）仅带来∼+0.009 R²的额外提升。
4. **交叉架构残差相关定量诊断谱系上限**：在组织盲上，跨架构残差相关系数ρ=0.939，同架构不同初始化控制ρ=0.974，差距约0.034，表明在当前特征堆栈下，架构选择只有约0.03的改进空间。
5. **精选生物学先验不提供额外信号**：突变、甲基化、药物靶点表达通道在基础模型嵌入到位后，其加入导致轻微负效应（∆R²约-0.004至-0.015），说明这些信息已被基础模型表示以组织相关方式编码。
6. **跨屏幕验证匹配测量重复性**：在PRISM上，模型Spearman相关系数0.627，与GDSC-to-PRISM测量上限0.635相差在0.01以内，说明模型捕捉了跨屏幕有效的排序信号。
7. **FiLM γ结构不反映生物学通路特定信息**：γ空间路径-对相似性在不同种子间可重复，但这种可重复性在随机置换标记后同样存在，因此不能声称反映特定的通路关系。

### 7. 优点：方法或实验设计上有哪些亮点

- **严格的泄漏审计**：对每条`fit()`调用按六种Asiaee模式分类，并提供了泄漏清理后的结果及消融证据，提升了结果的可靠性。
- **提出交叉架构残差相关诊断**：一个低成本、可复用的指标，用于定量判断特征堆栈的饱和程度，并以同架构控制校准，对领域具有借鉴意义。
- **诚实报告负结果**：包括精选生物学先验未改善预测、FiLM解释未通过置换检验、架构提升空间极小等，避免夸大贡献。
- **跨屏幕验证**：直接冻结模型在PRISM上测试，并与测量重复性上限比较，展示了模型在独立屏幕上的泛化能力，同时明确指出绝对IC50数值不可比。
- **公开数据集、代码、嵌入、预测数组**：所有材料开放，保证了可复现性；严格种子控制确保确定性。
- **多种子、多分割评估**：不仅随机分割，还包含组织盲和部位盲这类更具挑战的硬分割，且跨种子标准差远小于跨折标准差，证明了结果稳定性。
- **透明地指出局限性**：包括缺少临床数据、GNN架构过时、FiLM结果不稳健、未在所有主流数据集中评估等。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等

- **数据覆盖有限**：所有实验结果仅在GDSC1上获得，PRISM作为外部验证但仅有限重叠细胞系。缺少CCLE、gCSI、CTRPv2、PDO/PDX/临床数据，限制了跨数据集普遍性的结论。
- **GNN架构过时**：使用的图注意力网络（GAT）是2018年的架构，作者也承认当前中等标准是图Transformer，并认为由于谱系上限，架构升级可能仅带来约0.03 R²的提升，但这仍需实验验证。
- **FiLM解释性不成立**：γ空间的结构虽然可重复，但无法证明是通路特异性的，因此相关生物学解释不能作为结论输出。
- **临床转化缺口**：没有使用患者来源的类器官或异种移植模型，也未进行临床试验数据微调，实际临床预测能力未知。
- **无跨数据集泛化评估**：尽管提到了IMPROVE基准，但未实际执行，跨数据集性能可能明显下降（作者预期如此）。
- **计算资源未详细说明**：仅提到约80 A100 GPU小时，但GPU数量、训练具体耗时等信息缺失，不利于他方复现资源配置。
- **混合精度引入噪声**：非确定性约10⁻⁴ R²，小差异可能不可重现。
- **无数据泄漏审计的第三方独立复现**：虽然作者自己进行了审计，但领域最佳实践应由第三方重复泄漏检查。

（完）
