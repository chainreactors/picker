---
title: VMware 修复Fusion中的高危代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=3&sn=899efb652a40601d77b2cb2fffa9e4a2&chksm=ea94a0f6dde329e0c294039de56f65cffda877a972c98fbfebe68abac81d4ee415d453a6203e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-05
fetch_date: 2025-10-06T18:27:00.168753
---

# VMware 修复Fusion中的高危代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQFiaibvHLibibPhJbHJslBahJyXTUMltudvS5gwvxB9FQpBZyrjqXDmIlMubJZuT0qSibw2zPlzx2fNww/0?wx_fmt=jpeg)

# VMware 修复Fusion中的高危代码执行漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周二，虚拟化软件技术厂商 VMware 为 Fusion 管理程序推出安全更新，修复了可导致代码执行的高危漏洞CVE-2024-38811。**

该漏洞的CVSS评分为8.8，是一个不安全的环境变量，“VMware Fusion 中包含一个因使用不安全环境变量导致的代码执行漏洞。VMware 已将其严重性评级为‘重要’。”

VMware 提到，该漏洞可被用于在Fusion 上下文中执行代码，从而可能导致系统完全攻陷。VMware 表示，“具有标准用户权限的恶意人员可利用该漏洞在 Fusion 应用上下文中执行代码。”该公司感谢 RIPEDA 咨询公司研究员 Mykola Grymalyuk 发现并报送该漏洞。

该漏洞影响 VMware Fusion 13.x版本，已在13.6中修复。

目前尚不存在任何应变措施，建议用户尽快更新 Fusion 实例，不过VMware 并未提到是否已遭在野利用。

最新的VMware Fusion版本还推出对 OpenSSL 3.0.14的更新。该版本在6月推出，修复了三个可导致拒绝服务条件或可导致受影响设备变慢的漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[VMware 修复Aria Automation 中严重的SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=1&sn=c47470c41eba485c6761c101be23ab04&chksm=ea94be4cdde3375a05493cfa38283ce2ea210148cf20f12ae01666d4ae7d06828b0073a00526&scene=21#wechat_redirect)

[VMware 修复多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519781&idx=1&sn=6951e2970725eafcd08fdb56f31e3df5&chksm=ea94bf4fdde3365926e476e57a166e8c5b13f60a4955215555a3a20948faf68e83c949a669da&scene=21#wechat_redirect)

[VMware 修复Workstation 和 Fusion 产品中的多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519506&idx=2&sn=15447e0bd14688896d0aac2ef6d85333&chksm=ea94bc78dde3356e2862d49586a76b04a8277c3e27ee0cbad93ba1906c685c4e45d848bd682a&scene=21#wechat_redirect)

[VMware修复多个严重的ESXi 沙箱逃逸漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519003&idx=2&sn=c494f1df6adfe5a6b91c813d2d236c8c&chksm=ea94ba71dde3336793921a1d4a9852067a51546a77a39e5c25ed0836ffe1f6e0706fb9618530&scene=21#wechat_redirect)

[VMware督促管理员删除易受攻击的认证插件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518869&idx=2&sn=accd15841c79ae4dc71415f736248c4a&chksm=ea94bbffdde332e9e7711a1bdb39f702a4a132456726e5e95a074e4055c5280db304ea16187d&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/vmware-patches-high-severity-code-execution-flaw-in-fusion/

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