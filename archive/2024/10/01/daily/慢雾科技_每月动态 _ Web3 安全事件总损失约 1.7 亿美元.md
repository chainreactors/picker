---
title: 每月动态 | Web3 安全事件总损失约 1.7 亿美元
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500472&idx=2&sn=cbc8fb3fc309128cb863b0539d28d5f0&chksm=fddebc3fcaa9352943aa2777205c0b4790d1f2b4d27af2e56821981d458ff073fec926fe11a9&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-10-01
fetch_date: 2025-10-06T18:53:10.980525
---

# 每月动态 | Web3 安全事件总损失约 1.7 亿美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8T1Z0CzickUXVg5Znkb7L1icdMK6EFksqHRgPMHic3KhkEFoLtw5qsDZibA/0?wx_fmt=jpeg)

# 每月动态 | Web3 安全事件总损失约 1.7 亿美元

慢雾安全团队

慢雾科技

**Q3 概览**

据慢雾安全团队统计，2024 年 Q3 季度，Web3 安全事件呈现出持续频发的趋势，安全形势依旧严峻：

* 本季度共发生 93 起被黑事件，钓鱼事件受害者超过 3.3 万人。
* 本季度安全事件造成的总损失约为 7.84 亿美元，其中有 2,754 万美元得以追回。
* 7 月的损失约达 3 亿美元，接着，8 月的损失攀升至 3.16 亿美元，其中大部分损失归因于一起涉及 2.43 亿美元的骗局。
* 9 月的损失较前两月有所下降，但安全压力仍然较大，9 月有 3 起安全事件的损失规模达千万美元，被黑事件数与 8 月持平，钓鱼事件的规模和损失依然维持在较高水平。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt833RicmzhoDsYynU5eibh7HLDtMPJibicek5bibP3Zl56RwiaDYLDehXUsN8A/640?wx_fmt=png&from=appmsg)

###

### **9 月概览**

