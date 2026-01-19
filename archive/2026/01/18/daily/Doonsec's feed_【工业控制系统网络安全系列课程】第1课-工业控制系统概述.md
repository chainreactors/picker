---
title: 【工业控制系统网络安全系列课程】第1课-工业控制系统概述
url: https://mp.weixin.qq.com/s/j6xLz_6LSqYE_zbHw0aPmQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:35:39.216899
---

# 【工业控制系统网络安全系列课程】第1课-工业控制系统概述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UovezlRiaNGIOpyzGvg006nC1jMjD3qaCw1ic1ZxtQukW1V7KHTwfD31NQ/0?wx_fmt=jpeg)

# 【工业控制系统网络安全系列课程】第1课-工业控制系统概述

原创

老付话安全
老付话安全

老付话安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7UnMUNqGIz071DWbJdrzpdJpDxlHDFtnMDlvK8TeibfibdovgH3vMKfIloQibicL6TTiaXQib28nacKJv8qx7AJNnm8g/640?wx_fmt=gif)

**点击蓝字**

**关注我们**

关注我，带给你不一样的精彩

世界因你的沉淀而出彩

**始于理论，源于实践，终于实战**

**老付话安全，每天一点点**

**激情永无限，进步看得见**

![](https://mmbiz.qpic.cn/mmbiz_png/lB1oaPhdMNvxZ67rEjeQWUFqwCxiacBblWHRAxzuoMfYPQXETZ7Y5bsGSLBPy2QGDKIbia74ruAWgJXhWkMlGgkA/640?wx_fmt=png)

**严正声明**

本号所写文章方法和工具只用于学习和交流，严禁使用文章所述内容中的方法未经许可的情况下对生产系统进行方法验证实施，发生一切问题由相关个人承担法律责任，其与本号无关。

特此声明！！！

本文字数：

2094字，18图

阅读时间：

11分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

前言

要更有效地保护工控系统，我们首先需要了解常见的漏洞与系统弱点。这将帮助我们提出有针对性的修复方案，并制定相应的策略与计划，从而构建起所需的纵深防御体系，为工作环境中的工业控制系统提供更为可靠的保护。

安全工作需要一种独特的思维模式。

安全专业人员看待世界的方式往往与众不同——就像经验丰富的老刑警走进商店时会不自觉留意偷窃可能一样，安全人员在操作电脑时会思考其中可能存在哪些安全漏洞，在使用投票软件时则会设想如何防止重复投票。

这种思维方式并非大多数人天生具备，对工程师而言也并非自然形成。

良好的工程实践关注如何让系统运转起来，而安全思维则要求想象系统如何可能被破坏。这需要我们从攻击者、对手或破坏者的视角出发去审视系统。

我们并非一定要利用所发现的漏洞，但若不学会以这样的角度观察世界，便很难觉察到大多数安全问题。

因此，研究新的漏洞是否符合伦理？答案无疑是肯定的。尽管存在潜在风险，漏洞研究仍具有不可替代的重要价值。

安全本质上是一种思维方式，而寻找漏洞正是培养这种思维的关键途径。如果从业人员不采用这一重要的学习工具，整个安全领域都将因此受到损害。

要了解常见的漏洞与系统弱点并发现漏洞就需要我们对工业控制系统运行逻辑有所了解，生产现场的运行业务逻辑有深入的理解才能发现系统漏洞和弱点。

但是我们也不用走进死胡同，去深入学习自动化技术；自动化技术是为安全服务的，我们只要能够了解他们的业务逻辑即可，降低学习成本从而能够快速的理解安全在工控系统应该起到的作用。

工业控制系统

工业控制系统（Industrial Control System，简称 ICS）是指用于监控和控制工业过程的硬件与软件组合。它广泛应用于电力、水利、石油化工、制造业、交通运输等关键基础设施领域，确保生产流程的自动化、高效与安全运行。

工业控制系统通常包含以下关键组成部分：

1. **监控与数据采集系统**（SCADA）：负责对分布广泛的工业设施进行集中监控、数据采集和过程控制。
2. **分布式控制系统**（DCS）：常用于流程工业（如化工厂），对生产环节进行分散控制、集中管理。
3. **可编程逻辑控制器**（PLC）：用于执行具体的逻辑控制指令，驱动机器或生产线。
4. **人机界面**（HMI）：提供操作人员与控制系统交互的界面。
5. **远程终端单元**（RTU）：安装在远程现场，用于采集数据并执行控制指令。
6. **控制回路与现场设备**：包括传感器、执行器、仪表等，直接与物理过程交互。

工业控制系统传统上侧重于**可靠性、实时性与稳定性**，常运行于相对封闭的环境。但随着数字化与网络化转型，越来越多的工业控制系统与 IT 系统、互联网连接，也使其面临日益严峻的**网络安全威胁**，因此保护其安全性已成为现代工业发展的关键议题。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoDJCfl0o4HibpcD7Jvxtf1w7DmRey6Evdib4pM2mJicaHqTBISjX2K1lSQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoHN8JttmZDmqKs3bNibRHTrk3yt7ic3qcYXnPDEibdMdOoMRSCsB8PDqHQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoB1y40UbFYK2kAico5xL2wtjslLhmGBJ6jP0KBEpO6HP2ZKdibNOCWPZw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoIgWvibc3cRW96KvX75bzp1gEkKhen9GYdS05weyeTv9zgDS8vCqMTAA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoUVdJSettYREmy7TC9jaYf6q8Ol8m4wrYlzlB2rtchdfjARGeTexHGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61Uo7icCgz8FbiaIs6w3I5Biahko5Qz71e72bwxHib2RibZ04WdK1MeAKOgj8ag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UorMJ3pSfJs2aicGORWZBia9d5PtZ5DWXe3dVsiaicInVwIaIZ3s0B3el7AQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61Uog9orJ0UUZGEC5qGaFgESkBVqGsiadnibaXtUD4OVbiaiaMM2ic0iazCILXzA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61Uoeibpx6cb1lvZ0oWuibM103xo42YGUavq3u9do0HTd9tncv11HzAzyxgw/640?wx_fmt=png&from=appmsg)

