---
title: 倒计时 1 天 ｜ 云原生安全立方项目
url: https://mp.weixin.qq.com/s/uL3bnEGP3_YwZXZuL4F0vA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:40:10.811335
---

# 倒计时 1 天 ｜ 云原生安全立方项目

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjvq9jCvmn0ObGDN5ZGuAicqPeEZsjoqyRHT3STwZsS5VZKO5YIBDboNA/0?wx_fmt=jpeg)

# 倒计时 1 天 ｜ 云原生安全立方项目

原创

miao2sec
miao2sec

喵苗安全

![]()

在小说阅读器中沉浸阅读

***CLOUD NATIVE SECURITY***

**01**

**作者介绍**

*/ INTRODUCTION*

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjx03XyXo4rtruwJXV2mnB4WvDuibUByHhIbs5nwEeWpMLvese1IFFTNg/640?wx_fmt=png&from=appmsg)

**Yaney**，喵苗安全（miao2sec）创始人，资深安全研发工程师。具备金融行业与车企的一线企业安全治理实战经验，长期深耕 **云 / 云原生安全、AI 安全与软件供应链安全** 三大核心方向。

专注于 **容器镜像安全、组件漏洞降噪及漏洞管理体系建设**，具备从 **0 到 1** 规划、设计、研发并落地 **CNAPP（云原生应用保护平台）** 的完整工程与实践能力。

作为 **开源容器镜像安全工具 Trivy 官方认证社区贡献者**，同时也是公安三所《**ICTS****供应链安全治理研究**》特邀作者。曾受邀在 **CCS 大会、FCIS 大会、腾讯云开发者先锋（TDP）、平安 SRC** 等会议与社区分享 **甲方视角下的云原生安全实践与落地经验**。

个人博客：https://www.yaney.me/

**02**

**课程目录精彩一览**

*/ CATALOG*

容器安全真正困难的地方，并不在于某一个漏洞或工具，而在于如何从整体上理解风险是如何产生、如何被放大，以及又该在哪里被阻断。

《第 1 课 容器安全威胁》将带你从“容器为何出现”讲起，逐步建立起风险、威胁与缓解措施的分析框架，并通过威胁建模的方法，将零散的安全问题串联成完整的攻击路径。

学完这一课，你将不再只是被动地“修漏洞”，而是能够站在攻击者和防守者的双重视角，识别容器环境中真正重要的风险，理解安全边界、多租户与安全原则在云原生中的实际含义，并为后续的技术细节打下清晰、可落地的安全思维基础。

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjicRMB0yicI688D1bnzv7uEamWjBsKibh8bCzkzBV6cEiblMCuxRCz6TFew/640?wx_fmt=png&from=appmsg)

在容器环境中，很多安全问题并不是来自复杂的漏洞，而是源于对 Linux 权限模型的误解。

《第 2 课 容器安全基础：Linux 权限控制 》从系统调用（Syscall）出发，逐步拆解文件权限、特殊权限位（Setuid 和 Setgid）与 Capability 的工作方式，结合真实可复现的案例，说明权限是如何被继承、放大并最终导致风险的。

理解这些基础机制，将帮助你从根本上判断容器中的权限边界是否可靠。

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjbl4BI2B0wuzgoA8BnPb8tDaDbPBFxerQjoukp7uPA1Y4GAD4fzWibyg/640?wx_fmt=png&from=appmsg)

容器中的资源限制并不是简单的参数配置，而是内核层面一整套约束机制的结果。

《第 3 课 容器资源限制：Cgroup》将从 Cgroup 的设计初衷出发，带你理解资源是如何被分配和限制的，以及这些机制在什么情况下会成为稳定性的保障，又在什么情况下演变为安全风险。

学完这一课，你将能够看懂容器资源限制背后的真实含义，判断配置是否合理，并为后续理解容器安全与逃逸问题打下清晰的底层认知基础。

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjhAYdVAFhpq16MbXzssiaq6yiaQCDUtrpZgmhylW4Yaynqy0pzic89o0NQ/640?wx_fmt=png&from=appmsg)

在容器环境中，漏洞不再只是代码层面的缺陷，而是以镜像为载体贯穿整个软件生命周期的问题。

《第 7 课 容器镜像安全》从漏洞披露流程入手，系统讲解镜像中常见的风险来源，包括组件漏洞、许可证风险、错误配置与敏感信息泄露，并深入分析镜像扫描的原理、工具差异与落地流程。

通过本课的学习，你将理解为什么不同扫描器会给出不同结果，如何在 CI/CD 中正确使用扫描工具，以及如何将镜像漏洞管理转化为一套可持续运转的工程化能力。

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjIIfBK02msRsYdYq5XczXpmun6N4ruyAuYl0FeqJxzsxVraODXic4lFQ/640?wx_fmt=png&from=appmsg)

《第 11 课 向容器中传递 Secret》将带你快速看清容器环境中 Secret 是如何被使用、滥用以及泄漏的，帮你分清哪些做法只是“看起来安全”，哪些才是真正可靠。

通过理解 Secret 的核心特性、常见风险以及 Docker 和 Kubernetes 的能力边界，你将建立起对敏感信息安全的整体认知，为后续更深入的容器与云原生安全学习打下坚实基础。

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsVTSPo60Jq0RQNiaOsyNdtrjgOBfflicicv3EBlK1SN3joLhGfNicIhtPsMRFkFhicffXgdN1A4gLS0ICQ/640?wx_fmt=png&from=appmsg)

**03**

**获取更多课程信息！**

*/  MORE*

了解更多关于[《云原生安全立方项目》](https://mp.weixin.qq.com/s?__biz=Mzg5MjkwODc4MA==&mid=2247487417&idx=1&sn=f5266422c9b6d782b74a9210d9bf1a8c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsUNLZJ9fKA1sRwfTQyztE3vicwL4xqiasscGWAwOibdOtxxlJicMKJtNU9ItyCNNQXX2cl89bGgNfBrwg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=Mzg5MjkwODc4MA==&mid=2247487417&idx=1&sn=f5266422c9b6d782b74a9210d9bf1a8c&scene=21#wechat_redirect)

如对本次内容感兴趣，欢迎进群交流：

![](https://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsXfovtrpMcWdv8bYO9uskrR99t3OkQU9A5Ye07Yhv1g5t3seQibyLmqT5XgXTmLRt8aGaYd137Eatg/640?wx_fmt=png&watermark=1#imgIndex=4)

🐱 作者也在群里哦 🐱

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsU6dkx953YXJSjxfwKn6V5A4TocLcGcicEKdRxPo3UsDpjECYDbVxicSiagx4baJa88rM4Anfjc3BRVQ/0?wx_fmt=png)

喵苗安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/wjnOkgIccsU6dkx953YXJSjxfwKn6V5A4TocLcGcicEKdRxPo3UsDpjECYDbVxicSiagx4baJa88rM4Anfjc3BRVQ/0?wx_fmt=png)

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