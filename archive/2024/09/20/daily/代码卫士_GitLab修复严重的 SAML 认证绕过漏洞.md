---
title: GitLab修复严重的 SAML 认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520856&idx=1&sn=99796b9ba1361fcd9611a05729e2219d&chksm=ea94a332dde32a2463e0bfdcf157730ba4f594970fb1f1c5d6338bd7b9fb1c0f066de30cf974&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-20
fetch_date: 2025-10-06T18:27:41.503358
---

# GitLab修复严重的 SAML 认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTeq7TomYdD3GlE3biaxN4btDcM2ibhVNalQnq3l6hcq0nFk1PcJadAsnO3iaLq9loQWHubHtAWxZXbQ/0?wx_fmt=jpeg)

# GitLab修复严重的 SAML 认证绕过漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**GitLab 发布安全更新，修复了影响 GitLab CE（社区版）和EE（企业版）自管理安装中的一个严重的 SAML 认证绕过漏洞 CVE-2024-45409。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTeq7TomYdD3GlE3biaxN4btickd5amxQWic49yicCxWunRkZpRb948cbVXibfj3G3nibzhQgeuCT7aLtww/640?wx_fmt=png&from=appmsg)

SAML 是单点登录 (SSO) 认证协议，允许用户使用同样的凭据登录不同的服务。该漏洞是由位于 OmniAuth-SAML和Ruby-SAML 库中的一个问题引发的。GitLab 使用这些库处理基于SAML的认证。

当身份提供商向 GitLab 发送的SAML响应中包含配置不当问题或者遭操控时，就会触发该漏洞。具体而言，该漏洞涉及对 SAML 断言中关键元素的验证不充分问题，如 extern\_uid（外部用户id）。攻击者可构造恶意SAML响应，诱骗 GitLab 将其识别为认证用户，绕过SAML认证并获得对 GitLab 实例的访问权限。

该漏洞影响 GitLab 17.3.3、17.2.7、17.1.8、17.0.8、16.11.10及这些分支之前的所有发布。该漏洞已在GitLab 17.3.3、17.2.7、17.1.8、17.0.8和 16.11.10中修复，即 OmniAuth SAML 已升级至2.2.1和 Ruby-SAML 升级至1.17.0。

GitLab 在安全通告中提到，“我们强烈建议所有运行受这些问题影响的版本的用户尽快升级至最新版本。”GitLab.com 上 GitLab Dedicated 实例用户无需采取任何措施，因为该漏洞仅影响自管理安装程序。

如用户无法立即升级至安全版本，则 GitLab 建议为所有用户启用双因素认证机制，并将SAML 2FA绕过选项设置为“禁止”。

**利用迹象**

虽然 GitLab 并未说明该漏洞此前是否遭利用，但在安全公告中提供了尝试或成功利用的证据，这说明恶意人员可能已经在攻击中利用了该漏洞。

尝试或成功利用的迹象如下：

* 与 RubySaml:ValidationError 相关的错误（尝试失败）
* 认证日志中新的或异常的 extern\_uid值（尝试成功）
* SAML响应中的信息缺失或不正确
* 单个用户的多个 extern\_uid 值（账户可能遭攻陷）
* 与用户通常访问模式相比，来自不熟悉的或可疑 IP地址的SAML认证

GitLab 尚未说明该漏洞是否已遭在野利用。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitLab 提醒注意严重的管道执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520799&idx=1&sn=2e34312c9e5c05291452bf69189cd8b5&chksm=ea94a375dde32a6355837cb4f23e5933d2192469425e3f2054204b18a8780163e090447f172b&scene=21#wechat_redirect)

[GitLab 又爆新的CI/CD管道接管漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520065&idx=2&sn=2dfd0b72bc28e69fa94a19fdb4828ace&chksm=ea94be2bdde3373d1294a08d90375f52d1f101e29fb038fd092aa8b03a83c90099f9a89ab166&scene=21#wechat_redirect)

[GitLab 严重漏洞导致攻击者以任意用户身份运行管道](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519913&idx=1&sn=f485e4897bd8f134b2685e61ec98b8ae&chksm=ea94bfc3dde336d543b1cf68c7773d682b657af8bfc3a495d9433d47d2b67144447e9a9c5422&scene=21#wechat_redirect)

[GitLab 高危漏洞可导致账号遭接管](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=1&sn=8ca7ba7442a6234b2f5910147094c5bb&chksm=ea94bc0adde3351ccee634db2e180e9bc4d66ff43d4aa7e08ca703c79df1444bcf27d1b960de&scene=21#wechat_redirect)

[GitLab 提醒注意严重的零点击账户劫持漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=1&sn=e9e78678e6c35cd6c0c37b638d5a988c&chksm=ea94b8a7dde331b16bdf8306a2700a04ea240bc5baa204b72ab3c9664a58b77c6fc92b1841f4&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/gitlab-releases-fix-for-critical-saml-authentication-bypass-flaw/

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