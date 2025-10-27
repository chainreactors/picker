---
title: G.O.S.S.I.P 阅读推荐 2024-10-11 RAID 2024最佳实践论文奖之KernJC
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498972&idx=1&sn=50a5553993efdac4b203269a9eb5fbce&chksm=c063d205f7145b13db364bcc761c0677a378e30aa482ce5a481620549aae2a71126e10f82f6a&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-12
fetch_date: 2025-10-06T18:53:27.619086
---

# G.O.S.S.I.P 阅读推荐 2024-10-11 RAID 2024最佳实践论文奖之KernJC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GOG6giczzHng3pRmlZTnBPybHlT7BtMVGwVFoZ8JZyaP0jicv3Plkyrbic9DEBZcBapLWpSIk5mHMEQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-10-11 RAID 2024最佳实践论文奖之KernJC

原创

阮博男

安全研究GoSSIP

2024年9月30日到10月2日，为期3天的RAID 2024会议在意大利北部城市帕多瓦顺利举行（此处要@一下我们的某位读者）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyGVBpicCt7nroFXdesfUxibEuRrRBuFCCyccibsWrBP40RUibWhRXFvgNYg/640?wx_fmt=png&from=appmsg)

今年的RAID会议一共收到了172篇投稿，最终录用了43篇论文，录用率25%，竞争相当激烈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyUUxlAJkUoRTbp0xLPwWRWQl15ic2xw8XUh854oxaolyVcwN0vO4pbBQ/640?wx_fmt=png&from=appmsg)

而我们今天要为大家推荐的论文，获得了RAID 2024唯一Best Practical Paper奖，这就是由新加坡国立大学梁振凯研究组完成的工作——KernJC: Automated Vulnerable Environment Generation for Linux Kernel Vulnerabilities

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyo8bBM94rK8pZf2LibrxEtFphDUM7SQmRf9aNaaBiaAH5Nf3bPS1hZiaNA/640?wx_fmt=png&from=appmsg)

在Linux系统中，内核漏洞的复现对于评估漏洞的严重性、设计解决方案及制定防护策略至关重要。然而，构建脆弱环境以复现漏洞的过程较为复杂，且容易受到版本声明错误和配置不当的影响。本文介绍了KernJC，这是一个专门用于自动生成Linux内核漏洞环境的工具，旨在解决Linux内核漏洞复现中的环境搭建问题。KernJC通过基于补丁的漏洞版本识别和基于图的内核配置识别，自动生成虚拟化漏洞环境，从而显著提升漏洞复现的效率和准确性。

与手动方法相比，KernJC在复现漏洞时实现了高效的漏洞版本和配置识别，不仅发现了多个漏洞数据库中存在的错误版本声明，还通过非默认配置的启用，成功为多个复杂的内核漏洞自动化生成了漏洞复现环境。本文提出了针对所有新发现内核漏洞的复现环境生成方案，为提高Linux内核漏洞复现的自动化程度提供了全新的解决策略。

论文的贡献主要包括：

* 修正和增强内核CVE信息：本文开发了技术来修正和改进内核CVE中的信息，修复了版本错误并添加了漏洞复现所需的关键配置项。特别是，研究发现了NVD数据库中128个漏洞版本声明不准确的情况，强调了提高漏洞报告准确性的重要性。
* 开源工具实现：作者将该解决方案实现为开源工具KernJC，并附带用户手册和示例演示，以便用户能够方便地使用。
* 漏洞评估：作者使用真实的内核漏洞对KernJC进行了评估，结果展示了KernJC在自动化漏洞环境生成中的有效性，使得目标漏洞在用户空间中可以被触发和复现。
* 公开数据集：作者编制并公开了一个包含2256个内核漏洞的数据集，其中1829个漏洞的脆弱版本已被识别（针对版本范围在NVD数据库中有记录的内核漏洞），1633个漏洞具有识别出的内核配置项（不包括不依赖于任何内核配置的漏洞）。

下面我们来详细介绍一下论文的内容：

## 背景

Linux内核是现代计算基础设施的核心部分，支撑着从云服务器、安卓设备到物联网节点的广泛应用。内核漏洞的利用可能带来灾难性的后果，例如在传统服务器上的权限提升、安卓设备上的root权限获取，或在云原生环境中的容器逃逸。因此，内核的安全性对于保障整个系统的稳定和安全至关重要。

