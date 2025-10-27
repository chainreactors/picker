---
title: Buterat后门攻击企业以建立持久化控制端点
url: https://www.anquanke.com/post/id/312152
source: 安全客-有思想的安全新媒体
date: 2025-09-16
fetch_date: 2025-10-02T20:11:18.616522
---

# Buterat后门攻击企业以建立持久化控制端点

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

# Buterat后门攻击企业以建立持久化控制端点

阅读量**47655**

发布时间 : 2025-09-15 18:21:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/buterat-backdoor-attacking-enterprises/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

名为Backdoor.WIN32.Buterat的复杂后门恶意软件已成为企业网络的重大威胁，其具备**高级持久化技术与隐身能力**，使攻击者能对受感染系统维持长期未授权访问。该恶意软件通过精心策划的**钓鱼邮件、恶意附件及植入木马的软件下载**，针对政府与企业环境发起攻击。与专注于即时破坏或数据窃取的传统恶意软件不同，Buterat优先追求**长期潜伏与隐蔽操作**，通过加密通信通道与远程命令控制（C2）服务器建立连接，执行任意命令、部署额外载荷并横向移动，同时规避传统检测机制。

### **技术细节：线程劫持与持久化机制**

Point Wild研究人员通过SHA-256哈希值f50ec4cf0d0472a3e40ff8b9d713fb0995e648ecedf15082a88b6e6f1789cdab识别出该样本，发现其采用**Borland Delphi编译**并结合复杂混淆技术。恶意软件伪装成合法系统进程，通过**修改注册表键值**实现系统重启后持久化。

![]()

#### **高级线程操纵与注入技术**

Buterat的核心威胁在于**线程劫持技术**：利用混淆的API调用（如SetThreadContext和ResumeThread），在不创建新进程或修改入口点的情况下精确控制线程执行。攻击者通过SetThreadContext修改线程上下文，注入恶意代码至合法进程，再通过ResumeThread激活被篡改的线程——这一过程**无新进程创建记录**，大幅降低行为分析系统的检测概率。

感染期间，Buterat在用户目录释放amhost.exe 、bmhost.exe 、cmhost.exe 等多个可执行文件，建立**多持久化点**，并尝试连接C2服务器http://ginomp3.mooo.com/ ，实现数据窃取与远程控制。

### **防御建议**

安全团队需监控上述**IOC（入侵指标）**，实施网络级阻断以阻止与恶意基础设施的通信，并加强对线程异常行为、注册表篡改及可疑进程注入的检测。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/buterat-backdoor-attacking-enterprises/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312152](/post/id/312152)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/buterat-backdoor-attacking-enterprises/)

如若转载,请注明出处： <https://cybersecuritynews.com/buterat-backdoor-attacking-enterprises/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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