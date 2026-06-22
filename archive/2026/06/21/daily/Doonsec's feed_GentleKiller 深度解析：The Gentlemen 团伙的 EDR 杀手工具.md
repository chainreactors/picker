---
title: GentleKiller 深度解析：The Gentlemen 团伙的 EDR 杀手工具
url: https://mp.weixin.qq.com/s/D7isrUhBt_Pvwkgp7YA5yw
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:35.977229
---

# GentleKiller 深度解析：The Gentlemen 团伙的 EDR 杀手工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0107TCFvQiaJETyw2UKTL3DwqJZB6Oa3FQhmdRQG6lRZNc8Xq0fibgAVKMqft8uNxOdQh7IPedbFD2BZwmosve7Nfl5iaG9W8ZV8/0?wx_fmt=jpeg)

# GentleKiller 深度解析：The Gentlemen 团伙的 EDR 杀手工具

FreeBuf
FreeBuf

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX2ndfiaTttXorGibJp2Q0mFMiayY8UjrBiaScGswfqAVvraWEicYib8jvGpTwOepV0JicFpQf3QmXLz62ia2NEoBZNe8JWxvts0YNCBwcI/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1tZhq3qDSvqJicRUEmjKN9HtjvXZNCGKFX1zM3V4yibk24bLfUmefXVy479g2dQfF0yqGVm2v9L6uO6I5eNqLl6Xjx8wuFvtvGk/640?wx_fmt=png&from=appmsg)

The Gentlemen为旗下分支机构提供了一套集中化的EDR（终端检测与响应）清除工具套件，能够快速利用BYOVD（自带漏洞驱动程序）攻击手段在勒索软件攻击前禁用安全防护工具。2026年6月18日，ESET发布了对该团伙技术基础设施的详细分析报告，这份报告基于数月的事件级调查，并得到了该团伙2026年5月内部数据泄露的佐证。自2025年底出现以来，The Gentlemen已宣称攻击了504个受害者，成为2026年第一季度最活跃的五大勒索软件组织之一。其独特之处不在于勒索软件本身，而在于执行勒索前提供给分支机构的工具。

Part01

标准化攻击框架

大多数勒索软件即服务（RaaS）运营商让分支机构自行寻找禁用终端安全工具的方法，而The Gentlemen采取了不同策略。ESET报告指出："该团伙展示了一种有趣的做法：由运营商统一管理的EDR杀手工具，供分支机构直接使用。当大多数勒索软件团伙仍将EDR清除任务下放给分支机构时，The Gentlemen选择通过提供即用型标准化EDR清除套件来集中这一功能。这一决策使其成为对分支机构极具吸引力的运营商，因为实质上降低了准入门槛，使他们的工作更加轻松。"

泄露的内部数据证实了ESET自2026年2月以来的推测：该团伙首领zeta88曾公开讨论向分支机构维护和分发EDR清除工具包。

![GentleKiller工具架构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3QC8sxsDVkHKW1uiaRGrA6Xtd3pwXs3ceKUODcymrzjHoibicGaVwFwVsSVEnO3LkOxIB1hgTKFNBicASERlib8zCOP7ibghnBnbbKw/640?wx_fmt=jpeg)

Part02

GentleKiller 核心组件

该套件的核心是GentleKiller，一个包含至少八个不同变种的内部框架。每个变种都伪装成不同的合法产品，并通过BYOVD技术滥用不同的漏洞或恶意内核驱动程序。ESET表示："GentleKiller是目前在The Gentlemen生态系统中观察到的最普遍的EDR清除工具。截至本文撰写时，我们已发现至少八个不同变种，每个都伪装成不同的合法产品并滥用不同的漏洞或恶意驱动程序。当剥离伪装层和使用的特定驱动程序后，底层代码显示出众多结构和行为上的共性，强烈表明使用了共享开发模板。该模板在各变种间重复使用，仅做最小修改。"

这八个变种针对的驱动程序来自卡巴斯基、FACEIT反作弊系统、Valorant、Javelin、Safetica、Zemana、奇虎360、IObit以及PoisonX rootkit。所有变种的GentleKiller会搜寻超过400个进程，涉及48种不同的安全产品，包括CrowdStrike、SentinelOne、Microsoft Defender、Sophos、Carbon Black和ESET自身。

