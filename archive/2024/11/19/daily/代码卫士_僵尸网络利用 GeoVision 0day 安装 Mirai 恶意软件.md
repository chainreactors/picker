---
title: 僵尸网络利用 GeoVision 0day 安装 Mirai 恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521513&idx=2&sn=667b6f9c61b6f2d2077659cd4d4cdc70&chksm=ea94a583dde32c95f18dabad1da69d1c1444aebf79a867a8ada6e4d24e51a03b28c8eb27076a&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-19
fetch_date: 2025-10-06T19:18:44.343879
---

# 僵尸网络利用 GeoVision 0day 安装 Mirai 恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeib2yhS3qATEln173987rmlDZcWlpaNpalcvEkk8TPFkHL2SPnKrUujMw/0?wx_fmt=jpeg)

# 僵尸网络利用 GeoVision 0day 安装 Mirai 恶意软件

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**一个恶意软件僵尸网络正在利用已达生命周期的 GeoVision 设备中的一个 0day 漏洞发动 DDoS 或密币挖掘攻击。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeibvxd5tc1COE4kUV1E9ZmEQiaHvJ1Wicapmnu7L9zKeSN2xB8WnBrRMYJg/640?wx_fmt=gif&from=appmsg)

该漏洞是CVE-2024-11120，是由 The Shadowserver Foundation 公司的研究员 Piort Kijewski 发现的。它是一个严重的（CVSS v3.1 9.8）的命令注入漏洞，可导致未认证攻击者在设备上执行任意系统命令。

中国台湾CERT 提醒称，“未认证的远程攻击者能够利用该漏洞注入并在设备上执行任意系统命令。另外，该漏洞已遭利用，我们已收到相关报告。”

该漏洞影响如下设备机型：

* **GV-VS12****：**2通道 H.264视频服务器，将模拟视频信号转换为数字流进行网络传输。
* **GV-VS11****：**单通道视频服务器，旨在为网络串流技术设计的数字化模拟视频。
* **GV-DSP LPR V3****：**专门用于许可证识别 (LPR) 的基于Linux 的系统。
* **GV-LX4C V2/GV-LX4C V3****：**为移动监控应用设计的小型数字录像机 (DVRs)。

所有这些机型已经到达生命周期，不再受厂商支持，因此不会发布安全更新。威胁监控平台 Shadowserver Foundation 报道称，大约有1.7万台 GeoVision 设备暴露在网络且易受CVE-2024-11120影响。

Kijewski 表示，该僵尸网络似乎是Mirai的一个变体，而后者常被用作 DDoS 平台的一部分或用于执行密币挖掘。多数（9100台）被暴露的设备位于美国，其次为德国 (1600)、加拿大 (800)、中国台湾 (800)、日本 (350)、西班牙 (300) 和法国 (250)。

一般而言，僵尸网络攻陷的迹象包括设备过热、响应缓慢或无响应，以及配置遭随意改变。如发现这些情况，则应重置设备，将默认管理员密码更改为强密码，关闭远程访问面板以及通过防火墙保护设备。在理想情况下，应用受支持机型替换这些设备，但如果无法实现，则应置于专门的LAN或子网隔离并密切监控。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[未修复的 Apache Tomcat 服务器传播 Mirai 僵尸网络恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517295&idx=1&sn=7f61402b12fbd46cb399a19ff93ca28e&chksm=ea94b505dde33c13b5e70aa9fdbdf02fc8dc58ac05568e19c5af6385458348da2464e9fa4c8b&scene=21#wechat_redirect)

[Spring4Shell 漏洞已遭Mirai 僵尸网络利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511304&idx=2&sn=157f1ecf43e8268adf1d188b3bdab4db&chksm=ea949c62dde31574804aed120e44fb4c92f7d939f027277177016748f7508403563363b53f6e&scene=21#wechat_redirect)

[警惕！Mirai 新变体带着11个新利用攻击企业设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489462&idx=2&sn=5e37f9a866349fb70248e1ccd2fdf1ba&chksm=ea9726dcdde0afcae9fa9f8641fc9203bcc29806396b12da2e07bd9d4c05bb0681ad834fbf07&scene=21#wechat_redirect)

[Mirai 作者之一被罚 860 万美元](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488370&idx=2&sn=15fe33af93617e0a388f3cceadc58a75&chksm=ea972218dde0ab0e5537a684b60d50e1487e754bef2147349c2b4607bf32ee99bba50b1e1064&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/botnet-exploits-geovision-zero-day-to-install-mirai-malware/

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