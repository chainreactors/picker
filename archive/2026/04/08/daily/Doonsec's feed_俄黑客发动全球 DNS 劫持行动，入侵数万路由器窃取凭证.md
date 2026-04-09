---
title: 俄黑客发动全球 DNS 劫持行动，入侵数万路由器窃取凭证
url: https://mp.weixin.qq.com/s/C_jF5Z105SaBjjtu6CU1jA
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:29:40.361093
---

# 俄黑客发动全球 DNS 劫持行动，入侵数万路由器窃取凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ricqMN2UMva44WTib1OZ4Yt6iaq2klemMXQochZ3Yat9R1F4V9lLLobMUF9GNdqziavwjwticHicJvP0anjv6s0k8VeHpQoQF24O9eCiaeGH8iaWYPE/0?wx_fmt=jpeg)

# 俄黑客发动全球 DNS 劫持行动，入侵数万路由器窃取凭证

HackerNews
HackerNews

安全威胁纵横

![]()

在小说阅读器中沉浸阅读

高危漏洞

**紧急修复指南**

RCE Patch

俄罗斯APT28组织（又名Forest Blizzard）自2025年5月起入侵MikroTik和TP-Link路由器，将其转为恶意基础设施用于网络间谍活动。

推测e

Lumen旗下Black Lotus Labs将俄罗斯关联威胁行为体APT28（又名Forest Blizzard）与代号为"FrostArmada"的大规模行动关联。

自2025年5月起，该组织入侵不安全的MikroTik和TP-Link路由器，修改DNS设置将其转为受控恶意基础设施，作为网络间谍活动的一部分。微软指出，此举旨在劫持家庭和小型办公（SOHO）网络设备的DNS流量，实现网络数据被动收集。

据评估，活动最早于2025年5月小规模启动，8月初开始大规模扩张。2025年12月高峰期，来自120多个国家的超过1.8万个独立IP地址与APT28基础设施通信。微软已识别超过200个组织和5000台消费设备受影响。

**1**

**攻击手法与目标**

Black Lotus Labs报告显示，APT28修改受入侵路由器的DNS设置，劫持本地网络流量。当用户请求目标域名时，流量被重定向至中间人（AitM）节点，在无需终端用户交互的情况下捕获并外泄认证凭证。攻击主要针对北非、中美、东南亚和欧洲各国的外交部、执法部门及第三方邮件和云服务提供商。

微软表示，这是首次观察到该组织大规模利用DNS劫持支持TLS连接的中间人攻击。攻击者通过入侵大型目标上游的边缘设备，利用管理较松散的资产转向企业环境，实现持久被动侦察。

**2**

**漏洞利用与联合打击**

据称APT28利用TP-Link WR841N路由器的CVE-2023-50224漏洞（CVSS 6.5）进行DNS投毒，并通过特制HTTP GET请求提取存储凭证。此外还发现第二组服务器集群接收DNS请求并转发至远程攻击者服务器，该集群还对乌克兰少量MikroTik路由器进行交互式操作。

相关基础设施已在美国司法部、联邦调查局及其他国际合作伙伴的联合行动中被破坏并下线。

微软警告，虽然当前仅观察到信息收集活动，但攻击者可能利用中间人位置实现恶意软件部署或拒绝服务等进一步破坏。

转载请注明出处@安全威胁纵横，封面来源于网络；

**消息来源：https://thehackernews.com/2026/04/russian-state-linked-apt28-exploits.html**

更多网络安全视频，请关注视频号“知道创宇404实验室”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

安全威胁纵横

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

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