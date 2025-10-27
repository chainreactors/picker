---
title: Pwn2Own 2023迈阿密春季黑客大赛公布目标和奖金
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514911&idx=1&sn=edfb9902c59192447f4321dcba4b8d8d&chksm=ea948a75dde30363473d0e6eb0d684bc020aeaedc29885efc225876e18dd85ea482860ebc6b8&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-12-07
fetch_date: 2025-10-04T00:42:50.866747
---

# Pwn2Own 2023迈阿密春季黑客大赛公布目标和奖金

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTuVPuqrDOhQATDPibArtr44oAibWc96KiaoliaTWsWMOdicP0uymMxvicR5aPflyv3assukEom8hHf00zg/0?wx_fmt=jpeg)

# Pwn2Own 2023迈阿密春季黑客大赛公布目标和奖金

ZDI

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**2023年2月14日至16日，以工控系统为主题的Pwn2Own 大赛将在迈阿密举行。本次比赛共分四个类别，且与往年不同，反映了ICS行业不断变化的现状以及SCADA系统目前面临的威胁。这四个类别是：**

* **OPC UA 服务器**
* **OPC UA 客户端**
* **数据网关**
* **Edge系统**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44WugHhuwF565mY24HPfbmMGX3VULiaUVtvvojvRNoZsC3vshEfINrpvg/640?wx_fmt=gif)

**OPC UA 服务器类别**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

OPC UA 是独立于平台的、基于服务的架构，它将单个OPC Classic 标准的所有功能集成到一个可扩展框架中。OPC UA 是ICS 领域的通用转换协议。几乎所有的ICS产品都在使用该协议，在不同的厂商系统之间发送数据。虽然此前大赛曾列出OPC UA目标，但本次将分为“服务器”和“客户端”类别。

参赛选手必须在大赛网络中从笔记本对被暴露的目标网络服务发动攻击，造成拒绝服务条件、任意代码执行、凭据盗取或可信应用检查绕过的结果。应当证明“凭据盗取”的意义。在该场景下，参赛选手必须以一个可信任证书创建会话，但必须使用两种方式之一获得的凭据。这两种方式是：解密正在进行的会话中的密码，或利用漏洞检索服务器中存储的密码。该服务器将被配置一个 “admin” 账户，密码是12到16个字符长的随机密码。通过某种方式获得密码后，参赛选手必须以合法客户端的身份登录。不允许暴力攻击。

在“绕过可信任应用检查”场景下，参赛选手必须绕过创建安全信道之后的可信任应用检查。不允许通过操纵服务器安全配置的方式绕过检查。另外攻陷该目标还必须满足一些其它要求，具体可参加相关详细规则。

OPC UA 服务器类别的完整清单如下：

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTuVPuqrDOhQATDPibArtr44tUJnPZOxzJrq3xUNg1LdpYPrSDjsPsA3iaGYTEhibUNeksGYvESLwqrA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44WugHhuwF565mY24HPfbmMGX3VULiaUVtvvojvRNoZsC3vshEfINrpvg/640?wx_fmt=gif)

**OPC UA客户端类别**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

与“服务器”类别类似，“客户端”类别也有相关目标。再次强调的是，“绕过可信应用检查”的场景必须满足相关标准，具体可参见详细规则说明。

OPC US客户端类别的完整目标清单如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTuVPuqrDOhQATDPibArtr44jk8DdfjpI2A9LdBibV1TIot7FK8odRsQ2OeIH1IyBloxOI8PiaQJDYZg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44WugHhuwF565mY24HPfbmMGX3VULiaUVtvvojvRNoZsC3vshEfINrpvg/640?wx_fmt=gif)

**数据网关类别**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

该类别主要关注与不同协议下其它设备连接的设备。该类别中存在两款产品。第一款产品是 Triangle Microworks SCADA 数据网管产品。Triangle Microworks 是使用最为广泛的DNP3 协议栈。另外一款产品是 Softing Secure Integration Server。该产品官网介绍称，“Secure Integration Server 涵盖了全部的OPC UA 安全特性，赋能对最前沿安全解决方案的实现。”

