---
title: WebMCP，为硅基生物服务
url: https://mp.weixin.qq.com/s/DgCVx15PYK_btcZh3xMsTQ
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:16:40.095922
---

# WebMCP，为硅基生物服务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6MUBLO7YeeVXx7xxzI9BxUPJelcf0E18R9RsriatykQPvc1UjzaxgOUBia2fwMQ9VyBoXPx4RPH3uqLh4WaHlE58wOGc4uTxmlqs/0?wx_fmt=jpeg)

# WebMCP，为硅基生物服务

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器中沉浸阅读

最近由微软谷歌，联合推出了一个新的W3C 标准提案，WebMCP，Chrome已经宣布支持该标准协议，并且开启了预览版。

https://developer.chrome.com/blog/webmcp-epp

该标准协议是专门设计给AI Agent(人工智能代理)，便于Ai获取网页内容和操作网页。

* Google Chrome（从146 Canary开始）已经early preview了这个API，由Google + Microsoft工程师主导，W3C Web Machine Learning Community Group在孵化。
* 核心思路：网站主动暴露结构化“工具”（类似OpenAI/Anthropic的function calling schema），用navigator.modelContext这个浏览器API注册。

+ 有两种方式：Declarative（直接在HTML form加几个属性就能自动变成tool）和Imperative（用JS动态定义更复杂的工具）。

* 以前agent操作网页靠什么？截图 → 多模态模型猜按钮 → 模拟点击/输入，极其低效、容易出错、token消耗巨大。
* 现在有了WebMCP，agent直接像调用API一样调用网站的预定义功能，比如bookFlight(origin, destination, date)，返回结构化JSON，速度提升几十倍，准确率接近100%，而且网站还能控制权限、认证、上下文共享。

历史可能会记住，差不多是从WebMCP开始，软件设计从 “人类的视觉体验” 转向为 “AI 的调用效率”，也正式进入软件、工具等，不仅只是服务于人类，同时也要服务AI Agent(智能体)。

如去年初所写

[接下来的AI时代](https://mp.weixin.qq.com/s?__biz=Mzg4MzY3MTgyMw==&mid=2247484015&idx=1&sn=9b6f8ee748f95d2fd786a8045e74b7db&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PnialD7umqBib2icNianpyuoJPyYt38CJt6mcc4u6rQ61WG0bRc7sOYVtdnbHZnqvokM3woQOEsnOzu5MHyC3ySXa9FVmfTzBictpc/640?wx_fmt=png&from=appmsg)

社会发展需要适配更高效的生产力，但键盘、鼠标、显示器等之前适配人类生产的工具对ai来说太慢了，毕竟工具的形态，取决于谁是主要的使用者。

这只是个开始，之后会有越来越多的工具，会给agent开放接口，人类操作与ai操作并行，甚至之后的工具只是为了给ai Agent设计。

未来的工具、软件、甚至城市规划，必然会优先适配 AI 的“生理特征”（智能、高并发、API 连接、7x24小时在线），而不是人类的生理特征（视觉依赖、需要睡眠、手眼协调）。

就如曾经人类为了自身的生存，改造了地球的地貌，创造了城市、公路、电网这套适配人类生理和行为习惯的生存系统；当 AI 成为新的生产力主体，它也会逐步创造出适配自身算力、通信、能耗需求的物质形态和物理环境。

日新月异的AI发展速度，这一天真是越来越近了，甚至AI agents可能不用再假装是人了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

鬼麦子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

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