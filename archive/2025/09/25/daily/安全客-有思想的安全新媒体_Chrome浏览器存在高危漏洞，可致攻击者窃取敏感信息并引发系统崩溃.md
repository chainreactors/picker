---
title: Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃
url: https://www.anquanke.com/post/id/312366
source: 安全客-有思想的安全新媒体
date: 2025-09-25
fetch_date: 2025-10-02T20:37:57.773779
---

# Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃

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

# Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃

阅读量**99095**

发布时间 : 2025-09-24 16:42:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/chrome-high-severity-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌已针对其Chrome浏览器发布紧急安全更新，修复三个**高危漏洞**，这些漏洞可能允许攻击者访问敏感信息或导致系统崩溃。

公司建议用户**立即更新浏览器**，以降低与这些漏洞相关的潜在风险。

最新补丁将Windows和Mac版Chrome稳定通道版本升级至**140.0.7339.207/.208**，Linux版升级至**140.0.7339.207**。更新将在未来几天至几周内自动推送，但用户可手动触发更新以立即获得保护。

三个高危漏洞均存在于**V8 JavaScript和WebAssembly引擎**中——这是Chrome的核心组件，负责执行程序代码。

1. **CVE-2025-10890**：**侧信道信息泄露漏洞**。外部安全研究员Mate Marjanović报告了此漏洞。攻击者可诱使用户访问恶意网站，利用该漏洞读取浏览器内存中的敏感数据，绕过旨在隔离信息的安全措施。
2. **CVE-2025-10891和CVE-2025-10892**：均为V8引擎中的**整数溢出漏洞**，由谷歌Big Sleep研究团队内部发现。整数溢出是一种常见软件缺陷，当数值超出内存分配空间时会“回绕”，导致意外行为。

### **攻击者可能的利用方式**

成功利用这些漏洞通常需要攻击者诱骗受害者访问**特制的恶意网页**：

1. 对于CVE-2025-10890，页面中的恶意代码可触发侧信道漏洞，使攻击者推断用户设备上其他网站或进程的数据。
2. 两个整数溢出漏洞若被利用，可能导致浏览器突然崩溃。尽管谷歌公告未明确确认，但整数溢出有时可与其他漏洞链结合，实现对受影响系统的完全控制，因此威胁严重。

### **谷歌的应对措施与用户建议**

根据标准安全政策，谷歌目前限制公开这些漏洞的技术细节和利用证明（PoC），以防止大规模攻击，待更新广泛部署后再解除限制。

谷歌强烈建议所有Chrome用户确保浏览器更新至最新版本。检查和安装更新的步骤：

1. 打开Chrome菜单，选择“帮助”；
2. 点击“关于Google Chrome”；
3. 浏览器将自动扫描最新版本，并提示重启以完成安装。

谷歌还对发现和报告这些漏洞的安全研究员表示感谢，强调维护浏览器安全需要协作努力。公司指出，许多安全漏洞通过AddressSanitizer、MemorySanitizer等高级测试工具和各种模糊测试库检测，从而在漏洞进入稳定通道前修复。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/chrome-high-severity-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312366](/post/id/312366)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/chrome-high-severity-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/chrome-high-severity-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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