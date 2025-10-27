---
title: 新型 Ymir 勒索软件利用内存进行隐蔽攻击；目标是企业网络
url: https://www.anquanke.com/post/id/302368
source: 安全客-有思想的安全新媒体
date: 2024-12-04
fetch_date: 2025-10-06T19:37:28.224324
---

# 新型 Ymir 勒索软件利用内存进行隐蔽攻击；目标是企业网络

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

# 新型 Ymir 勒索软件利用内存进行隐蔽攻击；目标是企业网络

阅读量**54879**

发布时间 : 2024-12-03 10:49:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/new-ymir-ransomware-exploits-memory-for.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一个名为 “Ymir ”的新勒索软件家族，该家族在系统被名为 “RustyStealer ”的窃取恶意软件入侵两天后的一次攻击中被部署。

俄罗斯网络安全厂商卡巴斯基表示：“Ymir勒索软件引入了技术特征和战术的独特组合，增强了其有效性。”

“威胁者利用内存管理函数（malloc、memmove 和 memcmp）的非常规组合，直接在内存中执行恶意代码。这种方法偏离了常见勒索软件类型中的典型顺序执行流程，增强了其隐蔽能力。”

卡巴斯基表示，它观察到该勒索软件在针对哥伦比亚一家未具名组织的网络攻击中使用，威胁者此前曾发布RustyStealer恶意软件来收集企业凭证。

据信，窃取的凭证被用于未经授权访问该公司的网络，以便部署勒索软件。虽然初始访问代理和勒索软件制作者之间通常存在交接，但目前还不清楚情况是否如此。

卡巴斯基研究员克里斯蒂安-索萨（Cristian Souza）说：“如果经纪人确实是部署勒索软件的同伙，这可能预示着一种新趋势，即在不依赖传统勒索软件即服务（RaaS）团队的情况下，创造出更多劫持选择。”

这次攻击的显著特点是安装了 Advanced IP Scanner 和 Process Hacker 等工具。此外，SystemBC 恶意软件还使用了两个脚本，这两个脚本允许建立一个通往远程 IP 地址的隐蔽通道，用于渗出大小超过 40 KB 且在指定日期后创建的文件。

勒索软件二进制文件则使用流密码ChaCha20算法加密文件，并在每个加密文件上附加扩展名“.6C5oy2dVr6”。

卡巴斯基说：“Ymir非常灵活：通过使用–path命令，攻击者可以指定勒索软件搜索文件的目录。“如果某个文件在白名单上，勒索软件就会跳过该文件，不对其进行加密。这一功能让攻击者可以对加密与否进行更多控制。”

黑巴斯塔勒索软件背后的攻击者被发现使用微软团队聊天信息与潜在目标接触，并加入恶意二维码，通过将他们重定向到欺诈性域来促进初始访问。

ReliaQuest表示：“其根本动机可能是为后续社交工程技术奠定基础，说服用户下载远程监控和管理（RMM）工具，并获得对目标环境的初始访问权限。最终，攻击者在这些事件中的最终目标几乎肯定是部署勒索软件。”

这家网络安全公司表示，它还发现了威胁行为者试图通过伪装成IT支持人员，诱骗用户使用Quick Assist来获得远程访问权限的情况，微软在2024年5月曾对这种技术发出过警告。

作为网络钓鱼攻击的一部分，威胁者会指示受害者安装 AnyDesk 等远程桌面软件或启动 Quick Assist 以获得对系统的远程访问权限。

值得一提的是，该攻击的前一版本采用了恶意邮件战术，向员工的收件箱发送数千封电子邮件，然后冒充公司的 IT 服务台给员工打电话，声称可以帮助解决问题。

涉及 Akira 和 Fog 系列的勒索软件攻击还得益于运行 SonicWall SSL VPN 的系统，这些系统未针对 CVE-2024-40766 打补丁，从而入侵了受害者网络。据 Arctic Wolf 称，从 2024 年 8 月到 10 月中旬，已检测到多达 30 起利用这种策略的新入侵事件。

这些事件反映了勒索软件的持续演变及其对全球组织构成的持续威胁，即使执法部门为瓦解网络犯罪集团所做的努力已导致其进一步分裂。

上个月，将于明年初被 Sophos 收购的 Secureworks 公司透露，由于生态系统中出现了 31 个新的勒索软件集团，活跃的勒索软件集团数量同比增长了 30%。

该网络安全公司表示：“尽管勒索软件群组数量有所增长，但受害者人数却没有以同样的速度增加，这表明勒索软件群组的分布更加分散，这就提出了一个问题：这些新群组的成功率有多大。”

NCC Group 分享的数据显示，2024 年 9 月共记录了 407 起勒索软件案件，低于 8 月份的 450 起，月环比下降 10%。相比之下，2023 年 9 月共发生 514 起勒索软件攻击事件。在此期间，一些主要行业成为攻击目标，其中包括工业、自由消费和信息技术行业。

这还不是全部。最近几个月，勒索软件的使用范围扩大到了像 CyberVolk 这样出于政治动机的黑客组织，这些组织将 “勒索软件作为一种报复工具”。

与此同时，美国官员正在寻求新的方法来打击勒索计划，包括敦促网络保险公司停止对赎金支付的报销，以阻止受害者首先支付赎金。

美国负责网络和新兴技术事务的副国家安全顾问安妮-诺伊伯格在《金融时报》的一篇评论文章中写道：“一些保险公司的保单–例如涵盖赎金支付的报销–鼓励支付赎金，助长了网络犯罪生态系统。“这种做法令人不安，必须终止。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/new-ymir-ransomware-exploits-memory-for.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302368](/post/id/302368)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/new-ymir-ransomware-exploits-memory-for.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/new-ymir-ransomware-exploits-memory-for.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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