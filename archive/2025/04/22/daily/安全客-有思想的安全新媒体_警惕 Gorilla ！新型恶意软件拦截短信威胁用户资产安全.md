---
title: 警惕 Gorilla ！新型恶意软件拦截短信威胁用户资产安全
url: https://www.anquanke.com/post/id/306724
source: 安全客-有思想的安全新媒体
date: 2025-04-22
fetch_date: 2025-10-06T22:03:47.143441
---

# 警惕 Gorilla ！新型恶意软件拦截短信威胁用户资产安全

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

# 警惕 Gorilla ！新型恶意软件拦截短信威胁用户资产安全

阅读量**48930**

发布时间 : 2025-04-21 14:04:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-gorilla-android-malware-intercept-sms-messages/>

译文仅供参考，具体内容表达以及含义原文为准。

一种名为 Gorilla 的复杂新型 Android 恶意软件在网络安全领域出现了，它专门被设计用来拦截包含一次性密码（OTP）的 SMS。

这种恶意软件在后台悄无声息地运行，利用 Android 系统的权限机制来获取受感染设备上的敏感信息。

初步分析表明，Gorilla 主要针对银行客户以及诸如 Yandex 等热门服务的用户，它对窃取到的 SMS 进行分类，以便攻击者更轻松地利用这些信息。

该恶意软件利用了 Android 系统的关键权限，包括 “READ\_PHONE\_STATE” 和 “READ\_PHONE\_NUMBERS” 权限，来访问 SIM 卡信息并从受感染设备中获取电话号码。

一旦安装，Gorilla 会使用 WebSocket 协议与它的命令与控制（C2）基础设施建立持久连接，其连接格式为 “ws://\(URL/ws/devices/?device\_id=\)android\_id&platform=android”，以此与它的操控者保持持续通信。

这种连接使得恶意软件能够实时接收命令并将敏感数据泄露出去。

Catalyst 的研究人员发现，Gorilla 采用了一种不寻常的技术来逃避检测，它避免使用 getInstalledPackages 或 getInstalledApplications 应用程序编程接口（API），因为使用这些接口需要 REQUEST\_INSTALLED\_PACKAGES 权限，而这可能会引起怀疑。

相反，该恶意软件通过查询启动器意图来确定软件包名称、应用程序名称和版本，这样它就能在保持较低存在感的同时收集有关已安装应用程序的信息。

该恶意软件的命令与控制（C2）面板显示出其复杂的运作方式，被盗取的 SMS 被系统地归类在诸如“ Banks” 和 “Yandex” 等标签下，这表明它针对金融信息和热门服务采取了有针对性的攻击方式。

这种分类使攻击者能够快速识别并利用拦截到的 SMS 中包含的有价值的验证码和敏感信息。

从本质上讲，Gorilla 通过一系列后台服务运行，即使在用户不主动使用设备时也能确保其持续运行。

为了符合 Android 系统的要求，这些服务利用 startForeground API 以及 FOREGROUND\_SERVICE 权限来显示一条通知，有效地将其恶意活动伪装成合法的系统进程。

****技术分析：命令结构和功能****

该恶意软件的命令结构揭示了三种主要的操作类型，每种操作类型在攻击链中都有特定的功能。

“device\_info” 命令会提取并向攻击者传输有关受感染设备的详细信息。

“update\_settings” 命令目前似乎处于休眠状态，因为它只是记录接收情况而不采取进一步行动，但它很可能允许对恶意软件的行为进行远程配置。

最关键的是，“send\_sms” 命令允许攻击者从受感染设备向指定的接收者发送带有自定义消息文本的 SMS。

// Command handling structure in Gorilla malware

// Three primary command types:

device\_info // Transmits device information

update\_settings // Currently inactive but logs receipt

send\_sms // Allows remote SMS sending with specified text

在积极利用 SMS 拦截功能的同时，Gorilla 包含的一些组件表明它计划扩展其功能。

未使用的 WebViewActivity 类的存在尤其令人担忧，因为这个组件通常用于呈现 HTML 内容，并且在银行恶意软件中常被用来显示逼真的网络钓鱼页面，以获取银行凭证或信用卡信息。 该恶意软件还包含一个有趣但目前未激活的持久化机制，其形式为 USSDReceiver 类。

这个组件被设计用来监听拨打的代码 “\*#0000#”，并在检测到该代码时启动 MainActivity。虽然目前它未被注册或激活，但这种机制可以为攻击者提供一种额外的方法，确保即使在用户尝试删除恶意软件之后，它仍能继续运行。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-gorilla-android-malware-intercept-sms-messages/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306724](/post/id/306724)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-gorilla-android-malware-intercept-sms-messages/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-gorilla-android-malware-intercept-sms-messages/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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