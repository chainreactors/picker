---
title: Spring Framework 身份认证绕过漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516023&idx=1&sn=7a78fd326a65fcefb63640ca08718328&chksm=ea948e1ddde3070bbd81a64cbc30f293a43f08c270359b9dda6bb7d7a8cd0b43ca3fef303428&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-25
fetch_date: 2025-10-04T10:39:23.385701
---

# Spring Framework 身份认证绕过漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibZgcxc66wsEfib6W60uQwibiaQhBNndSFk5RNjkAmFwE2xnZ3XFk3ficyYMiaIic7V1ichw9t4H1kz4sYEw/0?wx_fmt=jpeg)

# Spring Framework 身份认证绕过漏洞安全风险通告

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

**安全通告**

Spring Framework 是一个开源应用框架，旨在降低应用程序开发的复杂度。它是轻量级、松散耦合的，具有分层体系结构，允许用户选择组件，同时还为 J2EE 应用程序开发提供了一个有凝聚力的框架。

近日，奇安信CERT监测到官方发布了**Spring Framework 身份认证绕过漏洞(CVE-2023-20860)**，当Spring Security使用mvcRequestMatcher配置并将"\*\*"作为匹配模式时，在Spring Security 和 Spring MVC 之间会发生模式不匹配，最终可能导致身份认证绕过。**鉴于此产品用量较大，建议客户尽快做好自查及防护。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | Spring Framework 身份认证绕过漏洞 | | |
| **公开时间** | 2023-03-20 | **更新时间** | 2023-03-22 |
| **CVE****编号** | CVE-2023-20860 | **其他编号** | QVD-2023-6995 |
| **威胁类型** | 身份认证绕过 | **技术类型** | 身份认证绕过 |
| **厂商** | VMware | **产品** | Spring Framework |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **中危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | Spring Framework存在身份认证绕过漏洞，当Spring Security使用mvcRequestMatcher配置并将"\*\*"作为匹配模式时，在Spring Security 和 Spring MVC 之间会发生模式不匹配，最终可能导致身份认证绕过。 | | |
| **影响版本** | Spring Framework 6.0.x <= 6.0.6  Spring Framework 5.3.x <= 5.3.25  **（其他低于****5.3.x****的系列版本不受此漏洞影响）** | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Spring Framework 身份认证绕过漏洞 | | | |
| **CVE****编号** | CVE-2023-20860 | **其他编号** | | QVD-2023-6995 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.1 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **用户认证（****Au****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 无 | |
| **危害描述** | 攻击者利用此漏洞可能在Spring Framework项目中实现身份认证绕过。 | | | |

处置建议

目前官方已有可更新版本，建议用户升级至:

Spring Framework 6.0.x >= 6.0.7

Spring Framework 5.3.x >= 5.3.26

更新信息可参考官方通告：https://spring.io/security/cve-2023-20860

参考资料

[1]https://spring.io/security/cve-2023-20860

时间线

2023年3月22日，奇安信 CERT发布安全风险通告。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[【安全风险通告】Spring Framework远程代码执行漏洞(CVE-2022-22965)安全风险通告第二次更新](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511203&idx=3&sn=17ae3622395ea3b9603c1dd9764af422&chksm=ea949dc9dde314df7186047b4eb6c86a65f948ab001f65145f87556e1e51e49fa989199a539f&scene=21#wechat_redirect)

[Spring Data MongoDB SpEL表达式注入漏洞安全风险通告第二次更新](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512551&idx=3&sn=1d82552fab1461f66ca02457161cf83b&chksm=ea94808ddde3099bca51c4d30afed76e7f9f6f4d553a89f6a7585832af3f8743faabd0c122ac&scene=21#wechat_redirect)

[Apache Struts 和 Spring 开源漏洞状况的对比](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247504205&idx=1&sn=440b7be16620ae39f0bd16cfa4850571&chksm=ea94e027dde36931160b5d8df1ee2c3ccad9d75c01331165e5671feec76f19482d0593118eab&scene=21#wechat_redirect)

**转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

点击**阅读原文**

到奇安信NOX-安全监测平台查询更多漏洞详情

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