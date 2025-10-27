---
title: Palo Alto 修复已遭利用的严重PAN-OS DoS 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521932&idx=1&sn=518332fa38f3263ee23df7a70c1187d3&chksm=ea94a7e6dde32ef0734d2279cc2338eb07d4063b92d89e4de919fa8fce43313cc34fe97331a2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-31
fetch_date: 2025-10-06T19:41:15.370126
---

# Palo Alto 修复已遭利用的严重PAN-OS DoS 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRicoqpSXwETiazJtyJ4LKibhGr8ZKN8wYCxpkTjdpYFDKt3o8g3ia0suQNOY4rgyzInfNCphdR2stibew/0?wx_fmt=jpeg)

# Palo Alto 修复已遭利用的严重PAN-OS DoS 漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Palo Alto Networks 披露了一个影响 PAN-OS 软件的高危漏洞（CVE-2024-3393，CVSS 8.7），它可在易受攻击设备上引发拒绝服务 (DoS) 条件。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRicoqpSXwETiazJtyJ4LKibhGxy2loicNAs99ksm8bVPD7icade5lNf7OBicvAQ5KFAibF3S4u5CfoaFIYw/640?wx_fmt=png&from=appmsg)

该漏洞影响 PAN-OS 10.X 和11.X 版本以及运行PAN-OS 10.2.8及后续或11.2.3之前版本的 Prisma Access。该漏洞已在 PAN-OS 10.1.14-h8、PAN-OS 10.2.10-h12、PAN-OS 11.1.5、PAN-OS 11.2.3以及后续PAN-OS版本中修复。

Palo Alto 公司上周五发布公告称，“Palo Alto Networks PAN-OS软件的DNS Security 特性中存在一个拒绝服务漏洞，可导致未认证攻击者通过负责重启防火墙的数据面板发送恶意数据包。反复触发该条件可导致防火墙进入维护模式。”

Palo Alto 公司表示在生产使用中发现了该缺陷，并发现客户“的防火墙拦截触发该问题的恶意DNS数据包时，经历了拒绝服务。”

这起攻击活动的范围目前尚不知晓。Palo Alto 公司证实称该漏洞已遭在野利用，“我们积极发布该公告，提供透明度并让客户获得保护自身环境安全的信息。”

值得注意的是，启用了DNS Security 日志记录功能的防火墙受该漏洞影响。另外如果访问权限是通过 Prisma Access 向已认证终端用户提供的，则该漏洞的CVSS严重性评分将至7.1分。

修复方案已扩展至其它常部署的维护发布版本中：

* PAN-OS 11.1 (11.1.2-h16、11.1.3-h13、11.1.4-h7和11.1.5)
* PAN-OS 10.2（10.2.8-h19、10.2.9-h19、10.2.10-h12、10.2.11-h10、 10.2.12-h4、10.2.13-h2和10.2.14）
* PAN-OS 10.1 (10.1.14-h8 和10.1.15)
* PAN-OS 10.2.9-h19 和 10.2.10-h12（仅适用于Prisma Access）
* PAN-OS 11.0（该版本已在2024年11月17日达到生命周期，因此无修复方案）

作为未管理的防火墙或由 Panorama 管理的防火墙的应变措施和缓解措施，客户可将通过 Objects＞Security Profiles＞Anti-spyware＞（选择一个配置）＞DNS Policies＞DNS Security，将每个 Anti-Spyware 配置的所有已配置DNS Security 类别的Log Severity 设为 “none”。

对于由 Strata Cloud Manager (SCM) 管理的防火墙，用户可按照如上步骤在每台设备上直接禁用 DNS Security 日志记录功能，或者通过打开支持案例的方式在所有设备上禁用。对于由SCM管理的Prisma Access 租户，建议打开支持案例关闭日志记录功能，等待执行升级。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Palo Alto 防火墙 0day 由低级开发错误引发](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521617&idx=2&sn=0e9ac32a3223e727cd6cd99460e0387e&scene=21#wechat_redirect)

[Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&scene=21#wechat_redirect)

[Palo Alto 修复多个严重的防火墙漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=1&sn=2987012f618a751eabf08e620add0615&scene=21#wechat_redirect)

[Palo Alto：注意！PAN-OS 防火墙 0day 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=1&sn=86e226003b5da9dd0d6867f4b45fcb1a&scene=21#wechat_redirect)

[Palo Alto Networks：PAN-OS DDoS 漏洞已遭在野利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513567&idx=1&sn=181b3bb7e1b34dc9dd67bfde798f4c7d&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/palo-alto-releases-patch-for-pan-os-dos.html

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