---
title: Fortra 修复严重的 FileCatalyst Workflow硬编码密码问题
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520627&idx=2&sn=55f55c9d3b09bddbe96a389aa7de60b3&chksm=ea94a019dde3290fd533c926dda23d81c729ab48c410a531c32bb235a3df34e071179f4157b6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-30
fetch_date: 2025-10-06T18:05:12.519611
---

# Fortra 修复严重的 FileCatalyst Workflow硬编码密码问题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTTFfHXjY7E49rLfdmuF5eibwLdIfggcjqYldITsBDpniaW4fJBj4NKRhKnEfQibD3pLvY6FhHKmP2dw/0?wx_fmt=jpeg)

# Fortra 修复严重的 FileCatalyst Workflow硬编码密码问题

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Fortra 公司提醒称，FileCatalyst Workflow 中存在一个严重的硬编码密码漏洞，可导致攻击者越权访问内部数据库以窃取数据并获得管理员权限。**

任何人可使用该硬编码密码远程访问被暴露的 FileCatalyst Workflow HyperSQL (HSQLDB) 数据库，获得对潜在敏感信息的越权访问权限。此外，这些数据库凭据可滥用于创建新的管理员用户，以便攻击者获得对 FileCatalyst Workflow 应用的管理员访问权限并完全控制系统。

Fortra 公司在今天发布的安全通告中提到，该漏洞的编号为CVE-2024-6633（CVSS v3.1：9.8），影响 FileCatalyst Workflow 5.1.6 Build 139及更老旧发布。建议用户升级至版本5.1.7或后续版本。

Fortra 公司在安全公告中提到，HSQLDB 的目的只是为了简化安装流程，并建议用户设置其它的安装后解决方案。安全公告提到，“厂商在指南中提到，HSQLDB仅用于方便安装流程，现已弃用，并非为生产使用目的。然而，未按照建议配置 FileCatalyst Workflow 来使用其它数据库的用户易受任何可触及 HSQLDB 的来源攻击。”

目前并不存在缓解措施或应变措施，因此建议系统管理员尽快应用可用的安全更新。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTTFfHXjY7E49rLfdmuF5eibPdZB53cRNEsbVXpJq09B0Fh5YwytSHqenkruicnqvDOngUibVgECrA9w/640?wx_fmt=png&from=appmsg)

**漏洞发现和细节**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTTFfHXjY7E49rLfdmuF5eibPdZB53cRNEsbVXpJq09B0Fh5YwytSHqenkruicnqvDOngUibVgECrA9w/640?wx_fmt=png&from=appmsg)

Tenable 公司在2024年7月1日发现了漏洞CVE-2024-6633，当时他们在所有的 FileCatalyst Workflow 部署上发现了相同的静态密码 “GOSENSGO613”。

Tenable 公司解释称，内部 Workflow HSQLDB 可通过该产品默认设置上的 TCP 端口4406进行远程访问，因此密码暴露影响重大。该公司表示，“攻击者一旦登录到HSQLDB，就能在数据库中执行恶意操作。例如，攻击者可在 DOCTERA\_USERS 表中增加管理员级别的用户，以管理员用户身份访问 Workflow web应用。”

Tenable 公司提到，终端用户无法通过常规方式修改该密码，因此唯一方法是升级至5.1.7或后续版本。访问权限高、利用简单以及犯罪分子获得潜在收益使得该漏洞对于 FileCatalyst Workflow 用户而言极其危险。

由于 Fortra 产品中的严重漏洞可用于大规模同时攻陷高价值企业网络，因此一直是攻击者的香饽饽。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Fortra 修复FileCatalyst 传输工具中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519101&idx=2&sn=525ea40a4a977a6379e49fae31ec7b42&chksm=ea94ba17dde333017d9ea69a177c784a7ffce58f8cdb1383421fceee4f6ce58f96ad89736c68&scene=21#wechat_redirect)

[速修复！Fortra GoAnywhere MFT 中存在严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518740&idx=1&sn=f97575a3c85c3e1d61c6ede1e31c0f1d&chksm=ea94bb7edde33268c42b5b9a74eb3ee30ceb5c34a906ff95500378175e985f1b8e0554fbcf3d&scene=21#wechat_redirect)

[Fortra 修复FileCatalyst 传输工具中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519101&idx=2&sn=525ea40a4a977a6379e49fae31ec7b42&chksm=ea94ba17dde333017d9ea69a177c784a7ffce58f8cdb1383421fceee4f6ce58f96ad89736c68&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fortra-fixes-critical-filecatalyst-workflow-hardcoded-password-issue/

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