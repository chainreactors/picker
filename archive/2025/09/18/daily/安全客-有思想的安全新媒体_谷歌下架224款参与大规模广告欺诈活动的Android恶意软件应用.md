---
title: 谷歌下架224款参与大规模广告欺诈活动的Android恶意软件应用
url: https://www.anquanke.com/post/id/312185
source: 安全客-有思想的安全新媒体
date: 2025-09-18
fetch_date: 2025-10-02T20:17:22.026646
---

# 谷歌下架224款参与大规模广告欺诈活动的Android恶意软件应用

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

# 谷歌下架224款参与大规模广告欺诈活动的Android恶意软件应用

阅读量**77312**

发布时间 : 2025-09-17 17:37:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/google-nukes-224-android-malware-apps-behind-massive-ad-fraud-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场名为“SlopAds”的大规模Android广告欺诈行动被挫败——Google Play商店中的224款恶意应用每日产生**23亿次广告请求**。

该欺诈活动由HUMAN的Satori威胁情报团队发现，这些应用累计下载量超**3800万次**，并通过**混淆和隐写术**隐藏恶意行为，以规避谷歌和安全工具的检测。活动波及全球228个国家，每日广告竞价请求达23亿次，其中广告曝光量最高的地区为美国（30%）、印度（10%）和巴西（7%）。

HUMAN解释：“研究人员将此行动命名为‘SlopAds’，因其关联应用看似‘AI粗制滥造’的量产产品，同时暗指威胁 actors 控制服务器上托管的一系列AI主题应用和服务。”

![]()

### **SlopAds广告欺诈活动细节**

该欺诈活动采用**多层规避策略**，以绕过谷歌应用审核流程和安全软件检测：

若用户通过Play商店自然安装SlopAds应用（非通过攻击者广告渠道），应用会表现为正常功能软件，执行宣传的功能。

![]()

但如果检测到用户是通过攻击者广告点击安装，应用会利用**Firebase Remote Config**下载加密配置文件，内含广告欺诈模块、变现服务器的URL及JavaScript载荷。

随后，应用会判断自身是否运行在真实用户设备上（而非研究人员或安全软件的分析环境）。通过检测后，它会下载**4个含隐写术的PNG图像**，其中隐藏恶意APK的碎片——这些碎片在设备上解密重组后，形成完整的“FatModule”恶意软件，用于实施广告欺诈。

![]()

### **欺诈执行：隐藏WebView与虚假流量**

FatModule激活后，会通过**隐藏WebView**收集设备和浏览器信息，随后导航至攻击者控制的欺诈变现域名。这些域名伪装成游戏或新闻网站，通过隐藏WebView界面持续加载广告，每日产生**超20亿次欺诈性广告曝光和点击**，为攻击者创造收益。

### **基础设施与后续威胁**

HUMAN指出，该活动基础设施包含多个命令与控制服务器及**300多个相关推广域名**，表明威胁 actors 计划在224款已识别应用之外进一步扩张。

谷歌已从Play商店下架所有已知SlopAds应用，Android的Google Play Protect也已更新，提示用户卸载设备上的残留应用。但HUMAN警告，此类广告欺诈活动的复杂性意味着攻击者可能调整策略，在未来发起新一轮攻击。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/google-nukes-224-android-malware-apps-behind-massive-ad-fraud-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312185](/post/id/312185)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/google-nukes-224-android-malware-apps-behind-massive-ad-fraud-campaign/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/google-nukes-224-android-malware-apps-behind-massive-ad-fraud-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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