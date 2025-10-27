---
title: 瞒天过海 —— BonqDAO 被黑分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496912&idx=1&sn=51626c406874ef0c3367bf1fbd55f75a&chksm=fdde8a57caa9034158cd1fcb92dc9ffcfc08371da28f1a0d647c9b9c980d658aa92dafd599c5&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-02-03
fetch_date: 2025-10-04T05:35:15.010979
---

# 瞒天过海 —— BonqDAO 被黑分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8TogvO6lUIMCb9gU2WKN1oIvrU61onzm3dlpKjtJLsryMWJutHicCdia96yWA/0?wx_fmt=jpeg)

# 瞒天过海 —— BonqDAO 被黑分析

原创

慢雾安全团队

慢雾科技

By: 九九

据慢雾安全团队情报，2023 年 2 月 2 日，Polygon 链上的 BonqDAO 项目遭到攻击，攻击者获利 1.13 亿枚 WALBT 和 9865 万枚 BEUR 代币。慢雾安全团队第一时间介入分析，并将结果分享如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togvx1uRw47AdHAKELm9HfI6eEKjhfDaSuicvwIrmuxLLruhky1ibkoBhq2Q/640?wx_fmt=png)

##

## **相关信息**

BonqDAO 是一个非托管、去中心化的借贷平台，用户可以为协议提供流动性或超额抵押借贷赚取收益。

以下是本次攻击涉及的相关地址：

攻击者 EOA 地址：

https://polygonscan.com/address/0xcAcf2D28B2A5309e099f0C6e8C60Ec3dDf656642

攻击合约地址：

https://polygonscan.com/address/0xED596991ac5F1Aa1858Da66c67f7CFA76e54B5f1

https://polygonscan.com/address/0xb5c0bA8ED0F4Fb9a31Fccf84B9fB3Da639a1eDe5

攻击交易：

https://polygonscan.com/tx/0xa02d0c3d16d6ee0e0b6a42c3cc91997c2b40c87d777136dedebe8ee0f47f32b1

https://polygonscan.com/tx/0x31957ecc43774d19f54d9968e95c69c882468b46860f921668f2c55fadd51b19

被攻击的预言机合约地址：

https://polygonscan.com/address/0x8f55D884CAD66B79e1a131f6bCB0e66f4fD84d5B

## **攻击核心点**

BonqDAO 平台采用的预言机来源是 TellorFlex 自喂价与 Chainlink 价格的比值，TellorFlex 价格更新的一个主要限制是需要价格报告者先抵押 10 个 TRB 代币才可以进行价格提交更新。而在 TellorFlex 中可以通过 updateStakeAmount 函数根据抵押物的价格进行周期性的更新价格报告者所需抵押的 TRB 数量。但由于 updateStakeAmount 函数一直没有被调用过，导致攻击者可以用极低的成本恶意修改代币价格。

## **具体细节分析**

1、攻击者首先抵押了 10 个 TRB 后成为了价格报告者，之后通过调用 submitValue 函数修改预言机中 WALBT 代币的价格。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8TogvB7xCxGdeA8kVOVRfVNKOWA2zGXs3mgl7YKttlDLtBsw3gbyACcISVQ/640?wx_fmt=png)

2、攻击者对价格进行修改后调用了 Bonq 合约的 createTrove 函数为攻击合约创建了 trove (0x4248FD)，该 trove 合约的功能主要是记录用户抵押物状态、负债状态、从市场上借款、清算等。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togvyf5q4PsmicmDiapWKtnXmtcgZ4iajAjAgnJgKL8uibEbicST8eNXkYF2nrg/640?wx_fmt=png)

3、紧跟着攻击者在协议里进行抵押操作，接着调用 borrow 函数进行借款，由于 WALBT 代币的价格被修改而拉高，导致协议给攻击者铸造了大量 BEUR 代币。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8TogvwC0riayBtdMl22sus21iadlLFjB1TONg6xPXXzq5fOMRuSbXt9tsN4kQ/640?wx_fmt=png)

