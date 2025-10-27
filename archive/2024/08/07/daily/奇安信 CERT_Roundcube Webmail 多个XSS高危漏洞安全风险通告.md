---
title: Roundcube Webmail 多个XSS高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501805&idx=1&sn=9bcc8e467e9b2b3ad370addf609efdf6&chksm=fe79e375c90e6a63762884c5e2c7beba403382963943a0863d187156c4387989205bcd4c533d&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-08-07
fetch_date: 2025-10-06T18:03:48.637939
---

# Roundcube Webmail 多个XSS高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icshasXShCm6C27W3D3gLT5XJqMRRweZiceu7gg0EXsOQ93jrB7rkPmibqOZB8lhFZWu7hKr7q0cwVQ/0?wx_fmt=jpeg)

# Roundcube Webmail 多个XSS高危漏洞安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Roundcube Webmail 多个XSS高危漏洞 | | |
| **漏洞编号** | CVE-2024-42008、CVE-2024-42009 | | |
| **公开时间** | 2024-08-04 | **影响量级** | 十万级 |
| **奇安信评级** | **高危** | ****CVSS 3.1分数**** | **9.8** |
| **威胁类型** | 代码执行 | **利用可能性** | **高** |
| **POC状态** | 未公开 | **在野利用状态** | 未发现 |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**未经身份验证的攻击者可以窃取电子邮件、联系人和密码等敏感信息。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

Roundcube Webmail是一个开源的基于Web的电子邮件客户端，使用户能够随时随地访问和处理他们的电子邮件。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复**Roundcube Webmail 跨站脚本漏洞(CVE-2024-42008)**和**Roundcube Webmail 跨站脚本漏洞(CVE-2024-42009)**。Roundcube Webmail在处理HTML和SVG等附件的过程中存在跨站脚本漏洞。未经身份验证的攻击者可以窃取电子邮件、联系人和密码等敏感信息。**鉴于之前的Roundcube Webmai漏洞曾多次在2023年被APT28、Winter Vivern等APT组织利用过，建议客户尽快做好自查及防护。**

**02**

**影响范围**

**>****>****>****>**

**影响版本**

Roundcube Webmai < 1.6.8

Roundcube Webmai < 1.5.8

**>****>****>****>**

**其他受影响组件**

无

**03**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，**Roundcube Webmail 跨站脚本漏洞(CVE-2024-42008)**和**Roundcube Webmail 跨站脚本漏洞(CVE-2024-42009)**关联的全球风险资产总数为3003195个，关联IP总数为342649个。全球风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icshasXShCm6C27W3D3gLT5Jw0icLFqljT9dibtjo9xYia60SiaKlJ9OichvcattAg6PUtveKYNO9xZWAA/640?wx_fmt=png&from=appmsg)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

目前官方已发布更新补丁，请及时升级至最新版本：

https://github.com/roundcube/roundcubemail/releases

**05**

**参考资料**

[1]https://roundcube.net/news/2024/08/04/security-updates-1.6.8-and-1.5.8

[2]https://www.sonarsource.com/blog/government-emails-at-risk-critical-cross-site-scripting-vulnerability-in-roundcube-webmail/

**06**

**时间线**

2024年8月6日，奇安信 CERT发布安全风险通告。

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