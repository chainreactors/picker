---
title: 1 个字符 Bug，脚本直接拿下 FreeBSD Root 权限
url: https://mp.weixin.qq.com/s/XAS6LUIgKYdWuKKMe_PbRg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:12.360265
---

# 1 个字符 Bug，脚本直接拿下 FreeBSD Root 权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzzibzicA2RSnywQZQq0eKOC1zt8hM3V6Gcpa2RyvSk71R9icVichp7kzibr7tFzYSmvGTKMEUQ335cEiaNoic6soiavcDq3suLcGKJTHEEs/0?wx_fmt=jpeg)

# 1 个字符 Bug，脚本直接拿下 FreeBSD Root 权限

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

FreeBSD 曝出本地提权漏洞（CVE-2026-7270，CVSS：7.8），攻击者利用内核 execve() 函数中的运算符优先级缺陷，通过精心构造的缓冲区溢出，可直接获取操作系统最高管理员权限。

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | FreeBSD execve 本地权限提升漏洞 | | |
| **漏洞编号** | CVE-2026-7270 | | |
| **公开时间** | 2026-04-30 | **POC状态** | **已公开** |
| **漏洞类型** | 本地权限提升 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 7.8 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的软件版本：

FreeBSD 15.0 系列 < 15.0-RELEASE-p7

FreeBSD 14.4 系列 < 14.4-RELEASE-p3

FreeBSD 14.3 系列 < 14.3-RELEASE-p12

FreeBSD 13.5 系列 < 13.5-RELEASE-p13

**02**

**修复建议**

**正式防护方案：**

官方已发布安全补丁，请立即升级至最新版本：

FreeBSD 15.0-RELEASE p7 或更高

FreeBSD 14.4-RELEASE p3 或更高

FreeBSD 14.3-RELEASE p12 或更高

FreeBSD 13.5-RELEASE p13 或更高

**03**

**漏洞描述**

CVE-2026-7270 是 FreeBSD 内核 execve 参数处理流程中的本地提权漏洞，问题位于 kern\_exec.c ，由于 memmove 长度计算错误，导致特定情况下发生越界内存复制（OOB memmove），破坏 exec\_map 中相邻数据结构。攻击者可利用OOB污染后续由 root 执行的进程环境，实现敏感环境变量注入。

漏洞触发依赖本地低权限账户、特定参数布局以及进程执行时序。公开分析中，攻击链通常利用 sshd fork/exec sshd-session 的窗口，通过覆盖环境变量注入 LD\_PRELOAD，使恶意动态库在 root 权限下加载执行，最终实现本地权限提升。漏洞还可能导致内核 panic 或系统异常。

**04**

**漏洞复现**

360漏洞研究院已成功复现 FreeBSD execve 本地权限提升漏洞（CVE-2026-7270），通过该漏洞在 FreeBSD 中实现权限提升。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzz8MsvmxCeDLpF8icgq7pVickmIKYzDR4QicssPdLfeuib1riadGiccks2YZTL69pgzaInb6D8eYLVbgurCYQPXyMOSeBNp6xuqPDHWiac/640?wx_fmt=jpeg&from=appmsg)

CVE-2026-7270 FreeBSD execve 本地权限提升漏洞复现

**05**

**时间线**

2026年05月09日，360漏洞研究院发布本安全风险通告。

**06**

**参考链接**

https://nvd.nist.gov/vuln/detail/CVE-2026-7270

**07**

**更多漏洞情报**

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg)

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