---
title: Kernel 新漏洞曝光！多款主流 Linux 发行版存在 Root 本地提权风险
url: https://mp.weixin.qq.com/s/rd9AN4jERTTy7Gok01YGZQ
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:04.885163
---

# Kernel 新漏洞曝光！多款主流 Linux 发行版存在 Root 本地提权风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dZ7ia5iaWFzz8bo4l2nuku6VZCbDrnA8y9sKlrBQsStWcmQRWcPp7MhKIsv5b80RSdJ6Yz70k3yPKlXLiarOlHdq7O1Lx1vskrB1PUicxHk6jLs/0?wx_fmt=jpeg)

# Kernel 新漏洞曝光！多款主流 Linux 发行版存在 Root 本地提权风险

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Linux 内核曝出 net/sched act\_pedit 本地提权漏洞（CVE-2026-46331，CVSS 7.1），低权限攻击者可以提权至 root 权限。

**利用前置条件：**

* 拥有 Linux 低权限账号

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Linux 内核 net/sched act\_pedit 本地提权漏洞 | | |
| **漏洞编号** | CVE-2026-46331 | | |
| **公开时间** | 2026-06-16 | **POC状态** | **已公开** |
| **漏洞类型** | 本地提权 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 7.1 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的内核版本：

v5.18 <= Linux Kernel < v7.1-rc7

影响周期：约 4 年（2022年5月 ~ 2026年6月）

已知受影响发行版：

* RHEL 10.0（内核 6.12.0-228.el10）
* Debian 13 trixie（内核 6.12.90+deb13.1）
* Ubuntu 24.04.4（内核 6.17.0-22）

**02**

**修复建议**

**正式防护方案**

官方修复已经发布commit进行修复。

在修复中将 skb\_ensure\_writable() 调用移入逐键循环内部，使每次写操作前均计算并保护实际写偏移范围；新增偏移算术溢出检查；对影响 headroom 的负偏移增加 skb\_cow() 处理。

链接如下: https://github.com/torvalds/linux/commit/899ee91156e57784090c5565e4f31bd7dbffbc5a

**03**

**漏洞描述**

CVE-2026-46331 是 Linux 内核 net/sched 子系统中 act\_pedit模块的一个部分COW（Copy-on-Write）页缓存污染漏洞。tcf\_pedit\_act() 函数在处理typed key（ PEDIT\_KEY\_EX\_HTYPE\_NETWORK / TRANSPORT）时，仅在进入循环前调用一次 skb\_ensure\_writable()，未将运行时追加的协议头偏移量纳入COW范围计算。攻击者可在 tc 规则中对 loopback 接口添加 act\_pedit 动作：首先将 IP IHL 字段设置为最大值（15），使内核误判报头长度；随后的 TCP 键写操作实际偏移超出已保护的COW范围，直接写入由 sendfile 加载进页缓存的文件页。

**04**

**漏洞复现**

360漏洞研究院已成功复现 Linux 内核 net/sched act\_pedit本地提权漏洞（CVE-2026-46331），通过运行 POC，成功获得 root 权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz9ibAqUjXD5ia9mkU0zlf6iceLrkSsziapRqicuU3WT5ms7icvZNxGFu67uiaiaUwXm7ibBJN4t5LUb5dGibyjtMxIU1km9LPiaHxyv4m2WFM/640?wx_fmt=png&from=appmsg)

CVE-2026-46331

Linux 内核 net/sched act\_pedit 本地提权漏洞复现

**05**

**时间线**

2026年6月17日，360漏洞研究院发布本安全风险通告。

**06**

**参考链接**

https://github.com/torvalds/linux/commit/899ee91156e57784090c5565e4f31bd7dbffbc5a

https://github.com/torvalds/linux/commit/d504a978572202ef43ac5ecfec2030adda64b13e

https://nvd.nist.gov/vuln/detail/CVE-2026-46331

**07**

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