---
title: Raman spectral signatures reflect altered metabolic state of exhausted T cells
title_zh: 拉曼光谱特征反映耗竭T细胞代谢状态的改变
authors: "Barai, A. A., Asani, P. C., Sarathi, P., Tiwari, A., Bose, S., Das, S., Mukherjee, G."
date: 2026-06-21
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.16.732575v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 研究肿瘤微环境中T细胞耗竭，这是新辅助治疗耐药的关键机制
tldr: T细胞耗竭是肿瘤微环境中CD8+ T细胞功能丧失的关键原因，限制了免疫治疗效果。本研究通过慢性抗原刺激建立体外耗竭模型，利用单细胞拉曼光谱获取活化与耗竭T细胞的生化指纹。主成分分析显示两种细胞光谱显著分离，差异峰对应核酸、蛋白质等代谢物，机器学习分类准确率较高。该工作证明拉曼光谱可作为无标记、非破坏性手段监测T细胞耗竭状态，为免疫分析提供新平台。
source: biorxiv
selection_source: fresh_fetch
motivation: T细胞耗竭导致抗肿瘤免疫失效，现有检测方法需标记或破坏细胞，亟需无标记实时监测技术。
method: 通过慢性抗原刺激OT-1 CD8+ T细胞建立体外耗竭模型，结合单细胞拉曼光谱和PCA分析生化差异。
result: 拉曼光谱PCA清晰区分活化与耗竭T细胞，差异峰对应核酸、蛋白质等代谢物，机器学习分类准确。
conclusion: 单细胞拉曼光谱可无标记、非破坏性识别耗竭T细胞，为免疫功能障碍监测提供新工具。
---

## 摘要
肿瘤微环境中的T细胞耗竭驱动CD8+ T细胞进入功能障碍状态，其特征是增殖能力和效应功能逐渐丧失，从而限制了抗肿瘤免疫和治疗效果。为了研究与耗竭相关的生化改变，通过慢性抗原刺激小鼠OT-1 CD8+ T细胞建立了CD8+ T细胞耗竭的体外模型。表型、功能、代谢和转录特征证实了耗竭状态的获得。随后采用单细胞拉曼光谱生成活化和耗竭CD8+ T细胞的生化特征。拉曼光谱数据的主成分分析（PCA）揭示了这两个细胞亚群的明显分离，反映了与其功能状态相关的潜在生化差异。对应于核酸、碳水化合物、蛋白质和脂质的差异拉曼光谱特征显著促进了这种分离，反映了耗竭进程中代谢和生物合成状态的改变。使用机器学习算法对光谱数据进行分类，能够准确区分活化和耗竭T细胞。总的来说，本研究表明单细胞拉曼光谱可以以无标记、非破坏性的方式区分耗竭的CD8+ T细胞，突显了其作为免疫分析和监测T细胞功能障碍平台的潜力。

## Abstract
T cell exhaustion within the tumor microenvironment drives CD8+ T cells into a dysfunctional state characterized by progressive loss of proliferative capacity and effector functions, thereby limiting anti-tumor immunity and therapeutic efficacy. To investigate the biochemical alterations associated with exhaustion, an in vitro model of CD8+ T cell exhaustion was established through chronic antigenic stimulation of murine OT-1 CD8+ T cells. Phenotypic, functional, metabolic, and transcriptional characterization confirmed the acquisition of an exhausted state. Single-cell Raman spectroscopy was subsequently employed to generate biochemical signatures of activated, and exhausted CD8+ T cells. Principal component analysis (PCA) of the Raman spectral data revealed distinct separation of these two cell subsets, reflecting underlying biochemical differences associated with their functional states. Differential Raman spectral features corresponding to nucleic acids, carbohydrates, proteins, and lipids contributed significantly to this segregation, reflecting altered metabolic and biosynthetic states during exhaustion progression. Classification of the spectral data using machine-learning algorithms enabled accurate segregation of activated and exhausted T cells. Collectively, this study demonstrates that single-cell Raman spectroscopy can distinguish exhausted CD8+ T cells in a label-free and non-destructive manner, highlighting its potential as a platform for immune profiling and monitoring T cell dysfunction.

