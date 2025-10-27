---
title: Veeam修复严重漏洞，可攻陷备份基础设施
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515885&idx=3&sn=ffefe13a8f5da2c680df756b9e641cfd&chksm=ea948f87dde30691fda5efbd07f068606a775eb6e6e596b39f44c7f1cd843a4c64a24c1a88a7&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-11
fetch_date: 2025-10-04T09:16:23.487580
---

# Veeam修复严重漏洞，可攻陷备份基础设施

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSETROYJryuoTIGLozibBpYdG8dv5HLPhLKdfBqZ3bXnWqgJNXQm9dWPlJcyIkZaEzhnwOt3uaGgMA/0?wx_fmt=jpeg)

# Veeam修复严重漏洞，可攻陷备份基础设施

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSETROYJryuoTIGLozibBpYdqnOY0kFYI6355vzpI9XjLVCCzziclkduic2CfgYXic8mcA7sjDJbTn9rA/640?wx_fmt=png)

Veeam 督促客户修复影响其Backup & Replication  (VBR) 软件的高危Backup Service 漏洞 (CVE-2023-27532)，影响所有的VBR版本。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSETROYJryuoTIGLozibBpYdSkTB8nLENXmia3FE3hjdmGXQEd4fFAYxNZV4OhwHCViarUbibUYgIK72A/640?wx_fmt=png)

未认证攻击者可获得存储在VeeamVBR配置数据库中的加密凭据，利用该漏洞访问备份基础设施主机。Veeam 公司发布公告称，根因在于 Veeam.Backup.Service.exe（默认在TCP端口9401上运行）可使未认证用户请求加密凭据。

Veeam 公司在本周二向客户发布邮件称，“我们以为V11和V12发布补丁缓解该漏洞，建议立即更新。如用户并非Veeam 环境的当前管理人员，请将此邮件转发给适当人选。”该公司为V11和V12发布安全更新解决该漏洞，并建议使用更老旧版本的客户首先更新至受支持的这两个版本之一。

**已有应变措施**

Veeam 公司还为无法立即部署补丁的客户发布临时修复方案。

为阻止攻击向量和易受攻击的服务器遭潜在利用尝试，用户也可使用备份防火墙拦截对端口TCP9401的外部连接。

不过值得注意的是，该应变措施应该仅能用于非分布式的Veeam 环境中，因为它还影响mount服务器与VRB服务器的连接。该公司提醒称，“漏洞披露后，威胁行动者将逆向补丁了解漏洞并在未修复的软件版本上实施利用。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Veeam 数据备份解决方案修复多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510935&idx=2&sn=16d2e8be99d29f0ceb82b7596b370911&chksm=ea949afddde313ebf772d24347c8ee4aa98f2e78b2da9850b34569457f918e386175b6d5b85a&scene=21#wechat_redirect)

[瑞士数据管理公司 Veeam 泄露4.45亿条客户记录](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488036&idx=3&sn=d07a6878bd7689705b7724c3d9fbe1b2&chksm=ea97234edde0aa586c8115f5eda113ca0ea18c04ede5002327dc6390698eec46066457c4971b&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/veeam-fixes-bug-that-lets-hackers-breach-backup-infrastructure/

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