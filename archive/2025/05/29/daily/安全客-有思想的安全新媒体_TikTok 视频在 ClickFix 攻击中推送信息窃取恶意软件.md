---
title: TikTok 视频在 ClickFix 攻击中推送信息窃取恶意软件
url: https://www.anquanke.com/post/id/307915
source: 安全客-有思想的安全新媒体
date: 2025-05-29
fetch_date: 2025-10-06T22:25:27.814423
---

# TikTok 视频在 ClickFix 攻击中推送信息窃取恶意软件

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

# TikTok 视频在 ClickFix 攻击中推送信息窃取恶意软件

阅读量**155562**

发布时间 : 2025-05-28 14:05:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/tiktok-videos-now-push-infostealer-malware-in-clickfix-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![TikTok]()

网络犯罪分子正在使用TikTok视频欺骗用户在ClickFix攻击中使用Vidar和StealC信息窃取恶意软件感染自己。

正如Trend Micro最近发现的那样,TikTok社交工程活动背后的威胁行为者正在使用可能使用AI生成的视频,这些视频要求观众运行声称激活Windows和Microsoft Office的命令,以及CapCut和Spotify等各种合法软件中的高级功能。

“这种攻击使用视频(可能是AI生成的)来指示用户执行PowerShell命令,这些命令伪装成软件激活步骤。TikTok的算法覆盖增加了广泛曝光的可能性,一个视频的观看次数超过50万 [, ” Trend Micro说。](https://www.trendmicro.com/en_us/research/25/e/tiktok-videos-infostealers.html)

“视频非常相似,相机角度和PowerShell用于获取有效载荷的下载URL只有细微的差异,”它补充说。

“这表明这些视频可能是通过自动化创建的。教学语音也出现在AI生成的,这加强了AI工具被用于制作这些视频的可能性。

其中一个视频声称提供了如何“立即提升你的Spotify体验”的说明,已经达到了近50万次观看,超过20,000次点赞和100多条评论。

![TikTok ClickFix 视频]()

在视频中,攻击者会提示观众运行 PowerShell 命令,该命令将从 *hxxps://allaivo[.]me/spotify* 下载并执行远程脚本,该脚本安装 Vidar 或 StealC 信息窃取恶意软件,将其作为具有更高权限的隐藏进程启动。

部署后[,](https://www.bleepingcomputer.com/tag/vidar/)Vidar可以截取桌面屏幕截图并窃取凭据,信用卡,Cookie,加密货币钱包,文本文件和Authy 2FA身份验证器数据库。

StealcStealc还可以从受感染的计算机中获取各种敏感信息,因为它针对数十个Web浏览器和加密货币钱包。

设备被破坏后,脚本将从 *hxxps://amssh[.]co/script[.]ps1* 下载第二个 PowerShell 脚本有效载荷,该脚本将添加一个注册表项以自动启动时启动。

![攻击流]()

### 什么是ClickFix?

ClickFixClickFix是一种策略,攻击者使用虚假错误或验证系统(如CAPTCHA提示)来欺骗潜在目标运行恶意脚本以在其设备上下载和安装恶意软件。

虽然通常通过PowerShell命令针对Windows用户,usersmacOSLinux但ClickFix也被采用用于攻击macOS和Linux用户。

国家支持的威胁组织也在类似的攻击中入侵了目标,最近几个月,APT28和ColdRiver(俄罗斯),Kimsuky(朝鲜)和MuddyWater(伊朗)[都在间谍活动中使用了这些策略。](https://www.bleepingcomputer.com/news/security/state-sponsored-hackers-embrace-clickfix-social-engineering-tactic/)

这不是TikTok视频第一次被用来推动恶意软件,网络犯罪分子利用名为“隐形挑战”的TikTok趋势挑战,[用安装WASP Stealer(Discord Token Grabber)](https://medium.com/checkmarx-security/wasp-attack-on-python-polymorphic-malware-shipping-wasp-stealer-infecting-hundreds-of-victims-10e92439d192)恶意软件的假应用程序感染数千人。

该恶意软件在发布后不久就通过视频推送,该视频获得了超过一百万的观看次数,并可以窃取Discord帐户,密码,信用卡和加密货币钱包。

近年来,诈骗者也充斥着TikTok的虚假加密货币赠品,几乎都使用埃隆·马斯克(Elon Musk),特斯拉(Tesla)或SpaceX主题。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/tiktok-videos-now-push-infostealer-malware-in-clickfix-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307915](/post/id/307915)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/tiktok-videos-now-push-infostealer-malware-in-clickfix-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/tiktok-videos-now-push-infostealer-malware-in-clickfix-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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