近年来，Linux内核漏洞的数量持续增加，高危和极危漏洞比例也显著上升。据统计，2023年，超过40%的报告漏洞被评为高危或极危，这一趋势表明，内核的攻击面正在扩大，迫切需要更加有效的漏洞管理和修复手段。

内核漏洞复现（reproduction）是评估漏洞严重性、设计修复方案以及验证防御技术的关键环节。复现的主要目标是创建一个脆弱环境，使漏洞能够在该环境中触发，从而帮助分析漏洞的行为、测试修复方案或开发攻击防护工具。复现环境的搭建包括两个核心部分：脆弱环境（Vulnerable Environment）和漏洞概念验证程序（Proof of Concept，简称PoC）。大部分现有研究集中于PoC的生成和优化，但忽视了脆弱环境的构建，这使得漏洞复现的自动化和有效性受到了限制。

建立脆弱环境的挑战主要有以下两点：

1. 漏洞版本识别困难：现有的漏洞数据库（如NVD）提供的漏洞信息并不总是准确，许多内核版本被错误地标记为存在漏洞，导致大量时间浪费在无效的内核版本测试上。例如，NVD声称5.12以下的Linux内核版本都受到CVE-2021-22555漏洞的影响，但实际测试表明从5.11.15版本起，该漏洞已经被修复。
2. 非默认配置的需求：许多内核漏洞无法在默认配置的内核中复现，这需要安全分析人员手动调整复杂的内核配置，以激活某些子系统或模块来触发漏洞。然而，找到这些特定配置项极具挑战性，因为相关信息常常缺乏。

> 复现CVE-2021-22555漏洞所需的内核配置项
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPypyDd8MCvoGQmia7MTHzZ92j5Zu57oibXz0snRREib1XD9hLKwWYXlgUvg/640?wx_fmt=png&from=appmsg)

## 研究方法

为了解决这些问题，本文设计并实现了一个用于生成内核漏洞复现环境的自动化工具——KernJC，旨在解决上述挑战。KernJC主要由四个模块组成：漏洞信息收集模块（vulnerability profiling）、漏洞版本识别模块（vulnerability version identification）、漏洞所需内核配置项识别模块（vulnerability config identification）和环境生成模块（environment provisioning）。其中，KernJC通过两种关键方法来自动化脆弱环境的生成：基于补丁的漏洞版本识别和基于图的内核配置识别。

> KernJC设计概览
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyQWWcicErkx2xOlztAen6GQrqwPTrK3IcU79XZPa5j64ia32ro91usbxA/640?wx_fmt=png&from=appmsg)

#### 1) 基于补丁的漏洞版本识别

> 漏洞版本识别方法
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyx7aym4fkrwRmBaWzOtYhVFwRZEUn2KeibIYUSibmyUBocoibDRABDT7sQ/640?wx_fmt=png&from=appmsg)

内核漏洞的复现依赖于找到真实存在漏洞的内核版本。KernJC通过补丁对比的方式来识别目标版本是否存在漏洞，避免漏洞数据库中错误的漏洞声明带来的困扰。具体而言，KernJC会根据CVE数据库中记录的补丁信息，自动检查内核源代码的相关文件，判断补丁是否已经应用于该版本。如果补丁已经被应用，那么该内核版本即不再脆弱；否则，KernJC将确认该版本确实存在漏洞。

例如，对于CVE-2021-22555漏洞，NVD声称内核版本5.11.22仍然脆弱，但KernJC通过对补丁的分析发现，该漏洞实际上在5.11.14版本后就已修复。因此，任何高于5.11.14的版本均不再受到该漏洞的影响。

#### 2) 基于图的内核配置识别

> 漏洞所需内核配置项识别方法
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyDemC7OIb6CoR1WSWhtOmwec9v5zCO1CTNvoBAXmVMxianhdz2th012g/640?wx_fmt=png&from=appmsg)

除了找到正确的内核版本，激活某些内核漏洞还需要特定的非默认配置。KernJC使用一种图结构（graph-based approach）来识别这些配置项。该方法首先通过解析漏洞描述信息、补丁和源代码文件，找到与漏洞相关的直接配置（Direct Configs），然后基于内核自身的Kconfig和Kbuild机制生成一个内核配置图（Kconfig Graph），进一步推导出与直接配置有关的隐藏配置（Hidden Configs）。这些隐藏配置通常是漏洞依赖的核心模块或子系统配置项。

