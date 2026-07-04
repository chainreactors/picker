---
title: Adobe ColdFusion 多个漏洞细节已公开，可导致远程代码执行
url: https://mp.weixin.qq.com/s/0mQcoUGa_IL4s6D_eJMVww
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:46:45.498007
---

# Adobe ColdFusion 多个漏洞细节已公开，可导致远程代码执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dZ7ia5iaWFzz919FvLHUcImzPicib7PDsDrFb4ia8EBFEFykgPkxQDrzvUAWXn6lsiaPYiar0EuxeRoSTKmnN9bibJltU0l8ia8FDgytAYSKvvRFsIDE/0?wx_fmt=jpeg)

# Adobe ColdFusion 多个漏洞细节已公开，可导致远程代码执行

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Adobe ColdFusion 曝出远程开发服务（RDS）无需认证高危路径穿越漏洞（CVE-2026-48282，CVSS 10.0），攻击者在特定配置下无需任何凭据，仅需构造特制 HTTP POST 请求，即可在 ColdFusion 服务当前运行账户权限上下文中实现远程代码执行。攻击者可能据此执行恶意命令、写入后门文件、访问应用可访问的数据，并进一步扩大对服务器的控制范围。

**利用前置条件：**

* 已启用 ColdFusion RDS
* 未启用 RDS 身份验证

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Adobe ColdFusion 路径穿越漏洞 | | |
| **漏洞编号** | CVE-2026-48282 | | |
| **公开时间** | 2026-06-30 | **POC状态** | **已公开** |
| **漏洞类型** | 路径穿越 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 10.0 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的软件版本：

Adobe ColdFusion 2025 <= Update 9

Adobe ColdFusion 2023 <= Update 20

**02**

**修复建议**

**正式防护方案**

受影响用户请立即升级至以下版本或更高版本：

Adobe ColdFusion 2025 用户请升级至 Update 10

Adobe ColdFusion 2023 用户请升级至 Update 21

**03**

**漏洞描述**

近日，安全研究人员披露了 Adobe ColdFusion 中存在的路径穿越漏洞（CVE-2026-48282）。该漏洞源于系统的远程开发服务（RDS）模块在处理文件操作命令时，缺乏有效的路径规范化与边界校验。当服务器开启 RDS 功能且未启用身份验证时，攻击者可以通过特定的 RPC 协议格式向后端服务发送特制的 FILEIO 写入请求，利用路径穿越序列突破 Web 根目录限制，在系统任意位置写入恶意的 CFML 脚本文件，最终在当前用户上下文中实现任意代码执行，导致系统失控。

研究人员同期公开了 ColdFusion RDS FILEIO 任意文件读取漏洞。研究显示，在启用 RDS 且未启用 RDS 身份验证的特定配置下，攻击者可向 FILEIO 接口发送构造的文件读取请求，读取服务器上的任意敏感文件，包括系统配置、应用配置及凭据文件等。根据研究人员的补丁比对推测，可能对应 Adobe 同期修复的 CVE-2026-48313。

研究人员还公开了 ColdFusion 内置 CKEditor 文件管理器文件上传路径穿越漏洞。当文件管理器上传功能被显式启用后，未经认证的攻击者可在上传请求的路径参数中插入路径穿越序列，使上传文件突破预期目录限制并写入指定位置。若危险类型文件被写入 Web 可访问目录，可能进一步导致远程代码执行。根据研究人员的补丁比对推测，可能对应 Adobe 同期修复的 CVE-2026-48276。

**04**

**漏洞复现**

360漏洞研究院已成功复现Adobe ColdFusion 路径穿越漏洞（CVE-2026-48282），通过构造特制 HTTP 请求，成功在服务器上触发了远程代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz9cOanNccMUEQPa5fjStpkS2VWzJg5n5AvDKCJcdTed9oy5AcHAOqWtdWibliavUIxUNu4Ik4IZGPynSPw2iaPEARK3YvL4pBarN8/640?wx_fmt=png&from=appmsg)

图1 发送 Payload

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzzice8zicB5icNqP2zPMVwibplmWCVxe9aoDXdtvqPesjbr40XtUJ4JaF0R5u5ibxPNwnxP3Auh4x6wTCnkQG7dQibzHqD05yJDwCK3Mc/640?wx_fmt=png&from=appmsg)

图2 CVE-2026-48282 Adobe ColdFusion 路径穿越漏洞复现

**05**

**产品侧支持情况**

**360安全智能体：**支持该漏洞攻击的智能分析**。**

**360测绘云 Quake**：默认支持该产品的指纹识别。

**360高级持续性威胁预警系统**：预计 2026年7月6日发布规则更新包，支持该漏洞利用行为的检测。

**360资产与漏洞检测管理系统**：预计 2026年7月6日发布规则更新包，支持该漏洞利用行为的检测。
**本地安全大脑**：默认支持该漏洞的PoC检测。

**06**

**时间线**

2026年7月3日，360漏洞研究院发布本安全风险通告。

**07**

**参考链接**

https://nvd.nist.gov/vuln/detail/CVE-2026-48282

https://labs.watchtowr.com/its-37oc-and-all-we-can-think-about-is-coldfusion-adobe-coldfusion-security-bulletin-apsb26-68-cve-bonanza/

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