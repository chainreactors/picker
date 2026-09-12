---
title: 表单提交下的越权删除漏洞
url: https://mp.weixin.qq.com/s/teOVmSF8KncbQsih3mhDeg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:45:04.268955
---

# 表单提交下的越权删除漏洞

# 表单提交下的越权删除漏洞

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
原文链接: https://0xsponge.medium.com/how-i-got-my-first-bounty-70cd498b9fc5
```

在进行大规模子域名枚举时，我发现了一个名为 ***inspire.example.com***的子域名，该子域名专门用于收集网站设计灵感。其核心功能允许用户通过表单提交设计创意，并等待管理员审核和批准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibwbRuU1CTziajpgibHqKgjhZSBclcrAG5sX0lL4diaKZUeaquBaoGibrTHrHWHaWuKzX7VlIib3oxGhjRCfSflCictRdxvgmaDlSKlkA/640?wx_fmt=png&from=appmsg)

但我是呢？难道我还要等管理员批准吗？不，我不得不绕过这个流程。

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibwYxMAYwl8gwehpCUozeg6LVK9KVqnde66zwtwyvbMQia47pIm3BkdsLFqlwS13tLLiclEqAXka5rMVPusEKadWDlT5NQ2aVrUrQ/640?wx_fmt=png&from=appmsg)

在检查端点时，我发现点击“发布”按钮会向 `/example/api_path/publish`该端点，并携带以下数据： `{"id":"inspiration-post-id","status":"Denied"}`

于是我心想——干脆把“拒绝”改成“批准”，看看服务器会不会盲目地相信它？

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibxp0Amk0rpWswCvXmBicnh0y3cyVmpBc2iaCIZQ9lQ7VpapoJvaHFbJAQumKoetPL8uWbuG3YlA1d4NMym7uSX0wtHKNrpae36Qc/640?wx_fmt=png&from=appmsg)

令人惊讶的是，服务器竟然在未进行任何验证的情况下就相信了我的请求！！！

但当我提交报告后，他们将其标记为“低优先级”。他们的理由是，管理员会定期审查帖子，并大约每20分钟删除一次。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/jow1el0IZibxlq8w0BmMO3YODsjZCbtXHSkAWLmPl2NwMYXCl90wLFXA1cwBFyZ4lejiaXYEdHvgU2F94Cmu55cv8q1zAAdrP5WgJcHjcQZaM/640?wx_fmt=gif&from=appmsg)

因此，我决定必须让这个漏洞变得更值得悬赏，并放大其影响。

于是，我开始深入研究该 `/example/api_path/publish`该端点进行更深入的探究。我再次尝试复现该漏洞，在第一次请求返回后 `{"success":true,"newStatus":"Approved"}`后，我再次发送了相同的请求。这次，服务器返回了 `{"success":true,"newStatus":"Unpublished"}`.
嗯……有意思。

于是我不禁想——我能否将 ID 改为任何其他文章的 ID，然后将其设为“未发布”？但有一个问题：我该如何获取那个随机的 ID 呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/jow1el0IZibweGicyAQZUQW6CBUQr8A3Lmb6HB7CPnG5iaYbRalAPU0eBYWgcvMkEaFagHDkkMdkE3gu57j3h5lEp3qrkwoicMGVdrjlt8ic18y0/640?wx_fmt=gif&from=appmsg)

于是，我记下了那篇给我带来灵感的文章的 ID，发布了这篇文章，打开了该文章的页面，并查看了源代码。我搜索了自己的文章 ID，想看看它是否被硬编码了，出乎意料的是，我发现它就在一个名为 `Dynamic-page-id`.

我在 `/example/api_path/publish`请求中，将我的帖子 ID 替换成了受害者的 ID，出乎意料的是，服务器接受了该请求并删除了受害者的帖子。我提交了报告，并获得了我的 **Bountyyy**！

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/jow1el0IZibzibz34QJVbUicl8TtQAK21sxseGwzRdtV76c31cgYEgmUXS12Pkxic5KpiaWkMVibWibuM4XCzsLSFJwHQntDB57hyN0ria6RNv0LlOQ/640?wx_fmt=gif&from=appmsg)

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