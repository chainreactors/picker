---
title: G.O.S.S.I.P 阅读推荐 2023-02-03 IoTSeer
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494029&idx=1&sn=98b367c91909687887b34e6c4353d909&chksm=c063c754f7144e429408c2b0a7d49a8674ee83d506625fbc334ebdfc51dc0d2aa2c70637bd90&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-02-04
fetch_date: 2025-10-04T05:41:26.610463
---

# G.O.S.S.I.P 阅读推荐 2023-02-03 IoTSeer

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6nDdULBk8ibKp5RDiaotJpvdgRVib76aWfjPVlZArcchAiawI5qVdeE94JQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-02-03 IoTSeer

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6RRLThOXxhK4jGclUOn5OwBNnsYlIpxKo5FzI4ibb7ePgHicfopfGos9A/640?wx_fmt=png)

在2022年的CCS会议上，一篇名为 *Discovering IoT Physical Channel Vulnerabilities* 的研究论文讨论了关于IoT设备的一种特殊的漏洞——physical interaction vulnerability，这种漏洞指的是攻击者通过触发特定IoT设备的物理功能（例如命令空调在夏天吹热风），触发邻近IoT设备的（不安全）行为（例如因为温度过高而开窗散热，导致安防系统失效）。事实上，现代住宅中这种互相影响的IoT设备还是挺多的，下图是一个实例：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6zxeQ1tgwxC4FLVFbdavZnzd2nXVS93icVsA8JsUvI9DxesnVRXdjQow/640?wx_fmt=png)

Figure 1更为直观地展示了此类漏洞的整个攻击流程：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6y1l0TPicu2T0EIBIyOUO2su8BfqNmN4sSGycwfkOQQznLESdgcaSvibA/640?wx_fmt=png)

论文提出了一种通过分析IoT companion app来识别此类漏洞的方法， 并且设计了名为`IoTSeer`的自动化分析系统，对现实世界的IoT companion app进行了漏洞检测。具体地，`IoTSeer`对IoT companion app的代码进行分析之后，能够将那些触发物理操作的事件和相关命令提取出来；接下来，`IoTSeer`将这些命令转换成名为 physical execution models (PeMs) 的模型，并且将多个app对应的模型统一为一个 composite physical execution model (CPeM)；与此同时，`IoTSeer`还会收集IoT设备的运行时交互信息，确定它们的执行参数，从而完善CPeM；最后，`IoTSeer`能够基于CPeM进行合规性分析，检查physical interaction vulnerability是否存在。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn67FNCic1qMSTPBQgke1gsYtVLibNTNibDqjbJNlI0C0nAlEx0YndFlvicEA/640?wx_fmt=png)

在本文中，作者定义的PeM是一个非常重要的抽象表述，它对IoT companion app以及相关的设备能够执行的操作进行了抽象。在这里，作者引入了一个名为hybrid I/O automata的概念（引自一篇2003年发表在 *Information and Computation* 的论文 *Hybrid I/O Automata*）。通过把IoT设备的物理特性转换为一系列的flow function（这个地方非常的数学，不仅有离散的函数，对于那些物理信息连续变化的设备，我们甚至还发现了偏微分方程的身影），PeM就能够定义设备的物理属性——给定一台IoT设备本身的属性以及它和与其他设备之间的物理距离，就可以计算出来一个它对其他设备的影响的值。进一步，通过把一系列的PeM进行合并，我们就可以评估设备与设备之间的互相影响的情况了（此处细节过多，请参阅论文）。
.

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6912vH0XMTVs3RsIFUldjiaCRVCZZ9hLSRPQdW4bYJvicZbjGHN31WpYQ/640?wx_fmt=png)

基于CPeM，我们能够建立设备之间互相影响的模型。再进一步，为了进行安全分析，首先需要定义一些必须满足的policy：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6VDdb7MJBzgP1FyeJoWEEKfdLw5YeeXXAsRt24sHicb9kTKY89eIlibRg/640?wx_fmt=png)

然后，在CPeM指定的模型上，就可以用经典的formal analysis的方法来检查是否存在policy violation，由于编辑部没有人懂formal analysis，因此这部分我们就略过了，请读者自己去论文中检查细节：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn698I2xj7ib9iazI0GBfZbbspkspOnDwt5sUQbDyo1yXc1ib2LTAvRpXHsA/640?wx_fmt=png)

作者在实验部分用我们在一开头提到的那个例子作为研究场景，分析这里面大量IoT设备之间到底有多少physical interaction vulnerability真实存在。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6jza3wYIEJ5ryArItGVjxH68dibEEe6ehMIRttUCYvGfC11ZewsuhHyA/640?wx_fmt=png)

实验结果表明，如果家里面这些智能设备多到一定程度，互相之间的影响还是很明显的，下表就给出了通过对模型的formal analysis找到的问题，直觉上这些问题都应该是存在于物理世界中的。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6DWSnNdfPeTJJyjGkwfP7XqmhRXNLqapMzqTmg6qqHEyDwxQChy2Sxg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn61qa8Mial5dxsXkX9ENllSNImcYpJFQIZrV0o8vYHTBFBYiaDw00MFFzg/640?wx_fmt=png)

最后作者也将`IoTSeer`和以往的一些工作进行了对比：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GjYqqSbDbUb7WXNJJwpWn6sQFVfzmKD8mtm5zrYVEELSe0pYGOSUSohZiaibUmr8l2LXfz0ibx17cLA/640?wx_fmt=png)

---

> 代码：https://github.com/purseclab/IoTSeer
> 论文：https://dl.acm.org/doi/abs/10.1145/3548606.3560644

预览时标签不可点

阅读原文

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