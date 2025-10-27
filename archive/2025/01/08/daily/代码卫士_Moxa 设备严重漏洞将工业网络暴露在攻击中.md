---
title: Moxa 设备严重漏洞将工业网络暴露在攻击中
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521996&idx=2&sn=dbafe74fa2a73a7ecd72c5ca600d8614&chksm=ea94a7a6dde32eb0768fd7281523c870565bc1d8ec2cd067e00a960f7468a905c6da64ea56e1&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-08
fetch_date: 2025-10-06T20:10:46.388714
---

# Moxa 设备严重漏洞将工业网络暴露在攻击中

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRK3GwH5ZhTcSkMz3aVNdyqhjwicicYVzhBg6td9665cBcZWgT1ib1SxJOibC6cfyZ8ljYKLzUTla6j4A/0?wx_fmt=jpeg)

# Moxa 设备严重漏洞将工业网络暴露在攻击中

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**工业网络和通信提供商 Moxa 提醒称，多个蜂窝路由器、安全路由器和网络安全设备的多个机型受一个高危漏洞和一个严重漏洞影响。这两个漏洞可导致远程攻击者在易受攻击设备上获得根权限并执行任意命令，从而导致任意代码执行后果。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRK3GwH5ZhTcSkMz3aVNdyqiaHX8stXkCqFrYWOcZLUeamk0NR6ibxZkzJ2Y1GMFbeh2t8zOwbanWFQ/640?wx_fmt=gif&from=appmsg)

**Moxa 路由器风险**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRK3GwH5ZhTcSkMz3aVNdyqGmMibOQDHVH5oQ7rNtf6icK0RbuDJ62ibuFb39EAHDgLvTKBIFgbL1X4w/640?wx_fmt=gif&from=appmsg)

Moxa 设备用于交通、公共设施和能源以及电信行业的工业自动化和控制系统环境中。上周五，该厂商发布关于如下两个漏洞的紧急提醒：

* CVE-2024-9138（8.6，高危）是一个硬编码凭据漏洞，可导致认证用户将权限提升至根。
* CVE-2024-9140（9.3，严重）是一个由利用输入限制不当缺陷造成的OS命令注入漏洞，可导致任意代码执行后果。

第二个漏洞尤为危险，因为它可遭远程攻击者利用。Moxa 已发布固件更新修复了这些漏洞并提到，“强烈建议立即采取措施，阻止潜在利用并缓解这些风险”。

如下设备同时受这两个漏洞的影响：

* 使用固件3.13.1及更早版本的EDR-8010 系列
* 使用固件3.13.1及更早版本的EDR-G9004系列
* 使用固件3.13.1及更早版本的EDR-G9010 系列
* 使用固件3.13.1及更早版本的EDF-G1002-BP 系列
* 使用固件1.0.5及更早版本的NAT-102系列
* 使用固件3.13及更早版本的OnCell G4302-LTE4系列
* 使用固件3.13及更早版本的TN-4900系列

此外，使用固件版本5.12.37及更老旧版本的 EDR-810系列、使用固件版本5.7.25及更老旧版本的EDR-G902和使用固件版本3.13及更老旧版本的TN-4900系列仅易受CVE-2024-9138的影响。

EDR-8010系列、EDR-G9004系列、EDR-9010和EDG-G1002-BP系列的用户应升级至在2024年12月31日发布的固件版本3.14，修复该漏洞。建议按照Moxa通告上每台设备的下载链接获得官方固件镜像。

建议 OnCell G4302-LTE4系列和TN-4900系列的管理员联系Moxa支持人员获得打补丁指南。对于NAT-102系列设备，目前尚不存在补丁，建议管理员应用缓解措施。

Moxa 建议限制设备的网络暴露和SSH访问权限，以及使用防火墙、IDS或IPS监控并拦截利用尝试。Moxa 在安全公告中提到，MRC-1002系列、TN-5900系列和OnCell 3120-LTE-1系列设备并不受其中任何一个漏洞的影响。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[台商 Moxa 网络设备被曝多个漏洞，导致工业环境易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492357&idx=2&sn=0d537358b33dda855b617e0308f53c5c&scene=21#wechat_redirect)

[Moxa IIoT 产品有缺陷 导致 ICS 易受远程攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489104&idx=4&sn=763f93957651f81be1c109d3a13ec6d0&scene=21#wechat_redirect)

[Moxa 路由器中存在多个严重漏洞易遭攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486898&idx=1&sn=841b60f17f7d5bea481367d80908835e&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/vulnerable-moxa-devices-expose-industrial-networks-to-attacks/

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