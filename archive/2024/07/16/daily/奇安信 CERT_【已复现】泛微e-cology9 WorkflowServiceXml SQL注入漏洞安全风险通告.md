---
title: 【已复现】泛微e-cology9 WorkflowServiceXml SQL注入漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501684&idx=1&sn=44cc19da424c8d5a4210ab1e390cabb8&chksm=fe79e3ecc90e6afab2dde978b8af8c436087de3554f33458a7969f346f01c69e5e5ceb22b23d&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-16
fetch_date: 2025-10-06T17:44:16.046063
---

# 【已复现】泛微e-cology9 WorkflowServiceXml SQL注入漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibk4pC7wiaphWwfxZm5f4qGeUZf5g0CLM9iccMFQh75r2BkZuwjZS9uH5ge6FIBwxoLu9LbJicqg2JZQ/0?wx_fmt=jpeg)

# 【已复现】泛微e-cology9 WorkflowServiceXml SQL注入漏洞安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 泛微e-cology9 WorkflowServiceXml SQL注入漏洞 | | |
| **漏洞编号** | QVD-2024-26136 | | |
| **公开时间** | 2024-07-10 | **影响量级** | 万级 |
| **奇安信评级** | **高危** | ****CVSS 3.1分数**** | **9.8** |
| **威胁类型** | 命令执行 | **利用可能性** | **高** |
| **POC状态** | **已公开** | **在野利用状态** | **已发现** |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**在默认配置下，未授权攻击者可利用该漏洞执行任意SQL语句，从而造成任意命令执行。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

泛微协同管理应用平台e-cology是一套兼具企业信息门户、知识文档管理、工作流程管理、人力资源管理、客户关系管理、项目管理、财务管理、资产管理、供应链管理、数据中心功能的企业大型协同管理平台。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到**泛微e-cology9 WorkflowServiceXml SQL注入漏洞(QVD-2024-26136)**在野利用行为，在默认配置下，未授权攻击者可利用该漏洞执行任意SQL语句，从而造成任意命令执行。**目前该漏洞PoC已在互联网上公开，****鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

泛微e-cology9 < 10.64.1

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现**泛微e-cology9 WorkflowServiceXml SQL注入漏洞(QVD-2024-26136)**，截图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibk4pC7wiaphWwfxZm5f4qGerwzqbR0LE1hp4zLGPTSbh78yN03UFqwdGEcu1B65axsx7REDAeE9vQ/640?wx_fmt=png&from=appmsg)

**04**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，**泛微e-cology9 WorkflowServiceXml SQL注入漏洞(QVD-2024-26136)**关联的国内风险资产总数为51855个，关联IP总数为8761个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibk4pC7wiaphWwfxZm5f4qGevjm5XicEN5pS4qDcRficibnibQIS2qiacjoDvdp6zv8J3RjEGhH89kOBlrQ/640?wx_fmt=png&from=appmsg)

**05**

**处置建议**

**>****>****>****>**

**安全更新**

目前官方已发布安全补丁，建议受影响用户升级至最新版本：

泛微e-cology 9 >= 10.64.1

官方补丁下载地址：

https://www.weaver.com.cn/cs/securityDownload.html

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibk4pC7wiaphWwfxZm5f4qGeovwBNvL5X1Y9BSXxDCefe5PyNUEf5vAKwkaNTsDiauxhBHjyu52Frvg/640?wx_fmt=png&from=appmsg)

**>****>****>****>**

**产品解决方案**

**奇安信天眼检测方案**

奇安信天眼新一代安全感知系统已经能够有效检测针对该漏洞的攻击，请将规则版本升级到3.0.0715.14409或以上版本。规则ID及规则名称：

0x10021C43，泛微e-cology9 WorkflowServiceXml SQL注入漏洞(QVD-2024-26136)。奇安信天眼流量探针规则升级方法：系统配置->设备升级->规则升级，选择“网络升级”或“本地升级”。

**奇安信网站应用安全云防护系统已更新防护特征库**

奇安信网神网站应用安全云防护系统已全局更新所有云端防护节点的防护规则，支持对泛微e-cology9 WorkflowServiceXml SQL注入漏洞(QVD-2024-26136)的防护。

**奇安信网神网络数据传感器系统产品检测方案**

奇安信网神网络数据传感器（NDS5000/7000/9000系列）产品，已具备该漏洞的检测能力。规则ID为：8077 ，建议用户尽快升级检测规则库至2407151730以上；

**奇安信自动化渗透测试系统检测方案**

奇安信自动化渗透测试系统已经能够有效检测针对该漏洞的攻击，请将插件版本和指纹版本升级到202407192600以上版本。规则名称：泛微e-cology9 WorkflowServiceXml SQL注入漏洞。奇安信自动化渗透测试系统规则升级方法：系统管理->升级管理->插件升级（指纹升级），选择“网络升级”或“本地升级”。

**06**

**参考资料**

[1]https://www.weaver.com.cn/cs/securityDownload.html

**07**

**时间线**

2024年7月15日，奇安信 CERT发布安全风险通告。

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