---
title: 速修复这些Netgear Orbi路由器漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516017&idx=1&sn=5e3c7c8f862132892592ddc4374aa0d8&chksm=ea948e1bdde3070dc62e414af95b3217979ff5f063fd707703f34555416351b9698de9b19f0e&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-24
fetch_date: 2025-10-04T10:29:53.451961
---

# 速修复这些Netgear Orbi路由器漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTawvfLWEDEbz6tTcTPHPDIAcOKuTvLNX9qCibDWk54KlnqZOmYicBRqUQuC3VJkpEzgnfxoapEFXxw/0?wx_fmt=jpeg)

# 速修复这些Netgear Orbi路由器漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTawvfLWEDEbz6tTcTPHPDIsCcIguWqrfo4ZKoE3LZdk3Sth2557MU3ib4elNocyhNGBZvlblA7FDA/640?wx_fmt=png)

**思科Talos团队发布了Netgear Orbi 740系列路由器和扩展卫星中多个漏洞的PoC exploit，其中一个漏洞是严重的远程命令执行漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTawvfLWEDEbz6tTcTPHPDIS1cw3lN1uhOlCibFTAIMfPkAJSwArquGqJUeJq1dicIWKw7CUnP4v7uw/640?wx_fmt=png)

Netgear Orbi 是适用于家庭用户的流行网络无线网格系统，可同时最多为5000至1.25万平方英尺之间的空间的40台联网设备提供强大的覆盖率和吞吐量。

思科研究人员在2022年8月30日向Netgear 报告，并督促用户将固件升级至2023年1月19日发布的最新版本4.6.14.3。

**Orbi 漏洞**

第一个也是最严重的漏洞是CVE-2022-37337（CVSS评分9.1），是位于Netgear Orbi 路由器访问控制功能中的一个可利用命令执行漏洞。攻击者可利用公开可访问的管理控制台，向该易受攻击的路由器发送特殊构造的HTTP请求，在设备上执行任意命令。

第二个漏洞是CVE-2022-38452，是位于路由器telnet服务中的高危远程命令执行漏洞，该漏洞的利用要求合法凭据和MAC地址。这是Netgear公司在一月固件更新中发布的四个漏洞中唯一一个没有修复的漏洞，因此目前尚未修复。

第三个漏洞是CVE-2022-36429，是位于Netgear Orbi 卫星后端通信功能中的一个高危命令注入漏洞，该功能与路由器相连以拓展网络覆盖。攻击者可向设备发送特殊构造的JSON对象序列，利用该漏洞。不过成功攻击需要获取管理员权限。

第四个漏洞CVE-2022-38458是一个影响Netgear Orbi路由器远程管理功能的明文传输问题，可导致中间人攻击，从而导致敏感信息遭泄露。

在发布这些漏洞详情时，思科并未发现它们遭利用的迹象。不过考虑到CVE-2022-37337的PoC已公开，攻击者可尝试查找配置不当且公开可访问的路由器实施利用。

好消息是这些利用要求本地访问权限、合法的登录凭据或要求管理员控制台可公开访问，使得漏洞难以遭利用。然而，从Shodan 快速搜索就可发现近1万台Orbi设备可从互联网公开访问，且多数位于美国。如果用户使用了管理员凭据，则可能遭攻击。

虽然Orbi确实支持自动安装更新，但BleepingComputer表示在一台Orbi设备上新固件并未自动安装，而改设备运行的是在2022年8月发布的软件。因此Netgear Orbi 750系列设备机主应当手动检查运行的是否是最新版本，如不是，则应尽快升级固件。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[速修复！Netgear 61款路由器和调制解调器中存在多个严重的预认证RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509274&idx=1&sn=216d21cb49d9020ea39826423b5b770f&chksm=ea949470dde31d664a63ac275e756e4df4883d2004af06b5d54e40dead7831e4e50c99fd17ae&scene=21#wechat_redirect)

[速修复！Netgear交换机曝3个严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507695&idx=1&sn=67fa6945d9b69defca30c5a951a27a8e&chksm=ea94ef85dde36693e4bd8e37deaa4e6f7f1c2659397805ea5adf422c7f39404fcf27fef53d39&scene=21#wechat_redirect)

[Netgear业务交换机被曝15个漏洞，有些不修复](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502189&idx=2&sn=66f26ac8db257384c42ee8ff229a4fe5&chksm=ea94f807dde37111b2b4868642cb4e6a40d34493a8c7611cadffcd1e307f6fc268bc8ba3e1a0&scene=21#wechat_redirect)

[这个严重 0day 可导致79款 Netgear 路由器遭远程接管，无补丁](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493584&idx=1&sn=6ca40eec9e17037795de2fa93e47e08d&chksm=ea94d6badde35fac49d80a9ba9d278abfac273c66ffd7abcc6de5a95b5aa5d6287a531778a5b&scene=21#wechat_redirect)

[Netgear修复路由器和交换机中的RCE缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485536&idx=5&sn=5730b1e1c2cf4abd50494ea5a3ec07fb&chksm=ea97390adde0b01ca33460a4569c67e3f27d00969bc4cc863fc6bb959c1ff1848bfb7034cb71&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/poc-exploits-released-for-netgear-orbi-router-vulnerabilities/

题图：Pexels License

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