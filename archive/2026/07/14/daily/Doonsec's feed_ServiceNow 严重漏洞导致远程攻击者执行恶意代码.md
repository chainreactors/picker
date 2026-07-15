---
title: ServiceNow 严重漏洞导致远程攻击者执行恶意代码
url: https://mp.weixin.qq.com/s/FiX2Pwt2f90bbapLGN6tUA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:53.684235
---

# ServiceNow 严重漏洞导致远程攻击者执行恶意代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfVAImjUm5Qn8qtAickyO6TiaXCG6GLlNI19CNazdubibvxcKVqVAzwbibJPP6pvUKVAbOpvoCUicHld1BgvmibLK5hgOYJUTCbqsbMas/0?wx_fmt=jpeg)

# ServiceNow 严重漏洞导致远程攻击者执行恶意代码

Abinaya
Abinaya

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**ServiceNow****披露并修复了位于****AI****平台中的一个严重的沙箱逃逸漏洞（****CVE-2026-6875****），可导致未经身份认证的攻击者在受影响的****ServiceNow****环境中执行代码。该漏洞影响托管和自托管****ServiceNow****部署版本。**

ServiceNow 被企业广泛用于IT服务管理、工作流自动化、客户运营、安全运营和内部业务流程。ServiceNow 公司表示，该漏洞可导致攻击者规避平台限制条件并在特定情况下绕过平台预设的限制并执行代码。由于利用无需进行身份认证，因此该漏洞可导致尚未收到安全更新的 ServiceNow 实例遭暴露。

成功的远程代码执行攻击可使攻击者破坏工作流、访问敏感数据、修改记录或将受陷环境作为进一步实施攻击活动的入口点。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXZHRDGr1d58q3PBjqDj2c4ljSfulyJkC6fP0Cwn6ibSguO7s1jeJWsapCPbr6kAzIMdOffp7hMk6M0NibKvdJ2kSzEl8DBB0E4E/640?wx_fmt=gif&from=appmsg)

**漏洞补丁和更新**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUiaT9924JAZ3UQILEF6xx6vjiaaicAuWhWvUnk5ARm9Y1Nmv76xBzW2B6rceYeru42mXNQScP6SZKrpUTyz6JmvL7ESdPxGDzn7I/640?wx_fmt=gif&from=appmsg)

该漏洞位于 ServiceNow AI 平台中。不过ServiceNow 公司并未发布关于漏洞底层根因的技术详情。该公司在2026年7月13日发布安全公告，仅将技术详情告知数量有限的客户，以便客户能够在攻击者开发出可靠利用前打补丁。

ServiceNow 已将安全更新部署到所托管的实例中。该公司还为自托管客户和合作伙伴提供了相关更新。自行管理ServiceNow环境的组织应审查当前的系列版本，并尽快安装相应的补丁或升级到已修复的版本。该问题已在Brazil Early Access和Brazil General Availability版本中修复。对于Australia版本，该漏洞已在Australia Patch 2中得到解决。Zurich客户应安装Zurich Patch 7b或Zurich Patch 9。Yokohama用户可通过Yokohama Patch 12 Hot Fix 1b或Yokohama Patch 13获得保护。ServiceNow表示，目前尚未发现CVE-2026-6875遭在野利用的情况。

然而，公开披露严重的未经身份验证的远程代码执行漏洞，很快会引起安全研究人员和恶意攻击者的关注。因此，即使尚未发现可疑活动，各组织机构也应将该问题视为紧急事项。管理员应确认ServiceNow实例是由ServiceNow托管还是部署在自托管环境中。托管客户应验证平台更新是否已应用。同时，自托管管理员应查阅ServiceNow的安全维护指南和补丁状态。安全团队还应在更新后监控管理活动、异常集成、意外的工作流变更以及可疑的API行为。

用户可通过CVE.org获取CVE记录，补丁和维护的更多信息可在ServiceNow公告KB2930717和KB2930740中查阅。及时修复仍是防范潜在漏洞利用的最有效防御措施。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Langflow 严重漏洞可导致未认证远程代码执行后果](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526389&idx=2&sn=a692a0a18f59def9c6fa164c8ac2ccec&scene=21#wechat_redirect)

[Libssh2 严重漏洞可导致攻击者执行远程代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526367&idx=1&sn=75309fe9323e5ed5c44c05f759fa40d9&scene=21#wechat_redirect)

[Fortra 访问管理器漏洞可导致远程命令注入攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526330&idx=2&sn=634ff7aee7d1db205f90e279a8c74f64&scene=21#wechat_redirect)

[Comet Backup 服务器严重漏洞可导致客户数据被远程泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526149&idx=2&sn=58f20be37a8c71d4f0e7d16aa1e8f1b5&scene=21#wechat_redirect)

[NGINX 新漏洞可导致远程攻击者触发恶意代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526088&idx=3&sn=353fe1e4d9d79dec6b4cce44a35da5fe&scene=21#wechat_redirect)

**原文链接**

https://cybersecuritynews.com/servicenow-remote-malicious-code/

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