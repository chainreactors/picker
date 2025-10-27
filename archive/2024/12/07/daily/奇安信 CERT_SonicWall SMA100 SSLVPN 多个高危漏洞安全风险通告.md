---
title: SonicWall SMA100 SSLVPN 多个高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502571&idx=1&sn=c30e1d47ae1059542d59b52c7c4ddfd5&chksm=fe79ee73c90e67653d869887a830bf2a25190cbd667ff181b5e7f6535ba46c4cfb73f220d44f&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-12-07
fetch_date: 2025-10-06T19:39:58.100909
---

# SonicWall SMA100 SSLVPN 多个高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icS66Cd5DvxFJLefBww7iajO5iaCQuClv6PIRjESxlxPsfdl7bptmYEjibygWrbsMlAMBIMKUhEpdJpw/0?wx_fmt=jpeg)

# SonicWall SMA100 SSLVPN 多个高危漏洞安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | SonicWall SMA100 SSLVPN 多个高危漏洞 | | |
| **漏洞编号** | CVE-2024-45318,CVE-2024-53703 | | |
| ****公开时间**** | 2024-12-05 | ****影响量级**** | 十万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **8.1** |
| **威胁类型** | 代码执行 | **利用可能性** | ****高**** |
| **POC状态** | 未公开 | **在野利用状态** | 未发现 |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**该漏洞可能使攻击者能够远程执行代码，获取系统控制权，从而造成严重的安全威胁。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

SonicWall SMA100 SSLVPN是一款为中小企业设计的SSL VPN设备，旨在提供安全的远程访问解决方案，允许用户通过加密的网络连接安全地访问内部网络资源。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复 **SonicWall SMA100 SSLVPN web管理页面栈缓冲区溢出漏洞(CVE-2024-45318)** 和 **SonicWall SMA100 mod\_httprp栈缓冲区溢出漏洞(CVE-2024-53703)**，SonicWall SMA100 SSLVPN的Web管理界面和Apache Web服务器加载的mod\_httprp库分别存在两个栈缓冲区溢出漏洞，这些漏洞可能允许远程攻击者执行任意代码，造成系统敏感数据泄露甚至服务器被接管等严重安全威胁。**鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

SMA 100 Series (SMA 200, 210, 400, 410, 500v) <= 10.2.1.13-72sv

**>****>****>****>**

**其他受影响组件**

无

**03**

**处置建议**

**>****>****>****>**

**安全更新**

SonicWall官方已经发布了修复这些漏洞的固件版本。用户应立即升级到官方推荐的固定版本，即SMA 100系列的10.2.1.14-75sv或更高版本。

官方补丁下载地址：

https://www.sonicwall.com/zh-cn/support

**修复缓解措施：**

1.限制对SMA100 SSLVPN管理接口的访问，只允许受信任的IP地址范围访问管理界面，以减少潜在攻击者的机会；

2.关注SonicWall的官方安全通告，以便在新的漏洞或威胁出现时及时获得信息，并采取相应的防护措施。

**04**

**参考资料**

[1]https://nvd.nist.gov/vuln/detail/CVE-2024-45318

[2]https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0018

**05**

**时间线**

2024年12月06日，奇安信 CERT发布安全风险通告。

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