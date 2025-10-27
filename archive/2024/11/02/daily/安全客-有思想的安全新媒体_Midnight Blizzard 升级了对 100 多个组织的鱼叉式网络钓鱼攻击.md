---
title: Midnight Blizzard 升级了对 100 多个组织的鱼叉式网络钓鱼攻击
url: https://www.anquanke.com/post/id/301484
source: 安全客-有思想的安全新媒体
date: 2024-11-02
fetch_date: 2025-10-06T19:12:17.088624
---

# Midnight Blizzard 升级了对 100 多个组织的鱼叉式网络钓鱼攻击

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

# Midnight Blizzard 升级了对 100 多个组织的鱼叉式网络钓鱼攻击

阅读量**63887**

发布时间 : 2024-11-01 10:27:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Cedric Pernet，文章来源：techrepublic

原文地址：<https://www.techrepublic.com/article/midnight-blizzard-spearphishing-us-officials/>

译文仅供参考，具体内容表达以及含义原文为准。

**名为 Midnight Blizzard 的俄罗斯黑客利用 RDP 文件对美国官员发起有针对性的鱼叉式网络钓鱼，以获取数据。**

微软威胁情报部门（Microsoft Threat Intelligence）发现了俄罗斯威胁行为者 Midnight Blizzard 的新攻击活动，目标是 100 多个组织的数千名用户。该攻击利用带有 RDP 配置文件的鱼叉式网络钓鱼电子邮件，允许攻击者连接并可能入侵目标系统。

这次攻击活动的目标是高等教育、国防、非政府组织和政府机构的数千名用户。数十个国家受到了影响，尤其是英国、欧洲、澳大利亚和日本，这与之前的午夜暴雪网络钓鱼活动一致。

**钓鱼邮件包含 RDP 配置文件**

在最新的 “午夜暴雪 ”攻击活动中，受害者收到了针对性很强的电子邮件，这些电子邮件使用了与微软、亚马逊网络服务和 “零信任 ”概念有关的社交工程诱饵。

据微软威胁情报部门称，这些电子邮件是利用威胁行为者在以前的入侵活动中收集的属于合法组织的电子邮件地址发送的。所有邮件都包含一个用免费的 LetsEncrypt 证书签名的 RDP 配置文件，其中包括几个敏感设置。

当用户打开该文件时，就会与攻击者控制的系统建立 RDP 连接。通过对已建立的 RDP 连接进行配置，威胁者就可以收集目标系统的信息，如文件和文件夹、已连接的网络驱动器、外围设备（包括打印机、麦克风和智能卡）。

它还能收集剪贴板数据、使用 Windows Hello 的网络身份验证、密码和安全密钥，甚至销售点设备。通过这种连接，威胁者还可以在目标系统或映射的网络共享上安装恶意软件。

![Malicious remote connection.]()
恶意远程连接。图片： 微软

出站 RDP 连接是建立在域上的，目的是诱使目标相信它们是 AWS 域。亚马逊与乌克兰 CERT-UA 合作打击该威胁，立即启动了扣押受影响域的程序，以破坏该操作。与此同时，微软直接通知了受影响的客户，这些客户已成为攻击目标或受到攻击。

**Midnight Blizzard近年来瞄准多个行业**

根据一份联合网络安全咨询报告，Midnight Blizzard 以及 APT29、Cozy Bear 和 Dukes 等威胁行为体与俄罗斯联邦对外情报局有关联。

至少自 2021 年以来，“午夜暴雪 ”一直以美国、欧洲和全球国防、技术和金融部门的实体为目标，追求网络间谍目的并促成进一步的网络行动，包括支持俄罗斯正在进行的入侵乌克兰行动。

2024 年 1 月，该组织以微软和惠普企业为目标，获取了几名员工的电子邮箱。事件发生后，微软表示，网络犯罪分子最初的目标是获取与《午夜暴雪》本身有关的信息的电子邮件账户。

据报道，2024 年 3 月，该威胁行为者调整了策略，将目标转向更多的云环境。

据微软称，午夜暴雪是最隐蔽的网络攻击者之一。微软的另一份报告指出，该组织曾在系统重启后禁用了该组织的端点检测和响应解决方案。然后，他们静静地等待计算机重启一个月，并利用未打补丁的易受攻击计算机。

该威胁行为者还具有很高的技术含量，因为据观察，他们部署了 MagicWeb，这是一种放置在 Active directory Federated Services 服务器上的恶意 DLL，可以保持持久性并窃取信息。该工具还允许 “午夜暴雪 ”生成令牌，从而绕过 AD FS 策略，以任何用户身份登录。

**如何防范午夜暴雪**

可以采取以下几种措施来防范这种威胁：

* 应禁止或限制与外部或公共网络的出站 RDP 连接。
* 应从电子邮件客户端或网络邮件中阻止 RDP 文件。
* 阻止用户执行 RDP 文件。
* 必须尽可能启用多因素身份验证。
* 应部署防网络钓鱼的身份验证方法，如使用 FIDO 令牌。不应使用基于短信的 MFA，因为它可能会被 SIM 卡劫持攻击绕过。
* 必须实施条件访问验证强度，以要求进行防网络钓鱼验证。

此外，必须部署端点检测和响应 (EDR)，以检测和阻止可疑活动。企业还应考虑部署反钓鱼和反病毒解决方案，以帮助检测和阻止威胁。

本文翻译自techrepublic [原文链接](https://www.techrepublic.com/article/midnight-blizzard-spearphishing-us-officials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301484](/post/id/301484)

安全KER - 有思想的安全新媒体

本文转载自: [techrepublic](https://www.techrepublic.com/article/midnight-blizzard-spearphishing-us-officials/)

如若转载,请注明出处： <https://www.techrepublic.com/article/midnight-blizzard-spearphishing-us-officials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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