---
title: 限时免费调用小米 MiMo 模型，一个脚本搞定
url: https://mp.weixin.qq.com/s/MZi63rmKmo4OxZGKeCM6xw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:12.301296
---

# 限时免费调用小米 MiMo 模型，一个脚本搞定

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9laT0icEalUIgicq1DHXSd1X8buAmsUdFRxjqonJoDHZbZOyT9VtJtmRlOBlO9fZwPtBgmJxjdzqYiaXg1s3REoOGXkGdoHuSx6xSiahY49jpKU/0?wx_fmt=jpeg)

# 限时免费调用小米 MiMo 模型，一个脚本搞定

原创

薛小蛮
薛小蛮

AI安全手记

![]()

在小说阅读器中沉浸阅读

小米最近发布了 **MiMo-V2-Pro** 和 **MiMo-V2-Omni**，联合 5 个 Agent 框架搞了一周免费活动。目前截止到4月2号活动结束。

这 5 个框架：OpenCode、OpenClaw、KiloCode、Cline、BLACKBOXAI。

![Pasted image 20260328222625.png](https://mmbiz.qpic.cn/mmbiz_png/9laT0icEalUIk9maNIApA0v90RmWcQP1rjhfFShibUyr6L53ehNWRT4gUSE37Y9ichGicAvDicIOqd5I4lKg3tURVwAuqkcZ852vVLvwt2s57PFQ/640?from=appmsg)

直接在这些框架里选 `MiMo V2 Pro (FREE)` 就能用。

---

## 痛点

但如果你想**用自己的程序调用**呢？

比如你用的是 Claude Code，它发的是 Anthropic 格式请求，而 OpenCode 平台用的是 OpenAI 格式——直接调会报错。

---

## 解决方案

参考了一下大佬的思路，写了个脚本，解决了两件事情。

第一件事情是不需要通过CPA，第二个就是直接通过脚本儿来调用模型。

脚本的核心原理：

**1. 翻译格式**

* 1

```
你的工具 → 代理脚本（翻译）→ OpenCode → 小米 MiMo
```

**2. 自动重试**

免费 API 遇到限流（429）会自动重试，最多 5 次。

---

## 使用方法

### 第一步：配置代理。

在CC-switch里面设置脚本的代理端口。

![Pasted image 20260328222139.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9laT0icEalUKp4zK0W7QraJOTNKtSFmyUiasicqymiaGTwtUA9AcGuJZv2ufxhHKmSZAENutoSUuVe4UTkCR44VxPmf2ibxBGdxOooUbNYDLbuJg/640?from=appmsg)

### 第二步：启动代理

* 1

```
python opencode_gateway.py
```

启动后代理运行在 `http://127.0.0.1:18080`

![Pasted image 20260328222434.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9laT0icEalUKXQuicuGJp0gJ2125sbDDWJUpA59l1ynCvW6j76uztqzez75esAkfV5g3JtRc89JjhvUhf1iaT2yY09LyCuxkU3bJryM8sQUyTY/640?from=appmsg)

### 第三步：配置你的工具

在Cloud Code里面正常调用即可。

![Pasted image 20260328222555.png](https://mmbiz.qpic.cn/mmbiz_png/9laT0icEalUJnx4BX3dgdcyia4VhLBjJvZQI2oiawxnN8VqQpfnpUcsPg6DibTDNOfru1j9pMjiaKrA8Luqc4F61xouWweyD4UjicX3jj8H8Eef3Q/640?from=appmsg)

---

## 原理说明

技术细节

脚本将 Anthropic `/v1/messages` 请求转换为 OpenAI `/v1/chat/completions` 格式，再转发给 OpenCode Zen 平台。
解决限流的问题。

---

> 有问题留言~

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LRFSic7veEzMqVJNmcur1bB6X9yRWib4MgN6I5hxOuibaS7NI9TK9ibt9CdoXIGeeujdFG5W76AEbibO8MhqWzibRP6A/0?wx_fmt=png)

AI安全手记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LRFSic7veEzMqVJNmcur1bB6X9yRWib4MgN6I5hxOuibaS7NI9TK9ibt9CdoXIGeeujdFG5W76AEbibO8MhqWzibRP6A/0?wx_fmt=png)

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