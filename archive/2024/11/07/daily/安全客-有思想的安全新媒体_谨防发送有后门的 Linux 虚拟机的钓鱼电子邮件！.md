---
title: 谨防发送有后门的 Linux 虚拟机的钓鱼电子邮件！
url: https://www.anquanke.com/post/id/301590
source: 安全客-有思想的安全新媒体
date: 2024-11-07
fetch_date: 2025-10-06T19:12:13.698994
---

# 谨防发送有后门的 Linux 虚拟机的钓鱼电子邮件！

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

# 谨防发送有后门的 Linux 虚拟机的钓鱼电子邮件！

阅读量**64152**

发布时间 : 2024-11-06 11:22:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/11/05/phishing-oneamerica-survey-linux-vm-backdoor/>

译文仅供参考，具体内容表达以及含义原文为准。

Securonix 研究人员发现，不明攻击者正试图诱骗 Windows 用户启动一个带有预配置后门的定制 Linux 虚拟机（VM）。

**攻击活动**

他们认为，攻击始于一封网络钓鱼电子邮件，但无法确定目标受害者。

该电子邮件包含一个指向异常大的 ZIP 文件（285 MB）的链接，其名称 OneAmerica Survey.zip 指向了可能的诱惑：由提供金融服务的美国公司 OneAmerica Financial 发起的一项调查。

研究人员解释说：“当用户解压缩时，会看到一个名为‘OneAmerica Survey’的文件（快捷方式）和一个包含整个 QEMU 安装目录的‘data’目录。”

研究人员解释说，”如果用户点击快捷方式文件，就会启动一个进程：

* ZIP 文件被 “解压缩”，其内容被放入用户的配置文件目录下一个名为 “datax ”的目录中
* 执行批处理 (BAT) 文件，并显示一个诱饵图像，提示 “服务器内部出错”，同时在后台执行一个（重命名的）QEMU 进程和命令行，以启动模拟的 Tiny Core Linux 环境

定制的 Linux 虚拟机旨在通过启动 SSH 连接在主机上创建一个交互式 shell（本质上是后门），攻击者可以通过该 shell 下载更多恶意有效载荷：

* 下载其他恶意有效载荷
* 在机器上安装其他工具
* 重命名文件
* 修改系统配置
* 通过系统和用户枚举进行基本侦察
* 渗出数据

“就像下棋一样，攻击者在准备他们的环境时就考虑到了策略。他们系统地安装、测试和执行了多个有效载荷和配置，每个都是为下一阶段做准备，”研究人员指出。

研究人员指出：“使用 bootlocal.sh 和 SSH 密钥表明，他们的目标是在机器上建立可靠的存在。有几次，他们从不同的 URL 下载了 crondx 文件（预配置 Chisel 客户端）。原因不明，但我们推测他们可能在修改有效载荷，直到其功能达到预期。”

![Linux VM backdoor]()

诱饵镜像（来源：Securonix）

Chisel 客户端经过预配置，可通过网络套接字自动连接到指定的命令与控制（C2）服务器，从而打开一个持久后门，攻击者可通过该后门访问被入侵的环境。

**逃避检测**

传统的防病毒解决方案通常无法（或默认情况下不会）扫描超大文件，也无法查看仿真 Linux 环境中发生的情况。

研究人员补充说：“Chisel 的设计使其在创建隐蔽的通信渠道和穿越防火墙隧道方面尤为有效，而且往往能躲过网络监控工具的监控。”

“攻击者对 QEMU 和 Chisel 等合法软件的依赖增加了额外的规避层，因为这些工具在许多环境中都不太可能触发警报。”

Securonix 分享了与此活动相关的危害指标，并建议企业监控常见的恶意软件暂存目录，监控从异常位置执行合法软件的实例，使用强大的端点日志来帮助 PowerShell 检测。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/11/05/phishing-oneamerica-survey-linux-vm-backdoor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301590](/post/id/301590)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/11/05/phishing-oneamerica-survey-linux-vm-backdoor/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/11/05/phishing-oneamerica-survey-linux-vm-backdoor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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