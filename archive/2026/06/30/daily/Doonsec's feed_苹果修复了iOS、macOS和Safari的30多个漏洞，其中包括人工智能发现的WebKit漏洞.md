---
title: 苹果修复了iOS、macOS和Safari的30多个漏洞，其中包括人工智能发现的WebKit漏洞
url: https://mp.weixin.qq.com/s/HpkT_rS83TVLNvAm1yZyHQ
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:21:21.472874
---

# 苹果修复了iOS、macOS和Safari的30多个漏洞，其中包括人工智能发现的WebKit漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Njib8AGSxjyDWhX6eRSHVA1BOvWib4LuGmc9hjyOzYljUiaak55tojnfKC8CaCEVeeZ4QMWUZWfkh0ufPlFkpg1YMMhnmutb5NPE/0?wx_fmt=jpeg)

# 苹果修复了iOS、macOS和Safari的30多个漏洞，其中包括人工智能发现的WebKit漏洞

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

苹果公司周一发布了iOS、macOS 和 Safari 网络浏览器的安全更新，以解决三十多个漏洞，其中包括使用 Anthropic Claude 和 OpenAI Codex Security 等人工智能 (AI) 工具发现的 WebKit 中的四个漏洞。

WebKit漏洞如下所示 -

* **CVE-2026-43707** - 内存损坏问题，可能导致在处理恶意构造的网页内容时进程意外崩溃。此问题已通过改进内存管理得到解决。
* **CVE-2026-43716** - 此漏洞未具体说明，可能导致 Safari 在处理恶意构造的网页内容时意外崩溃。该漏洞已通过改进内存管理得到解决。
* **CVE-2026-43745** - 越界写入漏洞，可能导致 Safari 在处理恶意构造的网页内容时意外崩溃。此漏洞已通过改进输入验证得到修复。
* **CVE-2026-43715** - 一个释放后使用漏洞，在处理恶意构造的网页内容时可能导致内存损坏。该漏洞已通过改进内存管理得到解决。

苹果公司将前三个安全缺陷归功于 OpenAI Codex Security，而 Anthropic 的研究人员 Milad Nasr 和 Nicholas Carlini 以及 Claude 则因 CVE-2026-43715 而受到表彰。

这四个漏洞只是苹果公司开发的开源网络浏览器引擎 WebKit 中近 30 个已修复漏洞的一部分。其他漏洞包括 WebKit Canvas 中的释放后使用漏洞 (CVE-2026-43720) 以及恶意网站可能利用该漏洞在沙箱之外处理受限网页内容的漏洞 (CVE-2026-43725)。

苹果公司还修复了三个可能被恶意应用程序利用的漏洞，这些漏洞可能导致敏感内核状态泄露（CVE-2026-43722）、系统意外终止或写入内核内存（CVE-2026-43724）以及内核内存损坏（CVE-2026-39868）。安全研究员金贤宇（Hyunwoo Kim）发现了Dirty Frag漏洞，并因此发现了 CVE-2026-43724 和 CVE-2026-43722 漏洞。

此次更新适用于iOS 26.5.2、iPadOS 26.5.2、macOS Tahoe 26.5.2和Safari 26.5.2。目前尚未披露任何已修复的漏洞已被实际利用。

苹果公司在一份与路透社分享的声明中表示，由于担心人工智能工具可能会加速漏洞利用的开发，并成为网络战的推动者，将发现漏洞和将其武器化之间的时间缩短到几个小时，因此苹果公司正在比以往更早地进行安全更新。

据路透社报道，该公司表示，“鉴于人工智能能够加速恶意黑客工具的开发，该公司正在适应这一现实，因此需要缩短更新首次公开到交付给客户之间的时间。

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