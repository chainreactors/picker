---
title: 【安全圈】PyPI 上的信息窃取恶意软件冒充了 DeepSeek AI 工具
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=1&sn=87a028f93da64d77ab88febfae2b2d56&chksm=f36e7b15c419f203e33e3b5abaadef4379c831d462ff19e8c519765b1a304ea1988195bb7e96&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-07
fetch_date: 2025-10-06T20:37:40.467952
---

# 【安全圈】PyPI 上的信息窃取恶意软件冒充了 DeepSeek AI 工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEsEcQxAbXxs3ATqhldybguI9ibK2Mhibv8QX6SUVek2S9vTEXj8RwPCHg/0?wx_fmt=jpeg)

# 【安全圈】PyPI 上的信息窃取恶意软件冒充了 DeepSeek AI 工具

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IErib6wgbqG5roYtX4LkFlEbVEE1NIZx9m2XmIrQmlwicDHpvaBia6ooA0w/640?wx_fmt=other&from=appmsg)

威胁行为者利用 DeepSeek 的日益流行，在 Python 包索引 (PyPI) 上推广两个恶意信息窃取程序包，他们在其中冒充 AI 平台的开发工具。

这两个软件包被命名为“deepseeek”和“deepsekai”，以中国人工智能初创公司的名字命名。该公司开发了最近 人气飙升的R1 大语言模型。

有趣的是，这些包裹是由一个 2023 年 6 月创建的“老”账户上传的，之前没有任何活动。

据发现该活动并将其报告给 PyPI 的 Positive Technologies 研究人员称，伪装成 DeepSeek AI Python 客户端的软件包是信息窃取程序，会从使用它们的开发人员那里窃取数据。

一旦在开发人员的机器上执行，恶意负载就会窃取用户和系统数据以及环境变量，例如 API 密钥、数据库凭据和基础设施访问令牌。

接下来，被盗信息通过合法自动化平台 Pipedream泄露至eoyyiyqubj7mquj.m.pipedream[.]net的命令和控制 (C2) 服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEtSchmic5IejHVGxib8TPlusYM0XxnpibbJUDpt3gibiaiaicnJd5z9hkcwlicw/640?wx_fmt=other&from=appmsg)

威胁行为者可以利用这些被盗信息访问开发人员使用的云服务、数据库和其他受保护资源。

Positive Technologies 的报告中写道：“这些软件包中使用的功能旨在收集用户和计算机数据并窃取环境变量。”

“当用户在命令行界面运行命令 deepseek 或 deepseekai（取决于软件包）时，有效载荷就会执行。”

“环境变量通常包含应用程序运行所需的敏感数据，例如 S3 存储服务的 API 密钥、数据库凭据以及访问其他基础设施资源的权限。”

## 多名受害者

恶意软件包 deepseeek 0.0.8 和 deepseekai 0.0.8 于 2025 年 1 月 29 日上传到 PyPI，两者之间间隔仅有 20 分钟。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEFqFJSNjR38iaAwXWEVJlf4ZCibIIMNemKKGpwtoNxK4kveOkVVqBAomQ/640?wx_fmt=other&from=appmsg)

来源：Positive Technologies

Positive Technologies 很快发现了这些问题并向 PyPI 报告，PyPI 隔离并阻止了这些软件包的下载，随后将其从平台上彻底删除。

尽管检测和响应迅速，但仍有 222 名开发人员下载了这两个软件包，其中大多数来自美国（117），其次是中国（36）、俄罗斯、德国、香港和加拿大。

使用这些软件包的开发人员应该立即轮换他们的 API 密钥、身份验证令牌和密码，因为它们现在可能已被泄露。还应检查任何凭证被盗的云服务，以确认它们没有受到损害。

来源：https://www.bleepingcomputer.com/news/security/deepseek-ai-tools-impersonated-by-infostealer-malware-on-pypi/

***END***

阅读推荐

[【安全圈】DeepSeek遭遇大规模网络攻击，暂停新用户注册](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=1&sn=110423832f37fabbb95e2bc014e2efb1&scene=21#wechat_redirect)

[【安全圈】DeepSeek AI 数据库曝光：超过 100 万行日志、密钥泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=2&sn=c07d521bd863d5ef6b8232fd91c2d58e&scene=21#wechat_redirect)

[【安全圈】Pwn2Own Automotive 2025 黑客因破解 49 个零日漏洞获 886,250 美元奖励](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=3&sn=15fafdc5115ba7e7a871e108304d8284&scene=21#wechat_redirect)

[【安全圈】以色列间谍软件公司Paragon涉嫌利用WhatsApp零点击漏洞发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=4&sn=cee4f0162f4215b03faa784f2a08ca29&scene=21#wechat_redirect)

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