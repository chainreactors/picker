---
title: GitHub Enterprise Server中存在严重漏洞，可越权访问实例
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521118&idx=1&sn=19780899ec9f4282e334e41a25f88aa3&chksm=ea94a234dde32b22456eab2d416b2ae3e9baeb788e7522fb6a65a51b8fbd47d5083ff9c5dbc1&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-17
fetch_date: 2025-10-06T18:51:55.196870
---

# GitHub Enterprise Server中存在严重漏洞，可越权访问实例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQUj27BlBYnXp57haTawo8Th14GVQRvJW9acwoWoEcheJrBaD8rnf86KNase5DVx1IaMN58STB3FA/0?wx_fmt=jpeg)

# GitHub Enterprise Server中存在严重漏洞，可越权访问实例

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**GitHub 发布Enterprise Server (GHES) 安全更新，修复了多个问题，其中一个严重漏洞CVE-2024-9487（CVSS评分9.5）可导致越权访问实例。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQUj27BlBYnXp57haTawo8TV4uyXT8e6l5CbaicIWB7EibJSLarIgJzN6ORwuicu03cxQkrhMjqGmGCQ/640?wx_fmt=png&from=appmsg)

GitHub 提到，“攻击者可利用可选加密断言特性，绕过SAML 单点登录 (SSO) 认证，导致越权用户利用 GitHub Enterprise Server 中存在的一个加密签名验证不当漏洞，访问该实例。”

GitHub 提到该漏洞是因CVE-2024-4985 （CVSS评分10）漏洞修复而引起的，后者在2024年5月修复。

GitHub 还修复了其它两个漏洞：

* CVE-2024-9539（CVSS评分5.7）是信息泄露漏洞。受害者点击 SVG 资产的恶意URL时，攻击者能够检索受害者的元数据。
* 管理面板中以HTML形式暴露的敏感数据（尚无CVE编号）。

所有这三个漏洞已在 Enterprise Server 版本3.14.2、3.13.5、3.12.10和3.11.16中修复。

8月份，GitHub 还修复了一个严重漏洞CVE-2024-6800（CVSS评分9.5），可被滥用于获取站点管理员权限。

建议运行易受攻击自托管 GHES 版本的组织机构尽快更新至最新版本。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitHub Enterprise Server 中存在严重的认证漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520551&idx=2&sn=c7d2ba1175a4c946fe47679b75e3c64e&chksm=ea94a04ddde3295bb0ef7a0d6531fee1957d5a1ffa8ba19cd572a05c40449b1f4706da88b90a&scene=21#wechat_redirect)

[GitHub 企业服务器中存在严重漏洞，可导致认证绕过](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519550&idx=1&sn=c9df29fac4cc88482637824b11ada5e4&chksm=ea94bc54dde335421f9f83bbe6ae67441821408144a318140245acf73e69aa18472aa1fc98fc&scene=21#wechat_redirect)

[GitHub 企业服务器被曝高危 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502656&idx=2&sn=e386be82e4fb8a3fb76d10976ed3ecad&chksm=ea94fa2adde3733c947c7f67cdc83372ebd8c09d1a3c23f10776d0eddfc50dfa28d12742cc8d&scene=21#wechat_redirect)

[存疑 CVE 漏洞带来无谓压力 热门开源项目开发者归档 GitHub 仓库](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=2&sn=acd4b1226ac3021b5aa91433e3f657f5&chksm=ea94bfd0dde336c6a6ba483f21d5d9572e139fb0e5cd5ac1a9ccde95f91e2330823dfbc71c20&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/github-patches-critical-flaw-in.html

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