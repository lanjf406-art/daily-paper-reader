---
title: TOX enforces the immunosuppressive program of tumor-infiltrating regulatory T cells
title_zh: TOX强化肿瘤浸润调节性T细胞的免疫抑制程序
authors: "Park, S., Park, D. J., Kim, M. J., Kelly, G., Zhang, R., Kim, G., Jeong, J., Kim-Schulze, S., Kim, H. R., Kim, K., Ha, S.-J."
date: 2026-06-24
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.19.732838v1.full.pdf"
tags: ["query:neo-resist"]
score: 8.0
evidence: 肿瘤微环境中Treg细胞的免疫抑制程序与耐药相关
tldr: 肿瘤浸润调节性T细胞(Treg)的免疫抑制状态由何种转录因子维持尚不清楚。本文发现转录因子TOX在肿瘤浸润Treg中特异性高表达。Treg特异性敲除TOX可减轻肿瘤负担、增强抗肿瘤免疫，并促进PD-1阻断疗效。单细胞测序和ATAC-seq揭示TOX维持Treg效应状态，其缺失使Treg转向祖细胞样表型。该研究确立TOX为Treg免疫抑制程序的关键调控因子，为免疫治疗提供新靶点。
source: biorxiv
selection_source: fresh_fetch
motivation: 明确肿瘤浸润Treg免疫抑制状态的转录调控因子，特别是TOX的作用。
method: 利用Treg特异性敲除小鼠、单细胞RNA测序、ATAC-seq及TCR克隆型分析。
result: TOX缺失导致Treg凋亡增加、效应功能下降并转向TCF7相关祖细胞样表型，同时增强CD8 T细胞对PD-1阻断的反应。
conclusion: TOX是维持肿瘤浸润Treg适应性和稳定性的关键因子，可作为增强PD-1免疫疗法的潜在靶点。
---

## 摘要
调节性T（Treg）细胞在肿瘤微环境（TME）中积累以抑制抗肿瘤免疫，但稳定其免疫抑制状态的转录调控因子尚不明确。本文显示，转录因子TOX在人类癌症和小鼠肿瘤模型的肿瘤浸润（TI）Treg细胞中选择性上调，而在外周和初始Treg群体中保持低水平。Treg特异性敲除TOX可减少肿瘤负荷，损害TI Treg介导的免疫抑制，并增强CD8和CD4 T细胞的效应功能。在马赛克小鼠中，TOX缺陷的Treg细胞被选择性从肿瘤中清除，伴随凋亡增加。单细胞RNA测序和TCR克隆型分析将TOX表达与具有克隆扩增的效应样TI Treg状态联系起来，而TOX缺失则使细胞向TCF7相关的前体样表型转变。ATAC-seq显示，TOX充足的TI Treg中AP-1基序富集，而TOX缺陷的对应细胞中则富集TCF7、LEF1和FOXO1基序，揭示了TOX下游的相反转录网络。此外，TOX缺陷增强了CD8 T细胞对PD-1阻断的反应。总之，这些发现确立了TOX是TI Treg适应性和稳定性的关键调控因子，并将其确定为增强基于PD-1的免疫治疗疗效的潜在治疗靶点。

## Abstract
Regulatory T (Treg) cells accumulate in the tumor microenvironment (TME) to suppress anti-tumor immunity, but the transcriptional regulators stabilizing their immunosuppressive state remain poorly defined. Here we show that transcriptional factor TOX is selectively upregulated in tumor-infiltrating (TI) Treg cells across human cancers and mouse tumor models, while remaining low in peripheral and naive Treg populations. Treg-specific deletion of TOX reduced tumor burden, impaired TI Treg-mediated immune suppression, and enhanced effector functions of CD8 and CD4 T cells. In mosaic mice, TOX-deficient Tregs were selectively depleted from tumors, accompanied by increased apoptosis. Single-cell RNA sequencing and TCR clonotype analysis linked TOX expression to an effector-like TI Treg state with clonal expansion, whereas TOX loss shifted cells toward a TCF7-associated progenitor-like phenotype. ATAC-seq revealed enrichment of AP-1 motifs in TOX-sufficient TI Tregs. In contrast, TCF7, LEF1, and FOXO1 motifs in TOX-deficient counterparts, uncovering the opposing transcriptional networks downstream of TOX. Furthermore, TOX deficiency augmented CD8 T cell responses to PD-1 blockade. Together, these findings establish TOX as a key regulator of TI Treg fitness and stability, and identify it as a potential therapeutic target to enhance the efficacy of PD-1-based immunotherapy.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：肿瘤微环境（TME）中，调节性T（Treg）细胞大量积累并抑制抗肿瘤免疫，但维持其免疫抑制状态的转录调控因子尚未明确。
- **研究动机**：揭示Treg在肿瘤中稳定发挥免疫抑制功能的分子机制，为免疫治疗提供新靶点。
- **背景意义**：Treg是肿瘤免疫逃逸的关键介质，但其在TME中的适应性分子基础不清楚；找到关键调控因子有助于设计联合疗法（如PD-1阻断）。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：假设转录因子TOX在肿瘤浸润Treg（TI-Treg）中特异性高表达并维持其免疫抑制程序，通过基因敲除验证功能。
- **关键技术细节**：
  - 使用**Treg特异性敲除TOX的小鼠模型**（Foxp3-Cre × Tox-flox）。
  - **马赛克小鼠模型**（混合骨髓移植）追踪TOX缺陷Treg在肿瘤中的命运。
  - **单细胞RNA测序（scRNA-seq）** 分析TI-Treg的转录状态及克隆型。
  - **ATAC-seq** 检测染色质可及性，鉴定TOX下游转录网络（AP-1 vs TCF7/LEF1/FOXO1）。
  - **TCR克隆型分析** 关联TOX表达与Treg克隆扩增。
  - 联合**PD-1阻断**评估TOX缺失对抗肿瘤免疫的增强效果。
