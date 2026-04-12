---
title: ESET警告：勒索软件团伙将EDR杀手的使用范围扩大到易受攻击的驱动程序之外
url: https://mp.weixin.qq.com/s/q8rLiMHHaYK3tLeHfeZtrw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:09.283405
---

# ESET警告：勒索软件团伙将EDR杀手的使用范围扩大到易受攻击的驱动程序之外

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NpRRlCgoxApIpXLVu6gNFiaCuQCEEaricAmhu20oO0CD530nA4YxeBUY1mnPm2Z5CrxQ98gUIwgIvVrXF00Y4jXRSrUj0HxicR94/0?wx_fmt=jpeg)

# ESET警告：勒索软件团伙将EDR杀手的使用范围扩大到易受攻击的驱动程序之外

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近年来，端点检测与响应 (EDR) 工具已成为现代勒索软件入侵中一种标准且高效的武器。网络犯罪分子在启动文件加密恶意软件之前，通常会部署专门的工具来绕过安全软件。

根据 ESET Research 的一份最新综合报告，威胁形势已经远远超出了众所周知的自带漏洞驱动程序 (BYOVD)技术。

攻击者现在大量使用无驱动方法、自定义命令行脚本和合法的反rootkit实用程序来关闭安全防御。

## **为什么攻击者更喜欢 EDR 杀手**

与其不断重写和更新勒索软件加密器以逃避安全检测，威胁行为者发现，直接关闭安全软件要容易得多。

EDR 杀手提供了一种高度可靠、低成本的解决方案，它为攻击者提供了一个可预测的窗口来运行其固有的嘈杂加密有效载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OtD2FMKIvr5wIDthaDrdCqLh7XR6ib72zgibGI95LpibqhAdsqwHseqhr7WGsPZiaQhCt6FxibzvgUfTGsA1V7Sx9KwsRYssstI28A/640?wx_fmt=png&from=appmsg)

有趣的是，ESET 指出，勒索软件联盟成员（而不是核心的勒索软件即服务运营商）通常会选择在攻击中部署哪个 EDR 杀手。

这种动态在实际应用中产生了巨大的工具多样性，因为不同的联盟会混合搭配各种 EDR 拦截器，以满足他们特定的入侵需求和技能水平。

虽然利用 BYOVD 漏洞内核驱动程序仍然是主要方法，但 EDR 杀手背后的技术正在迅速发展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7McasRLg7iauaF5zx9PBsrtohvV0YKAzZMrx97yicNyFPXu1TkNdjuMozicaGsNgz5gPQ6fl9gJ9h4IeYAa9cOOvhqwXnXNjWgeoY/640?wx_fmt=png&from=appmsg)

ESET 研究人员目前正在追踪近 90 种在实际应用中活跃的 EDR 攻击工具，其中 54 种依赖于 BYOVD 来利用 35 种不同的易受攻击的驱动程序。

一些技术水平较低的攻击者依靠基本的命令行脚本或将系统重启到 Windows 安全模式来绕过安全措施。而更老练的攻击者则会利用合法的反 rootkit 程序，例如 GMER 和 PC Hunter。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OBKDOoQwuoEp6ffdoMbcVA4pfRqGsHQ3k46ibQafyDt3HjEYAXXTjmuBQEGibibVzz7EtJB4f9LgTicMdqpTtoxk7icYMUCZCTrU9c/640?wx_fmt=png&from=appmsg)

这些工具最初是为清除内核深处的恶意软件而开发的，但它们所拥有的高级权限使它们成为终止活动安全进程的理想武器。

一种日益增长且危险的趋势是使用无需驱动的EDR清除工具。像EDRSilencer 和EDR-Freeze这样的工具完全不需要与系统内核交互。

相反，它们会阻断终端和安全后端之间的网络通信，或者强制EDR软件停止运行。由于这些方法不依赖于传统的驱动程序漏洞，因此网络防御者更难检测到它们。

ESET 的调查将这些工具的开发者分为三大类。第一类是封闭式组织，例如 Embargo、DeadLock 和 Warlock，它们从零开始开发自己的专有 EDR 攻击工具。

研究人员强烈怀疑像 Warlock 这样的组织正在使用人工智能来协助编写和更新他们的 EDR 杀手代码。

其次，许多攻击者会修改公开可用的概念验证（PoC）代码。开放代码库提供了现成的模板，攻击者可以通过更改编程语言或添加简单的代码混淆来轻松对其进行修改。

最后，蓬勃发展的地下市场现在提供“EDR 杀手即服务”。商业工具在暗网论坛上被积极出售给大型勒索软件团伙的成员，并提供完整的客户支持。

由于这些工具被大量交易和共享，网络安全防御者面临着巨大的挑战。仅仅分析某个存在漏洞的驱动程序已不足以识别特定的勒索软件团伙。

完全不相关的工具可能会滥用同一个驱动程序，同一个威胁组织可能会在不同的攻击中使用多个驱动程序。

随着 EDR 杀手市场不断成熟和商业化，组织必须专注于检测安全篡改的行为迹象，而不仅仅是跟踪特定的易受攻击的驱动因素。

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