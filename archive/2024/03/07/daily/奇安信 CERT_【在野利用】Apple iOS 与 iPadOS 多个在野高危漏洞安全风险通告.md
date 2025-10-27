---
title: 【在野利用】Apple iOS 与 iPadOS 多个在野高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247500578&idx=1&sn=f7f767f62adc6bdce5c6666e0137cb06&chksm=fe79e7bac90e6eac43c6e1a031a9ce9df3f17e78d3ba487e9f1874b137548132adb8f0982120&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-03-07
fetch_date: 2025-10-06T17:09:15.887609
---

# 【在野利用】Apple iOS 与 iPadOS 多个在野高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icKib0572Tood2NibwmOY9sHCicwnY1q3VibuFEUY6I6ot8k4XIN9e0CyIz8xlPghgFN5gY9Bo0YASHUg/0?wx_fmt=jpeg)

# 【在野利用】Apple iOS 与 iPadOS 多个在野高危漏洞安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Apple iOS 与 iPadOS 多个在野高危漏洞 | | |
| **漏洞编号** | CVE-2024-23296、CVE-2024-23225 | | |
| ****公开时间**** | 2024-03-05 | ****影响量级**** | 千万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **7.8** |
| **威胁类型** | 安全特性绕过 | **利用可能性** | **高** |
| **POC状态** | 未公开 | **在野利用状态** | **已发现** |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**需要本地触发、低权限用户。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

iOS是由苹果公司开发的移动操作系统。iPadOS（英文全称：iPad Operating System）是苹果公司基于iOS研发的移动端操作系统系列，于2019年6月4日推出。iPadOS主要运用于iPad等设备，聚焦了Apple Pencil、分屏和多任务互动功能，并可与Mac进行任务分享。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到Apple iOS 与 iPadOS 发布新版本修复了存在在野利用的**Apple iOS 与 iPadOS RTKit 安全特性绕过漏洞(CVE-2024-23296) 和 Apple iOS 与 iPadOS Kernel 安全特性绕过漏洞(CVE-2024-23225)**，具有任意内核读写能力的攻击者可能能够绕过内核内存保护。

苹果公司据一份报告称该漏洞可能已被利用。**鉴于这些漏洞已发现在野利用，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

**CVE-2024-23296：**

iOS < 17.4

iPadOS < 17.4

**CVE-2024-23225：**

iOS 17 < 17.4

iOS 16 < 16.7.6

iPadOS 17 < 17.4

iPadOS 16 < 16.7.6

**>****>****>****>**

**其他受影响组件**

无

**03**

**处置建议**

**>****>****>****>**

**安全更新**

目前官方已有可更新版本，建议受影响用户升级至最新版本：

**CVE-2024-23296：**

iOS >= 17.4

iPadOS >= 17.4

**CVE-2024-23225：**

iOS 17 >= 17.4

iOS 16 >= 16.7.6

iPadOS 17 >= 17.4

iPadOS 16 >= 16.7.6

https://support.apple.com/en-us/HT214081

https://support.apple.com/en-us/HT214082

**04**

**参考资料**

[1]https://support.apple.com/en-us/HT214081

[2]https://support.apple.com/en-us/HT214082

**05**

**时间线**

2024年3月6日，奇安信 CERT发布安全风险通告。

**06**

**漏洞情报服务**

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icKib0572Tood2NibwmOY9sHCJcGa5yHyFj6miapavnZowg6Ezy8AOky4M4EaSvtQlD8ibAsibEGqcicSug/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640 "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALHA威胁分析平台**订阅更多漏洞信息。

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