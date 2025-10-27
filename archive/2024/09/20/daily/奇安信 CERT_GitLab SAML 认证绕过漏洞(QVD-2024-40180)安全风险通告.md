---
title: GitLab SAML 认证绕过漏洞(QVD-2024-40180)安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502168&idx=1&sn=218d2b0e656b39a5e0ba5453cb151804&chksm=fe79edc0c90e64d60068b582d417b2f2df79b628fed0b9f6868a071dc3c2b6fd6480d3d17ed5&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-09-20
fetch_date: 2025-10-06T18:27:39.065466
---

# GitLab SAML 认证绕过漏洞(QVD-2024-40180)安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs49yeocNzVvnZpvCYok6GjdzSWgiaOMEYaOsNic6E49YVb1eQrlsopEcWN8bqUrBYdX8J8yicK45HfAiaQ/0?wx_fmt=jpeg)

# GitLab SAML 认证绕过漏洞(QVD-2024-40180)安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | GitLab SAML 认证绕过漏洞 | | |
| **漏洞编号** | QVD-2024-40180,CVE-2024-45409 | | |
| **公开时间** | 2024-09-17 | **影响量级** | 百万级 |
| **奇安信评级** | **高危** | ****CVSS 3.1分数**** | **10.0** |
| **威胁类型** | 安全特性绕过 | **利用可能性** | **高** |
| **POC状态** | 未公开 | **在野利用状态** | 未发现 |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**攻击者可以利用 GitLab 中的 SAML 认证机制中的漏洞绕过认证，通过创建特制的 SAML 响应来非法获取对 GitLab 实例的访问权限。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

GitLab 是一款用于仓库管理的开源项目，它提供了一整套工具来帮助开发团队进行项目管理、代码托管、持续集成/持续部署（CI/CD）、监控、以及更多的功能。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复**GitLab SAML 认证绕过漏洞(QVD-2024-40180)**，由于GitLab对 SAML 响应的不当处理，使得攻击者可以插入任意值，攻击者从而通过构造特定的 SAML 响应，绕过 GitLab 实例的身份验证机制，无需正确的凭证即可访问受保护的资源。**鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

GitLab CE/EE 17.3.\* < 17.3.3

GitLab CE/EE 17.2.\* < 17.2.7

GitLab CE/EE 17.1.\* < 17.1.8

GitLab CE/EE 17.0.\* < 17.0.8

GitLab CE/EE < 16.11.10

**>****>****>****>**

**其他受影响组件**

无

**03**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，**GitLab SAML 认证绕过漏洞(QVD-2024-40180)**关联的国内风险资产总数为1372328个，关联IP总数为24944个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs49yeocNzVvnZpvCYok6GjdzgJ4Fn5jk7ibyY6qyugTFqRwYlyBNbBDAENt5MoNkgb0B0Vdq7OzEBew/640?wx_fmt=png&from=appmsg)

**GitLab SAML 认证绕过漏洞(QVD-2024-40180)**关联的全球风险资产总数为1577166个，关联IP总数为55582个。全球风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs49yeocNzVvnZpvCYok6Gjdzn1KuWQia2Lmsibibc9bfib3VsZG46mvLmABGZ3ZYasdh15cWFZRwJ4ibfvA/640?wx_fmt=png&from=appmsg)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

将依赖项 omniauth-saml 更新至 v2.2.1 、ruby-saml 更新至 v1.17.0。

目前官方已有可更新版本，建议受影响用户升级至最新版本：

GitLab CE/EE 17.3.\* >= 17.3.3

GitLab CE/EE 17.2.\* >= 17.2.7

GitLab CE/EE 17.1.\* >= 17.1.8

GitLab CE/EE 17.0.\* >= 17.0.8

GitLab CE/EE >= 16.11.10

官方补丁下载地址：https://about.gitlab.com/update

**临时缓解方案：**

为 GitLab 上的所有用户启用 GitLab 双因素身份验证并不勾选 SAML 双因素绕过选项。

**05**

**参考资料**

[1]https://about.gitlab.com/releases/2024/09/17/patch-release-gitlab-17-3-3-released/

**06**

**时间线**

2024年9月19日，奇安信 CERT发布安全风险通告。

**07**

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