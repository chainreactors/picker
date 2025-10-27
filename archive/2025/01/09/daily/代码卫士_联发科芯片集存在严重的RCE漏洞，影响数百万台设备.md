---
title: 联发科芯片集存在严重的RCE漏洞，影响数百万台设备
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522013&idx=1&sn=9f3081df1533336e5c1747667ca72291&chksm=ea94a7b7dde32ea1e597df0873feded0e252ea15614c48b51a0e8c61873427069a205f763194&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-09
fetch_date: 2025-10-06T20:10:59.772590
---

# 联发科芯片集存在严重的RCE漏洞，影响数百万台设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS1GvLA9XSWiaWQ5mhCbZ2OmUfWyXAl4xibOdbTmgbicH3TJD8FyjlBK7CveW4icA67UTmNyXXh86K0ZQ/0?wx_fmt=jpeg)

# 联发科芯片集存在严重的RCE漏洞，影响数百万台设备

do son

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**2025年1月份，联发科发布产品安全公告，修复了影响多款芯片集的安全漏洞。该公告详细说明了从智能手机、平板、物联网设备和智能电视等产品中发现的漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS1GvLA9XSWiaWQ5mhCbZ2OmgZVwf5M5VQgkcpL9edn7r1jgahZGlq8dZBL7uLj5fLnRia3arbkmRibw/640?wx_fmt=gif&from=appmsg)

其中最严重的漏洞是CVE-2024-20154，它是位于联发科现代固件中的一个栈溢出漏洞。该漏洞是一个严重的远程代码执行 (RCE) 漏洞，属于CWE-21，可通过将用户设备连接到受攻击者控制的恶意基站的方式利用。利用无需用户交互或权限提升。该漏洞影响40多款机型，包括MT2735、MT6767、MT6785、MT6873和MT6880。

该公告还重点强调了其它多个高危漏洞，包括位于电源管理（CVE-2024-20140）和数字化音频子系统（CVE-2024-20143、CVE-2024-20144和CVE-2024-20145）中的多个界外写漏洞。这些漏洞可导致本地提权，可能导致攻击者获得对敏感数据或系统功能的越权访问权限。

WLAN 驱动还修复了其它多个漏洞（CVE-2024-20146和CVE-2024-20148），可导致在M4U子系统的远程代码执行和界外写（CVE-2024-20105）后果，从而导致本地提权后果。

联发科已将这些漏洞告知设备制造商并提供了相应的安全补丁。强烈建议用户查看设备制造商发布的更新并尽快应用，缓解安全风险。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[联发科漏洞影响智能手机、平板、WiFi 等芯片集](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516937&idx=2&sn=65d504384b5ecc49b9c872f25971c1d9&scene=21#wechat_redirect)

[联发科固件现窃听漏洞，影响全球约三分之一的手机和物联网设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509419&idx=2&sn=2f9d2960d52a795a5895a28287b29b59&scene=21#wechat_redirect)

[谷歌在三星Exynos 芯片集中发现18个0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515956&idx=1&sn=01fe340192b1659e658210ae4b02ac97&scene=21#wechat_redirect)

[谷歌Titan M 芯片的这个严重漏洞，从1万跳涨到7.5万美元](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513590&idx=1&sn=ccdaf7e2571a6b7d793132cce9bcb946&scene=21#wechat_redirect)

[无线共存：利用蓝牙和 WiFi 性能特性实现芯片间提权](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509867&idx=2&sn=19471663d9505977efc3cef7e3a39044&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/cve-2024-20154-critical-rce-flaw-in-mediatek-chipsets-impacts-millions/

题图：Pexels License

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