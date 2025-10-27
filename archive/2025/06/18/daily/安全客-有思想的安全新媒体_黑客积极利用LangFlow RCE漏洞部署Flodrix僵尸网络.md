---
title: 黑客积极利用LangFlow RCE漏洞部署Flodrix僵尸网络
url: https://www.anquanke.com/post/id/308540
source: 安全客-有思想的安全新媒体
date: 2025-06-18
fetch_date: 2025-10-06T22:51:52.907497
---

# 黑客积极利用LangFlow RCE漏洞部署Flodrix僵尸网络

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

# 黑客积极利用LangFlow RCE漏洞部署Flodrix僵尸网络

阅读量**54099**

发布时间 : 2025-06-17 16:07:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/langflow-rce-vulnerability-exploited/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员通过 CVE-2025-3248 发现了一个针对 Langflow 服务器的活跃网络攻击活动，CVE-2025-3248 是一个关键的远程代码执行漏洞，允许威胁行为者部署复杂的 Flodrix 僵尸网络恶意软件。

这些攻击表明，网络犯罪分子如何迅速将新披露的漏洞作为武器，以破坏云基础设施并扩大其僵尸网络作。

CVE-2025-3248 的 CVSS 评分为 9.8，影响 1.3.0 之前的 Langflow 版本，并已添加到 CISA 的已知利用漏洞目录中。

该漏洞存在于终端节点中，该终端节点在处理用户提供的 Python 代码片段时无法实施适当的身份验证。`/api/v1/validate/code`

攻击者可以通过发送构建的 POST 请求来利用此缺陷，该请求包含嵌入在函数默认参数或装饰器中的恶意 Python 负载。

该漏洞允许远程攻击者无需身份验证即可实现代码执行，因为 Langflow 通过使用 将恶意代码解析为抽象语法树来处理恶意代码，然后通过 Python 的 and 函数编译和执行它。此设计缺陷可在受影响的服务器上实现完全的系统危害。`ast.parse()``compile()``exec()`

## Langflow RCE 漏洞被利用

网络犯罪分子开发了一种系统方法来利用易受攻击的 Langflow 安装。他们首先使用 Shodan 或 FOFA 等工具扫描互联网，以识别公开暴露的 Langflow 服务器。一旦确定了目标，攻击者就会利用 GitHub 的开源概念验证漏洞来获得对易受攻击系统的远程 shell 访问权限。

在最初的入侵之后，攻击者会执行各种侦查命令，包括 、 和 来收集系统信息。`whoami``printenv``cat /root/.bash_history``ip addr show``systemctl status sshd`

收集到的情报被传回命令和控制服务器，可能用于识别高价值目标以供进一步利用。

![Langflow RCE 漏洞被利用]()

Langflow RCE 漏洞被利用

攻击以部署名为“docker”的特洛伊木马下载程序脚本而告终，该脚本从攻击者控制的 IP 地址为 80.66.75.1211 的基础设施获取并执行 Flodrix 僵尸网络负载。恶意软件下载程序尝试在多种系统类型上安装特定于架构的僵尸网络变体。

Flodrix 僵尸网络代表了 LeetHozer 恶意软件家族的演变，它结合了先进的隐身技术，包括自我删除和伪影删除，以逃避检测。该恶意软件使用密钥“qE6MGAbI”的 XOR 加密进行字符串混淆，以隐藏命令和控制服务器地址。

安装后，Flodrix 使用 TCP 和 UDP 协议与其基础设施建立双通信通道。僵尸网络可以根据从控制服务器收到的命令执行各种分布式拒绝服务攻击，包括 tcpraw、udpplain、handshake、tcplegit、ts3 和 udp 攻击类型。

此外，该恶意软件会主动终止竞争进程，并通过 UDP 通知向作员发送详细的系统信息。

运行 Langflow 的组织必须立即升级到版本 1.3.0 或更高版本，该版本对易受攻击的终端节点实施了适当的身份验证要求。该补丁添加了一个参数，用于在允许访问代码验证功能之前验证用户会话。`_current_user: CurrentActiveUser`

系统管理员还应限制对 Langflow 端点的公共访问，监控危害指标，并扫描是否存在隐藏文件，例如恶意软件用于持久性跟踪的文件。`.system_idle`

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/langflow-rce-vulnerability-exploited/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308540](/post/id/308540)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/langflow-rce-vulnerability-exploited/)

如若转载,请注明出处： <https://cybersecuritynews.com/langflow-rce-vulnerability-exploited/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [政策法规](/tag/%E6%94%BF%E7%AD%96%E6%B3%95%E8%A7%84)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* [Langflow RCE 漏洞被利用](#h2-0)

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