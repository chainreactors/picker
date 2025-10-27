---
title: 新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545855&idx=4&sn=7fff3ff03802bc5017a29eaf17bb61cb&chksm=fa93853ecde40c284a651ac669217dbafefe85c00f7abad6e0aa34594cf0d44a6567d003abb7&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-16
fetch_date: 2025-10-06T17:44:47.839635
---

# 新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nibia6O70bO3Ou8egKF1AIVZXDxxCLH2ib6WGyMeR9OSJ5bibUhuibibW6xLwzrNTCzNciavGHOfpP6PPOw/0?wx_fmt=jpeg)

# 新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM

网络安全应急技术国家工程中心

今年最新出现了一种名为 Eldorado 的新型勒索软件即服务 (RaaS)，它带有适用于 VMware ESXi 和 Windows 的锁版变种。该团伙目前已危害 16 名受害者，其中大部分在美国，涉及房地产、教育、医疗保健和制造业。

网络安全公司的研究人员监控了 Eldorado 的活动，并注意到其运营商在 RAMP 论坛上推广恶意服务，并寻求熟练的附属机构加入该计划。

Eldorado 还运营着一个列出受害者名单的数据泄露网站，但在撰写本文时该网站已处于瘫痪状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29R0lgLzHp97R9SjdUicTdLgWcUOP4Q6bdkMG9uW17FVQCHneaQjhjQ9Y849zL1oAR59sIwLlrrvcw/640?wx_fmt=png&from=appmsg&wxfrom=13)

Eldorado 勒索软件目标

# **加密 Windows 和 Linux**

Eldorado 是一款基于 Go 的勒索软件，可通过两个不同的变体加密 Windows 和 Linux 平台，且这两个变体的操作非常相似。

研究人员从开发人员那里获得了一个加密器，该加密器附带一份用户手册，其中说明有适用于 VMware ESXi 虚拟机管理程序和 Windows 的 32/64 位变体。

Group-IB 表示，Eldorado 是一个独特的开发项目。该恶意软件使用 ChaCha20 算法进行加密，并为每个锁定的文件生成唯一的 32 字节密钥和 12 字节随机数。然后使用 RSA 和最佳非对称加密填充 (OAEP) 方案对密钥和随机数进行加密。

加密阶段结束后，文件将被附加“.00000001”扩展名，名为“HOW\_RETURN\_YOUR\_DATA.TXT”的勒索信将被放置在 Documents 和 Desktop 文件夹中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29R0lgLzHp97R9SjdUicTdLgu81BIdW7DYWSBV78ouwvXv6B7POFKOTRkL3yefahjS0twgAltYLpzw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Eldorado 的赎金条

Eldorado 还利用 SMB 通信协议加密网络共享，以最大限度地发挥其影响，并删除受感染 Windows 计算机上的卷影副本，以防止恢复。

勒索软件会跳过 DLL、LNK、SYS 和 EXE 文件，以及与系统启动和基本功能相关的文件和目录，以防止导致系统无法启动/无法使用。最后，它默认设置为自我删除，以逃避响应团队的检测和分析。

据渗透到该行动中的安全研究人员称，联盟成员可以定制他们的攻击。例如，在 Windows 上，他们可以指定要加密的目录、跳过本地文件、针对特定子网上的网络共享，并防止恶意软件自我删除。

但是，在 Linux 上，自定义参数止步于设置要加密的目录。

# **防御建议**

安全研究人员强调，Eldorado 勒索软件威胁是一个新的、独立的行动，并不是以另一个组织的名义重新出现的。而尽管 Eldorado 相对较新，且并非知名勒索软件组织的改头换面，但它已在短时间内迅速证明了其能够对受害者的数据、声誉和业务连续性造成重大损害的能力。

研究人员建议采取以下防御措施，这将在一定程度上有助于用户防范所有勒索软件攻击：

·实施多因素身份验证 (MFA) 和基于凭证的访问解决方案。

·使用端点检测和响应 (EDR) 快速识别和响应勒索软件指标。

·定期备份数据以最大限度地减少损害和数据丢失。

·利用基于人工智能的分析和高级恶意软件引爆进行实时入侵检测和响应。

·确定优先级并定期应用安全补丁来修复漏洞。

·培训员工能够识别网络安全威胁。

·进行年度技术审计或安全评估并保持数字安全。

·不要支付赎金，因为它很少能确保数据恢复，而且可能导致更多攻击。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/new-eldorado-ransomware-targets-windows-vmware-esxi-vms/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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