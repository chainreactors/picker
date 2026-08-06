---
title: SharePoint漏洞被用于攻击瑞士联邦信息技术机构
url: https://mp.weixin.qq.com/s/8lgWXOihsVT3HSa6pHgMzg
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T05:00:22.094847
---

# SharePoint漏洞被用于攻击瑞士联邦信息技术机构

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyJoNicQ7saBtibK1gay79YibdEqEsziaaGZg5DdeaVQToNa6yxm6ozHqhCibV3L98WibQuJwfbW31LwQ19ZGEKRqX0SM2JlY3eAnH5Qk/0?wx_fmt=jpeg)

# SharePoint漏洞被用于攻击瑞士联邦信息技术机构

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

瑞士联邦信息技术与通信局（简称 BIT 或 FOITT）披露，未知攻击者已入侵其本地 SharePoint 服务器上约 200 个账户。该局表示，未知攻击者疑似利用了微软 SharePoint 软件中的漏洞。

瑞士联邦信息技术办公室是瑞士联邦政府中规模最大的信息技术服务提供商。该机构提供约5万台工作站系统，与各行政部门合作开发定制化、安全且易用的信息技术解决方案，并主要在其自有现代化数据中心中运营超过1000个专业应用程序。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyKpBBr00IqlY39O2BQUehJzoSN3xEdkhncQNv9jCYSeNmviaJQy9sWMLCXjPby7icppShkIv5MLovkibTey55dGN33qWvcClY2olI/640?wx_fmt=png&from=appmsg)

联邦信息技术办公室负责运营联邦政府自有数据中心的服务器，该机构已开始安装所提供的安全更新。该办公室于7月28日发现异常情况，并在三天后的7月31日确认账户遭入侵。

“专家们在分析过程中于7月31日发现，约200个用户账户和技术账户的登录信息已遭泄露。”瑞士资讯媒体报道称。

“据瑞士联邦信息技术与电信办公室（FOITT）自行表示，该机构已立即重置了相关密码。基于瑞士国家网络安全中心（NCSC）和微软公司协助下开展的截至目前的调查，目前没有发现任何进一步的数据泄露证据。不过，相关分析仍在进行中。”

用户账户和技术账户均受到影响。同日，异常访问行为被检测到，FOITT 封锁了 SharePoint 的外部互联网访问，并开始进行补丁修复。

该机构正在彻底重装受影响的服务器，同时已通过国家网络安全机构的平台，向瑞士关键基础设施运营商共享了所有相关技术指标。

微软于7月14日披露多个严重的SharePoint漏洞。其中一个编号为CVE-2026-50522（通用漏洞评分系统评分9.8分）的漏洞，可能让攻击者通过网络执行远程代码。

微软表示，该漏洞的利用复杂度较低，因为攻击者无需掌握系统的大量知识即可完成攻击。研究人员警告称，攻击者正在窃取计算机密钥以维持长期访问权限。最后这一点是关键细节：计算机密钥是IIS用于签署会话令牌的加密密钥，一旦被盗，攻击者就能伪造看似合法的请求，而完全打了补丁的服务器仍会接受这些请求。

瑞士联邦信息技术、电信和邮政办公室（FOITT）在网络事件发生后，正作为预防措施重新安装受影响的SharePoint服务器。相关工作完成前，外部互联网访问仍被封锁，而联邦员工仍可通过其他渠道访问和共享文档。该办公室指出，该平台并非用于存储机密信息或高度敏感的个人数据。

由于与微软身份验证系统深度集成，SharePoint 正日益成为黑客攻击目标。攻击者利用漏洞可将其作为突破口，入侵更广泛的网络，这使得 SharePoint 服务器直接暴露在公网成为日益严峻的安全风险。

微软和美国网络安全与基础设施安全局（CISA）均未公开将此次漏洞利用归因于任何特定的威胁组织。

技术报告：

https://securityaffairs.com/196625/hacking/sharepoint-flaws-used-to-hack-switzerlands-federal-it-agency.html

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