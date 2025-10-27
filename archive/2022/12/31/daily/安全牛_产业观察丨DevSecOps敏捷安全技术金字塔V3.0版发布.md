---
title: 产业观察丨DevSecOps敏捷安全技术金字塔V3.0版发布
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121182&idx=2&sn=b146d40316e3ebed8a73ef5fde88f468&chksm=bd1456cd8a63dfdb3d69bbac8d0cc802456b9e293a45d7309371d25a802e37a300710b305142&scene=58&subscene=0#rd
source: 安全牛
date: 2022-12-31
fetch_date: 2025-10-04T02:48:02.437753
---

# 产业观察丨DevSecOps敏捷安全技术金字塔V3.0版发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkBZULPf7Wpjvq1CibteDEbcCFic9zLEhia55coj2drPPwWjib3NIdPdiacpHvNjqb5iaibQyFgjXJdn53KeQ/0?wx_fmt=jpeg)

# 产业观察丨DevSecOps敏捷安全技术金字塔V3.0版发布

止黑守白

安全牛

2022年12月28日，由悬镜安全主办，3S-Lab软件供应链安全实验室、Linux基金会OpenChain社区、ISC、OpenSCA社区联合协办的第二届全球DevSecOps敏捷安全大会（DSO 2022）已线上直播形式圆满举行。

本届大会以“共生·敏捷·进化”为主题，以“敏捷共生，守护中国软件供应链安全”为使命，聚焦DevSecOps敏捷安全、软件供应链安全和云原生安全三大典型应用场景下的新技术、新态势、新实践。在本次会议中，大会出品人、悬镜安全创始人子芽正式发布第三版DevSecOps敏捷安全技术金字塔。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZULPf7Wpjvq1CibteDEbcCicic2yuJ7aZhBWiaZh9Z73EyFBibS8uLtbdAibV2MS125Q2ygEtCaQShTnQ/640?wx_fmt=png)

图1 DevSecOps敏捷安全技术金字塔V3.0

作为DevSecOps敏捷安全技术的实践指南，本次发布的3.0版本不仅延续了敏捷安全技术分层与企业组织DevSecOps成熟度非正比关系的编排原则，还引入了跨领域新技术与敏捷安全技术进行深入的实践融合。DevSecOps敏捷安全技术金字塔V3.0根据不同阶段相关技术的应用成熟度和落地效果进一步细化了敏捷安全应用实践的阶层，包含传统建设层、应用实践层（敏捷安全实践第一层）、技术探索层、效果度量层和卓越层（最高层）共五个阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZULPf7Wpjvq1CibteDEbcCRT6mGT25jicthWfibcd0AXkXTBpXriaicRhicCC0ZWxctDlgTDTM3gGsMRw/640?wx_fmt=png)

图2 DevSecOps敏捷安全技术金字塔-演进对比

**传统建设层**

**WAF、EDR、Deception、CKS、ASTs**

从网络安全技术演进和传统纵深防御体系构筑的视角，典型实用的安全技术主要分为边界流量分析技术、端点环境检测响应技术和应用情境感知响应技术。

在金字塔V3.0中，首次将Deception（攻击欺骗）和CKS（容器和K8s安全）纳入并置于传统建设层，主要是考虑到趋势发展和相关应用实践的成熟性。作为传统纵深防御关键技术的WAF、EDR以及ASTs依然入选。其中ASTs包括了SAST（白盒）、DAST（黑盒）和MAST（移动应用安全）三种传统应用安全测试技术。

**应用实践层**

**IAST、SCA、RASP、BAS**

在应用实践层中，涵盖了四种既能在日常应用实践过程中具备较好应用效果，又能与DevOps CI/CD管道柔和融合的创新技术。

其中，RASP（Runtime Application Self-protection，运行时应用自我保护）由于在0DAY未知漏洞攻击防御、API威胁免疫、红蓝对抗、软件供应链攻击防御及应用东西向威胁流量检测响应过程中相对出色的表现预期以及技术性能的大幅度提升，日渐被市场青睐，从过往所处的技术探索层踊跃至DevSecOps敏捷安全技术实践的第一层。子芽预测，在接下来的三年中，RASP在HW、红蓝对抗等场景下会有更加广泛的市场应用。

**技术探索层**

**DRA、SDE、Fuzzing**

作为DevSecOps敏捷安全技术实践的第二层，引入的创新技术都是具备强技术突破性，可具体解决某类应用场景下突出问题，但在通用应用效果、市场需求和实践方面还有巨大提升潜力的前瞻性技术。

