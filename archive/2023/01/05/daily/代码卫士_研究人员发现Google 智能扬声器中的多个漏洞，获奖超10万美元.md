---
title: 研究人员发现Google 智能扬声器中的多个漏洞，获奖超10万美元
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515192&idx=2&sn=272bc0a3af1895e35d8757fc824d54e7&chksm=ea948d52dde3044428c3a85f3626292aa92baae3cad83b4c5ec41f5fe18285b316d2ca225fa6&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-05
fetch_date: 2025-10-04T03:04:41.974622
---

# 研究人员发现Google 智能扬声器中的多个漏洞，获奖超10万美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSfgiamuOvibLI4GvAxMV0iaOS0wRLorxw8j1KQOnbCCXicicJc29fnphGS9LbfPkMfZ9g2boHibbtXFadw/0?wx_fmt=jpeg)

# 研究人员发现Google 智能扬声器中的多个漏洞，获奖超10万美元

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSfgiamuOvibLI4GvAxMV0iaOSZFDPEATO5HUCkhA6zVrzYQbvT1EMHb3icWnMvH96hOUmGOY6Mx3gicnA/640?wx_fmt=gif)

**安全研究员 Matt Kunze 表示，谷歌因他负责任地提交了Google Home Mini智能扬声器中的多个漏洞，而获得10.7万美元的奖励。**

Kunze 表示，这些漏洞可被在无线范围内的攻击者在设备上创建恶意账户，之后执行多种操作。他表示，他能够使用这些账户在互联网上向设备发送远程命令、访问麦克风并在本地网上提出任意HTTP请求，从而可能直接暴露WiFi密码或访问其它设备。

Google Home智能扬声器支持声音命令，可通过Google Home 应用与安卓设备配对使用，还可使用户将账户连接到设备，发布被称为“例程”的多种命令。Kunze提到，“实际上，例程可使具有与设备连接账户的任何人远程发送命令。除了对设备的远程控制外，相连接的账户还可使用户安装‘动作’（小应用程序）。”他发现，攻击者能够通过篡改连接过程，在无需Google Home 应用的情况下，将账户连接到智能扬声器。为此，他在账户连接过程中拦截交换的HTTP请求，发现实际上它首先通过本地API获取设备信息（设备名称、证书和云ID），之后向谷歌服务器发送包含设备信息的连接请求。

Kunze 表示，他能够将连接请求payload中的字符串替换为恶意字符串，因此在设备上创建一个“后门”账户。他随后创建一个Python 脚本提取Google凭据和将IP地址作为输入，并借此将账户连接到所提供IP的Google Home 设备。”

利用该漏洞的攻击者可创建恶意例程，在设备上远程执行声音命令，其中包括一个“呼叫电话号码”的命令，可在精确的小时、分钟和秒处激活。该研究员指出，“实际上可使用该命令告知设备从麦克风向一些任意电话号码发送数据。”

**0****1**

**攻击场景**

Kunze 表示，其中一个可能的攻击场景是，用户安装攻击者的应用程序，检测Google Home设备并能够自动发布两个HTTP请求，将攻击者账户连接到设备。

他还发现，如果Google Home Mini 从本地网络断开，则会进入“设置模式”，创建自己的网络，让机主进行连接。在无线范围内不知道受害者WiFi密码的攻击者可通过监听MAC地址发现Google Home设备，发送非认证数据包，断开设备连接，之后连接到设备自身网络来请求设备信息。接着，攻击者可通过所获取信息，通过互联网将账户连接到设备。

Kunze 发现，谷歌向开发人员提供的功能可悲攻击者滥用于将WebSocket初始化到本地主机，之后将任意HTTP请求发送到受害者LAN上的其它设备。

该研究员还发布PoC代码，演示了攻击者如何使用这些漏洞监控受害者，在受害者设备上提出任意HTTP请求，甚至在所连接设备上读取或编写任意文件。

研究人员表示，谷歌通过拒绝连接未添加至Home的账户权限以及不再允许通过例程远程初始化“呼叫[电话号码]”命令，解决了这些漏洞。

虽然目前还可能取消认证Google Home 设备，但“设置模式”不再支持账户连接。智能扬声器中还增加了其它防护措施。

**0****2**

**获得奖励**

Kunze 表示，他最初在2021年1月将这些漏洞告知谷歌，当时谷歌表示这些行为是预料中的行为。他之后发送了更多信息，漏洞报告在2021年3月重新启动，他在4月获得奖励。一个月之后，谷歌提高了Nest和Fitbit设备的漏洞奖励金额，并颁发给他一笔奖金。

Kunze提到，“虽然我发现的这些漏洞现在看起来是显而易见的，但我认为它们实际上很细微。不是通过发送本地API请求控制设备，而是发送本地API请求来检索看似无害的设备信息，并结合利用云API来控制设备。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[研究员发现 Google Cloud 项目中的 SSRF 漏洞，获1万美元奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509349&idx=3&sn=d8378d91c487794e8bfe850aa68365f2&chksm=ea94940fdde31d19e8694f9162ea55a7fc85f53ad85b655e8d115c73c89b07d83f8967e0c81b&scene=21#wechat_redirect)

[搬起石头砸自己的脚？Google Home Hub 把自己踢出网络](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488415&idx=3&sn=f709e8a2e8657d51634bf8c28c6296a0&chksm=ea9722f5dde0abe367127d64d083fffcb8326921188f73cef17193d3317dc491074578629045&scene=21#wechat_redirect)

[Google Home Mini因硬件问题自动记录上传用户音频信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485456&idx=1&sn=05023a69ffe855bf6747f9941180c220&chksm=ea97397adde0b06caa2aa329cd34d763da9227da201713df2d1596d1ec5e55d06b66ab106377&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/researcher-says-google-paid-100k-bug-bounty-smart-speaker-vulnerabilities

题图：Pexels License‍

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