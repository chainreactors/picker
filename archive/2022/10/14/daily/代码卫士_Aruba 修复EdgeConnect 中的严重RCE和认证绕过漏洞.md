---
title: Aruba 修复EdgeConnect 中的严重RCE和认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514198&idx=2&sn=7355930428f40ec6edfaaa22d7aee746&chksm=ea94893cdde3002ae09057a6941995beea58bffa9829737ad255d7b107096c28655b9bb0dfb1&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-10-14
fetch_date: 2025-10-03T19:50:45.487165
---

# Aruba 修复EdgeConnect 中的严重RCE和认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuF0iaALltZwCp35627oWoJcKViczlE8EUoia9nCHLdGZ4Jm4iaAfOMkIZAcBJiaru8h0aa6V6IbWiaiacw/0?wx_fmt=jpeg)

# Aruba 修复EdgeConnect 中的严重RCE和认证绕过漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQuF0iaALltZwCp35627oWoJvzYfeTeiaWWelKklTqic1pibVt42wxnSYd17W71HoXR8QcW9kcKolNWmQ/640?wx_fmt=png)

**摘要**

Aruba 发布EdgeConnect Enterprise Orchestrator 安全更新，修复了可导致远程攻击者攻陷主机的多个严重漏洞。

Aruba EdgeConnect Orchestrator 是一款广泛使用的WAN管理解决方案，为企业用户提供优化、管理、自动化和实时可见性和监控特性服务。该产品中存在严重的可利用漏洞，为系统和网络带来安全风险，因此管理员应将安装安全更新作为优先任务对待。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQuF0iaALltZwCp35627oWoJvzYfeTeiaWWelKklTqic1pibVt42wxnSYd17W71HoXR8QcW9kcKolNWmQ/640?wx_fmt=png)

**修复的漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQuF0iaALltZwCp35627oWoJmqJgzdh1bwibGzXr2vic1au2iaTsGMs3LiacWKBxeQwgRBnHcOOLYnNR2w/640?wx_fmt=gif)

CVE-2022-37913和CVE-2022-37914的CVSS v3.1评分为9.8，是位于EdgeConnect Orchestrator web管理接口中的认证绕过漏洞，可导致未认证的远程攻击者绕过认证。攻击者如成功利用该漏洞，可在无需凭据的情况下将权限提升至管理员权限，从而完全控制主机。

CVE-2022-37915的CVSS v3.1评分为9.8，是位于EdgeConnect Orchestrator web管理接口中的群贤，可导致在底层主机上执行任意命令并导致系统遭完全攻陷。

已修复这些漏洞的Aruba EdgeConnect Orchestrator 版本是9.2.0.40405及以上版本、9.1.3.40197及以上版本、9.0.7.40110及以上版本与8.10.23.40015及以上版本。

Aruba已不支持老旧版本，因此将不会发布相关安全更新。因此，建议使用老旧版本的用户尽快升级产品版本。

不过Aruba 提供了缓解措施，将该产品的CLI和web管理接口先知道专门的二层分区/VLAN或者将防火墙策略设置为三层及以上。

Aruba 公司提到，尚未发现上述漏洞遭利用的迹象或者关于PoC的讨论。不过，鉴于这些漏洞的严重程度之高且在高价值环境中的广泛部署，可以说攻击者将尝试创建相关漏洞利用。即使没有PoC利用，黑客也常在漏洞发布的数分钟之内扫描可利用的目标，供后续使用或出售。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[严重漏洞 TLStorm 2.0 影响大量 Aruba 和 Avaya 网络交换机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=3&sn=dbd40a2f39fbe2dbc3f9c231419eeb3c&chksm=ea949f0bdde3161dcdb5174d3558c3061c592544166666e55d459619aa5a8da5b4e7b78dca18&scene=21#wechat_redirect)

[惠普企业警告：Sudo 漏洞可使攻击者获得 Aruba 平台的 root 权限](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507580&idx=2&sn=a556d290841b3c2b031726bc075c1f8e&chksm=ea94ef16dde36600a21ca747c0a372c113f1e3765ea65f22821ccb9d2107936899b88541454d&scene=21#wechat_redirect)

[Aruba访问策略平台修复多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485519&idx=4&sn=68db7cc19a8c96244c0dbfd2f6193ab5&chksm=ea973925dde0b03322cafce3ccc4e0244e24ffde736b84128935ef46069f385b1b5df3900dbc&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/aruba-fixes-critical-rce-and-auth-bypass-flaws-in-edgeconnect/

题图：网络‍

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