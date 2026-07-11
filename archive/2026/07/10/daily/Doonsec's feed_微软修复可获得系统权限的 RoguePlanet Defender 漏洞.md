---
title: 微软修复可获得系统权限的 RoguePlanet Defender 漏洞
url: https://mp.weixin.qq.com/s/5UpsjWQCLqXIZ5OJct5y-g
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:01:07.418027
---

# 微软修复可获得系统权限的 RoguePlanet Defender 漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfWDfz281bMiapPKQKRBZ3diayNxgJNTldCN2Kbv4BPaa7Gr52WgsAkoLhTEK1AibCvTAE9X7EsICARNOU7FuILAP6c1gEjRmLkMLo/0?wx_fmt=jpeg)

# 微软修复可获得系统权限的 RoguePlanet Defender 漏洞

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**微软已修复Defender漏洞“RoguePlanet”（CVE-2026-50656，CVSS评分7.8），距离该漏洞的技术细节被公开已过去近一个月。**

该漏洞是位于微软恶意软件保护引擎（“mpengine.dll”）中的一个权限提升问题。该引擎为防病毒和反间谍软件提供扫描、检测和清除功能。该漏洞已在微软恶意软件保护引擎1.1.26060.3008版本中修复，同时微软还发布了深度防御更新，强化未指定的安全相关功能。

RoguePlanet最初由一名ID为Chaotic Eclipse（又名Nightmare-Eclipse）的安全研究人员披露，该漏洞被指为一个竞争条件漏洞，可用于生成具有SYSTEM级别权限的shell，进而使攻击者能够执行任意代码或进行未授权操作。该漏洞利用被指可在安装了2026年6月补丁星期二更新且保持最新状态的Windows系统上运行。随后，Chaotic Eclipse还透露，无论实时保护是否开启，该利用均能生效。微软并未正式将漏洞发现归功于Chaotic Eclipse。

RoguePlanet是 Chaotic Eclipse披露的第四个Defender漏洞，此前三个分别为BlueHammer（CVE-2026-33825）、UnDefend（CVE-2026-45498）和RedSun（CVE-2026-41091），所有这些漏洞均已由微软修复。

微软表示，安装该漏洞的更新，客户无需采取任何操作，该软件会频繁更新，保护客户免受新旧威胁的威胁。微软表示：“对于企业部署和终端用户，微软反恶意软件软件的默认配置有助于确保恶意软件定义和微软恶意软件保护引擎自动保持最新。根据所使用的微软反恶意软件软件及其配置方式，该软件在连接到互联网时，可每天检查一次引擎和定义更新，甚至每天多次检查。客户也可以随时选择手动检查更新。”

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[微软六月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526255&idx=1&sn=b5c19c4120582e72f64c7e7a6e4c4ae4&scene=21#wechat_redirect)

[微软修复影响 SharePoint 多个版本的 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526116&idx=1&sn=2dba11975b0d1b5a35299b0e18f14c1d&scene=21#wechat_redirect)

[微软提醒注意两个已遭利用的 Defender 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526088&idx=1&sn=b80d042e47259040384c71978889be86&scene=21#wechat_redirect)

[微软推出 Defender 漏洞奖励计划，最高奖金$2万](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518206&idx=1&sn=5262405ff7209703aeea0bb434ce7f9d&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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