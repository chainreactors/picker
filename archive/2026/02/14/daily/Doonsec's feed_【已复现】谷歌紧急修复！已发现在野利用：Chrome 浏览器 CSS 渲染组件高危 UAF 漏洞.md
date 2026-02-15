---
title: 【已复现】谷歌紧急修复！已发现在野利用：Chrome 浏览器 CSS 渲染组件高危 UAF 漏洞
url: https://mp.weixin.qq.com/s/5IdXMdgtz98_PZTspdkq_Q
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:39.740415
---

# 【已复现】谷歌紧急修复！已发现在野利用：Chrome 浏览器 CSS 渲染组件高危 UAF 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzz8ZOmxOVmYMj94kKU7iaYLsr8CmLPhuScQUUOgmfO3uuwRw0SZf2VxZuppDic2HkhlAicsjaXahYzVZwlGHgsBehAIOSP18Oia6T1I/0?wx_fmt=jpeg)

# 【已复现】谷歌紧急修复！已发现在野利用：Chrome 浏览器 CSS 渲染组件高危 UAF 漏洞

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器中沉浸阅读

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg)

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Chrome CSS 渲染组件释放后重用漏洞 | | |
| **漏洞编号** | CVE-2026-2441 | | |
| **公开时间** | 2026-02-13 | **POC状态** | **已公开** |
| **漏洞类型** | UAF | **EXP状态** | 未公开 |
| **利用可能性** | 高 | **技术细节状态** | 未公开 |
| **CVSS 3.1** | 8.8 | **在野利用状态** | **已发现** |

**01**

**影响组件**

Google Chrome 是由 Google 开发的一款网页浏览器，凭借其稳定、安全及高效的浏览体验，占据了目前最高的市场份额。作为 Chrome 及 Chromium 的核心组件，Blink 渲染引擎负责解析 HTML 与 CSS，并执行页面的排版与渲染，它对 CSS 字体样式设计能力的支持，便于开发者统一且精细地管理网页字体显示效果。正是鉴于 Chrome 的广泛普及，Blink 引擎也成了攻击者眼中的高价值目标。

**02**

**漏洞描述**

2026年2月13日，Google 安全团队发布紧急安全公告，披露了一个 Chrome 浏览器 Blink的CSS渲染模块中的高危漏洞，该漏洞CVE编号为CVE-2026-2441，其内部Issue ID为483569511。该漏洞的根本原因在于CSSFontFeatureValuesMap 在迭代期间允许对底层 map 修改，导致迭代器失效，从而进一步引发内存安全问题。

该漏洞已被**确认存在在野利用**，攻击者可以通过构造恶意网页并诱导用户访问，从而在浏览器沙箱内执行任意代码。Google 官方已在新版本中修复此漏洞，并强烈建议所有用户立即更新。

**03**

**漏洞复现**

360 漏洞研究院已复现 CSSFontFeatureValuesMap 迭代器失效释放后重用漏洞（CVE-2026-2441），通过构造恶意HTML网页，成功在Chrome 浏览器上触发漏洞，并打印崩溃日志。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz9rq9fCVepPfG5zYmg9R6HQAYaugiaUiaod88W9OGRsWj5TnKjr7P9QDo4ru0icbKPolm7CfiancVnHEeq5Jeoj6rniaIZQ6Gos4Y8M/640?wx_fmt=png&from=appmsg)

CVE-2026-2441 Chrome CSS 渲染组件释放后重用漏洞复现

**04**

**漏洞影响范围**

受影响版本：

Google Chrome(Windows) < 145.0.7632.75/76

Google Chrome(Mac) < 145.0.7632.75/76

Google Chrome(Linux) < 145.0.7632.75

**05**

**修复建议**

**正式防护方案**

一. 自动更新

1. 打开 Google Chrome 浏览器

2. 点击右上角的三点菜单(⋯)

3. 选择"帮助" -> "关于Google Chrome"

4. 浏览器将自动检查并下载更新，下载完成后点击"重新启动"应用修复

二. 手动更新

通过 Chrome 官方网站下载最新安装包并安装：

- Google Chrome(Windows) >=  145.0.7632.75/76

- Google Chrome(Mac) >= 145.0.7632.75/76

- Google Chrome(Linux) >=  145.0.7632.75

官方下载地址：https://www.google.cn/chrome/

**06**

**时间线**

2026年2月14日，360漏洞研究院发布本安全风险通告。

**07**

**参考链接**

https://chromereleases.googleblog.com/2026/02/extended-stable-updates-for-desktop\_13.html

https://nvd.nist.gov/vuln/detail/CVE-2026-2441

**08**

**更多漏洞情报**

建议您订阅360数字安全-漏洞情报服务，获取更多漏洞情报详情以及处置建议，让您的企业远离漏洞威胁。

邮箱：360VRI@360.cn

网址：https://vi.loudongyun.360.net

**“洞”悉网络威胁，守护数字安全**

**关于我们**

360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

360漏洞研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

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