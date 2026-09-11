---
title: 测试那些没人愿意测试的接口，总能发现点什么
url: https://mp.weixin.qq.com/s/WpQ6zc5yoZq9DEqsWvjAqQ
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:49:13.301660
---

# 测试那些没人愿意测试的接口，总能发现点什么

# 测试那些没人愿意测试的接口，总能发现点什么

Adhamkhairy
Adhamkhairy

漏洞集萃

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> **本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途；如有侵权烦请告知，我们会立即删除并致歉，谢谢**

在测试一个私有漏洞赏金计划时，我遇到了一个

```
作者: Adhamkhairy
原文链接: https://0xsponge.medium.com/debugging-endpoints-nobody-bothers-to-test-leads-to-some-crits-579eb9fbceb7
```

如何通过在调试器中阅读两行代码，将一个 Cookie 政策页面变成了一个关键漏洞。

该网址是这样一个无聊的链接：

```
https://app.example.com/cookie-policy/es/es
```

一个 Cookie 政策页面。路径中包含语言代码。仅此而已。

没人会测试这个。你看 `/cookie-policy/`通过测试工具查看时，你的视线会直接略过它，径直跳转到登录流程、文件上传、支付接口……任何真正能触发操作的地方。一个纯粹用于展示 Cookie 相关法律文本的页面，在任何测试目标中都是最无趣的东西。

我还是在上面打开了调试器，主要是出于固执。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibzofAX49CWtVXR017TowDuuepqtZoFv2ibsgULXE9TvTFXyEKDEeV5FTmQW4l1fK1icJiaNn75FnseeljfYRPqkVN8qyFLNzdLEZw/640?wx_fmt=png&from=appmsg)

调试器告诉我这不是一个静态页面

我打开了该页面，启动了开发者工具，然后开始逐步调试。

没有理论，也没有预设的预期结果。只是在组件的早期阶段设置了一个断点，然后一行一行地向前执行，观察代码是如何自行运行的。

结果才看了几帧，我一开始的设想就彻底破产了。

我一直在阅读 `/cookie-policy/es/es`像处理任何本地化 URL 那样——将其视为**静态路由**。 `en`是**英语**。有一个**英语**页面。它返回该**英语**页面。太无聊了，搞定，继续下一条。URL *看起来*就是这个意思。

不过调试器显示 `en`根本没有选择任何页面。它只是作为值从路由中提取出来的：

```
const { language } = this.route.snapshot.params;
```

那不是路由。那是*读取我的输入*。我在地址栏中输入的字符串现在已成为应用程序内部的一个变量，而在输入过程中，没有任何机制检查它是否是一个真实的区域设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibyDaVdpGAvLDqaXnMbOGibtkZh0LiccrqXuVtTSVa1jvSNic6jLUfFLoT4icEVQFR7GDsAocGmto5hic5zw0ByfWIrTObqmjV9RQib8k/640?wx_fmt=png&from=appmsg)

这重新定义了整个页面的攻击面。静态的区域设置路由没有攻击面。将路径片段提升为变量的页面，其攻击面大小完全取决于该变量后续被如何使用。

于是，我继续一步步地走下去。慢慢地。并不是在寻找有效载荷——只是沿着代码中属于我自己的那条线索，一行一行地追踪，直到看清它最终落在了哪里。

两帧之后：

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibwI9D2hbcwCaeRP4wnYe11h8ib7XYgiczxY3144eZSCJ6zancUu7oM4YIIoiajxCUh77n0rMRBS9whEAnk7UandD9p64jhWNIsA0o/640?wx_fmt=png&from=appmsg)

```
const link = AppConfig.cookieConsentFrameUrl + language;
trustArcWindow.html = trustArcWindow.html.replace("{path}", link);
```

于是，我就不读下去了。

## 这些话的实际含义是什么

重新向上： `language`直接取自 URL。既没有验证，也没有白名单，更没有检查它是否为真实的区域设置。

然后它会被**拼接到一个配置 URL 上。**不是 `encodeURIComponent`。不是 URL 对象。而是字符串拼接。

然后，将结果填入 HTML 模板中，通过替换一个 `{path}`占位符。

它被放置的模板是一个 iframe：

```
<iframe width='100%' height='800' src='{path}'></iframe>
```

因此，我的输入会直接进入一个 HTML 属性中，该属性位于即将被渲染的 HTML 字符串内。我又追踪了一个帧，想弄清楚它是如何被渲染的，结果就看到了：

```
addHtml(u){ this.htmlContainer.nativeElement.innerHTML = u }
```

