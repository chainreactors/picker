---
title: 【安全圈】Fortinet 通过第三方确认客户数据泄露
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064456&idx=4&sn=b5bf8c69ef9501702abdd965db04ef36&chksm=f36e6688c419ef9e2fd7f0f668505a305d8d47ec7d22e2f594e499dbd8eb7b2b05f3ecf683c9&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-17
fetch_date: 2025-10-06T18:26:51.233728
---

# 【安全圈】Fortinet 通过第三方确认客户数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFBbhGXuUic04WYaJnCGVIeN1wXCmxYmRtlL5p7lDanJrga2ov9oWyn4Ig/0?wx_fmt=jpeg)

# 【安全圈】Fortinet 通过第三方确认客户数据泄露

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

数据泄露

Fortinet 已确认属于其“少数”客户的数据遭到泄露，此前一名黑客本周使用有点色彩缤纷的绰号“Fortibitch”泄露了 440GB 的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFBXAtZ5RMoIfUaF7hco17VqOL0pfMhG6XOkt8Shh8cLeeceOMCaLRDQw/640?wx_fmt=jpeg)

黑客声称从 Azure SharePoint 站点获取了数据，并声称他们在公司拒绝与该个人就赎金要求进行谈判后泄露了这些数据。研究人员表示，这种情况再次凸显了公司必须保护第三方云存储库中保存的数据的责任。

## 未经授权访问 SaaS 环境

Fortinet 本身尚未具体确定泄露的来源。 但在 9 月 12 日的公告中，该公司表示，有人“未经授权访问了存储在 Fortinet 基于云的第三方共享文件驱动器实例上的有限数量的文件”。

这家安全供应商是全球市值最大的安全供应商之一，它发现该问题影响了其全球 775,000 多家客户中的不到 0.3%，这将使受影响的组织数量约为 2,325 家。

Fortinet 表示，它没有看到围绕受感染数据进行恶意活动的迹象。“Fortinet 立即执行了一项保护客户的计划，并酌情直接与客户沟通并支持他们的风险缓解计划，”该安全供应商在公告中指出。“该事件不涉及任何数据加密、勒索软件部署或访问 Fortinet 的企业网络。”Fortinet 表示，预计该事件不会对其运营或财务产生任何重大影响。

在与 Dark Reading 共享的威胁情报报告中，CloudSEK 表示，它观察到一个使用 Fortibitch 手柄的威胁行为者泄露了似乎不仅包括客户数据，还包括财务和营销文件、产品信息、来自印度的人力资源数据以及一些员工数据。

“该行为者试图勒索公司，但在谈判失败后，公布了数据，”CloudSEK 说。该公司推测，如果数据有任何真实价值，黑客会先尝试出售这些数据。

Fortinet 没有确认或否认黑客是否试图与该公司就被盗数据进行接触。

该黑客在 BreachForums 上的帖子包括对 Fortinet 收购 Lacework 和 NextDLP 的上下文无关的引用。它还提到了其他一些威胁行为者，其中最有趣的是被追踪为 DC8044 的乌克兰组织。“Fortibitch 和 DC8044 之间没有直接联系，但语气表明两者之间存在历史，”CloudSEK 表示。“根据现有信息，我们可以中等置信度确定威胁行为者位于乌克兰境外。”

## 泄露 Cloud Data Exposure 风险提醒

Fortinet 泄露事件（虽然显然不是太严重）提醒人们，在没有适当护栏 的情况下使用软件即服务 （SaaS） 和其他云服务时，企业组织的数据泄露风险会增加。Metomic 最近对大约 650 万个 Google Drive 文件进行了扫描，结果显示其中超过 40% 的文件包含敏感数据，包括员工数据和包含密码的电子表格。

通常，组织将数据存储在 Google Drive 文件中，几乎没有保护。超过三分之一 （34.2%） 的扫描文件与外部电子邮件地址共享，超过 350,000 个文件已公开共享。

Metomic 的首席执行官兼创始人 Rich Vibert 表示，在云环境中保护数据时，组织会犯三个基本错误：不使用多因素身份验证 （MFA） 来控制对 SaaS 应用程序的访问;为员工提供对应用程序本身中的文件夹和敏感资产的过多访问权限;以及存储敏感数据的时间过长。

目前尚不清楚黑客是如何从 Fortinet 的 SharePoint 环境中访问数据。但 CloudSEK 的威胁情报记者 Koushik Pal 表示，一种可能的情况是，攻击者通过网络钓鱼等方式获得了对有效登录凭据的访问权限，然后登录并从 SharePoint 和类似环境中泄露了数据。Pal 指出，信息窃取程序也是一种“非常常见”的攻击媒介。

## 重新思考云安全

“通常，开发人员应该使用环境变量、保险库或加密存储来存储敏感信息，并避免在源代码中对凭据进行硬编码，”Pal 说。开发人员通常会将 API 密钥、用户名和密码等访问凭证硬编码到源代码中，并无意中将代码推送到公共或不安全的私有存储库中，从那里可以相对容易地访问它们。

“组织应强制要求访问 SharePoint 和其他关键系统时使用 MFA，以防止未经授权的访问，即使凭据被盗用，”Pal 解释说。“定期监控存储库，以发现泄露的凭据、敏感数据或错误配置，并在所有团队中实施安全最佳实践。”

Synopsys Software Integrity Group 网络安全高级经理 Akhil Mittal 表示，像 Fortinet 经历的事件表明，为什么组织将其云资产的安全完全交给云服务提供商是一个错误。“组织应该重新考虑如何将客户数据存储在共享驱动器中，确保关键信息与不太敏感的文件分开保存，”他说。

对传输中和静态的敏感数据进行加密也是一个好主意，这样即使攻击者获得了访问权限，也可以减轻损害。Mittal 认为对云资产的持续监控是保护云资产的基础。“将零信任原则应用于第三方平台还可以确保不会自动信任任何外部服务，从而降低未经授权访问的风险，”他补充道。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibjicbKBqZwLQOxpR2qCTWlaiaM5jCxqdicU8OIgjqQBficHFboNPXYSLA7LQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibj8Zw7CkjRgdkISTjGSylfpzEbSeU0MR1MyV4mNgsDVGYFpFRciaw820Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibjUZHVxvj9xuwq2VUNY7LWzsU86Iq9WQVMCN792aE23UQIC6BtOzoNHA/640?wx_fmt=other)[【安全圈】57岁前员工怒删公司备份、搞瘫3000+台电脑，勒索532万元未遂被捕！网友：怀疑他是被裁的](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064438&idx=3&sn=437555202148f978ad5399834d57c798&chksm=f36e66f6c419efe00dd8ee70aca196a85b33e51b6e80c08228cc0809448d3628bdddffa8bdf1&scene=21#wechat_redirect)

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