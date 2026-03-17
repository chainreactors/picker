---
title: 【已复现】OpenClaw WebSocket共享令牌权限提升漏洞(QVD-2026-13829)安全风险通告
url: https://mp.weixin.qq.com/s/E1zb8_RV3oF5aEU0_Yrw4A
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:12:39.305153
---

# 【已复现】OpenClaw WebSocket共享令牌权限提升漏洞(QVD-2026-13829)安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555ttLia7RDcea2AGmXAbPX30l9guVYeTZkFC9ZKPoDuFNX2LCeGEAfQndK8BjIwBdWib5OBIjjKow3ZaZoBp5wuFJGGicUYtoPmvO8/0?wx_fmt=jpeg)

# 【已复现】OpenClaw WebSocket共享令牌权限提升漏洞(QVD-2026-13829)安全风险通告

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | OpenClaw WebSocket共享令牌权限提升漏洞 | | |
| **漏洞编号** | QVD-2026-13829 | | |
| ****公开时间**** | 2026-03-13 | ****影响量级**** | 十万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **9.9** |
| **威胁类型** | 权限提升 | **利用可能性** | ****高**** |
| **POC状态** | **未公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **未公开** | **技术细节状态** | **未公开** |
| **危害描述：**攻击者利用该漏洞伪造管理员令牌，完全控制服务器，造成数据泄露、服务中断或横向移动等严重后果。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

OpenClaw是一款开源的AI智能体平台，能够在本地环境中自主运行，通过自然语言指令直接操作用户计算机完成各类任务，包括文件读写、Shell命令执行、网页浏览以及与邮件、Slack、Jira、GitHub等第三方服务的集成。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复OpenClaw WebSocket共享令牌权限提升漏洞(QVD-2026-13829)，该漏洞存在于OpenClaw网关的WebSocket连接处理逻辑中。在2026.3.12版本之前，当使用无设备共享令牌或密码认证的后端连接时，系统未能正确验证和限制客户端自行声明的权限范围，攻击者可利用该漏洞，通过获取或构造无设备共享令牌，在WebSocket连接建立时自行声明高权限作用域，从而绕过正常的权限控制机制。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

OpenClaw <= 2026.3.11

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现OpenClaw WebSocket共享令牌权限提升漏洞(QVD-2026-13829)，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555sUonVsBzJFeLkxcTicpiaV3ibwOgD67Q4Nx7136zNvqPYv1QAMKsIoADicKo9LX5KHj60d8jo1Bv6kxxaFQ5GDbHAm7AkL3Qv062Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555sakoozCtQYeljvuHnY6ibASLtsrjJaAEyZTpAZQ31IEZa3p6LZ1ibkUkqZzIZicXXugJBdNW8PDkJib6uKZ9Eiad1SoJQgPdBgaNzI/640?wx_fmt=png&from=appmsg)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布安全补丁，请及时更新至最新版本:

OpenClaw >= 2026.3.12

下载地址：

https://github.com/openclaw/openclaw

**05**

**参考资料**

[1]https://github.com/openclaw/openclaw/security/advisories/GHSA-rqpp-rjj8-7wv8

**06**

**时间线**

2026年03月16日，奇安信 CERT发布安全风险通告。

**07**

**漏洞情报服务**

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BY9IJ0MPzeiashvK2XLpdl3XtTtCD91h0jS26fqvuWpEMXgmXa85qLkoA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3 "漏洞订阅上线.png")

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=5 "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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