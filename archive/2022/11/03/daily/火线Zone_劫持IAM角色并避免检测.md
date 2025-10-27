---
title: 劫持IAM角色并避免检测
url: https://mp.weixin.qq.com/s?__biz=MzI2NDQ5NTQzOQ==&mid=2247497140&idx=1&sn=8f9e6adf255931aa77dd5938000dfa89&chksm=eaa97d94dddef4827efb969cecc84c09024533bf1b899bc1bd1a66a616220a5b75a63f86e465&scene=58&subscene=0#rd
source: 火线Zone
date: 2022-11-03
fetch_date: 2025-10-03T21:40:25.400494
---

# 劫持IAM角色并避免检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsm68otVHLzfcbqn4BJqIV13W5tgfYZwarneBIrGoIianuetIDs3WIubA/0?wx_fmt=jpeg)

# 劫持IAM角色并避免检测

火线小助手

火线Zone

****本文为翻译文章，原文链接：https://frichetten.com/blog/hijack-iam-roles-and-avoid-detection/****

构建安全基础设施时的一个常见问题是身份验证。如何让您的服务器安全地使用其他服务进行身份验证？AWS提供了一种通过IAM角色管理资源身份验证的简单方法。IAM角色允许您向EC2实例提供一组AWS API的权限。这极大地使开发人员更容易，但也引入了一些独特的安全问题。

IAM角色将为我们管理凭据，并通过实例元数据服务定期轮换凭据，而不是将凭据存储在EC2实例本身上。此服务可在http://169.254.169.254获得，只能从EC2实例访问。然而，有一个小问题，攻击者可能会劫持它们，并以EC2实例的权限提出AWS API请求。更令人担忧的是，他们可以做到这一点，而无需触发警报。

劫持IAM角色密钥

作为攻击者，我们的目标是*通过*EC2实例到达实例元数据服务。两种常见的方法是通过服务器端请求伪造和系统上的直接代码执行。为了本文的目的，我们将演示SSRF路线。

首先，让我们创建一个名为“SecureS3Role”的IAM角色，该角色可以访问S3。然后，我们将创建一个EC2实例，并附加我们刚刚创建的角色。最后，让我们创建一个S3存储桶供我们查询。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsynYxmJgXcoiaKakaOfrXa92Yo1kz9SSHsxEV8XYXIUTjV7K5hxCtL7Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibswzlrjEd6oSvj6TwhWtUTmYZic9DJictENTiaRrSSPRCNJuYHEDvn2BVMQ/640?wx_fmt=png)

接下来，我们需要在 EC2 实例上创建一个易受攻击的服务。为此，我们将使用 Jobert Abma 为这篇HackerOne 博客文章创建的示例。这将创建一个容易受到 SSRF 攻击的简单 Web 服务器。

为了展示实际存在的漏洞，这里是通过 SSRF 获取我的网站（并以损坏的方式呈现它）。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsq4x5clxE5km2RPqChZTRGjHvJR1ZHzUaiaEgmWoib1Htv1VcpGngKJeA/640?wx_fmt=png)

我们的下一个目标是访问实例元数据服务并访问 IAM 角色密钥。这里有一个小技巧，我们需要识别与 EC2 实例关联的 IAM 角色的名称。值得庆幸的是，实例元数据服务将为我们提供这一点。只需联系以下端点。

