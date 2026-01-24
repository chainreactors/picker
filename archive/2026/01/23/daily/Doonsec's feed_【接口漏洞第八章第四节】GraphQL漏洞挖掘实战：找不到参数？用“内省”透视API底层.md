---
title: 【接口漏洞第八章第四节】GraphQL漏洞挖掘实战：找不到参数？用“内省”透视API底层
url: https://mp.weixin.qq.com/s/DND4mvouRPfdwAJtiQSGNg
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:26:01.244366
---

# 【接口漏洞第八章第四节】GraphQL漏洞挖掘实战：找不到参数？用“内省”透视API底层

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q3Mp9e2GARkdiahLh74hKN4iaHGdQdWAKU73dDLiaCRkqFQN4jfibl7icpwrRxCia93CBXdVlZibMiaAOTJmA/0?wx_fmt=jpeg)

# 【接口漏洞第八章第四节】GraphQL漏洞挖掘实战：找不到参数？用“内省”透视API底层

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

在上一节中[【接口漏洞第八章第三节】下一个漏洞赏金：或许就藏在未净化的GraphQL参数里](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797774&idx=1&sn=adda8ec9796e76df5b6ebf932d02873f&scene=21#wechat_redirect)我们讲到了GraphQL参数 ，这里大家可能有个疑问，如果找到了 GraphQL api 端点，但不知道参数的话，要怎么才能做进一步挖掘呢？

别担心，今天我们就一起来看看如何对 GraphQL api 进行参数信息挖掘。

要找到可用参数，测试API的下一步就是发现、整合底层模式的相关信息。

这里最佳方法就是使用内省查询。内省是GraphQL的内置功能，允许我们向服务器查询模式信息。

内省有助于理解如何与GraphQL API进行交互，它也可能泄露潜在敏感数据，例如描述字段。

如何使用内省功能？

要通过内省发现模式信息，可以通过查询 \_\_schema 字段。该字段在所有查询的根类型中都可用。

这个字段与常规查询类似，在运行内省查询时，您可以指定返回的响应字段和结构。例如，您可能希望响应仅包含可用变更操作的名称。

有点迷糊了？还是不知道怎么使用查询 \_\_schema 字段进行内省查询？，接着看下面，我们通过结合burpsuite 工具来进一步理解：

首先，我们在浏览目标应用程序，查找对 GraphQL 端点的请求。

GraphQL 服务通常使用相似的端点后缀。请关注以下路径的查询：

* /graphql
* /api
* /api/graphql
* /graphql/api
* /graphql/graphql

这些端点可能还包含版本号作为后缀，例如 /graphql/v1，通过以上请求，找到graphql api 端点【在[【接口漏洞第八章第二节】挖掘GraphQL漏洞第一步：高效发现端口的三大实战技巧](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797769&idx=1&sn=00787ba60635a8768756f58f0d77b3e8&scene=21#wechat_redirect)有提到过如何找到该端点】后，在burpsuite的历史请求接口中，右键单击 GraphQL api 端点的请求，然后选择发送到 Repeater。

在 Repeater 中，右键单击消息编辑器的 Request（请求） 面板中的任意位置，然后选择 GraphQL > 设置内省查询，将内省查询插入请求体中。

点击 Send（发送）。

如果启用了内省，服务器应在响应中返回 GraphQL API 的完整模式，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3Mp9e2GARkdiahLh74hKN4ia6picQMCqEZ94CMNp33vicFo77LmqQaVric6uiczP0LbhXibYlYOtR30ZWVg/640?wx_fmt=png&from=appmsg)

成功的内省查询会返回 API 底层模式的详细信息，这些信息对用户和攻击者都有帮助【这里面可能就包含了我们一开始时想要找到的参数】。

以上介绍的内省查询适用于大多数 GraphQL 服务器。但如果使用的是较旧的 GraphQL 服务器，可能会失败。若出现这种情况，我们就在消息编辑器的 Request（请求） 面板中右键单击任意位置，然后选择 GraphQL > 设置传统内省查询，并重试，具体如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3Mp9e2GARkdiahLh74hKN4ia1J3Sicibf7Biaq6PxhDG4Rias1PvBTvqKOvNIw94Ndh8WMd8utUY547bxA/640?wx_fmt=png&from=appmsg)

在消息编辑器的 Response（响应） 面板中右键单击任意位置，然后选择 GraphQL > 保存 GraphQL 查询至站点地图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3Mp9e2GARkdiahLh74hKN4iaLxEgXVFJFia3QiaUQAXSUhkAVcHNOPSvPibzQK3xH0s42uGos1NX2Zfdw/640?wx_fmt=png&from=appmsg)

burpsuite在内省过程中发现的每个可用查询都将作为节点保存到站点地图中，我们就可以检查这些数据了。

通过以上操作后，我们就能掌握 GraphQL API 的大部分参数及内部信息了。今天我们就先分享到这里，关于如何利用通过以上方式获取到的信息，我们在后续章节会持续深入分享，感兴趣的可以点点关注。

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