---
title: 鱼叉式网络钓鱼活动锁定企业CFO， 复杂多阶段攻击链浮出水面
url: https://www.anquanke.com/post/id/311405
source: 安全客-有思想的安全新媒体
date: 2025-08-23
fetch_date: 2025-10-07T00:17:50.840077
---

# 鱼叉式网络钓鱼活动锁定企业CFO， 复杂多阶段攻击链浮出水面

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

# 鱼叉式网络钓鱼活动锁定企业CFO， 复杂多阶段攻击链浮出水面

阅读量**76043**

发布时间 : 2025-08-22 17:18:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/spear-phishing-campaign-targets-cfos-with-sophisticated-multi-stage-intrusion/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

亨特智库最新研究报告揭露，一场**高度定向的鱼叉式网络钓鱼活动**正在全球范围内系统性针对企业首席财务官（CFO）及财务高管。该攻击活动融合**社会工程学**、**多阶段恶意软件投递**及**合法远程工具滥用**等手段，实现对受害者环境的持久控制。

攻击始于冒充罗斯柴尔德公司招聘人员的欺诈邮件，将受害者引导至托管于Firebase平台的钓鱼页面。这些页面采用**定制化验证码挑战机制**，既增强可信度又有效规避自动化检测。亨特智库指出：”攻击始于伪装成罗斯柴尔德招聘人员的社会工程学邮件，最终指向带有自定义验证码的Firebase钓鱼页面。”

目标对象一旦交互，就会被诱导下载包含恶意VBScript文件（VBS）的ZIP压缩包。该脚本执行后会静默安装NetBird和OpenSSH，创建隐藏管理员账户并启用远程桌面协议（RDP）。报告强调该**多阶段感染链**的复杂性：初始VBS下载器会从攻击者控制的基础设施获取后续载荷。研究人员发现：”提取的`F-144822.vbs`文件包含恶意脚本，从指定地址下载额外载荷，将其保存为`C:\bin\cis.vbs`后通过隐藏窗口提权执行。”

后续载荷会部署NetBird隧道、调整防火墙规则并配置RDP服务实现持久化。攻击者还通过**删除桌面快捷方式**和**自动化服务重启**来消除痕迹，确保隐蔽存在。报告显示：”最终阶段脚本确保Netbird服务随系统启动，并删除所有用户桌面的快捷方式，有效隐藏新安装软件。”

亨特调查发现，攻击基础设施横跨Firebase和Web.app域名，常使用**AES加密重定向**及法语编写的”数学关卡”验证码挑战。这些技术既掩盖钓鱼机制，又通过多样化托管路径规避封禁。值得注意的是，该基础设施与已知APT组织**MuddyWater**存在高度重叠。亨特智库确认：”与Maltrail威胁情报数据交叉比对显示，该IP地址此前就与MuddyWater活动关联，进一步强化了归因结论。”

该活动最令人警觉的是其对**合法远程访问软件的滥用**。除NetBird外，攻击者还部署了`AteraAgent.exe`——这款商业远程管理工具在既往MuddyWater相关入侵中同样被滥用。这场横跨多大陆的精准攻击以高价值财务职位为目标，其**先进的持久化技术**及**基础设施重叠特征**，暗示其背后存在资金充足且具有国家背景的威胁组织，这与历史MuddyWater行动的特征高度吻合。

本文翻译自securityonline [原文链接](https://securityonline.info/spear-phishing-campaign-targets-cfos-with-sophisticated-multi-stage-intrusion/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311405](/post/id/311405)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/spear-phishing-campaign-targets-cfos-with-sophisticated-multi-stage-intrusion/)

如若转载,请注明出处： <https://securityonline.info/spear-phishing-campaign-targets-cfos-with-sophisticated-multi-stage-intrusion/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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