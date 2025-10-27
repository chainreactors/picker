---
title: 新型恶意广告活动利用GitHub仓库分发恶意软件
url: https://www.anquanke.com/post/id/312146
source: 安全客-有思想的安全新媒体
date: 2025-09-16
fetch_date: 2025-10-02T20:11:18.245718
---

# 新型恶意广告活动利用GitHub仓库分发恶意软件

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

# 新型恶意广告活动利用GitHub仓库分发恶意软件

阅读量**48000**

发布时间 : 2025-09-15 18:22:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-malvertising-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期出现一起复杂的恶意广告活动，攻击者通过**悬挂提交（dangling commits）** 滥用GitHub仓库，借助伪造的GitHub Desktop客户端分发恶意软件。这种新型攻击向量标志着网络犯罪战术的显著进化——利用GitHub平台的**信任度与合法性**，诱骗无防备用户下载恶意软件。

### **攻击流程：伪装仓库与诱导下载**

该活动通过推广**遭入侵的GitHub仓库**（含悬挂提交）作为恶意载荷分发载体。当用户通过被篡改的广告搜索“GitHub Desktop”时，会被重定向至**外观合法的恶意仓库**，其代码结构中隐藏了恶意软件。攻击核心在于利用用户对GitHub界面的熟悉度及对平台安全性的信任，降低警惕性。

### **感染后行为：持久化与隐蔽通信**

成功入侵后，恶意软件会在受害者系统中**建立持久化机制**，同时通过隐蔽的命令与控制（C2）服务器通道保持通信，为后续数据窃取或进一步攻击做准备。

![]()

Unit 42研究人员通过可疑GitHub仓库活动的行为分析及与伪造GitHub Desktop安装程序相关的异常下载模式，识别出了该活动。\*\*

### **高级感染机制与载荷执行**

恶意软件采用复杂的**多阶段感染流程**，始于用户下载看似合法的GitHub Desktop安装程序。

初始载荷会执行**全面的系统探测**，收集受感染机器的详细信息，包括操作系统详情、已安装软件和网络配置。这些侦察数据会立即被窃取至攻击者控制的服务器，随后进入下一感染阶段。

该活动在基于系统特征的**条件性载荷部署**方面展现出极高复杂性：

1. 基于PowerShell的载荷从命令与控制基础设施下载NetSupport远程访问木马（RAT）；
2. 可执行文件变体部署带有COM文件扩展名的AutoIT解释器以逃避检测。

恶意软件通过**注册表实现持久化**，并利用MSBuild.exe 、RegAsm.exe 等**合法系统工具**进行数据窃取，将恶意活动与正常系统操作深度融合。

其检测规避技术包括：启用浏览器远程调试功能、设置Windows Defender排除路径、借助可信系统进程执行载荷，导致传统安全解决方案难以有效抵御这一复杂威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-malvertising-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312146](/post/id/312146)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-malvertising-campaign/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-malvertising-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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