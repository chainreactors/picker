---
title: 恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险
url: https://www.anquanke.com/post/id/308238
source: 安全客-有思想的安全新媒体
date: 2025-06-10
fetch_date: 2025-10-06T22:54:02.386336
---

# 恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险

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

# 恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险

阅读量**129691**

发布时间 : 2025-06-09 17:01:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 肖恩，文章来源：securitybrief

原文地址：<https://securitybrief.asia/story/malware-hits-16-react-native-npm-packages-1m-downloads-at-risk>

译文仅供参考，具体内容表达以及含义原文为准。

合气道安全已经确定了影响npm注册表上16个React Native包的活跃供应链攻击,估计每周有100万次下载共同面临风险。

攻击被追踪到负责之前的rand-user-agent妥协的同一威胁行为者,该活动扩展到针对采用JavaScript技术的主要企业使用的广泛使用的React Native组件。折衷方案始于2025年6月6日晚,从@react-native-aria/focus包开始,仅每周就有10万次下载。

根据合气道安全提供的时间表,攻击分几个阶段展开。6月6日格林尼治标准时间21:43+0,攻击者突破了@react-native-aria/focus(版本0.2.10)。在接下来的几个小时里,6月7日00:37至00:48之间又有8个包裹被泄露。当天格林尼治标准时间14:28至14:46 + 0之间检测到进一步的入侵,影响了另外7个包裹,包括@gluestack-ui/utils。到6月8日01时22分,所有受损的包裹都被各自的维护者标记为弃用。

总体而言,受影响的软件包每周从全球开发人员和企业获得约100万次下载。这种影响规模凸显了事件的严重性,引发了整个软件供应链社区的重大担忧。

通过这些受感染的软件包传递的恶意软件是远程访问木马(RAT),该木马装备可以在受感染的机器上执行任意shell命令,上传和下载文件,并通过%LOCALAPPDATA%\Programs\Python\Python3127文件夹在Windows环境中保持持久性。RAT与命令和控制服务器通信,价格为136.09[.]8和85.239.62[.]36,允许攻击者持续访问受感染的系统。

合气道安全的技术分析显示,在恶意代码中使用基于空白的混淆技术,旨在通过将有害脚本从屏幕外推送来隐藏其在标准代码编辑器中的存在。持久性机制是攻击的一个关键方面,即使维护人员推送旨在解决安全漏洞的软件包更新,恶意软件也能保留在系统上。

合气道安全公司(Aikido Security)的恶意软件研究员查理·埃里克森(Charlie Eriksen)评论说:“看到这个威胁行为者在短短几周内就在npm上妥协了几个重要的软件包,这令人担忧。根据我们的数据,受损的软件包非常受欢迎,并且被许多大企业使用。这种违规行为的范围和规模很难低估。

他进一步强调了这个问题的紧迫性:“关于这个故事有很多话要说,但考虑到攻击的严重性,我们希望尽快提高对它的认识,以便人们可以保护自己。这些攻击者一直表现出妥协包的能力,部署他们的远程访问木马(RAT)。

埃里克森还谈到了妥协的时机,他说:“一方面,这发生在周五晚上,在世界大部分地区的营业时间之后,这是不幸的。然而,它也减少了影响,因为大多数人都在享受周末。在这样的情况下,补救时间至关重要 。 ”

即使在包裹更新之后,攻击者仍能保持持久性,从而促进各种攻击路径,包括非法加密货币挖掘,拒绝服务活动,窃取凭据和敏感数据,以及通过受影响组织网络的潜在横向移动。

受影响的软件包的完整列表包括:@react-native-aria/focus(0.2.10),@react-native-aria/utils(0.2.13),@react-native-aria/overlays(0.316),@react-native-aria/interactions(0.2.17),@react-native-aria/toggle(0.2.12),@react-native-aria/swict.

鉴于该漏洞,合气道安全建议组织在使用任何受影响的软件包版本时立即采取几个步骤。首先,建议他们检查防火墙日志,以查找试图到达指定命令和控制服务器的连接。其次,管理员应该检查Windows上Python安装目录中的持久化文件系统。第三,合气道建议将所有具有这些包的系统视为可能受到损害,并采取适当步骤,例如凭据轮换和对访问控制进行审计。

本文翻译自securitybrief [原文链接](https://securitybrief.asia/story/malware-hits-16-react-native-npm-packages-1m-downloads-at-risk)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308238](/post/id/308238)

安全KER - 有思想的安全新媒体

本文转载自: [securitybrief](https://securitybrief.asia/story/malware-hits-16-react-native-npm-packages-1m-downloads-at-risk)

如若转载,请注明出处： <https://securitybrief.asia/story/malware-hits-16-react-native-npm-packages-1m-downloads-at-risk>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全活动](/tag/%E5%AE%89%E5%85%A8%E6%B4%BB%E5%8A%A8)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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