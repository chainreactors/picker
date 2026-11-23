---
title: 网址没变，页面怎么成了钓鱼网站？Across Protocol事件里的签名陷阱
url: https://mp.weixin.qq.com/s/tMKNkDZeTXuvuPejBvpSiQ
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:30.261860
---

# 网址没变，页面怎么成了钓鱼网站？Across Protocol事件里的签名陷阱

# 网址没变，页面怎么成了钓鱼网站？Across Protocol事件里的签名陷阱

原创

ChainSecLabs
ChainSecLabs

ChainSecLabs

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

区块链安全相关的内容

我们将在这里分享一些

*Hi，这里是ChainSecLabs!*

**#关键词：**

***域名劫持、社会工程、签名钓鱼、代币授权***

**#官方披露的域名被接管时间：**

***北京时间2026年11月11日约02:45***

**#损失金额****：**

***据Bitquery数据估计，约40.2万美元。***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsKBZXpSbzq3E9bQia2DnVib17WPDtkicib1jVGU58s0NlBCicXhU33EtnYibBybQU5ZEUVntPSeK9eFMPibSC0V7sCNJn8LicBUaWYom0Y/640?wx_fmt=png&from=appmsg)

背景介绍

Across Protocol是一个跨链协议，用户可以通过网页发起跨链操作。一次典型操作涉及三个环节：浏览器打开网页，网页向钱包发出操作请求，钱包展示待确认的信息。用户看到的是一套连续的界面，背后却涉及域名、网站前端、钱包和链上合约。域名决定用户会访问到哪个页面，网页可以构造钱包请求，用户则需要判断该请求是否符合自己的操作意图。

据Across团队通报，北京时间11月11日约02:45，攻击者通过针对域名注册商Namecheap的社会工程取得了官方域名的控制权。用户即使沿用过去的书签或者手动输入原来的网址，也可能被引向攻击者控制的页面。由此产生了本次事件最值得分析的问题：一个运行在链下的网页，怎样通过钱包签名影响链上的资产？

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsLuhWeoeksBbzoGxgYibzLaAtFEzqEFic35K4rPQt1dwsFuezrmWcs0LtEQGyngV6htiauhia71zp10IoRkI3osZ37ibL8vIjAa83icE/640?wx_fmt=png&from=appmsg)

攻击地址及交易信息

Bitquery在此次域名劫持事件的调查中，追踪到同一个以太坊钱包连续四笔转出aWETH。下表选取第一笔交易，展示代币转出地址、两个收款地址及各自收到的金额。该笔交易发生于北京时间2026年11月11日04:09:23。Etherscan将该代币显示为aEthWETH，下文简称aWETH。

首笔aWETH转移交易明细：

|  |  |
| --- | --- |
| 项目 | 链上信息 |
| 代币转出地址 | `0x42e7…483c` |
| 收款地址一 | `0x2846e69d3298e99eddf2fd8116e952844da11fde`，收到约115.23aWETH |
| 收款地址二 | `0x0c7c656126aa62625fdd8051eb69dc14aee8d37b`，收到约28.81aWETH |
| 首笔交易流出合计 | 约144.04aWETH |

四笔aWETH转移明细（图中时间为UTC时间）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsJzCB3Jchajf8QxczgB0Yvq0SHpHdDMTKvP8yyHEKl8V5pe7WmrUqmtqibHWktZIFWLAF4AsibqpndN8yVUWMflJIuvmA383y66E/640?wx_fmt=png&from=appmsg)

图源：ChainBounty社区调查

首笔交易中，两个收款地址分别收到该笔流出额的约80%和20%。后续三笔交易使用了相同的转出地址和收款地址，分配比例也一致，四笔累计流出约148.60aWETH。Bitquery观察到，收到约20%的地址在事件发生前已有类似的收款记录，据此推测该地址可能用于收取盗币工具的分成。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsJibeqdJ0gPicAfCHhib2B0RH0xG6icDZgwDTt0nlDPF7gxGhYiccLFsAfzPuibX1INiazAvULWd4JLbxfn8mFH7Eic8sroXZJ0TFc5ib9A/640?wx_fmt=png&from=appmsg)

攻击过程

