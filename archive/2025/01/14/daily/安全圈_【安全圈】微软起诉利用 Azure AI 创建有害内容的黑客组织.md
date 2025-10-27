---
title: 【安全圈】微软起诉利用 Azure AI 创建有害内容的黑客组织
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067321&idx=4&sn=4ea1e634e045d59be08019f06a4fd52b&chksm=f36e79b9c419f0afb77e12ec0c05482c0c727401e2761ea07b3093e610802a46b227f479adae&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-14
fetch_date: 2025-10-06T20:11:13.903173
---

# 【安全圈】微软起诉利用 Azure AI 创建有害内容的黑客组织

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljiazuFMNGnUe5Ms2UhJ2sTxbBk1AkJ71ZgDrgicphkLNdvGPaz2W9TZnliaHsoMKLvic811oOnaVIJuw/0?wx_fmt=jpeg)

# 【安全圈】微软起诉利用 Azure AI 创建有害内容的黑客组织

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

人工智能

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljiazuFMNGnUe5Ms2UhJ2sTxrwDrMJ92R6SILbEMTTa1fcqz7RvkBtc4OibILA9x43Cje7ia6iaWk9D9w/640?wx_fmt=other&from=appmsg)

微软透露，它正在对一个“外国威胁行为者团体”采取法律行动，因为该团体运营一个黑客即服务基础设施，故意绕过其生成人工智能 (AI) 服务的安全控制并制作攻击性和有害内容。

该科技巨头的数字犯罪部门（DCU）表示，已经观察到威胁行为者“开发复杂的软件，利用从公共网站上抓取的暴露的客户凭证”，并“试图识别和非法访问具有某些生成性人工智能服务的账户，并故意改变这些服务的功能。”

攻击者随后利用这些服务（例如 Azure OpenAI Service）将访问权限出售给其他恶意行为者，从而将访问权限货币化，并向他们提供有关如何使用这些自定义工具生成有害内容的详细说明。微软表示，它于 2024 年 7 月发现了这一活动。

这家 Windows 制造商表示，它已经撤销了该威胁行为者的访问权限，实施了新的对策，并加强了安全措施，以防止此类活动再次发生。该公司还表示，它已获得法院命令，要求查封一个对该组织犯罪活动至关重要的网站（“aitism.net”）。

OpenAI ChatGPT 等人工智能工具的流行也导致了威胁行为者滥用它们进行恶意攻击，从制作违禁内容到开发恶意软件。法庭文件显示，至少有三名身份不明人员是此次行动的幕后黑手，他们利用窃取的 Azure API 密钥和客户 Entra ID 身份验证信息入侵微软系统，并使用DALL-E创建有害图像，违反了其可接受使用政策。据信，另有七人也利用他们提供的服务和工具来达到类似目的。

目前尚不清楚 API 密钥的获取方式，但微软表示，被告对多个客户进行了“系统性 API 密钥盗窃”，其中包括几家美国公司，其中一些位于宾夕法尼亚州和新泽西州。

该公司在一份文件中表示：“被告利用窃取的属于美国微软客户的微软 API 密钥，创建了一种黑客即服务方案，可通过

‘rentry.org/de3u’和‘aitism.net

’域名等基础设施访问，专门用于滥用微软的 Azure 基础设施和软件。”

根据现已删除的 GitHub 存储库，de3u 被描述为“具有反向代理支持的 DALL-E 3 前端”。有问题的 GitHub 帐户于 2023 年 11 月 8 日创建。

据称，在“aitism.net”被查封后，威胁行为者采取措施“掩盖他们的踪迹，包括试图删除某些 Rentry.org 页面、de3u 工具的 GitHub 存储库以及部分反向代理基础设施”。

微软指出，威胁者使用 de3u 和定制的反向代理服务（称为 oai 反向代理），使用窃取的 API 密钥进行 Azure OpenAl 服务 API 调用，以便使用文本提示非法生成数千张有害图像。目前尚不清楚创建了什么类型的攻击性图像。

服务器上运行的 oai 反向代理服务旨在通过 Cloudflare 隧道将来自 de3u 用户计算机的通信汇集到 Azure OpenAI 服务，并将响应传回用户设备。

雷德蒙解释说：“de3u 软件允许用户通过一个简单的用户界面发出 Microsoft API 调用，使用 DALL-E 模型生成图像，该界面利用 Azure API 访问 Azure OpenAI 服务。”

“被告的 de3u 应用程序使用未记录的 Microsoft 网络 API 与 Azure 计算机进行通信，以发送旨在模仿合法 Azure OpenAPI 服务 API 请求的请求。这些请求使用被盗的 API 密钥和其他身份验证信息进行身份验证。”

值得指出的是，Sysdig 在 2024 年 5 月强调了使用代理服务非法访问 LLM 服务的情况，该活动与针对Anthropic、AWS Bedrock、Google Cloud Vertex AI、Microsoft Azure、Mistral 和 OpenAI 的 AI 产品的LLMjacking 攻击活动有关，该攻击使用被盗的云凭证并将访问权限出售给其他参与者。

微软表示：“被告通过协调和持续的非法活动模式来管理 Azure 滥用企业的事务，以实现其共同的非法目的。”

“被告的非法活动模式不仅限于对微软的攻击。微软迄今发现的证据表明，Azure Abuse Enterprise 一直在针对并攻击其他 AI 服务提供商。”

来源：https://thehackernews.com/2025/01/microsoft-sues-hacking-group-exploiting.html

***END***

阅读推荐

[【安全圈】腾讯协助警方破获木马盗窃游戏账号案，涉案金额超 3000 万](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067304&idx=1&sn=e99889dcbf4e15a2ad7a2217e3f850a3&scene=21#wechat_redirect)

[【安全圈】勒索木马 Banshee 针对苹果 macOS 下手，冒充安全组件躲避检测](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067304&idx=2&sn=72944b1de7bb9205840492e28ba936b4&scene=21#wechat_redirect)

[【安全圈】卡西欧遭勒索软件攻击？8500人数据被窃取！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067304&idx=3&sn=1f094579cd41cb8e1f1583f6eb592503&scene=21#wechat_redirect)

[【安全圈】江苏一男子利用小程序Bug逃匿28万加油费，法院判了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067274&idx=1&sn=5bef640b5980a10e736f5e8b28bb6773&scene=21#wechat_redirect)

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