4、在另一笔攻击交易中，攻击者上述同样的手法修改了 WALBT 的价格，然后清算了市场上其他存在负债的用户以此获得大量的 WALBT 代币。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togvfc47JibxwEfVh7WPrE3LvKkvJQTyicR0PIWUicCxCDia7jlVCA1fMxiaRibg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8TogvnOXEHxrvrdbib5A2Q52QC46d4xcANhUDHWLWg7Xbicmjeme3knx8UXDw/640?wx_fmt=png)

5、根据慢雾 MistTrack 分析，1.13 亿 WALBT 已在 Polygon 链 burn 并从 ETH 链提款 ALBT，后部分 ALBT 通过 0x 兑换为 ETH；部分 BEUR 已被攻击者通过 Uniswap 兑换为 USDC 后通过 Multichain 跨链到 ETH 链并兑换为 DAI。截止目前，黑客在 ETH 上的地址仍有近 565 万美元的资产，包含 ALBT、ETH、DAI 币种。MistTrack 将持续监控黑客异动并跟进拉黑。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togvl8yNXoQIA22dqSrNUbEV2qZIMK6fB31zYESOMnpBhQicQyvQP6wl4bw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8TogvQfaNcPnib3UTJrmlpzfcdCC4NRHbIyJHcaynAjwV8ib8nNlicRRyRezxg/640?wx_fmt=png)

**总结**

本次攻击事件是由于修改预言机报价所需抵押物的成本远低于攻击获得利润造成攻击者恶意提交错误的价格操控市场并清算其他用户。慢雾安全团队建议协议在采用喂价来源时应对预言机的各种功能机制做好考察和研究，考虑与项目的兼容性与安全性。

值得一提的是，Liquity 在几个月前也收到了相同漏洞的反馈，Liquity 将 Tellor 作为后备预言机来使用，当主预言机（Chainlink）发生故障或冻结，Liquity 才会切换到后备预言机 Tellor 的价格数据作喂价。具体可参考以下链接：

https://www.liquity.org/blog/tellor-issue-and-fix。

**往期回顾**

[喜迎五周年 | 慢而有为，雾释冰融（文末有惊喜）](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496889&idx=1&sn=82e7a4703406a90cc51205c1f47a2eee&chksm=fdde8a3ecaa90328101608c67378fc1267915fbeb732fc1efe4a6c143e0c640b77eac6dd4f93&scene=21#wechat_redirect)

[引介｜EVM 深入探讨 Part 4](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496856&idx=1&sn=cb805902a8b54d49a8f5771072385813&chksm=fdde8a1fcaa903093e7b8cf6dd6ee58b91e3fae03615a52c66feb11b5d246888b5714b78ed76&scene=21#wechat_redirect)

[慢雾出品 | 2022 区块链安全及反洗钱分析年度回顾](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496854&idx=1&sn=20106c4b003793a087682a51bb963ef4&chksm=fdde8a11caa903076979966f2bf4fd82f03fb2088b2f8d3894afb72a67147fb3bb3881aeef75&scene=21#wechat_redirect)

[智能合约安全审计入门篇 —— 移花接木](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496825&idx=1&sn=a6154c7c7aaa2502839f51c85f4efc34&chksm=fdde8afecaa903e8875c586cf1f49e7bef350ee4cb490306fe5ad6b59cf13e61a2d7622d3935&scene=21#wechat_redirect)

[慢雾：朝鲜 APT 组织对 NFT 用户大规模钓鱼分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496811&idx=1&sn=d8b7abf891ebd1b8ceec7b8a105ccb2d&chksm=fdde8aeccaa903fa0749587788e932abbc63a5150f6fe6e802e882fc6b4edff4ae8dfbe19ee7&scene=21#wechat_redirect)

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