下图以受影响的以太坊钱包0x42e7…483c为例，展示从域名劫持、诱导签名到aWETH被转走的攻击链路。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibicDQQkq5lsIiaVaXzMaBzfOKdE08U68gEUtL9TDY9QjYPnDP4uPa2o4lb1GK2gssiaZ5jM8dVSZxJuJabQNQDIKx3NwdtITiasJasllqRaaZN4/640?wx_fmt=jpeg)

第一步，接管官方域名。据Across团队通报，攻击者通过针对域名注册商Namecheap的社会工程取得了官方域名的控制权，并将访问者引向钓鱼页面。用户即使从原来的书签进入，页面也可能已由攻击者控制。

第二步，诱导用户签署代币授权。Bitquery的调查将其中一组aWETH转账与钓鱼页面收集的permit签名联系起来。permit是一种签名授权。用户签名时，代币余额可以保持原样。拿到签名的一方随后可以将其提交上链，由代币合约验证签名并登记支出额度。

第三步，使用授权转移代币。首笔交易中，同一钱包的aWETH被分别转入两个地址，随后又发生了三笔流向相同的转移。链上记录可以核对授权和代币流向。Bitquery结合交易发生的时间和收款地址，把这些转移与域名劫持事件关联起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsLaCAtcWg2XxEWSMYqtUw3UbGmUOerzgsV6mqh7eiagBGZCwZs7S3gFtsmsMOk31swusLn084ia066qymeF5qpL6CP41BVO45aT4/640?wx_fmt=png&from=appmsg)

漏洞分析

为什么同一个域名能指向不同的服务器

浏览器通过域名解析确定要连接的服务器。攻击者取得域名的控制权后，可以修改解析配置，把访问者引向自己控制的站点。此时，地址栏仍显示原来的域名，页面内容却已经可以由攻击者控制。当用户连接钱包后，这个仿冒页面就可以向钱包发起代币授权请求。

为什么签名时余额没变，代币之后却能被转走

permit允许代币持有人签署一条消息，指定哪个地址可以代为支出代币，以及最多可以支出多少。用户签名时，代币余额可以保持原样。拿到有效签名的一方可以随后将它提交上链，代币合约验证签名、提交期限等条件后，登记相应的支出额度。被授权地址可以在额度内调用transferFrom，将代币转给指定的收款地址。

首笔交易中，aWETH合约发出的第265条日志记录了一次Approval授权事件。owner为0x42e7…483c，与前文表格中的代币转出地址一致。spender是获得支出权限的地址。授权额度value为uint256的最大值，通常称为无限额度授权。

