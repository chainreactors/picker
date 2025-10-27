---
title: 漏洞通告 | 通天星CMSV6车载定位监控平台远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247506252&idx=1&sn=f5849bfe706eb5b54b6813a1eb248021&chksm=cfcaba58f8bd334eab9878982c9ed49c2e133b8e9752c2f81e9e9163eaf07f54433995842471&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-07-10
fetch_date: 2025-10-06T17:45:20.112358
---

# 漏洞通告 | 通天星CMSV6车载定位监控平台远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKvuA4JZzEuGMdeYeUoZSjBcsMbRPD6ibdQ3bxr9iaFqmZgM8qI0ibX7Vp5Xt6PTLpat3M3xaq9sIZ0Q/0?wx_fmt=jpeg)

# 漏洞通告 | 通天星CMSV6车载定位监控平台远程代码执行漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

通天星CMSV6拥有以位置服务、无线3G/4G视频传输、云存储服务为核心的研发团队，专注于为定位、无线视频终端产品提供平台服务，通天星CMSV6产品覆盖车载录像机、单兵录像机、网络监控摄像机、行驶记录仪等产品的视频综合平台。

近日，微步漏洞团队获取到通天星CMSV6车载定位监控平台远程代码执行漏洞情报（https://x.threatbook.com/v5/vul/XVE-2023-24846）。攻击者可通过该漏洞在默认配置下写入WebShell，进而控制服务器。该漏洞利用难度低，造成危害大，建议用户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2023-24846 |
| 漏洞类型 | SQL to RCE |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 微步已捕获攻击行为 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | CMSV6车载定位监控平台 |
| **受影响版本** | version < 7.33.0.7\_20240508 |
| **影响范围** | 千级 |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=app=%22%E9%80%9A%E5%A4%A9%E6%98%9FCMSV6%E8%BD%A6%E8%BD%BD%E5%AE%9A%E4%BD%8D%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%22

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKvuA4JZzEuGMdeYeUoZSjBSZLrX4E3XedFAQv0KEGeGtoZ5GuylQxBgYBhxQWxFOV7V1eNS8gQtg/640?wx_fmt=png&from=appmsg)

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKvuA4JZzEuGMdeYeUoZSjBicFH7JkyOfQPFye6asBZBUDetsa3dBrp4NMAfdnicD8sJ1J99VibbY4Gg/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

厂商已发布漏洞修复程序，请尽快前往官网（http://www.g-sky.cn/list-70-1.html）下载更新至7.33.0.7\_20240508及以上版本。

## **临时修复方案：**

* 使用防护类设备对相关资产进行防护，拦截URL编码后的恶意SQL语句。
* 如非必要，避免将资产暴露在互联网。

**微步产品侧支持情况**

微步威胁感知平台TDP已支持检测，检测ID为S3100125197 ，模型/规则高于20230813000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKvuA4JZzEuGMdeYeUoZSjB3qAIBp0CpJHRxc0VHdibkZT7BMRMjQSZjTYCNxpCaoK1qibZ4xdrpCibA/640?wx_fmt=png&from=appmsg)

微步威胁防御系统OneSIG已支持防护，规则ID为3100125197。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKvuA4JZzEuGMdeYeUoZSjBzcj7SrsqG1GicCmWYmelg2ibKYbL9sx1C1eJuhrAj1Ntgm2VCH2TrEaw/640?wx_fmt=png&from=appmsg)

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