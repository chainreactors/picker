---
title: 0day速修 | H3C SecCenter SMP 安全管理平台远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507478&idx=1&sn=3427d3a5f23b7973076ac0219e3c2073&chksm=cfcabd02f8bd341450c49c57e2944986992da9eb9a85e28e0cfe030a99e5f5ff31e48b65fd77&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-11-30
fetch_date: 2025-10-06T19:16:18.653699
---

# 0day速修 | H3C SecCenter SMP 安全管理平台远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSibfONW0ib18vsxvniae0dvDGyNH4YzdjmskGMeKXoCGr0Cr6FzbVsxu5w/0?wx_fmt=jpeg)

# 0day速修 | H3C SecCenter SMP 安全管理平台远程代码执行漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png)

**漏洞概况**

H3C SecCenter SMP（Security Manager Platform，安全业务管理平台）是一个负责网络安全业务的独立平台。SMP 能够对网络中的防火墙、入侵防御安全设备进行统一管理，并适应各种网络规模需求，为部署于各关键位置的安全设备提供集中的安全策略管理与控制，且能直观地为实时事件监控和综合分析攻击等各种安全事件提供丰富的统计报告。

近日，微步情报局通过X漏洞奖励计划获取到H3C SecCenter SMP 安全管理平台远程代码执行漏洞情报（https://x.threatbook.com/v5/vul/XVE-2024-5470），攻击者可利用该漏洞上传Webshell，进而控制服务器，利用难度较低。

H3C官方已发布修复补丁，建议受影响的用户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-5470 |
| 漏洞类型 | 文件上传 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | 新华三技术有限公司-SecCenter SMP 安全管理平台 |
| **受影响版本** | version < E1113P05（E1114P03及以前版本) |
| **有无修复补丁** | 有 |

**漏洞复现**

1. 上传jsp文件

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMK9mkMFJGAibA0RFVuc95Y8eG8I4FFLEic4LIs2icSK7tIia0Ac9eZWhoOvyLV2INWWq2txq8gyVflH1Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMK9mkMFJGAibA0RFVuc95Y8eVMEVxwJB0ZCtZiavSiam69E6GWB8cxXtPaxNQLQ7tp1vjvh6hibedpibww/640?wx_fmt=png&from=appmsg)

2. 访问上传的文件

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMK9mkMFJGAibA0RFVuc95Y8exsEfZUHjQqVhboGib3S7Jjd41ic4eR4Rb9sJiaAPgeEx2Ku3oL7ibmsviaA/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

H3C官方已发布安全通告，请尽快联系厂商下载更新补丁。官方通告链接：

https://www.h3c.com/cn/Service/Online\_Help/psirt/security-notice/detail\_2021.htm?Id=226

## **临时修复方案：**

* 使用防护类设备进行防护，拦截请求中出现的恶意jsp代码。
* 如非必要，避免将资产暴露在互联网。

**微步产品侧支持情况**

微步威胁感知平台TDP已于2024年4月7日支持检测，检测ID为S3100140149、S3100139924、S3100139934、S3100139928，模型/规则高于20240407000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMK9mkMFJGAibA0RFVuc95Y8eeVofaFObNxUclyDviaGzYuia2icGZnkpulvGrqXlpMZqQrWicmtGcfa7iag/640?wx_fmt=png&from=appmsg)

微步威胁防御系统OneSIG已支持防护，规则ID为3100140149、3100139924、3100139934、3100139928。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLQ0mRaw7ArfDf0NmEuWorskrfPpe8gsWwoictP1e3JDZKDwEu3SHkBEnlDjUOyjG8PFxpJ9e9wfEw/640?wx_fmt=png&from=appmsg)

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

修改于

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