参赛选手必须实现任意代码执行，才能通关。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTuVPuqrDOhQATDPibArtr44XCZDOcu6G8kEVicqgEQQyj1b2baQcms5d8qjlLao82bR1Aeibnua6ZLQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44WugHhuwF565mY24HPfbmMGX3VULiaUVtvvojvRNoZsC3vshEfINrpvg/640?wx_fmt=gif)

**Edge 类别**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

该类别是2023年新推出的类别，反映了Edge 设备经常用于ICS/SCADA网络中，管理和维护系统。本次大赛的唯一一个目标是AVEVA Edge Data Store。Edge Data Store 从远程无人资产中收集、存储和提供数据。

参赛选手必须实现任意代码执行，才能通关。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTuVPuqrDOhQATDPibArtr44ytGUmJtOYt2FNnlLL4KyoibyoicWOGICV1ib8VwBxAyHNe2AlKtEwNWCg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44WugHhuwF565mY24HPfbmMGX3VULiaUVtvvojvRNoZsC3vshEfINrpvg/640?wx_fmt=gif)

**“破解之王”称号获取规则**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTuVPuqrDOhQATDPibArtr44iaRva35OibIvs1roVLvrW4lAHWqFFib0icaa4iaNacVLLlsoIqI2RhB9XPg/640?wx_fmt=gif)

没有“破解之王”冠冕的Pwn2Own大赛是不完整的，2023年也不例外。获得该称号的参赛选手将获得6.5万个ZDI积分点（立即晋升为2024年的铂金级别，包括一次性奖励约2.5万美元）。按照规则，虽然每个类别中只有第一个成功演示的参赛选手才能获得全额奖励，但每次成功尝试均可获得全部积分点。由于参赛顺序是抽签决定，因此后续中签的参赛选手即使获得少量现金但仍然可以获得“破解之王”的称号。

另外，如果选手注册利用尝试却放弃，则会受到惩罚。如果在实际尝试前退出，则参赛选手的总积分将减去该尝试积分的一半作为惩罚。由于Pwn2Own 大赛通常是团体赛，因此同一家公司的所有参赛团队都会受到同等惩罚。

更多详情可见：https://www.zerodayinitiative.com/Pwn2OwnMiami2023Rules.html。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Pwn2Own 2022多伦多大赛确定目标和奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513770&idx=1&sn=5add0c86a1dc441c5bc3cced0fc8dff5&chksm=ea9487c0dde30ed6b5ac62548162b39108da3ebfc869c793d8bed447fd2dae4b566efc58e74f&scene=21#wechat_redirect)

[Pwn2Own 2022 温哥华大赛Master of Pwn 诞生](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511950&idx=1&sn=f710579aeb4b9fed2ecf99bb8b97b6a8&chksm=ea949ee4dde317f22ed67c20f1b31b15da09bd82cd1c5f1a49a1c7d62b9ab5eed9c7c8b7f9f0&scene=21#wechat_redirect)

[Pwn2Own 2022迈阿密大赛落幕  去年春季赛冠军蝉联Master of Pwn](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511504&idx=1&sn=8b4fc83a50611faeb66599c8ede17787&chksm=ea949cbadde315ac262fa80134e5021adec56b55766b3f478081e48a1fbaa319f2d4431dcdb7&scene=21#wechat_redirect)

[第15届Pwn2Own大赛确定目标和奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510120&idx=1&sn=afffed3852278ea1dbb00be370216df8&chksm=ea949902dde31014584b09eb99853d7c9aff5d6c2c00879d61c91dedaacd597e8b102e8d9149&scene=21#wechat_redirect)

[Pwn2Own 大赛赐我灵感，让我发现仨Oracle VirtualBox 漏洞，其中俩提权](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509396&idx=1&sn=09b11f725ded56f10eeadd369fc07c50&chksm=ea9494fedde31de8931022db99114fb8daa81e316236072167a1c183754fbf4da77c1d671e44&scene=21#wechat_redirect)

**原文链接**

https://www.zerodayinitiative.com/blog/2022/11/30/pwn2own-returns-to-miami-beach-for-2023

题图：Pexels License‍

文内图：ZDI

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