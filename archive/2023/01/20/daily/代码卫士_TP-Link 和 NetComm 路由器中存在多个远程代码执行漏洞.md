---
title: TP-Link 和 NetComm 路由器中存在多个远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515346&idx=1&sn=3d1acdb97283a7d9606c441b9ca5eb27&chksm=ea948db8dde304aea15c93964eceaeb7328f9d6fd59ebe7ea979943fac2a6e48c8fd1b9087c2&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-20
fetch_date: 2025-10-04T04:23:11.252873
---

# TP-Link 和 NetComm 路由器中存在多个远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTemklgaj68k6nObQicJq7m7F85JX62ue7Jea1bTJibaEPSo6HClsTgvGdkBFWOs2icMkMqXIXhXSXjA/0?wx_fmt=jpeg)

# TP-Link 和 NetComm 路由器中存在多个远程代码执行漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**TP-Link 和 NetComm 路由器机型中存在多个漏洞，可用于实现远程代码执行 (RCE)。**

TP-Link WR710N-V1-151022和Archer-C5-V2-160201 SOHO 路由器中存在两个漏洞，可导致攻击者执行代码、破坏设备或猜测登录凭据。

第一个漏洞是CVE-2022-4498，是在HTTP基本认证模式下接受的构造数据包引发的堆溢出漏洞。攻击者可利用该漏洞引发拒绝服务条件或RCE。第二个漏洞是CVE-2022-4499，是因为一个HTTPD函数易受侧信道攻击而导致的，可使gong记者猜测用户名和密码字符串的每个字节。

卡耐基梅隆大学CERT/CC提到，TP-Link已在2022年11月得到关于这些漏洞的通知但目前两个漏洞仍未修复，“这些SOHO设备是由TP-Link出售的，它们的最新固件版本已在2023年1月11日可用，目前其中存在两个漏洞。”

在另一份安全公告中，该CERT/CC 提醒称，NetComm NF20MESH、NF20和NL1902路由器机型中存在两个漏洞，该厂商已修复。

第一个漏洞CVE-2022-4837是一个缓冲区溢出漏洞，可导致应用崩溃。第二个漏洞CVE-2022-4847是一个认证绕过漏洞，可导致对内容的越权访问。安全公告指出，“组合利用这两个漏洞可使远程未认证攻击者执行任意代码。攻击者可首先获得对受影响设备的越权访问，之后利用这些入口点获得对其它网络的访问权限或者攻陷从内网所传输数据的可用性、完整性或机密性。”

2022年12月，NetComm发布固件更新，修复了这些漏洞。

一个月前，该公司指出，这些漏洞是由其芯片提供商博通的代码中引入的，然而后者声称代码并不易受影响。博通公司指出，“尝试在博通参照代码中复现该问题时，客户证实称该漏洞是由不受博通控制的软件变更造成的。”

本月早些时候，发现了这两个漏洞的研究员 Brendan Scarvell 发布相关漏洞详情以及PoC 利用。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[TP-Link 路由器被曝严重漏洞：无需密码即可登录](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247491921&idx=1&sn=ff747109c1daa0e227fdebb93dfb47bd&chksm=ea94d03bdde3592d75c69d82c32070566c30aaa67321a6bd8b613cfd525ae38688db073d635c&scene=21#wechat_redirect)

[TP-Link WiFi 扩展器被曝存在严重的 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247490231&idx=2&sn=a755875c26dbf80ca944a86a6034cbeb&chksm=ea972bdddde0a2cb3ce9b4c573a5767fb550f59a45fad7ff5da4179dc757810ec7a3d443e01f&scene=21#wechat_redirect)

[TP-Link 修复 SOHO 路由器中的远程代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488569&idx=3&sn=b629d305a12b7d97c3af6139f9face62&chksm=ea972553dde0ac45f6e6d3a3ed4427c1f71adcddbc89d333f83d2f88e32e89d1164d0eece89e&scene=21#wechat_redirect)

[InHand工业路由器中存在多个漏洞，导致OT网络易受攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515321&idx=2&sn=21b3cad712a7f1267e677ed2354c90e9&chksm=ea948dd3dde304c5320dac4c1f977dc1871ae5bfa1be6fe37d8cad7f7662c9d4936faa0df6c6&scene=21#wechat_redirect)

[思科不打算修复SMB路由器中严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515297&idx=2&sn=460499858dd7355f4569e49b316d18b4&chksm=ea948dcbdde304dd13d7b674af7f35b59b16dd02b31770de7ae9738688f20bcc072fae10dce9&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/remote-code-execution-vulnerabilities-found-tp-link-netcomm-routers

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