---
title: 思科修复已遭利用的 Unified CM RCE 0day漏洞
url: https://mp.weixin.qq.com/s/9bLUTAz1KmsqpOTvd46AQg
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:27:19.800317
---

# 思科修复已遭利用的 Unified CM RCE 0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS78Rq3GiaAMZce95JhZO3ENx1S06dN2SO1zwtXt0rIVlxRPf7UEp6icDbLZqHYMwLuU8KfeOpHJKSQ/0?wx_fmt=jpeg)

# 思科修复已遭利用的 Unified CM RCE 0day漏洞

Lawrence Abrams
Lawrence Abrams

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**思科已修复位于 Unified Communications 和 Webex Calling中一个严重的RCE漏洞CVE-2026-20045。该漏洞已遭利用。**

该漏洞影响思科 Unified CM、Unified CM SME、Unified CM IM & Presence、思科 Unity Connection和 Webex Calling Dedicated Instance。

思科在安全公告中提到，“该漏洞是因为对 HTTP 请求中用户提供的输入验证不当造成的。攻击者可将一系列构造的HTTP请求发送到受影响设备基于 web 的管理接口，利用该漏洞。成功利用该漏洞可导致攻击者获得对底层操作系统的用户级访问权限并提权至 root。”

虽然该漏洞的CVSS 评分为8.2，但由于利用该漏洞可获得服务器的根访问权限，思科将其研判为“严重”级别。思科已发布软件更新和修复文件修复该漏洞，涵盖Unified CM、Unified CM SME、Unified CM IM & Presence、思科 Unity Connection和 Webex Calling Dedicated Instance。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS78Rq3GiaAMZce95JhZO3ENaTAhrZpibWZwDo8fz9fcGqgYibdlUJIsNDb9JQaJxOR9eibX8mNzcdn0w/640?wx_fmt=png&from=appmsg)

Cisco Unity Connection 发布：

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS78Rq3GiaAMZce95JhZO3ENhL9kkCNUcypITcAK1uxOObicvHTnptdqibmIRvUd5FdPXN8gTf1Ngic6w/640?wx_fmt=png&from=appmsg)

思科表示补丁对应不同的版本，因此在应用补丁前应先查看 README 文件。思科产品安全事件响应团队已证实称该漏洞已遭在野利用，因此督促客户尽快更新至最新软件版本。另外，思科提到不存在缓解该漏洞的应变措施，因此须立即安装更新。

美国网络安全和基础设施安全局 (CISA) 已将该漏洞纳入其必修清单，并督促联邦机构在2026年2月11日前部署更新。本月早些时候，思科还修复了一个已存在利用代码的 ISE 漏洞，以及一个自11月起就遭利用的 AsyncOS 0day漏洞。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[思科：速修复已出现 exp 的身份服务引擎漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524828&idx=1&sn=d0696191628f6b13a09be6edecbbec4d&scene=21#wechat_redirect)

[思科修复 Contact Center Appliance 中的多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524343&idx=2&sn=54f09a81eb6da8e9b06f5a17b8b70644&scene=21#wechat_redirect)

[速修复！思科ASA 两个0day漏洞已遭利用，列入 CISA KEV 清单](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524078&idx=1&sn=a668c49a8bfda90e1da60201307dc79b&scene=21#wechat_redirect)

[思科修复影响路由器和交换机的 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524071&idx=1&sn=31248d9d535baaa71b2ec67ceef617e8&scene=21#wechat_redirect)

[思科 Nexus 交换机中存在高危DoS 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523927&idx=1&sn=f6c3c875a12b2af4c8e6c00c06bc60d9&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisco-fixes-unified-communications-rce-zero-day-exploited-in-attacks/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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