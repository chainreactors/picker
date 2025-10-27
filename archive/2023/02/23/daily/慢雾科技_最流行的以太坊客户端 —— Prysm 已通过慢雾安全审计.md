---
title: 最流行的以太坊客户端 —— Prysm 已通过慢雾安全审计
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497093&idx=1&sn=c96c09970099c484242a758938b57bd7&chksm=fdde8b02caa90214a34aa116c0f7bd3c1116dbadce29636882a0caebc24559c91903ba253876&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-02-23
fetch_date: 2025-10-04T07:51:40.686977
---

# 最流行的以太坊客户端 —— Prysm 已通过慢雾安全审计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYBCWibmyVYOVd33sUwS0Nibhkzqd5fhqkvM0MoOU3uovNksibWKpMbiaYYr2hibXN2zTW8wYhDDU3x4JA/0?wx_fmt=jpeg)

# 最流行的以太坊客户端 —— Prysm 已通过慢雾安全审计

慢雾安全团队

慢雾科技

近期，慢雾(SlowMist) 正式完成了对以太坊共识层客户端 Prysm 的安全审计服务。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYBCWibmyVYOVd33sUwS0Nibh1sL9JKnBaoib7XLTNZoFTibprAbslCtbkPVNuv2sMWqaWExmUo23Ed9A/640?wx_fmt=png)

众所周知，以太坊节点的行为是由其运行的客户端软件控制的，因此客户端多样性对以太坊的网络健康至关重要，客户端内的错误占比超过 33% 会导致以太坊离线。当拥有三分之二多节点的客户端出现严重漏洞，可能会导致链错误分叉，并可能造成罚没。

Prysm 是一个用 Go 编写的以太坊共识层实现，由以太坊核心开发团队 Prysmatic Labs 开发，用户可以使用 Prysm 运行一个节点来参与以太坊的去中心化经济。Prysm 是共识协议的一种实现，注重可用性、安全性和可靠性，它也是当前用户规模最大的以太坊客户端，目前有超过 42% 的验证节点都在使用 Prysm 验证交易。

作为专注于区块链生态安全的行业头部公司，慢雾(SlowMist) 也一直关注着以太坊的发展，这次安全审计合作，不仅是深度地参与了以太坊生态，更是与 Prysmatic Labs 在其对安全重视的前提下，共同助力了以太坊生态的安全发展。

本次审计在 2022 年 11 月 1 日 - 2022 年 11 月 21 日之间进行，慢雾(SlowMist) 采用“黑盒、灰盒为主、白盒为辅”的策略，以最接近真实攻击的方式对项目进行完整的安全测试，目标是通过发现并修复安全漏洞，并向团队提供修复与加强建议，以保护项目及用户安全。慢雾(SlowMist) 对链的安全审计过程重点包括以下两个步骤：1）使用自动化工具分析扫描/测试源代码以查找常见的编码缺陷；2）针对列举的安全问题对代码进行人工审计，手动分析代码以查找任何潜在问题。

审计我们主要关注的漏洞范围包括：

* **P2P：**

     女巫攻击

     日蚀攻击

     窃听攻击

     拒绝服务攻击

     BGP 劫持攻击

     异形攻击

     时间劫持

* **RPC：**

     窃听攻击

     拒绝服务攻击

     以太坊黑色情人节漏洞

     HTTP 恶意输入攻击

     跨域钓鱼攻击

* **共识：**

     长程攻击

     贿赂攻击

     种族攻击

     活性冻结攻击

     审查攻击

     芬尼攻击

     Vector76 攻击

     替代历史攻击

     51% 攻击

     权力压迫攻击

     币龄累积攻击

     自私挖矿攻击

     区块双产

* **加密：**

     密码学攻击

     私钥预测

     长度扩展攻击

* **交易：**

     重放攻击

     交易延展性攻击

     交易时间锁攻击

     假充值攻击

