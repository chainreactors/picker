---
title: Progress 紧急修复影响 LoadMaster 的超危RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520732&idx=1&sn=8fafa0f4d8f56d2a8361866cce3ac84c&chksm=ea94a0b6dde329a0b734a3f78a7d08346686d7c08491cae9150d82ce56df6a5d2aa9356b6d2b&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-10
fetch_date: 2025-10-06T18:28:06.528415
---

# Progress 紧急修复影响 LoadMaster 的超危RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQCD1O2gZF63RXVQYzxpwDZbfOL40z1OpKFoQDgJULMgU4oQTD7K4jIHeMtCSOHlk2LG9u5bjCxUQ/0?wx_fmt=jpeg)

# Progress 紧急修复影响 LoadMaster 的超危RCE漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Progress Software 公司紧急修复了影响 LoadMaster 和 LoadMaster Mult-Tenant (MT)  Hypervisor产品的CVSS满分漏洞 (CVE-2024-7591)，它可导致攻击者在设备上远程执行命令。**

该漏洞被归类为输入验证不当漏洞，可导致未认证的远程攻击者使用特殊构造的 HTTP 请求访问 LoadMaster的管理接口。然而，缺乏用户输入清理还可导致攻击者在易受攻击的端点上执行任意系统命令。

该安全公告提到，“未认证的远程攻击者如能访问LoadMaster的管理接口来发布特殊构造的HTTP请求，将导致执行任意系统命令。”该漏洞目前已修复。

LoadMaster 是一款由大型组织机构使用的应用交付控制器 (ADC) 和加载均衡解决方案，用于优化应用性能、管理网络流量并确保服务高可用性。LoadMaster MT Hypervisor是位多租户环境设计的 LoadMaster 版本，可允许在同样的硬件上运行多个虚拟网络功能。

CVE-2024-7591影响 LoadMaster 7.2.60.0及之前版本、MT Hypervisor 7.1.35.11及之前版本。Long-Term Support（LTS）和Long-Term Support with Feature (LTSF) 分支也受影响。

为修复该漏洞，Progress 发布可在任何易受攻击版本（包括老版本）上安装的附件程序包，因此目前尚不存在升级至的目标版本。不过，该补丁并不适用于 LoadMaster 免费版本。

Progress Software 公司表示，截止到公告发布之时，并未收到任何关于该漏洞遭活跃利用的报告。尽管如此，建议所有的 LoadMaster 用户采取恰当措施确保自己的环境不受影响，包括安装该附件包以及执行厂商推荐的安全加固措施。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Progress 提醒注意Telerik Report Server中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520228&idx=1&sn=d9e2734ebb4a13c747b20000c240d7bd&chksm=ea94be8edde33798e81c133dacfe538263083021026fe777545f067b211569e604c359b9c639&scene=21#wechat_redirect)

[速修复！Progress Telerik 中存在严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519654&idx=1&sn=22b4f342e957ddb68acf5d7dabc14f7b&chksm=ea94bcccdde335da0a488c11021c8d947834829e062cbd4a5917bc946b3037f54a151014c361&scene=21#wechat_redirect)

[速修复Progress Flowmon中的这个CVSS满分漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519358&idx=2&sn=398290f1e1cbf32a9f72ff26e3d708c4&chksm=ea94bd14dde334025bccac4bf83cd4b90113971ba22d26184385ccc5d530c62314ca6d06d349&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/progress-loadmaster-vulnerable-to-10-10-severity-rce-flaw/

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