Part03

快速适应能力

研究人员指出，快速适应能力是其另一显著特征。报告继续说明："这种设计优先考虑分支机构的部署便捷性和操作灵活性，同时最小化运营商开发工作量。它使The Gentlemen运营商能够在EDR清除PoC公开后很快将滥用的驱动程序集成到工具集中。UnknownKiller和PoisonKiller就是这种情况，它们在公开几天内就被采用。"ESET以天为单位测量了这一速度——UnknownKiller和PoisonKiller的概念验证都在公开发布后数日内被采用。

除GentleKiller外，该套件还包含三个第三方工具。HexKiller曾仅与Warlock勒索软件团伙关联，使用百度杀毒驱动程序，出现在与GentleKiller相同的GentlemenCollection目录下的入侵活动中。ThrottleBlood更常见于MedusaLocker和DragonForce分支机构攻击，使用TechPowerUp驱动程序。HavocKiller由Huntress在2026年3月公开披露，但早在1月23日就已在The Gentlemen入侵活动中活跃。ESET评估认为，这三个工具均由运营商从外部获取，然后采用与GentleKiller相同的防御规避层进行标准化处理：通过Enigma或Themida进行二进制保护、模仿安全厂商的文件名、伪造版本信息、复制数字签名以及匹配图标。

Part04

独特的受害者选择模式

受害者分布打破了大多数主要勒索软件运营的固有模式。与Qilin、DragonForce和Akira主要集中在美国（通常占受害者半数左右）不同，The Gentlemen的名单偏向东南亚、南美和西欧。泄露数据表明这并非偶然：该团伙主要根据FortiGate配置错误而非地理位置选择受害者，并集中向分支机构分发目标。这是一种结构化选择过程，而非由各分支机构自行选择目标。

ESET还发现了一个名为OxideHarvest（也被追踪为buildx641）的基于Rust的凭证窃取程序，与其中一个分支机构关联。它针对Chrome、Edge、Firefox、Brave、Opera、OperaGX、Vivaldi、Waterfox等十余种浏览器，使用提供的凭证登录指定主机，提取浏览器凭证并写入输出文件。与有明显内部开发证据的GentleKiller不同，OxideHarvest被归因于名为quant的分支机构而非核心运营商。

Part05

团伙头目身份曝光

2026年6月10日，Brian Krebs发布了关于该团伙创始人hastalamuerte真实身份的证据，确认为36岁的俄罗斯公民Alexander Andreevich Yapaev，曾是Qilin、Embargo、LockBit、Medusa和BlackLock的分支机构成员。Krebs写道："数据泄露追踪服务Constella Intelligence报告称，Hastalamuerte的Telegram ID关联到另一个用户名'bu4vs'以及俄罗斯电话号码79127650004。在Constella中查询该电话号码可获取来自被黑俄罗斯政府数据库的多条记录，显示其归属于一位来自伊热夫斯克的36岁男子Alexander Andreevich Yapaev。"

报告显示，The Gentlemen能快速将新披露的BYOVD概念验证武器化，通常在公开后数日内就将漏洞驱动程序攻击整合到运营中。对防御者而言，ESET报告的实际意义在于：GentleKiller的进程目标列表现已公开，这意味着防御者可以利用它设计监控和检测策略，即使对尚未构建的变种也能保持有效性。

参考来源：

Inside GentleKiller: The EDR-Killer Powering The Gentlemen

https://securityaffairs.com/193941/uncategorized/inside-gentlekiller-the-edr-killer-powering-the-gentlemen.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1X4enJ3Jg430Lq35ib6TKMfwMWPxpHxMTQkuB9iaHj8Dj755KsjMFZvicpFQEoIcZc5MiblY9MAMfKjrACxXChC1QibqxBjRdYoSAM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3X7WGI2rXPqAzCWXrGjRKsN5yjUV9BoibElELIHDAkotuemLyRebpuqevWQ5EkFXCsicicbVEnB6iaAgd8a7hBYX4m430XS37O4CQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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