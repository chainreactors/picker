---
title: Stellar 上 YieldBlox DAO 事件分析
url: https://mp.weixin.qq.com/s/FOKFiMUY4psO7O8kgVPBxQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:50.285338
---

# Stellar 上 YieldBlox DAO 事件分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyquvVVDyRoJARSVGRXXlkNOW5xCpvRiaRA8211WrO1OT1MlO7q44xF3XTYbDoHVPKXpOdcYBZddU8tNv25g4CE6yd98cGUT9HQYw/0?wx_fmt=jpeg)

# Stellar 上 YieldBlox DAO 事件分析

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyquT0xlZPgURyF523KI8RSEA7ialqW1LOcEqBPBOS5f9MYuqEp4c55JIluIOCdsyDibE8ibzWXay3dCpGAiblFpvXBGibjRV5gb1tosU/640?wx_fmt=gif&from=appmsg)

**一、 摘要**

2026 年 2 月 22 日，Stellar 上 Blend V2 的一个由 YieldBlox DAO 运营的借贷池遭到攻击，损失超过 1000 万美元。

攻击者先在 SDEX 上操纵 USTRY/USDC 市场价格。随后，该池配置的 Reflector 预言机路径接受了该操纵价格，导致 USTRY 抵押品被高估，并使攻击者得以抽离池内资产（USDC 和 XLM）。

本次事件并非 Blend V2 核心合约问题，而是池运营方（YieldBlox DAO）的配置问题。

**二、背景**

在 Stellar 链上，Blend V2 是一个支持创建隔离借贷池的流动性协议。每个池可独立配置可借资产、抵押资产和预言机来源。

本次受影响池允许用户使用 USTRY 作为抵押借出 XLM 和 USDC。该池使用 Reflector 预言机 [2]，其 USTRY 定价基于 SDEX 上 USTRY/USDC 市场 [3] 的周期性更新。

**三、漏洞分析**

漏洞成立的关键在于池侧定价设计依赖可操纵市场：

1. SDEX 上 USTRY/USDC 市场流动性很浅。
2. 攻击者可以吃掉正常挂单并挂出异常报价，快速抬高市场价格。
3. Reflector 随后更新到该异常价格。
4. 池风控将该价格用于抵押品估值，从而高估可借额度。

**四、攻击分析**

1. （Tx 1, 2）攻击者在 SDEX 上将 USTRY 从约 $1.06 拉升至约 $107。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqvDslOcCwtFxJlkSGDw5yibZ10SPsvbBbVzSRcGPC4574ZaHWUCcAs4AochibUd4EBhYiajF3AN2L8tqicHTOOWk1qU3UBDcV04SBM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtYwdlZ0gHpic2xZtqaCOBNLVrao7CBXJic0EIvS2Lz5JVaupSdVuDa4pDjTb7nh3H0rXpPUP08uHJU3XeteKBRibVG5JnUYuAlpo/640?wx_fmt=png&from=appmsg)

2. （Tx 3）Reflector 拉取并更新被操纵后的价格。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqs3WsUfGnOnhH0ibx17mtXzxDJUOFoKFKmZufW9Wwrwdeibn0PZb3AdyHc9jxI2liaHzGLRofJriaViaic3Fhy0nOxGP8Fw9W4p3gtjI/640?wx_fmt=png&from=appmsg)

3. （Tx 4, 5）攻击者以 12,881e7 USTRY 抵押，借出 1,000,196e7 USDC。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsvE8eNgicnJzmiclVtjtbh8SiagJVfsBfBC42rs9DFzWZKKLhxkHKqF1LAyhKYYqibBAwVKZsxLNvhfTNEG8NqErxbibZYClgSMAq4/640?wx_fmt=png&from=appmsg)

4. （Tx 6, 7）攻击者以 14,987,610e7 USTRY 抵押，借出 6,124,927,810e7 XLM。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqumAjLQrjXlKibTGdPTpMVHicJeQ8cbAS8yiaqichQ1udozFHMZUG9IROmPiaRlAcppbYRevbbBiay7tR7jqcicTByDXHDx0YmMqc0ECA/640?wx_fmt=png&from=appmsg)

5. （Tx 8, 9, 10）攻击者将被盗资产桥接至 Base、BSC 和 Ethereum。

**五、损失/获利分析**

Stellar 上估算损失约 $10M+。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqs3COQFOdbUAibcu9u0Cpf2RJ80YYRg89M0nnicJbHBWZCg3Ktl6PL8bJB1gJzuAloJ7y1z6bKPn6vA5NFj7enlZnLzLQu3W9Micc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtMvicibORc3vHIfBMcK5kVG2lta97rXh5GBZSevFwZe3WddUibqiapQkqarNcszic8r5NxibW5YAOP8AhrMK82Faxa4ibUF4w2BwUNzg/640?wx_fmt=png&from=appmsg)

**六、结论**

本次事件的核心问题很明确：该池抵押品估值依赖了可被操纵的价格来源。问题是 pool 使用方（YieldBlox DAO）配置问题，不是 Blend V2 核心合约问题。这也再次提醒，借贷池在选择与监控价格依赖时，必须具备更强的抗操纵能力。

**参考资料**

[1] [YieldBlox DAO](https://x.com/YieldBloxDAO)

[2] [https://reflector.network/](https://reflector.network/)

[3] [USTRY/USDC Market on the SDEX](https://www.stellarx.com/markets/USTRY:GCRYUGD5NVARGXT56XEZI5CIFCQETYHAPQQTHO2O3IQZTHDH4LATMYWC/USDC:GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN)

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth 和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 500 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rJ6BYJY1Za0W3PlFxMWuWJI7ZfbN4ywnFgYViaYnPWsVe7YgBCPbCSKA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491136&idx=1&sn=26271064f94f00073f89e2ffd95c4f6e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIje0g9kj9ic4b9GEzwpo1TCWq94NdL91n7Yt1FYkWUmPEXrkGzHKNvuQbOlu36LFXShpNOTklWvKw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)

#BlockSec

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

BlockSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

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