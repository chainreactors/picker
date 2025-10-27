---
title: 新的 OpenSSH 漏洞可能导致 Linux 系统以 Root 身份进行 RCE
url: https://www.anquanke.com/post/id/297640
source: 安全客-有思想的安全新媒体
date: 2024-07-03
fetch_date: 2025-10-06T17:39:23.732090
---

# 新的 OpenSSH 漏洞可能导致 Linux 系统以 Root 身份进行 RCE

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

# 新的 OpenSSH 漏洞可能导致 Linux 系统以 Root 身份进行 RCE

阅读量**192692**

发布时间 : 2024-07-02 13:24:34

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/07/new-openssh-vulnerability-could-lead-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

OpenSSH 维护人员发布了安全更新，以修复一个严重的安全漏洞，该漏洞可能导致基于 glibc 的 Linux 系统中以 root 权限执行未经身份验证的远程代码。

该漏洞代号为 regreSSHion，CVE 标识符为 CVE-2024-6387。它位于OpenSSH 服务器组件（也称为 sshd）中，用于监听来自任何客户端应用程序的连接。

Qualys 威胁研究部门高级主管 Bharat Jogi 在今天发布的一份披露文件中表示：“该漏洞是 OpenSSH 服务器 (sshd) 中的信号处理程序竞争条件，允许在基于 glibc 的 Linux 系统上以 root 身份进行未经身份验证的远程代码执行 (RCE) 。该竞争条件会影响默认配置下的 sshd。”

该网络安全公司表示，已发现至少 1400 万个暴露在互联网上的潜在易受攻击的 OpenSSH 服务器实例，并补充说，这是一个已修补的 18 年前的漏洞（跟踪号为CVE-2006-5051）的回归，该问题于 2020 年 10 月作为 OpenSSH 版本 8.5p1 的一部分重新出现。

OpenSSH 在一份公告中表示：“已证明在具有 [地址空间布局随机化]的 32 位 Linux/glibc 系统上可成功利用该漏洞。在实验室条件下，攻击平均需要 6-8 小时的连续连接，直至达到服务器可接受的最大连接时长。”

该漏洞影响 8.5p1 和 9.7p1 之间的版本。4.4p1 之前的版本也容易受到竞争条件漏洞的影响，除非它们针对 CVE-2006-5051 和CVE-2008-4109进行了修补。值得注意的是，OpenBSD 系统不受影响，因为它们包含阻止该漏洞的安全机制。

该安全漏洞很可能也会影响 macOS 和 Windows，尽管其在这些平台上的可利用性仍未得到证实，需要进一步分析。
具体来说，Qualys 发现，如果客户端在 120 秒内未进行身份验证（由 LoginGraceTime 定义的设置），则 sshd 的 SIGALRM 处理程序将以非异步信号安全的方式异步调用。

利用 CVE-2024-6387 的最终结果是完全系统入侵和接管，使威胁行为者能够以最高权限执行任意代码、破坏安全机制、窃取数据，甚至保持持续访问。

“漏洞一旦修复，又会在后续软件版本中再次出现，这通常是由于更改或更新无意中再次引入了该问题，”Jogi 说道。“这起事件凸显了彻底的回归测试在防止已知漏洞再次引入环境中的关键作用。”

虽然该漏洞由于其远程竞争条件性质而存在重大障碍，但建议用户应用最新补丁以防范潜在威胁。还建议通过基于网络的控制来限制 SSH 访问，并实施网络分段以限制未经授权的访问和横向移动。

本文翻译自 [原文链接](https://thehackernews.com/2024/07/new-openssh-vulnerability-could-lead-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297640](/post/id/297640)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/07/new-openssh-vulnerability-could-lead-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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