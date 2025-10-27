---
title: Apache Tomcat 漏洞导致服务器易受RCE攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521893&idx=1&sn=867f98595849107577a98fcaf043a177&chksm=ea94a70fdde32e19100b879ef6b6206b25f1ce4ef2d06f4980913cc6dfccd6675021781e9401&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-26
fetch_date: 2025-10-06T19:38:47.750960
---

# Apache Tomcat 漏洞导致服务器易受RCE攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQAziaFIBouMS7MoF4tVTYp7MV7cs2oJa7lGJRWVEPX2IrWOR0u92ibqU8PVWQvw3OGetM36woPmPYA/0?wx_fmt=jpeg)

# Apache Tomcat 漏洞导致服务器易受RCE攻击

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache 软件基金会 (ASF) 发布安全更新，修复了位于 Tomcat 服务器软件中的一个重要漏洞。该漏洞在一定条件下可导致远程代码执行 (RCE) 后果。**

该漏洞的编号是CVE-2024-56337，是因位于同样产品中另外一个严重漏洞CVE-2024-50379（CVSS评分9.8）的缓解不完整引发的，后者于2024年12月17日修复。

项目维护人员在上周发布安全公告提到，“在大小写敏感的文件系统上运行 Tomcat 的用户，启用了默认的伺服小程序写权限，可能需要额外的配置才能完全缓解CVE-2024-50379，具体取决于他们通过 Tomcat 使用的 Java 版本。”

这两个漏洞都是TOCTOU 条件竞争漏洞。当默认的伺服小程序启用获得写权限时，可导致在大小写敏感的文件系统上实现代码执行。Apache 在发布针对CVE-2024-50379的告警中提到，“在同样文件中加载之下的并发读取和上传可绕过 Tomcat 的大小写敏感检查并导致被上传的文件被当作JSP处理，导致远程代码执行后果。“

CVE-2024-56337 影响 Apache Tomcat 如下版本：

* Apache Tomcat 11.0.0-M1 至 11.0.1（在11.0.2或后续版本修复）
* Apache Tomcat 10.1.0-M1 至 10.1.33 （在10.1.34或后续版本修复）
* Apache Tomcat 9.0.0.M1 至 9.0.97（在9.0.98或后续版本修复）

此外，用户应根据所运行的 Java 版本，执行如下配置变更：

* Java 8 或 Java 11——直接明确地将系统属性sun.io.useCanonCaches设为false（默认为true）。
* Java 17 ——如已设置，则将系统属性sun.io.useCanonCaches 设置为false（默认为false）。
* Java 21 及后续——无需任何操作，因为系统属性已被清除。

与此同时，ZDI分享了位于 Webmin 中严重漏洞（CVE-2024-12828，CVSS评分9.9）的详情。该漏洞可导致远程攻击者执行任意代码。ZDI提到，“该缺陷存在于CGI请求处理中，是因为在使用由用户提供的字符串执行系统调用前，缺乏正确验证。攻击者可利用该漏洞在 root 上下文中执行代码。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Apache修复 Struts 2 中的严重 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521787&idx=1&sn=aa7443d590ca0182f0cbd4386c81152a&scene=21#wechat_redirect)

[Apache Avro SDK 中存在严重漏洞，可导致在 Java 应用中实现RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520994&idx=1&sn=0feb249fd14e6b8b07d5d6531f3287c2&scene=21#wechat_redirect)

[CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520886&idx=1&sn=d50fe47ebc8b4ad640aab8d8ead453e4&scene=21#wechat_redirect)

[Apache 修复严重的 OFBiz 远程代码执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520714&idx=2&sn=a3784b5b2245f1449edaefa3064d676f&scene=21#wechat_redirect)

[【已复现】Apache OFBiz 授权不当致代码执行漏洞(CVE-2024-38856)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=2&sn=db306ee3ac03c2a6708b7ae1cc72beaf&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/apache-tomcat-vulnerability-cve-2024.html

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