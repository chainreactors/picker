---
title: 建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵
url: https://www.anquanke.com/post/id/300195
source: 安全客-有思想的安全新媒体
date: 2024-09-20
fetch_date: 2025-10-06T18:23:45.840322
---

# 建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵

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

# 建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵

阅读量**98316**

发布时间 : 2024-09-19 16:44:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Dark Reading Staff，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/application-security/contractor-software-targeted-mssql-loophole>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者一直以建筑行业总承包商常用的 Foundation 会计软件为目标，利用管道、HVAC 和混凝土子行业等中的积极漏洞。

Huntress 的研究人员最初在 9 月 14 日跟踪活动时发现了这种威胁。“让我们感到震惊的是，主机/域枚举命令是从 sqlservr.exe 的父进程中生成的，”研究人员在他们的咨询中写道。

应用程序使用的软件包括一个 Microsoft SQL Server （MSSQL） 实例，用于处理其数据库操作。据研究人员称，虽然将数据库服务器保存在内部网络或防火墙后面很常见，但 Foundation 软件包含允许通过移动应用程序访问的功能。因此，“TCP 端口 4243 可能会公开供移动应用程序使用。这个 4243 端口提供对 MSSQL 的直接访问。

同时，Microsoft SQL Server 有一个默认的系统管理员帐户，称为“sa”，该帐户对整个服务器具有完全管理权限。凭借如此高的权限，这些账户可以让用户运行 shell 命令和脚本。

据观察，针对该应用程序的威胁行为者大规模暴力破解应用程序，并使用默认凭据来访问受害者帐户。此外，威胁行为者似乎正在使用脚本来自动化他们的攻击。

建议组织轮换与 Foundation 软件关联的凭据，并保持安装与 Internet 断开连接，以防止成为这些攻击的受害者。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/application-security/contractor-software-targeted-mssql-loophole)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300195](/post/id/300195)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/application-security/contractor-software-targeted-mssql-loophole)

如若转载,请注明出处： <https://www.darkreading.com/application-security/contractor-software-targeted-mssql-loophole>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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