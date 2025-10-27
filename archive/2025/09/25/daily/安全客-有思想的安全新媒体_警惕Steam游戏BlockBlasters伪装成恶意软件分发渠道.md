---
title: 警惕Steam游戏BlockBlasters伪装成恶意软件分发渠道
url: https://www.anquanke.com/post/id/312391
source: 安全客-有思想的安全新媒体
date: 2025-09-25
fetch_date: 2025-10-02T20:37:59.505083
---

# 警惕Steam游戏BlockBlasters伪装成恶意软件分发渠道

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

# 警惕Steam游戏BlockBlasters伪装成恶意软件分发渠道

阅读量**100410**

发布时间 : 2025-09-24 16:39:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/blockblasters-when-a-steam-game-turns-into-a-malware-delivery-vehicle/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款前景光明的独立平台游戏，演变为2025年Steam平台上最令人警惕的恶意软件植入游戏案例之一。据G DATA安全实验室报告，2D射击游戏《BlockBlasters》于2025年8月30日发布的一个补丁（Build 19799326）中植入了恶意文件，这些文件能够窃取凭证、浏览器数据，甚至**加密货币钱包信息**。

《BlockBlasters》于2025年7月31日上线，获得了积极评价并积累了一定数量的玩家基础。但仅仅一个月后，该更新开始从毫无防备的用户那里**窃取敏感数据**。

正如报告所解释的：“当用户玩游戏时，游戏运行所在的电脑中的各种信息会被窃取——包括加密货币钱包数据。数百名用户可能已受到影响。”

这一事件与Steam平台上恶意软件隐藏在游戏中的**上升趋势**相呼应，此前的案例包括PirateFi和Chemia，攻击者在这些案例中向抢先体验版或免费游戏中注入恶意二进制文件。

感染链始于一个名为**game2.bat 的可疑批处理文件**，它执行了几个对于合法游戏进程来说不常见的恶意功能：

1. 通过ipinfo[.]io和ip[.]me收集IP和地理位置信息；
2. 检测防病毒软件进程；
3. 窃取Steam登录详细信息，包括SteamID、AccountName和PersonaName；
4. 将窃取的数据上传至C2服务器hxxp://203[.]188[.]171[.]156:30815/upload；
5. 执行隐藏的VBS启动脚本（launch1.vbs 和test.vbs ）。

然后，该脚本会在**仅Windows Defender处于活动状态时**解压受密码保护的压缩包（v1.zip ）——这是一种旨在绕过检测的规避技巧。

VBS脚本充当加载器，**静默运行额外的批处理文件**（1.bat 和test.bat ）。

test.bat 脚本会收集浏览器扩展和加密货币钱包信息，并将数据泄露至攻击者的C2服务器。

主批处理文件1.bat 会采取额外步骤**禁用保护机制**：“它将v3.zip 压缩包中可执行文件的目标文件夹添加到Microsoft Defender Antivirus的排除列表中。这将使安全扫描和行为检查时忽略该目标文件夹。”

随后部署两个关键载荷：

1. **Client-built2.exe** ——一个基于Python的后门程序，连接回同一个C2服务器；
2. **Block1.exe** ——一个StealC恶意软件变体，能够从Chrome、Brave和Edge浏览器中提取存储的数据。

G DATA观察到：“此StealC恶意软件使用RC4加密（多年前已被弃用）来隐藏其API和关键字符串……它连接到另一个C2通道hxxp://45[.]83[.]28[.]99。”

遥测数据显示，自受感染的补丁部署以来，《BlockBlasters》的下载量超过100次，发现问题后仅剩少数活跃玩家。

然而，**人力成本更为令人警醒**。据vx-underground报道，在一场为癌症治疗举办的慈善直播中，一名主播的系统在直播过程中被实时感染。

《BlockBlasters》案例凸显了一个关键的安全挑战：游戏玩家现在在娱乐平台上面临**供应链式威胁**。随着恶意软件通过Valve的初始安全筛查，玩家对合法游戏更新的信任正被利用。

正如G DATA所总结的，《BlockBlasters》从Steam下架对那些已被感染的用户来说为时已晚——但这鲜明地提醒我们，恶意软件不再局限于可疑下载渠道；它正在渗透到主流平台。

本文翻译自securityonline [原文链接](https://securityonline.info/blockblasters-when-a-steam-game-turns-into-a-malware-delivery-vehicle/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312391](/post/id/312391)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/blockblasters-when-a-steam-game-turns-into-a-malware-delivery-vehicle/)

如若转载,请注明出处： <https://securityonline.info/blockblasters-when-a-steam-game-turns-into-a-malware-delivery-vehicle/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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