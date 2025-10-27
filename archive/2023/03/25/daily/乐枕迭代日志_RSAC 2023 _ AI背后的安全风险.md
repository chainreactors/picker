---
title: RSAC 2023 / AI背后的安全风险
url: https://mp.weixin.qq.com/s?__biz=MzA3NTMyNDg3OQ==&mid=2652519538&idx=1&sn=4079998bad994dde4d4b71ea3671f254&chksm=849cd0d2b3eb59c48f8183f253709df84144e973aaa4162ca57904befd03b00521e5f1ad2710&scene=58&subscene=0#rd
source: 乐枕迭代日志
date: 2023-03-25
fetch_date: 2025-10-04T10:39:46.549294
---

# RSAC 2023 / AI背后的安全风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJPtYF2TpqxjJ2RDpJXEGNb0GJLCI2ycXPdJ7icA5nlmIdCIICFHjic3YQ/0?wx_fmt=jpeg)

# RSAC 2023 / AI背后的安全风险

原创

cdxy

乐枕迭代日志

RSAC创新沙盒 作为安全行业全球性的创新风向标，每年评选出Top 10初创厂商，18年来这些厂商共收获了125亿美元投资和75次收购。

今年的Final List中包含三家数据/隐私厂商，一家AI模型防护厂商，让人很难不与最近ChatGPT的爆火联系到一起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJlbabUOe9sP5PO0hicEb6rf5BBsA94NzsT4V8z1IxfY4AZETVZjGsd6g/640?wx_fmt=jpeg)

AI安全场景

* 软件系统的安全性（AI Application Security）：将AI视作一个软件，背后的代码、开发与运维环境、软件供应链等基础设施都存在被攻破的可能。
* 模型的安全性（AI Model Security）：针对模型算法和数据的特性建立的对抗手段。
* 合规问题：数据隐私方面如联邦学习、安全多方计算和同态加密、数据安全管理；内容风控方面AIGC和其他GC一样，针对AI输出内容都要有意识形态上的限制。

AI系统攻击链

2022年微软与MITRE和其他16个组织一起创建了ML威胁矩阵「ATLAS」。该威胁矩阵以我们熟知的ATT&CK框架为蓝本，填充了不同阶段针对AI系统的攻击方法，从而对AI系统的威胁进行分类。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJLib9h6LjcrFzJFMwHGsiaZA6feoGRXlCqzlcxgJooZltQRRQbQ7SodaA/640?wx_fmt=png)

https://atlas.mitre.org/matrices/ATLAS

此威胁矩阵重在 **强调ML模型层的对抗方式，及围绕这些新的攻击方式所构建的攻击链路**，包括信息收集、持久化等原有技术的调整，偏实战化。

同时，此威胁矩阵继承了很多传统Application Security的攻击手段。

AI模型对抗

Adversarial Robustness Toolbox项目由IBM发起，后捐赠给Linux Foundation for AI。该项目从adversarial machine learning的科研视角，将攻击定义为**投毒(Poisoning)、逃逸(Evasion)、模型提取(Extraction)和推断(Inference)**四大类，并从红蓝对抗的角度，给出了常见攻击方法(算法)和检测方法的工具化实现。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJrpDMxo1dThsUc6JoDHfQqhyTxHB8cyonAu2ROzMAHtKiaQk9iatjVDkA/640?wx_fmt=png)

https://github.com/Trusted-AI/adversarial-robustness-toolbox

投毒(Poisoning)：攻击者操纵训练数据集，让机器学习到错误的知识，从而影响其判断效果。

例如：你家门口装了安全摄像头。攻击者可能每天凌晨3点路过你家，让他的狗穿过草坪，从而触发安全警报。那个遛狗的人实际上在提供训练数据，让安全系统知道每天凌晨3点发生的事是无害的。当系统被训练成「忽略凌晨3点发生的任何事情」后，攻击者就趁机发起攻击。

逃逸(Evasion)：不破坏目标AI系统，通过构造特定输入样本以达到欺骗目标系统的效果。

在上例中，攻击者可以穿上狗服，绕过摄像头的检测。

模型提取(Extraction)：攻击者获取AI系统的副本进行调试，反复试探将自己的攻击模型伪造成合法的行为方式。

在上例中，攻击者可以弄一副望远镜观察你家的摄像头是什么型号，然后买同款摄像头自己尝试如何绕过检测。

