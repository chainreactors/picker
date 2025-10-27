---
title: Progress 提醒注意Telerik Report Server中的严重RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520228&idx=1&sn=d9e2734ebb4a13c747b20000c240d7bd&chksm=ea94be8edde33798e81c133dacfe538263083021026fe777545f067b211569e604c359b9c639&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-27
fetch_date: 2025-10-06T17:43:08.214538
---

# Progress 提醒注意Telerik Report Server中的严重RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS8BY61icLViaX2jVuzSdo1AicjXiaA9fwvfRmpM2Y9ETsaPfgb66T0tpczEy8IN4AdLvh5GBGzCViaCPQ/0?wx_fmt=jpeg)

# Progress 提醒注意Telerik Report Server中的严重RCE漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Progress Software 公司提醒客户修复位于 Telerik Report Server中一个严重的远程代码执行漏洞 (CVE-2024-6327)，它可用于攻陷易受攻击的设备。**

Telerik Report Server 是一款基于服务器的报告平台，为报告以及用于在组织机构范围内创建、部署、交付和管理报告的工具提供中心化存储服务。

该漏洞是因为不可信数据的反序列化弱点造成的，该弱点可被用于在未修复服务器上实施远程代码执行。该漏洞影响 Report Server 2024 Q2 (10.1.24.514) 及更早版本，已在2024 Q2 (10.1.24.709) 版本中修复。

Progress Software 公司在周三的安全公告中提醒称，“更新至 Report Server 2024 Q2 (10.1.24.709) 或后续版本是清除该漏洞的唯一方式。Progress Telerik 团队强烈建议升级至最新版本。”

管理员可通过如下方式检查自己的服务器是否易受这些攻击：
 1、 进入 Report Server web UI 并通过具有管理员权限的账户登录

2、 打开配置页面 (~/Configuration/Index)

3、 选择“关于”标签，版本号会在右边的面板中显示

Progress 还为无法立即升级设备的用户提供了临时的缓解措施。Report Server Application Pool 用户可更改为权限有限的用户。无法创建 IIS 用户并分配 App Pool 程序的用户可参照 Progress 支持文档中的信息缓解该漏洞。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS8BY61icLViaX2jVuzSdo1Aic08icPYmiba5M2ZQ2NShIO5rAJ9AhV8Gnqqjv9KTbNnrrjguCA5VCAAdQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS8BY61icLViaX2jVuzSdo1Aic0fLEG1WJDYcmfW24Z9VN6iaZhhGOqemBs8thUAUP36pzqp6EOJD0YPQ/640?wx_fmt=png&from=appmsg)

**老旧 Telerik 缺陷已遭攻击**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS8BY61icLViaX2jVuzSdo1Aic0fLEG1WJDYcmfW24Z9VN6iaZhhGOqemBs8thUAUP36pzqp6EOJD0YPQ/640?wx_fmt=png&from=appmsg)

虽然 Progress 公司并未分享 CVE-2024-6327 是否已遭在野利用，但其它 Telerik 漏洞近年来已遭攻击。

例如，在2022年，美国一家联邦机构的微软互联网信息服务 (IIS) web 服务器遭 CVE-2019-18935漏洞利用攻击。CISA、FBI和MS-ISAC 发布联合公告指出，至少两个威胁组织（其中一个是越南的XE Group组织）攻陷了该易受攻击的服务器。在这次攻击活动中，威胁行动者部署了多个恶意软件 payload 并收集提取了信息，同时在2022年11月和2023年1月早些时候维护对受陷网络的访问权限。

近期，安全研究人员通过组合利用严重的认证绕过漏洞 (CVE-2024-4358)和高危 RCE 漏洞 (CVE-2024-1800) 开发并发布了针对 Telerik Report Server上 RCE 的 PoC。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[速修复！Progress Telerik 中存在严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519654&idx=1&sn=22b4f342e957ddb68acf5d7dabc14f7b&chksm=ea94bcccdde335da0a488c11021c8d947834829e062cbd4a5917bc946b3037f54a151014c361&scene=21#wechat_redirect)

[速修复Progress Flowmon中的这个CVSS满分漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519358&idx=2&sn=398290f1e1cbf32a9f72ff26e3d708c4&chksm=ea94bd14dde334025bccac4bf83cd4b90113971ba22d26184385ccc5d530c62314ca6d06d349&scene=21#wechat_redirect)

[OpenSSH 易受RCE新漏洞影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520029&idx=2&sn=b58737a69aeafc6a694ae82500739603&chksm=ea94be77dde33761e93ffb3f17cb9934c2daba72097bc6e458bf6b3ad866cd59cf38419701cf&scene=21#wechat_redirect)

[Ghostscript库中的RCE漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520021&idx=1&sn=eac7f44a62e58334fb97c1e5e162e2f7&chksm=ea94be7fdde33769f2de9443ced8789298cfe040ee0d5216a54f3437207c0d8100956627b6f2&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/progress-warns-of-critical-rce-bug-in-telerik-report-server/

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