---
title: 【安全圈】研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066063&idx=3&sn=fd139cbc62a8b20cf6ae19f09c9b869f&chksm=f36e7d4fc419f459b22649e69eb0e69a8f7ce49a075b11ead7d774157b77dfd51ba8497355f6&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-19
fetch_date: 2025-10-06T19:19:02.591820
---

# 【安全圈】研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaoJcEW2HSZ5j9I5YeEKmia7QIrbbQw330G3libu6bF92e1rhhnUibky4J5mOaBEVHTgS6V3rGouXic6w/0?wx_fmt=jpeg)

# 【安全圈】研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络钓鱼

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaoJcEW2HSZ5j9I5YeEKmia7nSibnE6UcB2IF4UvPFbC996lN69Yq3AnJEIv8WDgfKvL8fO6rAcf9Dw/640?wx_fmt=other&from=appmsg)

Perception Point 的最新发现揭露了一种先进的两步式网络钓鱼技术，该技术利用 Microsoft Visio 文件（.vsdx）和 SharePoint 发起极具欺骗性的凭证盗窃活动。

Microsoft Visio 文件传统上用于绘制流程图和网络地图等专业图表，但现在已被武器化。Perception Point 的报告显示：“在最近的网络钓鱼活动中，Visio 文件正被用来传递恶意 URL，在两步攻击路径中创建一个欺骗性传递点。”

这种方法利用了用户对 SharePoint 和 Microsoft Visio 等熟悉平台的信任。通过在被入侵的 SharePoint 账户托管的 .vsdx 文件中嵌入恶意 URL，攻击者可以绕过许多标准安全措施。

攻击分为两步，旨在逃避检测和利用用户行为：

1. 第一步：诱惑
   攻击者首先利用被攻破的电子邮件账户向目标发送网络钓鱼电子邮件。“这些电子邮件因其来源而看似合法，通常包含令人信服的叙述，如紧急商业提案或采购订单。”这些电子邮件可能包含一个链接或 .eml 文件附件，其中包含一个指向 SharePoint 托管的 Visio 文件的 URL。
2. 第二步：陷阱
   点击链接后，受害者会重定向到一个托管 Visio 文件的受攻击 SharePoint 页面。该文件包含一个嵌入式 “行动召唤 ”按钮，通常标注为 “查看文档”。受害者被指示按住 Ctrl 键并点击，这个简单的操作可以绕过自动安全系统。一旦点击，嵌入的 URL 就会将用户引导到一个伪造的 Microsoft 365 登录页面，该页面的目的是收集凭证。“该报告解释说：”与链接互动会将受害者重定向到一个冒充 Microsoft 365 的钓鱼页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaoJcEW2HSZ5j9I5YeEKmia79SMcL2TNwuWWrK6LtZStHj9J62mf4hKV6sHicyopQRibBWRmQ3K4l06w/640?wx_fmt=jpeg)

图片 感知点 X-Ray

这种网络钓鱼技术结合了复杂的技术和心理操纵。通过要求用户执行按住 Ctrl 键等手动操作，攻击者可以躲避自动电子邮件安全扫描仪和检测工具。此外，合法品牌（包括组织徽标）的使用也增加了恶意 Visio 文件的可信度。

Perception Point 的研究人员观察到，使用这种方法的攻击明显增加，目标是全球数百家组织。报告警告说，这些活动 “旨在逃避检测和利用用户的信任”，强调了在企业环境中保持警惕的重要性。

***END***

阅读推荐

[【安全圈】耗时2个月，四川小伙用专业知识把自己“送进去”了。](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=1&sn=fcc2314e273fd8cbd7197bf86dbb628e&chksm=f36e7cb8c419f5ae9d4910c6a41e61dc61e3b3141c312e2229cc7b013421e198fac317742acb&scene=21#wechat_redirect)

[【安全圈】安全公司曝光黑客利用 Office 已知漏洞散播 Remcos   RAT 木马程序](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=2&sn=cf11d094cb7fc2770df2100227dc34db&chksm=f36e7cb8c419f5ae9268e1d2eb9675ef94bccbcfe66627cb209b0883944215f205a8d17b7028&scene=21#wechat_redirect)

[【安全圈】物联网云平台 OvrC 曝一系列漏洞，黑客可远程执行恶意代码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=3&sn=628c0be39463e5a5db076252eae42974&chksm=f36e7cb8c419f5ae9694e18d60dde2a26e6a3cdec1633acf1fe266e96be9e59868eaad6f37a5&scene=21#wechat_redirect)

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