```
http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

来自实例元数据服务的响应将为我们提供我们试图劫持的 IAM 角色的名称。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsrh1T43HHtPG739K8iaoK4G158CnaWwicQ2YzutWnSgOfqTs71gptsmzQ/640?wx_fmt=png)

只需将此名称附加到上一个查询中（确保在名称末尾包含“/”），您将获得以下结果。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibs5BqcIakrgS8z8ibfgg7Tb9ibFmmmGMZNNdNiacQiba67TrzDMcZSVBPSGg/640?wx_fmt=png)

（据我所知，泄露旧的IAM密钥没有风险，但它仍然让我紧张，因此为什么我混淆了结果）

我们现在拥有向AWS API发出请求所需的一切。有几种方法可以做到这一点，首先，您可以使用Pacu及其模块之类的东西来列举该角色的访问权限。或者，您可以打开终端提示符，并使用此处定义的“导出”来临时设置AWS CLI的特权。就我个人而言，我喜欢在AWS CLI中使用名称配置文件。这有几个优点，例如能够使用“--profile”标志在不同凭据集之间无缝交换（假设您的pentest进展顺利）。

规避检测

在使用这些密钥之前，让我们花点时间谈谈检测。由于这是一个常见的攻击，AWS的GuardDuty将检测到它。如果您不熟悉GuardDuty，这是AWS内置的威胁检测服务，将使用CloudTrail、VPC流日志和DNS日志检测常见攻击。

阻碍我们努力的检测特别称为UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration。如上所述，“此发现通知您尝试使用在AWS帐户中的EC2实例上创建的临时AWS凭据从EC2以外的主机运行AWS API操作”。

听起来很有效，对吧？因为我们只是滥用SSRF（因此，在EC2实例上没有立足点），听起来这会很快发现我们，防御者会很快关闭我们，对吗？对我们来说，好消息，对防守者来说，坏消息是，这里有一个相当严重的漏洞。前一段的描述是100%准确的。来自EC2之外主机的API操作是唯一触发这种情况的东西。因此，如果我们窃取这些IAM密钥并从另一个EC2实例（即使是我们拥有的实例）使用它们，则不会触发警报。

理解这一点的更好方法是，GuardDuty只检查源IP是否在EC2 IP地址范围内。只要是，警报就不会发出。Rhino Security的书《使用Kali Linux进行动手AWS渗透测试》中涵盖了这一点。如果您想更熟悉AWS渗透测试，我强烈建议您拿起它。在我看来，犀牛安全是AWS pentesting的行业领导者。

那么，我们如何在不被提醒的情况下利用我们的访问权限呢？首先，让我们在我们的帐户中创建一个新的EC2实例（注意：我使用AWS组织来确保所有请求都来自一个唯一的帐户）。

实例准备就绪后，我们登录，安装AWS CLI，然后使用我们从受害者那里偷走的IAM密钥创建一个新的凭据文件。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsXgj0ibXGxg1iaTffuHkriaT6qJmtHYgQf5jq8U0C8rhZBM2Sia1TP6a8Zw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsFAcWgWhxNNejDDsRSg5vW6w4UkLiaXe76RQD2QqAdcOSBAlg1cONV5w/640?wx_fmt=png)

接下来，让我们查询S3，看看我们可以访问什么。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsjU1tmOhTNIzYBbZpFRDYjXk5l5M5J721xMicmdQrIc9oc35icPcNiby1g/640?wx_fmt=png)

有趣的是，我们可以使用S3桶！不幸的是，对我们来说，它是空的。为了演示，让我们通过将文本文件上传到S3存储桶向防御者发送消息。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibs6ZPwdAZxnGVOzX55FsTJDUJthNR7OQE1VKstAgXQ0xddXjk5zaWw2Q/640?wx_fmt=png)

接下来，让我们等一下GuardDuty赶上。通常需要5-15分钟。为了这次示威的目的，我等了半个小时。这就是结果：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibsreMJsztVhDL52IrzUZOY4jianq7XXe84TckxxluKmEnXZevjOQzUHLQ/640?wx_fmt=png)

GuardDuty对我们来说，劫持IAM密钥并不明智

如果我们粗心大意，或者不知道这个开发后技巧，我们可能会将IAM密钥移动到我们自己的框中并运行API调用。

这将在GuardDuty中创建以下发现。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQ9ibGLmscd4dN0iblRlX99ibs3pN8UrcZJB4Spc7TdIiagAncH5icYgAYAJRvgr63pibvAdjTowCsOrqNg/640?wx_fmt=png)

终止实例

在结束本文之前，我想介绍的最后一个主题是以下问题：如果我终止实例会发生什么？IAM密钥还能用吗？

你的直觉可能是想“如果IAM键绑定到实例，而我终止了实例，那么它们应该在实例关闭后不久失效”。不幸的是，情况并非如此。这些密钥有效，并将持续到预定的到期时间。默认情况下，这是六个小时。因此，作为攻击者，即使实例被关闭，我们也可以窃取这些密钥并在其余生中使用它们。

**【火线Zone云安全社区群】**

进群可以与技术大佬互相交流

进群有机会免费领取节假日礼品

进群可以免费观看技术分享直播

识别二维码回复**【社区群】**进群

![](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaTf5R6lHvwO5WVsDRNyynwGQLM4tsY4nTvLyBeGWOtv4GficOaAWl9lhop3l4o7zahn4ib4R5YsW7QQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaTf5R6lHvwO5WVsDRNyynwGicdWbB2xBTFib0XzJO1ertfuF3jocicHB88Zxn0cfhATzCLHicKju6EaLw/640?wx_fmt=png)

火线Zone是[火线安全平台]运营的云安全社区，内容涵盖云计算、云安全、漏洞分析、攻防等热门主题，研究讨论云安全相关技术，助力所有云上用户实现全面的安全防护。欢迎具备分享和探索精神的云上用户加入火线Zone社区，共建一个云安全优质社区！

如需转载火线Zone公众号内的文章请联系火线小助手：hxanquan（微信）

![](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaTf5R6lHvwO5WVsDRNyynwG1OK03VUOHaicOibhdUZUxesnic7VYym0AxpYHDHMVghddk29FTUzjbFAw/640?wx_fmt=jpeg)

//  火线Zone //

微信号 : huoxian\_zone

![](https://mmbiz.qpic.cn/mmbiz_gif/CkzQxaHZX9KdW919vwagVwhCeicQPXuMGibHcf2WqiaFyvfy5p1oIk1C5SOdtTyLlQmOtEia7FMKicknJzGTmYLWb2Q/640?wx_fmt=gif)

点击阅读原文，加入社区，共建一个有技术氛围的优质社区！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaTIhKZJRWlQlI7jNqgnBiazDQfwhAfLQoWQege0A5eTVNn9ficjgQhsKznU8lFfWBpDfIaz1ia4Kr6HQ/0?wx_fmt=png)

火线Zone

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaTIhKZJRWlQlI7jNqgnBiazDQfwhAfLQoWQege0A5eTVNn9ficjgQhsKznU8lFfWBpDfIaz1ia4Kr6HQ/0?wx_fmt=png)

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