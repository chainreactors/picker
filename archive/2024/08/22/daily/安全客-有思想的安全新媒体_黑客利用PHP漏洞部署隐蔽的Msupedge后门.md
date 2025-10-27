---
title: 黑客利用PHP漏洞部署隐蔽的Msupedge后门
url: https://www.anquanke.com/post/id/299353
source: 安全客-有思想的安全新媒体
date: 2024-08-22
fetch_date: 2025-10-06T18:01:23.728521
---

# 黑客利用PHP漏洞部署隐蔽的Msupedge后门

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

# 黑客利用PHP漏洞部署隐蔽的Msupedge后门

阅读量**64502**

发布时间 : 2024-08-21 14:09:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/hackers-exploit-php-vulnerability-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

一个名为 Msupedge 的以前未记录的后门已被用于对抗针对台湾一所未命名大学的网络攻击。

“这个后门最显着的特点是它通过DNS流量与命令和控制（C&C）服务器进行通信，”博通旗下的赛门铁克威胁猎人团队在与The Hacker News分享的一份报告中表示。

后门的起源目前尚不清楚，攻击背后的目标也尚不清楚。

据说可能有助于部署 Msupedge 的初始访问向量涉及利用最近披露的影响 PHP 的严重漏洞（CVE-2024-4577，CVSS 评分：9.8），该漏洞可用于实现远程代码执行。

有问题的后门是一个动态链接库 （DLL），它安装在路径“csidl\_drive\_fixed\xampp\”和“csidl\_system\wbem\”中。其中一个 DLL wuplog.dll由 Apache HTTP 服务器 （httpd） 启动。第二个 DLL 的父进程不清楚。

Msupedge最值得注意的方面是它依赖于DNS隧道与C&C服务器进行通信，其代码基于开源dnscat2工具。

“它通过执行名称解析来接收命令，”赛门铁克指出。“Msupedge不仅通过DNS流量接收命令，而且还使用C&C服务器的解析IP地址（ctl.msedeapi[.]net）作为命令。

具体来说，解析的 IP 地址的第三个八位字节用作开关大小写法，通过从后门中减去 7 并使用其十六进制表示法来触发适当的响应来确定后门的行为。例如，如果第三个八位字节为 145，则新派生的值将转换为 138 （0x8a）。

下面列出了 Msupedge 支持的命令 –

* 0x8a：使用通过 DNS TXT 记录接收的命令创建进程
* 0x75：使用通过 DNS TXT 记录接收的下载 URL 下载文件
* 0x24：在预定的时间间隔内睡觉
* 0x66：在预定的时间间隔内睡觉
* 0x38：创建一个用途未知的临时文件“%temp%\1e5bf625-1678-zzcv-90b1-199aa47c345.tmp”
* 0x3c：删除文件“%temp%\1e5bf625-1678-zzcv-90b1-199aa47c345.tmp”

这一发展是因为 UTG-Q-010 威胁组织与一个新的网络钓鱼活动有关，该活动利用加密货币和工作相关的诱饵来分发一种名为 Pupy RAT 的开源恶意软件。

赛门铁克表示：“攻击链涉及使用带有嵌入式DLL加载器的恶意.lnk文件，最终导致Pupy RAT有效载荷部署。“Pupy 是一种基于 Python 的远程访问木马 （RAT），具有反射 DLL 加载和内存中执行等功能。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/hackers-exploit-php-vulnerability-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299353](/post/id/299353)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/hackers-exploit-php-vulnerability-to.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/hackers-exploit-php-vulnerability-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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