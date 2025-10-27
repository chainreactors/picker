---
title: ESET 研究人员公布了 Gelsemium 高级持续性威胁（APT）组织的 Linux 对应程序 WolfsBane
url: https://www.anquanke.com/post/id/302174
source: 安全客-有思想的安全新媒体
date: 2024-11-26
fetch_date: 2025-10-06T19:12:08.905967
---

# ESET 研究人员公布了 Gelsemium 高级持续性威胁（APT）组织的 Linux 对应程序 WolfsBane

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

# ESET 研究人员公布了 Gelsemium 高级持续性威胁（APT）组织的 Linux 对应程序 WolfsBane

阅读量**57448**

发布时间 : 2024-11-25 15:06:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/wolfsbane-gelsemiums-linux-backdoor-debut/>

译文仅供参考，具体内容表达以及含义原文为准。

![Gelsemium APT group - WolfsBane]()

ESET研究人员公布了基于Windows的Gelsevirine后门的Linux对应程序WolfsBane，这是Gelsemium高级持续性威胁（APT）组织发展过程中的一个重要里程碑。这个与中国结盟的组织以针对东亚和中东地区的网络间谍活动而闻名，它的武器库中增加了Linux系统，这标志着随着对手适应Windows防御系统的加强，其战略也发生了转变。

WolfsBane是Gelsemium公司首次记录的Linux恶意软件，Gelsemium公司自2014年开始活跃。报告称：“这是第一份记录Gelsemium使用Linux恶意软件的公开报告，标志着他们的行动策略发生了显著转变。该恶意软件以及名为FireWood的第二个Linux后门代表了APT组织转向Linux系统的日益增长的趋势。”

ESET将这一转变归因于Windows安全性的提高，如端点检测和响应（EDR）工具的广泛采用，以及微软默认禁用Visual Basic for Applications（VBA）宏。这些变化迫使对手探索新的攻击面，基于 Linux 的面向互联网的系统成为首要攻击目标。

WolfsBane 是在台湾、菲律宾和新加坡上传到 VirusTotal 的档案中发现的。该恶意软件由三个阶段的链条组成：下载器、启动器和后门本身。该程序模仿合法的系统实用程序，如 cron，以逃避检测。一旦部署，它就会利用系统服务和部署用户rootkit来隐藏自己的存在，从而建立持久性。

后门本身与 Gelsevirine 关系密切，具体表现为

* 命令执行机制： Linux 和 Windows 变种都使用一个命令哈希值映射到函数的表格，用于执行从命令与控制（C&C）服务器接收到的命令。
* 自定义库： 两个版本都加载了用于网络通信的自定义库，其代码库中有相同的错别字，如 “create\_seesion”。
* 配置结构： 配置文件中的字段名称和值相似，包括 pluginkey 和 controller\_version。

WolfsBane 的 C&C 通信依赖于支持 UDP 和 HTTPS 协议的嵌入式库，有利于数据外渗和远程命令执行。它的加密机制允许在不被发现的情况下进行更新，使其成为一种具有高度持久性和适应性的威胁。

ESET 还发现了 FireWood，这是一个可能与 Project Wood 恶意软件家族有关的 Linux 后门。虽然 FireWood 与 Gelsemium 的联系仍不紧密，但它与已知的中国 APT 工具有几个共同特征，包括特定的命名规则、TEA 加密和一致的 C&C 通信模式。FireWood 利用 Netlink 协议进行内核级交互，并采用各种持久性机制来确保运行寿命。

向Linux恶意软件的转变反映了威胁形势的广泛变化。ESET 指出：”面向互联网的基础设施中存在的漏洞，尤其是那些基于 Linux 的系统，正日益成为攻击目标。由于Linux系统在服务器环境中占主导地位，并为关键应用程序提供动力，因此利用这些系统为对手提供了获取敏感数据和长时间访问的途径。

WolfsBane 恶意软件体现了 Gelsemium APT 组织的适应能力，因为他们将攻击面扩大到了 Linux 系统。通过利用隐蔽性、持久性和先进的通信机制，WolfsBane 对使用基于 Linux 基础设施的组织构成了重大风险。正如 ESET 总结的那样，“这些 Linux 系统正在成为这些对手的新首选目标”。

本文翻译自securityonline [原文链接](https://securityonline.info/wolfsbane-gelsemiums-linux-backdoor-debut/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302174](/post/id/302174)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/wolfsbane-gelsemiums-linux-backdoor-debut/)

如若转载,请注明出处： <https://securityonline.info/wolfsbane-gelsemiums-linux-backdoor-debut/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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