慢雾(SlowMist) 在审计过程中发现了 2 个低风险和 1 个建议漏洞。同时，慢雾审计人员提出了加强建议。在与 Prysmatic Labs 团队沟通后，问题已得到解决，并由审计人员再次审查并通过。审计报告详情可点击原文链接查看。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYBCWibmyVYOVd33sUwS0NibhIv4uc8X885BNKHU3CTeUCT5EwhiaHMPxic0KfHGTA8xQ5SickmXSXxJOA/640?wx_fmt=png)

#

# **关于****Prysmatic Labs**

#

Prysmatic Labs 是负责以太坊网络维护、升级和创新的核心软件开发团队之一，也是以太坊客户端 Prysm 的开发团队。Prysmatic Labs 致力于以太坊横向扩容，为以太坊区块链上有价值的 DApps、智能合约提供支持。

官网：https://prysmaticlabs.com/

GitHub：https://github.com/prysmaticlabs

# **关****于慢雾(SlowMist)**

慢雾(SlowMist) 作为一家行业领先的区块链安全公司，在安全审计方面深耕多年，安全审计不仅让用户安心，更是降低攻击发生的手段之一。

除此之外，慢雾的安全解决方案包括：威胁情报(BTI)、防御部署等服务并配套有加密货币反洗钱(AML)、加密货币追踪(MistTrack)、假充值漏洞扫描、漏洞监测(Vulpush)、被黑档案库(SlowMist Hacked)、智能合约防火墙(FireWall.X) 等 SaaS 型安全产品。基于成熟有效的安全服务及安全产品，慢雾联动国际顶级的安全公司，如 Akamai、BitDefender、FireEye、RC²、天际友盟、IPIP 等及海内外加密货币知名项目方、司法鉴定、公安单位等，从威胁发现到威胁防御上提供了一体化因地制宜的安全解决方案。慢雾(SlowMist) 在行业内曾独立发现并公布数多起通用高风险的区块链安全漏洞，得到业界的广泛关注与认可。给区块链生态带来安全感是慢雾努力的方向。

官网：https://www.slowmist.com/

微博：https://weibo.com/slowmist

Twitter：https://twitter.com/SlowMist\_Team

GitHub：https://github.com/slowmist/

**往期回顾**

[NFT 防钓鱼指北：如何选择一款防钓鱼插件](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497080&idx=1&sn=7d238035ebad68267044085f503976da&chksm=fdde8bffcaa902e98dd964116386ad6674e305411faf7aec99b5996601298115ad21267d0486&scene=21#wechat_redirect)

[ZKP 系列之 Circom 验证合约输入假名漏洞复现](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497028&idx=1&sn=79d9c0773c1a16a5e94d32294b7ca75c&chksm=fdde8bc3caa902d5ac89af5b6c59233bcffe37ce7cce8aa4fe8eb6aa9cd388a4065ab92a5bfa&scene=21#wechat_redirect)

[慢雾：盘点 ZKP 主流实现方案技术特点](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497003&idx=1&sn=21a449f322652cd26b739fbf87f17d78&chksm=fdde8baccaa902ba0956dfbb2f747451ed7ef543fbe33e4e062d88dbc4b5a50106266c8e8145&scene=21#wechat_redirect)

[慢雾：“揭开” 数千万美金大盗团伙 Monkey Drainer 的神秘面纱](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496989&idx=1&sn=b1129d682fb132b08aa44e380c741c66&chksm=fdde8b9acaa9028c6d506e974a2a038b28834cf26d036aab0ac1d96342a1b64dbbe0a3844212&scene=21#wechat_redirect)

[暗度陈仓 —— Orion Protocol 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496929&idx=1&sn=67eefeea3c1161bbf2ea6e1de92d5093&chksm=fdde8a66caa90370fe7b27060e3c23d11cc830c61a7c760d5fb9a9e03bee46b680e23123bc2a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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