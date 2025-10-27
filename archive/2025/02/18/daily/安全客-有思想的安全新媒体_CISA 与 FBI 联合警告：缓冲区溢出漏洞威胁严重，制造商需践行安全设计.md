---
title: CISA 与 FBI 联合警告：缓冲区溢出漏洞威胁严重，制造商需践行安全设计
url: https://www.anquanke.com/post/id/304396
source: 安全客-有思想的安全新媒体
date: 2025-02-18
fetch_date: 2025-10-06T20:36:05.921266
---

# CISA 与 FBI 联合警告：缓冲区溢出漏洞威胁严重，制造商需践行安全设计

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

# CISA 与 FBI 联合警告：缓冲区溢出漏洞威胁严重，制造商需践行安全设计

阅读量**58819**

发布时间 : 2025-02-17 14:27:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/buffer-overflows-vulnerabilities-cisa-fbi-issue-urgent-warning/>

译文仅供参考，具体内容表达以及含义原文为准。

![Buffer Overflows Vulnerabilities]()

美国网络安全与基础设施安全局（CISA）和联邦调查局（FBI）在一份联合发布的 “安全设计警报” 中，就缓冲区溢出漏洞带来的持续性威胁发出了警告，此类漏洞有可能危及软件安全，并对国家和经济安全造成危害。该警报强调，制造商有必要采用 “安全设计” 原则以及经实践验证的缓解技术，以消除这类安全缺陷。

这两个机构着重指出了缓冲区溢出漏洞的普遍性，这是一种内存安全缺陷，“常常会导致系统被攻破”。正如该机构所解释的那样，“当威胁行为者在计算机内存的错误区域（即在内存缓冲区之外）访问或写入信息时，就会出现缓冲区溢出漏洞（CWE-119）”。这些漏洞可能表现为基于栈的溢出（CWE-121）或基于堆的溢出（CWE-122），并可能产生严重后果，包括数据损坏、敏感数据泄露、程序崩溃，以及最令人担忧的 —— 未经授权的代码执行。

该警报强调了这一威胁的严重性，并指出 “威胁行为者经常利用这些漏洞，先获取对某个组织网络的初始访问权限，然后在更广泛的网络中进行横向移动”。警报中列举了一些近期的案例，包括 CVE-2025-21333、CVE-2025-0282、CVE-2024-49138、CVE-2024-38812、CVE-2023-6549 和 CVE-2022-0185，这表明此类问题一直存在。

尽管有大量记录在案的缓解措施，但 CISA 和 FBI 仍表示担忧，称 “许多制造商继续采用不安全的软件开发实践，使得这些漏洞一直存在”。他们坚称，采用不安全的做法，“尤其是使用内存不安全的编程语言”，对 “我们的国家和经济安全构成了不可接受的风险”。

该警报呼吁制造商立即采取行动，敦促他们采用文件中概述的 “安全设计” 实践。这些实践包括使用内存安全的语言、实施适当的输入验证，以及采用其他经实践验证的技术来防止缓冲区溢出。CISA 和 FBI 还建议软件客户 “向制造商要求提供安全的产品”，具体方式是索要软件物料清单（SBOM）和安全软件开发证明。这使客户能够核实制造商是否正在采取必要措施来解决这些关键漏洞。

这两个机构强调，虽然所有内存安全漏洞都值得关注，但缓冲区溢出漏洞是其中特别容易理解的一类，并且有现成的解决方案。他们强调，软件中没有理由继续存在这些漏洞。警报中指出：“出于这些原因，以及这些缺陷被利用可能造成的损害，CISA、FBI 和其他相关机构将缓冲区溢出漏洞认定为不可原谅的缺陷。”

本文翻译自securityonline [原文链接](https://securityonline.info/buffer-overflows-vulnerabilities-cisa-fbi-issue-urgent-warning/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304396](/post/id/304396)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/buffer-overflows-vulnerabilities-cisa-fbi-issue-urgent-warning/)

如若转载,请注明出处： <https://securityonline.info/buffer-overflows-vulnerabilities-cisa-fbi-issue-urgent-warning/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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