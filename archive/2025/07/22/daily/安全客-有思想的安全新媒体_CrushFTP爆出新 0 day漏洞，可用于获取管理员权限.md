---
title: CrushFTP爆出新 0 day漏洞，可用于获取管理员权限
url: https://www.anquanke.com/post/id/310331
source: 安全客-有思想的安全新媒体
date: 2025-07-22
fetch_date: 2025-10-06T23:16:44.559607
---

# CrushFTP爆出新 0 day漏洞，可用于获取管理员权限

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

# CrushFTP爆出新 0 day漏洞，可用于获取管理员权限

阅读量**74115**

发布时间 : 2025-07-21 17:35:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-crushftp-zero-day-exploited-in-attacks-to-hijack-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

CrushFTP近日发布安全公告，警告其产品中存在一个被命名为**CVE-2025-54309**的零日漏洞，攻击者正在积极利用该漏洞，通过Web界面在未修复的服务器上获取管理员权限。

CrushFTP是一款**企业级文件传输服务器**，广泛用于通过FTP、SFTP、HTTP/S等协议进行文件的安全共享与管理。

据CrushFTP披露，攻击行为最早于7月18日北京时间上午9点被发现，实际攻击可能始于更早的时间。

CrushFTP首席执行官Ben Spink向外媒BleepingComputer表示，该漏洞原本并未被识别，但此前一项**针对AS2功能的修复措施**“意外”屏蔽了该漏洞的利用路径。他指出：“我们此前修复了一个与HTTP(S)中AS2功能相关的问题，恰巧关闭了这个漏洞的攻击向量。”

CrushFTP认为攻击者通过逆向分析其软件，发现了此漏洞并开始在未及时打补丁的设备上展开攻击。

“我们认为该漏洞影响的是7月1日前发布的版本……最新版本已修复该问题。”官方公告称，“攻击途径为HTTP(S)，我们起初未意识到此前的漏洞可被以这种方式利用。**攻击者通过我们的代码变更，推断出漏洞的存在并加以利用。**”

目前确认受影响的版本为CrushFTP v10.8.5和v11.3.4\_23之前的版本。CrushFTP强调，保持系统及时更新的用户不受影响。使用了**DMZ架构**将主服务器隔离的企业用户通常不受本次漏洞影响。

对于怀疑系统可能遭入侵的用户，CrushFTP建议从7月16日前的备份中恢复默认用户配置。潜在入侵迹象包括：

1. MainUsers/default/user.XML 文件中出现异常条目，尤其是新增字段如 `last_logins`；

2. 出现陌生的管理员账号，例如 `7a0d26089ac528941bf8cb998d97f408m`；

3. 默认用户被非法修改，但攻击者仍可利用。

Spink指出：“我们观察到的主要入侵指标是**默认用户配置被以异常方式修改**，这种方式对攻击者可用，但其他用户则无法使用。”

为防止进一步的攻击，CrushFTP建议采取以下措施：

1. 对服务器和管理端启用IP白名单限制；

2.部署DMZ实例分离主服务器；

3. 启用自动更新功能。

不过，网络安全公司Rapid7提醒，DMZ并非绝对安全的缓解措施。“出于审慎考虑，Rapid7不建议仅依赖DMZ作为防御手段。”该公司表示。

目前尚不清楚攻击者是否通过此次漏洞实施数据窃取或恶意软件部署，但近年来托管文件传输系统（MFT）频繁成为高级数据窃取活动的攻击目标。

过去，勒索软件组织Clop等曾多次利用类似平台中的零日漏洞（包括Cleo、MOVEit Transfer、GoAnywhere MFT和Accellion FTA）发动大规模数据窃取和勒索攻击。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-crushftp-zero-day-exploited-in-attacks-to-hijack-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310331](/post/id/310331)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-crushftp-zero-day-exploited-in-attacks-to-hijack-servers/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-crushftp-zero-day-exploited-in-attacks-to-hijack-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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