---
title: 新版 macOS.ZuRu 木马伪装为 Termius 应用渗透系统
url: https://www.anquanke.com/post/id/309897
source: 安全客-有思想的安全新媒体
date: 2025-07-12
fetch_date: 2025-10-06T23:16:30.165354
---

# 新版 macOS.ZuRu 木马伪装为 Termius 应用渗透系统

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

# 新版 macOS.ZuRu 木马伪装为 Termius 应用渗透系统

阅读量**79177**

发布时间 : 2025-07-11 16:13:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/new-macos-zuru-variant-uses-trojanized-termius-app-to-infiltrate-systems/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种新发现的macOS.ZuRu恶意软件变种正在通过被篡改的Termius应用——一款流行的跨平台SSH和服务器管理工具——渗透macOS系统。根据SentinelOne的研究，这次攻击活动标志着该恶意软件在传播和后期利用策略方面的重大技术演进，结合了定制的Khepri command-and-control (C2) beacon，具备高度持久性、隐蔽性和远程控制能力。

ZuRu的攻击活动首次曝光是在2021年7月，当时用户在百度搜索像iTerm2这样的macOS应用时被重定向到恶意版本。自那时以来，恶意软件通过篡改广泛使用的后端工具，如Navicat、SecureCRT和微软的Mac版远程桌面，扩展了其传播范围。

SentinelOne指出：“被篡改的应用选择表明，恶意软件作者的目标是那些使用后端工具进行SSH和其他远程连接的用户。”

如今，在2025年5月，研究人员发现了一个恶意的Termius磁盘映像文件（.dmg），其大小比正版版本大约多出23MB，里面包含了两个额外的可执行文件——.localized和.Termius Helper1——它们触发了恶意软件的感染链。

![]()

正版Termius（上）与被篡改版本（下），后者包含两个额外的二进制文件 | 图片来源：SentinelOne

与之前通过注入恶意.dylib文件到应用程序包中的变种不同，这个版本通过替换Termius Helper.app为一个修改过的二进制文件来传播恶意软件。执行时，.localized会在后台启动，下载并部署来自download.termius[.]info的Khepri beacon，并将其存储在/tmp/.fseventsd中。

“攻击者已将开发者的代码签名替换为他们自己的临时签名，以绕过macOS的代码签名规则。”

该恶意软件会静默请求提升权限，安装一个用于持久性的LaunchDaemon（com.apple.xssooxxagent），并确保通过以下方式每小时执行一次：

```
launchctl bootout system/com.apple.xssooxxagent;
launchctl bootstrap system/com.apple.xssooxxagent;
```

该植入物还会将自身复制到/Users/Shared，并使用已废弃的macOS API进行权限提升。

第二阶段的有效负载——通过自定义的XOR加减解密例程下载并验证——是一个修改过的Khepri C2 beacon。该版本首次出现在2024年12月，专为macOS Sonoma 14.1及更高版本量身定制，表明其主要针对最新的系统。

SentinelOne将Khepri描述为“一款功能齐全的C2植入物，具备文件传输、系统侦察、进程控制和命令执行等功能。”

值得注意的是，该beacon具备以下功能：

* 支持-s和-bd标志，用于隐蔽性和后台守护进程模式。
* 通过53端口进行通信（通常用于DNS）。
* 使用www.baidu[.]com作为诱饵域名，实际连接到ctl01.termius[.]fun，解析到阿里云的IP地址。
* 信标的心跳间隔设置为5秒，比开源版本Khepri的默认10秒更快。

研究人员还强调了残留的功能，如\_startBackgroundProcess()和\_startLaunchDaemon()，这些功能模仿或重复了现有的功能，可能是早期版本的残留或复用的源代码。

报告指出：“该二进制文件中的工件可能表明恶意软件的源代码可能被用于早期的攻击活动。”

本文翻译自securityonline [原文链接](https://securityonline.info/new-macos-zuru-variant-uses-trojanized-termius-app-to-infiltrate-systems/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309897](/post/id/309897)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-macos-zuru-variant-uses-trojanized-termius-app-to-infiltrate-systems/)

如若转载,请注明出处： <https://securityonline.info/new-macos-zuru-variant-uses-trojanized-termius-app-to-infiltrate-systems/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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