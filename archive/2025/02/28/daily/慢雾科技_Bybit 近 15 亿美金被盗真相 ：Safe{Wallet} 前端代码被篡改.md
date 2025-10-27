---
title: Bybit 近 15 亿美金被盗真相 ：Safe{Wallet} 前端代码被篡改
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501336&idx=1&sn=2ad6eea9d1534aab1a5dea8dd06ea6a3&chksm=fddeb89fcaa9318933e8ac42c616d776ee75398cbaa81d3bb9cda3ea362fa081b3b01393847e&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-02-28
fetch_date: 2025-10-06T20:38:53.916962
---

# Bybit 近 15 亿美金被盗真相 ：Safe{Wallet} 前端代码被篡改

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEU4Ohys3vo8PLT8IaG7iaq8lueYpibSgKIyvVWw55j5T1bI7ibA6cmcSf8A/0?wx_fmt=jpeg)

# Bybit 近 15 亿美金被盗真相 ：Safe{Wallet} 前端代码被篡改

原创

慢雾安全团队

慢雾科技

作者：23pds & Thinking

编辑：Liz

**背景**

2 月 26 日晚间， Bybit 与 Safe 同时发布关于之前 Bybit 价值近 15 亿美金的加密货币被盗事件的安全调查公告。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUuuDlYQoiaJEECevhmo8YwR1IstpqGKaicWks3icKCXnk69uiaAzZdNgd3Q/640?wx_fmt=png&from=appmsg)

Safe 方面表示：

Lazarus Group 对 Bybit 发起的针对性攻击的取证分析表明，攻击者通过入侵 Safe{Wallet} 开发人员机器，从而提交了一笔伪装的恶意交易提案，并诱导 Bybit 的 Safe 钱包 Owner 签署恶意交易，实现对 Bybit Safe 钱包的攻击。

外部安全研究人员的取证分析未发现 Safe 智能合约、前端或相关服务的源代码存在任何漏洞。事件发生后，Safe{Wallet} 团队进行了彻查，并分阶段恢复了以太坊主网上的 Safe{Wallet}。Safe{Wallet} 团队已完全重建、重新配置了所有基础设施，并轮换了所有凭证，确保完全消除了攻击媒介。待调查最终结果出炉后，Safe{Wallet} 团队将发布完整的事后分析。

Safe{Wallet} 前端仍在运行，并采取了额外的安全措施。但是，用户在签署交易时需要格外小心并保持警惕。

Bybit 方面表示：

* **攻击时间：**恶意代码于 2025 年 2 月 19 日被注入到 Safe{Wallet} 的 AWS S3 存储桶中，并在 2025 年 2 月 21 日 Bybit 执行 multisig 交易时触发，导致资金被盗。
* **攻击方法：**攻击者通过篡改 Safe{Wallet} 的前端 JavaScript 文件，注入恶意代码，修改 Bybit 的 multisig 交易，将资金重定向到攻击者地址。
* **攻击目标：**恶意代码专门针对 Bybit 的 multisig 冷钱包地址及一个测试地址，仅在特定条件下激活。
* **攻击后操作：**恶意交易执行后约两分钟，攻击者从 AWS S3 存储桶中移除恶意代码，以掩盖痕迹。
* **调查结论：**攻击源自 Safe{Wallet} 的 AWS 基础设施（可能是 S3 CloudFront 账户/API Key 泄露或被入侵），Bybit 自身基础设施未被攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUL4qmkf1aAcribic9Uic1peMuOYx9uN55zkQ046OLpe7e6qNzfFVbzcsIg/640?wx_fmt=png&from=appmsg)

美国联邦调查局(FBI) 发布公告，确认朝鲜黑客组织“TraderTraitor”（亦称 Lazarus Group）是 2 月 21 日针对 Bybit 交易所发起的黑客攻击的幕后黑手，此次攻击导致价值 15 亿美元的加密资产被盗。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUU1fBloOxAGIp4UibsEzIQS56Tk4lvEicWk1s0ocHpk3Z6Jbm076QSsiaA/640?wx_fmt=png&from=appmsg)

**回顾分析**

慢雾作为外部第三方安全机构，虽然没有直接介入分析，但是我们也持续关注事情的进展。

2 月 26 日上午，慢雾安全团队内部对攻击进行复盘时，慢雾 CISO 23pds 发现自 2 月 21 日攻击发生后，Safe 开始各种修改前端等代码，于是 23pds 在 X 发布部分分析，并立即通知慢雾安全团队负责人 Thinking 关注：

https://app.safe.global/\_next/static/chunks/pages/\_app-52c9031bfa03da47.js

