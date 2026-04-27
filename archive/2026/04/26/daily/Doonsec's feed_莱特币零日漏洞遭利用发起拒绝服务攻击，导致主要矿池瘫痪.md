---
title: 莱特币零日漏洞遭利用发起拒绝服务攻击，导致主要矿池瘫痪
url: https://mp.weixin.qq.com/s/h5VwXQTWWdix-25c5T9UkQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:03:23.465421
---

# 莱特币零日漏洞遭利用发起拒绝服务攻击，导致主要矿池瘫痪

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PqJpBDPWa8WBEC25yicL3Y4Fr0uCbNufPOpc64xDwyvEmlTSfE5eVjUhYePwZiaY2tBjL4L82VJsjA7bibJJvAuo5XrqlKSnOkR8/0?wx_fmt=jpeg)

# 莱特币零日漏洞遭利用发起拒绝服务攻击，导致主要矿池瘫痪

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

莱特币网络中的一个关键零日漏洞被积极利用，发起了拒绝服务 (DoS) 攻击，在开发者发布完整补丁之前，导致主要矿池的运营暂时中断。

安全研究人员证实，该漏洞允许威胁行为者将无效的 MWEB（MimbleWimble 扩展区块）交易注入未打补丁的节点，从而引发一系列网络中断，影响矿池稳定性，并短暂破坏链上的交易完整性。

这个零日漏洞专门针对那些尚未应用最新莱特币软件更新的挖矿节点。攻击者精心构造了一个格式错误的MWEB交易，这些未更新的节点会将其视为有效交易，这是输入验证逻辑中的一个严重缺陷。

一旦处理完毕，无效交易就使得代币可以在未经适当授权的情况下锚定到第三方去中心化交易所 (DEX) ，从而有效地绕过了标准交易控制。

MWEB 是莱特币推出的隐私扩展层，旨在实现保密交易，但在此次事件中却成为了攻击面。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OvVBRQq1vpA2uiadgTkbWcY26YSTd59V93S6oVw4SAjo4XQVPeLV5ic4ZWVaXnej4escfcib2zDH7y6CyacB6eoxic4h4HmaXGkLw/640?wx_fmt=png&from=appmsg)

由于并非所有矿池运营商都已迁移到最新节点版本，漏洞窗口持续开放足够长的时间，攻击者可以大规模利用该漏洞。

为应对此次漏洞攻击，莱特币开发团队和网络利益相关者启动了一次包含 13 个区块的重组（reorg），这是一种有意回滚的机制，将链的状态恢复到无效交易被纳入之前的状态。这有效地从规范链中清除了非法的 MWEB 交易。

至关重要的是，在此期间处理的所有合法交易仍然有效且不受影响。根据莱特币开发团队事后声明，用户和交易所预计不会因该事件遭受任何资金损失。

13 个区块的重组被认为是区块链事件响应中的一项重大但并非史无前例的措施，通常仅在链的完整性受到直接威胁时才会部署。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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