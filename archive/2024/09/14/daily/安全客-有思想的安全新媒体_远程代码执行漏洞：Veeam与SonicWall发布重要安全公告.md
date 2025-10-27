---
title: 远程代码执行漏洞：Veeam与SonicWall发布重要安全公告
url: https://www.anquanke.com/post/id/300062
source: 安全客-有思想的安全新媒体
date: 2024-09-14
fetch_date: 2025-10-06T18:24:08.227318
---

# 远程代码执行漏洞：Veeam与SonicWall发布重要安全公告

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

# 远程代码执行漏洞：Veeam与SonicWall发布重要安全公告

阅读量**86616**

发布时间 : 2024-09-13 15:12:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 cyberhoot

原文地址：<https://cyberhoot.com/advisory/dual-critical-advisory-critical-vulnerabilities-in-veeam-backup-replication-and-sonicwall-sonicos/?utm_source=rss&utm_medium=rss&utm_campaign=dual-critical-advisory-critical-vulnerabilities-in-veeam-backup-replication-and-sonicwall-sonicos>

译文仅供参考，具体内容表达以及含义原文为准。

## Veeam Backup & Replication：漏洞的关键补丁

**概述：**Veeam发布了针对13个高严重性和五个关键性漏洞的补丁，其中包括Veeam备份与复制中的一个无需认证的远程代码执行（RCE）漏洞（CVE-2024-40711），该漏洞的CVSS评分为9.8。此漏洞可能允许攻击者完全接管系统，发现该漏洞的安全公司CODE WHITE警告称，公开技术细节可能会导致勒索软件团伙利用这一漏洞。

**主要漏洞：**

* 无需认证的RCE：无需用户认证即可远程执行代码并危害系统。
* 其他漏洞可能导致未经授权的访问、数据暴露和系统操控。

**建议：**

* **立即修补**：将最新的 Veeam 更新应用于所有受影响的系统。
* **加强监控**：对修补后的异常活动实施增强监控。
* **定期备份**：确保异地和离线备份可用于快速恢复。

## SonicWall SonicOS：CVE-2024-40766 正在被积极利用

**概述：**在SonicWall的SonicOS管理访问和SSLVPN（CVE-2024-40766）中发现了一个关键漏洞，这可能导致未经授权的资源访问。在某些情况下，此漏洞可导致防火墙崩溃。SonicWall确认该漏洞正在野外被积极利用，使得这一漏洞尤为紧急。

**受影响的系统：**

* SOHO （Gen 5） 5.9.2.14-12o 及更早版本
* Gen6 防火墙 6.5.4.14-109n 及更早版本
* Gen7 防火墙 SonicOS 内部版本：7.0.1-5035 及更早版本

**威胁情报：**SonicWall 报告称，CVE-2024-40766 被积极利用，因此迫切需要立即采取行动。

**风险：**

* **大中型企业**：高
* **小型企业**：中
* **家庭用户**：低

**建议：**

* **立即应用补丁**：使用 SonicWall 提供的最新安全补丁更新 SonicOS Management Access 和 SSLVPN 系统。
* **实施网络分段**：使用逻辑网络分段来隔离关键系统并减少暴露。
* **监控和响应**：确保监控系统到位以检测未经授权的访问尝试，并为潜在的入侵制定响应计划。

本文翻译自 [原文链接](https://cyberhoot.com/advisory/dual-critical-advisory-critical-vulnerabilities-in-veeam-backup-replication-and-sonicwall-sonicos/?utm_source=rss&utm_medium=rss&utm_campaign=dual-critical-advisory-critical-vulnerabilities-in-veeam-backup-replication-and-sonicwall-sonicos)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300062](/post/id/300062)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cyberhoot.com/advisory/dual-critical-advisory-critical-vulnerabilities-in-veeam-backup-replication-and-sonicwall-sonicos/?utm_source=rss&utm_medium=rss&utm_campaign=dual-critical-advisory-critical-vulnerabilities-in-veeam-backup-replication-and-sonicwall-sonicos>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [Veeam Backup & Replication：漏洞的关键补丁](#h2-0)
* [SonicWall SonicOS：CVE-2024-40766 正在被积极利用](#h2-1)

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