---
title: 漏洞通告 | Ivanti Cloud Service Appliance 路径穿越漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507011&idx=1&sn=e966bc67a09c85f8e234fadcb822e12b&chksm=cfcabf57f8bd36418bf9a324af25302777a1d6e6ec1f3dfa7c0a2f2d2d55fe4c40778ed553e8&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-09-24
fetch_date: 2025-10-06T18:27:34.611674
---

# 漏洞通告 | Ivanti Cloud Service Appliance 路径穿越漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyicOiatUKcfOxp6WlrpY31eicsUmQ6zRfsr7ibMtkiaeibmdIgCWjP13dCpYg/0?wx_fmt=jpeg)

# 漏洞通告 | Ivanti Cloud Service Appliance 路径穿越漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

Ivanti Cloud Service Appliance (CSA) 是 Ivanti 提供的一款本地部署的虚拟设备，旨在简化和增强 Ivanti 产品与云服务的集成。

微步情报局于近日获取到Ivanti Cloud Service Appliance 路径穿越漏洞情报(https://x.threatbook.com/v5/vul/XVE-2024-27923)。未经认证的攻击者可利用该漏洞访问受限功能，绕过管理员权限校验。据官方描述(https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-CSA-4-6-Cloud-Services-Appliance-CVE-2024-8963?language=en\_US)，该漏洞可结合登陆后RCE XVE-2024-27180(https://x.threatbook.com/v5/vul/XVE-2024-27180)，实现未授权远程执行任意代码。

该漏洞PoC虽暂未被公开，但已被CISA标记在野利用，建议及时修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-27923 |
| 漏洞类型 | 路径穿越 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 已在野利用 | 是 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Ivanti-Cloud Services Appliance |
| **受影响版本** | 4.6 Patch 518 及之前版本 |
| **影响范围** | 千级 |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=title=%22Ivanti(R)%20Cloud%20Services%20Appliance%22

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLiavl8LVJAkJIOyT8RS70zHW8gMTepwESor66HrST34CjToU2yoPE9sI3W0k8Uf2WMiaR9mEcJFvNw/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

目前厂商已发布升级补丁以修复漏洞，补丁获取链接:

https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-CSA-4-6-Cloud-Services-Appliance-CVE-2024-8963?language=en\_US

## **临时修复方案：**

暂无临时修复方案，建议尽快根据官方修复方案升级到指定版本。

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

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

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