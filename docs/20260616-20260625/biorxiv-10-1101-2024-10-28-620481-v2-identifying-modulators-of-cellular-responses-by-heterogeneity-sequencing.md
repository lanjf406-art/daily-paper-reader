---
title: Identifying Modulators of Cellular Responses by Heterogeneity-sequencing
title_zh: 通过异质性测序识别细胞反应的调节因子
authors: "Berg, K., Sakellaridi, L., Rummel, T., Hennig, T., Whisnant, A., Lodha, M., Krammer, T., Toussaint, C., Szymanska-De Wijs, K., Zheng, Y., Prusty, B. K., Doelken, L., Saliba, A.-E., Erhard, F."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.1101/2024.10.28.620481v2.full.pdf"
tags: ["query:neo-resist"]
score: 9.0
evidence: 结合单细胞RNA-seq和机器学习识别药物反应异质性的因果驱动因素
tldr: 单细胞对药物或病毒的反应高度异质，但传统测序破坏细胞，无法比较初始状态与结果。Heterogeneity-seq结合单细胞RNA-seq、代谢RNA标记（scSLAM-seq）和双重机器学习，同步测量未标记和标记RNA，揭示细胞状态到反应结果的因果链条。该方法成功识别了驱动药物响应的已知和新基因，以及巨细胞病毒感染中的促抗病毒宿主因子。这一技术实现了从相关关联到因果解析的跨越，为理解细胞反应异质性提供了强大工具。
source: biorxiv
selection_source: fresh_fetch
motivation: 传统单细胞方法只能识别细胞反应与初始状态的相关性，无法确定因果驱动因素。
method: 整合scSLAM-seq和双重机器学习，通过代谢标记区分新旧RNA，分析刺激前后的转录变化。
result: 识别出药物处理和巨细胞病毒感染中调控细胞反应的因果基因，包括已知和新发现因子。
conclusion: Heterogeneity-seq实现了从相关到因果的跨越，为解析异质性细胞反应提供新范式。
---

## 摘要
单个细胞对药物处理、病毒感染或其他分子刺激的反应高度异质性，取决于细胞的初始状态。单细胞转录组学的文库制备具有破坏性，无法直接比较初始状态与刺激结果。因此，当前方法仅限于识别相关性关联，而非解析异质性结果的因果驱动因素。我们开发了异质性测序（Heterogeneity-seq），该方法结合了单细胞RNA测序与代谢RNA标记（scSLAM-seq）以及双重机器学习，以克服这一限制。通过利用单个细胞中未标记和标记RNA的同时测量，异质性测序揭示了从刺激前细胞状态到不同刺激结果在数千个细胞中的转变。这些关联使得识别因果支配异质性细胞反应的因子成为可能。我们使用异质性测序识别了驱动对药物处理反应的已知和新基因，以及控制巨细胞病毒感染的促病毒和抗病毒宿主因子。

## Abstract
The response of individual cells to drug treatment, virus infections or other molecular stimuli is highly heterogeneous and depends on the cells initial state. Library preparation for single-cell transcriptomics is destructive, precluding a direct comparison between the initial state and the stimulus outcome. Consequently, current methods are restricted to identifying correlative associations rather than resolving causal drivers of heterogeneous outcomes. We developed Heterogeneity-seq, which combines single-cell RNA-seq with metabolic RNA labeling (scSLAM-seq) and double machine learning to overcome this limitation. By leveraging simultaneous measurements of unlabeled and labeled RNA in individual cells, Heterogeneity-seq uncovers the transition from pre-stimulated cell states to distinct stimulation outcomes across thousands of cells. These links enable the identification of factors that causally govern heterogeneous cellular responses. We used Heterogeneity-seq to identify both known and novel genes that drive responses to drug treatment, as well as pro- and antiviral host factors governing cytomegalovirus infection.

---

## 论文详细总结（自动生成）

好的，以下是对该论文的结构化、深入、客观的中文总结。

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：在生物学中，即使是遗传上相同的细胞，对药物、病毒感染等外源性刺激的反应也存在高度异质性。传统单细胞转录组学（scRNA-seq）只能提供刺激前后的“静态快照”，但由于测序会破坏细胞，无法直接追踪单个细胞从初始状态到最终反应结果的完整过程，因此只能发现相关性，无法确定异质性的因果驱动因素。现有通过RNA干扰或CRISPR进行活性扰动的筛选方法虽有效，但存在非生理性、脱靶效应、补偿性通路激活等问题，可能掩盖真实的因果机制。
- **整体含义**：该论文提出了一个名为**异质性测序（Heterogeneity-seq）** 的框架，旨在解决这一根本性挑战。其核心思想是利用细胞群体中天然存在的转录异质性，结合代谢RNA标记和机器学习方法，建立刺激前细胞状态与刺激后反应结果之间的因果链路，从而在不进行基因扰动的情况下，识别出真正支配细胞反应异质性的**因果调节因子**。

