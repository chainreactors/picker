---
title: Unix系统打印服务爆RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507014&idx=1&sn=61509a9ff7f832712d14e53f16aa5587&chksm=cfcabf52f8bd36446dd0ad3a1f8b89c463fec0ad2bb65bbd333807707111b21ff33e1d6ceb4d&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-09-28
fetch_date: 2025-10-06T18:27:35.247522
---

# Unix系统打印服务爆RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMJDMico8tUSPf286Ekvdw8fyicOiatUKcfOxp6WlrpY31eicsUmQ6zRfsr7ibMtkiaeibmdIgCWjP13dCpYg/0?wx_fmt=jpeg)

# Unix系统打印服务爆RCE漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

cups-browsed是CUPS(Common Unix Printing System，通用Unix打印系统)一个重要组件，它是一个轻量级的后台服务，用于在本地网络中自动发现和共享打印机。

微步情报局于近日获取到cups-browsed远程代码执行漏洞情报(https://x.threatbook.com/v5/vul/XVE-2024-28256)。

根据漏洞发现者公开披露的信息(https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/)，未经认证的攻击者通过构造恶意的IPP服务器，通过引导受害者配置该恶意打印机，当受害者尝试从恶意设备打印时，攻击者即可利用该漏洞实现远程命令执行。

目前Canonical(Ubuntu开发商)、Debian、Red Hat以及其他发行版的开发团队和公司已经对该漏洞发布了安全通告：

* https://www.redhat.com/en/blog/red-hat-response-openprinting-cups-vulnerabilities
* https://security-tracker.debian.org/tracker/CVE-2024-47176
* https://ubuntu.com/security/notices/USN-7043-1

虽然网传该漏洞CVSS评分可能为9.9，根据Red Hat的公告信息，该漏洞的利用有以下条件：

1.若想在互联网环境下使用该漏洞，攻击者需要能远程访问cups-browsed 服务，且cups-browsed 服务所在的服务器必须能够出网(但并非所有Linux发行版都默认启用CUPS服务)

2.需要受害者被动配合，配置攻击者的恶意IPP服务器

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-28256 |
| 漏洞类型 | 远程命令执行 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 非默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 需要被动配合 |
| **利用情报** | POC是否公开 | 是 |
| 已在野利用 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | OpenPrinting - cups-browsed |
| **受影响版本** | <= 2.0.1 |
| **有无修复补丁** | 无 |

**修复方案**

**官方修复方案：**

暂无官方修复方案

## **临时修复方案：**

1.排查主机上是否启用cups-browsed服务。例如RedHat系统使用sudo systemctl status cups-browsed

2.排查该服务是否绑定在0.0.0.0，且对外开放。该服务默认绑定在631端口，使用netstat -ano | grep 631

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKEMKFyAyJBiafkl03aOaCOeH8X5koAPapFQIHgszpu5SmDXYTVDK9p9F5fKazP4HUP3pHib0OP6ibQQ/640?wx_fmt=png&from=appmsg)

3.若确认已开启该服务，如果业务场景不需要打印的情况下可禁用该服务。例如 RedHat 系统使用 sudo systemctl disable cups-browsed

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