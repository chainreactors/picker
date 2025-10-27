---
title: 威胁行为者利用Gafgyt恶意软件利用配置错误的Docker远程API服务器进行攻击
url: https://www.anquanke.com/post/id/302404
source: 安全客-有思想的安全新媒体
date: 2024-12-05
fetch_date: 2025-10-06T19:33:14.859248
---

# 威胁行为者利用Gafgyt恶意软件利用配置错误的Docker远程API服务器进行攻击

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

# 威胁行为者利用Gafgyt恶意软件利用配置错误的Docker远程API服务器进行攻击

阅读量**48200**

发布时间 : 2024-12-04 10:37:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/threat-actors-exploiting-misconfigured-docker-remote-api-servers-with-gafgyt-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-21626]()

趋势科技研究发现，Gafgyt 恶意软件（又称 Bashlite 或 Lizkebab）的行为发生了重大变化，它现在将错误配置的 Docker Remote API 服务器作为攻击目标。这标志着 Gafgyt 从传统上以易受攻击的物联网设备为攻击重点的转变。

报告显示，威胁者利用公开暴露和配置错误的 Docker 远程 API 服务器来部署 Gafgyt 恶意软件。攻击者使用合法镜像（如轻量级 “高山 ”镜像）创建 Docker 容器，并利用权限升级等技术获得对主机系统的控制权。报告称：”攻击者使用该命令将主机的根目录（/:）挂载到容器内的/mnt目录。这意味着容器可以访问和修改主机的文件系统，就好像它是自己文件系统的一部分。通过这样做，攻击者可以提升权限，并有可能获得对主机系统的控制权”。

![Gafgyt Docker API]()
Gafgyt 恶意软件攻击链 | 图片： 趋势科技

在观察到的攻击中，Gafgyt 二进制文件以 “rbot ”和 “atlas.i586 ”等文件名部署，这两个文件名都硬编码了命令与控制（C&C）服务器的 IP 地址和端口。这些二进制文件使攻击者能够使用 UDP、TCP、HTTP 和其他协议发起分布式拒绝服务 (DDoS) 攻击。趋势科技高级威胁研究员苏尼尔-巴蒂（Sunil Bharti）指出：“在容器部署尝试失败的情况下，攻击者会通过部署一个shell脚本再次尝试部署另一个变种的Gafgyt僵尸网络二进制文件，该脚本会针对不同的系统架构下载并执行僵尸网络二进制文件。”

一旦部署成功，恶意软件就会连接到其 C&C 服务器接收指令。然后，它就可以利用多种协议执行各种 DDoS 攻击，使目标不堪重负。此外，该恶意软件还包括通过与谷歌 DNS 服务器（8.8.8.8）交互来识别受害主机本地 IP 地址的功能。这一步骤可确保攻击者的命令在正确的网络环境中执行。

通过攻击 Docker 远程 API 服务器，威胁行为者可以利用企业级基础设施，从而可能导致比传统物联网设备入侵更严重的后果。Bharti 强调：“随着其目标扩展到通常范围之外，其行为发生了转变。”

趋势科技敦促企业通过禁用远程 API 访问（如果不需要）、实施强大的身份验证以及监控网络流量的异常活动来保护其 Docker 环境的安全。定期打补丁和适当的配置管理仍然是缓解此类威胁的关键。

本文翻译自securityonline [原文链接](https://securityonline.info/threat-actors-exploiting-misconfigured-docker-remote-api-servers-with-gafgyt-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302404](/post/id/302404)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/threat-actors-exploiting-misconfigured-docker-remote-api-servers-with-gafgyt-malware/)

如若转载,请注明出处： <https://securityonline.info/threat-actors-exploiting-misconfigured-docker-remote-api-servers-with-gafgyt-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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