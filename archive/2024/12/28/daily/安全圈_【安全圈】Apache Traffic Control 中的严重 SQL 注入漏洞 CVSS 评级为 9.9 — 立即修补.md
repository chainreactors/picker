---
title: 【安全圈】Apache Traffic Control 中的严重 SQL 注入漏洞 CVSS 评级为 9.9 — 立即修补
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066971&idx=2&sn=f33a68d33d05344d8693a65a70f992ef&chksm=f36e78dbc419f1cdcdcf32755abea904b5b856bdc3e50b4b246d6fb2c1e03efbf5eba2adf433&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-28
fetch_date: 2025-10-06T19:39:16.323767
---

# 【安全圈】Apache Traffic Control 中的严重 SQL 注入漏洞 CVSS 评级为 9.9 — 立即修补

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgBD2icZhFccozdbiaDibbkZTsibbChowktTWfBO5ice3iaf9qqoUtYicsz2q12tibv7km4u1TibAuNZFJgjZw/0?wx_fmt=jpeg)

# 【安全圈】Apache Traffic Control 中的严重 SQL 注入漏洞 CVSS 评级为 9.9 — 立即修补

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgBD2icZhFccozdbiaDibbkZTsWicpGY2A15QIjSVIOVHHWKdF9ha3tiacXE2JibpTVTzwLSs4iczO7U7o4g/640?wx_fmt=other&from=appmsg)

Apache 软件基金会 (ASF) 已发布安全更新来修复流量控制中的一个严重安全漏洞，如果成功利用该漏洞，攻击者可以在数据库中执行任意结构化查询语言 (SQL) 命令。

该 SQL 注入漏洞的编号为CVE-2024-45387，在 CVSS 评分系统中的评分为 9.9 分（满分 10.0 分）。

项目维护人员在一份公告中表示：“Apache Traffic Control <= 8.0.1、>= 8.0.0 中的 Traffic Ops 中存在一个 SQL 注入漏洞，允许具有

‘admin’、‘federation’、‘operations’、‘portal’、‘steering’

角色的特权用户通过发送特制的 PUT 请求对数据库执行任意 SQL 。 ”

Apache Traffic Control是内容分发网络 (CDN) 的开源实现。它于 2018 年 6 月被AS宣布为顶级项目 (TLP)。

腾讯云顶安全实验室发现并报告了该漏洞。该漏洞已在 Apache Traffic Control 8.0.2 版本中得到修复。

此次开发正值 ASF解决了Apache HugeGraph-Server (CVE-2024-43441) 1.0 至 1.3 版本中的身份验证绕过漏洞。1.5.0 版本中已发布了针对该缺陷的修复程序。

它还发布了针对 Apache Tomcat（CVE-2024-56337）中一个重要漏洞的补丁，该漏洞可能在某些条件下导致远程代码执行（RCE）。

SQL注入攻击是一种常见的网络攻击手段，攻击者通过在输入字段中插入恶意SQL代码，试图欺骗应用程序以执行不安全的数据库操作。建议用户将其实例更新到软件的最新版本，以防范潜在威胁。

检测SQL注入攻击的方法

输入检查：对用户输入进行充分的验证和转义，防止恶意的SQL代码被执行。
日志分析：分析应用程序的访问日志，检测异常的URL、异常的用户行为等。
数据库监控：监视数据库的活动，检测异常的查询和操作。
漏洞扫描：使用漏洞扫描工具检测应用程序中的安全漏洞，包括SQL注入漏洞。
Web应用程序防火墙：监控应用程序的流量，检测和阻止SQL注入攻击。

### 防御SQL注入攻击的措施

使用预编译语句和参数化查询：这是防止SQL注入的最有效方法之一，通过使用占位符而不是直接拼接字符串来构建SQL命令。
输入验证：检查用户输入的合法性，确信输入的内容只包含合法的数据。
错误消息处理：避免出现详细的错误消息，因为黑客们可以利用这些消息。
最小权限原则：为数据库账号分配最小必要的权限，即使存在注入漏洞，攻击者也无法执行高风险操作。

参考来源：https://thehackernews.com/2024/12/critical-sql-injection-vulnerability-in.html

***END***

阅读推荐

[【安全圈】看不到的尽头，回顾与展望哈以冲突以来的中东网络战](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=1&sn=41fcfb549fe6615344138a9b1dd305a6&scene=21#wechat_redirect)

[【安全圈】日本航空系统遭受网络攻击，航班运营受到影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=2&sn=3e1dc47d1e9b6168f7631925ca6ddc17&scene=21#wechat_redirect)

[【安全圈】iOS 设备比 Android 设备更容易受到网络钓鱼的攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=3&sn=61fa616d789cbc824c026a48a98d9e84&scene=21#wechat_redirect)

[【安全圈】土耳其出台更严格的加密货币反洗钱法规](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066949&idx=4&sn=4490e636262f92d14975414c55a29edb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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