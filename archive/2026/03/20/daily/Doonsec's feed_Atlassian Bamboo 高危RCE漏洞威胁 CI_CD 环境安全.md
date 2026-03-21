---
title: Atlassian Bamboo 高危RCE漏洞威胁 CI/CD 环境安全
url: https://mp.weixin.qq.com/s/IFDiovAzxF0SyPVSGpyyrw
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:02:17.789704
---

# Atlassian Bamboo 高危RCE漏洞威胁 CI/CD 环境安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfW4D9Hc6FgkLTxDG2eKV8aRFNuSf0R0MyDFb2ewicVAnVXMnlQicAzQml8vsyHBbygGRX8koGhkOs46Z1FCjQXc8O8ibPib6DX9L9I/0?wx_fmt=jpeg)

# Atlassian Bamboo 高危RCE漏洞威胁 CI/CD 环境安全

Ddos
Ddos

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Atlassian 提醒其 Bamboo Data Center 用户注意一个高危远程代码执行漏洞CVE-2026-21570（CVSS评分8.6），可导致攻击者夺取对开发环境的控制权。该漏洞凸显了对大型企业持续集成和部署流水线的重大风险。**

作为众多软件开发生命周期的基石，Bamboo 一旦遭入侵，可能导致恶意代码被注入下游软件产品，因此安装此补丁成为 IT 安全团队的首要任务。该漏洞可导致已获得系统认证访问权限的攻击者通过执行任意代码来升级其影响。尽管需要认证设置了一定的门槛，但其对系统机密性、完整性和可用性具有"高"度影响的潜力，使其成为一个严重问题。

该漏洞有效地绕过了标准的安全边界，使恶意行为者能够直接与远程系统的底层架构进行交互。该漏洞影响范围相当广泛，波及Data Center 产品的多个主要发布周期。安全公告提到，该漏洞被引入以下版本：

* 9.6.0
* 10.0.0、10.1.0、10.2.0
* 11.0.0、11.1.0
* 12.0.0 和 12.1.0

Atlassian 强烈建议所有 Bamboo Data Center 客户立即迁移到最新的可用版本。对于因故只能使用特定发布分支的组织，已指定以下最低修复版本：

|  |  |
| --- | --- |
| **分支** | **所需升级版本** |
| 9.6 | 9.6.24 或更高版本 |
| 10.2 | 10.2.16 或更高版本 |
| 12.1 | 12.1.3 或更高版本 |

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Atlassian 和思科修复多个高危漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522791&idx=2&sn=841f61a29df71610844f2e021c5c9bab&scene=21#wechat_redirect)

[Atlassian 修复Confluence 和 Crowd 中的多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522309&idx=2&sn=75d35854eb171a70fb22bd76ed1b2cf4&scene=21#wechat_redirect)

[Atlassian Bamboo Data Center and Server中存在RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520541&idx=1&sn=f403f1139228e0543f485dc49192281e&scene=21#wechat_redirect)

[Atlassian 修复Confluence等产品中的多个高危漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520092&idx=2&sn=cc02ff9f6ef98e6d539f13b4c6c892c2&scene=21#wechat_redirect)

[Atlassian Confluence 高危漏洞可导致代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519665&idx=2&sn=86259d3f96b173403f1a65b601fc1989&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/high-severity-rce-flaw-atlassian-bamboo-data-center-cve-2026-21570/

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