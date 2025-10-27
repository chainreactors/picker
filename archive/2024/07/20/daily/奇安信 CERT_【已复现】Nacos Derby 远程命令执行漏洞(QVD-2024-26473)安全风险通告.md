---
title: 【已复现】Nacos Derby 远程命令执行漏洞(QVD-2024-26473)安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501756&idx=1&sn=d2a6bccad06819cf70176bc02a7ee944&chksm=fe79e324c90e6a32139fd6113ec70cea92a332ab1c089e0b8e3b4676c71774730911e98195de&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-20
fetch_date: 2025-10-06T17:43:06.144083
---

# 【已复现】Nacos Derby 远程命令执行漏洞(QVD-2024-26473)安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibXfLoe3oGVefOz7CibdxJKlRKFsjxX2QbcYP1P0TuJBnvxgmzTgoKXclX63OX77etTev0t1Robh4Q/0?wx_fmt=jpeg)

# 【已复现】Nacos Derby 远程命令执行漏洞(QVD-2024-26473)安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Nacos Derby 远程命令执行漏洞 | | |
| **漏洞编号** | QVD-2024-26473 | | |
| **公开时间** | 2024-07-15 | **影响量级** | 万级 |
| **奇安信评级** | **高危** | ****CVSS 3.1分数**** | **9.8** |
| **威胁类型** | 命令执行 | **利用可能性** | **高** |
| **POC状态** | **已公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **已公开** | **技术细节状态** | **已公开** |
| **危害描述：**此漏洞允许未经身份验证的远程攻击者执行任意代码，可能导致数据泄露、服务中断或系统被完全控制。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

Nacos 是一个功能强大的服务注册与发现、配置管理平台，为微服务架构和云原生应用提供了重要的基础设施支持。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复**Nacos Derby 远程命令执行漏洞(QVD-2024-26473)**，由于Alibaba Nacos部分版本中derby数据库默认可以未授权访问，恶意攻击者利用此漏洞可以未授权执行SQL语句，最终导致任意代码执行。**目前该漏洞PoC已在互联网上公开，****鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

Nacos <= 2.4.0-BETA

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现**Nacos Derby 远程命令执行漏洞(QVD-2024-26473)**，截图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibXfLoe3oGVefOz7CibdxJKlcPqROTPtuEIKXae6oOZUX96owmmfFbrUwRxBfNQZz4t1iaNLlyqxoIw/640?wx_fmt=png&from=appmsg)

**04**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，**Nacos Derby 远程命令执行漏洞(QVD-2024-26473)**关联的国内风险资产总数为40575个，关联IP总数为8171个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibXfLoe3oGVefOz7CibdxJKlOV1sfIJKz3ia3iaOhqSfttFVzKF5xIoYhcNvnncech6uibgMmSo0iaoUEg/640?wx_fmt=png&from=appmsg)

**05**

**处置建议**

**>****>****>****>**

**安全更新**

1. 目前官方已经在最新代码中通过默认禁用derby接口的方式对本漏洞进行了修复，修复代码如下所示：

https://github.com/alibaba/nacos/commit/ed7bd03d4c214d68f51654fee3eea7ecf72fd9ab

2. 开启Nacos derby数据库接口鉴权。具体操作请参考链接：

https://nacos.io/zh-cn/docs/v2/guide/user/auth.html

**>****>****>****>**

**产品解决方案**

**奇安信天眼检测方案**

奇安信天眼新一代安全感知系统已经能够有效检测针对该漏洞的攻击，请将规则版本升级到3.0.0716.14410或以上版本。规则ID及规则名称：

0x10021C45，Nacos Derby 远程命令执行漏洞(QVD-2024-26473)。奇安信天眼流量探针规则升级方法：系统配置->设备升级->规则升级，选择“网络升级”或“本地升级”。

**奇安信网站应用安全云防护系统已更新防护特征库**

奇安信网神网站应用安全云防护系统已全局更新所有云端防护节点的防护规则，支持对Nacos Derby 远程命令执行漏洞(QVD-2024-26473)的防护。

**奇安信网神网络数据传感器系统产品检测方案**

奇安信网神网络数据传感器（NDS5000/7000/9000系列）产品，已具备该漏洞的检测能力。规则ID为：8078 ，建议用户尽快升级检测规则库至2407161130以上；

**奇安信自动化渗透测试系统检测方案**

奇安信自动化渗透测试系统已经能够有效检测针对该漏洞的攻击，请将插件版本和指纹版本升级到202407192600以上版本。规则名称：Nacos Derby 远程命令执行漏洞。奇安信自动化渗透测试系统规则升级方法：系统管理->升级管理->插件升级（指纹升级），选择“网络升级”或“本地升级”。

**06**

**参考资料**

[1]https://github.com/alibaba/nacos/issues/10613

[2]https://www.weaver.com.cn/cs/securityDownload.html#

**07**

**时间线**

2024年7月19日，奇安信 CERT发布安全风险通告。

**08**

**漏洞情报服务**

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BY9IJ0MPzeiashvK2XLpdl3XtTtCD91h0jS26fqvuWpEMXgmXa85qLkoA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp "漏洞订阅上线.png")

![](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

预览时标签不可点

阅读原文

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