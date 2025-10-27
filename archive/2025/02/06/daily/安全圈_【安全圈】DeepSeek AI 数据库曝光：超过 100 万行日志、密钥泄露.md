---
title: 【安全圈】DeepSeek AI 数据库曝光：超过 100 万行日志、密钥泄露
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=2&sn=c07d521bd863d5ef6b8232fd91c2d58e&chksm=f36e7b7bc419f26da11945bfa3793982820aa3fb47f2f07f95107d2007d285e2f3c070eb268a&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-06
fetch_date: 2025-10-06T20:36:57.461962
---

# 【安全圈】DeepSeek AI 数据库曝光：超过 100 万行日志、密钥泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh6va8PhaiauHBQUYnw3dCvAuib5KomiaVrsbw826Trk6rdfY7lv3LW6UWRWfeICAibpRvj9iczoicGa7HQ/0?wx_fmt=jpeg)

# 【安全圈】DeepSeek AI 数据库曝光：超过 100 万行日志、密钥泄露

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

DeepSeek

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh6va8PhaiauHBQUYnw3dCvAPU0kfh9Jgb0b2yibDnO4dSYmWKDZ7La3F8RU5F41YLve3dWO0thjzibQ/640?wx_fmt=other&from=appmsg)

近日人气飙升的中国人工智能初创公司DeepSeek的一个数据库暴露在互联网上，这可能让恶意行为者获取敏感数据。

Wiz 安全研究员 Gal Nagli表示，ClickHouse 数据库“允许完全控制数据库操作，包括访问内部数据的能力” 。

此次曝光还包括超过一百万行日志流，其中包含聊天记录、密钥、后端详细信息以及其他高度敏感的信息，例如 API 机密和操作元数据。在云安全公司尝试联系 DeepSeek 后，该公司已修补了安全漏洞。

据称，托管在oauth2callback.deepseek[.]com:9000 和 dev.deepseek[.]com:9000 的数据库允许未经授权访问大量信息。Wiz 指出，此次暴露允许在 DeepSeek 环境中实现完全数据库控制和潜在特权升级，而无需任何身份验证。

这涉及利用 ClickHouse 的 HTTP 接口直接通过 Web 浏览器执行任意 SQL 查询。目前尚不清楚是否有其他恶意行为者抓住机会访问或下载数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh6va8PhaiauHBQUYnw3dCvAkSLcQmAzFqejrgUic8boFRYk50g730zwtaOxqq4U26mEEXRc4ntOYJw/640?wx_fmt=other&from=appmsg)

纳格利在与 The Hacker News 分享的一份声明中表示：“在没有相应安全保障的情况下快速采用人工智能服务本身就存在风险。尽管人们对人工智能安全的大部分关注都集中在未来威胁上，但真正的危险往往来自基本风险——比如数据库的意外外部暴露。”

“保护客户数据必须仍然是安全团队的首要任务，而且安全团队与人工智能工程师密切合作以保护数据并防止泄露至关重要。”

DeepSeek 因其突破性的开源模型而成为人工智能圈的热门话题，这些模型号称可以与 OpenAI 等领先的人工智能系统相媲美，同时又高效且经济实惠。其推理模型 R1 被誉为“人工智能的斯普特尼克时刻”。

这家新兴公司的人工智能聊天机器人已经在多个市场的 Android 和 iOS 应用商店排行榜上名列前茅，尽管它已成为“大规模恶意攻击”的目标，导致其暂时停止注册。

在 2025 年 1 月 29 日发布的更新中，该公司表示已经发现该问题，并且正在努力实施修复。

与此同时，该公司的隐私政策也受到严格审查，更不用说其与中国的关系已成为美国国家安全问题的关注点。

此外，在意大利数据保护监管机构 Garante 要求提供有关其数据处理实践以及其从何处获取训练数据的信息后不久，DeepSeek 的应用程序在意大利就无法使用。目前尚不清楚应用程序的下架是否是为了回应监管机构的质询。爱尔兰数据保护委员会 (DPC) 也发出了类似的请求。

彭博社、金融时报和华尔街日报也报道称，OpenAI 和微软都在调查 DeepSeek 是否在未经许可的情况下使用了 OpenAI 的应用程序编程接口 (API)，并在 OpenAI 系统的输出上训练自己的模型，这种方法被称为“蒸馏”。

OpenAI 发言人向《卫报》表示：“我们知道，中国的一些团体正在积极尝试使用包括所谓的提炼方法在内的方法来复制先进的美国人工智能模型。”

来源：https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html

***END***

阅读推荐

[【安全圈】Microsoft Entra ID允许普通用户更新自己的UPN](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067622&idx=2&sn=a56656b05bfd9f42f777c577cffe85e3&scene=21#wechat_redirect)

[【安全圈】黑客利用Windows RID劫持技术创建隐藏管理员账户](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067622&idx=3&sn=ad95819ae6f36cb189f9da9618fff556&scene=21#wechat_redirect)

[【安全圈】2000余名网红遭信息“开盒” 嫌疑人获利几十万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=1&sn=06c7d132a1649380a5b7629742f5d3f7&scene=21#wechat_redirect)

[【安全圈】微软 Win10 / Win11 新威胁：RID 劫持可提权至管理员控制你的 PC](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=2&sn=efa053f9e1755bb17193b5a5868fb8ce&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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