推断(Inference)：攻击者获取到用于训练的数据集，然后利用数据中的漏洞或偏差实施攻击。

在上例中，攻击者可能会监视你的房子，摸清楚附近路人车辆情况。当攻击者注意到每天凌晨3点有遛狗者经过、并且安全系统会忽视遛狗者时，就有可能利用这一规律实施攻击。

AI合规问题

**隐私**

> 如果某些东西是免费的，我们很可能在用我们的数据来支付费用。

隐私需求的崛起是数据价值显化的结果，AI的现象级应用推动了这个进程。

对于AI模型构建者来讲，合法获取训练数据是一个挑战。在ChatGPT开放的过程中，有用户发现AI向其他用户泄露了自己的电话号码。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJxokGvon1uWFXtdrqJDIxdoKmQrIicFNea9RflerLc9kX7dCNGrIn5icQ/640?wx_fmt=png)

https://twitter.com/DaveLeeFT/status/1626288109339176962

同时，对于B端产品而言，大量工作中的效率工具集成AI能力后，这种数据回传或员工不经意间输入的「问题」都可能会导致企业信息泄露。

在以公司/业务为主体的B端数据共享场景中，如何既保证数据的使用价值，又不泄露数据内容，也需要专业的解决方案来实现。

**内容审查**

AI的世界里也要受意识形态的限制。

ChatGPT Jailbreak指利用一些prompt技巧如：模拟游戏、模拟梦境等方法，使得ChatGPT不再受内容策略限制，生产违规内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJtibict2UJ8BQBibOCeC4szMqaXMBjF51gahDUibwHKicUSPIctUsP5n5ibvg/640?wx_fmt=jpeg)

我国2022年12月颁布的《互联网信息服务深度合成管理规定》中，针对“深度合成技术”服务提供者提出“对用户输入数据和合成结果进行审核、建立违法和不良信息特征库、建立健全辟谣机制”等要求。

在此情况下，AI供应商在创立之初就不得不在商业模型的画布上记下合规成本，并寻求专业供应商建议。

AI安全解决方案

Gartner对AI风险管理的粗略定义中，模型+数据=ModelOps，此外还包含了Application Security、数据隐私。内容审查方面的能力并未加入其中。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJvkNYctI8iaG6OWbpsflaFiaKvB5DnJQmSTsq32kKFEeEDbBvDVATXjvw/640?wx_fmt=png)

Gartner: "Market Guide for AI Trust, Risk and Security Management", 2023

**Hiddenlayer MLDR**

AI模型层的攻防，有两个安全能力植入点：

1. ModelOps流程（类比DevOps->Dev**Sec**Ops）

2. Runtime防护（类比防火墙）

从早先的 EDR、NDR 到 ITDR、MLDR（Machine Learning Detection & Response）被提出，安全领域“万物皆DR”，说不定过段时间还能看到"ModelSecOps"大旗。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJUJV9g2B1e4p9JTraEuGwammiavE5lOhVC9XcSkcic9nzV0jOmDuBiaVkQ/640?wx_fmt=png)

**Bosch AI Shield**

模型弱点扫描+运行时攻击行为阻断+威胁运营（SIEM集成）。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJBOKeeqpVBQeLC4lkP8ajw7JSTgwUbeqakOGY4NrYxOR8b2JDn9sqZQ/640?wx_fmt=png)

**TROJ.AI**

对抗样本测试、模型审计（类似安全基线的概念）、训练数据扫描、模型防火墙。

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJFN7Ua5nnicax9ko3M7iatibtqib6EREcXK6Fv2iaNiahiaA1yk9DIo5h41xSA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZwdYa2Jvibicy8MasXiaVQicMjJl0xYX5C25HWfNI13PqMdWpErBHibT6ersOLtm1EADaKpgsia0vSumyFw/640?wx_fmt=png)

AI可能改变世界，不过暂时还没改变安全行业的造词逻辑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZxy3icZpxoTMM34X5EN2YSSIydevicOVoCxUjH4CdTxAOWrzia7RVFBrVAmlWdLdKjyAhBWcQbEU5VicA/0?wx_fmt=png)

乐枕迭代日志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WdJky8oWwZxy3icZpxoTMM34X5EN2YSSIydevicOVoCxUjH4CdTxAOWrzia7RVFBrVAmlWdLdKjyAhBWcQbEU5VicA/0?wx_fmt=png)

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