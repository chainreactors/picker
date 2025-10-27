---
title: 【更新】Unix打印机组件RCE漏洞已复现
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650182336&idx=1&sn=e6cc1cbfee8b7289ecfe56d1b9ee179f&chksm=f448697cc33fe06afdf4135e96754b4e3309faa336f83f0a173cf1371a5ad604e58c775d3618&scene=58&subscene=0#rd
source: 微步在线
date: 2024-09-28
fetch_date: 2025-10-06T18:27:59.826614
---

# 【更新】Unix打印机组件RCE漏洞已复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTtdVvQsuhQg18icPfSiaccicn8jibzN9yH1pD4zFsh4ibx3Rib2jR9a4PNdEdeDeGyYHI9sibeNE8k90MCQ/0?wx_fmt=jpeg)

# 【更新】Unix打印机组件RCE漏洞已复现

微步在线

以下文章来源于微步在线研究响应中心
，作者微步情报局

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5aJJ0hMuzqFKnIqVJvyZPgBp5zLia7Gsicshib4xjO0DuOg/0)

**微步在线研究响应中心**
.

微步情报局最新威胁事件分析、漏洞分析、安全研究成果共享，探究网络攻击的真相

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

**漏洞概况**

cups-browsed是CUPS(Common Unix Printing System，通用Unix打印系统)一个重要组件，它是一个轻量级的后台服务，用于在本地网络中自动发现和共享打印机。

微步情报局已复现cups-browsed远程代码执行漏洞(https://x.threatbook.com/v5/vul/XVE-2024-28256)并初步确认漏洞原理。该漏洞是CVE-2024-47076(https://x.threatbook.com/v5/vul/XVE-2024-28262),CVE-2024-47175(https://x.threatbook.com/v5/vul/XVE-2024-28259),CVE-2024-47177(https://x.threatbook.com/v5/vul/XVE-2024-28261)的组合利用，涉及到libppd，libcupsfilters，cups-filters等CUPS组件。攻击者需要模拟一个恶意的打印机服务，通过诱使受害者将打印任务发送给恶意的打印机服务，从而触发漏洞，执行恶意命令。从漏洞利用方式来看，该漏洞的利用需要配合相对钓鱼手段，由此可以推断Linux桌面版面临的风险更高。

另外值得一提的是，根据公开信息(https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/)披露，cups-browsed服务中还存在缓冲区溢出和条件竞争，但暂无公开PoC。

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

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTtdVvQsuhQg18icPfSiaccicnht6KJC2ZIw0ibxaYrfm1sQLiaictoibqct6ZtexGDt4IL9a0aUv1gG3VTw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTtdVvQsuhQg18icPfSiaccicnqerzXlobpVXujGtCWUpl7YHKOdPA2fZHpHVXcPPN9fJbbI0Sa9Hcmw/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

暂无官方修复方案

## **临时修复方案：**

1.排查主机上是否启用cups-browsed服务。例如RedHat系统使用sudo systemctl status cups-browsed

2.排查该服务是否绑定在0.0.0.0，且对外开放。该服务默认绑定在631端口，使用netstat -ano | grep 631

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKEMKFyAyJBiafkl03aOaCOeH8X5koAPapFQIHgszpu5SmDXYTVDK9p9F5fKazP4HUP3pHib0OP6ibQQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

3.若确认已开启该服务，如果业务场景不需要打印的情况下可禁用该服务。例如 RedHat系统使用sudo systemctl disable cups-browsed

**微步在线产品侧支持情况**

微步威胁感知平台TDP已支持检测，检测ID为S3100154554，模型/规则高于20240927000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTtdVvQsuhQg18icPfSiaccicnhJaeuKx7lhicCExtPlKEznKYyx2qA83TiblFS2MTBgCX3WiaG307XMzVw/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

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

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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