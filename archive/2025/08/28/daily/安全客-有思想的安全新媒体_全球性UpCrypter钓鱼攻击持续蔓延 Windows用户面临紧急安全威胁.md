---
title: 全球性UpCrypter钓鱼攻击持续蔓延 Windows用户面临紧急安全威胁
url: https://www.anquanke.com/post/id/311523
source: 安全客-有思想的安全新媒体
date: 2025-08-28
fetch_date: 2025-10-07T00:18:25.450219
---

# 全球性UpCrypter钓鱼攻击持续蔓延 Windows用户面临紧急安全威胁

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

# 全球性UpCrypter钓鱼攻击持续蔓延 Windows用户面临紧急安全威胁

阅读量**69611**

发布时间 : 2025-08-27 17:50:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Aminu Abdullahi，文章来源：techrepublic

原文地址：<https://www.techrepublic.com/article/news-upcrypter-phishing-microsoft-windows/>

译文仅供参考，具体内容表达以及含义原文为准。

###

![]()

网络安全研究人员发现针对Windows设备的钓鱼邮件数量激增。据Fortinet旗下FortiGuard实验室监测，黑客正在利用UpCrypter加载器展开攻击活动，该工具可安装多种远程访问工具（RAT），使攻击者能长期维持对受感染机器的控制。

这些钓鱼邮件伪装成未接语音邮件或采购订单。点击附件的受害者将被重定向至精心设计的虚假网站，这些网站通常使用企业标识增强可信度。Fortinet表示，这些钓鱼页面会诱导用户下载包含高度伪装JavaScript投放器的ZIP压缩包。一旦打开，脚本将在后台触发PowerShell命令，连接攻击者控制的服务器进行下一阶段攻击。

FortiGuard实验室研究员Cara Lin指出：”这些页面专门诱骗收件人下载作为UpCrypter投放器的JavaScript文件，构成精密攻击链的初始环节。”

### **UpCrypter攻击链深度解析：反检测机制与三重远程控制工具协同作案**

安全研究人员揭示了UpCrypter在攻击链中的精密运作机制。一旦执行，该加载器会立即**扫描系统环境**，检测是否处于沙箱分析或取证调查中。若发现监控迹象，将立即触发重启中断调查。

当确认环境安全后，恶意软件开始下载并执行后续载荷。攻击者采用**隐写术**将文件隐藏于普通图片中，有效规避杀毒软件检测。最终部署的恶意工具包括：

1. **PureHVNC**：实现隐藏式远程桌面访问；
2. **DCRat（DarkCrystal RAT）**：具备间谍功能和数据窃取能力的多用途工具；
3. **Babylon RAT**：支持攻击者对设备进行全面控制。

### **全球攻击态势与行业影响**

Fortinet研究人员指出，攻击者采用多重技术伪装恶意代码：包括**字符串混淆**、通过**注册表修改实现持久化**、以及**内存运行代码**避免磁盘留痕等手法，形成高度隐匿的攻击体系。

此次网络钓鱼活动自2025年8月初持续活跃，已呈现国际化传播趋势。监测数据显示**奥地利、加拿大、埃及**等地攻击活动最为密集。

受冲击最严重的行业包括：**制造业、****科技行业、****医疗机构、****建筑行业、****零售与酒店业，**Fortinet研究人员指出，短短两周内检测到的攻击数量**实现翻倍增长**，印证了该攻击行动的快速扩张态势。此次攻击不仅窃取用户名和密码，更通过**多阶段恶意软件链**实现在企业系统中长期隐蔽驻留。

正如Fortinet所强调：”用户和组织应高度重视此威胁，采用强化邮件过滤器，并确保员工接受过识别和规避此类攻击的培训。”

本文翻译自techrepublic [原文链接](https://www.techrepublic.com/article/news-upcrypter-phishing-microsoft-windows/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311523](/post/id/311523)

安全KER - 有思想的安全新媒体

本文转载自: [techrepublic](https://www.techrepublic.com/article/news-upcrypter-phishing-microsoft-windows/)

如若转载,请注明出处： <https://www.techrepublic.com/article/news-upcrypter-phishing-microsoft-windows/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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