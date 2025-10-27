---
title: 演讲议题巡展 | CodeQL Java Optimisation
url: https://mp.weixin.qq.com/s?__biz=MzIzOTAwNzc1OQ==&mid=2651137854&idx=1&sn=4e02f0d23c7f2bdb0560a0aec81f2cc1&chksm=f2c1265ec5b6af48202eca32e89b64ac2d5a95d9ec57c7a9b83e4ae5f0b9d9ed46e17acfbdaa&scene=58&subscene=0#rd
source: KCon 黑客大会
date: 2024-08-14
fetch_date: 2025-10-06T18:03:48.098163
---

# 演讲议题巡展 | CodeQL Java Optimisation

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbJWPTA8FgCjacUVZdOof3ouZNYnkIRxeYxVGDlnOfZFUT8r4bmFnUguK3rtrdBKYImayRF1NlC9g/0?wx_fmt=jpeg)

# 演讲议题巡展 | CodeQL Java Optimisation

KCon 黑客大会

![](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbJWPTA8FgCjacUVZdOof3oCtolnFFkGOW1TkEicSAk7CPXic3BQ0ia1pYoofbq61LugnzzMhtqJgD3Q/640?wx_fmt=jpeg&from=appmsg)

*经过精心筹备与多方努力*

*KCon 2024 黑客大会敲定举办时间*

*将于8月24日-25日举办*

本次大会涵盖了网安领域的不同热点话题

为了展示演讲议题风采

让大家了解更多大会情况

特此开展议题巡展

欢迎围观~

![](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbIYfVZDQJGDrYtCSLlUY108DW0ctCvyicMsEMKfF75H4nlqtfy3cMtwQa7ibKzmbqib8yLasHKtY8Fg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbJWPTA8FgCjacUVZdOof3oCtolnFFkGOW1TkEicSAk7CPXic3BQ0ia1pYoofbq61LugnzzMhtqJgD3Q/640?wx_fmt=jpeg&from=appmsg)

**演讲者：**

**m0d9**

来自腾讯云鼎实验室

![](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbJWPTA8FgCjacUVZdOof3oCtolnFFkGOW1TkEicSAk7CPXic3BQ0ia1pYoofbq61LugnzzMhtqJgD3Q/640?wx_fmt=jpeg&from=appmsg)

**议题介绍：**

**CodeQL Java Optimisation：Make CodeQL Data Flow Analysis support java features such as java reflection, threading, etc**

CodeQL 是全球最大代码托管平台Github 默认的静态程序分析工具。其自建的QL 语言继承了Datalog 的语义，而且在语法上类似SQL 语言，这使得它具有更好的可读性。

在Java 静态程序分析上，有Native 方法和Reflection 两大难题，CodeQL 目前也没有很好的解决。例如近期出现的ActiveMQ CVE-2023-46604 / RocketMQ CVE-2023-33246，前者因为跨线程，后者还涉及到反射，都无法用CodeQL 通用规则检出。

本文介绍了CodeQL DataFlow 实现原理，在此基础上对其进行改造以支持Java 的一些特性分析，比如Java 反射、跨线程等，并对近期一些原本未能发现的经典漏洞进行回溯发现，最后讲讲增强后的CodeQL新发现。

**期待与师傅们在线下相聚，不见不散！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbJWPTA8FgCjacUVZdOof3oCtolnFFkGOW1TkEicSAk7CPXic3BQ0ia1pYoofbq61LugnzzMhtqJgD3Q/640?wx_fmt=jpeg&from=appmsg)

**KCon 2024 门票**

KCon 2024的线上售票通道已开启

购票网址：

**https://www.4hou.com/tickets/eERv**

**长按识别下方二维码**或

点击文末**“阅读原文”**

立即购票

![](https://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIbJWPTA8FgCjacUVZdOof3oBY0rnZqiayJSnGPSWJm7Qwia0rkLN0sSsZnNGnRhd5CNibaHfJgjgxnpw/640?wx_fmt=png&from=appmsg)

● 学生票：410元（需提供相关证明）

● 团队票：1434元（3张起购）

● 普通票：2048元

● 学生团体票：738（2张）984（3张）1435元（5张）（需提供相关证明）

● KCon XCon联合购票：2069元（名额仅限30人）

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIYvJeWfDicggbpjWluw8URLyM4jux7SrsiaqupEy9mdqQOmoib3ickpxdfTEyhqwttmlX8kmX6MNxwpMw/0?wx_fmt=png)

KCon 黑客大会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIYvJeWfDicggbpjWluw8URLyM4jux7SrsiaqupEy9mdqQOmoib3ickpxdfTEyhqwttmlX8kmX6MNxwpMw/0?wx_fmt=png)

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