原始 `innerHTML`，直接写入 DOM 节点。

这是 Angular。Angular 提供了一个数据净化器。Angular *希望*为你对数据进行净化——这正是 `[innerHTML]`绑定。有人绕过了它，直接向 `nativeElement`，这会关闭框架的内置保护机制。

源头与汇口，相距四行，其间空无一物。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibxQuTfZXweznd4xo8JGQTrNia1v60EMyJ5USHDAevN0Rcaib1H1AEwibJH7Tc4On7I2zfaGuASNYia2f0ZjqITP7WRqSbKZSP1qaicc/640?wx_fmt=png&from=appmsg)

有效载荷会自动写入

一旦你能看到“sink”，那么这个创意就不再是富有创意的作品了。你只不过是在关闭已经打开的东西罢了。

我的数值位于 `src='...'`。因此：

* A `'`关闭该属性
* `>`

  关闭 iframe 的开始标签
* `</iframe>`

  — 这一点很重要。Iframe 的子元素会被解析为原始文本，因此你注入*到*该元素内的任何内容都处于非活动状态。你必须先将其关闭，才能恢复为可解析的 HTML。
* 那么，作为兄弟元素，你可以放任何内容

大致是这样的：

```
'></iframe><svg onload=...>
```

将其加载到一个新的标签页中，脚本便会在应用程序自身的源上执行。

正因如此，Cookie 政策页面便不再仅仅是一个 Cookie 政策页面。同源原则意味着注入的脚本位于应用程序的安全边界之内——它可以读取应用程序自身的端点，干预已登录用户正在进行的任何操作，并冒充该用户与后端进行交互。就这个特定目标而言，这意味着一个处理用户个人提交信息和文档上传的工作流。

这篇文章很无聊，但刊登它的平台却并非如此。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibwSibyOHoQibH4fBsSIv4FM6ib6DVIWq1DcSsJ55frmNZKmCMPvgKJYjWZ8MIls815rc5pmuzpiaKPotO6rMp9lNFa0xY939aqTLsg/640?wx_fmt=png&from=appmsg)

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibwUfviaBILEz7O2aibDiaUy4ia1bwnWLBMJBtcSj2eXgmfiaQ0BEEuNtbuXMVknuXh6R3GwGBreg29D5wEWU4gpDtCLmrQFbpwaf23E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/jow1el0IZibwCzN8sFyiaI4HAcKhAw9acRsJhCloFL7WPpJKnn9538uyJrPmhPbAicrDX0ReFBy0ibD2zAz4vBRxtMLvU4a1jgMDDsZficxVh6Lw/640?wx_fmt=gif&from=appmsg)

XSS 成功了！！！！！！

## 真正的教训

这就是我希望你们从中总结出的规律，因为这是可以反复运用的部分。

本地化内容的渲染是一个**已解决的问题**。每个框架都有相应的实现方法。最基础的实现方式如下：

```
@app.get("/{lang}")  →  return templates[lang]
```

查询区域设置。返回模板。完成。输出中不包含任何用户输入。

当你发现有人用一种*独特*的方式在处理同一个已解决的问题时——比如通过 `+`，用 `.replace()`，或者将数据写入 `innerHTML`——而框架明明提供了经过安全处理的绑定接口——这每次都是一个危险信号。

并不是因为自定义代码不好。而是因为自定义代码意味着有人认为安全路径不适合他们的场景，于是偏离了这条路径。框架的默认设置在设计上就是安全的。任何围绕这些默认设置手动编写的代码，都是由开发者为了让功能正常运行而编写的，而非考虑当遇到恶意字符串时会发生什么。

已解决问题的自定义实现中往往存在错误。

而你只有通过设置断点，一行一行地阅读代码，才能看到它们，直到查明你的输入最终流向了哪里。这个过程既慢又乏味，这也正是我为何在其他人早已滑过的页面上，依然能发现那个线索的原因。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[逻辑漏洞：邮箱注册 tips #11](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485053&idx=1&sn=518c8e66c4b2fdf4eb7a0c57c8a28005&scene=21#wechat_redirect)

[非常用403绕过 Tips](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485249&idx=1&sn=42308de5857f3dd4f4d1414e94169dab&scene=21#wechat_redirect)

[Android IPC 漏洞利用系列](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485391&idx=1&sn=5092c4204d9910fa5b514d8dba7bb3b5&scene=21#wechat_redirect)

[新技术绕过文件上传](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485346&idx=1&sn=c35a5732cb610a100e608d249c56fd3b&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

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