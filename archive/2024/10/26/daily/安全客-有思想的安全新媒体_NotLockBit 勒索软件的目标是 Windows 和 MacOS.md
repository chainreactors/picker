---
title: NotLockBit 勒索软件的目标是 Windows 和 MacOS
url: https://www.anquanke.com/post/id/301256
source: 安全客-有思想的安全新媒体
date: 2024-10-26
fetch_date: 2025-10-06T18:45:40.882912
---

# NotLockBit 勒索软件的目标是 Windows 和 MacOS

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

# NotLockBit 勒索软件的目标是 Windows 和 MacOS

阅读量**62559**

发布时间 : 2024-10-25 10:22:45

**x**

##### 译文声明

本文是翻译文章，文章来源：heimdalsecurity

原文地址：<https://heimdalsecurity.com/blog/notlockbit-ransomware-targets-both-windows-and-macos/>

译文仅供参考，具体内容表达以及含义原文为准。

![article featured image]()

研究人员警告说，NotLockBit 是一个模仿 LockBit 勒索软件的新型恶意软件系列，可影响 Windows 和 macOS 系统。

该恶意软件似乎是首个针对 macOS 系统的全功能勒索软件，超越了以前的概念验证（PoC）样本。

**什么是 NotLockBit 勒索软件？**

安全研究人员称，NotLockBit 是一款 Go 编写的恶意软件。与许多其他勒索软件一样，它的目的是实现双重勒索：

* 加密文件，使受害者无法读取文件
* 删除阴影副本，防止数据恢复

NotLockBit 会用“.abcd ”扩展名标记加密文件。然后，它会在每个被破坏的文件夹中留下一张赎金条，并试图用 LockBit 2.0 的横幅来更改桌面墙纸。

该恶意软件使用 RSA 非对称加密，这意味着没有私钥就无法解密主密钥。

在开始加密过程之前，勒索软件会将数据外泄到攻击者控制的亚马逊 S3 存储桶中。为此，它使用了硬编码的 AWS 凭据。研究人员告诉 SecurityWeek.com：

我们怀疑勒索软件作者使用的是他们自己的 AWS 账户或被入侵的 AWS 账户。我们发现了三十多个可能来自同一作者的样本，这表明该勒索软件正在被积极开发和测试。

来源：SecurityWeek.com

目前，他们已经向 AWS 报告了这一恶意活动，AWS 暂停了访问密钥和相关账户。

不过，运行 macOS 系统的安全团队应保持警惕，因为该威胁仍在全面发挥作用。

**如何确保 macOS 系统免受 NotLockBit 的攻击**

作为分层防御策略的一部分，DNS 过滤是最有效的勒索软件预防工具之一。

要窃取并加密你的数据，黑客需要在你的电脑上部署勒索软件。然后，他们必须与指挥控制中心建立连接，安装其他恶意软件。最后，他们还必须使用另一个连接将数据外泄到 C2。所有这三个步骤都意味着黑客必须在计算机和恶意域之间建立连接。这就是 DNS 过滤发挥作用的地方。

最好的 DNS 安全软件运行的引擎可以检测并阻止恶意域，即使没有人将其标记为恶意域。如果员工打开钓鱼邮件并点击恶意链接，即使该域名没有被列入黑名单，DNS 过滤器也会将其识别为有害域名。因此，它会当场阻止连接。没有恶意通信，没有恶意软件部署，也就不会造成危害。

本文翻译自heimdalsecurity [原文链接](https://heimdalsecurity.com/blog/notlockbit-ransomware-targets-both-windows-and-macos/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301256](/post/id/301256)

安全KER - 有思想的安全新媒体

本文转载自: [heimdalsecurity](https://heimdalsecurity.com/blog/notlockbit-ransomware-targets-both-windows-and-macos/)

如若转载,请注明出处： <https://heimdalsecurity.com/blog/notlockbit-ransomware-targets-both-windows-and-macos/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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