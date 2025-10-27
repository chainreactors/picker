---
title: Brocade SANavv SAN 管理软件中披露的严重缺陷
url: https://www.anquanke.com/post/id/296077
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:36.899685
---

# Brocade SANavv SAN 管理软件中披露的严重缺陷

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Brocade SANavv SAN 管理软件中披露的严重缺陷

阅读量**67106**

发布时间 : 2024-04-28 11:07:56

**x**

##### 译文声明

本文是翻译文章，文章来源：https://thehackernews.com/2024/04/severe-flaws-disclosed-in-brocade.html

译文仅供参考，具体内容表达以及含义原文为准。

Brocade SANavav 存储区域网络 (SAN) 管理应用程序中披露的多个安全漏洞可能会被利用来危害易受影响的设备。

据发现并报告这些缺陷的独立安全研究员 Pierre Barre 称，这 18 个缺陷影响了2.3.0 及之前的所有版本。

这些问题包括不正确的防火墙规则、不安全的根访问、Docker 配置错误以及缺乏身份验证和加密，从而允许攻击者拦截凭据、覆盖任意文件并完全破坏设备。

下面列出了一些最严重的缺陷 –

CVE-2024-2859（CVSS 评分：8.8） – 该漏洞可能允许未经身份验证的远程攻击者使用 root 帐户登录受影响的设备并执行任意命令
CVE-2024-29960（CVSS 评分：7.5）- 在 OVA 映像中使用硬编码的 SSH 密钥，攻击者可利用该密钥来解密至 SANnav 设备的 SSH 流量并对其进行破坏。
CVE-2024-29961（CVSS 评分：8.2） – 该漏洞允许未经身份验证的远程攻击者利用 SANav 服务定期在后台向 gridgain 域发送 ping 命令这一事实发起供应链攻击[.]com 和 ignite.apache[.]org 检查更新
CVE-2024-29963（CVSS 评分：8.6）- 在 SANav OVA 中使用硬编码 Docker 密钥通过 TLS 到达远程注册表，从而允许攻击者对服务器进行中间对手 (AitM) 攻击交通
CVE-2024-29966 （CVSS 评分：7.5）-公开文档中存在 root 用户的硬编码凭据，可能允许未经身份验证的攻击者完全访问 Brocade SANava 设备。
继 2022 年 8 月和 2023 年 5 月两次负责任地披露后，这些缺陷已在 2023 年 12 月发布的 SANavv 2.3.1 版本中得到解决。博科的母公司博通（还拥有赛门铁克和 VMware）本月早些时候发布了针对这些缺陷的公告。

截至 2024 年 4 月 18 日，Hewlett Packard Enterprise 还针对 HPE SANava Management Portal 版本 2.3.0a 和 2.3.1 中的部分漏洞发布了补丁。

[![SANavav SAN管理软件]( "SANavav SAN管理软件")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivK9RYXyp11cybPUq0sODv6VQcYpUPIK4z3BsKUVBiTZyIb1YXdFqdCIp9AX-KAj2XeGXUYVY9jKW1xbGkbf0fGgR-ND9ocUJQmHsfLczH5COhhSJRkTXTOLZ28NXw369pwIRC5JYOmSEQzVTxsfpZQ8bwhagXECU8toVTxsfdsPwUUZ8RyZVf6-sJL-GX/s728-rw-e365/2024-sannav-credentials.png)

本文翻译自https://thehackernews.com/2024/04/severe-flaws-disclosed-in-brocade.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296077](/post/id/296077)

安全KER - 有思想的安全新媒体

本文转载自: https://thehackernews.com/2024/04/severe-flaws-disclosed-in-brocade.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)