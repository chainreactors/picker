---
title: 黑客利用 GitHub 上的破解软件传播 RisePro 信息窃取程序
url: https://www.anquanke.com/post/id/294028
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:50.800090
---

# 黑客利用 GitHub 上的破解软件传播 RisePro 信息窃取程序

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

# 黑客利用 GitHub 上的破解软件传播 RisePro 信息窃取程序

阅读量**72684**

发布时间 : 2024-03-18 10:36:38

**x**

##### 译文声明

本文是翻译文章，文章来源：https://thehackernews.com/2024/03/hackers-using-cracked-software-on.html

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现许多 GitHub 存储库提供破解软件，这些软件用于传播名为 RisePro 的信息窃取程序。

据 G DATA 称，该活动代号为gitgub ，包括与 11 个不同账户相关的 17 个存储库。此后，相关存储库已被微软旗下子公司删除。

这家德国网络安全公司表示：“这些存储库看起来很相似，都有一个 README.md 文件，并承诺提供免费破解软件。 ”

“Github 上通常使用绿色和红色圆圈来显示自动构建的状态。Gitgub 威胁参与者在他们的 README.md 中添加了四个绿色 Unicode 圆圈，假装在当前日期旁边显示状态，并提供合法性和新近度的感觉。 ”

网络安全
存储库列表如下，每个存储库都指向一个包含 RAR 存档文件的下载链接（“digitalxnetwork[.]com”） –

andreastanaj/AVAST
andreastanaj/声音助推器
aymenkort1990/fabfilter
BenWebsite/-IObit-Smart-Defrag-破解
Faharnaqvi/VueScan-破解
javisolis123/Voicemod
lolusuary/傲梅备份
lolusuary/守护进程工具
lolusuary/EaseUS-分区大师
lolusuary/SOOTHE-2
mostofakamaljoy/ccleaner
rik0v/ManyCam
Roccinhu/Tenorshare-Reiboot
Roccinhu/Tenorshare-iCareFone
True-Oblivion/傲梅-分区助手
vaibhavshiledar/droidkit
vaibhavshiledar/TOON-BOOM-HARMONY
RAR 存档要求受害者提供存储库 README.md 文件中提到的密码，其中包含一个安装程序文件，该文件解压下一阶段的有效负载，这是一个膨胀到 699 MB 的可执行文件，旨在使分析工具崩溃，例如IDA 专业版。

该文件的实际内容（总计仅为 3.43 MB）充当加载程序，将 RisePro（版本 1.6）注入 AppLaunch.exe 或 RegAsm.exe 中。

RisePro 在 2022 年底突然成为人们关注的焦点，当时它使用名为 PrivateLoader 的按安装付费 (PPI) 恶意软件下载服务进行分发。

网络安全
它用 C++ 编写，旨在从受感染的主机收集敏感信息并将其渗透到两个 Telegram 通道，威胁行为者经常使用这两个通道来提取受害者的数据。有趣的是，Checkmarx 最近的研究表明，可以渗透攻击者的机器人并将消息转发到另一个 Telegram 帐户。

Splunk 详细介绍了Snake Keylogger采用的策略和技术，将其描述为一种窃取恶意软件，“采用多方面的方法进行数据泄露”。

“FTP 的使用有助于文件的安全传输，而 SMTP 则可以发送包含敏感信息的电子邮件，”Splunk说。“此外，与 Telegram 的集成提供了一个实时通信平台，可以立即传输被盗数据。”

窃取者恶意软件变得越来越流行，常常成为勒索软件和其他高影响力数据泄露的主要载体。根据 Specops 本周发布的一份报告，RedLine、Vidar 和 Raccoon 已成为使用最广泛的窃取者，仅 RedLine 在过去六个月中就窃取了超过 1.703 亿个密码。

本文翻译自https://thehackernews.com/2024/03/hackers-using-cracked-software-on.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294028](/post/id/294028)

安全KER - 有思想的安全新媒体

本文转载自: https://thehackernews.com/2024/03/hackers-using-cracked-software-on.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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