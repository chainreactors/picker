---
title: 【已复现】用友U8cloud XChangeServlet SQL注入漏洞(QVD-2026-38848)安全风险通告
url: https://mp.weixin.qq.com/s/CIKNm78KOXbfkO_aXCcgIg
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:57:39.362096
---

# 【已复现】用友U8cloud XChangeServlet SQL注入漏洞(QVD-2026-38848)安全风险通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555tqMibibLMkxpJQTZsFNEMwwzYX9uEkGfuibiac5nsM8hkicf25EYwmNv6S1jN7qJ61IVb5DQszgRQS5tibU9r7j9GIpIWy9OTLgBSew/0?wx_fmt=jpeg)

# 【已复现】用友U8cloud XChangeServlet SQL注入漏洞(QVD-2026-38848)安全风险通告

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 用友U8cloud XChangeServlet SQL注入漏洞 | | |
| **漏洞编号** | QVD-2026-38848 | | |
| ****公开时间**** | 2026-07-08 | ****影响量级**** | 万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **9.1** |
| **威胁类型** | 信息泄露、代码执行 | **利用可能性** | ****高**** |
| **POC状态** | **未公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **未公开** | **技术细节状态** | **未公开** |
| **危害描述：**该漏洞可造成任意命令执行，攻击者可进一步获取服务器控制权限。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

用友 U8cloud 是用友网络面向成长型、集团型企业推出的云 ERP 产品，主要用于企业财务、供应链、生产制造、人力资源、协同办公等业务管理场景。该系统通常部署在企业内网或私有云环境中，为企业提供多组织、多地点、多业务单元的统一管理能力，支持财务核算、采购、销售、库存、生产、成本、报表等核心业务流程。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复用友U8cloud XChangeServlet SQL注入漏洞(QVD-2026-38848)，该漏洞源于用友 U8cloud 的XChangeServlet 接口存在 SQL 注入漏洞。该接口用于处理 XML 格式的数据交换请求，服务端在解析请求体中的 ufinterface 节点属性时，对 sender 参数缺少严格校验，并将其带入后端 SQL 查询逻辑，导致攻击者可以构造恶意 SQL片段破坏原有查询语句结构。攻击者无需登录，只要能够访问目标系统 Web 服务，即可向XChangeServlet 发送恶意 XML 请求，在 sender 属性中注入 SQL 语句。该漏洞可造成任意命令执行，攻击者可进一步获取服务器控制权限。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

用友U8Cloud 2.0

用友U8Cloud 2.1

用友U8Cloud 2.3

用友U8Cloud 2.5

用友U8Cloud 2.6

用友U8Cloud 2.7

用友U8Cloud 2.65

用友U8Cloud 3.0

用友U8Cloud 3.1

用友U8Cloud 3.2

用友U8Cloud 3.5

用友U8Cloud 3.6

用友U8Cloud 3.6sp

用友U8Cloud 5.0

用友U8Cloud 5.0sp

用友U8Cloud 5.1

用友U8Cloud 5.1sp

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现用友U8cloud XChangeServlet SQL注入漏洞(QVD-2026-38848)，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555sq9ayKo4uxTIdvlf9GMjnyWLJBQEk85M9tfFXEibHJjIfmJIhePhJJWUdP69K18qKl2dDfjse1wJpPT4ukVHOibw5ro0oXablhA/640?wx_fmt=jpeg)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布补丁：https://security.yonyou.com/#/noticeInfo?id=784

使用U8C安全补丁升级工具进行安全补丁更新，各版本对应补丁如下：

V2.0-V2.3

补丁名称：patch\_V2.0-2.1\_XChangeServlet接口存在SQL注入漏洞的补丁(注入点sender)\_chengxlk\_20260706

校验码：

a178803f1ce550f69d85bc133a3e59394bc397e212da0d51ba48daa279ddb560

V2.5-V3.6sp

补丁名称：patch\_V2.3-3.6sp\_XChangeServlet接口存在SQL注入漏洞的补丁(注入点sender)\_chengxlk\_20260706

校验码：

4716faa6ec1ff41d55b574581fc3c2ea6d000b6fb539b0c1777decb733e47d08

V5.0-V5.1sp

补丁名称：patch\_V5.0-5.1sp\_XChangeServlet接口存在SQL注入漏洞的补丁(注入点sender)\_chengxlk\_20260706

校验码：

69c0f8701a1df13c93b56916990ad5a86750acc026f1b1b20e764411291d7e30

临时缓解措施：

1. 限制 /XChangeServlet 接口的公网访问，避免直接暴露在互联网。

2. 对访问该接口的来源 IP 设置白名单，仅允许可信业务系统访问。

**05**

**参考资料**

[1]https://security.yonyou.com/#/noticeInfo?id=784

**06**

**时间线**

2026年07月09日，奇安信 CERT发布安全风险通告。

**07**

**漏洞情报服务**

「奇安信漏洞情报平台」重磅上线，诚邀您来体验：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555tuTOrO8WdDMiaSolWIdC6eaJXmL2eictxM8TXBiaCS5GgS5hNlXgww5ts7iaGPoOHFD4McaLf3dbDeAGgh1ziaHL2ia17PYlKrpXUwo/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4 "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

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