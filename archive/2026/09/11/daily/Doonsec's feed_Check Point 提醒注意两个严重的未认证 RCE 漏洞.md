---
title: Check Point 提醒注意两个严重的未认证 RCE 漏洞
url: https://mp.weixin.qq.com/s/QGDB2_-2Tom3ExB1BZvGeg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:42:16.885137
---

# Check Point 提醒注意两个严重的未认证 RCE 漏洞

# Check Point 提醒注意两个严重的未认证 RCE 漏洞

Swati Khandelwal
Swati Khandelwal

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

**Check Point****已修复因防火墙和管理产品处理****VPN****证书方式引发的两个严重漏洞（****CVE-2026-85102****和****CVE-2026-85103****）。该公司表示，这两个漏洞都可能导致未经身份验证的远程攻击者运行代码，但仅限于该公司并未描述的****“****特定条件****”****下。**

Check Point 于 9 月 9 日在向客户社区发布的通知中披露了这些漏洞，并于同日开始提供修复程序。该公司表示，这两个漏洞都由内部发现，且未有迹象表明其中任何一个已被用于攻击。

CVE-2026-85102 是在 VPN 协商期间未能正确验证证书信任。未经身份验证的远程攻击者可能能够在防火墙设备 Security Gateway 上运行代码。CVE-2026-85103 是一个基于堆的缓冲区溢出，发生在产品解码 VPN 证书的 ASN.1 结构时未经身份验证的远程攻击者可能能够在 Quantum Security Management 和 Quantum Security Gateway 系统上运行代码。这两个漏洞的 CVSS 评分均为 9.8。Check Point 自行分配了这些标识符和评分。

这两个漏洞的受影响版本相同，如下：

* R82.10 搭配 Jumbo Hotfix Take 43 或更低版本
* R82 搭配 Jumbo Hotfix Take 125 或更低版本
* R81.20 搭配 Jumbo Hotfix Take 165 或更低版本

以上版本是受影响版本，并非包含修复的版本。该列表涵盖三个 Quantum 分支，并未提供其它任何版本信息。加拿大网络安全中心当晚发布的公告列出了更广泛的产品，但并未提供版本信息。它列出了 Security Gateway、Security Management Server 和 Spark Firewall，即 Check Point 的小型企业产品线。Spark 出现了两次，一次针对使用站点到站点或远程访问 VPN 的部署，一次针对没有该条件的情况。

在同一社区帖子中，一名 Check Point 员工被问及关闭了 VPN 软件刀片的网关是否受 CVE-2026-85103 漏洞的影响。该员工回复称，该问题涉及证书处理，因此理论上，在没有 VPN 但存在 VPN 证书的环境中也可能被触发。

Check Point 为客户提供了两条修复途径。第一种是 Check Point Live Patch。该公司表示，使用它的客户会随着 rollout 开始而自动受到保护，该 rollout 已于 9 月 9 日开始。一名 Check Point 员工在帖子中表示，它可以安装在 R81.20、R82.00 和 R82.10 的任何 Jumbo Hotfix 级别之上，并且只列出了这三个版本。第二种是 Jumbo Hotfix。Check Point 告知客户称，应尽早安装部署版本的最新 Jumbo Hotfix 。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfURibmDD0SEO03KcIxibfEAUEqdh7fPwozlKpqWqAju2c7Czdfia4BFKHJL8icTs7oicw07r9ibC7a7zwUCyQg5CibupibZUmGKbJ7WQcI/640?wx_fmt=gif&from=appmsg)

**如无法打补丁**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWliczOcpicPzicLibVeLcZ3bU98aSNDkZdq7ddhHfFlf2TLgFgkgjYZUzMKiaIb6tqjXf0Q3ZWWBNiaXzN3PhdfG9JB0ibg1mLw57rdg/640?wx_fmt=gif&from=appmsg)

两名客户在帖子中表示，他们正在运行 R81.10，并且数周内不会迁移离开该版本。其中一人表示，该分支没有可用的 Jumbo Hotfix，也没有 Live Patch，因此缓解措施是唯一选择。

该客户称，公告中的缓解措施是关闭 VPN 的未明确规则，并称其过于含糊，无法据此采取行动，还询问应注释掉哪些配置行。另一人询问如何在不影响远程用户的情况下应用该缓解措施。这两个问题在帖子中都没有得到回答。几名客户还表示，自动 rollout 尚未覆盖他们。五个不同账户报告称，在公告发布当天，网关仍停留在紧急安全更新包的 Take 18 或 Take 17；其中一人发布了一份更新日志，显示 Take 18 于 9 月 1 日安装，此后没有任何更新。

几名客户报告称，两份公告中的下载链接对他们无效，一名 Check Point 员工回复称，链接已经过检查并且可用。一名客户随后表示，公告链接在两个浏览器中仍然失败，而 Live Patch 文章中的链接则可用。

6 月和 7 月，Check Point 修复了这些产品中的严重漏洞，并称在宣布时这些漏洞已被利用。6 月的是 CVE-2026-50751，是 Remote Access VPN 和 Mobile Access 证书验证中的身份验证绕过漏洞。美国网络安全和基础设施安全局 (CISA) 于 6 月 8 日将其加入已知被利用漏洞目录。

7 月的是 CVE-2026-16232，是一个 SmartConsole 身份验证绕过漏洞，CISA 在其披露当天将其加入同一目录。这是 Check Point 当月修复的三个漏洞之一，其中两个影响 Security Management Server，也就是 CVE-2026-85103 所触及的同一组件。

Check Point 尚未发布这两个新漏洞的妥协指标。当在帖子中被问及日志是否会显示利用它们的尝试时，一名员工表示，公司没有看到外部利用的证据，并且妥协指标只适用于已经存在的利用。

Check Point 的通知以及本文审阅的任何公开记录，均未说明哪些 Spark 或 Security Management 版本受影响、哪些构建包含修复，或该公司所称这些漏洞需要哪些具体条件。这些材料中也没有任何内容说明安装修复程序是否会移除攻击者可能已经获得的访问权限。

客户可参见Check Point 的公告 sk1000117 和 sk1000118，获取受影响产品、缓解指导和修复步骤的文件指南。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[攻击者利用 Check Point VPN 访问企业网络](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519614&idx=2&sn=61729da3c7c16514ae5bdae557f4e001&scene=21#wechat_redirect)

[黑客利用 vBulletin 0day 攻陷 Check Point 旗下软件安全公司](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247491542&idx=2&sn=6500e7b105b4d3af132fb5fc82757a55&scene=21#wechat_redirect)

[Zimbra SNMP 未认证 RCE 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526941&idx=1&sn=11e4c40814e3f01c72e6879ff92a5b4c&scene=21#wechat_redirect)

[Langflow 高危漏洞被用于未认证RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526269&idx=2&sn=0d7a31b3a12799330b0f67e3123dcd7c&scene=21#wechat_redirect)

[SolarWinds 修复四个严重漏洞，可导致未认证RCE和认证绕过](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525028&idx=3&sn=70181900e6f00cf38ce9655f395495d9&scene=21#wechat_redirect)

[速修复！React满分漏洞同时影响 Next.js，可导致未认证RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524584&idx=2&sn=d601040ac12c82888e8edba633d2fc02&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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