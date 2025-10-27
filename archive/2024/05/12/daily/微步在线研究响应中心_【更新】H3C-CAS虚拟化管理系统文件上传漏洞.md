---
title: 【更新】H3C-CAS虚拟化管理系统文件上传漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247505762&idx=1&sn=42f58b5109a63fd7a453c861fa31434c&chksm=cfcab476f8bd3d6044348c18134db67022bf0366b36d1d4233ba4527640accbbb41c7c911e6f&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-05-12
fetch_date: 2025-10-06T17:17:00.830024
---

# 【更新】H3C-CAS虚拟化管理系统文件上传漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMLcTFB5GQpIqPnp1Utf1MIXV4dypQP1iaq7Fhmd3YAFwNPTNsltXvSIAHpPwibria9t39oNIkCOKFAzg/0?wx_fmt=jpeg)

# 【更新】H3C-CAS虚拟化管理系统文件上传漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

H3C-CAS虚拟化管理系统是新华三集团推出的一套面向企业级用户的云计算解决方案，旨在帮助企业构建高效、灵活、可靠的云计算环境。

微步漏洞团队通过“X 漏洞奖励计划”获取到H3C-CAS虚拟化管理系统文件上传漏洞情报（https://x.threatbook.com/v5/vul/XVE-2023-35299），该漏洞利用难度低，攻击者可利用该漏洞绕过鉴权，上传恶意文件，从而获取服务器权限。经过分析和研判，建议尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：****高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2023-35299 |
| 漏洞类型 | 文件上传 |
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
| **产品名称** | H3C-CAS虚拟化管理系统 |
| **受影响版本** | * E0535H03之后的5.0版本 * E0730P11H07之前版本 * E0760P03H08之前版本 * E0783之前的版本   **注**：2.0、3.0均不涉及 |
| **影响范围** | 该产品公网部署较少，大都部署于内网 |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=app%3D"H3C-CAS"

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLcTFB5GQpIqPnp1Utf1MIXVvJYbz8sDyflf0zzLaymCVrtibej6B6ugCyJfqPMLQiaXQyA0Qb3QBRw/640?wx_fmt=png&from=appmsg)

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLcTFB5GQpIqPnp1Utf1MIX0P0yhseNSjx1jLYAYPkbeMxkIUlON7Eic1jUpVxjkibfWow8bL1tmA5Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLcTFB5GQpIqPnp1Utf1MIXu5jOjQoa49cenbu3DOD1o9tdG9Nf9aMhEPD6S8cWic1Mahtg41qwhMg/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

H3C通告链接：

https://www.h3c.com/cn/Service/Online\_Help/psirt/security-notice/detail\_2021.htm?Id=125

受影响的用户建议在线升级至以下安全版本：

* E0730P11H07
* E0760P03H08
* E0783
* E9003H01-UPLOAD版本

## **临时修复方案：**

* 使用防护类设备对相关资产进行防护
* 如非必要，避免将资产暴露在互联网

**微步产品侧支持情况**

* 微步威胁感知平台TDP已支持检测，检测规则ID为 S3100135233、S3100135307、S3100135204， 模型/规则高于20231212000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLcTFB5GQpIqPnp1Utf1MIXXNoV0Wnklm1eqcbHRVqygCPg0ia1vMLIEyFJibgE2e8RrWHrZLToiaDYg/640?wx_fmt=png&from=appmsg)

* 微步安全情报网关OneSIG已支持防护，防护规则ID为 3100135233、3100135307、3100135204。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLcTFB5GQpIqPnp1Utf1MIXZhcCiaJ0j7BOVic6vJ5XicrgJYLu7mGkO26Qk6TZic4v0sLLZf0KnAOGcA/640?wx_fmt=png&from=appmsg)

**时间线**

* 2023.11 微步"X漏洞奖励计划"获取该漏洞相关情报
* 2023.12 TDP和OneSIG支持检测和防护
* 2024.03 厂商发布补丁
* 2024.04 微步发布报告
* 2024.05 微步发布更新报告

![](https://mmbiz.qpic.cn/mmbiz_gif/Yv6ic9zgr5hSjF5ugwo1dgibkJbx9quORvic1Jd3cbE6HTJcib0K3hVSYpChOHM4OsFcibNib1G4qfCVrglZ348Oebkg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

网安人不容错过的年度盛会——CSOP 2024 · 深圳站正在火热报名中，只有干货，席位紧俏。扫码立即报名 ↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKBBQYEhCnIgn2InoWbNJRSL4bt2m5c4icfkibB3YrS8ZJKVyLOKx5ywzKERKtgjqx1h5qz5H4TQ6iaw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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