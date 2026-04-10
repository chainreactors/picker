---
title: CISA：须在周日前修复已遭利用的 Ivanti EPMM 漏洞
url: https://mp.weixin.qq.com/s/vV0zHzicF_AGGftp8zqLow
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:43:19.167965
---

# CISA：须在周日前修复已遭利用的 Ivanti EPMM 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXDmW76BleIrud7YHq1Rpx6wVPoPyaISHFRKDNEx5L9dTP4SDw4sNhfFBOLjos0zIAibbsWibLMyktZFcOics7fCR8jhsDSzVddick/0?wx_fmt=jpeg)

# CISA：须在周日前修复已遭利用的 Ivanti EPMM 漏洞

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全与基础设施安全局（CISA）要求联邦政府机构在四天内完成系统加固，以防范 Ivanti Endpoint Manager Mobile（EPMM）中已在今年1月份遭实际利用的一个高危漏洞CVE-2026-1340。**

该漏洞是一个高危代码注入漏洞，可导致未授权攻击者在暴露于互联网且未打补丁的 EPMM 设备上实现远程代码执行。Ivanti 公司于 1 月 29 日发布安全更新，修复了该漏洞及另一个安全漏洞 (CVE-2026-1281)，并指出这两个漏洞被用于 0day 攻击。Ivanti 当时“强烈建议”所有客户更新系统，以阻断正在进行的漏洞利用行为。Ivanti 公司当时表示：“成功利用该漏洞可导致未授权远程代码执行。在漏洞披露时，我们已知晓极少数客户的解决方案已遭到利用。”

互联网安全监测组织 Shadowserver 目前追踪到近 950 个仍处于暴露状态的Ivanti EPMM 指纹 IP 地址，其中大部分位于欧洲（569 个）和北美（206 个）。不过，目前尚无法知晓其中有多少设备已完成补丁更新。

当地时间本周一 CISA 将该漏洞纳入已知被利用漏洞目录（KEV），并根据《约束性操作指令 22-01》（BOD 22-01）的要求，责令联邦民事行政部门 (FCEB) 机构在 4 月 11 日周六午夜前完成 EPMM 系统的补丁修复。

CISA 警告称：“此类漏洞是恶意网络行为者的常见攻击入口，对联邦机构的企业网络构成重大风险。请按照厂商指引进行加固，遵循 BOD 22-01 中针对云服务的相关指导；若无法实施缓解措施，则应停止使用该产品。”尽管 BOD 22-01 仅适用于美国联邦机构，CISA 仍建议包括私营部门在内的所有防御方，优先修复该漏洞，尽快加固设备安全。

近年来，多个其它 Ivanti 漏洞已在 0day 状态下被用于攻破各类目标，其中包括全球多家政府机构。总体而言，CISA 已将 33 个 Ivanti 漏洞标记为已遭利用，其中 12 个被多个勒索软件团伙利用。

Ivanti的全球合作伙伴超过 7000 家，为超过 40000 家客户提供 IT 资产管理产品服务。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[CISA要求三天内修复这个严重的 F5 BIG-IP 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525571&idx=1&sn=3596dc720ddc3cfdb3245a4b7597f249&scene=21#wechat_redirect)

[CISA：Wing FTP 已遭利用漏洞可泄露服务器路径](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525482&idx=2&sn=92844a4f59d7d7b8344f344ed41a3600&scene=21#wechat_redirect)

[CISA：VMware Aria Operations RCE漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525306&idx=2&sn=bd95e3c5ab9c19e0a8d50c704895e37c&scene=21#wechat_redirect)

[Ivanti Endpoint 管理器漏洞可导致远程攻击者泄露任意数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525108&idx=2&sn=eb3ace41d769ee7dcd8d459a227040f3&scene=21#wechat_redirect)

[Ivanti 提醒注意已遭利用的两个 EPMM 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525028&idx=2&sn=762ebd580b93c85ca6f361c47033a215&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-ivanti-epmm-flaw-by-sunday/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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