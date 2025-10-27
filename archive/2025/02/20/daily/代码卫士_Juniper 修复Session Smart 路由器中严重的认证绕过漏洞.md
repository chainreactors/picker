---
title: Juniper 修复Session Smart 路由器中严重的认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522278&idx=2&sn=076acb12a1297f5e59b788217253c1ac&chksm=ea94a68cdde32f9aa2f9b837e6ff7718aa5648f24cb5db327e106bce3c5c39c85665a423c9eb&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-20
fetch_date: 2025-10-06T20:35:32.222899
---

# Juniper 修复Session Smart 路由器中严重的认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQhr6jXufaic6PJrZauaJPDaIwxGMricqJ1d4RbqCq2mHUoYaxsGU7j27f8hGYS2icTSamPosoj7qNuA/0?wx_fmt=jpeg)

# Juniper 修复Session Smart 路由器中严重的认证绕过漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Juniper Networks 公司修复了一个严重漏洞，它可导致攻击者绕过认证并接管Session Smart Router (SSR) 设备。**

该漏洞的编号是CVE-2025-21589，是Juniper Networks 公司在内部产品安全测试过程中找到的，它同时影响 Session Smart Conductor和WAN Assurance Managed Routers。上周，该公司在一份带外安全公告中提到，“Juniper Networks Session Smart Router 中存在通过可选路径或信道绕过认证的漏洞，可导致基于网络的攻击者绕过认证并控制设备。”

Juniper Networks安全事件响应团队 (SIRT) 提到，尚未发现该漏洞已遭利用的证据。该公司已在SSR-5.6.17、SSR-6.1.12-lts、SSR-6.2.8-lts、SSR-6.3.3-r2和之后版本中修复该漏洞。虽然该公司表示与Mist Cloud 相连接的一些设备已得到修复，但建议管理员将所有受影响系统升级至已修复版本。

Juniper 表示，“在Conductor管理的部署中，仅修复 Conductor 节点即可，修复方案将会自动推送到联网路由器。在实践中，路由器应当升级至已修复版本，尽管它们连接至已升级的 Conductor后并不易受影响。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQhr6jXufaic6PJrZauaJPDaD1ibGiaFMEGFsj7NfhCojnSXl4L07PJSBB07fT9Nq8ENpy0ywg1icNS0A/640?wx_fmt=gif&from=appmsg)

**常遭攻击**

因用于关键环境中Juniper 设备常遭攻击，经常在厂商发布安全更新不到一周时间后就会被攻击。

例如，去年6月，Juniper 公司发布紧急更新，修复了另外一个SSR 认证绕过漏洞（CVE-2024-2973），它可用于完全接管未修复设备。8月，ShadowServer 威胁监控服务提醒称，威胁行动者利用watchTowr Labs 发布的利用代码攻击 Juniper EX交换机和 SRX 防火墙。一个月之后，VulnCheck 公司发现数千台 Juniper 设备仍然受该利用链的影响。去年12月，Juniper还提醒称攻击者正在使用默认凭据扫描互联网中的Session Smart路由器并通过 Mirai 恶意软件实施感染。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Juniper 紧急修复严重的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=1&sn=fb9fb97863d38cac47e2e8c94fdfc267&scene=21#wechat_redirect)

[Juniper Networks 修复交换机、防火墙中的多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518790&idx=2&sn=8654a2f71be0f352dbd073de6482ef88&scene=21#wechat_redirect)

[Juniper 提醒注意防火墙和交换机中的严重RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=2&sn=0cbdae2b9be2d7406ffaea5ba7dc47d1&scene=21#wechat_redirect)

[CISA 提醒注意已遭活跃利用的 Juniper 预认证 RCE 利用链](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518122&idx=1&sn=d6b5a20e45ee8897ed249a7bdde21ebb&scene=21#wechat_redirect)

[Juniper Networks 修复Junos OS中的30多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517894&idx=2&sn=dfa23961cb9b4c490ab70b8e96d111c7&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/juniper-patches-critical-auth-bypass-in-session-smart-routers/

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