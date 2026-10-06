---
title: ISO/SAE 21434 标准解析：道路车辆网络安全工程的组织与项目级管理
url: https://mp.weixin.qq.com/s/n7e0pztUDM5iXqO9u50Rgg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:41.241745
---

# ISO/SAE 21434 标准解析：道路车辆网络安全工程的组织与项目级管理

# ISO/SAE 21434 标准解析：道路车辆网络安全工程的组织与项目级管理

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

ISO国际标准化组织于2021年8月31日正式发布了汽车信息安全领域首个国际标准ISO/SAE 21434《Road vehicles—Cybersecurity engineering（道路车辆-信息安全工程）》。目的是就重要的网络安全问题达成全行业协议，并确保整个供应链具有支持设计方法安全的过程。标准共由15个章节组成，其中主体部分为4-15章。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvNQDRfyzqrNLg3tJDBK6nOmMmpRcD2ic6aGQrhkWhVG2Ijk2TuKjTEeNA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvNorIDFOoZialA68F6tu22BSdqT6iaYzKuIcpV6STxU0YvpTYPmOqaHjicw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**01**

**概述**

该章节对21434进行了一个总括性的描述，总结下来说了两件事：

1. 研究对象和范围
2. 风险管理的概念

**1. 研究对象和范围**

在21434中，网络安全工程的研究对象被称为item，可翻译为“相关项”, item的定义为：实现整车特定功能的相关电子器件和软件。它包含了一个或多个Component以及其之间的交互和运行环境。Item可以是车辆的E/E架构或实现车辆某个功能的系统（如刹车系统）。

21434标准只在item层面描述网络安全工程的相关活动，不会规定分配到组件上的具体工程方案。

网络安全工程的范围涵盖车辆的全生命周期，因此也包括了售后和服务环节。车辆外部的系统（如后台）在标准中也会涉及，但不是该文件研究的重点。总结来说，21434是一项针对车端的网络安全规范。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvNs9ibOEjQ6zajc5bDowOWKB8qBQh84ia7aH9KlOqLmsbCibgicFztE2A2cQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**2. 风险管理**

风险管理是21434的核心概念，它是一项贯穿产品整个生命周期的持续性活动。在开发阶段，主要关注威胁分析和风险评估（第15章）以及通过纵深防御缓解网络安全风险；在运维阶段，通过安全监控、漏洞管理和安全事件响应等持续的网络安全活动（第8章），处置不断变化的外部环境中出现的安全风险。此外，风险管理活动可针对项目进行相应的适配和裁剪（第6章），对于分布式开发的环节，需要明确客户与供应商的网络安全职责（第7章）。

**02**

**组织级网络安全管理**

第5章 组织级网络安全管理（organizational cybersecurity management）规定了公司/组织层面网络安全管理的要求，是组织内部最高层面的安全方针，标准中从7个方面提出了要求：

* 网络安全治理（cybersecurity governance）
* 网络安全文化（cybersecurity culture）
* 信息共享（Information Sharing）
* 管理体系（Management System）
* 工具管理（Tool Management）
* 信息安全管理（Information security management）
* 组织网络安全审计（organization cybersecurity audit）

**1. 网络安全治理（cybersecurity governance）**

网络安全治理是最宏观层面的安全治理方针，总共有5条要求，可总结为以下几点：

* 领导层重视

公司管理层必须具备车辆网络安全风险管理的意识，并且承诺对车辆的网络安全风险进行管理。

* 流程保证

建立网络安全管理体系（CSMS）来支持相关网络安全活动的实施，CSMS涵盖了概念、开发、生产、运维、退役、TARA方法论，安全监控，信息共享，应急响应等21434中提及的所有环节的相关流程定义，指导手册，方法论和模板多级文件。

* 职责划分

组织必须为CSMS中定义的各项网络安全活动分配相应的职责部门/人员，确保相关的活动能够真正实施。

* 资源保证

组织必须提供足够的资源以保证网络安全活动的正确实施。资源包括了足够的、具备合格能力的人员，合适的工具等。

* 与其他现有流程的结合

组织应考虑如何将网络安全管理活动嵌入组织现有的开发流程、质量管理流程中。于此同时，还应考虑网络安全体系与功能安全、隐私保护等其他安全领域的交互和融合。

**2. 网络安全文化（cybersecurity culture)**

这一节规定了组织实施网络安全管理需具备的“软实力”，可归结为以下3点：

* 建立良好的网络安全文化

对于什么是“良好”的网络安全文化，可参考文件后的附录B，内容和26262中提及的安全文化示例基本一致。

* 保证人员足够的网络安全能力和意识

能力涵盖了多个方面，如具备网络风险管理、功能安全、隐私保护等相关领域的知识，掌握车辆工程，系统开发的基本知识，了解常见的攻击方法，安全防护措施等。

* 持续改进

持续改进需贯穿在网络安全工程的所有活动中，改进可以来源于内/外部的监控获取的信息、lessons learn, 相似项目的经验，开发过程中发现的问题、体系/流程审核中发现的问题等。

**3. 信息共享（Information Sharing)**

信息共享要求组织必须考虑组织内外部哪些数据共享是必须的、允许的，哪些是被禁止的，并根据这个准则去管理与第三方共享的数据。

在具体实施层面，通常会对信息进行分级，制定相关的信息共享流程，使用专门的信息传输工具，与第三方确定漏洞披露原则等。

**4. 管理体系（Management System)**

组织应建立一个质量管理体系来支撑网络安全工程。主要支持网络安全工程中的变更管理、文档管理、配置管理和需求管理。其中产品的安全配置信息必须在产品终止维护前保持可用。此外，本节中还建议组织制定生产制造环节的网络安全管理体系。