> 内核配置项的分类
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPylbDVSz3wic9cmQZ7fn5KUoxrXibZEQk5kLuu1q8dRrUn22qFxkgW3sXw/640?wx_fmt=png&from=appmsg)

下图展示了KernJC对于CVE-2021-22555漏洞的配置识别结果。可以看到，KernJC正确识别出了触发CVE-2021-22555漏洞需要的配置项。

> KernJC对于CVE-2021-22555漏洞所需配置项的识别结果
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPycEvd3lMXmIEDmwPibtfXIMG2wuCQGuhbcBfzsrY1NQ4zvwwk83b5gMA/640?wx_fmt=png&from=appmsg)

## 评估

为评估KernJC的有效性，作者构建了一个包含66个真实内核漏洞和概念性验证程序（Proof of Concept，PoC）的测试集，并从以下三个方面对KernJC进行了评估。

#### 1) 漏洞复现性能

作者使用KernJC对66个选自近五年信息安全顶会上Linux内核漏洞相关研究的漏洞进行了复现实验，结果表明KernJC能够成功构建适用于所有66个漏洞的脆弱环境。其中，32个漏洞需要非默认配置才能激活，KernJC通过自动化配置识别顺利完成了这些漏洞的复现工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPyMicPic7IAgwia5AsQEPSgO4YO9cXvYjAQib1v0vibMxAShYVvgdoaFqYvUg/640?wx_fmt=png&from=appmsg)

KernJC的版本识别方法同样表现出色，成功检测到其中4个漏洞的NVD版本声明存在错误。通过对比NVD中的漏洞声明和KernJC识别出的真实脆弱版本，作者发现例如CVE-2021-22555这样的漏洞，其实际脆弱版本比NVD记录的版本范围更窄。

#### 2) 配置识别效果

KernJC在评估过程中展示了强大的配置识别能力。通过对内核配置图的深度解析，KernJC成功识别出多个漏洞所需的隐藏配置。例如，在Netfilter子系统中的漏洞，KernJC发现了`CONFIG_NETFILTER_XT_TARGET_NFQUEUE`等关键配置，这些配置对于漏洞的激活至关重要。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPybu5nia60vRxiba5KEDxjgOsxfNSAZOMGHrv2eG5qQQSwsKXEl6c1RMFg/640?wx_fmt=png&from=appmsg)

评估结果显示，48.5%的漏洞无法在默认配置下复现，必须依赖KernJC识别出的非默认配置。此外，KernJC在复杂子系统如eBPF和Netfilter中的表现尤为突出，成功识别了多个复杂漏洞所需的内核配置项。

#### 3) 版本声明的准确性

KernJC还对NVD中的漏洞版本声明进行了大规模检测，结果显示，NVD中的128个内核漏洞存在错误的版本声明，影响了3042个内核版本。KernJC通过精确的补丁对比和代码分析，成功发现了这些错误声明，显著提高了漏洞复现的准确性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GOG6giczzHng3pRmlZTnBPy0a8nA2ibarruH0PgPibW8zzuNXLPmnWd6GN4pFnDX6zcdR8D2ANVfS4Q/640?wx_fmt=png&from=appmsg)

欢迎大家在研究和工作中使用和一起改进KernJC项目！

---

> 论文链接：https://raid2024.github.io/papers/raid2024-1.pdf
> KernJC开源项目链接：https://github.com/NUS-Curiosity/KernJC

---

投稿作者简介：

> 阮博男，2024级新加坡国立大学博士生，导师为梁振凯老师，目前主要研究方向为漏洞挖掘和漏洞评估，相关研究成果发表在ASE、RAID等软件工程和信息安全领域的国际会议上，也曾在KCon、CIS等国内工业界知名信息安全会议上发表演讲。

> 个人主页：https://profile.wohin.me/

> 对NUS Curiosity Research Group感兴趣的读者，可以关注梁振凯老师，梁老师招收系统安全方向的博士生和博士后，详细信息可以参考：

> 梁振凯老师个人主页：https://www.comp.nus.edu.sg/~liangzk/
> NUS Curiosity研究小组主页：https://nus-curiosity.github.io/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过