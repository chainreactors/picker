---
title: CISA 和 Ivanti： Cloud Services Appliance 高危漏洞已遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520811&idx=1&sn=890fffef04e0244ca4a0fe359dfb3886&chksm=ea94a341dde32a57534c153b9526fd132574d3fa54a5c70c2bf6fe73dcf1c38e1c35c88ce3d1&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-15
fetch_date: 2025-10-06T18:26:24.613497
---

# CISA 和 Ivanti： Cloud Services Appliance 高危漏洞已遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSvsO3lmQ4hWJTYLztiaYT648gbYL6UyCskG4bv5UIQ3uW6oicU2CsYEULHnoXtrnlvozjaZSribV48Q/0?wx_fmt=jpeg)

# CISA 和 Ivanti： Cloud Services Appliance 高危漏洞已遭利用

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**CISA 紧急提醒称，Ivanti Cloud Services Appliance (CSA) 中存在一个高危漏洞 (CVE-2024-8190) 且正遭活跃利用。该漏洞被归类为OS命令注入漏洞，可导致具有管理员权限的攻击者实施远程代码执行。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSvsO3lmQ4hWJTYLztiaYT64dd6iaJmfWVFcU4icSlE3DhSdOpm5J2qIC6dbRN7xn0t0iaL5GGibcicmAMw/640?wx_fmt=png&from=appmsg)

Ivanti CSA 是安全远程访问基础设施中的一个关键组件。CVE-2024-8190可导致以管理员权限验证的攻击者在系统上执行任意命令。鉴于 Ivanti CSA 通常部署在企业网络中保护远程连接，该漏洞可导致大量威胁，包括系统遭完全攻陷、数据提取以及在受影响网络中的横向移动等。

虽然并未披露确切的利用方法，但 Ivanti 已证实称数量有限的客户已沦为受害者。CISA将该漏洞纳入必修清单说明了其严重性。CISA要求联邦机构在10月4日前执行这些补救措施，保护网络安全。

该漏洞主要影响Ivanti CSA 4.6版本，但该版本目前已不在受支持范围内。强烈建议组织机构升级至 CSA 5.0版本，确保受到全面保护。或者，使用 CSA 4.6 Patch 518的客户也可应用 Patch 519作为折中方案。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Ivanti 修复Endpoint Management 软件中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520759&idx=2&sn=1fc5e0f7a15b2f6ee85191294e7148e0&chksm=ea94a09ddde3298b03f1d93d760c4ebe1bbf0831c2823c5d15bdc98a012ee7662c48075afa5d&scene=21#wechat_redirect)

[Ivanti 修复Endpoint Manager 中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=3&sn=2aa72d7f1d783c31f298fa9a0f01f07f&chksm=ea94bc0adde3351c1cf417917d51eb468cc181088b1cf49ea4d38cc9f05da775e3aa19c6dd05&scene=21#wechat_redirect)

[Ivanti：注意！Avalanche MDM 解决方案中存在多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519303&idx=2&sn=e86decfa003bf7ebcb19d43552440c7f&chksm=ea94bd2ddde3343b1eba25473eb57c432ce40d7ded22623619060fbc6c299c461dc0087f1d1b&scene=21#wechat_redirect)

[产品中又现4个漏洞，Ivanti 宣布安全大检修](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519242&idx=1&sn=6c9094b038e67aea0f2968fffbb125e0&chksm=ea94bd60dde334764a9154d61f5809e1fd0a977ba3617a96d698def9b968b04b3039d7ecc3b2&scene=21#wechat_redirect)

[Ivanti 修复由北约报送的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519117&idx=1&sn=cde689326429491acd44848ceeacab57&chksm=ea94bae7dde333f1f0011d550d4f6a0c206cfdb62dda27f77ba6e432c6883a80c8ff30be2a51&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/cisa-ivanti-warn-of-active-exploitation-cloud-services-appliance-flaw-cve-2024-8190/

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