DRA（Data Risk Assessment，数据风险评估）是首次引入金字塔的创新技术，作为开展数据安全治理工作的基础， DRA主要关注数据安全风险包括数据传输、个人隐私、数据生命周期管理、技术漏洞等，不但受国家法律和监管要求的强推动，而且是DevSecOps敏捷安全技术实战需求。

同样作为首次引入金字塔的创新技术，SDE（Securing Development Environment，开发环境安全）涉及保护完整的软件开发环境，包括但不限于源代码存储库、CI/CD 管道、应用程序工件和用户身份信息。鉴于软件供应链攻击、开源工具的广泛使用以及远程工作方式导致的风险增加，保护开发环境变得至关重要。

这一层中第三个创新技术是连续三次引入金字塔的Fuzzing（API模糊测试），聚焦未知漏洞挖掘和异常风险发现。子芽表示，受限于其独特的技术原理和高应用门槛，对常态化使用它的用户有着较高的专业技能要求，且在检测精度、技术性能上有较大提升空间，Fuzzing未来仍需要一段时间才能成熟。

**效果度量层**

**ASOC、CNAPP**

作为DevSecOps敏捷安全技术实践的第三层，引入的都是框架型平台技术，侧重于提升整个敏捷安全体系的运营效率，但在市场需求和实践方面尚有巨大提升潜力。ASOC（Application Security Orchestration and Correlation，应用安全编排与关联）也是首次引入金字塔的创新技术。它是由过往版本金字塔中的ASTO（Application Security Testing Orchestration，应用安全测试自动化编排）和AVC（Application Vulnerability Correlation，应用程序漏洞关联）两项技术合并而成，核心优势在于可以较大程度提高DevSecOps的运行效率，可将面向应用安全（Appsec）的DevSecOps敏捷安全工具链真正运营起来，是安全左移实践思想的重要落地抓手。ASTO强调的是向下编排安全工具链，以智能自动化的方式来完成安全活动；AVC则从漏洞入手，针对各种AST工具长久以来无法解决的误报、重复等问题，引入漏洞关联分析手段协助用户进行更好的修复优先级判断。

CNAPP（Cloud-Native Application Protection Platform，云原生应用保护平台）同样是首次引入，它不是简单拼凑工具，而是一个云原生安全框架型技术，通过将现有的云安全技术融合到一个统一的面向应用全生命周期的解决方案中，并将已经存在的单点防护进行整合，实现了从代码开发到构建再到部署运行整个应用生命周期的安全可视化以及安全防护。

**卓越层**

**CARTA**

作为DevSecOps敏捷安全技术实践的最高层，也是DevSecOps敏捷安全体系建设的终极愿景，连续三年被CARTA占据。CARTA（Continuous Adaptive Risk and Trust Assessment，自适应风险与信任评估）从规划、构建、运营三个维度动态评估企业的数字化业务在整个软件全生命周期中面临的风险和信任，不追求零风险，不要求100%信任，持续构建一个信任和弹性的研运一体化安全环境，使得企业组织能够敏捷地、和业务共生地、持续进化地参与到软件供应链安全建设和保障中去。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZULPf7Wpjvq1CibteDEbcCepVF6St26mlXarfd4WeBqUicT1HobGw1qwjDq1mgpgjpHlfMWRPFfOQ/640?wx_fmt=png)

图3 CARTA自适应风险与信任评估框架

子芽表示，网络安全的本质是风险和信任的动态平衡。DevSecOps不是安全开发和安全运营的简单结合，安全开发的终点也不能简单归结为漏洞处置，安全运营的终点亦不能简单归结为威胁响应，而是应以终（漏洞处置和威胁响应）为始，回归应用和体系，以人为本，结合智能自动化技术实现共生、敏捷、进化的安全新局面，形成真正意义上的应用全生命周期持续安全大循环，这才是DevSecOps敏捷安全体系建设的终极愿景，也正是DevSecOps莫比乌斯环所真正象征的意义。

相关阅读

[从 DevSecOps 流程视角看 IAST 技术应用与发展](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651107909&idx=1&sn=cadbb22d61980c73e05629e0ef96778c&chksm=bd1402968a638b80804a28576edecc624117b2fa5c6ff8fc1e3f5cbe510898a84a79ebbca6d1&scene=21#wechat_redirect)

[漏洞高检出＋脏数据拦截：构建“出厂即安全”的DevSecOps流程](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651109718&idx=2&sn=e10a7fe826241c1354c881db1507dee1&chksm=bd1409858a6380934dce2a449f11490454c4d1984abd7fbb2374ec470c32823bb4c938a2516e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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