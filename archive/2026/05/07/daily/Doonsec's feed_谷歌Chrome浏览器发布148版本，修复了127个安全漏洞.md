---
title: 谷歌Chrome浏览器发布148版本，修复了127个安全漏洞
url: https://mp.weixin.qq.com/s/zjD5hHNaNMQvn_Nnj5X2ag
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:22.380903
---

# 谷歌Chrome浏览器发布148版本，修复了127个安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PrIu1gWgAXMTTqp6M1fM2Vt5kJAB2naibMh0d5mXK9NR13icoPIwF0buT53C0h7YCWkzSzd9je0FEc1rajpKuSk0ZGZlUw6jdUk/0?wx_fmt=jpeg)

# 谷歌Chrome浏览器发布148版本，修复了127个安全漏洞

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

谷歌已正式向稳定版渠道推出 Chrome 148 版本，带来了大规模的安全更新，解决了 Windows、Mac 和 Linux 系统中的 127 个漏洞。

该更新现已推出，Linux 版本为 148.0.7778.96，Windows 和 Mac 版本为 148.0.7778.96 或 148.0.7778.97，修复了几个严重的内存管理漏洞，这些漏洞可能允许攻击者执行任意代码或破坏底层系统。

随着网络威胁日益复杂，本次发布凸显了快速部署补丁的重要性，以便在威胁行为者利用高危浏览器漏洞之前将其武器化，从而缓解这些漏洞。

## **已解决的关键内存管理漏洞**

本次修复周期中，最紧迫的问题之一是三个关键漏洞。其中包括 CVE-2026-7896，这是 Blink 渲染引擎中的一个整数溢出漏洞，外部安全研究人员因发现该漏洞而获得了 43,000 美元的漏洞赏金。

另外两个严重漏洞，编号分别为 CVE-2026-7897 和 CVE-2026-7898，分别涉及 Mobile 组件和 Chromoting 组件中的释放后使用漏洞。这类内存损坏错误仍然是远程代码执行攻击的主要途径。

它们允许恶意行为者诱骗用户加载特制的网页，然后这些网页会覆盖相邻的系统内存以运行未经授权的命令。

修复这些关键漏洞可以防止攻击者绕过浏览器安全沙箱，从而完全控制受影响的设备。

Google 的更新还修复了影响核心浏览器组件的 31 个高危缺陷，包括 V8 JavaScript 引擎、ANGLE、Skia 和 WebRTC。

值得注意的是，安全研究人员因发现 V8 引擎中的越界读写漏洞 CVE-2026-7899 而获得 55,000 美元奖励。另一位研究人员因发现 ANGLE 中的堆缓冲区溢出漏洞（编号为 CVE-2026-7900）而获得 16,000 美元奖励。

为了在这些根深蒂固的内存安全问题进入稳定版本发布渠道之前主动识别它们，谷歌大量依赖其一套先进的自动化安全测试工具。

AddressSanitizer、MemorySanitizer、libFuzzer 和 Control Flow Integrity 等检测框架在整个软件开发流程中发挥了至关重要的作用，用于检测释放后使用、未初始化使用和越界写入等情况。

这些自动化工具模拟了无数种攻击场景，以确保浏览器代码能够抵御内存操纵技术。

企业安全管理员和个人用户应通过打开 Chrome 设置菜单手动验证浏览器版本，因为自动更新将在未来几周内逐步推出。

虽然谷歌可能会限制公众访问特定错误详情，直到大多数用户成功更新为止，但这些修复的数量之多、严重性之大，使得立即修复成为当务之急。

延迟此次更新可能会使企业网络和个人设备面临被恶意利用的风险。确保系统完全打上补丁是抵御攻击者利用这些新披露的漏洞的最有效防御措施。

## **Chrome 严重和高危漏洞表**

| CVE | Severity | Component | Vulnerability Type |
| --- | --- | --- | --- |
| CVE-2026-7896 | Critical | Blink | Integer overflow |
| CVE-2026-7897 | Critical | Mobile | Use after free |
| CVE-2026-7898 | Critical | Chromoting | Use after free |
| CVE-2026-7899 | High | V8 | Out of bounds read and write |
| CVE-2026-7900 | High | ANGLE | Heap buffer overflow |
| CVE-2026-7901 | High | ANGLE | Use after free |
| CVE-2026-7902 | High | V8 | Out of bounds memory access |
| CVE-2026-7903 | High | ANGLE | Integer overflow |
| CVE-2026-7904 | High | Fonts | Out of bounds read |
| CVE-2026-7905 | High | Media | Insufficient validation of untrusted input |
| CVE-2026-7906 | High | SVG | Use after free |
| CVE-2026-7907 | High | DOM | Use after free |
| CVE-2026-7908 | High | Fullscreen | Use after free |
| CVE-2026-7909 | High | ServiceWorker | Inappropriate implementation |
| CVE-2026-7910 | High | Views | Use after free |
| CVE-2026-7911 | High | Aura | Use after free |
| CVE-2026-7912 | High | GPU | Integer overflow |
| CVE-2026-7913 | High | DevTools | Insufficient policy enforcement |
| CVE-2026-7914 | High | Accessibility | Type Confusion |
| CVE-2026-7915 | High | DevTools | Insufficient data validation |
| CVE-2026-7916 | High | InterestGroups | Insufficient data validation |
| CVE-2026-7917 | High | Fullscreen | Use after free |
| CVE-2026-7918 | High | GPU | Use after free |
| CVE-2026-7919 | High | Aura | Use after free |
| CVE-2026-7920 | High | Skia | Use after free |
| CVE-2026-7921 | High | Passwords | Use after free |
| CVE-2026-7922 | High | ServiceWorker | Use after free |
| CVE-2026-7923 | High | Skia | Out of bounds write |
| CVE-2026-7924 | High | Dawn | Uninitialized Use |
| CVE-2026-7925 | High | Chromoting | Use after free |
| CVE-2026-7926 | High | PresentationAPI | Use after free |
| CVE-2026-7927 | High | Runtime | Type Confusion |
| CVE-2026-7928 | High | WebRTC | Use after free |
| CVE-2026-7929 | High | MediaRecording | Use after free |

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