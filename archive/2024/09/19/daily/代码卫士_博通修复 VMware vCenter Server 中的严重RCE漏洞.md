---
title: 博通修复 VMware vCenter Server 中的严重RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=2&sn=d95814f9037c7711dfcb09cd0e590f0c&chksm=ea94a33adde32a2cc2d70ae1c9f784e58a1068b3439966be8fc0130d96ff48e1aae33021a835&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-19
fetch_date: 2025-10-06T18:25:49.423931
---

# 博通修复 VMware vCenter Server 中的严重RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT7lctusib0CJe6kmfLUSPUwo2KPicpBQDRFKnj5nCbJbicibgVrHqpzmox0TKxG5eKpwyCpbbibokgRYA/0?wx_fmt=jpeg)

# 博通修复 VMware vCenter Server 中的严重RCE漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**博通修复了一个严重的 VMware vCenter Server 漏洞，可被攻击者通过网络数据包在未修复服务器上获得远程代码执行能力。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT7lctusib0CJe6kmfLUSPUwffoqp44kZ7BSibPFbNZyhCdngYicKiauxY4cDvXjKp8BydaPibyEWzYHVg/640?wx_fmt=png&from=appmsg)

vCenter Server 是 VMware 的 vSphere 套件的集中管理中心，助力管理员管理和监控虚拟化的基础设施。该漏洞 (CVE-2024-38812) 由 vCenter DCE/RPC 协议执行中的一个堆溢出弱点引发，在中国“矩阵杯”黑客大赛发现。它还影响包括 vCenter 的多款产品，如 VMware vSphere、VMware Cloud Foundation等。

未认证的攻击者可在低复杂度攻击中远程利用该漏洞，无需用户交互，“只需发送特殊构造的网络数据包就可能导致远程代码执行后果”。用户可通过标准的 vCenter Server 更新机制访问该漏洞补丁。博通指出，“为完全保护您自身及所在组织机构的安全，安装 VMware Security Advisory 中所列的更新版本。根据所在组织机构安全态势的不同，还可能存在其它缓解措施、纵深防御策略以及防火墙配置，每家组织机构都必须独立评估这些防火措施的适当性。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT7lctusib0CJe6kmfLUSPUwicjTS7ys7l2ibzQXEwWiciaysPsTb6KVj7AdgeMYEmicPgB8YJfdIqwOEDQ/640?wx_fmt=gif&from=appmsg)

**未遭利用**

Hello autumn

博通指出，尚未发现该RCE漏洞遭利用的迹象。

无法立即应用安全更新的管理员应严格控制对 vSphere 管理组件和接口的网络边界访问权限，包括存储和网络组件等，目前尚不存在官方应变措施。

博通还修复了一个高危提权漏洞 (CVE-2024-38813)，可被用于通过特殊构造的网络数据包在易受攻击服务器上获得root 权限。6月份，该公司还修复了一个类似的 vCenter Server RCE 漏洞 (CVE-2024-37079)，可通过特殊构造的数据包利用。1月份，该公司透露称CVE-2023-34048已遭利用。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[VMware 修复Fusion中的高危代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=3&sn=899efb652a40601d77b2cb2fffa9e4a2&chksm=ea94a0f6dde329e0c294039de56f65cffda877a972c98fbfebe68abac81d4ee415d453a6203e&scene=21#wechat_redirect)

[VMware 修复Aria Automation 中严重的SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=1&sn=c47470c41eba485c6761c101be23ab04&chksm=ea94be4cdde3375a05493cfa38283ce2ea210148cf20f12ae01666d4ae7d06828b0073a00526&scene=21#wechat_redirect)

[VMware 修复多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519781&idx=1&sn=6951e2970725eafcd08fdb56f31e3df5&chksm=ea94bf4fdde3365926e476e57a166e8c5b13f60a4955215555a3a20948faf68e83c949a669da&scene=21#wechat_redirect)

[VMware 修复Workstation 和 Fusion 产品中的多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519506&idx=2&sn=15447e0bd14688896d0aac2ef6d85333&chksm=ea94bc78dde3356e2862d49586a76b04a8277c3e27ee0cbad93ba1906c685c4e45d848bd682a&scene=21#wechat_redirect)

[VMware修复多个严重的ESXi 沙箱逃逸漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519003&idx=2&sn=c494f1df6adfe5a6b91c813d2d236c8c&chksm=ea94ba71dde3336793921a1d4a9852067a51546a77a39e5c25ed0836ffe1f6e0706fb9618530&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/broadcom-fixes-critical-rce-bug-in-vmware-vcenter-server/

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