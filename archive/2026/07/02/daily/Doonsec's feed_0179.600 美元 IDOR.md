---
title: 0179.600 美元 IDOR
url: https://mp.weixin.qq.com/s/2nifaVvAn5LnYc5DfMfWBA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:54.260728
---

# 0179.600 美元 IDOR

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89Busyx1AAm90rLLtGPviaAoc4lQeEibHqWvFjiaA6wAFNMtqs0zR5yibia3HKYSUPaicAgz92s7eZt0e7Isnu7DfZ68xicGD5ibe0YmChxO0/0?wx_fmt=jpeg)

# 0179.600 美元 IDOR

原创

Rajveer
Rajveer

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：IDOR

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89BuuLqYXR1PEmHtic0ktx5DCVnIN9UTDJQmPxhsicTJmibT9QQru5HuEks0H9NalVVJmxeoGziaO4BW0shypZZ96fSIibqJibSV8zcTb5A/640?wx_fmt=jpeg&from=appmsg)

这篇文章讲述了我如何找到一个 IDOR（身份识别服务器），它允许我下载私人内容。

为保密起见，部分细节已作修改。

和往常一样，我首先手动测试目标，了解应用程序的行为和限制。

## 发现

该应用程序允许用户发布他们的 3D 模型，并选择**公开**或**私有的**可见性。

我创建了一个**公开**可见的模型，并捕获了用于获取其详细信息的端点。

接下来，我将可见性更改为**私有**，并再次测试了相同的 API 端点。不出所料，它返回了一个错误。

此时，我开始与所有其他可能泄露模型数据的接口进行交互。测试过程中，我发现**下载**接口仍然有效。

现在我只需要模型的 UUID 就可以下载任何私有 3D 模型了。

显然，UUID 是无法猜测的。

## 查找 UUID

我浏览了应用程序的其他部分，并使用搜索栏搜索了该型号的名称。

用户界面上没有显示任何结果，所以我检查了 API 响应，然后……

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MW9pCm89Bussrr9SpWKVjbX3CjBPcN99ol0O8BVVpIUIpsKc87fV8YHX3JINGAn7QSXkknbIbicOKjg1X9xpNAib0aWuxjLeynHRv9U8t0gXQ/640?wx_fmt=gif&from=appmsg)

我找到了 UUID

现在我可以下载私有的 3D 模型了，但请求需要一个额外的参数： file\_id ，它用于跟踪对模型所做的更改。

每当模型被修改时，其 file\_id 都会改变。我首先尝试的是暴力破解 file\_id 它只有四位数，而且没有速率限制。

利用 UUID 和 file\_id ，我能够下载私有 3D 模型，这使得该漏洞影响巨大。

我通过漏洞赏金计划报告了该问题并获得了奖励。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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