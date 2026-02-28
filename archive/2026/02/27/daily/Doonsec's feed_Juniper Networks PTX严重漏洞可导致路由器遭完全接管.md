---
title: Juniper Networks PTX严重漏洞可导致路由器遭完全接管
url: https://mp.weixin.qq.com/s/ItyPOyPSK5HdMXBjkgishQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:09.701868
---

# Juniper Networks PTX严重漏洞可导致路由器遭完全接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfVu2hiby8ZOeQwGgXqssTkpyiaiaoxf3leT6c0mmc5kPGGae8qiclfOhjkCiaDtq7sBjXichAKDmwVWgFDhhlaJibdxkDvu2BEPg0YWoo/0?wx_fmt=jpeg)

# Juniper Networks PTX严重漏洞可导致路由器遭完全接管

Bill Toulas
Bill Toulas

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**在Juniper Networks 公司 PTX 系列路由器上运行的Junos OS Evolved 网络操作系统中存在一个严重漏洞CVE-2026-21902，可导致未经身份验证的攻击者以 root 权限远程执行代码。**

PTX系列路由器是专为高吞吐量、低延迟和大规模扩展而构建的高性能核心与对等互联路由器，广泛应用于互联网服务提供商、电信服务及云网络应用领域。

该漏洞的成因是“机载异常检测”框架中存在错误的权限分配。该框架本应仅通过内部路由接口向内部进程开放。然而，Juniper Networks公司在一份安全公告中解释道，该故障导致可通过外部暴露的端口访问此框架。由于该服务以root权限运行且默认启用，一旦成功利用此漏洞，已处于网络中的攻击者无需身份验证即可完全控制设备。

该漏洞影响 PTX 系列路由器 25.4R1-S1-EVO 和 25.4R2-EVO 之前的 Junos OS Evolved 版本。旧版本也可能受影响，但供应商不会对已达到工程结束或生命周期结束阶段的版本进行评估。25.4R1-EVO 之前的版本以及标准（非 Evolved）Junos OS 版本不受影响。Juniper Networks 已在 25.4R1-S1-EVO、25.4R2-EVO 和 26.2R1-EVO 版本中提供了修复方案。

Juniper 的安全事件响应团队表示，在发布安全公告时，未发现该漏洞已遭恶意利用的证据。

如果无法立即修补，建议使用防火墙过滤器或访问控制列表，将对易受攻击端口的访问权限限制于可信网络。或者，管理员可以使用以下命令完全禁用该易受攻击的服务：

```
'request pfe anomalies disable'
```

由于该网络设备由需要高宽带的服务提供商如云数据中心和大型企业使用，因此Juniper Networks 产品通常是高阶黑客颇具吸引力的目标。2025年1月，一场名为 "J-magic" 的恶意软件活动瞄准了半导体、能源、制造和 IT 领域使用的 Juniper VPN 网关，部署了在接收到 "魔法包" 时激活的网络嗅探恶意软件。2024年12月，Juniper Networks 的智能路由器成为 Mirai 僵尸网络活动的目标，被纳入分布式拒绝服务攻击集群。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Juniper Networks 修复多个严重的 Junos Space 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524163&idx=2&sn=cfef545f117f95276ee5407dd826e0f2&scene=21#wechat_redirect)

[Juniper 修复Session Smart 路由器中严重的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522278&idx=2&sn=076acb12a1297f5e59b788217253c1ac&scene=21#wechat_redirect)

[Juniper 紧急修复严重的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=1&sn=fb9fb97863d38cac47e2e8c94fdfc267&scene=21#wechat_redirect)

[Juniper Networks 修复交换机、防火墙中的多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518790&idx=2&sn=8654a2f71be0f352dbd073de6482ef88&scene=21#wechat_redirect)

[Juniper 提醒注意防火墙和交换机中的严重RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=2&sn=0cbdae2b9be2d7406ffaea5ba7dc47d1&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/critical-juniper-networks-ptx-flaw-allows-full-router-takeover/

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