---
title: 【安全圈】新型复杂攻击利用 Windows Defender 绕过 EDR
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066971&idx=3&sn=838beca7d5e601a4b9c07173c7639859&chksm=f36e78dbc419f1cdae40ee1c823f9700669fdab4f9651c6afdfdaee8ae37c8ff795b8653caf2&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-28
fetch_date: 2025-10-06T19:39:17.415042
---

# 【安全圈】新型复杂攻击利用 Windows Defender 绕过 EDR

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgBD2icZhFccozdbiaDibbkZTsTJTXMrHT2PtXfoWgnB9R0pZRicuTSPP3yJYiaXQ8eGS4uYFSMnhqmgwg/0?wx_fmt=jpeg)

# 【安全圈】新型复杂攻击利用 Windows Defender 绕过 EDR

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgBD2icZhFccozdbiaDibbkZTseibOhPKb8T5TJhHzpp1Cibvs5JiaricVicygtxEE4iazeNHoOiayvoNLzzJWQ/640?wx_fmt=jpeg&from=appmsg)

一种复杂的攻击技术，利用 Windows Defender 应用程序控制 (WDAC) 来禁用 Windows 机器上的端点检测和响应 (EDR) 传感器。

WDAC 是 Windows 10 和 Windows Server 2016 中引入的一项技术，旨在让组织对其 Windows 设备上的可执行代码进行细粒度控制。

然而，安全专家发现，恶意行为者可以利用此功能，从而可能使整个网络容易受到攻击。

该技术属于 MITRE ATT＆CK 框架的“削弱防御”类别（T1562），允许具有管理权限的攻击者制定和部署专门设计的 WDAC 策略。

这些策略可以有效阻止 EDR 传感器在系统启动期间加载，使其无法运行，并允许对手在不受这些关键安全解决方案约束的情况下进行操作。

攻击可以以各种方式执行，从针对单个计算机到破坏整个域。在最严重的情况下，具有域管理员权限的攻击者可以在整个组织中分发恶意 WDAC 策略，系统地禁用所有端点上的EDR 传感器。

## **攻击如何进行**

此次攻击涉及三个主要阶段：

1. **策略放置**：攻击者创建自定义 WDAC 策略，允许自己的工具执行，同时阻止安全解决方案。然后，将此策略放置在 `C:\Windows\System32\CodeIntegrity\` 目标计算机上的目录中。
2. **重启要求**：由于 WDAC 策略仅在重启后才适用，因此攻击者需要重新启动端点以强制执行新策略。
3. **禁用 EDR**：重新启动后，恶意策略生效，阻止 EDR 传感器启动并使系统容易受到进一步攻击。

一个名为“Krueger”的概念验证工具已经出现，专门针对这种攻击媒介而设计。Krueger 由安全研究员 Logan Goins 创建，可以作为后利用活动的一部分在内存中运行，使其成为攻击者武器库中的有力武器。

由于此攻击使用了合法的 Windows 功能，因此检测起来很困难，但专家建议采取几种缓解策略。

这些措施包括通过组策略强制执行 WDAC 策略、限制代码完整性文件夹和 SMB 共享的权限以及遵守网络管理中的最小特权原则。

## **缓解策略**

组织可以通过以下方式减少受到此威胁的风险：

* **通过 GPO 执行 WDAC 策略**：部署覆盖本地更改的中央 WDAC 策略，确保恶意策略无法生效。
* **应用最小特权原则**：限制修改 WDAC 策略、访问 SMB 共享或写入敏感文件夹的权限。
* **实施安全管理实践**：使用 Microsoft 的本地管理员密码解决方案 (LAPS) 等工具禁用或保护本地管理员帐户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgBD2icZhFccozdbiaDibbkZTsT2jia02apN1Duz9l9U3GwicKzJGnwDTsKMtqP4hgmvmTK1gxb5tyWmaQ/640?wx_fmt=jpeg&from=appmsg)

一家财富 500 强公司的首席信息安全官马克·约翰逊警告称：“组织需要意识到这种威胁并采取主动措施。实施强大的访问控制和定期审核 WDAC 政策现在比以往任何时候都更加重要。”

随着安全工具变得越来越复杂，破坏它们的方法也越来越复杂。这凸显了采取多层次网络安全方法的必要性，以及在新兴攻击技术面前保持警惕的必要性。

当网络安全社区努力应对这一新威胁时，我们敦促各组织审查其安全态势并确保采取适当的保障措施。

来源：https://cybersecuritynews.com/attack-weaponizes-windows-defender/

***END***

阅读推荐

[【安全圈】看不到的尽头，回顾与展望哈以冲突以来的中东网络战](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=1&sn=41fcfb549fe6615344138a9b1dd305a6&scene=21#wechat_redirect)

[【安全圈】日本航空系统遭受网络攻击，航班运营受到影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=2&sn=3e1dc47d1e9b6168f7631925ca6ddc17&scene=21#wechat_redirect)

[【安全圈】iOS 设备比 Android 设备更容易受到网络钓鱼的攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=3&sn=61fa616d789cbc824c026a48a98d9e84&scene=21#wechat_redirect)

[【安全圈】土耳其出台更严格的加密货币反洗钱法规](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=4&sn=4490e636262f92d14975414c55a29edb&scene=21#wechat_redirect)

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

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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
在看
，轻点两下取消在看
分享
留言
收藏
听过