---
title: 漏洞通告 | 已修复！Nacos RCE 漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247506507&idx=1&sn=843cdb4e55d16425fc965f93f16e0c28&chksm=cfcab95ff8bd30493077a4f3294ca470692f064eaa62fbc37008dda2e6870ac49aaac1c5fe91&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-07-20
fetch_date: 2025-10-06T17:43:00.245834
---

# 漏洞通告 | 已修复！Nacos RCE 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyicOiatUKcfOxp6WlrpY31eicsUmQ6zRfsr7ibMtkiaeibmdIgCWjP13dCpYg/0?wx_fmt=jpeg)

# 漏洞通告 | 已修复！Nacos RCE 漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

Nacos是一个动态命名和配置服务的开源项目，旨在帮助用户构建云原生应用。它提供了动态服务发现、配置管理和服务共享等基础设施，适用于各种云环境，包括私有云、混合云和公有云。

2024年7月15日，微步漏洞团队监测到Nacos远程命令执行漏洞（https://x.threatbook.com/v5/vul/XVE-2023-35021）利用工具在Github公开。该漏洞的利用前提为Nacos未开启身份认证（默认未开启，开启身份认证时此利用无法利用），通过SQL注入进而构造RCE。

微步已捕获关于该漏洞的在野利用行为，危害较大，建议受影响的用户尽快修复。另外，微步漏洞团队监控到Nacos于7月18日发布了最新的代码更新（https://github.com/alibaba/nacos/commit/ed7bd03d4c214d68f51654fee3eea7ecf72fd9ab），通过默认禁用derby接口的方式对本漏洞进行了修复，但该修复代码还未合并到发行版本中。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2023-35021 |
| 漏洞类型 | SQL to RCE |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 1. 未开启身份认证  2. 使用derby内置数据库 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 是 |
| 微步已捕获攻击行为 | 是 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Alibaba-Nacos |
| **受影响版本** | version ≤ 2.4.0 BETA   version ≤ 2.3.2 |
| **影响范围** | 万级 |
| **有无修复补丁** | 有 |

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyp2Ksv2Yh7Bcpm57jEYF0NOtbh6C09nUeRPKToFgeHuHL9Ereyxfs7g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyiaP03mhOlMYhpiarCOKwxlDMOfD6OYdRWGiapAh5Dq4nxOVOJjoVAib7ibw/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

官方已经在最新代码中通过默认禁用derby接口的方式对本漏洞进行了修复，但还未合并到发行版本，修复代码如下所示：

https://github.com/alibaba/nacos/commit/ed7bd03d4c214d68f51654fee3eea7ecf72fd9ab

## **临时修复方案：**

* 在不影响业务的情况下，使用MySQL等外置数据库
* 配置Nacos开启身份认证，设置强密码。详细操作过程可参考官方手册：

  https://nacos.io/docs/latest/guide/user/auth/
* 如非必要，避免将资产暴露在互联网

**微步产品侧支持情况**

微步威胁感知平台TDP在**2023年12****月**已支持检测，检测ID为S3100136879，模型/规则高于20231213000000 可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyXdc2jxHqGy4YMJWp31QibCOvV3L5wrsAU6jDOGWEue3BXoR0aIibK8Vw/640?wx_fmt=png&from=appmsg)

微步威胁防御系统OneSIG在**2023年12月**已支持防护，规则ID为 3100136879。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyQxbicAHf6Aa5KHeEibGuCOTIsbvCXS8D6EPNgN4gkhBjib5L7grYhHvaA/640?wx_fmt=png&from=appmsg)

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