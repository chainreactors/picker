---
title: 苹果紧急推送超30项安全更新，Safari/WebKit曝多重高危缺陷
url: https://mp.weixin.qq.com/s/rYdt82_tRFMCRF1-ey1F9Q
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:22:30.233355
---

# 苹果紧急推送超30项安全更新，Safari/WebKit曝多重高危缺陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3hIIIGyB0W1xqsjutnxgDIQicFMrmJm5YDkGcC306YFlkyN6rB7UXtaDPbhXAYdvPm3hzuFAqqVYIW9n4y6THHuowU3ZvJiaEhY/0?wx_fmt=jpeg)

# 苹果紧急推送超30项安全更新，Safari/WebKit曝多重高危缺陷

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

苹果公司近日面向 iOS、iPadOS、macOS 以及 Safari 浏览器发布了一轮重要安全更新，一口气修复了超过30个安全漏洞。其中，WebKit 浏览器引擎成为本轮修复的“重灾区”，多达数个高危缺陷被集中修补，引发安全圈高度关注。

此次更新版本包括 iOS 26.5.2、iPadOS 26.5.2、macOS Tahoe 26.5.2 以及 Safari 26.5.2，目前苹果尚未发现这些漏洞在野外被实际利用。

**WebKit漏洞集中爆发：AI工具首次深度参与发现**

本次最受关注的，是 WebKit 中发现的4个关键漏洞，这些问题均可能被恶意构造的网页触发，导致 Safari 崩溃甚至内存破坏。

具体包括：

* 内存损坏漏洞（CVE-2026-43707）：恶意网页可能导致进程异常崩溃
* Safari崩溃问题（CVE-2026-43716）：处理特定网页内容时触发异常退出
* 越界写入漏洞（CVE-2026-43745）：可能引发程序崩溃或数据破坏
* 释放后使用漏洞（CVE-2026-43715）：潜在导致内存被恶意利用

值得注意的是，这一批漏洞的发现方式出现了变化：

部分问题由 OpenAI Codex Security 与 Anthropic Claude 等 AI 安全工具辅助发现，这是安全研究领域中 AI 参与漏洞挖掘的典型案例。

其中，前三个漏洞由 OpenAI Codex Security 相关研究贡献，而 CVE-2026-43715 则由 Anthropic 研究人员联合 Claude AI 发现。

**不止浏览器：内核级漏洞同样被修复**

除了 WebKit，苹果还修复了一批更敏感的系统级漏洞，其中部分甚至涉及内核权限问题：

* 应用可能读取敏感内核状态
* 可触发系统崩溃或写入内核内存
* 存在内核内存损坏风险

这些问题一旦被利用，攻击者可能突破系统隔离机制，对设备安全造成更深层影响。

相关漏洞也得到了安全研究人员的披露与报告支持，包括发现“Dirty Frag”相关研究的人员。

**苹果罕见表态：AI正在压缩漏洞“武器化时间”**

苹果在接受媒体采访时表示，此次快速更新的节奏并非偶然，而是对当前安全形势变化的直接回应。

公司指出，随着 AI 工具越来越强大，漏洞从“发现”到“武器化”的时间正在被大幅压缩，可能从过去的数天甚至数周缩短到“小时级”。

因此，苹果正在调整安全响应策略：

尽可能缩短漏洞披露与补丁推送之间的时间窗口，让攻击者没有足够时间构建利用代码。

**安全趋势变化：AI正在改变攻防节奏**

AI 不仅在提升开发效率，也正在深刻改变漏洞挖掘与网络攻防节奏。

一方面，AI辅助工具让安全研究人员更快发现隐藏漏洞；另一方面，也意味着潜在攻击者可能以更低成本、更快速度构建利用链。

浏览器引擎、内核系统等传统高风险区域，正在进入一个“更快发现、更快修复、更快对抗”的新阶段。

*资讯来源：苹果官方安全更新公告及相关媒体报道综合整理*

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K39uk049usaQH1yXGLibMtRDc3UVLg0hIPgDMYic2XkpZXvdW5u3jq0ykW4KO4r3juep8rRmj9LWicAaYMVJOiabRicboqlSHTMvMvQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K3f7Dn361oHJqu9axN3sMibv7byS4HvLfePqF0ib3G1jJVkXr3kibRgYsaWIdXH3KnXc9Tj6ncOUuwwz66hnjibHBiaZricTlXqkOPrA/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K0HDygGp54AIw6KfcmgMARrw3L9C2SqREv9ozOwSBK5yUL2gHHq3CHTJt4RgQtlYBK1TicCbOibkHhY6sWVzrfsMzGIYTBks2mUM/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1nibLR2InbMr5SNOXb8kxHhDdOO7gzOfZJD1EmN22MQfzuDpEfkxJdcWiaqJOWZmT5DbWrJPDMKKibAP247ibWZmYSK0pl7ELbb5I/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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