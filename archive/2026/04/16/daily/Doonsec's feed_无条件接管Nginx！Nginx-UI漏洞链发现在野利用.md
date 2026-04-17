---
title: 无条件接管Nginx！Nginx-UI漏洞链发现在野利用
url: https://mp.weixin.qq.com/s/KUPsiUFwLerRwBpgabPTaw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:47:18.055390
---

# 无条件接管Nginx！Nginx-UI漏洞链发现在野利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKRfkOibMss786PqPwUGjHu4siboRiaqI4mguqRmR09PN8XVEaw2KnV8ORyrCRF8ZQz35agEmw3yebIQ/0?wx_fmt=jpeg)

# 无条件接管Nginx！Nginx-UI漏洞链发现在野利用

原创

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

漏洞概况

Nginx-UI是一款广受欢迎的开源Nginx可视化管理面板，它提供简洁友好的Web界面，帮助用户轻松管理Nginx配置、申请证书、查看日志以及重载服务。

近日，微步情报局监测到Nginx-UI相关漏洞：CVE-2026-33032 出现在野利用行为。微步情报局已成功复现。经分析，Nginx-UI的MCP功能存在严重的鉴权缺陷：/mcp接口实现了严格的身份认证，但/mcp\_message接口仅做了IP白名单校验，且当IP白名单为空（默认配置）时，系统会允许所有IP访问。由于/mcp接口需要严格认证，攻击者难以直接建立有效的MCP会话，也就无法获取sessionId，因此仅从本漏洞来看，单独利用的难度较高，实际危害较为有限。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-10589）

但攻击者可以结合另一个漏洞CVE-2026-27944，下载并解密Nginx-UI的备份文件，从而获取有效的node\_secret。随后使用node\_secret 请求/mcp接口，建立MCP会话，获得有效的sessionId，最终实现对 /mcp\_message 的未授权访问，执行任意MCP操作（如新增或修改Nginx配置、写入恶意文件、甚至重启Nginx服务），造成严重安全风险。

漏洞处置优先级(VPT)

**综合处置优先级：**中风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-10589 |
| CVE编号 | CVE-2026-33032 |
| 漏洞类型 | 认证绕过 |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 是 |
| 对被攻击系统的要求 | 无特殊要求 |
| 利用漏洞的权限要求 | 无须用户权限 |
| 是否需要受害者配合 | 否 |
| 利用情报 | POC是否公开 | 是 |
| 已知利用行为 | 存在在野利用行为 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | Nginx-UI |
| 受影响版本 | version <= 2.3.3 |
| 有无修复补丁 | 有 |

漏洞复现

![image.png](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMR6526cgWy0kricoxTNibEhYSzpJLMTDYWRp8XxK73vPVYUSQQVNH8aOwwc2CcV7JH0aiaHrGAGCrYyWooecLzZGBD4080EVV82I/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

官方已发布修复方案，请访问链接下载：
https://github.com/0xJacky/nginx-ui/releases/tag/v2.3.6

### 临时缓解措施

配置层： 将可信IP设置为白名单(默认路径/etc/nginx-ui/app.ini)

微步产品支撑

微步漏洞情报于2026-03-31收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

针对CVE-2026-33032，微步威胁感知平台TDP已于20260416支持检测，检测ID：S3100174604，模型/规则高于：20260416000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOnrpGEaxskWcmkcNrnzDRFicp1OQ54txYTWsicribrBeQPtDBgfK4KZzwasESOYiab4QXwTkUTGn0oBmKzBs83DVM76V3TdP4ZJAE/640?wx_fmt=png&from=appmsg)

针对CVE-2026-27944，微步威胁感知平台TDP已于20260416支持检测，检测ID：S3100174602，模型/规则高于：20260416000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOFIsyovZ0MzeSqBf2FhibHYWiaSAcauS6tlEFVDYj6FA4WZGw8nrT9Ky0CiaVdYmwtCibicJYgJoibvegria4SVBGEY48ZwFB475BZy8/640?wx_fmt=png&from=appmsg)

- END -

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