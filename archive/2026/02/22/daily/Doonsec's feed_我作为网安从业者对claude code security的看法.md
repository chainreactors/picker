---
title: 我作为网安从业者对claude code security的看法
url: https://mp.weixin.qq.com/s/qz8K3QIyNem7jJYtHxdyFA
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:29.242410
---

# 我作为网安从业者对claude code security的看法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pAJyKDSMFzPd5WibzyovkxmB20Df2uSJUdGuHrrtqibAbzqtpjQnDSHNnAY8eVz11JQworvw1dKL3GF5OPtluGnsVJkSQM6n2qspCpGPUAZHo/0?wx_fmt=jpeg)

# 我作为网安从业者对claude code security的看法

原创

cc
cc

蓝剑实验室

![]()

在小说阅读器中沉浸阅读

#### 前言

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pAJyKDSMFzM60aibibr1LobVcuwKdHNP5cPm2lnd2K6SB4fnxPkCK7pkjZUFwSicicRnFk6Vz94GyGB5BgHKUj187qTDZP6eXVjic6cdBiaweBoTM/640?wx_fmt=gif&from=appmsg)

####

![image-20260222145251632](https://mmbiz.qpic.cn/mmbiz_jpg/pAJyKDSMFzNMsiblEOTNsz0VWqiaIYiamqRIVxQlnIn6lRrN8FiatRcugh8ccgzn7Ql5FxGEfSnpnptWbEWulyq1nw9a3TcjmtISbvMdr9tNPMQ/640?wx_fmt=jpeg)

大过年的这两天被这些文章刷屏，但是不知道有多少人去真正体验过

最近我也在学习agent的各个技术栈做ai for security的多agent产品开发，刚好发表我的一些浅见

首先这个功能只开放给team和企业用户，个人用户是没有这个入口的，但是这个价格确实比一个代码审计人员便宜太多了

![image-20260222143145159](https://mmbiz.qpic.cn/sz_mmbiz_png/pAJyKDSMFzOYoZNlcDtMFRAEYrWJ82ia5CnE6abQzYaicrcWW27DWB9NmqGx3PjzAVIxzicuudZF1C0ics3tdNWFCxmgKZNv0OgMt2DPOBtsaGM/640?wx_fmt=png&from=appmsg)

其次是使用条款，使用即授权，一旦使用这个功能就代表把源码交给anthropics公司

对于国内的一些甲方来说应该很难接受吧，同时不允许扫描第三方的代码，这对乙方来说就有限制了

但规定是规定，实操起来如果没有什么强制性的手段我估计还是有很多人拿甲方的源码去扫的

![image-20260222144111903](https://mmbiz.qpic.cn/mmbiz_png/pAJyKDSMFzOkCUNzt7nwV4yKCibKSEmURt38Pp0mFzPGJUADJiaAmtRDavh1icLLyia0k3wPCpcPmK7SRbJibKomt7BveYDtfZpqADtpFdlEDia8A/640?wx_fmt=png&from=appmsg)

股价问题，股价反映的是未来的趋势，资本用脚投票，anthropics本身的影响力加剧了这一反应，资本家老手段了

那么国内安全公司股价为什么没有跌呢，因为节假日休市![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)，具体如何看初八开盘吧

另外，anthropics开源的安全左移项目，不知道跟前两天上线的claude code security是不是同一套，有兴趣可以体验下：

https://github.com/anthropics/claude-code-security-review

#### 安全开发角度

这段时间我也体验了国内外各个厂家的大模型（比如opus4.6、5.3codex、glm5）和AI IDE（比如cursor、codebuddy、monkeycode）进行深度开发agent不管是从0到1的开发还是重构，各种新兴的技术栈（比如deepagent、langfuse、langraph）等等这些

以我作为安全人员而非专业开发的角度来看，vibe coding确实减少了很多重复性的工作，但是无形中对开发人员的要求其实更高了

你需要有架构思维，需要对ai写的代码有更高的纠错能力

如果他写什么就信什么，看不懂他为什么使用这个技术栈，各个组件之间是如何通信，数据如何在各个层级之间流转，前后端如何对接

就直接去运行部署到生产环境，那只是沦为被ai驯养的现实世界里的机械臂罢了

另一方面同时这对安全转开发人员也是个很好的机会

相信很多渗透出身的人员并不熟悉企业软件工程的开发流程，使用ai开发能够学习先进的技术栈

就拿我来说，从前开发一些小工具只是在本地windows用ide开发

用上vibe coding以后，我先是习惯了用linux作为开发机，后面因为ai写的代码迭代太快

从前一个版本打一个虚拟机快照的方式很快就占满我的硬盘了，就不得不学习使用git进行版本控制，做轻量化的交付

以及CI/CD，ai写的代码不经过测试直接部署真的会浪费很多返工的时间，这同样变相提高了我的开发能力

#### 代码审计角度

我一直在寻找可以能够实现“一键代码审计”的ai产品

输入源码，由agent部署环境-->审计-->测试payload-->直接输出可用的poc

像最近大火的deepaudit、strix，还有一些商业闭源产品我都体验过，只能说框架思路很好

但想要实现Raas（最近被热炒的概念，结果即服务）的这种产品，还是需要调教二开

想要测试这种代码审计agent的能力，最简单的就是拿一套已经人工审计出poc的代码

然后交给agent看他能不能审计出一样的poc，还是只是给你输出一些合规性的漏洞

从我们攻防人员的角度来看，只有能够拿到权限或者能够拿到数据的漏洞才是有用的

包括一些组合拳漏洞也算，其他的都只是合规需要的普通漏洞而已

如果你有其他的看法，欢迎后台加我微信交流

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6PXS5KbxaUSn79ymHasOVySwZKpoQP5ZbsCSibsAibaib8ZRkerhWKBM4WluWicJVbE5HwYWFcHKwdwFNrwSiasqwRQ/0?wx_fmt=png)

蓝剑实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6PXS5KbxaUSn79ymHasOVySwZKpoQP5ZbsCSibsAibaib8ZRkerhWKBM4WluWicJVbE5HwYWFcHKwdwFNrwSiasqwRQ/0?wx_fmt=png)

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