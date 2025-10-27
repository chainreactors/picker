---
title: 微软：朝鲜威胁者部署新型 FakePenny 勒索软件
url: https://www.anquanke.com/post/id/296942
source: 安全客-有思想的安全新媒体
date: 2024-05-31
fetch_date: 2025-10-06T16:49:27.588096
---

# 微软：朝鲜威胁者部署新型 FakePenny 勒索软件

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

# 微软：朝鲜威胁者部署新型 FakePenny 勒索软件

阅读量**141837**

发布时间 : 2024-05-30 12:00:21

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/north-korea-deploying-fakepenny-ransomware/>

译文仅供参考，具体内容表达以及含义原文为准。

微软发现朝鲜威胁行为者部署了一种新的“FakePenny”勒索软件变种，其目标是软件、信息技术、教育和国防工业基础领域的组织，以进行间谍活动和获取金钱利益。

该威胁行为者被微软追踪为 Moonstone Sleet，它于 4 月份首次被发现向一家未公开的公司发送了一种新的定制勒索软件变种，几个月前该软件入侵了该公司的网络。

该勒索软件非常简单，包含一个加载器和一个加密器模块。朝鲜威胁行为者团体以前曾开发过此类定制勒索软件，但“这是我们第一次观察到该威胁行为者部署勒索软件，”该科技巨头表示。

**“微软评估 Moonstone Sleet 部署勒索软件的目的是为了获取经济利益，这表明该行为者开展网络行动既是为了收集情报，也是为了创造收入。”**

FakePenny 勒索软件要求的赎金数额极高，最近的要求高达 660 万美元的比特币。微软表示：“这与之前朝鲜勒索软件攻击（如 WannaCry 2.0 和 H0lyGh0st ）的较低赎金要求形成了鲜明对比。”

值得注意的是，FakePenny 勒索软件使用的赎金通知与臭名昭著的 NotPetya 勒索软件攻击中使用的通知非常相似，后者是由朝鲜组织 Seashell Blizzard 发起的。这种策略的连续性凸显了朝鲜网络行动的相互关联性。

### Moonstone Sleet 的战略和谍战技巧

Moonstone Sleet 拥有多种多样的行动来支持其财务和间谍目标。据观察，该组织创建虚假公司、使用合法工具的木马版本，甚至开发恶意游戏来渗透目标。他们同时进行操作以及快速发展和调整技术的能力引人注目。

如前所述，威​​胁行为者掌握了几种不同的技巧。2023 年 8 月初，Moonstone Sleet 通过 LinkedIn、Telegram 和自由职业网站等平台提供了开源终端仿真器 PuTTY 的受感染版本。当用户提供威胁行为者发送的恶意 Zip 文件中的文本文档中提到的 IP 和密码时，木马软件会解密并执行嵌入的恶意软件。另一名朝鲜行为者 Diamond Sleet 也使用了同样的技巧。

Moonstone Sleet 还利用通过自由职业网站和社交媒体分发的恶意“npm”软件包攻击受害者。这些软件包通常伪装成技术评估，执行后会导致额外的恶意软件下载。

自 2024 年 2 月以来，Moonstone Sleet 还采取了不同的方法，使用名为 DeTankWar 的恶意游戏来感染设备。该组织冒充游戏开发商或虚假公司接触目标，将该游戏伪装成区块链项目。启动游戏后，会加载其他恶意 DLL，执行名为“YouieLoad”的自定义恶意软件加载程序。此加载程序执行网络和用户发现以及浏览器数据收集。

### 虚假公司和雇佣工作计划

自 2024 年 1 月以来，Moonstone Sleet 创建了多家虚假公司，包括 StarGlow Ventures 和 CC Waterfall，以欺骗目标。这些公司冒充软件开发和 IT 服务公司，通常与区块链和人工智能有关，以建立信任并获得组织的访问权限。

Moonstone Sleet 还寻求在合法公司工作的机会，这与朝鲜利用远程 IT 员工创造收入的报道一致。最近，美国指控朝鲜存在就业欺诈团伙，该团伙正在筹集资金支持其核计划。该团伙诈骗了 300 多家美国公司，累计诈骗金额至少 680 万美元。

这种雇佣策略还可以为未经授权访问组织提供另一种途径。

Moonstone Sleet 发起的著名攻击包括入侵一家国防科技公司以窃取凭证和知识产权，以及针对一家无人机技术公司部署勒索软件。

“尽管 Moonstone Sleet 是一个新兴组织，但它已证明自己将继续成熟、发展和演变，并将自己定位为代表朝鲜政权进行复杂攻击的卓越威胁行为者。”

### 防御Moonstone Sleet

为了防御 Moonstone Sleet，微软建议使用端点检测和响应 (EDR)，实施攻击面减少规则以阻止来自电子邮件客户端和网络邮件的可执行内容，防止可执行文件运行（除非它们满足特定条件），使用高级保护措施防范勒索软件，并阻止从 LSASS 窃取凭据。

本文翻译自 [原文链接](https://thecyberexpress.com/north-korea-deploying-fakepenny-ransomware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296942](/post/id/296942)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/north-korea-deploying-fakepenny-ransomware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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