目前行业内绝大部分企业都通过了16949的认证，在实际实施中需要考虑的是将网络安全开发活动纳入原有的变更、文档、配置和需求管理等质量管理流程之中。

**5. 工具管理（Tool Management)**

组织应对能够影响相关项和组件网络安全的工具进行管理，这些工具可能包括:

* 开发过程中的工具如模型开发，静态代码检查，验证工具。
* 生产中的工具如软件刷写工具、产线检测仪。
* 运维阶段的工具如在线诊断工具等。

工具可以通过以下的方法进行管理：使用用户手册和勘误表，访问控制，权限控制，预防非预期行为和操作等。

此外，本节还建议在产品退役前，应保持相关环境（如软件编译、开发环境、测试环境）可复制，以便在后续发生网络安全事件时，可对漏洞进行复现和管理。

**6. 信息安全管理（Information security management)**

建议：相关的工作产品应该由一个信息安全管理系统来管理。对于已经建立完善的信息安全管理体系的组织来说，将网络安全的工作产品依照现有的信息安全管理流程进行管理即可。

**7. 网络安全审计（organization cybersecurity audit）**

组织应进行网络安全审计，以判断组织的流程是否达到了本标准的要求。需要注意几点：

* 审计人可以来自组织内部或外部，但必须保证审计的独立性，关于独立性的要求可以参考26262中的相关描述。
* 网络安全审计可以包含在质量体系的审计中（如IATF 16949）。
* 审计可以分阶段进行

**03**

**项目相关的网络安全管理**

项目相关的网络安全管理（Project dependent cybersecurity management) 一章描述了普适性的针对项目网络安全活动的管理原则。包括各项活动的职责分配（6.4.1），制定网络安全活动计划（6.4.2），裁剪原则（6.4.3），以及网络安全案例（6.4.7）和网络安全评估（6.4.8）、后开发阶段释放的要求（6.4.9）

**1. 网络安全职责**

分配和通报有关项目网络安全活动的责任。

注释：网络安全活动的责任可以转移，但必须进行沟通并提供相关信息。

输出物：在输出物CyberSecurity\_Plan文档里定义好相关角色及职责划分。

**2. 网络安全计划**

网络安全相关性判定：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvNW0HvtXZ9VZvGgh2TWZFYOkdXLeJYiboJia0Kuqpib2sfjmyNFN6hSlQmA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

* T-BOX/TCU或者网关节点
* 有功能安全等级的节点（尤其是ASIL C/D）
* 存储/处理与驾驶员/车辆有关数据的节点
* 有无线连接的节点（例如蓝牙、NFC、WIFI等）
* 有外部连接的节点（总线、OBD、蜂窝网络等）

网络安全计划应包括以下内容：

1. Objectives：活动需要有目标

2. Dependencies：活动之间有依赖关系

* 网络安全的计划需要和整个项目计划匹配
* 如果一些活动不做，另外一些活动就不能展开

3. 联系人：负责执行一项活动的人员。

4. 资源：执行一项活动所需的资源：人财物，多少钱，测试，几个样件，什么测试设备，测试人员

5. schedule：活动的起点或终点，以及预计持续时间；以及

6. Work Products：确定要产生的工作成果。

当发现需要执行的活动发生变化或改进时，应更新网络安全计划。

**3. 网络安全活动的裁剪**

可以对网络安全活动进行裁剪。如果网络安全活动被裁剪了，应提供说明，用来证明可以通过裁剪充分实现本标准的相关目标。

**1. 复用**

如果一个功能项或组件已经开发出来，并且符合以下情况，应进行重用分析。

* 计划进行修改。
* 计划在另一个运行环境中重新使用；或
* 计划在不进行修改的情况下重新使用，并且与该项目或部件有关的信息发生了相关变化。

a. 复用分析：

两个客户项目要做哪些修改，运行环境有哪些变化，有哪些信息更新，delta分析

b. 这些差异影响到定义中的活动

有些活动可以裁剪，有些活动甚至要增加或更新

2. 非特定场景组件 out of context

平台项目，做了很多假设

Generic performance，平台化产品，用在不同的客户项目上

给到客户项目，在平台已有的假设需求上考虑客户要求，做相关的网络安全计划调整

3. 外部组件 Off the shelf

由第三方机构开发的软件库或者开源的软件组件，可以嵌入到项目中去的

**04**

**网络安全案例**

创建一个网络安全事例，收集Work Products，为网络安全水平提供证据，有些活动如果理由充分，可以裁剪。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvN2SWNRgoZX4LrbJEEF8p3g1PJb3uMs3KbibzgmLee4gxib6WziauRbWrQw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvNNgmzFF1gHB7HAKFXwQfe1UFTYG5W8MOAYGtxFEOrPSupcopXrT5ib6w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**05**

**网络安全评估**

判断网络安全活动有没有执行到位

不做的话要说明理由，理由要进行独立评审

独立的评估：独立性

网络安全评估包括：

* Work Products有没有按计划逐一到位，写的符不符合规则
* 网络安全的控制，活动有没有落实执行
* 相关的目标有没有达成
* 网络安全风险的处置合不合理

网络安全评审结果包括：

* recommendation for acceptance
* Conditional acceptance
* Rejection

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8NoiaqNdrfPLaAKRMrXiblvNTMO8yD6dCum3AvTdRJAIq8Dl3vFsqlAAGoW8ibXzyBRfngTvr0iaygBw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

**06**

**后开发的释放**

1. cybersecurity case准备就绪

2. cybersecurity assessmenty要是绿灯或黄灯

3. 后开发阶段网络安全的要求文档（第十章）

都满足之后，可以发布放行

在已有的发布流程中，加入网络安全的发布流程。

原文链接：

https://blog.csdn.net/2301\_76563067/article/details/145143238

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jb...