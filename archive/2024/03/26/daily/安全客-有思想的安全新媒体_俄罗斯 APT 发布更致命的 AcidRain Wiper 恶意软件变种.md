---
title: 俄罗斯 APT 发布更致命的 AcidRain Wiper 恶意软件变种
url: https://www.anquanke.com/post/id/294276
source: 安全客-有思想的安全新媒体
date: 2024-03-26
fetch_date: 2025-10-04T12:11:27.852948
---

# 俄罗斯 APT 发布更致命的 AcidRain Wiper 恶意软件变种

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

# 俄罗斯 APT 发布更致命的 AcidRain Wiper 恶意软件变种

阅读量**112973**

发布时间 : 2024-03-25 10:14:22

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/russian-apt-releases-more-deadly-variant-of-acidrain-wiper-malware>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员发现，俄罗斯军事情报部门在 2022 年 2 月入侵乌克兰之前，曾使用该恶意软件破坏乌克兰的卫星宽带服务，该恶意软件更为危险且多产。

新的变体“ AcidPour ”与它的前身有很多相似之处，但它是针对 X86 架构编译的，这与 AcidRain 不同，AcidRain 的目标是基于 MIPS 的系统。据发现该威胁的 SentinelOne 研究人员称，新型雨刮器还具有比 AcidRain 更广泛的功能，可用于对抗更广泛的目标。

**更广泛的破坏能力**

SentinelOne 高级威胁研究员 Tom Hegel 表示：“AcidPour 扩展的破坏性功能包括 Linux 未排序块映像 (UBI) 和设备映射器 (DM) 逻辑，这些逻辑会影响手持设备、物联网、网络，或者在某些情况下影响 ICS 设备。” “存储区域网络 (SAN)、网络附加存储 (NAS) 和专用 RAID 阵列等设备现在也受到 AcidPour 的影响。”

Hegel 说，AcidPour 的另一个新功能是自删除功能，可以从其感染的系统中删除恶意软件的所有痕迹。他说，总体而言，AcidPour 是一个比 AcidRain 更复杂的擦拭器，并指出后者过度使用进程分叉和无端重复某些操作，作为其整体草率的例子。

SentinelOne 于 2022 年 2 月发现 AcidRain，此前一次网络攻击导致与通信提供商 Viasat 的 KA-SAT 网络相关的约 10,000 个卫星调制解调器离线。这次攻击中断了乌克兰数千名客户和欧洲数万人的消费者宽带服务。 SentinelOne 得出的结论是，该恶意软件很可能是与 Sandworm（又名 APT 28、Fancy Bear 和 Sofacy）相关的组织所为，Sandworm 是俄罗斯的一个组织，对乌克兰发生的多起破坏性网络攻击负有责任。

SentinelOne 研究人员于 3 月 16 日首次发现新变种 AcidPour，但尚未观察到有人在实际攻击中使用它。

**沙虫领带**

他们对雨刮器的初步分析揭示了与 AcidRain 的多种相似之处，随后的深入研究证实了这一点。 SentinelOne 发现的显着重叠包括 AcidPour 使用与 AcidRain 相同的重启机制，以及相同的递归目录擦除逻辑。

SentinelOne 还发现 AcidPour 基于 IOCTL 的擦除机制与 AcidRain 和 VPNFilter 中的擦除机制相同，VPNFilter 是美国司法部与 Sandworm 关联的模块化攻击平台。 IOCTL 是一种通过向设备发送特定命令来安全地擦除或擦除存储设备中的数据的机制。

SentinelOne 表示：“AcidPour 最有趣的方面之一是它的编码风格，让人想起广泛用于针对乌克兰目标的实用CaddyWiper以及Industroyer 2等著名恶意软件。” CaddyWiper 和 Industroyer 2 都是俄罗斯支持的国家组织在俄罗斯 2022 年 2 月入侵乌克兰之前就使用的恶意软件，对乌克兰的组织进行破坏性攻击。

SentinelOne 表示，乌克兰 CERT 分析了 AcidPour，并将其归因于 UAC-0165，UAC-0165 是 Sandworm 组织的一部分。

AcidPour 和 AcidRain 是俄罗斯行为者近年来针对乌克兰目标部署的众多擦拭器之一，尤其是在两国之间当前战争爆发之后。尽管威胁行为者在 Viasat 攻击中设法使数千个调制解调器离线，但该公司在删除恶意软件后仍能够恢复并重新部署它们。

然而，在许多其他情况下，组织在擦除器攻击后被迫丢弃系统。最引人注目的例子之一是 2012 年针对沙特阿美公司的Shamoon擦除器攻击，导致该公司约 30,000 个系统瘫痪。

与 Shamoon 和 AcidRain 的情况一样，威胁行为者通常不需要使雨刮器变得复杂就能发挥作用。这是因为恶意软件的唯一功能是覆盖或删除系统中的数据并使它们变得无用，因此不需要与数据盗窃和网络间谍攻击相关的规避策略和混淆技术。

针对擦除器的最佳防御措施（或限制其造成的损害）是实施与勒索软件相同的防御措施。这意味着对关键数据进行备份并确保强大的事件响应计划和能力。

网络分段也很关键，因为当擦拭器能够传播到其他系统时，它们会更加有效，因此这种类型的防御态势有助于阻止横向移动。

本文翻译自 [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/russian-apt-releases-more-deadly-variant-of-acidrain-wiper-malware)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294276](/post/id/294276)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/russian-apt-releases-more-deadly-variant-of-acidrain-wiper-malware>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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