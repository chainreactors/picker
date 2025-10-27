---
title: Traccar GPS 系统的严重漏洞使用户面临远程攻击
url: https://www.anquanke.com/post/id/299520
source: 安全客-有思想的安全新媒体
date: 2024-08-28
fetch_date: 2025-10-06T18:03:47.590697
---

# Traccar GPS 系统的严重漏洞使用户面临远程攻击

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

# Traccar GPS 系统的严重漏洞使用户面临远程攻击

阅读量**68489**

发布时间 : 2024-08-27 11:03:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/critical-flaws-in-traccar-gps-system.html>

译文仅供参考，具体内容表达以及含义原文为准。

开源 Traccar GPS 跟踪系统中已披露两个安全漏洞，在某些情况下，未经身份验证的攻击者可能会利用这些漏洞来实现远程代码执行。

Horizon3.ai 研究员 Naveen Sunkavally 表示，这两个漏洞都是路径遍历缺陷，如果启用访客注册，则可能会被武器化，这是 Traccar 5 的默认配置。

缺点的简要描述如下 –

* **CVE-2024-24809**（CVSS 评分：8.5）- 路径遍历：’dir/../../filename’ 和不受限制地上传危险类型的文件
* **CVE-2024-31214** （CVSS score： 9.7） – 设备镜像上传中存在不受限制的文件上传漏洞，可能导致远程代码执行

“CVE-2024-31214 和 CVE-2024-24809 的最终结果是，攻击者可以将包含任意内容的文件放置在文件系统上的任何位置，”Sunkavally 说。“但是，攻击者只能部分控制文件名。”

这些问题与程序如何处理设备映像文件上传有关，有效地允许攻击者覆盖文件系统上的某些文件并触发代码执行。这包括与以下命名格式匹配的文件 –

* device.ext，攻击者可以在其中控制 ext，但必须有一个扩展
* blah“，其中攻击者可以控制 blah，但文件名必须以双引号结尾
* blah1“;blah2=blah3，攻击者可以控制 blah1、blah2 和 blah3，但必须存在双引号分号序列和等于符号

在 Horizon3.ai 设计的假设概念验证 （PoC） 中，攻击者可以利用 Content-Type 标头中的路径遍历来上传 crontab 文件并在攻击者主机上获得反向 shell。

但是，这种攻击方法不适用于基于 Debian/Ubuntu 的 Linux 系统，因为文件命名限制禁止 crontab 文件使用句点或双引号。

另一种机制需要利用以 root 用户身份安装的 Traccar 来删除内核模块，或配置 udev 规则以在每次引发硬件事件时运行任意命令。

在易受攻击的 Windows 实例上，还可以通过在 C：\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp 文件夹中放置名为“device.lnk”的快捷方式 （LNK） 文件来实现远程代码执行，该文件随后在任何受害者用户登录到 Traccar 主机时执行。

Traccar 版本 5.1 到 5.12 容易受到 CVE-2024-31214 和 CVE-2024-2809 的攻击。这些问题已在 2024 年 4 月发布的 Traccar 6 中得到解决，该版本默认关闭自注册，从而减少攻击面。

“如果注册设置为 true，readOnly 为 false，deviceReadonly 为 false，则未经身份验证的攻击者可以利用这些漏洞，”Sunkavally 说。“这些是 Traccar 5 的默认设置。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/critical-flaws-in-traccar-gps-system.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299520](/post/id/299520)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/critical-flaws-in-traccar-gps-system.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/critical-flaws-in-traccar-gps-system.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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