---
title: 资产识别阶段最容易犯的错误
url: https://mp.weixin.qq.com/s/EL4xL2XXQE3_zKrct2QPuw
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:24:05.544090
---

# 资产识别阶段最容易犯的错误

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FT3A8r9icDylf30wia74mQqNeaozSrnWphSdjCWEJXO6kRvAnt8TECMb45PPNIbHgvgfQyEFbTKAnRg2Tu8OMbhU52z6X0XY7GKhGyqWaoLoY/0?wx_fmt=jpeg)

# 资产识别阶段最容易犯的错误

原创

我出趟远门
我出趟远门

ListSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 风险评估中，我们会识别这些东西吗？

##

## 1. 只识别系统，不识别业务

这也是我们很多人做资产识别忽略的问题，看起来资产很全，但不知道哪些最关键，后面风险分析容易失焦。

特别是在帮客户梳理资产时，通常会通过扫描器识别ip，端口，域名，目录等信息，再加上网络、安全设备，形成资产清单，而不会深入业务。

要了解业务肯定需要客户配合，也许客户也不清楚，需要找开发商，就比较耗费时间，沟通成本也比较大，一般不会去做。

虽然风险评估中会识别业务，但都很表面，只需要了解系统干什么的就可以了，如果真要梳理出系统与业务的关系，估计只有客户自己去梳理，除非客户有需求，否则基本不会识别业务信息。

## 2. 只看系统，不看数据与服务

除了业务，还应识别数据和服务，风险最终常常不是“系统挂了”，而是：数据泄露了、关键服务断了，所以数据和服务必须单独识别。

数据需要识别数据资产清单，对数据进行分类分级，涉及数据安全风险评估。

## 3. 只看内部资产，不看外部依赖

现在很多关键业务依赖：云资源、第三方接口、证书服务、运营商线路、短信平台、外包运维，这些都可能是关键资产链的一部分。

外部依赖很容易成为突破口，也是比较容易忽略的点。

## 4. 只列清单，不建关系

没有业务—资产映射关系，后面就很难：判断关键资产、做准确赋值、做风险分析。

一点拙见，班门弄斧了，主要是想记录下，也方便自己理解。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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