---

## 论文详细总结（自动生成）

### 论文结构化总结

#### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：肿瘤微环境（TME）中CD8⁺ T细胞的耗竭是限制免疫疗法效果的主要原因。耗竭T细胞表现出增殖能力丧失、效应功能下降、抑制性受体共表达、代谢与转录重编程等特征，但现有检测方法（如流式细胞术、功能分析）需要标记或破坏细胞，且无法直接反映细胞内在的生化复杂性。
- **整体含义**：需要一种无标记、非破坏性的技术以在单细胞层面实时识别和表征耗竭T细胞。拉曼光谱（Raman spectroscopy）通过探测分子振动提供生化指纹，有望区分不同功能状态的T细胞。本研究探索了该技术的可行性，旨在为免疫监测和治疗响应评估建立新平台。

#### 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：利用单细胞拉曼光谱获取活化与耗竭CD8⁺ T细胞的生化指纹，通过主成分分析（PCA）揭示差异，再结合机器学习分类器实现自动判别。
- **关键技术细节**：
  - **体外耗竭模型建立**：使用OT-1转基因小鼠脾脏CD8⁺ T细胞，通过重复（每48小时）刺激SIINFEKL-H2Kb pMHC复合物，模拟慢性抗原刺激。前两次使用平板结合pMHC，后两次使用可溶性pMHC和条件培养基。对比组为急性刺激（AS，48h激活后静息）和未刺激（UT）细胞。
  - **拉曼光谱采集**：固定后的细胞滴铸在载玻片上，使用532 nm激发激光，50×物镜，600 g/mm光栅，积分时间5 s/次×10次积累，采集单细胞光谱（120个/亚群，3个生物学重复）。
  - **光谱预处理**：去除宇宙射线、基线校正。
  - **多元分析与分类**：
    - PCA：对均值中心化、单位方差缩放的数据矩阵进行奇异值分解。
    - 机器学习：随机森林（RF, 500棵树）、支持向量机（SVM, RBF核）、极限梯度提升（XGBoost, 300估计器，最大深度4，学习率0.05），采用分层五折交叉验证评估。还测试了PCA降维后的分类效果。
  - **分类性能指标**：准确率、ROC AUC、混淆矩阵、精确率、召回率、F1分数。
  - **外部验证**：使用独立的40个活化+40个耗竭细胞光谱验证最优模型。

#### 3. 实验设计：数据集/场景、benchmark、对比方法
- **数据集**：小鼠OT-1 CD8⁺ T细胞，分为活化（48h激活后静息）和耗竭（慢性刺激第6天，CS6）两种状态。每个状态120个单细胞光谱（3个生物学重复），外加40+40用于外部验证。
- **Benchmark**：无外部公开基准，以表型/功能/代谢/转录特征（如Ly108、PD-1、LAG-3、CD39、TCF-1、TOX等）验证模型真实性，以PCA可视化作为初始判别依据。
- **对比方法**：
  - 三种机器学习算法（RF、SVM、XGBoost）在原始光谱特征和PCA降维特征上的表现对比。
  - 主要比较准确率和AUC。

#### 4. 资源与算力
- **未明确说明**：论文未提及GPU型号、数量、训练时长等算力信息。所有数据处理和机器学习可能在普通工作站或R/Python环境下完成（依赖CPU），因为光谱数据维度（1650个波数×240个样本）较小。

#### 5. 实验数量与充分性
- **实验数量**：
  - 体外模型表征：增殖曲线（Fig 1B）、Ly108+/-动态（Fig 1C-D）、CD25/IL-2（Fig 1E-F）、Granzyme/CD107a（Fig 1G-H）；抑制性受体表达（Fig 2）、代谢标志物（CD36、CD39；Fig 3A-B）、转录因子（TCF-1、TOX；Fig 3C-D）。
  - 拉曼光谱：活化与耗竭各120个单细胞光谱（共240个），来自3个生物学重复；外部验证80个光谱。
  - 机器学习：5折交叉验证对比三种模型，选择最佳后另设20%测试集（48个光谱）以及独立外部验证（80个光谱）。
