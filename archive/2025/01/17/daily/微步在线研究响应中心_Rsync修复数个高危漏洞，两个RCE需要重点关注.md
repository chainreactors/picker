---
title: Rsync修复数个高危漏洞，两个RCE需要重点关注
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507685&idx=1&sn=f6f13d9e6ca46b986c4c17ce7424d252&chksm=cfcabdf1f8bd34e7a4bb18b1d16702e6a4feb5c65a3c5642728ea446c51edaaba876ffe2c928&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2025-01-17
fetch_date: 2025-10-06T20:10:48.442043
---

# Rsync修复数个高危漏洞，两个RCE需要重点关注

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSibfONW0ib18vsxvniae0dvDGyNH4YzdjmskGMeKXoCGr0Cr6FzbVsxu5w/0?wx_fmt=jpeg)

# Rsync修复数个高危漏洞，两个RCE需要重点关注

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png)

**漏洞概况**

Rsync 是一个强大的、快速的、通用的文件同步工具。它可以实现本地或远程主机之间的文件和目录同步，并且在传输过程中只同步差异部分，大大节省了带宽和时间。它是一个命令行工具，通常用于备份、镜像、数据迁移等场景。

微步情报局监控到Rsync官方修复了6个漏洞，其中：

* XVE-2024-38820(CVE-2024-12084)和XVE-2024-38810(CVE-2024-12085)为服务端缓冲区溢出漏洞，影响Rsync守护进程（Rsyncd），攻击者只需要拥有对Rsync服务器匿名读取（常见于公开镜像站）的权限，成功利用以上漏洞则可在该服务器上远程执行任意命令；
* XVE-2024-38860(CVE-2024-12087)和XVE-2024-38861(CVE-2024-12088)为路径穿越漏洞，当Rsync使用--inc-recursive和--safe-links参数时，会分别受以上两个漏洞影响；
* XVE-2024-38859(CVE-2024-12086)为客户端文件读取漏洞，成功利用该漏洞可导致恶意的Rsync服务器能读取任意Rsync客户端文件，但该漏洞的利用较为复杂；
* XVE-2024-38862(CVE-2024-12747)为客户端条件竞争导致的提权漏洞，已经拥有低权限的攻击者成功利用此漏洞可绕过Rsync对符号链接的校验，读取敏感文件，从而造成权限提升。

以上漏洞PoC暂未公开，微步情报局将持续追踪以上漏洞。鉴于Rsync使用较广，建议受影响的客户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：****中**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-38810(CVE-2024-12085)  XVE-2024-38820(CVE-2024-12084) |
| 漏洞类型 | 缓冲区溢出 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 无 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

#

**综合处置优先级：****低**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-38860(CVE-2024-12087)  XVE-2024-38861(CVE-2024-12088) |
| 漏洞类型 | 路径遍历 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 无 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

#

**综合处置优先级：****低**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-38859(CVE-2024-12086) |
| 漏洞类型 | 文件读取 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 无 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

#

**综合处置优先级：****中**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-38862(CVE-2024-12747) |
| 漏洞类型 | 权限提升 |
| **利用条件评估** | 利用漏洞的网络条件 | 本地 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 无 |
| 利用漏洞的权限要求 | 低权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Redhat - Rsync |
| **受影响版本** | 缓冲区溢出漏洞：      XVE-2024-38820 (CVE-2024-12084)：3.2.7 < version < 3.4.0  XVE-2024-38810 (CVE-2024-12085)：version < 3.4.0  路径遍历漏洞：  XVE-2024-38860 (CVE-2024-12087)：version < 3.4.0  XVE-2024-38861 (CVE-2024-12088)：version < 3.4.0  文件读取漏洞：  XVE-2024-38859 (CVE-2024-12086)：version < 3.4.0  权限提升漏洞：  XVE-2024-38862 (CVE-2024-12747)：version < 3.4.0 |
| **有无修复补丁** | 有 |

**修复方案**

**官方修复方案：**

Rsync官方已发布漏洞公告，请尽快前往下载最新版本：

https://lists.samba.org/archive/Rsync-announce/2025/000120.html

## **临时修复方案：**

##

1. 修改Rsyncd的配置，添加 auth users 和 secrets file 配置，并创建包含用户和密码的密码文件，禁止 Rsync 的匿名读取权限。
2. 使用流量防护设备，对使用Rsync协议传输敏感文件的流量进行阻断防护。

- END -

//

**微步漏洞情报订阅服务**

微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：

* 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；
* 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；
* 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；
* 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新。

扫码在线沟通

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png)

点此电话咨询

**X漏洞奖励计划**

“X漏洞奖励计划”是微步X情报社区推出的一款针对未公开漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。

活动详情：https://x.threatbook.com/v5/vulReward

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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