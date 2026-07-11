---
title: Viral rewiring of DDR signaling activates a pro-survival network that drives chemotherapy resistance
title_zh: 病毒对DDR信号的重编程激活了一个促进存活的网络，从而驱动化疗耐药性
authors: "Kong, J., Azhar, H. M. F., Akmel, A., Wen, F., Xu, J., Thomas, M. A."
date: 2026-07-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.06.736708v1.full.pdf"
tags: ["query:neo-resist"]
score: 7.0
evidence: 通过DDR信号传导的化疗耐药机制
tldr: 放疗和化疗依赖DNA损伤反应（DDR）阻滞细胞周期并清除受损细胞，但肿瘤常产生耐药性。本研究发现腺病毒通过重编程DDR激酶ATM和ATR，使其从CHK1/CHK2依赖的检查点阻滞转向激活NEMO-NF-κB生存通路，诱导应激耐受和抗凋亡转录程序，促进异常DNA含量细胞积累。这一DDR可塑性新机制类似早期肿瘤演化，为化疗耐药提供了新解释。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1592, \"height\": 1996, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1696, \"height\": 964, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 634, \"height\": 1786, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1726, \"height\": 1387, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1739, \"height\": 2068, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1683, \"height\": 1570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1630, \"height\": 967, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 557, \"height\": 1002, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1527, \"height\": 517, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1524, \"height\": 131, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1720, \"height\": 1176, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1720, \"height\": 843, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-07-06-736708-v1/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1563, \"height\": 436, \"label\": \"Table\"}]"
motivation: 解析肿瘤如何规避DDR依赖性治疗并产生化疗耐药性的分子机制。
method: 利用腺病毒系统模拟肿瘤信号网络重塑，分析DDR激酶ATM/ATR的靶标转换。
result: ATM和ATR被重编程从CHK1/CHK2检查点转向激活NEMO-NF-κB生存通路，诱导促耐药转录程序。
conclusion: DDR可塑性产生促生存状态，提示ATM/ATR通路可被劫持促进治疗耐药，类似早期肿瘤进化。
---

## 摘要
放疗和化疗依赖于完整的DNA损伤应答（DDR）来阻止细胞周期进程并清除受损细胞，然而许多肿瘤能够逃避这些效应并产生耐药性。腺病毒以类似于肿瘤进化的方式重塑宿主信号网络，为剖析DDR通路如何被颠覆提供了一个强大的系统。在这里，我们识别了两种情景，其中中央DDR激酶ATM和ATR被重新编程，从执行CHK1/CHK2依赖的检查点阻滞转变为激活NEMO-NF-κB生存通路。这种重编程诱导与应激耐受、抗凋亡信号和化疗耐药相关的转录程序，并促进具有异常DNA含量的细胞积累。这些发现揭示了DDR可塑性的一种先前未被认识到的模式，该模式产生了一种类似于早期肿瘤进化的促生存状态，并提示ATM和ATR依赖通路如何被利用以促进治疗耐药性。

## Abstract
Radiation and chemotherapy rely on an intact DNA damage response (DDR) to halt cell-cycle progression and eliminate damaged cells, yet many tumors evade these outcomes and develop resistance. Adenoviruses remodel host signaling networks in ways that mirror tumor evolution, providing a powerful system to dissect how DDR pathways are subverted. Here, we identify two scenarios in which the central DDR kinases ATM and ATR are reprogrammed from enforcing CHK1/CHK2-dependent checkpoint arrest to activating a NEMO-NF-{kappa}B survival pathway. This rewiring induces transcriptional programs associated with stress tolerance, anti-apoptotic signaling, and chemoresistance, and promotes the accumulation of cells with abnormal DNA content. These findings reveal a previously unrecognized mode of DDR plasticity that generates a pro-survival state reminiscent of early tumor evolution and suggest how ATM- and ATR-dependent pathways can be co-opted to promote therapeutic resistance.