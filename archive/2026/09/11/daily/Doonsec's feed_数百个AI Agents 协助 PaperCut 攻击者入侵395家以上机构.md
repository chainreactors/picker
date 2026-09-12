---
title: 数百个AI Agents 协助 PaperCut 攻击者入侵395家以上机构
url: https://mp.weixin.qq.com/s/IsAx4cOQnMylGSP5y5tSEw
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:46:50.343956
---

# 数百个AI Agents 协助 PaperCut 攻击者入侵395家以上机构

# 数百个AI Agents 协助 PaperCut 攻击者入侵395家以上机构

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

一名未知攻击者利用数百个AI代理，利用PaperCut MF/NG的两个漏洞入侵了至少395家机构。受害者主要集中在美国教育领域，且入侵行动进展迅速。其中有一例，一所美国高中从初步获取访问权限到获得域管理员权限仅用了7分钟。

![Papercut Logo 70+ Thousand Paper Cut Logo Royalty Free Images, Stock](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyJv0Dn3Jc2Uo2OTOxibTUl8CxUqddSzibG1AwnE7Wx8NK7YiaFmBic6hNItCJJU4picZo8IXyibKXOzAaHibqVjeFk9ETRSqWMdiaPGIkY/640?wx_fmt=jpeg&from=appmsg)

据威胁情报公司 GreyNoise 称，这些由 OpenAI 的 Codex 工具集和 DeepSeek 模型驱动的智能体还让恶意攻击者得以大规模攻击各类组织。该情报机构于 8 月 31 日追踪发现，此次攻击行动的指挥控制服务器 IP 地址为 45.142.193.132。

“攻击者仅用不到四小时就从空白的工作环境实现了对真实受害者的远程代码执行，又在两小时内拿下首个域管理员权限；而整个攻击活动启动后，仅用26秒就入侵了至少11家机构。”GreyNoise的分析师在周三发布的报告中表示。

这家安全供应商将这些入侵归因于一名“很可能讲俄语”的犯罪分子，此人利用人工智能针对几天前刚披露的一对 PaperCut 漏洞开发了攻击代码。

8月28日，打印管理软件供应商PaperCut发布紧急补丁以修复CVE-2026-81578和CVE-2026-82078漏洞，当时该供应商警告称，其“已确认收到客户受影响事件，并将以最高优先级处理此事”。

这些漏洞影响PaperCut NG和PaperCut MF，这两款软件是自托管的Java网络应用程序，在Windows系统上默认以系统级权限运行。

PaperCut 的首席执行官后来表示，首起被报告的安全事件发生在8月27日，涉及一家教育行业公司。

周四，PaperCut 发布了安全维护版本，以替代此前的紧急修复程序。

不过据 GreyNoise 称，目前已有至少 440 个实例遭到入侵，这些实例由 48 个国家的 395 个已确认受害组织托管。该威胁情报公司表示：“还有其他真实受害者无法归属于某一具体组织。”

勒索软件和其他网络犯罪活动通常会明确避免攻击俄罗斯及其他独联体国家，这些国家的政府往往为勒索者和受经济利益驱动的罪犯提供避风港——尤其是如果这些人同时还担任国家支持的黑客的日常工作。此外，除非犯罪团伙感染了本国境内的组织，否则当地警方通常会对这类网络入侵置之不理。

然而，PaperCut 攻击活动中的这些代理并非始终遵循这些指令，在某些情况下，他们仍对列入“禁止攻击名单”的目标发动了攻击。GreyNoise 表示：“目前尚不清楚[攻击者的]代理为何偏离了指令，但这是代理失控的一个典型例子。”

美国和英国是受害者人数最多的两个国家，分别为98人和59人。学校及其他教育行业机构是受影响最严重的群体，受害者达204人。相比之下，排名第二的行业（其他/未分类）有51名受害者，零售/商业/专业服务业以38名受害者位列第三。

在利用人工智能开发漏洞利用程序、实现远程代码执行并在自建实验室中窃取凭证后，这名恶意攻击者在公开互联网上部署了数百个人工智能代理，以寻找并攻击面向公众的易受攻击实例。GreyNoise 表示：“此次攻击活动似乎是机会主义行为。美国境内的目标高度集中在教育领域；不过，这很可能更多归因于 PaperCut NG/MF 的客户群。”

有趣的是，攻击者并未立即对所有受害者开展入侵后的恶意操作。GreyNoise 指出，攻击者在获取初始访问权限与获得域管理员权限之间存在“数天的延迟”，但这完全是因为攻击者自身未采取行动。最快的耗时为五分钟，最长则达到了144分钟。

目前也不清楚这名犯罪分子是仅专注于获取受入侵组织的访问权限，随后计划将攻击转交给附属机构或其他数据盗窃、勒索和勒索软件团伙，还是打算利用这一访问权限自行开展后续的恶意活动。

GreyNoise 自7月初以来一直在追踪45.142.193.132的恶意使用情况，并表示该IP地址曾被用于针对Palo Alto、Ubiquiti、思杰、SonicWall和Proxmox VE等面向互联网的技术和设备的攻击。

报告全文：

https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf

新闻链接：

https://www.theregister.com/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650

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