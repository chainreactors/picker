---
title: Windows 11默认启用BitLocker存储加密
url: https://www.anquanke.com/post/id/296375
source: 安全客-有思想的安全新媒体
date: 2024-05-11
fetch_date: 2025-10-06T17:15:25.559431
---

# Windows 11默认启用BitLocker存储加密

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

# Windows 11默认启用BitLocker存储加密

阅读量**102375**

发布时间 : 2024-05-10 11:34:14

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/tech/windows-11-enable-default-bitlocker-encryption/>

译文仅供参考，具体内容表达以及含义原文为准。

***据报道，Windows 11 的全新安装可能很快就会自动激活 BitLocker 并默认加密硬盘驱动器（存储设备），如 Insider Preview 版本中所示。虽然这将大大提高安全性，但建议用户正确保存恢复密钥。***

据 Deskmodder.de 称，下一个 Windows 11 更新（24H2）将通过自动激活 BitLocker 来修改设置过程。

BitLocker 是一项内置全卷加密功能，首次随 Windows Vista 引入。它对硬盘上的数据进行编码，因此没有密钥就无法读取。

虽然加密可以在设备丢失或被盗时防止未经授权的访问，但默认启用它也会引起一些担忧，因为不知情的用户可能会在重新安装 Windows 后失去对其文件的访问权限。

根据 Deskmodder.de 的一份报告，这一变化会影响“Home”、“Pro”和更高版本的 Windows。更新后，所有计算机都将在设备安全设置中将设备加密功能设置为“打开”。但是，驱动器不会立即加密。

“任何新安装过 24H2 的人都应该先检查一下。将加密设置为“关闭”、撤消加密或确保备份 BitLocker 密钥。因为 Windows 不仅会加密系统磁盘 (C:)，还会加密所有连接的硬盘。”Deskmodder.de 警告道。

用户还可以在安装过程中通过更改注册表项或使用 Rufus 或其他类似软件制作自己的可启动安装介质来绕过加密。

要备份 BitLocker 恢复密钥，请点击 Windows“开始”按钮并键入 BitLocker，然后从搜索结果中选择“管理 BitLocker 控制面板”应用。在这里，选择备份您的恢复密钥并选择要保存它的位置。 Microsoft提供了将其保存到 Microsoft 帐户、USB 闪存驱动器、文件或通过打印密钥的选项。

目前尚不清楚默认加密功能是否会出现在 Windows 11 24H2 的最终版本中，该版本将于 2024 年下半年发布。

Windows更新应该会带来更先进的Microsoft Copilot、新的节能模式、可滚动的快速设置、用于Wi-Fi共享的QR码、除了文件资源管理器中的ZIP之外还支持创建7z和TAR存档、更新任务管理器具有 RAM 性能和其他功能的新指标。 Cyber​​news 此前报道称，Windows 还将在未来的 Windows 版本中删除基本文字处理程序 WordPad 和 Cortana。

本文翻译自 [原文链接](https://cybernews.com/tech/windows-11-enable-default-bitlocker-encryption/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296375](/post/id/296375)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/tech/windows-11-enable-default-bitlocker-encryption/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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