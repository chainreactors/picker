---
title: Joomla! 多个扩展存在未授权RCE漏洞
url: https://mp.weixin.qq.com/s/VmMBhvHaVHaf9g1WkkLvlw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:04:01.653187
---

# Joomla! 多个扩展存在未授权RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzz83v0hJGaG1eVNiaHbKNPfjh8NribuZBpu5u9jx1Roy5HlCNq8hCw9oKG5RWnznXaB7UQibjhlOHFZ9jsCzNmZh1eZ8sGWdZhDRLE/0?wx_fmt=jpeg)

# Joomla! 多个扩展存在未授权RCE漏洞

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Joomla! 广泛集成的 JCE Editor 与 SP Page Builder 扩展组件曝出未授权任意文件上传漏洞，攻击者无需认证即可通过接口上传恶意脚本，实现稳定的远程代码执行并控制服务器。

**利用前置条件：**

* 目标系统已安装并启用受影响版本的 JCE Editor（1.0.0 ~ 2.9.99.4）或 SP Page Builder（1.0.0 ~ 6.6.1）
* 相关组件的功能接口对外可访问

目前 **360漏洞挖掘智能体已成功复现该系列漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Joomla! JCE Editor 与 SP Page Builder 未授权任意文件上传漏洞 | | |
| **漏洞编号** | CVE-2026-48907  CVE-2026-48908 | | |
| **公开时间** | 2026-06-05  2026-06-20 | **POC状态** | **已公开** |
| **漏洞类型** | 文件上传 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 4.0** | 10.0 | **在野利用状态** | **已发现** |

**01**

**漏洞影响范围**

受影响的软件版本：

1.0.0 <= JCE Editor <= 2.9.99.4

1.0.0 <= SP Page Builder <= 6.6.1

**02**

**修复建议**

**正式防护方案**

升级至以下或更高的安全版本：

JCE Editor >= 2.9.99.5

SP Page Builder >= 6.6.2

**03**

**漏洞描述**

两个漏洞均源于对用户上传功能的信任过度及验证缺失，但具体利用链条略有不同：

CVE-2026-48907 (JCE Editor)存在于 JCE 扩展的配置导入功能中。攻击者首先通过访问目标首页提取 CSRF 令牌，随后向 index.php?option=com\_jce&task=profiles.import 接口发送恶意请求。该接口允许上传看似 XML 配置文件的恶意 PHP 脚本。由于服务端未严格校验上传文件的实际内容及扩展名，攻击者可将 PHP Webshell 伪装成配置文件上传至 /tmp/ 等可访问目录，并通过 HTTP 请求直接执行，从而获取服务器权限。

CVE-2026-48908 (SP Page Builder) 位于 SP Page Builder 的 asset.uploadCustomIcon 任务中。该接口允许未认证用户上传自定义图标字体包（ZIP 格式）。攻击者利用服务端文件名过滤的大小写敏感缺陷（如服务端屏蔽 .php 但未屏蔽 .PHP），结合 .htaccess 文件覆盖服务器配置，实现代码执行。具体而言，攻击者上传包含恶意 .PHP 文件和配置 .htaccess 的 ZIP 包，后者指示 Web 服务器将 .PHP 后缀文件作为 PHP 脚本解析。这种组合拳绕过了常见的扩展名黑名单和服务器默认配置，实现了稳定的远程代码执行。

**04**

**漏洞复现**

360漏洞研究院已成功复现 Joomla! JCE Editor 与 SP Page Builder 未授权任意文件上传漏洞（CVE-2026-48907/48908），通过漏洞以匿名身份上传任意文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzzibicsnfHwFa8wWdCA0X8VaajedDHRKz8RmfKevflfRU2uvcD76bjwpC2GCdbWPtsDIic5WzqGnLEPq8Viae8nB7foHlTqG0LYafAA/640?wx_fmt=png&from=appmsg)

CVE-2026-48907 以匿名身份上传任意文件

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz9UibNft2Dib2L5xxh93ibSIJGC9zoI61pia9ceahDrTEfpkQQ3OYrQjA65eiaQKiahbG6Kicw2mbiaflibeoK0k0BiaplGMpTAQcOia2Y6ak/640?wx_fmt=png&from=appmsg)

CVE-2026-48908 以匿名身份上传任意文件

**05**

**产品侧支持情况**

**360安全智能体：**支持该系列漏洞攻击的智能分析**。**

**360测绘云 Quake**：默认支持该产品的指纹识别。

**360高级持续性威胁预警系统**：预计 2026年6月24日发布规则更新包，支持该系列漏洞利用行为的检测。

**360资产与漏洞检测管理系统**：预计 2026年6月24日发布规则更新包，支持该系列漏洞利用行为的检测。
**本地安全大脑**：默认支持该系列漏洞的PoC检测。

**06**

**时间线**

2026年6月23日，360漏洞研究院发布本安全风险通告。

**07**

**参考链接**

https://www.cve.org/CVERecord?id=CVE-2026-48907

https://www.cve.org/CVERecord?id=CVE-2026-48908

**08**

**更多漏洞情报**

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/dZ7ia5iaWFzz8YToicKab1BicPnEdr7jiatvQUVWSMnYTBeG5ibibgxkGAG1rF4pUdpowPcCmokOO5tp4UjjhUsos4Zf4VwE1aM9NTUz3ogfgdwwFw/640?wx_fmt=gif&from=appmsg)

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