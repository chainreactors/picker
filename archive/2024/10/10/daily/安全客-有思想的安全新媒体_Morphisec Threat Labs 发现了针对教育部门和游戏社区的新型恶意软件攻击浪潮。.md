---
title: Morphisec Threat Labs 发现了针对教育部门和游戏社区的新型恶意软件攻击浪潮。
url: https://www.anquanke.com/post/id/300636
source: 安全客-有思想的安全新媒体
date: 2024-10-10
fetch_date: 2025-10-06T18:51:54.286444
---

# Morphisec Threat Labs 发现了针对教育部门和游戏社区的新型恶意软件攻击浪潮。

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

# Morphisec Threat Labs 发现了针对教育部门和游戏社区的新型恶意软件攻击浪潮。

阅读量**56745**

发布时间 : 2024-10-09 10:48:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/global-malware-campaign-exploits-lua-in-gaming-and-education-sectors/>

译文仅供参考，具体内容表达以及含义原文为准。

Morphisec威胁实验室发现了一波新的恶意软件攻击，目标是教育部门和游戏社区。安全研究人员Shmuel Uzan表示，这些复杂的恶意软件变种利用Lua（游戏开发中广泛使用的脚本语言）通过GitHub等平台渗透系统。该运动已在全球范围内展开，北美洲、南美洲、欧洲、亚洲和澳大利亚均报告有感染病例。

![Lua Malware]()

这种恶意软件的兴起可以归因于它利用了Lua的流行，尤其是在使用Roblox等游戏引擎的学生游戏玩家中。据报道，“搜索游戏作弊的用户最后往往会从GitHub等平台或类似来源下载文件。”攻击者利用这些寻求作弊的用户，在看似无害的下载中嵌入恶意Lua脚本。

恶意软件通常通过ZIP存档传递，其中包含多个组件，包括Lua编译器、Lua DLL文件、模糊的Lua脚本和批处理文件。这些组件一旦安装在受害者的机器上，就会一起执行恶意操作。执行后，Lua脚本与命令与控制（C2）服务器建立通信，发送有关受感染系统的详细信息。

一旦恶意软件处于活动状态，C2服务器将向受感染的计算机提供指令，这些指令分为两种类型的任务:Lua加载任务和任务有效载荷。Lua加载任务保持持久性和隐藏进程，而任务有效载荷则专注于下载其他恶意软件有效载荷或应用新配置。报告解释说，“Lua加载器任务涉及维持持久性或隐藏进程等操作”，而有效载荷的设计目的是扩展恶意软件的能力。

为了逃避检测，Lua脚本使用Prometheus Obfuscator进行了模糊处理，这是一种旨在保护底层代码不受逆向工程影响的工具。这种程度的混淆使得安全研究人员很难分析和理解恶意软件的全部功能。乌赞在报告中指出:“使用普罗米修斯混淆器对脚本进行混淆……使得研究人员分析和理解代码变得更加困难。”

为了阻止研究人员反转或重新格式化代码，该恶意软件采用了一种独特的反反转技术，当试图美化模糊代码时，该技术会触发错误消息。混淆器的功能包括通过检查执行过程中生成的错误消息的行数来检测代码是否被篡改。如果代码已被更改，恶意软件终止，显示一条消息:“检测到篡改！”

![]()

除了混淆之外，该恶意软件还利用Lua的ffi（外部函数接口）库直接执行C代码。这种技术允许攻击者调用C函数和使用C数据结构，而不需要编写C包装代码。Lua和C之间的这种集成增强了恶意软件操纵系统级进程和执行更高级攻击的能力。

恶意软件一旦渗入受害者的系统，就会通过创建计划任务和生成随机任务名称来建立持久性。该恶意软件还收集受害者计算机的大量信息，包括用户的GUID、计算机名称、操作系统和网络详细信息。它甚至捕获受损系统的屏幕截图，并将这些数据发送到攻击者的C2服务器。

报告强调，“脚本检索 MachineGuid…并把从计算机收集的数据和截图发送给对手C2。”此级别的数据收集使攻击者能够全面了解受影响的计算机，从而更有效地定制后续攻击。

一旦恶意软件成功收集到所需的数据，C2服务器就会以封锁消息或JSON响应做出响应，该响应将为执行任务或下载额外有效载荷提供进一步的指示。如果服务器响应被阻止，恶意软件会尝试从备份位置（如pastebin.com）检索新地址，确保与攻击者继续通信。

这种恶意软件提供的有效载荷包括Redline Infostealers，这是一种用来从受害者那里获取凭据和敏感信息的恶意软件。报告指出，Redline因其窃取宝贵数据的能力，在网络犯罪领域获得了突出地位，这些数据后来在暗网上出售。乌赞警告说:“从这些攻击中获取的证件被卖给更复杂的组织，用于攻击的后期阶段。”

本文翻译自securityonline [原文链接](https://securityonline.info/global-malware-campaign-exploits-lua-in-gaming-and-education-sectors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300636](/post/id/300636)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/global-malware-campaign-exploits-lua-in-gaming-and-education-sectors/)

如若转载,请注明出处： <https://securityonline.info/global-malware-campaign-exploits-lua-in-gaming-and-education-sectors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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