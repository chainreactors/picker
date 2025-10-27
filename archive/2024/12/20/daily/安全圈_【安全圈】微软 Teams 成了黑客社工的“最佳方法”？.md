---
title: 【安全圈】微软 Teams 成了黑客社工的“最佳方法”？
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066717&idx=5&sn=12a7ff0e81888cf4e8950bc71072a080&chksm=f36e7fddc419f6cb58254a6747062882b84c53fcac2dd1f5da04e5b1d6582f3efb761f95c16d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-20
fetch_date: 2025-10-06T19:39:06.680090
---

# 【安全圈】微软 Teams 成了黑客社工的“最佳方法”？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgHibQfohsTenqicl4ia6QlKicicIdiaRWicficHWLCicHt8wdTDW1kK7cD83P4iaaE5eR1ia9LibI80LiaYic4TANw/0?wx_fmt=jpeg)

# 【安全圈】微软 Teams 成了黑客社工的“最佳方法”？

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

一项新的社会工程活动显示，大量攻击者利用微软Teams作为部署已知恶意软件DarkGate的手段。Trend Micro研究人员Catherine Loveria、Jovit Samaniego和Gabriel Nicoleta表示，“攻击者通过微软Teams电话进行社会工程，冒充用户的客户并获得远程访问他们系统的权利。攻击者未能安装微软远程支持应用程序，但成功指示受害者下载AnyDesk，这是一种常用于远程访问的工具。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgHibQfohsTenqicl4ia6QlKicic6bvDhq2ORstIaBb0DtBMjON1pNsZ3AIYG8qF2ticawCPWrcxcMpdkoA/640?wx_fmt=jpeg)

据网络安全公司Rapid7最近的报告，攻击者向目标的电子邮箱发送数千封邮件，然后通过微软Teams假装成外部供应商的员工接触目标。随后攻击者指示受害者在其系统上安装AnyDesk，远程访问随后被用于传送多个负载，包括凭据窃取工具和DarkGate恶意软件。

自2018年以来一直活跃的DarkGate是一种远程访问木马（RAT），后来演变为一种恶意软件即服务（MaaS）产品，其多种功能包括凭据窃取、键盘记录、屏幕捕捉、音频录制和远程桌面。过去一年针对DarkGate活动的分析表明，该恶意软件已通过使用AutoIt和AutoHotKey两条不同的攻击链进行分发。在Trend Micro检查的事件中，恶意软件可通过一个名为AutoIt脚本进行部署。

虽然在任何数据外泄活动发生之前攻击已被阻止，但这些发现表明攻击者如何使用多种初始访问途径传播恶意软件。因此安全专家建议组织启用多因素身份验证（MFA）、将批准的远程访问工具列入白名单、阻止未验证的应用程序，并彻底审核第三方技术支持提供商以消除语音钓鱼风险。

该事态进展正值各类网络钓鱼活动激增之时，这些活动利用各种诱惑和技巧欺骗受害者对信息进行泄露：

1. 一个大规模的YouTube定向活动中，假装成知名品牌，通过电子邮件联系内容创作者，试图进行潜在的推广、合作提案和市场合作，并敦促他们点击链接签署协议，部署Lumma Stealer。
2. 一场利用附带PDF文件的网络钓鱼邮件的活动，该PDF内含有一个二维码，用户扫描后会被引导到一个假的Microsoft 365登录页面以窃取凭据。
3. 利用Cloudflare Pages和Workers的信任设置假网站，模仿Microsoft 365的登录页面和假的CAPTCHA验证，号称为查看或下载文档。
4. 使用HTML电子邮件附件伪装成合法文档如发票或人力资源政策但含有嵌入的JavaScript代码，以执行恶意操作如引导用户访问钓鱼网站、窃取凭据，以及在修复错误的名义下诱使用户运行任意命令。
5. 利用可靠平台如Docusign、Adobe InDesign和Google Accelerated Mobile Pages (AMP)的电子邮件网络钓鱼活动，诱骗用户点击旨在窃取其凭据的恶意链接。
6. 声称来自Okta支持团队的网络钓鱼企图，以获取用户凭据并入侵组织系统。

针对印度用户的网络钓鱼信息通过WhatsApp分发，指示接收者安装恶意银行或用于Android设备的实用程序应用程序，能够窃取财务信息。攻击者也往往迅速利用全球事件，将其纳入到他们的网络钓鱼活动中，通常抓住紧迫性和情感反应操作受害者，诱使他们执行意外操作。这些活动还伴随有域名注册，使用与事件相关的关键词。

“备受瞩目的全球事件，包括体育锦标赛和产品发布，会吸引网络罪犯试图利用公众的兴趣，”Palo Alto Networks Unit 42表示，“这些罪犯注册欺骗性域名模仿官方网站，以出售假冒商品和提供欺诈服务。”

参考来源：https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html

***END***

阅读推荐

[【安全圈】2024年11月国内数据泄露及勒索事件汇总](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=1&sn=2eb63c63a1b65f13023240b667bf4930&scene=21#wechat_redirect)

[【安全圈】知名间谍软件公司 Paragon 被美国私募收购](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=2&sn=70318b76606cc51314d90fe11428590f&scene=21#wechat_redirect)

[【安全圈】APT组织开始大量抄袭红队先进的战术和工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=3&sn=05ca26f017e4cc04fbaee8e8adfb38d9&scene=21#wechat_redirect)

[【安全圈】Meta因6年前的数据泄露事件被罚款2.64亿美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=4&sn=3d0218c3c7069eebaad560f58a4eca10&scene=21#wechat_redirect)

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