---
title: CISA 将 ADOBE COMMERCE 、 MAGENTO、SOLARWINDS SERV-U 和 VMWARE VCENTER SERVER 多个漏洞添加到其已知利用漏洞目录中
url: https://www.anquanke.com/post/id/298138
source: 安全客-有思想的安全新媒体
date: 2024-07-23
fetch_date: 2025-10-06T17:42:17.030904
---

# CISA 将 ADOBE COMMERCE 、 MAGENTO、SOLARWINDS SERV-U 和 VMWARE VCENTER SERVER 多个漏洞添加到其已知利用漏洞目录中

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

# CISA 将 ADOBE COMMERCE 、 MAGENTO、SOLARWINDS SERV-U 和 VMWARE VCENTER SERVER 多个漏洞添加到其已知利用漏洞目录中

阅读量**62584**

发布时间 : 2024-07-22 11:25:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/165981/hacking/u-s-cisa-adds-adobe-commerce-and-magento-solarwinds-serv-u-and-vmware-vcenter-server-bugs-to-its-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

美国网络安全和基础设施安全局 （CISA） 在其已知利用漏洞 （KEV） 目录中添加了以下漏洞：

* CVE-2024-34102Adobe Commerce 和 Magento 开源 XML 外部实体引用 （XXE） 的不当限制漏洞
* CVE-2024-28995SolarWinds Serv-U 路径遍历漏洞
* CVE-2022-22948VMware vCenter Server 默认文件权限不正确漏洞

以下是添加到 KEV 目录中的缺陷的描述：

**CVE-2024-34102**（CVSS 评分为 9.8）– 该缺陷是 XML 外部实体引用 （’XXE’） 的不当限制漏洞，可导致任意代码执行。攻击者可以通过发送引用外部实体的构建的 XML 文档来利用此问题。专家指出，利用这个问题不需要用户交互。该漏洞会影响 Adobe Commerce 版本 2.4.7、2.4.6-p5、2.4.5-p7、2.4.4-p8 及更早版本。Adobe警告说，它知道CVE-2024-34102已在针对Adobe Commerce商家的有限攻击中被广泛利用。

**CVE-2024-28995**（CVSS 评分为 7.5）– 该缺陷是 SolarWinds Serv-U Path 中的一个高严重性目录横向问题，允许攻击者读取主机上的敏感文件。该漏洞由 Hussein Daher 发现并报告。威胁情报公司 GreyNoise 的专家报告称，威胁行为者正在积极利用公开可用的概念验证 （PoC） 漏洞利用代码。

“SolarWinds Serv-U 容易受到目录横向漏洞的影响，该漏洞允许访问读取主机上的敏感文件。”阅读公告。

该漏洞于 6 月 6 日披露，它会影响 Serv-U 15.4.2 HF 1 和以前的版本。

在 Rapid7 发布有关该漏洞和 PoC 漏洞利用代码的技术细节后，GreyNoise 研究人员开始调查该问题。GitHub 用户 bigb0x 还分享了一个概念验证 （PoC） 和一个针对 SolarWinds Serv-U CVE-2024-28995 目录遍历漏洞的批量扫描程序。

“该漏洞非常简单，可以通过向根（）请求访问，并带有参数并设置为所需的文件。这个想法是文件夹，他们试图验证没有路径遍历段 （）。 是文件名。**报道**灰色噪音。`GET``/``InternalDir``InternalFile``InternalDir``../``InternalFile`

GreyNoise的研究人员在周末开始观察针对此问题的利用尝试。

一些失败的尝试依赖于公开可用的 PoC 漏洞的副本，而另一些尝试则与对攻击有更好了解的攻击者相关联。

*“我们看到人们正在积极地尝试这个漏洞——甚至可能是一个拿着键盘的人。这个漏洞和RCE之间的路线很棘手，所以我们很好奇人们会尝试什么！GreyNoise表示。*

**CVE-2022-22948**（CVSS 评分为 6.5）– vCenter Server 中的信息泄露漏洞，由文件权限不当导致。对 vCenter Server 具有非管理访问权限的恶意执行者可利用此问题获取敏感信息的访问权限。

根据约束性操作指令 （BOD） 22-01：降低已知利用漏洞的重大风险，FCEB 机构必须在截止日期前解决已识别的漏洞，以保护其网络免受利用目录中缺陷的攻击。

专家还建议私营组织审查目录并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2024 年 8 月 7 日之前修复此漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/165981/hacking/u-s-cisa-adds-adobe-commerce-and-magento-solarwinds-serv-u-and-vmware-vcenter-server-bugs-to-its-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298138](/post/id/298138)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/165981/hacking/u-s-cisa-adds-adobe-commerce-and-magento-solarwinds-serv-u-and-vmware-vcenter-server-bugs-to-its-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/165981/hacking/u-s-cisa-adds-adobe-commerce-and-magento-solarwinds-serv-u-and-vmware-vcenter-server-bugs-to-its-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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