- **未涉及公式或算法流程，均为实验和组学分析**。

## 3. 实验设计：使用的数据集/场景、benchmark、对比方法

- **数据集与场景**：
  - 人类癌症样本（多种类型）中检测TOX表达。
  - 小鼠肿瘤模型（具体类型未列出，推测为皮下/原位肿瘤模型）。
  - 分为：野生型（WT）Treg vs TOX-KO Treg；外周Treg vs TI-Treg。
- **Benchmark**：未明确设立标准化benchmark，但以WT小鼠和未处理组作为对照。
- **对比方法**：
  - TOX充足 vs TOX缺陷Treg在肿瘤内、外周、淋巴器官中的表型对比。
  - 比较TOX表达与TCF7、LEF1等转录因子的关联。
  - 比较PD-1阻断前后CD8 T细胞反应差异。

## 4. 资源与算力

- 元数据**未明确说明**使用的GPU型号、数量或训练时长。涉及scRNA-seq和ATAC-seq分析可能使用高性能计算集群，但未提供具体信息。

## 5. 实验数量与充分性

- **实验组数**：包括Treg特异性KO小鼠、马赛克小鼠、scRNA-seq、ATAC-seq、PD-1阻断联合实验等多个独立实验。元数据未列具体数字，但覆盖了分子、细胞、体内功能等多个层面。
- **充分性评价**：实验设计较为充分：
  - 使用遗传学敲除（因果验证）。
  - 多组学（scRNA-seq、ATAC-seq）揭示机制。
  - 马赛克小鼠排除系统性偏差。
  - 联合免疫治疗增强临床相关性。
- **客观公平性**：使用了适当的对照（WT、Foxp3-Cre对照），但缺乏其他转录因子（如NFAT、BATF）的对比实验，可能略显局限。

## 6. 论文的主要结论与发现

- **核心发现**：TOX在肿瘤浸润Treg中特异性高表达，且是维持Treg免疫抑制状态的关键转录因子。
- **具体结论**：
  - TOX缺失导致TI-Treg凋亡增加、效应功能下降，肿瘤负荷减少。
  - TOX缺陷的Treg转向TCF7阳性祖细胞样表型（前体样）。
  - ATAC-seq揭示TOX维持AP-1通路活性，同时抑制TCF7/LEF1/FOXO1通路。
  - TOX缺失增强CD8 T细胞对PD-1阻断的治疗反应。
- **意义**：TOX可作为联合PD-1免疫治疗的潜在靶点。

## 7. 优点：方法或实验设计上的亮点

- **多模型验证**：同时使用Treg特异性KO小鼠和马赛克小鼠，确保细胞内在效应。
- **多组学整合**：scRNA-seq + ATAC-seq + TCR克隆型分析，从转录组、表观遗传组和克隆动态层面全面解析。
- **临床相关性**：验证人类癌症中TOX的表达模式，增加转化潜力。
- **功能与治疗结合**：直接测试TOX缺失对PD-1阻断疗效的影响，具有直接临床意义。

## 8. 不足与局限

- **局限一**：仅在小鼠模型中验证，缺乏人类肿瘤内Treg的遗传学实验（如CRISPR敲除人Treg的TOX）。
- **局限二**：未探索TOX在其他免疫细胞（如CD8 T细胞中TOX的已知功能）的交叉影响，可能混淆观察到的CD8 T细胞增强效应（间接而非直接）。
- **局限三**：ATAC-seq仅比较TOX充足vs缺陷，未进行CUT&Tag或ChIP-seq直接证明TOX在染色质上的结合位点。
- **局限四**：未测试其他免疫检查点阻断（如CTLA-4）的联合效果。
- **偏差风险**：所有实验基于特定小鼠肿瘤模型（未列出具体类型），可能无法泛化至所有肿瘤类型。

（完）