### 2. 论文提出的方法论

- **核心思想**：通过代谢RNA标记（scSLAM-seq），在施加刺激前引入核苷类似物（4sU）。在刺激后的单细胞中，测序到的**有标记的新RNA**反映了细胞对刺激的反应（结果），而**未标记的旧RNA**则反映细胞在刺激前的状态（原因）。通过分析旧/新RNA的差异，可以在同一个细胞中将“因”与“果”关联起来，从而区分哪些基因表达差异是反应的结果，哪些可能是原因（因果因子）。
- **关键技术细节与算法流程**：
    1.  **数据生成（scSLAM-seq/ sci-fate）**：在施加刺激前开始进行4sU标记，在刺激后的不同时间点获取细胞，进行单细胞测序。
    2.  **新旧RNA定量（GRAND-SLAM 3.0的卷积版本）**：
        -   使用改进的GRAND-SLAM 3.0算法，基于T-to-C碱基转换来量化新RNA与总RNA的比率。
        -   为解决单细胞数据稀疏性导致的定量偏差，开发了**“卷积NTR”** 方法，即借用表达模式相似的邻近细胞的读段信息来更准确地估计每个细胞的NTR。
        -   基于细胞特异性半衰期，对旧RNA进行降解校正，得到代表刺激前状态的**“先前RNA”** 表达量。
    3.  **单细胞轨迹推断（最优非重叠轨迹）**：
        -   使用**“最小成本流”（MinCostFlow）** 算法，在不同时间点的细胞间建立一一对应的、无重叠的最优连接轨迹。
        -   距离函数基于先前/总RNA的典型相关分析（CCA）嵌入的欧氏距离，确保轨迹反映了最可能的细胞状态随时间的演化路径。该算法克服了“最近邻”法导致的细胞连接稀疏问题。
    4.  **因果因子识别**：
        -   根据轨迹终点（如最后时间点）的细胞反应强度（如DEX评分、病毒载量），将细胞分为“强反应者”和“弱反应者”。
        -   **基于分类的异质性测序（SVM）**：以轨迹起点（0h）细胞的单个基因表达量（以及细胞周期等协变量）为特征，训练支持向量机（SVM）来预测终点细胞是强反应还是弱反应。使用AUC（ROC曲线下面积）作为预测能力的衡量标准，AUC高的基因即为候选调节因子。
        -   **基于因果推断的异质性测序（双重机器学习dML）**：使用双重机器学习框架（DoubleML），通过其他所有基因的表达量来“回归掉”潜在混淆因子的影响，然后评估单个基因对反应结果的**因果效应**。该方法能有效区分直接因果因子和相关因子，提供更严格的因果证据。

### 3. 实验设计

- **数据集**：
    - **地塞米松（DEX）响应数据集**：使用公开的sci-fate数据，包括A549细胞系在DEX处理0/2/4/6/8/10小时后的时间序列数据。
    - **巨细胞病毒（MCMV）感染数据集**：自产的单细胞scSLAM-seq数据，包括NIH-3T3细胞在MCMV感染2小时后（感染初期）的数据。
- **Benchmark**：论文没有与现有的特定方法进行直接“比拼”，而是采用了**模拟实验**来验证因果推断方法的性能。
- **对比的方法**：论文对比了自身框架内的不同分析策略：
    - 使用总RNA vs. 新RNA vs. 旧RNA进行异质性分析的对比。
    - 使用“最近邻”法 vs. “最小成本流”法进行轨迹推断的对比。
    - 使用统计差异分析、SVM分类和双重机器学习（dML）三种方法进行因果因子筛选的对比。
- **模拟实验**：
    - 从DEX数据集中选取已知相关性（与所有其他基因的平均相关系数）的基因群（Group 1-10），将其中部分基因模拟为真正的因果因子。
    - 测试SVM和dML方法在不同噪声水平（扰动轨迹）下识别这些模拟因果因子的能力（FPR@100%TPR）。

### 4. 资源与算力

- **论文未明确提及使用的具体GPU型号、数量或训练时长**。作者提到GRAND-SLAM 3.0进行了底层代码重写以提高可扩展性，使其能应用于数千个细胞的数据集，并公开了R包（HetSeq）。计算主要在CPU上完成，轨迹推断和机器学习模型也属于计算密集型任务，但未量化硬件资源需求。

### 5. 实验数量与充分性

