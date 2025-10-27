---
title: GitLab：注意严重的任意分支管道执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521035&idx=1&sn=2551f0b914e44081d01813a9f39a47c4&chksm=ea94a261dde32b77e9f71015064c4ea237b5843d654575058520e4256615a479b230e5b288a8&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-12
fetch_date: 2025-10-06T18:53:15.536529
---

# GitLab：注意严重的任意分支管道执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQG3kFB9yBcSibtJQvUYgoiaJaRcQlibwjCqKjGSak5Jz1zib3DJicg8RuMTczCjcicuxHSxibqb5gaicr4ibA/0?wx_fmt=jpeg)

# GitLab：注意严重的任意分支管道执行漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**GitLab 发布安全更新，修复了位于社区版 (CE) 和企业版 (EE) 中的多个漏洞，其中一个是严重的任意分支管道执行漏洞 (CVE-2024-9164)。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQG3kFB9yBcSibtJQvUYgoiaJ1nnkiaiavmyEib6LHLRMpibTSdzEabFTOlr2FcONjU84aicxyF0YNySFmCg/640?wx_fmt=gif&from=appmsg)

该漏洞可导致未授权用户在仓库的任何分支上触发持续集成/持续交付 (CI/CD) 管道。CI/CD管道是执行多种任务如构建、测试和部署代码的自动化流程，通常仅向具有恰当权限的用户开放。

如攻击者能够绕过分支防护措施，则可执行代码或访问敏感信息。该漏洞的CVSS v3.1评分为9.6，为“严重”级别，影响所有 GitLab EE 版本，从12.5到17.2.8、从17.3到17.3.4，以及从17.4到17.4.1。补丁已发布在17.4.2、17.3.5和17.2.9，GitLab强烈建议用户尽快升级至这些版本。

不过，GitLab 专属用户无需采取任何措施，其基于云的实例一直运行的是最新可用版本。

除该漏洞外，GitLab还修复了如下安全问题：

* CVE-2024-8970：高危的任意用户模拟漏洞，可导致攻击者以其它用户身份触发管道。
* CVE-2024-8977：位于 Analytics Dashboard 中的高危SSRF漏洞，可导致实例易受SSRF攻击。
* CVE-2024-9631：当查看存在冲突的合并请求的差异时，该高危漏洞可导致性能减慢。
* CVE-2024-6530：位于OAuth页面中的高危HTML注入漏洞，可导致OAuth授权进程中的跨站点脚本问题。
* CVE-2024-9623、CVE-2024-5005、CVE-2024-9596：低危到中危级别的漏洞，分别是部署密钥推送到已归档仓库、guest用户通过API披露项目模板以及GitLab 实例版本被披露给未授权用户。

最近，GitLab 管道成为该平台及其用户的稳定的安全漏洞来源。今年，GitLab 修复了多个任意管道执行漏洞，如上个月修复了CVE-2024-6678、7月份修复了CVE-2024-6485以及在6月份修复了CVE-2024-5655，它们均为严重级别的漏洞。

用户可在GitLab的官方下载门户查看相关指南、源代码和程序包，以及GitLab Runner 程序包等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitLab修复严重的 SAML 认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520856&idx=1&sn=99796b9ba1361fcd9611a05729e2219d&chksm=ea94a332dde32a2463e0bfdcf157730ba4f594970fb1f1c5d6338bd7b9fb1c0f066de30cf974&scene=21#wechat_redirect)

[GitLab 提醒注意严重的管道执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520799&idx=1&sn=2e34312c9e5c05291452bf69189cd8b5&chksm=ea94a375dde32a6355837cb4f23e5933d2192469425e3f2054204b18a8780163e090447f172b&scene=21#wechat_redirect)

[GitLab 又爆新的CI/CD管道接管漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520065&idx=2&sn=2dfd0b72bc28e69fa94a19fdb4828ace&chksm=ea94be2bdde3373d1294a08d90375f52d1f101e29fb038fd092aa8b03a83c90099f9a89ab166&scene=21#wechat_redirect)

[GitLab 严重漏洞导致攻击者以任意用户身份运行管道](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519913&idx=1&sn=f485e4897bd8f134b2685e61ec98b8ae&chksm=ea94bfc3dde336d543b1cf68c7773d682b657af8bfc3a495d9433d47d2b67144447e9a9c5422&scene=21#wechat_redirect)

[GitLab 高危漏洞可导致账号遭接管](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=1&sn=8ca7ba7442a6234b2f5910147094c5bb&chksm=ea94bc0adde3351ccee634db2e180e9bc4d66ff43d4aa7e08ca703c79df1444bcf27d1b960de&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-arbitrary-branch-pipeline-execution-flaw/

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