- **充分性**：
  - **优点**：模型构建经过了多维度（功能、表型、转录、代谢）表征，与已知文献一致，保证了耗竭状态的可靠性。拉曼光谱数据的生物学重复（n=3）和单细胞数量（120）足够。外部独立验证证实了模型泛化性。
  - **不足**：仅比较了三种经典机器学习算法，未尝试深度学习（如CNN）或集成其他特征。PCA降维后分类无改善，但未详细讨论原因。缺乏在混合细胞群体或病理样本中的验证。未与流式细胞术等“金标准”直接对比分类一致性（如相关性分析）。

#### 6. 论文的主要结论与发现
- **耗竭模型成功建立**：慢性刺激细胞表现出增殖下降、Ly108⁻过渡/终末耗竭细胞增加、IL-2/Granzyme/CD107a减少、抑制性受体（PD-1/LAG-3/TIGIT/TIM-3）共表达、CD36↑、CD39↑、TCF-1↓、TOX↑，符合耗竭特征。
- **拉曼光谱可区分活化与耗竭T细胞**：PCA中活化与CS6细胞在3D空间中明显分离，主要差异波数对应胆固醇（426、546 cm⁻¹）、核酸（780、1250、1320 cm⁻¹）、苯丙氨酸（1003-1005 cm⁻¹）、色氨酸（1340 cm⁻¹）、蛋白质/脂质（1440、1580、1650、2800-3000 cm⁻¹）和碳水化合物（850-950 cm⁻¹）。
- **定量分析**：耗竭细胞胆固醇、苯丙氨酸、碳水化合物相关峰强度升高；核酸、色氨酸、蛋白质/脂质相关峰强度降低。
- **机器学习判别**：XGBoost表现最优（准确率85.8±3.58%），在外部验证中达100%准确率（AUC=1.0），证明光谱信号足以稳健分类。

#### 7. 优点
- **无标记、非破坏性**：无需染色或裂解细胞，保留细胞完整性，适用于原位或临床样本。
- **单细胞分辨率**：捕捉细胞异质性，可反映耗竭进程中的连续状态（尽管本实验仅比较了两个端点）。
- **多维度验证模型**：结合表型、功能、代谢、转录数据确认耗竭状态，增加拉曼分析的生物学解释性。
- **外部独立验证**：使用不同批次的独立样本验证XGBoost泛化能力，结果极好，增强可信度。
- **开放方法、数据驱动**：详细提供了光谱预处理、PCA、机器学习参数，可复现。

#### 8. 不足与局限
- **模型局限性**：
  - 仅使用小鼠OT-1系统，人类耗竭T细胞是否具有相似拉曼光谱特征有待验证。
  - 仅对比了活化（48h）与耗竭（第6天）两个时间点，未涵盖耗竭全过程（如第2、4天早期耗竭）或终末耗竭（第8天），也缺少与其他功能障碍状态（如衰老、失能）的区分。
- **光谱解析局限**：
  - 峰归属基于文献，未进行去卷积或从头分子验证，部分区域（如1003 cm⁻¹）可能来自多种振动。
  - 固定处理（4%多聚甲醛）可能改变某些构象，未比较活细胞与固定细胞光谱差异。
- **机器学习方面**：
  - 样本量（240个细胞）较小，易过拟合，尽管外部验证表现好，但可能因独立样本来自相同小鼠品系和培养条件。
  - 未使用更先进的分类器（如深度学习）或集成多种数据模态。
- **实验公平性**：
  - 未与流式细胞术等标准方法在同一细胞上进行平行比较（拉曼后无法继续功能分析，但可进行共定位实验）。
  - 缺少对光谱采集参数（如激光功率、曝光时间）的系统优化描述。
- **应用限制**：
  - 需要固定细胞，限制实时监测；若用于临床，需开发活细胞拉曼平台。
  - 细胞准备步骤（洗涤、空气干燥）可能引入人为变化。

（完）
