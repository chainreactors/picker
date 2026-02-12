---
title: 【已复现】微信 Linux版本命令执行漏洞(QVD-2026-7687)安全风险通告
url: https://mp.weixin.qq.com/s/Jopoi2JGbbJYhmcRqa6-0w
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:19:27.426389
---

# 【已复现】微信 Linux版本命令执行漏洞(QVD-2026-7687)安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uw1QWVnGU8v57CdjbClTm9eAy4DBFYLHZk84R7yk7JU5YJdqneicB0gw6dRs1zGkgDdMYVvaD7iamkAObhicGchQlV7cuYLzlicC0/0?wx_fmt=jpeg)

# 【已复现】微信 Linux版本命令执行漏洞(QVD-2026-7687)安全风险通告

奇安信 CERT
奇安信 CERT

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 微信 Linux版本命令执行漏洞 | | |
| **漏洞编号** | QVD-2026-7687 | | |
| ****公开时间**** | 2026-02-10 | ****影响量级**** | 千万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **8.0** |
| **威胁类型** | 命令执行 | **利用可能性** | ****高**** |
| **POC状态** | **已公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **未公开** | **技术细节状态** | **已公开** |
| **危害描述：**攻击者可诱导用户打开恶意文件名的文件从而导致命令执行，获取系统权限。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

微信 Linux版一款跨平台的通讯工具。支持单人、多人参与。通过手机网络发送语音、图片、视频和文字。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到微信 Linux版本命令执行漏洞(QVD-2026-7687)，该漏洞源于微信 Linux版文件名校验不严格，攻击者可诱导用户打开恶意文件名的文件从而导致命令执行，获取系统权限。目前该漏洞PoC已公开。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**>****>****>****>**

**利用条件**

用户点击恶意文件。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

微信 Linux版本 <= 4.1.0.13

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现微信 Linux版本命令执行漏洞(QVD-2026-7687)，截图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555sD1OOmM612CAbqHJJcBLmtt3dxkX1ms43O8ibe0VeQ87leBe73lN2MnBQiayyBT7werfh0PCNdU0QQQCW5LvadOiaPFRkg9UDxA4/640?wx_fmt=jpeg&from=appmsg)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布安全补丁，请及时更新至最新版本：

微信 Linux版本 >= 4.1.0.16

下载地址：

https://linux.weixin.qq.com/

**05**

**参考资料**

[1]https://linux.weixin.qq.com/

**06**

**时间线**

2026年02月11日，奇安信 CERT发布安全风险通告。

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