梯形逻辑练习我给大家推荐一个在线工具：

```
https://www.plcfiddle.com/
```

注意：PLC fiddle 是 Firefox、Chrome 和 Safari 浏览器支持的在线梯 形图逻辑模拟器。Microsoft EDGE 不完全支持 plcfiddle。

使用方法：

+ 单击并拖动变量并将其放置在梯级上

+ 从下拉菜单中选择一个标签名称

+ 通过输入名称 （tagname） 并选择数据类型来添加其他变量

PLC Fiddle 数据类型

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61Uo9ZD6h0GvCp9Dqxemhw4djQ54n6lZQLTIWQjbgRBLHanicuMTawSumKA/640?wx_fmt=png&from=appmsg)

注意：您可以保存您的工作。每次按 SAVE 时，都会生成一个唯一的 URL，以便您返回到创建的 梯形图逻辑。

创建一个新梯级以完成以下操作：

1. 除非窗户关闭，否则将发出警报的窗户警报器（关闭时警报）

 • 添加一个新变量，将其命名为“window”，并选择Boolean作为类型

 • 拖放一个常闭的联系人，从下拉列表中选择“窗口”

• 创建一个新的布尔变量，将其命名为“alarm”

• 拖放线圈，从下拉列表中选择“警报”

2. 模拟门铃（瞬时按钮）仅在最初按下时才会响起铃声。与一直亮着直到关闭的电灯开关不同。

3. 当按下启动按钮 3 次时打开电机的计数器

4. 一个计时器，用于在 3 秒计时器到期后打开电机

有关练习 1-4 的可能解决方案，请参见

https://www.plcfiddle.com/fiddles/38a3f32d-ebfd-47e1-8331- a65afc080b1a

创建一个模拟车速表;

• 开/关按钮

• 速率 = 当前速度

• SP = 设定值 = 期望速度

• 滑行 = 让您当前的速度慢慢降低

• Incr = 将您的设定值增加 1 英里/小时

请参阅 https://www.plcfiddle.com/fiddles/e68cad0b-be8f-44e7-bd8a-fdf6766d44be，了解巡航控制练习的解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UotsynCZzz0icuXrGxWuQYOacVnjp0mfFKIQib0TUKRy5m5iaNtFlQyErzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoNhRIyPs0Iae1jQiaFiaHWhdFTGYibrDHQGrq4NLVvqE3RATrazPuh8p0g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UobnsIIotRQhUe3xdpCwfsAic6nCBl1AUA4ib0gyleqTKZp7hkU9FP8rNw/640?wx_fmt=png&from=appmsg)

end

**往期内容**回顾****

|  |
| --- |
| [【大话工控安全】工业控制系统基础知识](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484945&idx=1&sn=b0af8363f409985ac45ef855cecfca1d&scene=21#wechat_redirect) |
| [【大话工控安全】工业控制系统基础知识之设备通讯](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484960&idx=1&sn=76206a10ca8b43bc13551839651d5fde&scene=21#wechat_redirect) |

@请赐予我力量，关注和转发是最大的支持@

+VX：TCMAFNS119  欢迎进群交流

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

老付话安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

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