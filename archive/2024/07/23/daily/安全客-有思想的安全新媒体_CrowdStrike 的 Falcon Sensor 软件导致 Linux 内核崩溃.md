---
title: CrowdStrike 的 Falcon Sensor 软件导致 Linux 内核崩溃
url: https://www.anquanke.com/post/id/298132
source: 安全客-有思想的安全新媒体
date: 2024-07-23
fetch_date: 2025-10-06T17:42:22.413989
---

# CrowdStrike 的 Falcon Sensor 软件导致 Linux 内核崩溃

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

# CrowdStrike 的 Falcon Sensor 软件导致 Linux 内核崩溃

阅读量**81752**

发布时间 : 2024-07-22 09:58:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Simon Sharwood，文章来源：the register

原文地址：<https://www.theregister.com/2024/07/21/crowdstrike_linux_crashes_restoration_tools/>

译文仅供参考，具体内容表达以及含义原文为准。

CrowdStrike的Falcon Sensor软件，上周导致大量Windows电脑出现故障，现在也被发现与Linux内核恐慌和系统崩溃有关。六月份，Red Hat警告其客户在使用版本为5.14.0-427.13.1.el9\_4.x86\_64的内核启动后，由Falcon Sensor进程引发的“观察到内核恐慌”问题，影响了部分Red Hat Enterprise Linux 9.4用户。

第二个问题报告标题为“在cshook\_network\_ops\_inet6\_sockraw\_release+0x171a9处系统崩溃”，建议用户寻求帮助以解决CrowdStrike Falcon Sensor/Agent安全软件套件提供的内核模块可能引起的问题。Red Hat还建议，“禁用CrowdStrike Falcon Sensor/Agent软件套件……将缓解崩溃并为正在调查问题的系统提供暂时的稳定性”。这个问题不仅限于特定版本，而是被观察到在版本6和7中。

我们也发现了CrowdStrike疑似在Debian和Rocky Linux中引起问题的报告。Linux内核恐慌与Windows蓝屏死机大致相似。CrowdStrike在导致许多Windows实例崩溃前几周就发生了内核恐慌，这暗示了这家安全供应商更广泛的问题。

*The Register* 已要求 CrowdStrike 对 Red Hat 发现的问题发表评论，如果我们收到大量信息，将更新此故事。

**CrowdStrike的CEO监督了非常相似的McAfee崩溃**

CrowdStrike的CEO之前曾负责过非常类似的McAfee崩溃事件。

2010年，全球PC因反病毒供应商McAfee推送错误更新而崩溃，导致电脑陷入无休止的重启循环。

当时，McAfee的首席技术官是George Kurtz，他现在担任CrowdStrike的CEO。

### 快速恢复工具即将推出

CrowdStrike在周日预告了一款快速恢复工具，用于解决它所造成的问题。

“我们与客户一起测试了一种新的技术来加速受影响系统的修复。”这家安全供应商在LinkedIn上表示，“我们正在将这一技术操作化，提供选择加入的选项。我们正以分钟为单位取得进展。”

这种进展可能引起极大关注，因为微软企业与操作系统安全部门副总裁David Weston周六估计，850万台Windows机器受到了这个问题的影响。

微软也创建了一个可从可引导USB存储设备运行的修复工具，可以在这里找到，以及使用说明。这些说明在周日进行了修改，要求彻底擦除USB设备，“以免在恢复过程中出错”。

**MORE CONTENT**

* CrowdStrike 股价下跌，因为全球 IT 中断严重破坏了全球系统
* 网络犯罪分子迅速利用 CrowdStrike 的混乱局面
* 愤怒的管理员分享 CrowdStrike 中断体验
* 生活中断：CrowdStrike 的补丁失败如何搞砸世界

### 不确定

CrowdStrike造成的中断程度仍然不确定，但我们已经读到仅上周五就有超过6800个航班被取消，一些航空公司直到周日晚上才恢复系统。

英国医学会警告说，“由于故障造成的积压，无法立即恢复正常服务。”

澳大利亚内政部长Claire O’Neill警告称，修复工作可能需要数周时间。

本文翻译自the register [原文链接](https://www.theregister.com/2024/07/21/crowdstrike_linux_crashes_restoration_tools/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298132](/post/id/298132)

安全KER - 有思想的安全新媒体

本文转载自: [the register](https://www.theregister.com/2024/07/21/crowdstrike_linux_crashes_restoration_tools/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/21/crowdstrike_linux_crashes_restoration_tools/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**0赞

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

* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险](/post/id/308238)

  2025-06-09 17:01:38
* ##### [阿联酋中央银行要求金融机构放弃短信和 OTP 身份验证](/post/id/308132)

  2025-06-05 12:29:10
* ##### [警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据](/post/id/308092)

  2025-06-04 15:31:41
* ##### [新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备](/post/id/307967)

  2025-05-29 14:59:17
* ##### [APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信](/post/id/307963)

  2025-05-29 14:55:27
* ##### [TikTok 视频在 ClickFix 攻击中推送信息窃取恶意软件](/post/id/307915)

  2025-05-28 14:05:13

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