---
title: UAC-0125 滥用 Cloudflare 工作者分发伪装成 Army+ 应用程序的恶意软件
url: https://www.anquanke.com/post/id/302876
source: 安全客-有思想的安全新媒体
date: 2024-12-21
fetch_date: 2025-10-06T19:36:16.604763
---

# UAC-0125 滥用 Cloudflare 工作者分发伪装成 Army+ 应用程序的恶意软件

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

# UAC-0125 滥用 Cloudflare 工作者分发伪装成 Army+ 应用程序的恶意软件

阅读量**81849**

|评论**1**

发布时间 : 2024-12-20 10:27:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/uac-0125-abuses-cloudflare-workers-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

CERT-UA披露，它追踪到的一个名为 UAC-0125 的威胁行为者正在利用 Cloudflare Workers 服务，诱骗该国军人下载伪装成 Army+ 的恶意软件，这是一款由国防部于 2024 年 8 月推出的移动应用程序，旨在使武装部队实现无纸化。

访问假冒 Cloudflare Workers 网站的用户会被提示下载 Army+ 的 Windows 可执行文件，该文件是使用 Nullsoft Scriptable Install System（NSIS）创建的，NSIS 是一种用于创建操作系统安装程序的开源工具。

打开二进制文件会显示一个待启动的诱饵文件，同时还会执行一个 PowerShell 脚本，该脚本的目的是在受感染主机上安装 OpenSSH，生成一对 RSA 密钥，将公钥添加到 “authorized\_keys ”文件中，并使用 TOR 匿名网络将私钥传输到攻击者控制的服务器上。

CERT-UA 说，攻击的最终目的是让对手远程访问受害者的机器。目前还不知道这些链接是如何传播的。

该机构进一步指出，UAC-0125 与另一个名为 UAC-0002 的集群有关，该集群被称为 APT44、FROZENBARENTS、Sandworm、Seashell Blizzard 和 Voodoo Bear，是一个高级持续性威胁（APT）组织，与俄罗斯联邦武装力量总参谋部（GRU）下属的 74455 部队有联系。

本月早些时候，Fortra 发现 “合法服务滥用呈上升趋势”，不良行为者利用 Cloudflare Workers 和 Pages 托管虚假的 Microsoft 365 登录和人工验证页面，以窃取用户凭据。

该公司表示，针对Cloudflare Pages的网络钓鱼攻击增加了198%，从2023年的460起增加到2024年10月中旬的1370起。同样，利用Cloudflare Workers的网络钓鱼攻击也激增了104%，从2023年的2447起事件上升到迄今为止的4999起事件。

欧洲理事会对 16 名个人和 3 个实体实施了制裁，称他们对 “俄罗斯破坏海外稳定的行动 ”负有责任。

其中包括参与欧洲各地外国暗杀、爆炸和网络攻击的 GRU Unit 29155、在中非共和国和布基纳法索开展亲俄秘密影响行动的虚假信息网络 Groupe Panafricain pour le Commerce et l’Investissement，以及在非洲扩大俄罗斯宣传和虚假信息的新闻机构 African Initiative。

制裁还针对 “二重身”（Doppelganger）。“二重身 ”是一个由俄罗斯主导的虚假信息网络，以传播叙事和支持俄罗斯对乌克兰的侵略战争、操纵反对乌克兰的舆论和削弱西方支持而闻名。

为此，俄罗斯联邦总统信息和通信技术及通信基础设施发展办公室主任索菲亚-扎哈罗娃（Sofia Zakharova）和GK Struktura（又名Company Group Structura）的负责人和创始人尼古拉-图皮金（Nikolai Tupikin）已被冻结资产和禁止旅行。

早在 2024 年 3 月，图皮金还因参与外国恶意影响活动而受到美国财政部外国资产控制办公室（OFAC）的制裁。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/uac-0125-abuses-cloudflare-workers-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302876](/post/id/302876)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/uac-0125-abuses-cloudflare-workers-to.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/uac-0125-abuses-cloudflare-workers-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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