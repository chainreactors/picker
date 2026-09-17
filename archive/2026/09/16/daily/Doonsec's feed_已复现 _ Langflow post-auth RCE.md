---
title: 已复现 | Langflow post-auth RCE
url: https://mp.weixin.qq.com/s/A0h3oCFG6EB8TEomt5Pxbw
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:54:51.394712
---

# 已复现 | Langflow post-auth RCE

# 已复现 | Langflow post-auth RCE

原创

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞概况

Langflow 是 IBM 维护的开源低代码 AI 应用构建平台（Langflow OSS），通过可视化流程编排与自定义 Python 组件搭建大模型应用。

近日，微步情报局监测到互联网披露了Langflow 认证后远程代码执行漏洞（CVE-2026-17633）。微步情报局已成功复现该漏洞。经分析，由于自定义组件提交接口缺失对组件源码的内容安全检查，已认证用户可提交任意 Python 组件代码；持有凭据的攻击者可通过一条请求在 Langflow 后端进程上下文中执行任意代码，并读取 LLM API key、数据库凭据或 vector store token 等敏感凭据用于横向移动。

（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-45745）

该漏洞技术细节已在互联网公开，攻击者可据此快速复现并实施攻击，风险较高，建议受影响用户尽快修复。

漏洞处置优先级(VPT)

**综合处置优先级：**高风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-45745 |
| CVE编号 | CVE-2026-17633 |
| 漏洞类型 | 远程代码执行 |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | 无特殊要求 |
| 利用漏洞的权限要求 | 需认证凭据 |
| 是否需要受害者配合 | 否 |
| 利用情报 | 是否有POC | 是 |
| 已知利用行为 | 暂无 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | Langflow |
| 受影响版本 | 1.0.0<=version<1.11.0 |
| 有无修复补丁 | 有 |

漏洞复现

获取token后，执行POC发送请求，实现以Langflow 后端进程权限执行任意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEOfuWO9X6FDR2sRzicf4QMj9onRXm08ia72zyemRvZysMGxF2JDFsa96hyOTJCd8bGAoJXORwVurgxBwjCzPv4PTUQnJsZfzDPFQ/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

官方已发布修复方案，请访问链接下载：
https://github.com/langflow-ai/langflow/releases

### 临时缓解措施

1、若业务可暂时不使用自定义组件，将环境变量 LANGFLOW\_ALLOW\_CUSTOM\_COMPONENTS 设为 false，阻止新建/修改自定义组件代码。

 2、收紧可登录并创建自定义组件的账号面：仅保留业务所需账号，回收不再使用的账号与 API token。

微步产品支撑

微步漏洞情报于2026-08-05收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报中心已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

微步威胁感知平台TDP已于20260916支持检测，检测ID：S3100184607，模型/规则高于：20260916000000 可检出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEP701aR24F7wr2XHzgEJLxnlrh2dcbibAwqD9VmrJko1qNEbPhQuCF47LicXMGNaaRzqYRXp0IO9D4x29dG790UEFLfNNpymCuO0/640?wx_fmt=png&from=appmsg)

微步威胁防御系统OneSIG已支持防护规则ID为：3100184607

微步云原生应用安全平台 OneCloud 已于 2026-09-16 支持检测该漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOxyFcYTNRQkiaIqcSib4jrYovhRgboqJ2tqPj1djg9xx3BicwfoqZ57In17Bm11dhtf0mo7nIefHXvhheAdFoaGkMfjVTFEXxQYM/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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