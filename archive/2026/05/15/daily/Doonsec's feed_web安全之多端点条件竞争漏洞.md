---
title: web安全之多端点条件竞争漏洞
url: https://mp.weixin.qq.com/s/eAG0u5SFs6Bon_wt0OL_BA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:14:03.554184
---

# web安全之多端点条件竞争漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Jql0Y1qckZQCPwmEM6icmc6icLzMMaN2glopDzT5jHsj6ZmRry53za4HGicVe2iaxKt8GS6ErudV1e3Sy4vaPrYtnHtYB4OrsZ9gbUnsQDibTN3M/0?wx_fmt=jpeg)

# web安全之多端点条件竞争漏洞

原创

流岁金沙
流岁金沙

迷雾光航

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

web安全之多端点条件竞争漏洞

简介

* 多端点条件竞争（Multi-Endpoint Race Condition）是条件竞争的一种更复杂、更隐蔽的形态。

* 普通条件竞争：单一请求入口，多个并发请求操作同一接口

多端点条件竞争：攻击者操作的是多个不同的API端点，这些端点之间存在业务逻辑依赖，通过精心设计的并发请求组合，实现绕过原本独立的业务限制

常见情况分析

低价买高价的物品

在部分电商系统中，如果后端对“购物车写入”和“订单支付”之间的状态校验处理不严谨，就可能出现一种典型的条件竞争（Race Condition）问题。 攻击者可以利用请求执行顺序的不一致，在支付阶段“偷渡”高价商品，从而以低价完成购买

正常情况下，一个完整的购买流程通常如下：

```
添加商品到购物车
↓
后端写入数据库
↓
提交订单
↓
校验订单金额/商品合法性
↓
支付订单
↓
清空购物车
```

但如果后端采用了：

* “先确认订单”

* “再执行支付”

* “最后清空购物车”

这样的逻辑，并且缺乏事务锁或状态隔离，就可能产生竞争窗口。

漏洞利用思路

攻击者首先：

1. 向购物车中添加一个低价商品
2. 在结算瞬间，并行发送两个请求：

* 一个是添加高价商品

* 一个是提交订单/支付

由于并发执行，请求的实际执行顺序可能变成：

```
[线程 A] 开始支付订单
↓
[线程 A] 校验订单金额（此时购物车仍是低价商品）
↓
[线程 B] 写入高价商品到购物车
↓
[线程 A] 继续执行支付逻辑
↓
订单中已包含高价商品
↓
完成支付
```

案例复现

https://portswigger.net/web-security/race-conditions/lab-race-conditions-multi-endpoint

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZSRwibysDdRsOp3icgWiaXekVJ9veicdS23uDXOMHQ2rLewLdKBe9TJNibTMfaHL262ib28ic9ygkONlNVib3MD4mLqcLOmGXpSd3aqlpE/640?wx_fmt=png)

首先添加10美元的礼品卡到购物车，然后支付订单，查看这个流程的数据包和响应时间

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZTick0zVlyaMibXHeozSbRST92Kseq97yiboHpGMnd41icjlZonuqrWXwFZLJyEpz8STWS0jtMVTibouN17bW1R6C4cHrwHicqlIicUlQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZRrFNRMwN82a5EDUC0BnER4ficFtiakDIFzicjMjQdPkfjLEUAVEc0zxTrFyfau1Lx0qdO1mzRpWecfBQMjedYeJurIs4Gn37y07E/640?wx_fmt=png)

支付的响应时间明显比添加商品的响应时间要久一点，说明很可能会出现竞争窗口

重新添加10美元的礼品卡到购物车，然后并发发包添加第一个1337美元的商品和购买的数据包

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZS75IB0PRdg1jxfEQYhQqSRWf7EG0msNKRudrrLWdx1IpIHbuVQ0SoyXxLgicZMtTLIhafSQJmx0AIBqqDvSia2K7pUJZ7FGKicZA/640?wx_fmt=png)

成功购买1337的商品，并且余额变成了负数

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZTZGdYh2TicPKgv9ibYwsBeFuPfpyrEYla2RP0gRksZq2o7Oc3OYBoG0dK2z9DFWzwkls5KPkXOAYlvfnybBx1SxNtnGafvAtboM/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jJ8gG6mVnEFIJS8ZaAC70ibttTmGyY8Ued3BNFEbaVWibAhibYJCfGziaYzHLZiaS0IbmbXX9UXAl3WwuZ6Oxb9AUyw/0?wx_fmt=png)

迷雾光航

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jJ8gG6mVnEFIJS8ZaAC70ibttTmGyY8Ued3BNFEbaVWibAhibYJCfGziaYzHLZiaS0IbmbXX9UXAl3WwuZ6Oxb9AUyw/0?wx_fmt=png)

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