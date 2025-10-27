---
title: 微软：macOS “Sploitlight” 漏洞可泄露 Apple Intelligence 数据
url: https://www.anquanke.com/post/id/310676
source: 安全客-有思想的安全新媒体
date: 2025-07-31
fetch_date: 2025-10-06T23:16:36.389128
---

# 微软：macOS “Sploitlight” 漏洞可泄露 Apple Intelligence 数据

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

# 微软：macOS “Sploitlight” 漏洞可泄露 Apple Intelligence 数据

阅读量**83933**

发布时间 : 2025-07-30 17:08:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/microsoft-macos-sploitlight-flaw-leaks-apple-intelligence-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软发布的一份最新报告指出，攻击者可利用一个近期已修复的 macOS 漏洞，绕过**“透明度、同意与控制”（TCC）**安全机制，从而窃取用户的敏感信息，包括 Apple Intelligence 的缓存数据。

TCC 是苹果设备上的一项安全技术与隐私框架，旨在防止应用程序未经授权访问用户的私人数据，macOS 能通过该机制控制应用如何获取和使用这些数据。

苹果已于 3 月发布的 macOS Sequoia 15.4 补丁中修复了该漏洞（编号为 **CVE-2025-31199**），修复方式为**“改进数据脱敏处理”**。该漏洞由微软安全研究员 Jonathan Bar Or、Alexia Wilson 和 Christine Fossaceca 发现并报告。

尽管苹果对 TCC 机制做出限制，仅允许拥有完全磁盘访问权限的应用接触敏感数据，并默认阻止未授权代码的执行，但微软研究人员发现，攻击者可**滥用 Spotlight 插件的特权访问权限，读取敏感文件并窃取其中的数据**。

微软今日发布的报告中展示，攻击者可利用这一漏洞（微软命名为 “Sploitlight”，苹果则将其描述为“日志记录问题”）窃取高价值数据，包括 Apple Intelligence 相关信息，以及与其他 iCloud 账户绑定设备的远程信息。

此次披露的漏洞所泄露的**数据类型范围广泛**，包括但不限于：照片和视频的元数据、精确的地理位置信息、人脸和人物识别数据、用户行为及事件上下文、相册和共享图库、搜索记录和用户偏好设置，甚至还包括已删除的照片与视频。

![]()

自 2020 年以来，苹果已修复多项与 TCC 绕过相关的安全漏洞，其中包括**利用 Time Machine 挂载实现的绕过（CVE-2020-9771）、环境变量污染漏洞（CVE-2020-9934）以及捆绑识别漏洞（CVE-2021-30713）**。微软安全研究人员过去亦发现多个 TCC 绕过方式，如“powerdir”（CVE-2021-30970）和“HM-Surf”，均可被恶意利用以访问用户的私人数据。

微软本周一表示：“虽然 Sploitlight 与此前发现的绕过方式如 HM-Surf 和 powerdir 存在相似之处，但其影响更为严重，因为该漏洞能够提取并泄露 Apple Intelligence 缓存的敏感信息，如精确位置数据、媒体元数据、人脸识别信息、搜索历史、用户偏好等。”

微软进一步指出：“这些风险因 **iCloud 账户间的远程关联机制**而加剧。攻击者一旦入侵某台 macOS 设备，便可利用该漏洞探测与该账户绑定的其他设备的远程信息。”

近年来，微软安全团队还发现了**多项 macOS 的高危漏洞**。例如，2021 年披露的名为 “Shrootless”（CVE-2021-30892） 的 SIP（System Integrity Protection）绕过漏洞，可被攻击者用于在受害设备上安装 rootkit。此后，研究人员又发现了名为 “Migraine”（CVE-2023-32369）的新型 SIP 绕过漏洞，以及 “Achilles”（CVE-2022-42821），该漏洞可使不受信任的应用程序绕过 Gatekeeper 的执行限制安装恶意软件。

在 2024 年，微软还报告了另一个 SIP 绕过漏洞（CVE-2024-44243），攻击者可借此加载第三方内核扩展，植入恶意内核驱动程序。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/microsoft-macos-sploitlight-flaw-leaks-apple-intelligence-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310676](/post/id/310676)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/microsoft-macos-sploitlight-flaw-leaks-apple-intelligence-data/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/microsoft-macos-sploitlight-flaw-leaks-apple-intelligence-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**9赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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