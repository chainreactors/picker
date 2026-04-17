---
title: 成果分享｜[IEEE S&amp;P 2025] HouseFuzz: 让模糊测试真正理解固件网络服务
url: https://mp.weixin.qq.com/s/ewvWBsF3H-4JQgKHdb-L3w
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:46:05.630656
---

# 成果分享｜[IEEE S&amp;P 2025] HouseFuzz: 让模糊测试真正理解固件网络服务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0mdnIU7wBrrYT0l5ibTLy2qiaKBsozatWlHqS8THD8dHN6P8yl3ckricibJ5H5ialC7RhjoMIUhr4s65nM4Criaz7rVphicj8TQlHMhwdibv1eSTZdY/0?wx_fmt=jpeg)

# 成果分享｜[IEEE S&P 2025] HouseFuzz: 让模糊测试真正理解固件网络服务

原创

复旦白泽战队
复旦白泽战队

复旦白泽战队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

导语

在IoT设备无处不在的今天，固件安全绝非小众问题。路由器、摄像头、打印机、NAS等设备背后，运行着大量基于Linux的固件系统；一旦其中的网络服务存在漏洞，攻击者就可能直接从网络侧发起利用，造成远程代码执行、隐私泄露等严重后果。

近年来，灰盒模糊测试已成为固件漏洞挖掘的重要手段。然而，现有方法普遍忽略了固件服务的两个关键特性：一是“一个服务往往并不是一个进程，而是由 多个协同进程 共同支撑”；二是“服务协议中常常包含 厂商定制的语义约束 ”。这使得它们在服务识别、覆盖反馈和输入生成等方面都受到明显限制。

为此，我们提出HouseFuzz——一个具备多进程感知和协议定制化感知能力的Linux固件灰盒模糊测试框架。与前沿方法相比，HouseFuzz实现了 33.4% 的代码覆盖率提升和 175% 的零日漏洞发现能力提升，共发现 156 个零日漏洞，并获得 45 个CVE/CNVD编号。

论文地址：

https://ieeexplore.ieee.org/document/11023421

项目链接：

https://github.com/HouseFuzz/HouseFuzz

**为什么现有固件模糊测试还不够有效？**

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrr2pYyicz7oicjfgguONOWjd5quKlgrtKUnqnHKYkwvEDWoAGP9PUz9eXKGZagt3jr3FOjq4khPvfc82icYrBcAzlp1B1YibRcb2Ac/640?wx_fmt=png&from=appmsg)

**1. 服务识别不完整：关键进程未进入测试范围**

现有方法要么依赖启发式信息来确定测试目标，只锁定表层的网络进程，而忽略未被规则记录的网络进程和守护进程；要么受限于系统模拟的不稳定性，网络服务往往还未被完整识别就已经崩溃退出。这样一来，服务边界在一开始就被缩小了，后续测试自然难以覆盖完整逻辑。

**2. 缺乏多进程感知：误判了服务的测试边界**

灰盒模糊测试之所以有效，关键在于它不会盲目乱试，而是会利用程序执行过程中产生的覆盖反馈，不断调整输入，逼近更深层代码。因此，执行反馈的质量直接影响了灰盒模糊测试的聪明程度。

然而，现有的模糊测试技术误判了执行反馈的目标边界：只围绕单个进程收集代码覆盖信息，而忽略了其它协同进程的高价值执行反馈。这导致跨进程触发的执行路径无法被完整观察，代码探索效率自然大打折扣。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0mdnIU7wBrqUeUvic97whicHcMke2qdgHSYFGpNhXWSCjnNyIZYkbwyiauU0ibOj2a17QV0LfZ2rMLmQgH1S4NXt4ia6gW9DY9wl1B4AxahSEfia4/640?wx_fmt=jpeg&from=appmsg)

**3. 缺乏定制化协议感知：只能盲目地生成输入**

固件服务常常运行在 HTTP、UPnP 等常见协议之上，但其应用层消息中通常带有大量厂商自定义字段和语义依赖。例如，不同字段之间可能存在严格的取值约束。然而，现有固件模糊测试的输入生成往往仅停留在语法层面，或采用随机输入变异策略。因此，它们难以生成满足这些定制化语义要求的测试用例，从而难以通过前置校验并触发位于核心服务代码中的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0mdnIU7wBrpVwfyTCiaAhpxU8CfJ8XvibpUDwYQXu5nJe5cIo27p7IulQ3zMPmjl88mMpYUNm2ibYicQKmTY0GNbF6YqHbSFbYTfS4lyptCkDib4/640?wx_fmt=jpeg&from=appmsg)

**破局之道：充分感知服务特性**

