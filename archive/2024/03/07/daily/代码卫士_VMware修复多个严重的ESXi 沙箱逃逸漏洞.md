---
title: VMware修复多个严重的ESXi 沙箱逃逸漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519003&idx=2&sn=c494f1df6adfe5a6b91c813d2d236c8c&chksm=ea94ba71dde3336793921a1d4a9852067a51546a77a39e5c25ed0836ffe1f6e0706fb9618530&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-03-07
fetch_date: 2025-10-06T17:09:26.757319
---

# VMware修复多个严重的ESXi 沙箱逃逸漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRkjTv7icPV6zbzZRZVlAWUuicEL28fD76ZVMtlQ9AdxIh1Y3LzP7ib4kwiaPqUpxwVv6eILJvM2VKWEw/0?wx_fmt=jpeg)

# VMware修复多个严重的ESXi 沙箱逃逸漏洞

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周二，虚拟化技术厂商 VMware 紧急修复企业级产品 ESXi、Workstation、Fusion 和 Cloud Foundation 产品中的多个严重漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRkjTv7icPV6zbzZRZVlAWUuYrrFfDXnKFyHalmV5AUib8Y9iagURj8QYFLdzWvJt6boj97pk4xI1LMA/640?wx_fmt=gif&from=appmsg)

VMware 公司发布了四个漏洞，并提醒称其中最严重的漏洞可导致在虚拟机上具有本地管理员权限的恶意人员可以在主机上运行的虚拟机的VMX进程身份执行代码。

其中两个漏洞的CVSS评分为9.3，由于对组织机构的风险不断增多，VMware 甚至为一些已达生命周期的产品推出修复方案。该公司称这两个漏洞是释放后使用内存损坏漏洞，位于XHCI USB 控制器中（CVE-2024-22252和CVE-2024-22253），可组合用于逃逸沙箱缓解措施。

VMware 公司提醒称，“在ESXi上，该利用包含于 VMX沙箱中，而在 Workstation 和 Fusion 中这样做可能导致在安装了 Workstation 和 Fusion 上的机器上执行代码。”

VMware 公司证实称ESXi 中的一个界外写漏洞可导致沙箱逃逸利用，而位于 UHCI USB 控制器中的一个信息泄露漏洞可用于泄露 vmx 进程中的内存。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[VMware督促管理员删除易受攻击的认证插件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518869&idx=2&sn=accd15841c79ae4dc71415f736248c4a&chksm=ea94bbffdde332e9e7711a1bdb39f702a4a132456726e5e95a074e4055c5280db304ea16187d&scene=21#wechat_redirect)

[VMware 披露严重的VCD Appliance认证绕过漏洞，无补丁](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518139&idx=2&sn=4951a6280d077d8cd04309f6629182e3&chksm=ea94b6d1dde33fc71b53f7879454b257d922f83689acde6d310a195b1857f38098ca7685fcca&scene=21#wechat_redirect)

[VMware 发现34个Windows 驱动易受设备完全接管攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518061&idx=3&sn=d4a64266b93ecf83c41d5c0c3914555f&chksm=ea94b607dde33f115aa5272499ee1b24c6ed4deaf860e06465531de74905247f9b9f11dd84db&scene=21#wechat_redirect)

[VMware 修复严重的 vCenter Server 代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517985&idx=2&sn=bf96d48a8e813b54efe7b49e1d451d91&chksm=ea94b64bdde33f5d32a676ffb901bafbd88a9925b05af28720a33389cee0066b41f2b27046cb&scene=21#wechat_redirect)

[VMware 修复网络监控产品中的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517495&idx=2&sn=f20e793a89665c09e42c6341755a3e88&chksm=ea94b45ddde33d4bec3d0c06c238e806e9061130fc138a24354059fe0f857cafc9054fe04e3c&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/vmware-patches-critical-esxi-sandbox-escape-flaws/

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