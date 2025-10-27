---
title: Chaos勒索病毒：新兴的勒索软件即服务（RaaS）团队，启动语音欺诈和双重勒索攻击
url: https://www.anquanke.com/post/id/310647
source: 安全客-有思想的安全新媒体
date: 2025-07-29
fetch_date: 2025-10-06T23:50:19.449583
---

# Chaos勒索病毒：新兴的勒索软件即服务（RaaS）团队，启动语音欺诈和双重勒索攻击

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

# Chaos勒索病毒：新兴的勒索软件即服务（RaaS）团队，启动语音欺诈和双重勒索攻击

阅读量**69355**

发布时间 : 2025-07-28 16:39:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/chaos-ransomware-new-raas-group-likely-former-blacksuit-unleashes-vishing-double-extortion/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Cisco Talos Incident Response（Talos IR）发现了一种名为**Chaos的新型勒索软件即服务（RaaS）**运营活动，该活动正在全球范围内开展**大型猎杀和双重勒索攻击**。尽管Chaos与之前的恶意软件家族同名，Talos明确表示：

“Talos认为新的Chaos勒索软件与以前的Chaos构建工具生成的变种无关……该团伙使用相同的名称来制造混淆。”

在这一新品牌的背后，隐藏着一个复杂的威胁行为者，可能由前BlackSuit（Royal）勒索软件的成员组成。根据Talos的分析：

“Talos以中等信心评估认为，这个新团伙很可能由前**BlackSuit（Royal）**团伙的成员组成，**基于勒索软件加密方法、勒索通知结构以及攻击中使用的工具集之间的相似性**。”

Chaos的攻击开始时看似简单——**通过垃圾邮件轰炸引发语音钓鱼（vishing）策略**。受害者收到看似紧急的邮件，鼓励他们拨打一个冒充的IT支持电话。一旦接通电话，攻击者便**说服受害者启动Microsoft Quick Assist，从而启用远程桌面访问**。

![]()

一旦入侵成功，攻击者立即安装了**远程监控和管理（RMM）工具**，如AnyDesk、ScreenConnect、OptiTune、Syncro RMM和Splashtop，以建立持久的访问权限。

在取得立足点后，Chaos操作者**利用ipconfig、nltest和tasklist.exe等工具和命令进行全面的网络侦察，以识别用户、网络共享和信任关系**。

凭借Kerberoasting（通过ldapsearch）和通过net.exe进行密码重置，Chaos进行凭证窃取。注册表修改隐藏了用户账户，避免它们出现在登录界面，同时使用wmic禁用多因素认证应用程序。

Chaos勒索软件通过多线程混合加密系统进行部署，利用**椭圆曲线Diffie-Hellman（ECDH）和AES-256加密**，优化了速度和隐蔽性。如下所示的单个命令便能使整个网络瘫痪：

`Enc.exe /lkey:"<32-byte key>" /encrypt_step:40 /work_mode:local_network`

勒索软件会在文件名中附加.chaos扩展名，并丢下一个名为**readme.chaos.txt**的勒索通知。

“勒索软件利用多线程快速选择性加密、反分析技术，目标包括本地和网络资源，最大化影响力的同时，阻碍检测和恢复。”

Chaos展示了**高级的规避能力**，包括：

1. 环境检查，用于检测调试器、沙箱和虚拟机
2. 字符串混淆和XOR加密配置及勒索通知
3. 选择性加密，避免加密系统关键文件或目录
4. “所有这些检测规避技术都已实现…确保在检测到任何分析环境时，恶意软件立即终止执行。”

攻击者使用**GoodSync**（一个合法的备份工具）窃取数据并上传至攻击者控制的云存储。数据外泄通过重命名二进制文件（wininit.exe）巧妙地伪装，并过滤掉大型或不常见的文件类型以逃避检测。

受害者随后收到30万美元的勒索要求，通过基于Tor的联系方式进行沟通。Chaos威胁要：

1. 在公共数据泄露网站上泄露敏感数据
2. 对互联网暴露的系统发起DDoS攻击
3. 向客户和竞争对手通报此次泄露

勒索通知遵循结构化、操控性的剧本，声称此次攻击是一次“安全测试”，并承诺在支付赎金后恢复文件并删除数据。

“如果受害者未能支付赎金，攻击者威胁要公开被窃取的数据并发起分布式拒绝服务（DDoS）攻击……”

Talos注意到Chaos与之前的BlackSuit操作存在相似之处：

![]()

**这些相似之处，再加上共享的战术、技术和程序（TTPs）以及RMM工具的使用，强烈表明存在操作上的延续性。**

Chaos攻击了多个行业，涉及的国家包括：美国、英国、新西兰、印度。该组织采取机会主义策略，没有特定的行业重点。

本文翻译自securityonline [原文链接](https://securityonline.info/chaos-ransomware-new-raas-group-likely-former-blacksuit-unleashes-vishing-double-extortion/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310647](/post/id/310647)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/chaos-ransomware-new-raas-group-likely-former-blacksuit-unleashes-vishing-double-extortion/)

如若转载,请注明出处： <https://securityonline.info/chaos-ransomware-new-raas-group-likely-former-blacksuit-unleashes-vishing-double-extortion/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

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