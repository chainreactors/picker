---
title: 首个公开的针对苹果M5的macOS内核漏洞利用程序，使用Mythos Preview在五天内完成
url: https://mp.weixin.qq.com/s/-JLMLlpVoEyUnV2jQ_s1Fw
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:08:25.354242
---

# 首个公开的针对苹果M5的macOS内核漏洞利用程序，使用Mythos Preview在五天内完成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7N4RZTRj01SZHY5szNyXAYNAXDOZL8XhLVeHjA7xDxBCicdv7NEGlGxNnD5eoNictbzAZGl3kTVfNzdbyz6txXgTqITtvup3wNwU/0?wx_fmt=jpeg)

# 首个公开的针对苹果M5的macOS内核漏洞利用程序，使用Mythos Preview在五天内完成

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

据报道，苹果公司的 M5 芯片首次在公开的 macOS 内核内存损坏攻击中被利用，成功绕过了该公司著名的硬件级内存保护。

来自加州的研究人员 Bruce Dang、Dion Blazakis 和 Josh Maine 开发了一种针对裸机 M5 硬件上的 macOS 26.4.1 (25E253) 的内核本地权限提升 (LPE) 漏洞利用程序。

该攻击链从一个非特权本地用户账户开始，仅使用标准系统调用，即可获得完整的 root shell，而这一切都是在 Apple 的内存完整性强制执行 (MIE) 处于活动状态的情况下完成的。

该团队于 4 月 25 日发现了这两个底层漏洞，两天后联合起来，并在 5 月 1 日之前成功运行了可用的漏洞利用程序。

## **首个公开的 macOS 内核漏洞利用**

研究人员并没有通过标准的漏洞赏金流程提交报告，而是直接将这份长达 55 页的打印报告送到了位于库比蒂诺的苹果园区。此举旨在避开 Pwn2Own 等活动期间常见的拥挤提交队列。完整的技术细节将在苹果发布补丁后公布。

Memory Integrity Enforcement 是苹果公司基于 ARM 的 Memory Tagging Extension (MTE) 架构构建的硬件辅助内存安全系统。

MIE 是 M5 和 A19 芯片的主要安全功能，苹果公司花费了五年时间，据报道花费了数十亿美元，专门用于阻止内核内存损坏漏洞利用。

根据苹果公司自己的研究，MIE 破坏了所有已知的针对现代 iOS 的公开漏洞利用链，包括泄露的 Coruna 和Darksword漏洞利用工具包。

这项突破部分得益于 Anthropic 的 Mythos Preview，这是一个强大的 AI 模型，它帮助识别了这两个漏洞，并在整个漏洞利用开发过程中提供了帮助。

Calif 将该模型描述为一旦学习到某种问题类型，就能够将攻击模式推广到整个漏洞类别。

由于这些漏洞属于已知的漏洞类别，因此很快就被发现；然而，自主绕过 MIE 仍然需要大量的人类专业知识，这凸显了人机结合的力量。

针对苹果公司耗时五年才开发的防护措施，仅用了五天时间就完成了开发，这被认为是人工智能辅助攻击性安全研究的一个重要基准。

内存损坏仍然是所有现代平台（包括 iOS 和 macOS）上最常见的漏洞类型。诸如 MIE 之类的安全缓解措施旨在提高利用该漏洞的成本，而不是完全杜绝利用的可能性。

这项研究表明，随着人工智能模型越来越能够发现已知类别中的未知错误，即使是最好的硬件缓解措施也面临着有效窗口期不断缩小的局面。

加州将此次漏洞利用事件视为其所谓的“人工智能漏洞末日”时代的预演，在这个时代，小型、人工智能增强的安全团队可以实现以前需要大型、资金雄厚的组织才能实现的目标。

苹果公司诞生于 Mythos Preview 出现之前；此次漏洞利用表明硬件安全策略已经开始转变。

据报道，苹果正在努力修复此问题。在补丁发布之前，运行 macOS 26.4.1 且采用 M5 硬件的系统仍然存在通过这条未公开的攻击链进行本地权限提升的理论风险。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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