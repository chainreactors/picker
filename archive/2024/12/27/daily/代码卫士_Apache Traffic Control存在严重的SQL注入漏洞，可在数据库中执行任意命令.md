---
title: Apache Traffic Control存在严重的SQL注入漏洞，可在数据库中执行任意命令
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521906&idx=1&sn=9cb8ea9b9dbfb2a32eec80f9973d8cf1&chksm=ea94a718dde32e0eaffa96101dcd9b085998af672ffae70376866fc9a13fb6e62a0b045f8adf&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-27
fetch_date: 2025-10-06T19:37:33.301719
---

# Apache Traffic Control存在严重的SQL注入漏洞，可在数据库中执行任意命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR96r0VRImQA2AHuSVeFT8Dtx2zqicRFartDxuDkW4p30JEIj89zlmLibrXG0C4mwfQuzVeSMxqDlCw/0?wx_fmt=jpeg)

# Apache Traffic Control存在严重的SQL注入漏洞，可在数据库中执行任意命令

综合编译

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache 软件基金会 (ASF) 已发布安全更新，修复了 Traffic Control 中的一个严重漏洞CVE-2024-45387（CVSS评分9.9）。该漏洞可导致攻击者在数据库中执行任意SQL命令。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMR96r0VRImQA2AHuSVeFT8DayzibGhcpc3b5aeNxZX1yMuhYdpZpiaibxz63n8yoz2yiabNib7E9iaTkE2Q/640?wx_fmt=png&from=appmsg)

项目维护人员在一份安全公告中提到，“Apache Traffic Control <=8.0.1、>=8.0.0中存在一个SQL注入漏洞，可导致角色为 ‘admin’、’federation’、’operations’、‘portal’ 或 ’steering’ 的权限用户，通过发送特殊构造的PUT请求，在数据库中执行任意SQL命令。” 该漏洞已在 Apache Traffic Control 8.0.2中修复。

Apache Traffic Control 是内容交付网络 (CDN) 的一种开源实现，在2018年6月被宣布为一个顶层项目。

ASF还修复了Apache Hive 和 Apache Spark 中的另外一个严重漏洞CVE-2024-23945（CVSS评分8.7），它影响用于保护cookie完整性的 CookieSigner 安全机制，当信息验证失败时会暴露合法的cookie签名，可能导致恶意人员进一步利用系统。

此前，ASF还修复了位于Apache HugeGraph-Server 1.0至1.3版本中的一个认证绕过漏洞 (CVE-2024-43441)，该修复方案已在 1.5.0中发布。另外该基金会还修复了Apache Tomcat 中的一个重要漏洞 (CVE-2024-56337)，在一定条件下该漏洞可导致RCE后果。

建议用户将实例更新至最新版本，免受潜在威胁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Apache Tomcat 漏洞导致服务器易受RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521893&idx=1&sn=867f98595849107577a98fcaf043a177&scene=21#wechat_redirect)

[Apache修复 Struts 2 中的严重 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521787&idx=1&sn=aa7443d590ca0182f0cbd4386c81152a&scene=21#wechat_redirect)

[Apache Avro SDK 中存在严重漏洞，可导致在 Java 应用中实现RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520994&idx=1&sn=0feb249fd14e6b8b07d5d6531f3287c2&scene=21#wechat_redirect)

[CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520886&idx=1&sn=d50fe47ebc8b4ad640aab8d8ead453e4&scene=21#wechat_redirect)

[Apache 修复严重的 OFBiz 远程代码执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520714&idx=2&sn=a3784b5b2245f1449edaefa3064d676f&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/critical-sql-injection-vulnerability-in.html

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