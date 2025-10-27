---
title: CISA：Craft CMS代码注入漏洞已遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522334&idx=3&sn=f5c15f723d85e58e935d673891c323e3&chksm=ea94a974dde32062deaa7a995cad497c8687d3ed1373842bcc662824544918475c1ebf48d2cc&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-26
fetch_date: 2025-10-06T20:37:05.271645
---

# CISA：Craft CMS代码注入漏洞已遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS4dMlia1lj2iccRMpO2j3Q8a7BFI2Qlic2NBMibneGgMFsxHaJByqY2lh71Qex92xAqkTKicCW6gCo57g/0?wx_fmt=jpeg)

# CISA：Craft CMS代码注入漏洞已遭利用

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全和基础设施网络安全局 (CISA) 提醒称，Craft CMS 中的一个远程代码执行漏洞 (CVE-2025-23209) 已遭利用。**

CVE-2025-23209的CVSS评分8.0，是代码注入（RCE）漏洞，影响 Craft CMS 版本4和5。Craft CMS 是用于构建网站和自定义数字化体验的内容管理系统（CMS）。

虽然关于该漏洞的技术详情尚未发布，但利用该漏洞并不容易，因为要求攻陷Craft CMS的安全密钥。该安全密钥用于保护用户认证令牌、会话cookie、数据库值和敏感应用数据的安全性。只有当攻击者已获得该密钥的前提下，并借此解密敏感数据、生成认证令牌或远程注入并执行恶意代码时，该漏洞才成立。

CISA已将该漏洞加入必修清单，并未分享关于该漏洞范围、攻击来源及攻击目标的信息。联邦机构需要在2025年3月13日前修复该漏洞。该漏洞已在Craft 5.5.8和4.13.8中修复，因此建议用户尽快升级至这些版本或后续版本。

如用户怀疑自己被攻陷，则建议删除包含在 “.env” 文件中的老旧密钥并通过 php craft setup/security-key 命令生成新的密钥。需要注意的是，密钥变更会导致任何通过之前密钥加密的数据变得不可访问。

另外，CISA还将位于Palo Alto Networks 防火墙中的漏洞（CVE-2025-0111）纳入必修清单，联邦机构同样需要在3月13日前修复该漏洞。该漏洞是影响PAN-OS防火墙的文件读漏洞，已被用于由CVE-2025-0108和CVE-2025-9474构成的利用链中。用户也可访问该公司的安全通告获取更多信息。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[PHPFusion 开源 CMS 中存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517570&idx=2&sn=7f19eccf19674dfcdf5f6515082f6989&scene=21#wechat_redirect)

[开源CMS TYPO3中存在XSS漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513988&idx=2&sn=d8e2aa2199ecfa383521908c1073c29b&scene=21#wechat_redirect)

[开源的dotCMS 内容管理软件中存在严重的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=2&sn=b8446991d9e5831092d721d0b28041e9&scene=21#wechat_redirect)

[热门开源CMS平台 Umbraco 中存在多个安全漏洞，可使账户遭接管](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510233&idx=3&sn=a3b6ac9c3a90291e1ce56a9111954282&scene=21#wechat_redirect)

[开源 CMS Drupal 修复 XSS 和开放重定向漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493187&idx=2&sn=8ac5c62090bbee44166832232e092223&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisa-flags-craft-cms-code-injection-flaw-as-exploited-in-attacks/

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