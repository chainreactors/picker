---
title: 【安全圈】点了「不允许」它还在录：iOS权限旁路细节公开
url: https://mp.weixin.qq.com/s/56gYltJNw1q0R2mzR6Uptw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:08.699678
---

# 【安全圈】点了「不允许」它还在录：iOS权限旁路细节公开

# 【安全圈】点了「不允许」它还在录：iOS权限旁路细节公开

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

iOS

**核心事实**：iPhone 与 iPad 上，用户在麦克风弹窗里点了「不允许」，应用仍然能录音。漏洞编号 **CVE-2026-65339**，首次修复随 8 月 17 日的安全更新下发。Meta 红队与另一位独立研究者上周各自公开了技术细节。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHicZG9zKhHWCcZNBA2eGswq8ImTv6T1A2CW7tBhdGVu0KemSRRT54c87vA41BStcBNwjzribdXahniblqzShUG60xt5liafYd2pXc/640?wx_fmt=other&from=appmsg)

按 Tsytsarkin 的测试记录：应用第一次启动时弹出权限请求，点拒绝，录音不受影响；之后再启动，弹窗不再出现，权限状态是明确的「已拒绝」，录音照旧。Calap 那边的复现里，权限读数同样停在 denied，应用在录，灵动岛和下拉控制中心都没有橙色指示点。

苹果在 8 月的更新说明里只写了一句「应用可能泄露用户敏感信息」。研究者认为这句话漏掉了最要紧的部分——录音发生在授权被拒之后，而且指示器不亮。

## 🔍 漏洞在哪：一个服务信了应用的话

iOS 里决定「能不能用麦克风」的不是应用自己，是 TCC（Transparency, Consent, and Control）。TCC 检查的是**哪个进程在请求**，依据是一枚 audit token——内核给每个进程发的身份凭证。

问题出在音频服务 `audiomxd` 这一步。它接受调用方自己报上来的 audit token，而没有独立核实真实调用者。应用完全可以递过去一枚写着 `audiomxd` 自己的 token，服务就把它当成了自己人。

一旦被当成自己人，服务就走上了那条为自身内部音频准备的捷径——不查 TCC，直接放行。更麻烦的是，应用伪造身份所需的那些细节，是**内核自己交给它的**。这条路径不需要越狱，不需要私有 entitlement，一个普通沙箱应用就够。

## 🎤 录完之后，指示器也没亮

iOS 用橙色点提示麦克风正在被使用。Calap 的测试里这个点始终没出现；Tsytsarkin 更早一版的测试构建里同样没有，他自己在文章里补了一句——演示视频是后来在「恢复了橙色指示器」的构建上录的。

系统日志的解释很直白：日志里没有这个应用使用麦克风的记录，记录指向的是音频服务本身。也就是说，从系统的角度看，录音这件事是 `audiomxd` 干的，跟那个应用无关。指示器挂的应用侧状态，自然不会亮。

两位研究者都没有给出「事后怎么查自己有没有被录」的办法。前台的某个时刻必须已经开始录音，之后切后台、锁屏都能继续；带后台录音的版本还需要在 Info.plist 里加 `UIBackgroundModes = audio`。这些都发生在用户看不见的地方。

## 📦 影响范围与版本

Calap 在 7 月 27 日发布的 **iOS 26.6** 上复现成功，也在 iPadOS 27 的一个 beta 上复现。两个测试应用都是普通沙箱应用，没加任何 entitlement，唯一的隐私声明是让弹窗出现的 `NSMicrophoneUsageDescription`。

* **iOS / iPadOS 26.6.1**

  ：8 月 17 日，iPhone 11 及后续、iPad Pro 12.9 英寸第 3 代及后续、iPad Air 第 3 代及后续、iPad 第 8 代及后续、iPad mini 第 5 代及后续
* **iOS / iPadOS 18.7.11**

  ：10 月 26 日，覆盖 iPhone XS、XS Max、XR 与 iPad 第 7 代
* **macOS Tahoe 26.6.2**

  （8 月 17 日）、**macOS Sequoia 15.8**（9 月 14 日）、tvOS 27、watchOS 27、visionOS 27（均为 9 月 14 日）

有一点必须说清楚：两位研究者的测试应用都是通过 Xcode 直接装到设备上的，**没有走 App Review**。所以现有材料无法证明审核流程会不会拦住这类应用。另外，旁路只覆盖通过音频服务采集麦克风这一条路，应用拿不到其他隐私权限。

## 🔧 修的是什么

修复让 `audiomxd` 校验由内核提供的真实调用者身份，而不是采信调用方递来的那枚 token。外部调用方若想替换服务所依赖的客户端身份，需要持有私有 entitlement `com.apple.private.audio.client-audit-token-override`。这个 entitlement 应用无法自己给自己。

披露节奏本身有点意思。Meta 的时间线显示修复在 **8 月 10 日**就已进入 iOS 27.0 beta 5，但 iOS 27 的发布说明至今没有列出这个漏洞，8 月 17 日那次更新的说明也只写了「泄露敏感信息」。CVE 记录里，CISA 给出的 CVSS 评分是 **5.0**，该漏洞不在已知被利用漏洞目录中。

## ✅ 现在该做什么

没有任何设置项能挡住这条旁路，两位研究者也明确说了这一点。唯一的办法是把系统升到上面列出的版本或更高。苹果与两位研究者均未报告该漏洞被在野利用。

* **先看版本**

  ：设置 → 通用 → 关于本机。iOS 26.6 及以下、iOS 18.7.10 及以下都在受影响区间。
* **老设备别放弃**

  ：iPhone XS / XR 这一代拿的是 iOS 18.7.11，不是 26.6.1。两条更新线要分清。
* **别指望指示器**

  ：这次事件里橙色点缺失恰恰是特征之一。它的存在与否，不能作为「有没有被录音」的判断依据。

***END***

阅读推荐

[【安全圈】178个站点被投毒：官方CDN送出了盗卡脚本](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=1&sn=30b6dbda996787a2462c7afcd183f474&scene=21#wechat_redirect)

[【安全圈】运维工具长出蠕虫：SCKit跳到技术员电脑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=2&sn=a83acfe4ccc4a76cfdbf3a930ca47aca&scene=21#wechat_redirect)

[【安全圈】一次补掉17个洞：遗留API开关被彻底删除](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=3&sn=cbb961e616211be500f55d885d1a8cac&scene=21#wechat_redirect)

[【安全圈】无印良品明文存卡号：109万张信用卡多留了五年](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079900&idx=1&sn=07e67415a5bb07511d553704768da1d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过