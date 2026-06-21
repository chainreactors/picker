---
title: Anthropic 接口 与 OpenAI 接口有何差异
url: https://mp.weixin.qq.com/s/4D9-2PnraussGKZ58iaQpQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:35.050904
---

# Anthropic 接口 与 OpenAI 接口有何差异

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LjdkpgSF7PcXssbRefF9JIMiasicHK3kM86uWrwd38Zd2xglENzPUcF4njhC7PzibK9HcPicLlm5A73vickl2cq37vYcic89V9EKLtdOTsGHP1zgk/0?wx_fmt=jpeg)

# Anthropic 接口 与 OpenAI 接口有何差异

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

早期 OpenAI 接口是业界标准，后来 Claude Code 爆火，Anthropic 接口也后来居上成为新的二王争霸选手。

比如 DeepSeek 的接口：

|  |  |
| --- | --- |
| base\_url (OpenAI) | `https://api.deepseek.com` |
| base\_url (Anthropic) | `https://api.deepseek.com/anthropic` |

火山方舟的 Coding Plan 接口：

BaseURL：https://ark.cn-beijing.volces.com/api/coding/v3（兼容OpenAI 协议） 或 https://ark.cn-beijing.volces.com/api/coding（兼容 Anthropic 接口协议）

主流 API 提供方都支持这两种接口，体现在接口路径上，它们存在以下不同：

```
# OpenAIPOST https://api.openai.com/v1/chat/completions# AnthropicPOST https://api.anthropic.com/v1/messages
```

除了端点路径不同，在 system 消息位置上也有差异：

```
# OpenAI — system 放在 messages 数组里{  "model": "glm-5.2",  "messages": [    {"role": "system", "content": "你是助手"},  # ← 在数组内    {"role": "user", "content": "你好"}  ]}# Anthropic — system 是顶层字段{  "model": "glm-5.2",  "system": "你是助手",                       # ← 顶层  "messages": [    {"role": "user", "content": "你好"}  ]}
```

在认证上也不一样，一般有以下两种。

Bearer Token（Authorization 头）

```
-H "Authorization: Bearer sk-xxx"
```

x-api-key（自定义头）

```
-H "x-api-key: sk-ant-xxx"
```

Anthropic 一般用的是后一种。Bearer Token 是 HTTP 标准， x-api-key 是自定义头，两者传的内容一样，只是"包装"不同。x- 前缀表示这是自定义头（RFC 6648 之前 x- 约定表示实验性/私有），不是 HTTP 标准定义的。格式上它里面是直接放密钥值，没有 Bearer 这种 scheme 前缀。

Bearer 是一种认证方案（scheme），表示"持有此 token 的人即拥有权限"。

总之 Anthropic 接口 与 OpenAI 接口是两种完全不同的接口标准，Anthropic 接口之所以能够流行就是因为 Claude Code 的王者地位，以及Anthropic 提供的 Opus、Sonnet、Haiku、Fable 等模型。

AI 行业还是实力说了算，谁强谁就是事实上的标准。

全文完。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

生有可恋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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