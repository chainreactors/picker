---
title: DoNot APT扩展至欧洲：通过Google Drive钓鱼攻击外务部，传播LoptikMod恶意软件
url: https://www.anquanke.com/post/id/309905
source: 安全客-有思想的安全新媒体
date: 2025-07-12
fetch_date: 2025-10-06T23:16:35.694834
---

# DoNot APT扩展至欧洲：通过Google Drive钓鱼攻击外务部，传播LoptikMod恶意软件

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

# DoNot APT扩展至欧洲：通过Google Drive钓鱼攻击外务部，传播LoptikMod恶意软件

阅读量**73694**

发布时间 : 2025-07-11 16:13:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/donot-apt-expands-to-europe-targets-foreign-ministry-with-loptikmod-malware-via-google-drive-phishing/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在一项新揭露的攻击行动中，DoNot APT组织——也被追踪为APT-C-35、Mint Tempest、Origami Elephant和Viceroy Tiger——升级了其间谍活动，这次目标是一个欧洲外交事务部。该行动结合了精准钓鱼、隐蔽恶意软件和基于云的传递方式，展示了该组织不断发展的技术手段和对欧洲外交事务日益增长的兴趣。

Trellix的报告指出：“DoNot APT组织是一种持续的网络间谍威胁，自2016年起活跃，通常针对南亚地区的实体，但现在‘已扩展至欧洲外交通讯和情报’。”

此次活动的开始是通过一封伪装成国防官员的精准钓鱼邮件，邮件中提到一个听起来合法的事件：“意大利国防武官访问孟加拉国达卡”。邮件中包含一个指向恶意RAR压缩包（名为SyClrLtr.rar）的Google Drive链接，Trellix表示，这一手段凸显了该组织“在使用常见云服务进行初步感染方面的适应能力”。

一旦打开，该压缩包内含一个伪装成PDF文件的可执行文件（notflog.exe）。当执行时，该文件启动一个多阶段感染链，部署一个批处理脚本（djkggosj.bat），并通过名为PerformTaskMaintain的计划任务建立持久性。

通过远程监控，Trellix将该恶意软件与LoptikMod后门相关联，这是自2018年以来DoNot APT专门使用的后门。该可执行文件的字符串中揭示了“Loptik”等标记，并且故意进行了代码混淆，使静态分析变得困难。Trellix在报告中提到：

“恶意软件中嵌入的二进制字符串用于在运行时解码或恢复其他有意义的字符串…这种技术是一种混淆形式，用于阻止静态分析。”

动态API加载、简化的导入表以及反虚拟机逃避技巧进一步加强了该组织试图逃避检测并阻挠分析师的努力。

该恶意软件创建了一个互斥体08808，以确保只有一个实例在运行，并通过计划任务建立持久性。感染后，它悄悄地放置了一个名为socker.dll的DLL负载和另一个批处理文件（sfs.bat），该文件配置了名为MicorsoftVelocity的第二个任务。这个链条确保了长期访问和在受害者系统上执行命令。

该恶意软件收集了敏感的系统元数据，包括：

* CPU型号
* 操作系统版本和构建号
* 用户名和主机名
* 已安装的应用程序

这些数据经过AES和Base64编码后，通过HTTPS POST请求发送到一个命令控制（C2）域名：https://totalservices[.]info/WxporesjaTexopManor/ptomekasresdkolerts

尽管在分析时C2域名处于非活动状态，Trellix强调，该基础设施模拟了合法服务域名，可能是为了避免基于DNS的检测。

Trellix根据基础设施、工具集和TTPs将此次活动与DoNot APT联系在一起。尽管该组织之前主要集中在南亚地区，但现在显然已扩展到欧洲领域，符合更广泛的地缘政治情报目标。

报告总结道：“这些行动突显了DoNot APT持续且不断扩展的努力，旨在收集敏感的政治、军事和经济信息。”

本文翻译自securityonline [原文链接](https://securityonline.info/donot-apt-expands-to-europe-targets-foreign-ministry-with-loptikmod-malware-via-google-drive-phishing/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309905](/post/id/309905)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/donot-apt-expands-to-europe-targets-foreign-ministry-with-loptikmod-malware-via-google-drive-phishing/)

如若转载,请注明出处： <https://securityonline.info/donot-apt-expands-to-europe-targets-foreign-ministry-with-loptikmod-malware-via-google-drive-phishing/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

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