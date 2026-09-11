---
title: 分享的图片、视频、链接
url: https://mp.weixin.qq.com/s/i34VQDsZXhQD4D_6cgWKsA
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:49:32.608608
---

# 分享的图片、视频、链接

# Chaotic Eclipse 发布 ShieldCrash，用于Defender 零日漏洞的 PoC

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

研究员 Chaotic Eclipse 发布了 ShieldCrash，这是一个针对 Microsoft Defender 零日漏洞的 PoC 漏洞利用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyKibb3eOcmVYsSaOXAuslbZTEGibKXEXMiaIAOJr3lZcSL3J0Dia0kSdMCCLWXztbPkbelJOb49kzaibTQKPkYlBtcoOibHJx9UsHjkg/640?wx_fmt=jpeg&from=appmsg)

安全研究员 Chaotic Eclipse，也被称为 INFINITE NIGHTMARE、MSNightmare 和 Nightmare-Eclipse，发布了一个针对 Microsoft Defender 的新零日漏洞利用程序。研究员将该漏洞利用命名为 ShieldCrash，它以 SYSTEM 身份触发任意文件读取。

研究员Chaotic Eclipse称，微软尚未完全修复ShieldBreak漏洞（CVE-2026-69414）。据该研究人员表示，微软封堵了利用该漏洞的多种途径，但遗漏了一个特定条件，这一条件仍可让攻击者实施相同的攻击。

该研究人员发布了一份概念验证（PoC），证明其可利用系统权限读取任意文件，系统权限是 Windows 系统上的最高访问级别。他表示，即便安装了 2026 年 9 月的安全更新，所有受支持的 Windows 版本仍存在该漏洞。

“微软未能正确修复 ShieldBreak CVE-2026-69414，在特定条件下，仍有可能触发与 ShieldBreak 导致的完全相同的问题。尽管微软修复了多项内容以防止该问题被再次利用，但他们遗漏了一个仍可被利用 ShieldBreak 的地方。”

Chaotic Eclipse 写道：“该 PoC 可演示在 2026 年 9 月以系统权限实现任意文件读取，所有受支持的 Windows 版本均受影响。”

研究人员将此次概念验证（PoC）描述为目前的基础版本。他们后续可能会将其开发为完整的系统级漏洞利用程序，但目前仅发布了足以证明微软的补丁并未完全屏蔽 ShieldBreak 的代码。

微软近日更新了恶意软件防护引擎，以修复 CVE-2026-69414 漏洞。版本 1.1.26080.3 包含了该修复，此修复无需用户操作，且不会对禁用了微软 Defender 的系统产生影响。微软建议自动更新恶意软件定义和引擎。

上周，Chaotic Eclipse发布了一个针对英伟达的新型零日漏洞利用程序。研究人员将该利用程序命名为GreenSection，它会触发一个内存损坏漏洞。

近日，Chaotic Eclipse发布了一款针对卡巴斯基终端安全的零日漏洞利用程序，他将其命名为HardBreacher，该程序可触发权限提升漏洞。研究人员指出，该概念验证（PoC）程序不稳定，可能需要反复尝试，但成功利用后，它会以完全用户权限在系统32文件夹（System32）中创建一个动态链接库（DLL）。

该研究人员还声称，控制卡巴斯基的用户界面（UI）进程可破坏该杀毒软件并干扰文件访问控制，有可能使系统处于不稳定状态。

Chaotic Eclipse称，卡巴斯基终端安全零日漏洞可在运行卡巴斯基终端安全软件v14.0.0.504版本的完全补丁版Windows 11 25H2系统上实现权限提升。

这名研究员还发布了一款针对 GenDigital Avast 杀毒软件的零日漏洞利用工具，名为PrettyPrague。该利用工具可触发权限提升漏洞。

该研究人员声称在Avast防病毒软件发现一个漏洞，概念验证（PoC）程序利用Avast沙箱中的漏洞转储Windows SAM数据库，并获得系统级权限的shell。

据报道，即使是安装了所有最新补丁的Avast防病毒软件和Windows 11 25H2系统，该漏洞也能被利用。该研究人员还怀疑，该漏洞可能影响Gen Digital旗下的其他产品，包括AVG和诺顿。

最近，Chaotic Eclipse发布了一款针对 Crowdstrike Falcon 网络安全平台的新型零日漏洞利用程序，该漏洞利用程序被命名为 FalconFlank，它可触发权限提升漏洞。

据该研究人员称，FalconFlank 滥用了 Falcon 的“Microsoft Office 文件恶意宏移除”功能。该功能是 Falcon 修复能力的一部分，以高权限运行。研究人员表示，这一行为可被滥用来将权限从低权限本地用户提升至更高权限的上下文环境。

Chaotic Eclipse，又称Nightmare Eclipse，是一名安全研究员，以公开披露零日漏洞的概念验证（PoC）漏洞利用代码而闻名，他常在批评厂商对漏洞报告的处理方式后公开漏洞详细信息和漏洞利用代码。他的研究引发了关于负责任披露以及发布可利用漏洞的风险的争论。

新闻链接：

https://securityaffairs.com/198726/security/chaotic-eclipse-released-shieldcrash-a-poc-for-microsoft-defender-zero-day.html

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

爱拍照的老李

**讲述普通人能听懂的安全故事**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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