---
title: 新发现OpenSSH漏洞：潜在远程代码执行风险
url: https://www.anquanke.com/post/id/297844
source: 安全客-有思想的安全新媒体
date: 2024-07-13
fetch_date: 2025-10-06T17:39:35.316261
---

# 新发现OpenSSH漏洞：潜在远程代码执行风险

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

# 新发现OpenSSH漏洞：潜在远程代码执行风险

阅读量**182638**

发布时间 : 2024-07-12 09:59:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/new-openssh-vulnerability-discovered.html>

译文仅供参考，具体内容表达以及含义原文为准。

OpenSSH安全网络套件的某些版本存在一个新的漏洞，该漏洞可能触发远程代码执行（RCE）。

该漏洞被跟踪为 CVE-2024-6409（CVSS 评分：7.0），与 CVE-2024-6387（又名 RegreSSHion）不同，与由于信号处理中的争用条件而导致的 privsep 子进程中的代码执行情况有关。它仅影响 Red Hat Enterprise Linux 9 附带的 8.7p1 和 8.8p1 版本。

安全研究员亚历山大·佩斯利亚克（Alexander Peslyak）的别名是太阳能设计师，他因发现和报告该漏洞而受到赞誉，该漏洞是在本月早些时候Qualys披露CVE-2024-6387后在审查CVE-2024-6387时发现的。

“与 CVE-2024-6387 的主要区别在于，竞争条件和 RCE 潜力是在 privsep 子进程中触发的，与父服务器进程相比，该进程以较低的权限运行，”Peslyak 说。

“因此，直接影响较低。但是，在特定情况下，这些漏洞的可利用性可能存在差异，这可能使其中任何一个对攻击者来说更具吸引力，如果只有一个漏洞得到修复或缓解，那么另一个漏洞就会变得更加重要。

但是，值得注意的是，信号处理程序争用条件漏洞与 CVE-2024-6387 相同，其中如果客户端未在 LoginGraceTime 秒（默认为 120 秒）内进行身份验证，则 OpenSSH 守护进程的 SIGALRM 处理程序将被异步调用，然后调用各种非异步信号安全的函数。

根据漏洞描述，“此问题使其容易受到 cleanup\_exit（） 函数上的信号处理程序争用条件的影响，该条件在 SSHD 服务器的非特权子项中引入了与 CVE-2024-6387 相同的漏洞。

“由于攻击成功，在最坏的情况下，攻击者可能能够在运行 sshd 服务器的非特权用户中执行远程代码执行 （RCE）。

此后，在野外检测到 CVE-2024-6387 的活跃漏洞，未知威胁行为者主要针对位于中国的服务器。

“此攻击的初始向量源自 IP 地址 108.174.58[.]28，据报道，该目录列出了用于自动利用易受攻击的SSH服务器的漏洞利用工具和脚本，“以色列网络安全公司Veriti说。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/new-openssh-vulnerability-discovered.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297844](/post/id/297844)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/new-openssh-vulnerability-discovered.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/new-openssh-vulnerability-discovered.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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