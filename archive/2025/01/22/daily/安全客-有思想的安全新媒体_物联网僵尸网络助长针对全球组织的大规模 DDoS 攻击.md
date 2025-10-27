---
title: 物联网僵尸网络助长针对全球组织的大规模 DDoS 攻击
url: https://www.anquanke.com/post/id/303681
source: 安全客-有思想的安全新媒体
date: 2025-01-22
fetch_date: 2025-10-06T20:04:43.648867
---

# 物联网僵尸网络助长针对全球组织的大规模 DDoS 攻击

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

# 物联网僵尸网络助长针对全球组织的大规模 DDoS 攻击

阅读量**60334**

发布时间 : 2025-01-21 11:06:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/iot-botnet-fuels-large-scale-ddos-attacks-targeting-global-organizations/>

译文仅供参考，具体内容表达以及含义原文为准。

![IoT Botnet]()

据趋势科技研究公司（Trend Micro Research）的一份报告称，一个新发现的物联网僵尸网络与一系列针对全球组织（包括日本大型企业和金融机构）的大规模分布式拒绝服务（DDoS）攻击有关。该僵尸网络利用源自 Mirai 和 Bashlite 的恶意软件，利用远程代码执行漏洞和弱设备密码感染物联网设备并策划攻击。

趋势科技观察到，该僵尸网络的命令与控制（C&C）服务器发出针对亚洲、北美和欧洲实体的 DDoS 命令。该报告称，“自 2024 年末以来，一直观察到该僵尸网络发布 DDoS 攻击命令”，并补充说，攻击导致多个目标组织的连接暂时中断。

恶意软件通过易受攻击的物联网设备传播，如无线路由器和 IP 摄像机。一旦感染，设备就会执行有效载荷，连接到僵尸网络的 C&C 服务器，等待攻击命令。值得注意的是，该恶意软件会禁用看门狗定时器，以确保在资源密集型 DDoS 攻击期间不间断运行。

该僵尸网络支持多种 DDoS 技术，详见报告：

* **SYN Floods**： 用 TCP SYN 数据包淹没目标服务器。
* **ACK 泛滥**： 发送大量 ACK 数据包，扰乱服务器响应。
* **踩踏攻击**： 使用带有随机有效载荷的简单文本定向信息协议。
* **GRE 攻击**： 利用通用路由器封装协议。

在 2024 年 12 月至 2025 年 1 月期间，僵尸网络的攻击目标涉及多个行业的组织，日本目标和国际目标的攻击方法存在明显差异。例如，stomp 命令在日本的攻击中占 21%，而在国际目标中仅占 7%。相反，基于 GRE 的攻击在国际上更为常见。

主要受害者包括信息技术、金融和运输行业。国际目标主要是信息和通信行业，占攻击的 34%。

僵尸网络的构成反映了物联网设备不安全这一令人担忧的趋势。无线路由器占受感染设备的 80%，其中以 TP-Link 和 Zyxel 路由器居多。海康威视等公司生产的 IP 摄像机占 15%。印度和南非是受感染设备最多的国家，分别占 57% 和 17%。

趋势科技确定了导致僵尸网络增长的关键漏洞：

* **默认设置**： 未更改的默认密码使设备容易成为攻击目标。
* **过时固件**： 存在已知漏洞的旧版软件经常被利用。
* **安全功能不足**： 许多物联网设备缺乏足够的安全措施。

加强物联网设备的安全性对于应对僵尸网络带来的日益严重的威胁至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/iot-botnet-fuels-large-scale-ddos-attacks-targeting-global-organizations/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303681](/post/id/303681)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/iot-botnet-fuels-large-scale-ddos-attacks-targeting-global-organizations/)

如若转载,请注明出处： <https://securityonline.info/iot-botnet-fuels-large-scale-ddos-attacks-targeting-global-organizations/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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