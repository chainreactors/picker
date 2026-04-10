---
title: Chrome浏览器存在严重漏洞，攻击者可利用这些漏洞执行任意代码
url: https://mp.weixin.qq.com/s/pXUt7ewNu1U1AJj3y3EC4A
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:42:30.779486
---

# Chrome浏览器存在严重漏洞，攻击者可利用这些漏洞执行任意代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OtYPamyPRhXGA8NXeicrbXfON86evZA1jibHkXIalPWRJPw3LqWuZ4auQG0bicln8gnbHZKGXQN0HeOAAb5Libg3Qe5Q4Tg9icqgJE/0?wx_fmt=jpeg)

# Chrome浏览器存在严重漏洞，攻击者可利用这些漏洞执行任意代码

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

谷歌发布了针对其Chrome浏览器的紧急安全更新，修复了多个危险漏洞。

Chrome 团队于 2026 年 4 月 7 日将 147 版本推广到 Windows、Mac 和 Linux 用户的稳定版渠道。

此次重大更新修复了可能允许攻击者执行任意代码并完全控制受影响系统的漏洞。该更新目前正在未来几天和几周内向全球所有用户逐步推送。

此次更新中最严重的威胁是位于 WebML 组件中的两个关键漏洞。这些漏洞编号分别为 CVE-2026-5858 和 CVE-2026-5859，涉及堆缓冲区溢出和整数溢出。

由于这些漏洞构成高风险，谷歌向发现这些漏洞的安全研究人员发放了高达 43,000 美元的漏洞赏金。

这些严重漏洞可以通过诱骗用户访问特制网页来利用，因此立即修补至关重要。

除了关键缺陷之外，Chrome 147 还修复了分布在多个关键浏览器组件中的大量高危错误。

安全研究人员在 V8 JavaScript 引擎、WebRTC、Media、Blink 和 Skia 中发现了严重的安全问题，例如释放后使用错误、类型混淆以及越界读取和写入缺陷。

如果这些漏洞被利用，可能会导致浏览器崩溃或允许恶意行为者破坏底层系统。

谷歌向举报这些问题的道德黑客支付了数万美元的奖励，以防止这些问题落入不法分子之手。

为了保护用户，谷歌将严格限制这些漏洞的技术细节和利用方法。

这种协调一致的披露政策保证了大多数公众有足够的时间在网络犯罪分子逆向工程修复程序之前安装安全补丁。

它还能保护依赖于相同易受攻击的第三方库的其他软件项目，确保在开发和部署补丁的同时，更广泛的技术生态系统保持安全。

由于 WebML 漏洞的严重性，强烈建议个人用户和企业管理员立即更新浏览器。

您可以手动强制更新，方法是打开Chrome 菜单，导航至“帮助”，然后选择“关于 Google Chrome”。

浏览器将自动下载适用于 Linux 的 147.0.7727.55 版本或适用于 Windows 和 Mac 的 147.0.7727.55/56 版本，从而保护您的设备免受潜在的网络攻击。

## **Chrome 147 安全修复**

| CVE ID | Severity | Component | Vulnerability Type |
| --- | --- | --- | --- |
| CVE-2026-5858 | Critical | WebML | Heap buffer overflow |
| CVE-2026-5859 | Critical | WebML | Integer overflow |
| CVE-2026-5860 | High | WebRTC | Use after free |
| CVE-2026-5861 | High | V8 | Use after free |
| CVE-2026-5862 | High | V8 | Inappropriate implementation |
| CVE-2026-5863 | High | V8 | Inappropriate implementation |
| CVE-2026-5864 | High | WebAudio | Heap buffer overflow |
| CVE-2026-5865 | High | V8 | Type Confusion |
| CVE-2026-5866 | High | Media | Use after free |
| CVE-2026-5867 | High | WebML | Heap buffer overflow |
| CVE-2026-5868 | High | ANGLE | Heap buffer overflow |
| CVE-2026-5869 | High | WebML | Heap buffer overflow |
| CVE-2026-5870 | High | Skia | Integer overflow |
| CVE-2026-5871 | High | V8 | Type Confusion |
| CVE-2026-5872 | High | Blink | Use after free |
| CVE-2026-5873 | High | V8 | Out of bounds read and write |
| CVE-2026-5874 | Medium | PrivateAI | Use after free |
| CVE-2026-5875 | Medium | Blink | Policy bypass |
| CVE-2026-5876 | Medium | Navigation | Side-channel information leakage |
| CVE-2026-5877 | Medium | Navigation | Use after free |
| CVE-2026-5878 | Medium | Blink | Incorrect security UI |
| CVE-2026-5879 | Medium | ANGLE | Insufficient validation of untrusted input |
| CVE-2026-5880 | Medium | browser UI | Incorrect security UI |
| CVE-2026-5881 | Medium | LocalNetworkAccess | Policy bypass |
| CVE-2026-5882 | Medium | Fullscreen | Incorrect security UI |
| CVE-2026-5883 | Medium | Media | Use after free |
| CVE-2026-5884 | Medium | Media | Insufficient validation of untrusted input |
| CVE-2026-5885 | Medium | WebML | Insufficient validation of untrusted input |
| CVE-2026-5886 | Medium | WebAudio | Out of bounds read |
| CVE-2026-5887 | Medium | Downloads | Insufficient validation of untrusted input |
| CVE-2026-5888 | Medium | WebCodecs | Uninitialized Use |
| CVE-2026-5889 | Medium | PDFium | Cryptographic Flaw |
| CVE-2026-5890 | Medium | WebCodecs | Race |
| CVE-2026-5891 | Medium | browser UI | Insufficient policy enforcement |
| CVE-2026-5892 | Medium | PWAs | Insufficient policy enforcement |
| CVE-2026-5893 | Medium | V8 | Race |
| CVE-2026-5894 | Low | PDF | Inappropriate implementation |
| CVE-2026-5895 | Low | Omnibox | Incorrect security UI |
| CVE-2026-5896 | Low | Audio | Policy bypass |
| CVE-2026-5897 | Low | Downloads | Incorrect security UI |
| CVE-2026-5898 | Low | Omnibox | Incorrect security UI |
| CVE-2026-5899 | Low | History Navigation | Incorrect security UI |
| CVE-2026-5900 | Low | Downloads | Policy bypass |
| CVE-2026-5901 | Low | DevTools | Policy bypass |
| CVE-2026-5902 | Low | Media | Race |
| CVE-2026-5903 | Low | IFrameSandbox | Policy bypass |
| CVE-2026-5904 | Low | V8 | Use after free |
| CVE-2026-5905 | Low | Permissions | Incorrect security UI |
| CVE-2026-5906 | Low | Omnibox | Incorrect security UI |
| CVE-2026-5907 | Low | Media | Insufficient data validation |
| CVE-2026-5908 | Low | Media | Integer overflow |
| CVE-2026-5909 | Low | Media | Integer overflow |
| CVE-2026-5910 | Low | Media | Integer overflow |
| CVE-2026-5911 | Low | ServiceWorkers | Policy bypass |
| CVE-2026-5912 | Low | WebRTC | Integer overflow |
| CVE-2026-5913 | Low | Blink | Out of bounds read |
| CVE-2026-5914 | Low | CSS | Type Confusion |
| CVE-2026-5915 | Low | WebML | Insufficient validation of untrusted input |
| CVE-2026-5918 | Low | Navigation | Inappropriate implementation |
| CVE-2026-5919 | Low | WebSockets | Insufficient validation of untrusted input |

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