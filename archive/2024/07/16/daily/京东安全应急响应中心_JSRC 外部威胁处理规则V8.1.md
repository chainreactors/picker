---
title: JSRC 外部威胁处理规则V8.1
url: https://mp.weixin.qq.com/s?__biz=MjM5OTk2MTMxOQ==&mid=2727837217&idx=1&sn=918d915ee1a229e115d57398b5031bf4&chksm=8050a9a9b72720bf9b87f35514d8c4e3765ae75d01441ff9c0542367e7755ddf3f45badb5d7e&scene=58&subscene=0#rd
source: 京东安全应急响应中心
date: 2024-07-16
fetch_date: 2025-10-06T17:44:48.726504
---

# JSRC 外部威胁处理规则V8.1

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z9MuUwaeeGLmtrkHbaibrSLnQwicBd8I6IgGU53bWumQWDkS6EDibR6XA6n9dCusRogtjZhWqPxq467SNoD1XLLyQ/0?wx_fmt=jpeg)

# JSRC 外部威胁处理规则V8.1

京东安全应急响应中心

**JSRC 外部威胁处理规则**

**V8.1**

JSRC秉承公开、透明、合理的漏洞处理原则，为帮助白帽师傅们更好地了解评审规则，现V8.1版本针对漏洞处理规则等内容进行了更新。

小编已整理更新细则方便大家更快速了解，文末点击阅读原文可见完整版【JSRC 外部威胁处理规则 V8.1】。

**一、漏洞处理规则更新**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Z9MuUwaeeGLmtrkHbaibrSLnQwicBd8I6Ivibw8qNB1IYY8J8h0xXaZt5GGngq0CH4WFMDKVsicia8gRLjFeviaV7eog/640?wx_fmt=gif&from=appmsg)

**漏洞二次收录规则**

漏洞确认收录后，白帽子可对状态为**已修复**的漏洞进行复查，若问题**仍存在**，可**再次提交**反馈。JSRC 审核人员会对该问题审查确认，并再次计分或处理。

注：**修复中**状态漏洞再次提交，则**不收录**。

**同一漏洞导致的多个利用点收取规则**

**同一漏洞源**的多个漏洞仅收取 **1** 份报告。

以下情况也作同一漏洞源处理，即多个漏洞按一个处理。

1) 同一个系统存在未授权访问，前端页面可以访问任意接口引起多处越权问题仅收取一份报告。

2) 同一个系统存在注入漏洞，相同接口不同参数引起多处注入问题仅收取一份报告。
3) 同一个系统存在log4j rce漏洞引起的多处接口rce问题仅收取一份报告。
4) 多个域名解析同一个系统引起多处问题仅收取一份报告。
5）提权漏洞引起的多处问题仅收取一份报告。

**同一个系统**的同类问题**三个月内**重复提交，记**前三个**为有效。

例如：

1）同个系统的不同接口存在sql注入漏洞，记前三个为有效。

2）同个系统的不同接口存在水平越权漏洞，记前三个为有效。

3）同个系统的不同接口存在XSS漏洞，记前三个为有效。

**二、公示****数据泄露漏洞评级指南**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Z9MuUwaeeGLmtrkHbaibrSLnQwicBd8I6Ivibw8qNB1IYY8J8h0xXaZt5GGngq0CH4WFMDKVsicia8gRLjFeviaV7eog/640?wx_fmt=gif&from=appmsg)

为帮助大家更清晰地了解数据泄露漏洞相关评级准则，现公示评级指南供大家参考~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9MuUwaeeGLmtrkHbaibrSLnQwicBd8I6IWLAkU9QR7dMttl7vyqZBkiaaM7ZjQjic9lDyx7srnk1ibnIEudPCiaPb4Q/640?wx_fmt=png&from=appmsg)

JSRC

为师傅们带来更好的挖洞体验，我们将不断更新评审规则，同时JSRC正在筹备升级平台中，体验UP！奖金UP！玩法UP!

请持续关注，敬请期待！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z9MuUwaeeGIlXfXZDFfRBZuzMIeAKzMfMxSjmvm8OnyrJCz9K2bnuL1L3wdTZMh5mibyKD3sbQB0Mia5qZCvxNTw/0?wx_fmt=png)

京东安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z9MuUwaeeGIlXfXZDFfRBZuzMIeAKzMfMxSjmvm8OnyrJCz9K2bnuL1L3wdTZMh5mibyKD3sbQB0Mia5qZCvxNTw/0?wx_fmt=png)

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