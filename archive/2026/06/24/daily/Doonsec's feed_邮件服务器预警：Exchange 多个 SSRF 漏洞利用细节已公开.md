---
title: 邮件服务器预警：Exchange 多个 SSRF 漏洞利用细节已公开
url: https://mp.weixin.qq.com/s/52YAM_DXiI9hE4eXddOVlw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:00:58.946671
---

# 邮件服务器预警：Exchange 多个 SSRF 漏洞利用细节已公开

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzzicaxRzqTMxPI2LABRSACjj0lOJAPjNQFTwic3MApN3kpETcnF36q42GfwpRkUTgGBHXHKyc40Cwy4ibeltNd0ZKM1ulsYqF66yDk/0?wx_fmt=jpeg)

# 邮件服务器预警：Exchange 多个 SSRF 漏洞利用细节已公开

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Microsoft Exchange Server 曝出两处高危服务器端请求伪造漏洞（CVE-2026-45502，CVSS 5.0；CVE-2026-45504，CVSS 8.8）。低权限邮箱用户可通过构造 EWS InstallApp 请求，诱导 Exchange 服务端发起任意内部或外部 HTTP/HTTPS 请求，实现内网资源探测与信息收集，并在特定条件下扩大 SSRF 影响范围，访问更高权限上下文资源。

**利用前置条件：**

* 攻击者需持有有效 Exchange 低权限邮箱账号
* 目标系统 EWS 接口可正常访问
* 允许触发 InstallApp/ManifestUrl 请求流程

目前 **360漏洞挖掘智能体已成功复现该系列漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Microsoft Exchange Server SSRF 漏洞 | | |
| **漏洞编号** | CVE-2026-45502  CVE-2026-45504 | | |
| **公开时间** | 2026-06-09 | **POC状态** | **已公开** |
| **漏洞类型** | SSRF | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 5.0 / 8.8 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的软件版本：

Microsoft Exchange Server 2016 Cumulative Update 23 < 15.01.2507.069

Microsoft Exchange Server 2019 Cumulative Update 14 < 15.02.1544.041

Microsoft Exchange Server 2019 Cumulative Update 15 < 15.02.1748.046

Exchange Server Subscription Edition RTM < 15.02.2562.043

**02**

**修复建议**

**正式防护方案**

**方法一.使用Windows Update更新**

自动更新：

Microsoft Update默认启用，当系统检测到可用更新时，将会自动下载更新并在下一次启动时安装。

手动更新：

1、点击“开始菜单”或按Windows快捷键，点击进入“设置”。

2、选择“更新和安全”，进入“Windows更新”。

3、选择“检查更新”，等待系统将自动检查并下载可用更新。

4、重启计算机，安装更新系统重新启动后，可通过进入“Windows更新”->“查看更新历史记录”查看是否成功安装了更新。对于没有成功安装的更新，可以点击该更新名称进入微软官方更新描述链接，点击最新的SSU名称并在新链接中点击“Microsoft 更新目录”，然后在新链接中选择适用于目标系统的补丁进行下载并安装。

**方法二. 手动安装补丁**

Microsoft官方下载相应补丁进行更新。

安全更新下载链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45502

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45504

1.点击打开上述链接。

2.在微软公告页面底部左侧【产品】选择相应的系统类型，点击右侧【下载】处打开补丁下载链接。

3.点击【安全更新】，打开补丁下载页面，下载相应补丁并进行安装。

4.安装完成后重启计算机。

**03**

**漏洞描述**

近日，安全研究人员公开披露 Microsoft Exchange Server EWS 模块中存在 SSRF 相关漏洞（CVE-2026-45502、CVE-2026-45504）。攻击者在获取低权限邮箱凭据后，可通过构造特定 EWS 请求触发服务端请求行为，从而影响 Exchange 服务器对外部资源的访问与校验逻辑。

CVE-2026-45502 存在于 EWS InstallApp 功能对 ManifestUrl 参数的处理流程中。由于本地部署环境下内网地址校验逻辑未正确生效，攻击者可诱导 Exchange 服务器访问任意内外部 URL，实现内网服务探测、端口扫描及基础信息泄露。

CVE-2026-45504 影响 EWS 请求处理过程中的安全校验逻辑。在特定请求条件下，服务器对目标 URL 的访问控制与身份约束存在缺陷，攻击者可利用该问题诱导 Exchange 发起非预期网络请求，从而扩大可访问的内外部资源范围，造成更高风险的 SSRF 滥用场景。

**04**

**漏洞复现**

360 漏洞研究院已成功复现 CVE-2026-45502、CVE-2026-45504 两个 Microsoft Exchange Server SSRF 漏洞，分别通过服务端发起远程服务器访问与读取 Exchange 服务器本地文件两类利用场景完成了漏洞验证。

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz9fwKyKnhtTjqjmtrx6tcFdd9Yt9e5aTaa7tcnlkCwIttsdVWoBMquG0ic8p1LOrv2KLWHGjkCehww3AcVxuHAD4YzU5Mia7XibxQ/640?wx_fmt=png&from=appmsg)

发送 Payload

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzzic0cgN1MBA32byQpMSfP6IicT2aOFmFvegKDibQUibrABDibFSjkuMFnZMN2MFTE3W63cwGKBtjW1Tc3ibmBxd3EJXRcoygNuDUkVhw/640?wx_fmt=png&from=appmsg)

CVE-2026-45502 Microsoft Exchange Server SSRF 漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzziciasoorQkW0icuamrSarIgeyfaqFBNd6k8CGsHvRXLEQf3QBxQWWHW2ov5YkfB7NiakIXYu4wnobtZLhu8FxjC8y0C3gT0zcK85o/640?wx_fmt=png&from=appmsg)

CVE-2026-45504 Microsoft Exchange Server SSRF 漏洞复现

**05**

**产品侧支持情况**

**360安全智能体：**支持该系列漏洞攻击的智能分析**。**

**360测绘云 Quake**：默认支持该产品的指纹识别。

**360高级持续性威胁预警系统**：预计 2026年6月25日发布规则更新包，支持该系列漏洞利用行为的检测。

**360资产与漏洞检测管理系统**：预计 2026年6月25日发布规则更新包，支持该系列漏洞利用行为的检测。
**本地安全大脑**：默认支持该系列漏洞的PoC检测。

**06**

**时间线**

2026年6月24日，360漏洞研究院发布本安全风险通告。

**07**

**参考链接**

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45502

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45504

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