2024 年 9 月，Web3 安全事件总损失约 1.7 亿美元。其中，据慢雾区块链被黑档案库(https://hacked.slowmist.io) 统计，共发生 28 起被黑事件，导致损失约 1.24 亿美元，有 490 万美元得到返还，事件原因涉及合约漏洞、账号被黑和私钥泄露等。此外，据 Web3 反诈骗平台 Scam Sniffer 统计，本月有 10,525 名钓鱼事件受害者，损失规模达 4,643 万美元。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8SjY1rPccwEyia5tUjIvibWNn201icduAicfNicVI7BNpJtttIoT8XkPNTog/640?wx_fmt=png&from=appmsg)

(https://dune.com/scam-sniffer/september-scam-sniffer-2024-phishing-report)

###

### **9 月安全大事件**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8ZQibJy7HOR57GribGXBsfGIBktqKOVy1aATdVtaK9IwkDG5uVFSpHBkA/640?wx_fmt=png&from=appmsg)

**BingX**

2024 年 9 月 20 日，新加坡加密货币交易所 BingX 发现其热钱包遭到攻击，慢雾安全团队及时协助 BingX 调查此事件，统计受损金额约达 4,500 万美元。在慢雾安全团队的帮助下，约 100 万美元的被盗资金已被冻结。此外，我们针对此次事件成立了群组，以监控资金转移情况。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8FVm5jrialO8ibicnXUPwxWbIOgweRarMibibZia7MOqcic8kVWiawSkKUIol4g/640?wx_fmt=png&from=appmsg)

(https://x.com/SlowMist\_Team/status/1837062650179768523)

**Penpie**

2024 年 9 月 4 日，去中心化流动性收益项目 Penpie 遭攻击，攻击者获利近 3 千万美元。据慢雾安全团队分析，此次事件的核心在于 Penpie 在注册新的 Pendle 市场时，错误地假设所有由 Pendle Finance 创建的市场都是合法的。然而，Pendle Finance 的市场创建流程是开放式的，允许任何人创建市场，并且其中的关键参数如 SY 合约地址，可以由用户自定义。利用这一点，攻击者创建了一个含有恶意 SY 合约的市场合约，并利用 Penpie 池子在获取奖励时需要对外部 SY 合约调用的机制，借助闪电贷为市场和池子添加了大量的流动性，人为放大了奖励数额，从而获利，详细分析见[偏信则暗 —— Penpie 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500255&idx=1&sn=c386d921eca160f2ae1154052dad236b&chksm=fddebf58caa9364e534c03c87fc109f527d74db1deef0836e0ad8ab87a85a6a880a0e4094e4d&scene=21#wechat_redirect)。

**Indodax**

2024 年 9 月 11 日，印尼加密交易所 Indodax 遭攻击，攻击者从热钱包中盗取了约 2,200 万美元的各种代币。慢雾安全团队分析后认为热钱包被攻破的可能性较小，更可能是由于取款系统被攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8rfWediaib7gF4AS0oamwpibtXFfr0LA5Ud9wWZ7418yYibFjzO6BO1qUuw/640?wx_fmt=png&from=appmsg)

(https://x.com/SlowMist\_Team/status/1833707952353812782)

**DeltaPrime**

2024 年 9 月 16 日，DeltaPrime DeFi 协议由于私钥泄露，损失约 600 万美元。攻击者通过获取私钥，铸造了 1.1×10⁶⁹ DPUSDC 代币，这些代币可以按 1:1 的比例兑换 USDC 稳定币。攻击者随后使用类似方法，铸造了大量的比特币、以太坊和其他加密货币的存款凭证代币。最终，攻击者从这些巨量的存款凭证中兑换了一小部分，总计约 600 万美元的资产。

**Truflation**

2024 年 9 月 26 日，据链上侦探 ZachXBT 消息，Truflation 遭攻击，损失约 500 万美元，资金从“财库多签和个人钱包”中被盗取。攻击者利用了恶意软件发起攻击。慢雾安全团队及时跟进被盗资金的转移动向，攻击者当天已将 415 ETH 转移到 0xb1cf7880351e6d16313c03a6686b4c8a5ba6372a，目前，该地址上已沉淀了 523 ETH，暂未转出。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8aTEz2k5yIJTLSM0BdeyX3bLt3UqiaibH6WPgicyJpicvkQRl0sMAFBM5Ww/640?wx_fmt=png&from=appmsg)

(https://x.com/SlowMist\_Team/status/1839154230210543732)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8SibgqjIgh2MdbxnicNL3NjNjW4fFgGNVCG3aicOObLpxV4nejibNehqpnQ/640?wx_fmt=png&from=appmsg)

###

### **特征分析及安全建议**

本月，攻击原因为合约漏洞的安全事件有 9 起，导致损失规模达到 4,100 万美元，占总被黑损失（1.24 亿美元）的 33.06%；本月账号被黑事件有 8 起，相比上月（18 起）有显著减少，涉及平台主要集中在 X 和 Discord。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8YiaEysIibNcrvYIUCK5uY03tIvVAIECjztlnHJh44IdjxHGyw36UK5jA/640?wx_fmt=png&from=appmsg)

慢雾安全团队建议项目方始终保持警惕并定期进行全面的安全审计，跟踪和解决新的安全威胁和漏洞，保护项目和资产安全；此外，建议项目方建立健全的应急计划，以便在遭受攻击时能够快速、有效地应对，减轻损失并提高资金收回的机率。广大用户也应谨防钓鱼攻击，定期检查账户权限；多方确认消息的真实性，不点击不明链接，更不轻易输入私钥/助记词；安装杀毒软件（如卡巴斯基、AVG 等）和钓鱼风险阻断插件（如 Scam Sniffer），提高设备安全性。

最后，本文收录的事件为本月主要安全事件，更多区块链安全事件可在慢雾区块链被黑档案库(https://hacked.slowmist.io/) 查看，点击阅读原文可直接跳转。

**往期回顾**

[慢雾：Uniswap v3 协议分析与审计要点](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500440&idx=1&sn=e447aeff528fb5a5c96a3d88f2d31531&chksm=fddebc1fcaa9350964866990b32e3a928e3a6b76a9c39eabe7e8755c4bb47a03a15e48da678a&scene=21#wechat_redirect)

[慢雾：Sui - Move 合约审计入门](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500411&idx=1&sn=a9bd3a971824eb5bdb342a54e6da1782&chksm=fddebcfccaa935ea03d21c459875d19309c50a4822337c62f7285e0c9136698c750ee2584eb2&scene=21#wechat_redirect)

[报告解读｜FBI 发布 2023 年加密货币欺诈报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500371&idx=1&sn=0ca64fc5fb738f708f356eb36d0a2552&chksm=fddebcd4caa935c2e13981ab968ee71d08200546d133a886313dbbacf788f5cf016b72078291&scene=21#wechat_redirect)

[慢雾：Toncoin 智能合约安全最佳实践](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500342&idx=1&sn=3c8681b941ccf3f03a308fa32558c327&chksm=fddebcb1caa935a7fa5fbefc2033f84e7a2e95be20db37fb1551459959def7fb0d9150130903&scene=21#wechat_redirect)

[慢雾出品 | Web3 项目安全手册](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500304&idx=1&sn=4907efb9509e7e555ad6c8bbc0094f65&chksm=fddebc97caa93581bad6bf8a23f9ae6ab95e80ffcaa5a687a1a416a38f5e2baa50f358910b3b&scene=21#wechat_redirect)

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