针对上述三个瓶颈，HouseFuzz分别从服务识别、反馈建模和输入生成三个层面进行设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0mdnIU7wBrrty7MzLe2tic6FqYP7zr2RjxMKBvuNRA6pT7U1sialib6ThjnDJucwrRaDwoQVRypickHklicNWRHsYo9h6ZMMeIhv7BDKc5GWEOm0/640?wx_fmt=jpeg&from=appmsg)

HouseFuzz架构图

**1. 更全面地识别真实网络服务**

HouseFuzz不再将网络服务简单等同于某个监听端口对应的单个进程，而是沿着固件系统初始化过程进行分析，识别启动过程中被实际拉起并参与服务运行的进程集合。在初始化过程中，HouseFuzz从执行日志中自动识别可能导致服务崩溃和阻塞的直接原因，并加以修复。通过这种方式，HouseFuzz能够更完整地恢复真实服务边界，避免遗漏网络服务与对漏洞触发具有关键作用的后台进程。

**2. 多进程模糊测试框架**

在模糊测试阶段，HouseFuzz将与目标服务相关的多个进程共同纳入监控范围，统一收集覆盖反馈，并据此指导后续测试输入生成。相比传统单进程反馈机制，这种方式能够更准确地反映服务整体执行状态，也更适合发现跨进程传播和触发的漏洞。

**3. 定制协议语义约束提取**

针对固件服务中的定制化协议，HouseFuzz结合离线分析与在线分析提取输入中的语义约束，并利用这些约束指导测试用例生成。其核心目标，是让生成的输入不仅“格式合法”，而且“语义合理”，从而提高测试用例穿透多层检查逻辑、触达深层代码路径的能力。

**研究结果：这一关键想法带来的显著提升**

我们在大规模真实 Linux 固件样本上对 HouseFuzz 进行了系统评估，结果表明，该方法在多个关键指标上均优于现有前沿方法。

**1. 识别出更多真实网络服务**

首先，HouseFuzz能够识别出更完整的服务边界。与现有方法相比，其识别出的网络服务数量显著增加，整体上可多识别76%的网络服务。这一结果说明，许多原本被忽视的服务组件，在更精细的启动分析下可以被有效恢复。

**2. 提升模糊测试的覆盖深度**

其次，HouseFuzz能覆盖更深层代码。在相同服务上，HouseFuzz 利用多进程反馈机制和语义约束感知输入生成，能够探索到更多有效执行路径，实现33.4%的代码覆盖率提升。这说明其不仅扩大了测试目标范围，也提升了对已有目标的测试深度。

**3. 挖掘出更多真实零日漏洞**

更直观的是，HouseFuzz挖到了更多漏洞。HouseFuzz 比前沿方法多发现了175%的零日漏洞，共发现156个零日漏洞，并获得45个CVE/CNVD 编号。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrpbf3WHLqeY0jpEf6T4mDfZRJdSUakGWbHnJalkINzfHCdV9PyTeqa3UqibghlMtvGKwtZqQW6LCdgpYyMeMxZmI9O02rRU6uicM/640?wx_fmt=png&from=appmsg)

这些结果表明，多进程感知和协议定制化感知的灰盒模糊测试设计能够切实提升 Linux 固件漏洞挖掘的有效性。

**结语**

HouseFuzz 聚焦于现有模糊测试方法中的一个共性问题，即对固件服务的真实形态考虑不够充分。一方面，Linux 固件中的网络服务通常不是一个孤立进程；另一方面，很多关键逻辑也并不能仅靠通用协议格式触达。若测试系统不能识别真实的服务边界，不能观察多进程协同行为，也不能理解输入中的定制化语义约束，那么漏洞挖掘效果就很容易受到限制。

针对这些问题，HouseFuzz 进行了系统设计，并在真实固件样本上取得了较为明显的提升。相比现有方法，它不仅识别出更多网络服务、获得更高的代码覆盖率，也发现了更多真实漏洞。这也充分印证了感知固件服务的多进程与协议定制化特性，能够使模糊测试更加智能和高效。

**作者简介**

肖浩宇，复旦大学计算与智能创新学院系统软件与安全实验室博士研究生，师从杨珉教授、张源教授，研究方向主要包括软件安全、程序分析与模糊测试，重点关注嵌入式系统安全，尤其是IoT固件安全。相关研究成果发表于安全领域顶级会议IEEE S&P、CCS、USENIX Security和NDSS。个人主页：https://haoyu-xiao.github.io。

魏子淇，复旦大学计算与智能创新学院系统软件与安全实验室硕士研究生，师从杨珉教授、张源教授。研究方向主要包括物联网与嵌入式系统安全，重点关注静态与动态程序分析，以及嵌入式固件中内存与逻辑漏洞的检测。相关成果发表于安全领域顶级会议IEEE S&P和CCS。

素材：肖浩宇

排版：陈驰

责编：董佳仪

审核：张琬琪、洪赓

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、小红书搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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