---
title: 新 StrelaStealer 网络钓鱼攻击袭击了欧盟和美国的 100 多个组织
url: https://www.anquanke.com/post/id/294278
source: 安全客-有思想的安全新媒体
date: 2024-03-26
fetch_date: 2025-10-04T12:11:27.292663
---

# 新 StrelaStealer 网络钓鱼攻击袭击了欧盟和美国的 100 多个组织

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

# 新 StrelaStealer 网络钓鱼攻击袭击了欧盟和美国的 100 多个组织

阅读量**84514**

发布时间 : 2024-03-25 10:14:38

**x**

##### 译文声明

本文是翻译文章，文章来源：https://thehackernews.com/2024/03/new-strelastealer-phishing-attacks-hit.html

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了新一波网络钓鱼攻击，其目的是提供一种不断发展的信息窃取程序（称为StrelaStealer）。

Palo Alto Networks Unit 42 研究人员在发布的一份新报告中表示，这些活动影响了欧盟和美国的 100 多个组织。

研究人员 Benjamin Chang、Goutam Tripathy、Pranay Kumar Chhaparwal、Anmol Maurya 和 Vishwa Thothathri表示：“这些活动以带有附件的垃圾邮件形式出现，最终启动 StrelaStealer 的 DLL 负载。 ”

“为了逃避检测，攻击者将初始电子邮件附件文件格式从一个活动更改为下一个活动，以防止通过先前生成的签名或模式进行检测。”

StrelaStealer 于 2022 年 11 月首次披露，它能够从知名电子邮件客户端窃取电子邮件登录数据，并将其传输到攻击者控制的服务器。

此后，分别于 2023 年 11 月和 2024 年 1 月检测到两起涉及该恶意软件的大规模活动，针对欧盟和美国的高科技、金融、专业和法律、制造、政府、能源、保险和建筑行业

这些攻击还旨在提供一种新的窃取程序变体，该变体包含更好的混淆和反分析技术，同时通过带有 ZIP 附件的发票主题电子邮件进行传播，这标志着 ISO 文件的转变。

ZIP 存档中存在一个 JavaScript 文件，该文件会释放一个批处理文件，该批处理文件又会使用rundll32.exe（负责运行 32 位动态链接库的合法 Windows 组件）启动窃取程序 DLL 有效负载。

窃取者恶意软件还依赖于一系列混淆技巧，使沙盒环境中的分析变得困难。

研究人员表示：“随着每一波新的电子邮件活动，威胁行为者都会更新启动感染链的电子邮件附件和 DLL 负载本身。”

博通旗下的赛门铁克透露，在 GitHub、Mega 或 Dropbox 上托管的知名应用程序或破解软件的虚假安装程序正在充当名为 Stealc 的窃取恶意软件的渠道。

据 ESET观察，网络钓鱼活动还传播Revenge RAT和Remcos RAT（又名 Rescoms），后者通过名为AceCryptor的加密货币即服务 (CaaS) 进行传播。

![StrelaStealer 网络钓鱼攻击]()

该网络安全公司援引遥测数据表示：“在 [2023] 下半年，Rescoms 成为 AceCryptor 打包的最流行的恶意软件家族。” “其中一半以上的尝试发生在波兰，其次是塞尔维亚、西班牙、保加利亚和斯洛伐克。”

2023 年下半年，AceCryptor 中打包的其他著名现成恶意软件包括 SmokeLoader、STOP 勒索软件、RanumBot、Vidar、RedLine、Tofsee、Fareit、Pitou 和 Stealc。值得注意的是，许多恶意软件菌株也通过PrivateLoader传播。

Secureworks 观察到的另一个社会工程骗局被发现是针对在搜索引擎上寻找最近​​去世的个人信息的个人，在虚假网站上托管虚假讣告，通过搜索引擎优化 (SEO) 中毒增加网站流量，最终推送广告软件和其他不需要的程序。

该公司表示：“这些网站的访问者会被重定向到电子约会或成人娱乐网站，或者立即看到验证码提示，点击后会安装网络推送通知或弹出广告。 ”

“这些通知显示来自 McAfee 和 Windows Defender 等知名防病毒应用程序的虚假病毒警报警告，即使受害者单击其中一个按钮，它们也会持续存在于浏览器中。”

“这些按钮链接到基于订阅的防病毒软件程序的合法登陆页面，超链接中嵌入的附属 ID 会奖励威胁行为者的新订阅或续订。”

虽然假冒活动目前仅限于通过防病毒软件的附属程序来充实欺诈者的金库，但攻击链可以轻松地改变用途，以传播信息窃取程序和其他恶意程序，从而使其成为更强大的威胁。

在此开发之前，还发现了一个名为Fluffy Wolf 的新活动集群，该集群利用包含可执行附件的网络钓鱼电子邮件来传播多种威胁，例如MetaStealer、Warzone RAT、XMRig miner 和名为 Remote Utilities 的合法远程桌面工具。

该活动表明，即使是不熟练的威胁行为者也可以利用恶意软件即服务 (MaaS) 计划成功进行大规模攻击并掠夺敏感信息，然后可以进一步将其货币化以获取利润。

BI.ZONE表示：“尽管这些威胁行为者的技术水平平庸，但他们仅使用两套工具即可实现其目标：合法的远程访问服务和廉价的恶意软件。”

本文翻译自https://thehackernews.com/2024/03/new-strelastealer-phishing-attacks-hit.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294278](/post/id/294278)

安全KER - 有思想的安全新媒体

本文转载自: https://thehackernews.com/2024/03/new-strelastealer-phishing-attacks-hit.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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