---
title: 新型安卓恶意软件 GhostSpy 让攻击者完全控制受感染设备
url: https://www.anquanke.com/post/id/307895
source: 安全客-有思想的安全新媒体
date: 2025-05-29
fetch_date: 2025-10-06T22:25:32.290288
---

# 新型安卓恶意软件 GhostSpy 让攻击者完全控制受感染设备

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

# 新型安卓恶意软件 GhostSpy 让攻击者完全控制受感染设备

阅读量**110466**

发布时间 : 2025-05-28 13:30:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-android-malware-ghostspy/>

译文仅供参考，具体内容表达以及含义原文为准。

一种名为GhostSpy的复杂新的Android恶意软件菌株已成为对移动设备安全的重大威胁,展示了先进的功能,使网络犯罪分子能够完全控制受感染的智能手机和平板电脑。

这个基于Web的远程访问木马(RAT)采用多阶段感染过程,从看似无害的滴管应用程序开始,该应用程序无声地升级特权并部署旨在建立持久监视和控制功能的二级有效载荷。

该恶意软件代表了移动威胁的演变,利用先进的规避技术,自动权限处理和复杂的反卸载机制来维护对受害者设备的长期访问。

[GhostSpy的攻击向量通常涉及社会工程策略](https://cybersecuritynews.com/social-engineering/),将自己呈现为合法的应用程序更新或系统实用程序,以欺骗用户安装。

一旦建立,恶意软件利用Android的辅助功能和服务和设备管理员API来绕过安全限制,并在用户不知情的情况下授予自己广泛的权限。

Cyfirma分析师在持续的威胁监控活动中发现了这种高风险的Android恶意软件变体,并指出其监视功能和持久性机制的特别危险组合。

研究小组的分析显示,GhostSpy可以执行全面的数据盗窃,包括键盘记录,屏幕捕获,背景音频和视频录制,短信和通话记录提取,GPS位置跟踪和远程命令执行。

也许最令人担忧的是恶意软件能够绕过银行应用程序屏幕截图保护,使用骨架视图重建方法,从所谓的安全应用程序中获取完整的UI布局。

恶意软件的运营商基础设施表明巴西血统,多个有源的命令和控制服务器托管在不同位置,并支持多种语言,包括葡萄牙语,英语和西班牙语。

这个国际范围表明GhostSpy积极维护并分布在各个地区,主C2服务器位于cheltic.gstpainel.fun和其他端点在端口3000和4200上运行。

GhostSpy特别阴险的是其全面的设备妥协方法,将传统的RAT功能与现代移动特定攻击技术相结合。

[恶意软件可以窃取银行凭证进行财务欺诈](https://cybersecuritynews.com/prudential-financial-hack/),即使在屏幕截图限制的应用程序中也捕获屏幕内容,并通过Accessibility Service滥用执行未经授权的金融交易,从而对个人隐私和财务安全构成严重威胁。

### **高级感染和特权升级机制**

GhostSpy的感染机制在其多阶段部署策略中表现出显着的复杂性。

初始 dropper 应用程序包含一个关键方法,称为`updateApp()`这是有效载荷部署的触发因素。

此方法首先检查设备的`canRequestPackageInstalls()`权限,[它决定应用程序是否可以在 Google Play](https://cybersecuritynews.com/malicious-app-in-google-play-store/) 商店限制之外侧载 APK 文件。

如果未授予此权限,恶意软件将用户秘密重定向到`MANAGE_UNKNOWN_APP_SOURCES`设置页面,专门针对当前软件包请求安装权限。

获得必要的权限后,滴管执行`copyApkFromAssets("update.apk")`从其资产文件夹中提取捆绑的二级 APK 有效载荷,然后进行`installApk()`为执行。

安装过程使用与操作的Intent`android.intent.action.VIEW`针对通过 FileProvider 生成的内容 URI,确保安装 Activity 启动具有必要的 URI 访问权限。

被识别为“com.support.litework”的辅助有效载荷通过其自动许可授予机制展示了恶意软件最危险的功能。

因`AllowPrims14_normal`方法自动点击屏幕,通过模拟可能的按钮区域的触摸,在没有用户交互的情况下授予权限。

这种复杂的技术针对最新的Android版本,并通过所有必要的权限循环,尝试从45%到90%的屏幕高度,睡眠间隔,模仿人类行为,以降低检测风险。

补充这种自动化,`getAutomaticallyPermission`方法使用 AccessibilityNodeInfo 递归地遍历 UI 层次结构,以定位和与权限对话框按钮进行交互。

它专门针对 android.widget.Button 元素,其文本与各种语言的通用权限提示相匹配,包括“允许”、“使用应用程序和“Permitir”,自动单击这些按钮。`performAction(AccessibilityNodeInfo.ACTION_CLICK)`. .

这种多语言方法展示了恶意软件的全球定位策略以及对Android在不同设备配置和语言设置中的许可模型的复杂理解。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-android-malware-ghostspy/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307895](/post/id/307895)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-android-malware-ghostspy/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-android-malware-ghostspy/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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