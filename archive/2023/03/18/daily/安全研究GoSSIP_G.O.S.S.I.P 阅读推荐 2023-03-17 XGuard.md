---
title: G.O.S.S.I.P 阅读推荐 2023-03-17 XGuard
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494548&idx=1&sn=812f267a6ba5ec1845a3b4509a0c4bc5&chksm=c063c54df7144c5b8b9558b4c0e8fa246e28317ee7f9bba4bce11f8ddc758e8ed53567e9adb3&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-18
fetch_date: 2025-10-04T09:58:19.481554
---

# G.O.S.S.I.P 阅读推荐 2023-03-17 XGuard

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21G65b9wFFVomhJrGGF0wkHanYGJaN2FkVhLEZiaIHUoticvAUK5srcML0c11hHiaWZ9aoHZ1xIQkRkIA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-17 XGuard

原创

G.O.S.S.I.P

安全研究GoSSIP

又到了“G.O.S.S.I.P和朋友”时间，今天推荐的这篇CCS 2022论文 *Understanding and Mitigating Remote Code Execution Vulnerabilities in Cross-platform Ecosystem* 的第一作者肖峰曾经在我们这里学习生活过，后来前往佐治亚理工。他在web安全领域是非常厉害的技术好手，这篇论文里面也充分展现了这一点。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHafHSAlPGJDK1lRLicVPo0kqF94fzb2whiaibyhabJs9zibkKkrjVznvjX0Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHao65Qg8Bib7nbgJr4zIAyZd7fIXRLtAMKaiaz19kRJb3GFIpU4HV8QMXA/640?wx_fmt=png)

在这篇论文中，作者注意到了现在许多基于JavaScript和跨平台（cross-platform）框架开发的程序（包括智能手机上的app和桌面上的应用程序）中，存在远程代码执行的风险，我们在上周五（2023-03-10那期）的阅读推荐中已经介绍过这种问题了。在本文中，作者特别关注的是在此类程序中，负责前端rendering部分的js代码有没有可能去越权调用一些只有更底层的后端逻辑才能触发的操作：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHaLfiaTZu28iawdDV9xn3b4PLy6EcTuoU1gv08o7TKTsnSI8iastwddBf4Q/640?wx_fmt=png)

来看一个Microsoft Teams中的例子（是的，又是你，全是漏洞的Teams，叫你用Electron开发！）这里面攻击者可以构造一个恶意的聊天消息，首先欺骗前端（窗口）渲染部分去触发一个js下载操作，同时还能新打开一个窗口来加载这份js代码，而打开的新窗口会切换到system-side context权限，那么一旦这份js代码被打开，就可以执行高权限操作（例如新建一个子进程去执行后台操作）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHaVN53k6vSLPRiapeBsGXmaTuVEkeITiafnpJZ8Kf5BfW8EdpoicacWODicw/640?wx_fmt=png)

作者总结了前端的js代码触发高权限（system-side context）操作的三个途径：1）利用一些permission检查不严格的后端API；2）修改一些全局变量制造data-only attack；3）调用（完全没有权限检查的）私有后端API

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHa1mHlUVVFbwzIU8CpYYBWRpRBwP7thfGYcvDYxh1Ro0WpRibP4mEqVHQ/640?wx_fmt=png)

在理清了攻击者的三大利用途径后，作者就设计了`XGuard`这么一个静态分析防护系统，基于静态代码分析把合法、非法和可疑的调用路径进行分类，然后在运行时根据静态分析的结果，允许或者禁止相关的调用。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHaEDb7evhu2DploWpMc2wfOpdtpUDaW51kOdj3wnSPIdzORCx8IyCujQ/640?wx_fmt=png)

`XGuard`的设计目标是尽可能降低误报（虽然这有点不太像一个defense工作追求的目标），实验数据表明确实做到了：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21G65b9wFFVomhJrGGF0wkHatULYNxONW0MlRYLpAY3GdmvDTibfZdslWUFOZLPZ16qGexia3Gvad0Ig/640?wx_fmt=png)

> 大家有没有发现今天的论文推荐，图片特别的精美？这是我们编辑部小董的杰作，是不是力压GPT-4！

---

> 论文：https://dl.acm.org/doi/10.1145/3548606.3559340
> 代码：https://github.com/xiaofen9/XGuard （不得不批评一下这个家伙，一直忙于健身，代码仓库上空空荡荡）

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