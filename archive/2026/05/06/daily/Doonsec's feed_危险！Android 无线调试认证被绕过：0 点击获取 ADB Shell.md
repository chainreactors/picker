---
title: 危险！Android 无线调试认证被绕过：0 点击获取 ADB Shell
url: https://mp.weixin.qq.com/s/Axi6XZlFmiihXcARsPDwUw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:33:11.615742
---

# 危险！Android 无线调试认证被绕过：0 点击获取 ADB Shell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dZ7ia5iaWFzz8TCzTjSdTgaSdhibBVFTN5VKnibicyn4lfMoqN2z0cazic4nibUvgC7ezrGibFYgc94dduk4icoibaIMfk6bY3tfJJgomaPfTC21hyg4k/0?wx_fmt=jpeg)

# 危险！Android 无线调试认证被绕过：0 点击获取 ADB Shell

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Android ADB 曝出认证绕过高危漏洞（CVE-2026-0073，CVSS 3.1：8.8），攻击者通过构造特定算法的 TLS 证书，可绕过主机 RSA 密钥配对校验，直接获取目标设备的 Shell 权限。

漏洞触发前置条件：

* 设备开启 Developer options 和 Wireless debugging 或暴露 ADB TCP 服务。
* 设备/data/misc/adb/adb\_keys文件包含至少一个先前配对的 RSA ADB 主机密钥。
* 攻击者能够访问该 ADB TCP 端口，例如处于同一局域网。

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Android ADB认证绕过漏洞 | | |
| **漏洞编号** | CVE-2026-0073 | | |
| **公开时间** | 2026-05-05 | **POC状态** | **已公开** |
| **漏洞类型** | 鉴权绕过 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 8.8 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的软件版本：

Android 14、Android 15、Android 16、Android 16-qpr2 中未合入 2026 年 5 月安全补丁的版本。Google 公告说明，2026-05-01 或更高安全补丁级别已修复该问题；该漏洞归属 Android System 组件，子组件为 adbd。

**02**

**修复建议**

**正式防护方案**

普通个人用户应尽快应用安全补丁，设备应升级到包含修复的谷歌2026年5月安全补丁。

**临时防护措施**

* 关闭 Developer options 中的 Wireless debugging。
* 不要在公共 Wi-Fi、企业访客网络等不可信网络中开启无线调试。
* 清理已配对的无线调试设备。

**03**

**漏洞描述**

CVE-2026-0073 是 Android adbd 无线调试 / ADB-over-TCP 认证绕过漏洞。漏洞根因在 packages/modules/adb/daemon/auth.cpp 的 adbd\_tls\_verify\_cert()：adbd 会将 TLS 客户端证书公钥与 /data/misc/adb/adb\_keys 中保存的 RSA 主机公钥进行比较，但代码使用 if (EVP\_PKEY\_cmp(...)) 判断认证结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz8zbXYJBVKVTJuCa8MiaOSTasTHACDA4Cva7MkXuqObAg0ptEpNbibDSbXEnkfTWpUYrcs0Bk9n8ndmRW5ACdXwgOW2gP3eXQptI/640?wx_fmt=png&from=appmsg)

EVP\_PKEY\_cmp() 返回 1 才表示匹配，返回 0 表示不匹配，返回 -1 表示密钥类型不同；由于 -1 在 C/C++ 中也为 true，攻击者提交 EC/Ed25519 等非 RSA 证书时，RSA vs 非 RSA 的比较失败会被误判为认证成功，从而绕过 ADB 主机认证并获得 Shell 用户权限。

**04**

**漏洞复现**

360漏洞研究院已成功复现Android ADB认证绕过漏洞（CVE-2026-0073），获得远程设备的 Shell 用户权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzzicRVyibgE6B27DZgg8Y4mx6OmJafZ16gXYLj6icuADveKTQZhfgIVLqx5XNUzfVSa1MEicf2WsBvFIpuBbWpBHpJpZW4adqk0MGic4/640?wx_fmt=png&from=appmsg)

CVE-2026-0073 Android ADB认证绕过漏洞复现

**05**

**时间线**

2026年05月06日，360漏洞研究院发布本安全风险通告。

**06**

**参考链接**

https://source.android.com/docs/security/bulletin/2026/2026-05-01

https://barghest.asia/blog/cve-2026-0073-adb-tls-auth-bypass/

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