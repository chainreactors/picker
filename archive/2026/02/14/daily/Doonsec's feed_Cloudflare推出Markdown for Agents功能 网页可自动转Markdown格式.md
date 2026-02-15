---
title: Cloudflare推出Markdown for Agents功能 网页可自动转Markdown格式
url: https://mp.weixin.qq.com/s/S3ZapBrID9D8cWKIcT73hw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:25:19.301178
---

# Cloudflare推出Markdown for Agents功能 网页可自动转Markdown格式

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFticsonpo0eKfaBtZKKcxVLPphzSRX4yq0J1VSXeXKLHq6Q4ic2VibdkZLItc3DFOr29NJoyibwrY9ViaNQuPTr236zvribpMiapI7UlD0/0?wx_fmt=jpeg)

# Cloudflare推出Markdown for Agents功能 网页可自动转Markdown格式

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt9Nj6zjiayHbybRvbaXud4T5BcMFziaX900BCN3m0larJKj7V7scS7t0TJyDceuDus6ptehsCh3Jrz5SsIEQ1BibTbvtFaWwHicmas/640?wx_fmt=png&from=appmsg)导语：** Cloudflare近日宣布推出“Markdown for Agents”服务，允许大模型爬虫和AI Agent通过简单的HTTP请求头，直接获取网站的Markdown格式内容。随着互联网内容分发从“面向人类”转向“面向AI”，这一功能的上线标志着AI的成本和门槛将进一步大幅降低。

---

## 苦HTML久矣：大模型的“Token燃烧陷阱”

在构建RAG系统或AI Agent时，获取互联网公开数据是必不可少的环节。然而，现代Web网页是为人类的视觉和浏览器渲染设计的，其中充斥着大量对AI毫无语义价值的代码。

把未经处理的HTML直接“喂”给大模型，无异于把买椟还珠的“椟”也按克数算了钱。举个最直观的例子：一个简单的网页二级标题“关于我们”，在Markdown中（`## 关于我们`）只需消耗约3个Token；但在HTML中（`<h2 class="section-title" id="about">关于我们</h2>`），哪怕不计算外层的`<div>`、导航栏和脚本标签，也会轻易烧掉12到15个Token。

**根据Cloudflare官方公布的实测数据，一篇原本包含16,180个Token的HTML博客文章，在转换为Markdown后仅需3,150个Token。这意味着**高达80%的Token用量缩减。

Markdown格式凭借其清晰的结构化特征，已经成为大模型系统无可争议的“通用语言”。通过直接投喂Markdown，大模型不仅能大幅降低计算成本，更能获得更精准的上下文理解结果。

一些知名网站已经开始支持Markdown格式。例如Android的开发者文档，现在就有View AS Markdown的选项，点击后就会打开一个markdown格式的新页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt9l2xictzdOYT0AMmiamco1Qo3YuQ5iaTWDuDxQHbsiaqOtSCN0133ULu6CYialGUQUKiatKAMADzLlNK0bNZCkLXVzbMuiafCn0B4f44/640?wx_fmt=png&from=appmsg)

## 自动将HTML转换Markdown

Cloudflare此次推出的功能，将“网页转换 Markdown”这一高频动作前置到了边缘节点。对于AI而言，接入方式非常简单：**不需要引入复杂的DOM解析库或第三方清洗API，只需在发起HTTP请求时，利用标准的内容协商（Content Negotiation）机制即可。**

**![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFtic5p9y8Yc1DwTKyWbibTEDDthf4dIZL0HUd45gqickQn18X1SibV4FZfoVfMqv6tsDn3yrLBGWEWwUYqWrZHYLXCWq56kanZpDibVw/640?wx_fmt=png&from=appmsg)**

AI Agent仅需在请求头中添加一行声明：

`Accept: text/markdown`

当Cloudflare检测到带有该请求头的访问时（前提是目标站点开启了 Markdown for Agents），便会在自动拉取源站HTML，转换为Markdown并返回给AI。目前，包括Claude Code和OpenCode在内的主流Agent，已经开始在请求中广泛使用这一协议头。

不仅如此，**Cloudflare在返回的响应头中，加入了一个名为 `x-markdown-tokens` 的自定义标头，直接提示了该Markdown文档的预估Token数量。** 这项**设计**让内容送入大模型之前，就能精准计算上下文窗口占用，从而动态调整分块策略，告别“Token超载导致API报错”的尴尬局面。

## 拥抱合规：引入Content-Signal协议

在为AI大开方便之门的同时，如何保护网站所有者的权益？Cloudflare将Markdown转码与此前提出的**内容信号策略（Content Signals Policy）**进行了深度绑定。

当网络将Markdown返回给AI爬虫时，响应头中会明确带有授权声明，例如 `Content-Signal: ai-train=yes, search=yes, ai-input=yes`。**这一机制赋予了站长对数据用途的掌控权**，站长可以清晰界定自己的内容是否允许被用于大模型的基础训练、AI搜索结果呈现，或是作为AI Agent的实时输入上下文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFticAicsZ8RLPpydHKvPtRgdfnPnJO1DTdibOiatZice5gxNXxxibfTVp4JsAfgflvwzDy8wt9l7mMAJpMV94LibRqkh1H94ofkCwtDwU8/640?wx_fmt=png&from=appmsg)

---

## 点评

今天，AI Agent正成为新的流量分发中心。Cloudflare 精准捕捉到这一趋势：**让内容以 AI 原生格式直达Agent，既是效率优化，更是战略卡位**。

对于网站站长，建议尽早启用 Markdown for Agents，并关注 Content Signals 政策，以便在 AI 驱动的搜索、问答和自动化任务中保持可见性。对于 AI 开发者，则应在爬虫中增加 `Accept: text/markdown` 头部，毕竟Claude Code 和 OpenCode已经更新了，其他Agent也会慢慢跟进。不如主动利用这一特性，降低自身 token 成本并提升结果质量。

可以预见，未来网站不仅要为人类提供良好的阅读体验，还需为 AI 提供结构清晰的“数据接口”。Markdown for Agents 正是这座桥梁的雏形，让互联网在 AI 时代依然保持开放与可访问。

**以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnLIqb6wTzbSErRKzmg7cicZCtQB7Yz9PaKF4ichseJFxMOjJvgVtLVLmwInwfM88sTYvibpCibA7e6DMA/640?wx_fmt=png&from=appmsg)

*参考资料:* Introducing Markdown for Agents：https://blog.cloudflare.com/markdown-for-agents/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

玄月调查小组

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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