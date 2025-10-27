---
title: 【在野利用】Apple 多个在野高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502473&idx=2&sn=e5d76f1cef13f032535065aae0924b0a&chksm=fe79ee11c90e67077b61dd29c7571b5fa2c8d1a5ac9c4dc5629276ded403c4e0495fdeba1feb&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-11-21
fetch_date: 2025-10-06T19:16:05.486356
---

# 【在野利用】Apple 多个在野高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs49gvQmUtV0iaVrqxKneWyUzJQLZCF8XQvzCRwY37Gic5ibhdjJIFhpzWPm19OibjMWNzffKZnQ7xb9nXg/0?wx_fmt=jpeg)

# 【在野利用】Apple 多个在野高危漏洞安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Apple 多款产品输入验证错误漏洞 | | |
| **漏洞编号** | QVD-2024-47972、CVE-2024-44308 | | |
| ****公开时间**** | 2024-11-19 | ****影响量级**** | 千万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **8.8** |
| **威胁类型** | 代码执行 | **利用可能性** | **高** |
| **POC状态** | 未公开 | **在野利用状态** | **已发现** |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**成功利用可能造成代码执行、信息泄露等危害。 | | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Apple 多款产品跨站脚本漏洞 | | |
| **漏洞编号** | QVD-2024-47973、CVE-2024-44309 | | |
| ****公开时间**** | 2024-11-19 | ****影响量级**** | 千万级 |
| **奇安信评级** | ****中危**** | **CVSS 3.1分数** | ****6.1**** |
| **威胁类型** | 代码执行 | **利用可能性** | **高** |
| **POC状态** | 未公开 | **在野利用状态** | **已发现** |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**成功利用可在用户浏览器中执行任意 HTML 和脚本代码。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

iOS是由苹果公司开发的移动操作系统。iPadOS是苹果公司基于iOS研发的移动端操作系统系列。macOS 是苹果公司桌面和笔记本电脑的操作系统。Vision OS是苹果推出的一种空间计算操作系统。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到Apple发布新版本修复了**存在在野利用**的**Apple 多款产品输入验证错误漏洞(CVE-2024-44308)**，远程攻击者可以诱骗受害者访问特制的网页并在系统上执行任意代码。**Apple 多款产品跨站脚本漏洞(CVE-2024-44309)**，诱骗受害者点击特制的链接，在用户浏览器中在任意网站的上下文中执行任意 HTML 和脚本代码。**鉴于这些漏洞已发现在野利用，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

iOS < 17.7.2

iOS < 18.1.1

iPadOS < 17.7.2

iPadOS < 18.1.1

macOS Sequoia < 15.1.1

visionOS < 2.1.1

**>****>****>****>**

**其他受影响组件**

无

**03**

**处置建议**

**>****>****>****>**

**安全更新**

目前官方已有可更新版本，建议受影响用户升级至最新版本：

iOS >=17.7.2

iOS >= 18.1.1

iPadOS >=17.7.2

iPadOS >= 18.1.1

macOS Sequoia >= 15.1.1

visionOS >= 2.1.1

请参阅发布说明：

https://support.apple.com/en-us/100100

**04**

**参考资料**

[1]https://support.apple.com/en-us/100100

**05**

**时间线**

2024年11月20日，奇安信 CERT发布安全风险通告。

**06**

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