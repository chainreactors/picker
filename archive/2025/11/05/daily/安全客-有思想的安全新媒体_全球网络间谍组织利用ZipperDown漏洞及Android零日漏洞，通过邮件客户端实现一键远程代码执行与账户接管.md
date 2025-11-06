---
title: 全球网络间谍组织利用ZipperDown漏洞及Android零日漏洞，通过邮件客户端实现一键远程代码执行与账户接管
url: https://www.anquanke.com/post/id/313018
source: 安全客-有思想的安全新媒体
date: 2025-11-05
fetch_date: 2025-11-06T03:12:24.037124
---

# 全球网络间谍组织利用ZipperDown漏洞及Android零日漏洞，通过邮件客户端实现一键远程代码执行与账户接管

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

# 全球网络间谍组织利用ZipperDown漏洞及Android零日漏洞，通过邮件客户端实现一键远程代码执行与账户接管

阅读量**23154**

发布时间 : 2025-11-05 17:53:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/global-spies-use-zipperdown-and-android-zero-days-for-1-click-email-client-rce-and-account-takeover/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

奇安信威胁情报中心RedDrip团队发布新报告，详细披露了一系列**持续多年的零日漏洞利用活动**—针对桌面和Android环境实施**高度复杂的间谍行动**。

报告指出，攻击者的活动“远不止于端点层面”，并强调他们“捕获了多个针对Android邮件客户端的0-day攻击，技术水平已达**1-click（一键触发）**，且攻击者很可能已掌握类似‘Triangulation’的**0-click（零交互）能力**”。

尽管仅有少数零日漏洞（影响Internet Explorer、Firefox、Foxmail和WPS Office）被用于攻击政府和企业目标

### **ZipperDown漏洞：全球首次公开的在野利用**

报告最引人注目的发现之一是**ZipperDown漏洞的首次已知在野利用**——该漏洞最初由盘古实验室于2018年发现。“2018年至今，尚无公开报告显示APT组织在野外利用过该漏洞，”RedDrip团队指出，“RedDrip团队是全球首个披露ZipperDown漏洞被APT组织在野利用的安全团队。”

在这类攻击中，攻击者向Android设备发送包含恶意附件的特制邮件。当目标“在手机上点击邮件时，ZipperDown漏洞立即触发，解压精心构造的DAT文件并释放恶意SO和APK文件，覆盖目标应用组件。”

这些载荷常伪装成朝鲜《劳动新闻》的政治新闻，诱使受害者交互。

### **载荷演变：从图像处理漏洞到内存加载恶意APK**

RedDrip分析详细阐述了载荷随时间的变化：

#### **2022–2023年载荷**：

攻击者利用Android邮件应用中IMG图像处理的逻辑缺陷部署后门。恶意SO文件是**libttmplayer\_lite.so 的篡改版本**，保留正常功能的同时嵌入下载器逻辑，从命令与控制（C2）服务器获取进一步指令。

#### **2024–2025年载荷**：

武器化模块演变为**libpanglearmor.so** ，可“从远程服务器下载APK木马并加载到内存”。恶意软件通过`com.example.backservice.MainActivity` 执行后台任务，定期“从‘/command’获取命令并将结果发送至/result”，同时“上报设备连接的WIFI信息”。

命令功能包括：列出文件、执行任意进程、获取已安装应用、建立反向shell及数据窃取。

### **Android邮件客户端代码注入漏洞：无密码账户接管**

2024年，RedDrip在一款流行Android邮件客户端中发现另一个**代码注入漏洞**。该漏洞仅需**点击一次**即可触发——打开包含四个特制IMG标签的恶意邮件，标签会将JavaScript插入邮件正文。

攻击者滥用名为`localfile`的**未公开内部API参数**，实现任意文件读取（如`/data/data/…/databases/`路径），窃取账户令牌和配置文件。

RedDrip观察到：“攻击者请求两个文件……解析相关数据后获取目标账户令牌”，随后窃取应用XML配置文件，其中包含“账户配置信息，包括各类密钥”。

这使得攻击者能够**无密码接管账户**：“最终窃取用户登录状态，无需密码操作账户，访问所有邮件、联系人、文件及其他敏感数据。”

本文翻译自securityonline [原文链接](https://securityonline.info/global-spies-use-zipperdown-and-android-zero-days-for-1-click-email-client-rce-and-account-takeover/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313018](/post/id/313018)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/global-spies-use-zipperdown-and-android-zero-days-for-1-click-email-client-rce-and-account-takeover/)

如若转载,请注明出处： <https://securityonline.info/global-spies-use-zipperdown-and-android-zero-days-for-1-click-email-client-rce-and-account-takeover/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **653**

* 粉丝
* **6**

### TA的文章

* ##### [一文读懂香港金融科技周：DART将带领香港金融科技驶向何方？](/post/id/313039)

  2025-11-05 18:35:34
* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59

### 相关文章

* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59
* ##### [React Native CLI 中存在严重漏洞（CVE-2025-11953，CVSS 9.8），攻击者可经由暴露的Metro开发服务器实现RCE](/post/id/313021)

  2025-11-05 17:53:18
* ##### [Bugcrowd收购自动化测试工具Mayhem，以强化其应用安全测试平台能力](/post/id/313024)

  2025-11-05 17:52:48
* ##### [Open VSX扩展市场中出现新型“SleepyDck”恶意软件，允许攻击者远程控制Windows系统](/post/id/313027)

  2025-11-05 17:52:17

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