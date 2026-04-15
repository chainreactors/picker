---
title: Apache Tomcat 紧急修复多个漏洞
url: https://mp.weixin.qq.com/s/4hkGV7Iqj6ZD-hHXDfVZcg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:42:17.325295
---

# Apache Tomcat 紧急修复多个漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfU2ibD9GN9UYNb8M65zzpU91f5PGq1gT4S3kCXSOPgT0EoYaWoMRjb3bOLOW2Altv47BXRbNah69mM0BLjfmT55tlvPzlwoU37I/0?wx_fmt=jpeg)

# Apache Tomcat 紧急修复多个漏洞

Abinaya
Abinaya

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache****软件基金会发布紧急更新，修复了位于 Apache Tomcat 中的多个漏洞****。**

在这些漏洞中，其中一个是严重的补丁错误，可导致服务器面临拦截绕过的风险，其它问题与影响证书认证和填充预言机攻击有关。管理员必须立即更新部署，保护环境免受潜在利用。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXPQhkFTBS8Wyd0Bf1Ghcep8WpR83hzAsnU3815hkydBrDDDibGcjzia7Ds5lzZib90eAlC39HwvBZkghQIwTJicWGYUUAIyEdqCZk/640?wx_fmt=gif&from=appmsg)

**EncryptInterceptor 绕过与填充预言机攻击**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUHNCJ2T1LJ6icp2icwaia0tvVib7pXCU5GqdiawevxZxsvQAUAUpqfTyn1vdRaLkI40GdG3GomGxGuzGTm3kfw7zU6uicSfXSyE3LTE/640?wx_fmt=gif&from=appmsg)

其中最需紧急修复的问题源于一个有缺陷的安全补丁。最初，安全研究人员发现了“重要”级别的漏洞 CVE-2026-29146，其问题在于 EncryptInterceptor 默认使用了密码块链接 (CBC) 模式。该配置使服务器易受填充预言机攻击，可能导致恶意人员解密被截获的通信流量。

Oligo Security 公司的研究人员 Uri Katz 和 Avi Lumelsky 发现并报告了这一初始的加密弱点。为解决填充预言机威胁，Apache 发布了一轮初始更新。然而，该补丁引入了一个新的、同等严重的漏洞CVE-2026-34486。新漏洞由 striga.ai 的 Bartlomiej Dmitruk 发现，可导致攻击者完全绕过 EncryptInterceptor。由于初始补丁存在缺陷，运行中间更新版本的组织当前正暴露于该绕过机制的风险之下。

除了 EncryptInterceptor 相关问题外，Apache 还修复了一个“中等”严重程度的漏洞 CVE-2026-34500。该漏洞影响 Tomcat 中的在线证书状态协议（OCSP）检查功能。

在特定条件下，当使用外部函数与内存 (FFM）API 时，系统在 OCSP 验证期间会出现管理员已明确禁用的软失败行为。结果导致CLIENT\_CERT 认证未能按预期失败，产生了意外的认证行为，可能危及访问控制。

早稻田大学的研究人员 Haruki Oyama 发现并报告了这一证书验证错误（CVE-2026-34500）。这些漏洞影响多个 Apache Tomcat 分支，可导致 EncryptInterceptor 被绕过的有缺陷补丁（CVE-2026-34486）。具体影响以下版本：

* Apache Tomcat 11.0.20
* Apache Tomcat 10.1.53
* Apache Tomcat 9.0.116

这三个漏洞（包括最初的填充预言机攻击及证书验证失败）影响更多早期版本：

* Apache Tomcat 11.0.0-M1 至 11.0.20
* Apache Tomcat 10.1.0-M1 至 10.1.53
* Apache Tomcat 9.0.13 至 9.0.116

为全部修复这三个漏洞（包括有缺陷的 EncryptInterceptor 补丁及 OCSP 证书验证失败），管理员必须将其系统升级至最新的安全版本。

Apache 软件基金会强烈建议应用以下更新：

* 将 Apache Tomcat 11.x 部署升级至 11.0.21 或更高版本
* 将 Apache Tomcat 10.x 部署升级至 10.1.54 或更高版本
* 将 Apache Tomcat 9.x 部署升级至 9.0.117 或更高版本

运行已停止支持的旧版本Tomcat 的组织机构应立即迁移至仍在支持的分支，因为这些遗留系统不会收到针对填充预言机攻击及后续绕过漏洞的补丁。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[已存在13年的Apache ActiveMQ 严重漏洞可用于远程执行命令](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525686&idx=1&sn=51e7e391e06000c6fad494187241de39&scene=21#wechat_redirect)

[Apache Syncope 漏洞可用于劫持用户会话](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525048&idx=2&sn=58b797888d5027994282725ccb9f23de&scene=21#wechat_redirect)

[Apache Struts 2 严重 XXE 漏洞可用于窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524857&idx=1&sn=7d98b989a61c9b25103ccef5b0524560&scene=21#wechat_redirect)

[Apache StreamPipes 严重漏洞可用于获取管理员权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524778&idx=2&sn=17e6675d731950fb6f61f841bb161ef5&scene=21#wechat_redirect)

[速修复！Apache Tika 中存在严重的满分XXE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524600&idx=1&sn=fe09ca1df38ec9061341a2100567e69b&scene=21#wechat_redirect)

**原文链接**

https://cybersecuritynews.com/apache-tomcat-vulnerabilities-encryptinterceptor/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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