---
title: cPanel：LiteSpeed Web Server 企业版严重漏洞可导致提权
url: https://mp.weixin.qq.com/s/Hg5KbPZeA24zDtKcHWI9Pg
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:55:00.745999
---

# cPanel：LiteSpeed Web Server 企业版严重漏洞可导致提权

# cPanel：LiteSpeed Web Server 企业版严重漏洞可导致提权

Swati Khandelwal
Swati Khandelwal

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

**cPanel****在****9****月****14****日发布安全公告提醒称，****LiteSpeed Web Server****企业版中的一个严重漏洞可能让低权限网站用户在共享托管服务器上获得****root****访问权限。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVhpJa6QGOeI7QTpUyBVC4qSOSQNUD6Rf2IQ56giaxYYALMI1UQS2JUfcfmApcciamhA0eCSyRhdhWyOqic1KVkApvcNXRsibGFwYw/640?wx_fmt=gif&from=appmsg)

该公告提到在这类服务器上，许多客户的网站运行在同一台机器上，拥有其中一个托管账户的攻击者可利用该漏洞访问或篡改其它网站以及服务器本身。cPanel 表示已收到有关该漏洞的通知，该漏洞影响 6.3.7 之前的版本，并敦促管理员更新到LiteSpeed 于 9 月 11 日发布的6.3.7版本。

cPanel 表示，该漏洞可绕过用于隔离托管账户的控制机制如 CageFS。CageFS 是 CloudLinux 的一个工具，为每个托管账户提供受限的文件系统视图，使其无法看到其他账户或服务器的配置文件。

cPanel 的公告和 LiteSpeed 的发行说明均未描述该漏洞如何运作。LiteSpeed 在 6.3.7 版本的公告中称其为包含“安全改进、错误修复及更多内容！”的版本。其更新日志列出了三项安全变更，但没有提到权限提升漏洞，两家公司都没有公开说明哪项变更修复了该漏洞。该公告没有 CVE 标识符或严重性评分，9 月 15 日对已发布 CVE 记录的检查也未发现与该漏洞相关的记录。公告也没有说明该漏洞是否已被利用。

cPanel 和 LiteSpeed 均给出安装 6.3.7 版本的相同命令：

```
/usr/local/lsws/admin/misc/lsup.sh -f -v 6.3.7
```

由于6.3.7版本可能不会自行安装，因此手动更新很重要。LiteSpeed 表示，该版本进入自动更新之前“可能会有一些延迟”。截至 9 月 15 日，LiteSpeed 的下载页面仍将 6.3.6 列为稳定版本，同时列出的还有 7 月的 6.4.0 预发布版本（RC1），其更新日志并未列出这三项安全变更。cPanel 的公告并未说明 6.4.0 候选版本是否受影响。LiteSpeed 的更新文档称，使用此命令强制指定版本会阻止服务器遵循其稳定更新通道，管理员之后可以通过运行 touch /usr/local/lsws/autoupdate/follow\_stable 来恢复自动稳定更新。

cPanel 的公告和 LiteSpeed 的发行说明均未对无法立即更新的服务器提供应变方案，也并未提供用于检查服务器是否已被攻击的指标。该公告仅提到 企业版，没有涉及 LiteSpeed 的开源服务器 OpenLiteSpeed；截至 9 月 15 日，LiteSpeed 尚未为后者发布匹配的更新。

这是自今年5月以来发布的第三次cPanel 服务器LiteSpeed 软件漏洞报告，它们可让托管账户获得 root 访问权限，但这是第一次出现在 Web 服务器本身。5 月和 6 月，LiteSpeed 披露了用户端 cPanel 插件中的两个类似漏洞，CVE-2026-48172 和 CVE-2026-54420，称两者均遭活跃利用，并在插件中予以修复。CISA后续将这两个漏洞纳入其必修清单。

LiteSpeed、cPanel 和 CloudLinux尚未回应与该漏洞相关的其它问题。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[cPanel 新漏洞可导致单个托管账户接管整个服务器，影响所有版本](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247527085&idx=2&sn=401518b5ad719760f10f3a256a2c352a&scene=21#wechat_redirect)

[cPanel 存在严重漏洞，可导致托管客户以数据库 root 身份执行 SQL](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526822&idx=1&sn=fa6cba51e606ca4da3062cfdb3a53640&scene=21#wechat_redirect)

[cPanel 修复三个新漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525970&idx=1&sn=722d2a9f2b63e4126c12f9ca480729ea&scene=21#wechat_redirect)

[刚刚，cPanel紧急修复影响所有受支持版本的认证漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525909&idx=2&sn=80fc4007516f0fcfc9072f775b3c330a&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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