---
title: 联邦调查局称一名系统管理员锁定了数千台 Windows 工作站并索要赎金
url: https://www.anquanke.com/post/id/299645
source: 安全客-有思想的安全新媒体
date: 2024-08-31
fetch_date: 2025-10-06T17:59:22.110851
---

# 联邦调查局称一名系统管理员锁定了数千台 Windows 工作站并索要赎金

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

# 联邦调查局称一名系统管理员锁定了数千台 Windows 工作站并索要赎金

阅读量**106042**

发布时间 : 2024-08-30 14:48:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 杰西卡·莱昂斯，文章来源： theregister

原文地址：<https://www.theregister.com/2024/08/29/vm_engineer_extortion_allegations/>

译文仅供参考，具体内容表达以及含义原文为准。

一名前基础设施工程师据称将 IT 部门同事锁在雇主的系统之外，然后威胁如果不支付赎金就关闭服务器，他在 FBI 调查后被捕并受到指控。

密苏里州堪萨斯城 57 岁的丹尼尔·莱恩 （Daniel Rhyne） 现在因涉嫌勒索未遂而面临最高 35 年的监禁，此前他被指控犯有一项与威胁对受保护计算机造成损害有关的敲诈勒索罪、一项故意损坏受保护计算机的罪名和一项电汇欺诈罪。

根据法庭文件 ，Rhyne 于 2023 年 11 月在一家总部位于新泽西州萨默塞特县的未具名工业公司工作时策划了该计划。

据称，他的勒索计划于 2023 年 11 月 25 日美国东部标准时间 1600 左右开始，当时网络管理员收到了一个域管理员帐户和数百个用户帐户的密码重置通知。大约 44 分钟后，该公司的员工收到了一封主题为“您的网络已被渗透”的电子邮件。

这封电子邮件警告员工，所有 IT 管理员都被锁定，或者他们的帐户被删除，所有备份都已被删除。然后是每天关闭 40 台服务器的威胁，直到支付赎金。

据称，Rhyne 安排了删除 13 个域管理员帐户并更改属于 301 个域用户帐户和两个本地管理员帐户的密码的任务。这会将这些用户锁定在 254 台 Windows 服务器之外。

检察官称，疑似险恶的系统管理员还更改了另外两个本地管理员帐户的密码，这些帐户将影响 3,284 个工作站，并在 2023 年 12 月开始的几天内关闭了“几个”服务器和工作站。

据说 Rhyne 使用 Windows 的网络用户和 Sysinternals Utilities 的 PsPasswd 工具修改了这些帐户并将密码更改为“TheFr0zenCrew”！

非常有创意。但是，如果联邦调查局是对的，也许他应该放手一搏，因为他们声称他们追踪到了一个用于远程访问管理员帐户的隐藏虚拟机，可以追溯到 Rhyne 公司发放的笔记本电脑。他还对这个被盗用的帐户使用了相同的密码“TheFr0zenCrew！”。

法庭文件还详细说明了 Rhyne 所谓的网络搜索历史，检察官表示，其中包括查找短语，包括“更改密码的命令行”、“更改本地管理员密码的命令行”和“远程更改本地管理员密码的命令行”。

此外，据称该公司的安全摄像头和访问日志记录了 Rhyne 在登录公司笔记本电脑之前立即进入大楼，进行可疑搜索，查看公司密码电子表格，同时还访问了隐藏的虚拟机。

Rhyne 于 8 月 27 日在堪萨斯城联邦法院首次出庭。

与威胁对受保护计算机造成损害有关的敲诈勒索指控最高可判处 5 年监禁和 250,000 美元罚款。故意损坏受保护计算机的指控最高可判处 10 年监禁和 250,000 美元罚款。电汇欺诈罪最高可判处 20 年监禁和 250,000 美元罚款。

本文翻译自 theregister [原文链接](https://www.theregister.com/2024/08/29/vm_engineer_extortion_allegations/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299645](/post/id/299645)

安全KER - 有思想的安全新媒体

本文转载自:  [theregister](https://www.theregister.com/2024/08/29/vm_engineer_extortion_allegations/)

如若转载,请注明出处： <https://www.theregister.com/2024/08/29/vm_engineer_extortion_allegations/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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