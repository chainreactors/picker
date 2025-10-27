---
title: 新的 Grandoreiro 银行恶意软件变种出现，采用先进策略躲避检测
url: https://www.anquanke.com/post/id/301238
source: 安全客-有思想的安全新媒体
date: 2024-10-25
fetch_date: 2025-10-06T18:45:35.131205
---

# 新的 Grandoreiro 银行恶意软件变种出现，采用先进策略躲避检测

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

# 新的 Grandoreiro 银行恶意软件变种出现，采用先进策略躲避检测

阅读量**94790**

发布时间 : 2024-10-24 15:23:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/new-grandoreiro-banking-malware.html>

译文仅供参考，具体内容表达以及含义原文为准。

卡巴斯基周二发布分析报告称，一种名为 “Grandoreiro ”的银行恶意软件的新变种被发现采用了新的策略，试图绕过反欺诈措施，这表明尽管执法部门努力打击这一行动，但该恶意软件仍在继续积极开发。

卡巴斯基在周二发表的一份分析报告中说：“这个团伙只有一部分人被捕：Grandoreiro 背后的其余操作者继续攻击世界各地的用户，进一步开发新的恶意软件，建立新的基础设施。”

卡巴斯基周二发布的分析报告称：“其他一些新加入的伎俩包括使用域生成算法（DGA）进行指挥控制（C2）通信、密文窃取（CTS）加密和鼠标跟踪。此外，还观察到专门针对墨西哥银行客户的 “轻型本地版本。”

Grandoreiro 自 2016 年开始活跃，随着时间的推移不断演变，努力保持不被发现，同时还将其地理范围扩大到拉丁美洲和欧洲。它能够窃取分布在 45 个国家和地区的 1700 家金融机构的凭证。

据说它是以恶意软件即服务（MaaS）的模式运行的，但有证据表明它只提供给特定的网络犯罪分子和可信的合作伙伴。

今年有关 Grandoreiro 的最重要进展之一是逮捕了该组织的一些成员，这一事件导致恶意软件德尔菲代码库支离破碎。

卡巴斯基说：“这一发现的佐证是，在同时进行的活动中存在两个不同的代码库：较新的样本具有更新的代码，而较旧的样本则依赖于传统代码库，现在只针对墨西哥的用户–大约 30 家银行的客户。”

Grandoreiro 主要通过钓鱼邮件传播，其次是通过谷歌上的恶意广告传播。第一阶段是一个 ZIP 文件，其中包含一个合法文件和一个 MSI 加载器，后者负责下载和启动恶意软件。

在 2023 年观察到的活动中发现，通过伪装成 AMD 外部数据固态硬盘驱动器，利用文件大小为 390 MB 的超大可移植可执行文件绕过沙箱，在雷达的监视下飞行。

这种银行恶意软件具有收集主机信息和 IP 地址位置数据的功能。它还会提取用户名并检查其中是否包含 “John ”或 “WORK ”字符串，如果包含，则停止执行。

“Grandoreiro 搜索反恶意软件解决方案，如 AVAST、Bitdefender、Nod32、Kaspersky、McAfee、Windows Defender、Sophos、Virus Free、Adaware、Symantec、Tencent、Avira、ActiveScan 和 CrowdStrike，”该公司说。“它还会寻找银行安全软件，如 Topaz OFD 和 Trusteer。”

该恶意软件的另一个显著功能是检查系统中是否存在某些网络浏览器、电子邮件客户端、VPN 和云存储应用程序，并监控用户在这些应用程序中的活动。此外，它还可以充当剪切器，将加密货币交易转到威胁行为者控制的钱包中。

在今年的逮捕行动之后检测到的较新攻击链包括在执行主要有效载荷之前设置验证码障碍，以此绕过自动分析。

最新版本的 Grandoreiro 还进行了重大更新，包括自我更新、记录击键、选择国家列出受害者、检测银行安全解决方案、使用 Outlook 发送垃圾邮件以及监控 Outlook 邮件中的特定关键字。

它还配备了捕捉鼠标移动的功能，这表明它试图模仿用户行为，诱骗反欺诈系统将这些活动识别为合法活动。

研究人员说：“这一发现凸显了像 Grandoreiro 这样的恶意软件的不断演变，攻击者越来越多地采用旨在对抗依赖于行为生物识别和机器学习的现代安全解决方案的策略。”

一旦获得凭证，威胁者就会通过转账应用程序、加密货币、礼品卡或自动取款机将资金转入当地 “骡子 ”的账户。这些 “骡子 ”通过 Telegram 频道确认身份，每天向他们支付 200 到 500 美元。

使用基于 Delphi 的名为 Operator 的工具可以远程访问受害者机器，只要受害者开始浏览目标金融机构网站，该工具就会显示受害者名单。

卡巴斯基说：“Grandoreiro 银行恶意软件背后的威胁行为者正在不断改进他们的战术和恶意软件，以成功地对目标实施攻击并躲避安全解决方案。”

“巴西银行木马已经成为一种国际威胁；它们正在填补东欧犯罪团伙转移到勒索软件领域后留下的空白。”

几周前，墨西哥网络安全公司 Scitum 警告说，一个名为 “壁虎攻击”（Gecko Assault）的新活动正在针对拉丁美洲（LATAM）地区的 Windows 用户传播两个不同的银行恶意软件家族 Mispadu 和 Mekotio。

拉丁美洲和加勒比海地区的用户，尤其是巴西用户，还成为了另一个代号为 “Silver Oryx Blade ”的银行木马的攻击目标，该木马的目的是在用户通过浏览器访问银行网站时窃取敏感的金融信息。

Scitum 指出：“Silver Oryx Blade 可以窃取各类用户（包括企业员工）的银行信息。此外，它还具有命令执行能力。”

“该木马的传播方式是通过（针对巴西用户的）钓鱼邮件，以所谓的工资奖金、PIX转账和财政通知等为借口，冒充人力资源财务部门和巴西财政部。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/new-grandoreiro-banking-malware.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301238](/post/id/301238)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/new-grandoreiro-banking-malware.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/new-grandoreiro-banking-malware.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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