---
title: Citrix 分享Netscaler 密码喷射攻击的缓解措施
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521806&idx=1&sn=0678a9877c98e19004381988c56fc6c5&chksm=ea94a764dde32e72f71642dbcb7e6bab5e66378852fb60d4097593b85bb1641e488ce48c2674&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-17
fetch_date: 2025-10-06T19:40:11.336976
---

# Citrix 分享Netscaler 密码喷射攻击的缓解措施

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQfeiciaZuzYkmpK6lGIdr6fatUFEsQ6ARy2iaVk72SFOiah0oGHqAyx2gjM2TNice8UuDWXicIt3ALEicWQ/0?wx_fmt=jpeg)

# Citrix 分享Netscaler 密码喷射攻击的缓解措施

Lawrence Abrams

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Citrix Netscaler 是遭密码喷射攻击的最新目标，攻击者通过攻击边缘网络设备和云平台，最终攻击企业网络。**

3月份，思科报道称网络威胁者正在针对思科VPN设备发动密码喷射攻击。在某些情况下，这些攻击可导致拒绝服务状态，使思科最终从中发现了一个DDoS 漏洞并在10月份修复。10月份，微软提醒称 Quad7 僵尸网络滥用TP-Link、华硕、Ruckus、Axentra 和合勤网络设备对云服务发动密码喷射攻击。

本周早些时候，德国BSI网络安全机构援引多份报告提醒称，Citrix Netscaler 设备目前正遭类似的密码喷射攻击，攻击者的目的是窃取登录凭据并攻陷网络。BSI提到，“BSI 目前收到越来越多的报告称，关键基础设施行业和国际合作伙伴的Citrix Netscaler 网关遭暴力攻击。”

上周，媒体Born City 率先报道了这些攻击活动。该媒体读者表示自己的 Citrix Netscaler 设备从11月开始一直到12月一直在经历暴力攻击。其中一些读者表示攻击者使用多种通用用户名称（test、testuser1、veeam、sqlservice、scan、ldap、postmaster、vpn、fortinet、confluence、vpntest、stage、xerox、svcscan、finance、sales）对账户凭据发动暴力尝试，次数介于2万到100万次之间。密码喷射攻击中的其它用户名称还包括姓名、姓氏和名字组合以及邮件地址。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQfeiciaZuzYkmpK6lGIdr6fayYhfQzQ3KEujwicXMsu6UiajCRrXpLhojWof8DHH1qCicgribbrriao7HYw/640?wx_fmt=gif&from=appmsg)

**Citrix 发布安全公告**

Citrix 公司发布安全通告，提醒注意不断增多的针对Netscaler 设备的密码喷射攻击，并提供了降低这些影响的缓解措施。

Citrix 公司提到，“Cloud Software Group 最近发现针对NetScaler 设备的密码喷射攻击在增多。这些攻击的认证尝试和失败事发突然且次数突然增多，因此触发了监控系统如Gateway Insights 和 Active Directory 日志的告警。该攻击流量源自大范围的动态IP地址，导致传统的缓解策略如 IP 拦截和速率限制的有效性下降。Gateway Service 用户无需采取任何缓解措施。只有本地部署和在云基础设施上部署的 NetScaler/NetScaler Gateway 设备需要应用这些缓解措施。”

Citrix 公司进一步提到，突然的大量认证请求可能会使配置为正常登录量的Citrix NetScaler 设备不堪重负，导致日志增多且导致设备不可用或产生性能问题。该公司提到，从所观测到的攻击来看，认证请求攻击针对的nFactor 机制推出前的端点，这些端点用于兼容遗留配置的历史认证URL。

Citrix 公司还分享了降低这些攻击影响的一系列缓解措施，包括：

* 确保在LDAP因素之前配置了多因素认证机制。
* 由于攻击针对的是IP地址，Citrix 公司建议创建响应策略，以便释放认证请求，除非它们尝试针对特定的完全限定域名 (FQDN) 进行认证。
* 拦截与nFactor 机制推出前的认证请求相关联的 Netscaler 端点，除非它们是所在环境所必要的。
* 使用WAF 拦截因此前恶意行为而导致低声誉的IP地址。

Citrix 公司提到，这些缓解措施仅适用于 NetScaler 固件的13.0或以上版本。该公司还在安全公告中给出了如何应用这些缓解措施的详细指南。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Citrix 提醒注意已遭利用的两个 NetScaler 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518689&idx=1&sn=0c28377e9cd188322fb8de2c9b984d4f&scene=21#wechat_redirect)

[Citrix NetScaler 严重漏洞可泄露“敏感”数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517841&idx=2&sn=de64058a934247781132d8fdd5886240&scene=21#wechat_redirect)

[美国关基组织机构遭 Netscaler ADC 0day 漏洞利用攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517155&idx=2&sn=30be43df22f528bba04a0cd70d6a2ea4&scene=21#wechat_redirect)

[攻击者滥用 Citrix NetScaler 设备 0day，发动DDoS放大攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247499753&idx=3&sn=b3738632743f3cb88b1e3207dd79945a&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/citrix-shares-mitigations-for-ongoing-netscaler-password-spray-attacks/

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