- **实验数量与覆盖**：
    - **两种生物场景**：在药物（DEX）反应和病毒（MCMV）感染两个不同的系统中进行了验证，证明方法的通用性。
    - **多种分析方法对比**：在同一数据集上系统比较了不同RNA池、不同轨迹算法、不同因果推断方法的效果，设计全面。
    - **模拟验证**：进行了系统的模拟实验，从多个维度（基因表达水平、相关性、轨迹噪声）评估了核心算法的性能。
    - **时间序列分析**：在DEX数据上分析了从2h到10h的响应，探讨了影响“响应速度”和“响应强度”的不同因子。
    - **消融分析**：通过排除细胞周期效应、排除已识别的受调控基因等分析，排除了潜在混淆因素。
- **充分性评估**：整体而言，实验设计较为**充分和客观**。模拟实验是评估因果推断方法的有力手段，结果清晰展示了SVM的灵敏度和dML的特异性及其局限性。在两个独立生物学场景中的成功应用增加了结论的可信度。实验设计公平，内部对比充分。

### 6. 论文的主要结论与发现

1.  **Heterogeneity-seq方法有效**：通过代谢RNA标记区分新旧RNA，结合最优轨迹推断和因果机器学习，能够在单细胞水平上识别驱动细胞反应异质性的**因果因子**，而不需要主动的基因扰动。
2.  **方法性能出色**：模拟实验表明，SVM分类方法能可靠地（高AUC）将因果因子与其他基因区分开来，而双重机器学习（dML）方法具有更强的鲁棒性，能从强相关基因中精确识别出真正的因果因子，但对强共表达的基因网络可能漏检。
3.  **成功应用于DEX响应**：Heterogeneity-seq成功识别了已知（如**TRAM1**）和新型的糖皮质激素受体信号通路调节因子，并发现“细胞周期”是影响DEX反应强弱的一个主要混淆因子。
4.  **成功应用于病毒感染**：在MCMV感染模型中，该方法识别出了促病毒因子（如微管/肌动蛋白相关基因**Tubb4b、Acta2**）和抗病毒因子（如核糖体相关基因、**Vimentin**），与传统认知相符，并发现了新的潜在靶点。
5.  **揭示了响应的动力学**：通过对不同时间点的分析，发现有些基因影响的是反应的“强度”（如长期都保持高AUC的**ARNTL2**），而有些基因则主要影响反应的“速度”（如仅在早期有预测能力的基因）。

### 7. 优点

1.  **创新性强**：首次系统性地将代谢RNA标记、轨迹推断和双机器学习结合起来，实现单细胞层面的因果推断，是一个重要的方法论创新。
2.  **避免主动扰动**：利用自然异质性，避免了传统扰动实验的诸多缺点，能更真实地反映生理条件下的基因功能。
3.  **因果推断清晰度高**：通过区分新/旧RNA，克服了仅分析刺激后数据无法区分“因”与“果”的根本性模糊。dML方法进一步增强了因果推断的严谨性。
4.  **方法模块化与可扩展**：框架中的各个部分（RNA标记、NTR估计、轨迹推断、因果推断）可以独立使用和迭代升级，其核心软件（GRAND-SLAM 3.0, HetSeq包）均已开源。
5.  **通用性强**：方法不局限于特定刺激或细胞类型，可广泛应用于多种生物学问题（如药物响应、病原体-宿主互作、发育等）。

### 8. 不足与局限

1.  **技术噪声与局限性**：
    - **新旧RNA分离不完美**：4sU掺入率低和测序错误可能导致旧RNA中掺入少量新RNA，反之亦然，虽然卷积NTR方法有所缓解，但无法完全消除“溢出”效应。
    - **轨迹推断是近似**：轨迹是基于不同细胞在不同时间点的群体统计推断出来的，并非真正追踪同一个细胞，因此是“最优近似”。高的轨迹噪声会降低因果推断的准确性。
2.  **方法局限性**：
    - **dML检测失效**：当多个强相关的基因共同作为因果因子时，由于共线性问题，dML可能无法指认出任何一个为显著因果因子（所有基因p值都很大），导致漏检。
    - **对低表达基因不敏感**：模拟实验表明，SVM和dML对表达量极低的基因（Group 1）的预测能力均下降。
3.  **验证困难**：由于Heterogeneity-seq通过避免主动扰动来模拟生理条件，其发现的因果因子若用传统的KO或过表达进行功能验证，可能会引入新的混淆，使验证结果难以解释。论文建议应结合**正交证据**进行验证，而非单一依赖扰动实验。
4.  **实验覆盖有限**：仅在DEX和MCMV两个系统中进行了验证。虽然具有代表性，但方法的普适性仍需要在更多样化的生物学场景（如细胞分化、更复杂的信号通路响应等）中进行测试。
5.  **未量化计算成本**：论文未明确描述所需的硬件资源（如GPU）和计算时间，对于希望复现或应用此方法的研究者来说，缺少资源规划的参考。

（完）
