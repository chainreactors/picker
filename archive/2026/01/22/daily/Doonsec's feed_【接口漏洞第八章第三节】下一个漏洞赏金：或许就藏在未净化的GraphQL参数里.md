---
title: 【接口漏洞第八章第三节】下一个漏洞赏金：或许就藏在未净化的GraphQL参数里
url: https://mp.weixin.qq.com/s/6l0O2PL1a_VnWCHArk-BVg
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:31:16.769654
---

# 【接口漏洞第八章第三节】下一个漏洞赏金：或许就藏在未净化的GraphQL参数里

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q3FE9rW6iasicyeACLGETM2IdbSIicxF0ia41s9ITyjs1pQNO4eeKkYW2ic5QDrg7XQeAUsBh15nia6MEVg/0?wx_fmt=jpeg)

# 【接口漏洞第八章第三节】下一个漏洞赏金：或许就藏在未净化的GraphQL参数里

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

在上一节[【接口漏洞第八章第二节】挖掘GraphQL漏洞第一步：高效发现端口的三大实战技巧](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797769&idx=1&sn=00787ba60635a8768756f58f0d77b3e8&scene=21#wechat_redirect)中，我们知道如何发现GraphQL API端点了，接下来，我们就接着了解挖掘漏洞的技巧了。今天我们就重点了解下如何利用未经净化的参数来作为挖洞切入点

我们在开始寻找漏洞的时候，测试查询参数是一个很好的起点。如果 GraphQL API 直接使用参数来访问对象，则可能存在访问控制漏洞。用户只需提供与特定信息对应的参数，便可能访问本不应获得的信息。这种情况有时称为不安全的直接对象引用（IDOR）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3FE9rW6iasicyeACLGETM2IdXboF6RjwPiaLfBY2EhJsvJnVlpmUz8KibAVJRxibdFASqLibbDmyZ6qLag/640?wx_fmt=png&from=appmsg)

例如，以下查询请求在线商店的产品列表：

```
graphql# 示例产品查询query {    products {        id        name        listed    }}
```

返回的产品列表仅包含已上架的产品：

```
{    "data": {        "products": [            {                "id": 1,                "name": "Product 1",                "listed": true            },            {                "id": 2,                "name": "Product 2",                "listed": true            },            {                "id": 4,                "name": "Product 4",                "listed": true            }        ]    }}
```

根据这些信息，我们可以推断出以下内容：

* 产品被分配了连续的 ID。
* 产品 ID 3 未出现在列表中，可能是因为已下架。

我们可以通过查询缺失产品的 ID，就可以获取到这个本应该不显示的产品详细信息，即使该产品未在商店中上架且未在原始产品查询中返回：

```
graphql# 获取缺失产品的查询query {    product(id: 3) {        id        name        listed    }}# 正常查询到已下架数据{    "data": {        "product": {            "id": 3,            "name": "Product 3",            "listed": false        }    }}
```

好了，今天我们就先简单介绍下“利用未经净化的参数”的挖洞方式，更多挖洞技巧，我们后续章节继续分享，感兴趣的话，点关注。

觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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