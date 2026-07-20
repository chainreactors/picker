---
title: 非插件漏洞，WordPress 未授权 SQL 注入漏洞链可导致RCE
url: https://mp.weixin.qq.com/s/c8LpSEejoer04N1LiVFeqA
source: Doonsec's feed
date: 2026-07-19
fetch_date: 2026-07-20T05:31:27.111830
---

# 非插件漏洞，WordPress 未授权 SQL 注入漏洞链可导致RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzz9mta08ciceSc6l9x1Z5P3PI1EMpLKZawMIRIBmgt05gkn0pFvCSySs9QJ5zialZ4DsbvV1JhKaED3iaMl0p7N5IczIrPBlTTCCQY/0?wx_fmt=jpeg)

# 非插件漏洞，WordPress 未授权 SQL 注入漏洞链可导致RCE

山河学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于360漏洞研究院
，作者360漏洞研究院

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM4RI3VMgOt49J6uCpV1EZYmQBGpHBeafcxet1LBmQy8FA/0)

**360漏洞研究院**
.

“洞”悉网络威胁，守护数字安全。

WordPress 曝出 REST API 路由混淆与 SQL 注入漏洞（CVE-2026-63030、CVE-2026-60137），攻击者无需身份认证即可通过漏洞链触发数据库查询，实现管理员账户信息泄露。可实现未授权 SQL 注入获取管理员密码哈希，再通过破解管理员密码并利用插件安装功能可实现代码执行。

**利用前置条件：**

* 攻击者能够通过网络访问目标 WordPress 站点

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | WordPress REST API 路由混淆与 SQL 注入漏洞 | | |
| **漏洞编号** | CVE-2026-63030 / CVE-2026-60137 | | |
| **公开时间** | 2026-07-18 | **POC状态** | **已公开** |
| **漏洞类型** | 路由混淆 /  SQL注入 | **EXP状态** | 未公开 |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 7.5 / 9.1 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的软件版本：

7.0.0 <= WordPress < 7.0.2

6.9.0 <= WordPress < 6.9.5

6.8.0 <= WordPress < 6.8.6（仅受 CVE-2026-60137 影响）

**02**

**修复建议**

**正式防护方案**

官方已发布安全版本

WordPress 7.0.x 版本升级到 7.0.2 及以上版本

WordPress 6.9.x 版本升级到 6.9.5 及以上版本

WordPress 6.8.x 版本升级到 6.8.6 及以上版本

**03**

**漏洞描述**

近日，WordPress 公开披露了核心组件中存在的 REST API 路由混淆漏洞（CVE-2026-63030）以及 SQL 注入漏洞（CVE-2026-60137）。其中，CVE-2026-63030 源于 REST API Batch 接口处理多个子请求时，路由匹配结果与权限校验结果数组不同步，导致攻击者能够绕过部分请求限制，将特殊构造的请求分发到错误处理逻辑。结合 CVE-2026-60137 中的 WP\_Query 查询参数 SQL 注入缺陷，攻击者可通过未认证 REST API 请求触发数据库查询，实现布尔型或时间型 SQL 注入，并读取数据库中的用户信息，包括管理员账户密码哈希。公开 PoC 已经验证该攻击路径可以恢复管理员哈希数据。后续攻击者可在离线环境破解管理员密码，并通过 WordPress 管理员插件安装功能部署恶意插件实现代码执行。

**04**

**漏洞复现**

360漏洞研究院已成功复现 WordPress REST API 路由混淆与 SQL 注入漏洞（CVE-2026-63030、CVE-2026-60137），通过 SQL 注入成功读取 wp\_users 表数据并获取管理员密码哈希，验证了未授权数据库信息泄露风险。

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz8ydwlia2XpTRfXoUeZXoPMACia4PQZKUicewoBibBr8IAicibnLALM6zx4f9M18rWenZtWj5DmNoy43p70P3wGyQNRxiawc1xX1ZzYjY/640?wx_fmt=png&from=appmsg)

CVE-2026-63030、CVE-2026-60137

WordPress REST API 路由混淆与 SQL 注入漏洞复现

**05**

**产品侧支持情况**

**360安全智能体：**支持该漏洞攻击的智能分析**。**

**360测绘云 Quake**：默认支持该产品的指纹识别。

**360高级持续性威胁预警系统**：预计 2026年7月20日发布规则更新包，支持该漏洞利用行为的检测。

**360资产与漏洞检测管理系统**：预计 2026年7月20日发布规则更新包，支持该漏洞利用行为的检测。
**本地安全大脑**：默认支持该漏洞的PoC检测。

**06**

**时间线**

2026年7月19日，360漏洞研究院发布本安全风险通告。

**07**

**参考链接**

https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-ff9f-jf42-662q

https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-fpp7-x2x2-2mjf

https://wordpress.org/news/2026/07/wordpress-7-0-2-release/

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0sjvG0TycCrkwqc9NOyXnxJdd3Sx952ibuNc9JbaRIwgribBX5MRFHecGVwgntRMicphmT55OA24qTJdzwXhegujQ/0?wx_fmt=png)

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