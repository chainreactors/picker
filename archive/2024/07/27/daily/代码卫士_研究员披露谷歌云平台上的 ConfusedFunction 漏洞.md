---
title: 研究员披露谷歌云平台上的 ConfusedFunction 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520228&idx=2&sn=e2baa4f853063d34474bdd1973b4b156&chksm=ea94be8edde33798101d04ab50a6066bd659de102e44e7f9e8a8a8d63f9a91f86499e33bffbd&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-27
fetch_date: 2025-10-06T17:43:09.383191
---

# 研究员披露谷歌云平台上的 ConfusedFunction 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS8BY61icLViaX2jVuzSdo1Aicbic1lia27YDicgAJqL5TzicS4kJ9yVypMYXMGvIGwrxJycsbc399jZEGTA/0?wx_fmt=jpeg)

# 研究员披露谷歌云平台上的 ConfusedFunction 漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究员披露了一个影响Google Cloud Platform 的 Cloud Functions 服务的提权漏洞，可被用于越权访问其它服务和敏感数据。Tenable 公司将其称为 “ConfusedFunction”。**

Tenable 公司在一份声明中表示，“攻击者可将权限提升至默认的云构建服务账户并访问多种服务如 Cloud Build，存储（包括其它函数的源代码）、制品注册表和容器注册表。该权限可用于在受害者项目中进行横向移动和权限提升，访问越权数据，甚至是更新或删除它。”

Cloud Functions 是指serverless 执行环境，可使开发人员创建单一目的的函数，在对特定 Cloud 事件进行响应时触发，而无需管理服务器或更新框架。Tenable 公司发现的这个漏洞与 Cloud Build 服务账号在背景中创建并在创建或更新 Cloud Function 时默认与一个 Cloud Build 实例关联的事实有关。该服务账号导致权限过度造成的潜在恶意活动，因此导致能够创建或更新 Cloud Function 的攻击者能够利用该漏洞并将权限升级至服务账号。

该权限随后别滥用于访问其它也是通过 Cloud Function 创建的 Google Cloud 服务，如 Cloud Storage、Artifact Registry和 Container Registry。在理论攻击场景中，ConfusedFunction 可被用于通过 webhook 泄露 Cloud Build 服务账号令牌。

负责任地披露后，谷歌已更新该默认行为，以便 Cloud Build 使用 Compute Engine 默认服务账号以阻止滥用。然而，值得注意的是，这些变更并不适用于现有的实例。

安全研究员 Liv Matan 表示，“该 ConfusedFunction 漏洞凸显了云提供商服务中的软件复杂性和服务间通信可能造成有问题的场景。虽然 GCP 修复方案已经降低了未来部署问题的严重性，但它并未完全消除这一问题，因为CloudFunction的部署仍然触发之前所提 GCP 服务的创建。因此，用户必须仍然为 Cloud Build 服务账号分配最大但仍然相对宽泛的权限。”

前不久，Outpost24 详述了位于 Oracle Integration Cloud Platform 中的一个中危 XSS 缺陷，它可用于将恶意代码注入应用程序中。该漏洞的根因在于对于 “consumer\_url” 参数的处理，已由 Oracle 在本月早些时候发布的“关键补丁更新 (CPU)”中发布。

安全研究员指出，“创建新集成的页面可见 https://<instanceid>.integration.ocp.oraclecloud.com/ic/integration/home/faces/link?page=integration&consumer\_url=<payload>，并不要求其它参数。这意味着攻击者仅需识别特定集成平台的 instance-id向平台的任何用户发送功能性 payload。因此，攻击者可绕过了解特定集成ID的要求，二者一般仅可供已登录用户访问。”

Assetnote 也在前不久发现了 ServiceNow 云计算平台中的三个漏洞（CVE-2024-4879、CVE-2024-5178和CVE-2024-5217），可被纳入利用链中，获得完整的数据库访问权限并在Now Platform 上下文中执行任意代码。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[谷歌云 SQL Service 中存在严重漏洞，导致敏感数据遭暴露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516609&idx=1&sn=e6bef0b6cbbd3d38ef6d69c14130bdcc&chksm=ea94b0abdde339bd0efab5037b36b84212e32e77cb0a866ec8ea90ff15509d9afb7433ee96d5&scene=21#wechat_redirect)

[谷歌云被用来传播银行木马Telax](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485832&idx=6&sn=ee4852e34c391a8e8f9274f2afee1b42&chksm=ea9738e2dde0b1f45d1f6edebec9703272b70bd2ab53a0e41e222d64f77f81e9e119072614b5&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/07/experts-expose-confusedfunction.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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