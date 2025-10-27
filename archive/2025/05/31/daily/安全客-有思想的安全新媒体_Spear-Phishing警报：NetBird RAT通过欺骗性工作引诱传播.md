---
title: Spear-Phishing警报：NetBird RAT通过欺骗性工作引诱传播
url: https://www.anquanke.com/post/id/307997
source: 安全客-有思想的安全新媒体
date: 2025-05-31
fetch_date: 2025-10-06T22:24:49.910797
---

# Spear-Phishing警报：NetBird RAT通过欺骗性工作引诱传播

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

# Spear-Phishing警报：NetBird RAT通过欺骗性工作引诱传播

阅读量**152656**

发布时间 : 2025-05-30 16:44:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/spear-phishing-alert-netbird-rat-spreads-via-deceptive-job-lures/>

译文仅供参考，具体内容表达以及含义原文为准。

![NetBird 网络钓鱼 spear-phishing 活动]()

攻击流 | 图片: Trellix

Trellix的高级研究中心发现了一项针对欧洲、非洲、中东、加拿大和南亚金融高管的高度针对性和隐秘的鱼叉式网络钓鱼活动。攻击者的目标?欺骗受害者在罗斯柴尔德公司(Rothschild&Co.)的职业机会的幌子下安装NetBird,这是一个合法的基于WireGuard的远程访问工具。

网络钓鱼操作将巧妙的社交工程与规避策略相结合,例如Firebase托管,基于JavaScript的自定义CAPTCHA和分阶段的VBS下载器,有效地绕过了许多标准电子邮件和网络防御。

最初的网络钓鱼电子邮件是精心制作的,以冒充罗斯柴尔德公司的招聘人员,并在财务领导方面提供了一个诱人的“战略机会”。而不是真正的PDF,附加的小册子是一个Firebase托管的网页伪装成一个文件。

*“附加的’brochure’不是PDF,而是隐藏在数学测验自定义CAPTCHA后面的Firebase托管页面。*

一旦受害者解决了CAPTCHA,它们就会被重定向到一个提供ZIP存档的网站——Rothschild\_&\_Co-6745763.zip——其中包含启动恶意软件安装链的VBS脚本。

执行后,VBS 脚本默默地下载一个辅助 VBS 有效载荷:

1. 通过 MSI 文件安装 NetBird 和 OpenSSH。
2. 创建一个隐藏的本地管理员帐户(用户/Bs@202122)。
3. 启用 RDP 访问,配置防火墙规则,并将 NetBird 设置为自动启动。
4. 删除桌面快捷方式以避免检测。

*“该脚本创建一个隐藏的本地帐户……在打开防火墙时在远程桌面上翻转……并删除任何NetBird桌面快捷方式*,”报告解释说。

这导致通过加密渠道进行持久性和远程访问,这是横向移动和潜在数据泄漏的理想立足点。

钓鱼页面托管在Firebase和其他Google托管的应用程序平台上,使它们看起来值得信赖。他们使用自定义的基于JavaScript的CAPTCHA,在用户交互时解密隐藏的重定向URL,绕过传统的检测机制。

*“攻击者越来越依赖这些定制的CAPTCHA门,希望通过防御*,”报告警告说。

Trellix指出,这些策略模仿或与以前的民族国家网络钓鱼操作重叠,尽管在撰写本文时尚未做出归因。

Trellix的研究人员发现,类似的基础设施在旧活动中重复使用。值得注意的是,一个模仿SharePoint的旧页面仍然提供相同的VBS有效载荷,这表明更广泛的操作可能重复使用工具包和托管设置。

*“该页面仍然有效……它提供ZIP……存档会丢弃当前战役中看到的相同的VBS有效载荷*,”报告指出。

法国的Autorité des marchés金融家(AMF)最近也警告过网络钓鱼攻击冒充该组织。Trellix证实国际奥委会与他们目前的发现重叠,尽管诱惑有所不同。

组织应监控 Firebase 和 WebApp 托管,仔细检查 CAPTCHA 行为,并阻止端点的可疑 MSI 和 VBS 执行流程。

本文翻译自securityonline [原文链接](https://securityonline.info/spear-phishing-alert-netbird-rat-spreads-via-deceptive-job-lures/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307997](/post/id/307997)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/spear-phishing-alert-netbird-rat-spreads-via-deceptive-job-lures/)

如若转载,请注明出处： <https://securityonline.info/spear-phishing-alert-netbird-rat-spreads-via-deceptive-job-lures/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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