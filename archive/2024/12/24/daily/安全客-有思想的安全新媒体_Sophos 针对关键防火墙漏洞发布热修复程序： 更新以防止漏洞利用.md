---
title: Sophos 针对关键防火墙漏洞发布热修复程序： 更新以防止漏洞利用
url: https://www.anquanke.com/post/id/302935
source: 安全客-有思想的安全新媒体
date: 2024-12-24
fetch_date: 2025-10-06T19:36:39.377511
---

# Sophos 针对关键防火墙漏洞发布热修复程序： 更新以防止漏洞利用

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

# Sophos 针对关键防火墙漏洞发布热修复程序： 更新以防止漏洞利用

阅读量**64723**

|评论**1**

发布时间 : 2024-12-23 14:17:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/sophos-fixes-3-critical-firewall-flaws.html>

译文仅供参考，具体内容表达以及含义原文为准。

Sophos 已发布热修复程序，以解决 Sophos 防火墙产品中的三个安全漏洞，这些漏洞在某些条件下可被利用来实现远程代码执行并允许特权系统访问。

在这三个漏洞中，有两个的严重程度被评为 “严重”。目前还没有证据表明这些漏洞已在野外被利用。漏洞列表如下

* CVE-2024-12727（CVSS 得分：9.8）- 如果启用安全 PDF eXchange (SPX)的特定配置并结合防火墙在高可用性 (HA) 模式下运行，则电子邮件保护功能中的预授权 SQL 注入漏洞可能导致远程代码执行。
* CVE-2024-12728 (CVSS 得分：9.8) – 由於高可用性（HA）叢集初始化的建議和非隨機 SSH 登錄密碼，即使在 HA 建立過程完成後仍保持有效，因而產生弱憑證漏洞。
* CVE-2024-12729（CVSS 得分：8.8）- 用户门户中的验证后代码注入漏洞，允许通过验证的用户远程执行代码。

该安全厂商表示，CVE-2024-12727 会影响约 0.05% 的设备，而 CVE-2024-12728 则会影响约 0.5% 的设备。所有三个发现的漏洞都会影响 Sophos Firewall 21.0 GA (21.0.0) 及更早版本。以下版本已对该漏洞进行了修复

* **CVE-2024-12727** – v21 MR1 及更新版本（针对 v21 GA、v20 GA、v20 MR1、v20 MR2、v20 MR3、v19.5 MR3、v19.5 MR4、v19.0 MR2 的热修复程序）
* **CVE-2024-12728** – v20 MR3、v21 MR1 和更新版本（适用于 v21 GA、v20 GA、v20 MR1、v19.5 GA、v19.5 MR1、v19.5 MR2、v19.5 MR3、v19.5 MR4、v19.0 MR2 和 v20 MR2 的热修复程序）
* **CVE-2024-12729** – v21 MR1 及更新版本（适用于 v21 GA、v20 GA、v20 MR1、v20 MR2、v19.5 GA、v19.5 MR1、v19.5 MR2、v19.5 MR3、v19.5 MR4、v19.0 MR2、v19.0 MR3 的热修复程序）

为确保已应用热修补程序，建议用户按照以下步骤操作

* **CVE-2024-12727** – 从 Sophos Firewall 控制台启动 Device Management > Advanced Shell，然后运行命令 “cat /conf/nest\_hotfix\_status”（如果值为 320 或以上，则已应用热修复程序）。
* **CVE-2024-12728** 和 **CVE-2024-12729** – 从 Sophos Firewall 控制台启动设备控制台，并运行命令 “system diagnostic show version-info”（如果值为 HF120424.1 或更高版本，则会应用热修复程序）

作为补丁应用前的临时解决方法，Sophos 建议客户将 SSH 访问限制为仅访问物理上独立的专用 HA 链接，和/或使用足够长且随机的自定义口令重新配置 HA。

用户可以采取的另一项安全措施是禁止通过 SSH 访问广域网，并确保用户门户和 Webadmin 不暴露于广域网。

就在一周前，美国政府公布了对中国公民关天峰的指控，他涉嫌利用零日安全漏洞（CVE-2020-12271，CVSS 得分：9.8）入侵全球约 81,000 台 Sophos 防火墙。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/sophos-fixes-3-critical-firewall-flaws.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302935](/post/id/302935)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/sophos-fixes-3-critical-firewall-flaws.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/sophos-fixes-3-critical-firewall-flaws.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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