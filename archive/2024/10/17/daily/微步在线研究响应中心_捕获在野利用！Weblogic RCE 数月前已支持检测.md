---
title: 捕获在野利用！Weblogic RCE 数月前已支持检测
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507134&idx=1&sn=69655f32f2e4294df6a9d9cc5dac80e0&chksm=cfcabfaaf8bd36bcc77b7272635fa42e235244a9b23804d2bff2b3a4ed42012c70e89b9f7c11&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-10-17
fetch_date: 2025-10-06T18:52:06.521693
---

# 捕获在野利用！Weblogic RCE 数月前已支持检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicML494yC0qHyG9utu1aoibtP3oe3iagRH5KakI6JojMRMfxvuFXN4GwwXztY7q3NqqTEIwB5niczIdyBg/0?wx_fmt=jpeg)

# 捕获在野利用！Weblogic RCE 数月前已支持检测

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

WebLogic Server 是由 Oracle 公司开发的一款领先的 Java EE（现为 Jakarta EE）应用服务器。它提供了一个可靠、安全、可扩展的平台，用于开发、部署和管理企业级 Java 应用程序，包括 Web 应用程序、企业 JavaBeans (EJB) 和 Web 服务。

微步于2024年4月通过 “X漏洞奖励计划” 获取到Weblogic Server远程代码执行漏洞（https://x.threatbook.com/v5/vul/XVE-2024-4789) ，微步威胁感知平台TDP与威胁防御系统OneSIG已于2024年4月支持检测与拦截，并在7月捕获到该漏洞利用行为。

该漏洞利用方式较为简单，攻击者在未授权条件下，利用 T3、IIOP协议反序列化，实现远程代码执行，获取服务器权限（无需出网）。该漏洞已被Oracle官方修复，CVE编号为CVE-2024-21216，建议用户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-4789 |
| 漏洞类型 | 远程代码执行 |
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
| **产品名称** | Oracle Weblogic Server |
| **受影响版本** | 12.2.1.4.0, 14.1.1.0.0 |
| **影响范围** | 万级 |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=app%3D%22weblogic%22

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML494yC0qHyG9utu1aoibtP3gicfAR39cicvzTHiaos9gCBCV43IhlicdnBxuKXibCevQYgYsU3qGW8oQ3w/640?wx_fmt=png&from=appmsg)

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML494yC0qHyG9utu1aoibtP3qKqxTicF4BdBiavjV6dHhdFsiawAj5YhOeYQTspUYjfsF0ss0BeUcUasg/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

厂商已修复此漏洞，请尽快联系厂商获取补丁包下载更新：

https://www.oracle.com/security-alerts/cpuoct2024.html

## **临时修复方案：**

* 在不影响业务的情况下，临时禁用IIOP和T3，或针对白名单IP进行开放
* 如非必要，避免将资产暴露在互联网

**微步产品侧支持情况**

微步威胁感知平台TDP已支持检测，检测ID为S3100139826、S3100139830、S3100140791，模型/规则高于20240402000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML494yC0qHyG9utu1aoibtP3poCKJZYriaJGLMZJEq5P4HOdibGAaKptobya2Dibb6HK62MpViats79JOw/640?wx_fmt=png&from=appmsg)

微步威胁防御系统OneSIG已支持防护，规则ID为3100139826、3100139830、3100140791。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML494yC0qHyG9utu1aoibtP36m3fpMuOtr74X1ceiamaZ9XshdJTy9zbriclfM16EDEIEdBiavFPpjLNw/640?wx_fmt=png&from=appmsg)

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