```
spender为0x46A2a474D4c22bF1Ae4f8Fa55da7a58673472BE2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsKmovmJY7lUpC74qUPaTNfiaNLabzg6ppSPeshzzPw3ExWhCpXuic7r8ia0HzjlEOzlm31DIUAg6nmYOqOv7aCMxf4Duibkocia4Qhs/640?wx_fmt=png&from=appmsg)

以0x42e7…483c为转出方的两条aWETH Transfer日志，共记录约144.04aWETH的转移。对照两类日志，Approval中的spender表明谁获得了支出权限，Transfer中的to表明代币实际转给了谁。正确网址或书签也可能打开钓鱼页面。

为什么跨链页面还会影响Aave存款

aWETH是用户向Aave存入WETH后获得的凭证代币，可以转让，也支持permit。如果钓鱼页面请求的是aWETH的支出授权，用户签下有效授权后，被授权的一方就能转移这份代表存款权益的凭证。这解释了为什么访问一个跨链页面，也可能让钱包中来自其他协议的资产面临风险。本案中，Bitquery根据交易时间和收款地址等线索，将这组aWETH转移与Across域名劫持事件关联起来。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsJBfpJT3M1NEN7PAAA6fdUpFSBTHWZB1wczUYrYk4seRPuuEkAtFVia1u2ojAmHTObwiciaMDE16rAegBQoWoToncg3MIWFTibxvrA/640?wx_fmt=png&from=appmsg)

安全建议

用户签名前核对代币、授权对象与额度

即使浏览器地址栏显示的是熟悉的网址，也应核对钱包里的签名请求是否符合当前操作。遇到permit请求时，重点看涉及的代币、被授权地址spender、授权额度value和签名提交截止时间deadline。例如，原本只打算跨链转移一笔 USDC，钱包却要求向陌生地址授予aWETH的无限额度，此时应拒绝签名，并通过项目的其他官方渠道核实。

如果怀疑已经误签，应停止与可疑页面交互，通过可信渠道检查链上记录，并尽快撤销已生效的可疑授权。对于尚未上链的permit签名，还应检查它是否仍在有效期内，以及代币合约支持哪些失效方式。即使当前的链上授权额度已清零，仍需核查此前签署的消息是否还能被提交。

项目方加强域名保护与异常响应

项目方可以为域名注册账户启用多因素认证，限制能够修改域名配置的人员，并对域名解析记录及名称服务器的变更设置告警。如果注册服务支持锁定关键变更，可为核心域名启用相应保护。

发现域名异常后，应及时联系注册商，并通过独立于受影响域名的官方渠道发布警报。公告应写明受影响的时间范围，并在确认后公布相关的可疑合约或授权地址，帮助用户核对自己在这段时间内的签名及链上授权。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsKvbw1Q7U3Cc7ErNXzjicjO8TAsC7edqAILcVrtTm9Xm4QwREggBYJevt67oJGia3z2GFCIicbYYKS0cVC17pI0y9GrcWa80fHZS8/640?wx_fmt=png&from=appmsg)

参考链接

1. Across Protocol官方事件通报

https://x.com/AcrossProtocol/status/2120278803318489362

2. Bitquery对Across域名劫持的链上调查

https://bitquery.io/investigations/across-protocol-domain-hijack

3. Etherscan首笔aWETH转移交易及事件日志

https://etherscan.io/tx/0x2610f11fd3cde7113f83e7137853972ba98d8360b3d91eed6d5807f947a8bd38#eventlog

4. Chainbounty四笔aWETH交易明细及图表来源

https://community.chainbounty.io/posts/01a1cd16-cb81-7509-9dcf-40bfe03a1afb

5. ERC-2612签名授权标准

https://eips.ethereum.org/EIPS/eip-2612

6. Aave V3代币化合约文档

https://aave.com/docs/aave-v3/smart-contracts/tokenization#permit

7. ICANN域名保护指南

https://www.icann.org/en/blogs/details/practical-steps-for-protecting-domain-names-6-9-2013-en

作者：Elowen

编辑：Legend

审核：Zejie

---

***往期推荐***

ChainSecLabs

**01**

**[你在用的"去中心化"，到底是什么](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485285&idx=1&sn=842231d673b87a9e34e6528e56c3b3cc&scene=21#wechat_redirect)**

**02**

**[TrapDoor 事件深度解析：当黑客开始给你的 AI 编程助手"下毒"](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485220&idx=1&sn=4b634d0742cb69aa15c978f949aa2748&scene=21#wechat_redirect)**

**03**

**[账户抽象方案：ERC-4337 与 EIP-7702](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485194&idx=1&sn=a1637ede0d6dd58f90ace60acca8f587&scene=21#wechat_redirect)**

**04**

**[百亿TVL狂欢背后，藏着怎样的套娃代价？](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485167&idx=1&sn=1a63bf0aa6b043df68a61606c40c7f8c&scene=21#wechat_redirect)**

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlJuicHobAgAkYmYg8k9LKNWSibARYtAfX4VX0d6Q0HvQyKjdGKnkBRHYD9WGpQbtfD4W2ldGxKRBeBP2iaNFTFFg/640?wx_fmt=jpeg&from=appmsg)

**ChainSecLabs**

搜索公众号

关注我们

**免责声明**

本文章旨在分享安全技术相关知识与经验，内容仅供学习与研究参考。文中所提及的技术手段、工具或操作流程，均基于公开资料与作者个人理解，不代表任何官方立场，也不构成对读者的具体操作建议。

请勿将本文所述技术用于任何非法用途，否则后果自负。作者严禁并坚决反对一切网络攻击、非法入侵、数据窃取等违法行为，且不承担因读者不当使用文章内容而引发的任何直接或间接责任。

若文章中引用了第三方工具或资料，版权归原作者所有，若有侵权或不妥之处，请及时联系，我们将第一时间予以处理。

网络安全关乎法律与伦理，请读者在合法合规的前提下，自主学习、合理应用。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hlJuicHobAgDplSpg2SBicqBEmlAlkxzR1vgnpCD7JMrKzoohqQrwYTgPu4oFYhVLwibVPOPjSjOpeX1E0BNibN3hg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过