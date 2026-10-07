---
title: 攻击者将 ChatGPT 自定义 GPT 变成恶意软件传播诱饵
url: https://mp.weixin.qq.com/s/oa0jE5glrAcXOKbLkoRBxA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:04.422449
---

# 攻击者将 ChatGPT 自定义 GPT 变成恶意软件传播诱饵

# 攻击者将 ChatGPT 自定义 GPT 变成恶意软件传播诱饵

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个恶意 GPT 被命名为：

“Plus 5.6”

它被设计成看起来像官方 ChatGPT 产品。

据报道，一些在 Google 上搜索“ChatGPT”的受害者通过赞助搜索结果被引导至该恶意 GPT。

一旦受害者与之互动，该 GPT 就会返回一个假的“服务可用性通知”，声称主要服务可用性有限。

用户随后被引导至一个托管在 Google Sites 上的所谓备用站点。

该页面伪装成 Cloudflare 验证屏幕，并指示受害者执行 PowerShell 命令。

感染链随后部署了一个功能齐全的 RAT。

观察到的技术包括：

```
* PowerShell 执行* 恶意 MSI 交付* DLL 旁加载* 双重持久化机制* 滥用 Canon 签名的可执行文件* 在后续波次中滥用 Stardock 签名的可执行文件* 有效载荷隐藏在 WAV 文件中* 通过 NuGet 包进行后续有效载荷交付* 移除 Web 标记
```

该 RAT 提供广泛的远程功能，包括访问：

```
* 屏幕* 摄像头* 麦克风* 文件* 系统信息* 额外有效载荷执行
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXukPL4jibZQjehLU4LmNovuDAgNfYQ9rd21NAX5J52LPnZNWYtA7DwsE9f81hxYW0pJnOtCQiafhicX4wWeibcht80aFfwFUIeXOBhw/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

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