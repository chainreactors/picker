---
title: 网络攻击者在可能的间谍活动中利用 Google Sheets 进行恶意软件控制
url: https://www.anquanke.com/post/id/299698
source: 安全客-有思想的安全新媒体
date: 2024-09-03
fetch_date: 2025-10-06T18:23:59.910557
---

# 网络攻击者在可能的间谍活动中利用 Google Sheets 进行恶意软件控制

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

# 网络攻击者在可能的间谍活动中利用 Google Sheets 进行恶意软件控制

阅读量**92975**

发布时间 : 2024-09-02 16:55:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/cyberattackers-exploit-google-sheets.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种新型恶意软件活动，该活动利用 Google 表格作为命令和控制 （C2） 机制。

Proofpoint 从 2024 年 8 月 5 日开始检测到该活动，它冒充欧洲、亚洲和美国政府的税务机关，目标是通过名为 Voldemort 的定制工具针对全球 70 多个组织，该工具能够收集信息并提供额外的有效载荷。

目标行业包括保险、航空航天、运输、学术界、金融、技术、工业、医疗保健、汽车、酒店、能源、政府、媒体、制造、电信和社会福利组织。

可疑的网络间谍活动尚未归因于特定的指定威胁行为者。作为攻击的一部分，已经发送了多达 20,000 封电子邮件。

![Cybersecurity]()

这些电子邮件声称来自美国、英国、法国、德国、意大利、印度和日本的税务机关，提醒收件人其税务申报的变化，并敦促他们点击 Google AMP 缓存 URL，将用户重定向到中间登录页面。

该页面的作用是检查 User-Agent 字符串以确定操作系统是否为 Windows，如果是，则利用 search-ms： URI 协议处理程序显示一个 Windows 快捷方式 （LNK） 文件，该文件使用 Adobe Acrobat Reader 伪装成 PDF 文件，以试图诱骗受害者启动它。

“如果执行 LNK，它将调用 PowerShell 从同一隧道 （\library\） 上的第三个 WebDAV 共享运行Python.exe，并在同一主机上的第四个共享 （\resource\） 上传递 Python 脚本作为参数，”Proofpoint 研究人员 Tommy Madjar、Pim Trouerbach 和 Selena Larson 说。

“这会导致 Python 在不将任何文件下载到计算机的情况下运行脚本，直接从 WebDAV 共享加载依赖项。”

Python 脚本旨在收集系统信息，并以 Base64 编码字符串的形式将数据发送到参与者控制的域，然后向用户显示诱饵 PDF，并从 OpenDrive 下载受密码保护的 ZIP 文件。

就其本身而言，ZIP 存档包含两个文件，一个容易受到 DLL 旁加载的合法可执行“CiscoCollabHost.exe”和一个旁加载的恶意 DLL“CiscoSparkLauncher.dll”（即 Voldemort）文件。

Voldemort 是一个用 C 语言编写的自定义后门，具有信息收集和加载下一阶段有效载荷的功能，恶意软件利用 Google 表格进行 C2、数据泄露和执行操作员的命令。

Proofpoint 将该活动描述为与高级持续威胁 （APT） 保持一致，但由于使用了电子犯罪领域流行的技术，因此带有“网络犯罪氛围”。

“威胁行为者滥用文件架构 URI 来访问用于恶意软件暂存的外部文件共享资源，特别是 WebDAV 和服务器消息块 （SMB）。这是通过使用架构’file://’并指向托管恶意内容的远程服务器来完成的，“研究人员说。

这种方法在充当初始访问代理 （IAB） 的恶意软件家族中越来越普遍，例如 Latrodectus、DarkGate 和 XWorm。

此外，Proofpoint 表示，它能够读取 Google Sheet 的内容，总共确定了六名受害者，其中包括一名据信是沙盒或“已知研究人员”的受害者。

该活动被贴上了不寻常的标签，增加了威胁行为者在锁定一小群目标之前撒下大网的可能性。攻击者也可能具有不同的技术专业知识水平，计划感染多个组织。

![Cybersecurity]()

研究人员说：“虽然许多活动特征与网络犯罪威胁活动一致，但我们评估这可能是为支持尚不清楚的最终目标而进行的间谍活动。

“巧妙而复杂的能力与非常基本的技术和功能相结合，使得评估威胁行为者的能力水平和高度自信地确定活动的最终目标变得困难。”

这一发展是在 Netskope Threat Labs 发现 Latrodectus 恶意软件的更新版本（1.4 版）之际进行的，该恶意软件带有一个新的 C2 端点，并添加了两个新的后门命令，允许它从指定服务器下载 shellcode 并从远程位置检索任意文件。

“Latrodectus 发展得非常快，为其有效载荷添加了新功能，”安全研究员 Leandro Fróes 说。“了解应用于其有效载荷的更新使防御者能够正确设置自动管道，并使用这些信息进一步寻找新变体。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/cyberattackers-exploit-google-sheets.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299698](/post/id/299698)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/cyberattackers-exploit-google-sheets.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/cyberattackers-exploit-google-sheets.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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