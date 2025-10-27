---
title: 漏洞通告 | Apache Tomcat 远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507571&idx=1&sn=2ee4ea1d3100d5ff50536b0d61bec91d&chksm=cfcabd67f8bd34712f0110942c80bedd686614f7735dc66618734680a8d403b6643099ed3467&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-12-19
fetch_date: 2025-10-06T19:39:00.050846
---

# 漏洞通告 | Apache Tomcat 远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSibfONW0ib18vsxvniae0dvDGyNH4YzdjmskGMeKXoCGr0Cr6FzbVsxu5w/0?wx_fmt=jpeg)

# 漏洞通告 | Apache Tomcat 远程代码执行漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png)

**漏洞概况**

Tomcat 是一个开源的、轻量级的 Web 应用服务器 和 Servlet 容器。它由 Apache 软件基金会下的 Jakarta 项目开发，是目前最流行的 Java Web 服务器之一。

微步情报局获取到 Apache Tomcat 远程代码执行漏洞情报CVE-2024-50379（https://x.threatbook.com/v5/vul/XVE-2024-36623），当 Tomcat 的DefaultServlet Servlet 启用写入，并且部署在不区分大小写的文件系统（常见为Windows操作系统）上时，由于 JSP 编译过程中的 TOCTOU 竞争条件漏洞，攻击者可以通过条件竞争同时读取和上传同一文件，可能会绕过 Tomcat 的大小写敏感性检查，最终导致远程代码执行。

漏洞PoC已公开，建议受影响的客户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-36623 |
| 漏洞类型 | 远程代码执行 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 不区分大小写的文件系统（例如Tomcat部署在Windows上）  DefaultServlet的初始参数readonly为false(默认为true) |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | PoC是否公开 | 是 |
| 已知利用行为 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Apache软件基金会 - Apache Tomcat |
| **受影响版本** | 9.0.0.M1 ≤ version ≤ 9.0.97  10.1.0-M1 ≤ version ≤ 10.1.33  11.0.0-M1 ≤ version ≤ 11.0.1 |
| **有无修复补丁** | 有 |

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLicUqM1KDhX3lKcW2SYnJqntJIzmegMBGzly2l2KRY7ldnMlGNibXnUicptGicOVibBfd4amhwLyWMzFQ/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

Apache基金会官方已发布漏洞公告，请尽快前往下载更新补丁：

https://lists.apache.org/thread/y6lj6q1xnp822g6ro70tn19sgtjmr80r

## **临时修复方案：**

* 若启用了DefaultServlet，请不要将初始参数readonly设置为false；
* 如非必要，避免将资产暴露在互联网。

**微步产品侧支持情况**

微步威胁感知平台 TDP 通用规则可以检出，模型/规则高于 20220101000000 可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLicUqM1KDhX3lKcW2SYnJqnOn7uFpODsIjx88xJ1W4MicHrQ7S4sFaOrFVXiako50S0IUtCdaW4Nw9A/640?wx_fmt=png&from=appmsg)

微步威胁防御系统 OneSIG 默认支持防护。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLicUqM1KDhX3lKcW2SYnJqnfOefpqOtrtWACToqC0w8Z9165RFK3NYFBTNpYfbrqvVq4eq0qIF3Yg/640?wx_fmt=png&from=appmsg)

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