这个 JavaScript 代码的历史变更：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUibZ8SBmcYrrH2exZfK4Sibu2brH8G0Du5XUTwRU4SShicU0E6ejPI3U4w/640?wx_fmt=png&from=appmsg)

我们首先使用 urlscan 抓取 app.safe.global 近几个月来的变化，发现唯独 “\_app-52c9031bfa03da47.js” 这个文件发生了变更：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUUeIPV1GTc9KFzz7WA4YfjCIwP1RhxZlAfS50BiaFQLGgZXDPMozX1VA/640?wx_fmt=png&from=appmsg)

于是，我们通过 archive 分析这个文件的变更：

https://web.archive.org/web/20250219172905js\_/https://app.safe.global/\_next/static/chunks/pages/\_app-52c9031bfa03da47.js

如图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUZBqYLicQHguqBuOw4ibrWznpib0PAOIUHeEfeqHhpD15fkpzozibTIT5UA/640?wx_fmt=png&from=appmsg)

匹配到本次被黑事件攻击者使用的恶意实现合约地址：0xbdd077f651ebe7f7b3ce16fe5f2b025be2969516。

涉及的 “\_app-52c9031bfa03da47.js” JavaScript 代码分析如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUsnJ45ybuUeBX4DNiaaodlL4cCLIFbSrXIGlWPyxPvc6UgANaPAcGiccA/640?wx_fmt=png&from=appmsg)

(图片来源：ScamSniffer)

**整体攻击流程图**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZJBtUlXow7INKOj3Bw8mEUdBxVTXmwh9dhic2QZQpBWibiafWqx54miaMt1sF2uMD4B1Rybk6BwibBdsg/640?wx_fmt=png&from=appmsg)

巧合的是，我们在分析的过程中，Safe 和 Bybit 昨晚刚好发布了调查报告，最终事情有了定论，这无疑是件好事。至此，可以确认此次 Bybit 价值近 15 亿美元的加密货币被盗事件是攻击者精心策划的针对性攻击。此次事件揭示了黑客对开发环境和供应链的精准打击能力，并凸显了前端代码控制权的重要性。攻击者先获取到 app.safe.global 的前端代码的控制权，然后针对 Bybit 的 Safe{Wallet} 钱包进行精准攻击。在 Bybit 的多签 Owner 使用 app.safe.global 进行签名时，让 Safe{Wallet} 的界面展示正常地址，实则在发起交易时已将交易内容替换成恶意的待签名数据，从而欺骗 Owner 签署了经过修改后的恶意待签名数据。最终，攻击者成功接管了 Bybit 的多签钱包的合约控制权，并实施盗币。

身处区块链黑暗森林，如何更好地保护加密货币资产安全呢？除了进行安全审计，还需要采取更多防御措施来降低风险，慢雾安全团队推出的 MistEye (https://misteye.io/)，能够提供全面的 Web3 威胁情报和动态安全监控服务，如：[加密货币 APT 情报：揭秘 Lazarus Group 入侵手法](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501259&idx=1&sn=0b2183929367aa5845f0a9e1d1a42e74&scene=21#wechat_redirect)，前端代码和 DNS 变更监控，智能合约项目安全监控等。

此外，作为 Web3 项目，特别是基础设施提供方，更应确保供应链安全，更多安全建议请参考：[慢雾出品｜Web3 行业供应链安全指南](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247498025&idx=1&sn=1642e5f07a7b1c2c85c4f3da897d8b2f&scene=21#wechat_redirect)。

**往期回顾**

[慢雾解析｜Safe 困局，Guard 能否重构契约巴别塔？](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501278&idx=1&sn=78004ffc4dc09460a509369556a45ff9&scene=21#wechat_redirect)

[慢雾招聘令 | 加入我们，开启 Web3 安全之旅！](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501278&idx=2&sn=3a35e5354af1d075bf72a76dad3e9e45&scene=21#wechat_redirect)

[加密货币 APT 情报：揭秘 Lazarus Group 入侵手法](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501259&idx=1&sn=0b2183929367aa5845f0a9e1d1a42e74&scene=21#wechat_redirect)

[慢雾：Bybit 近 15 亿美元被盗背后的黑客手法与疑问](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501246&idx=1&sn=eafc7080cc28d1f8bf16c362f3ac2230&scene=21#wechat_redirect)

[顺藤摸瓜｜披露假冒慢雾员工行骗事件](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501212&idx=1&sn=996e238a420e98e240db4cddefff0343&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaa3Th7YiamUUBwq1Iiby9N9lWh3tKP2MVjM6L3UxtTnuUy6iaegsOP2IrqZYsIBM2v3XgC5O2JTbY5g/640?wx_fmt=png&from=appmsg)

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

修改于

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