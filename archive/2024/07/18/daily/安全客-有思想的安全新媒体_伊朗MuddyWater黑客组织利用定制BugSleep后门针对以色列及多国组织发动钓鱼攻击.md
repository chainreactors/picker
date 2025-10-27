---
title: 伊朗MuddyWater黑客组织利用定制BugSleep后门针对以色列及多国组织发动钓鱼攻击
url: https://www.anquanke.com/post/id/297994
source: 安全客-有思想的安全新媒体
date: 2024-07-18
fetch_date: 2025-10-06T17:38:39.544418
---

# 伊朗MuddyWater黑客组织利用定制BugSleep后门针对以色列及多国组织发动钓鱼攻击

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

# 伊朗MuddyWater黑客组织利用定制BugSleep后门针对以色列及多国组织发动钓鱼攻击

阅读量**153517**

发布时间 : 2024-07-17 12:33:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源：The Register

原文地址：<https://www.theregister.com/2024/07/17/irans_muddywater_phishes_israeli_orgs/>

译文仅供参考，具体内容表达以及含义原文为准。

伊朗政府支持的网络间谍组织 MuddyWater 使用自定义后门升级了其恶意软件，用于针对以色列组织。

该团伙与伊朗情报和安全部 （MOIS） 有联系，美国于 2022 年制裁了该部，以回应其对阿尔巴尼亚的袭击和其他“针对美国及其盟国的网络活动”。

在 2023 年 10 月 7 日哈马斯领导的袭击事件发生后，MuddyWater 加入了一场明显的反以色列运动，该运动涉及几个伊朗团体。根据 Check Point Research 的说法，此后它转向了部署新后门的网络钓鱼活动——称为 BugSleep。

该团伙的网络钓鱼诱饵最近使用邀请参加网络研讨会和在线课程。自 2 月以来，Check Point 记录了 50 多封此类邮件，这些邮件发送给以色列经济十个部门的数百人。

“其中包括针对以色列市政当局以及更广泛的航空公司，旅行社和记者的显着网络钓鱼活动，”Check Point的威胁情报团队在周一的一份报告中写道。

这些邮件通常是从受感染的组织电子邮件帐户发送的，这有助于诱骗用户打开它们。虽然大多数针对以色列企业，但其他人则被派往土耳其、沙特阿拉伯、印度和葡萄牙的公司。

这些电子邮件包含一个链接，该链接指向合法文件共享和协作平台 Egnyte.com 的子域。一旦用户点击网络钓鱼链接，他们就会看到合法公司或个人的名称，这为骗局提供了可信度。

“在发送给沙特阿拉伯一家运输公司的链接中，显示的所有者姓名是哈马斯前领导人哈立德·马沙尔（Khaled Mashal），也是哈马斯的杰出领导人之一，”Check Point Research写道。

* Microsoft：在哈马斯发动袭击几天后，伊朗的网络工作人员被困在以色列——而不是同时行动
* 山姆大叔就阿尔巴尼亚网络攻击制裁伊朗情报机构
* DarkGate 是恶意软件的瑞士军刀，在竞争对手 Qbot 被粉碎后蓬勃发展
* 中国的 APT41 工作人员在其工具箱中添加了一个隐蔽的恶意软件加载程序和新的后门

在针对以色列市政当局的袭击中，这些电子邮件宣传了一个不存在的市政应用程序，“旨在自动化任务，提高效率，并确保运营的最大安全性”。

但是，单击该链接不会下载应用程序。相反，它会将 BugSleep 放在受害者的机器上。

这种新的定制恶意软件“部分取代”了 MuddyWater 使用合法的远程监控和管理工具。“我们发现了正在分发的恶意软件的几个版本，每个版本之间的差异显示了改进和错误修复（有时还会创建新的错误），”Check Point建议道。这种策略还使安全软件更难获取攻击代码的签名。

威胁猎人进一步分析了恶意软件，并对其进行了如下描述：

BugSleep 主逻辑在所有版本中都是相似的，首先是多次调用 API 以规避沙箱，然后加载正常运行所需的 API。然后，它创建一个互斥锁（我们在示例中观察到）并解密其配置，其中包括 C&C IP 地址和端口。所有配置和字符串都以相同的方式加密，其中每个字节都用相同的硬编码值减去。`Sleep``"PackageManager"``"DocumentUpdater"`

Check Point 分析的样本创建了几个不同的计划任务，每 30 分钟触发一次，这也确保了受感染设备上的持久性。

其中包括将被盗文件发送到控制和命令服务器、将内容写入文件、删除任务和创建新任务以及更新睡眠时间和超时值。

分析的其中一个示例包括帮助恶意软件逃避端点检测工具检测的方法：

首先，恶意软件启用结构的标志，以防止进程加载未经 Microsoft 签名的图像。这样可以防止其他进程将 DLL 注入进程。`MicrosoftSignedOnly``ProcessSignaturePolicy`

接下来，它启用结构的标志，以防止进程生成动态代码或修改现有的可执行代码。启用可能有助于保护它免受 EDR 解决方案的影响，这些解决方案挂钩用户空间 API 函数以检查程序的意图。`ProhibitDynamicCode``ProcessDynamicCodePolicy``ProcessDynamicCodePolicy`

该恶意软件的另一个版本还包括自定义 shellcode 加载程序。

Check Point警告说，虽然工作人员继续专注于其恶意软件活动中的特定领域，但从定制诱饵转向更通用的诱饵也将使网络间谍更容易专注于更大规模的攻击。

本文翻译自The Register [原文链接](https://www.theregister.com/2024/07/17/irans_muddywater_phishes_israeli_orgs/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297994](/post/id/297994)

安全KER - 有思想的安全新媒体

本文转载自: [The Register](https://www.theregister.com/2024/07/17/irans_muddywater_phishes_israeli_orgs/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/17/irans_muddywater_phishes_israeli_orgs/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络钓鱼](/tag/%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC)
* [安全时讯](/tag/%E5%AE%89%E5%85%A8%E6%97%B6%E8%AE%AF)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [德国对沃达丰隐私和安全漏洞罚款 5100 万美元](/post/id/308315)

  2025-06-10 13:44:46
* ##### [CISA取消24亿美元网络安全采购](/post/id/307402)

  2025-05-15 16:10:04
* ##### [蝉联最多领域榜首！360获评权威报告“垂直赛道王者”](/post/id/307386)

  2025-05-15 15:23:30
* ##### [严重缺陷暴露100，000多个WooCommerce网站：未经验证的文件包含威胁全面收购](/post/id/307163)

  2025-05-07 18:09:06
* ##### [网络钓鱼短信诱骗Apple iMessage用户禁用保护](/post/id/303439)

  2025-01-13 11:04:56
* ##### [2024年的网络钓鱼：应对持续威胁和人工智能的双刃剑](/post/id/303433)

  2025-01-13 10:12:37
* ##### [新的二维码网络钓鱼活动利用 Microsoft Sway 窃取凭据](/post/id/299603)

  2024-08-29 15:57:15

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