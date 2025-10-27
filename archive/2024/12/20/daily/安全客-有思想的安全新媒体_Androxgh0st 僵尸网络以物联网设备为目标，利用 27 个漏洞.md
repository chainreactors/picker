---
title: Androxgh0st 僵尸网络以物联网设备为目标，利用 27 个漏洞
url: https://www.anquanke.com/post/id/302843
source: 安全客-有思想的安全新媒体
date: 2024-12-20
fetch_date: 2025-10-06T19:35:56.472835
---

# Androxgh0st 僵尸网络以物联网设备为目标，利用 27 个漏洞

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

# Androxgh0st 僵尸网络以物联网设备为目标，利用 27 个漏洞

阅读量**78970**

|评论**1**

发布时间 : 2024-12-19 10:42:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/androxgh0st-botnet-iot-devices-exploit-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

要点

* **快速漏洞利用**： Androxgh0st 僵尸网络扩大了其武器库，利用了网络服务器、物联网设备和各种技术（包括思科 ASA、Atlassian JIRA 和 TP-Link 路由器）中的 27 个漏洞。
* **与 Mozi 僵尸网络整合**： 僵尸网络整合了 Mozi 有效载荷，以物联网设备为目标，并可能共享命令和控制基础设施，这标志着协调性和复杂性的提高。
* **关注薄弱的安全实践**： Androxgh0st 采用暴力破解攻击、凭证填充和利用默认密码或弱密码设备来获取管理访问权限并保持持久性。
* **全球和中国特定目标**： 该僵尸网络利用全球系统和中国特定技术中的漏洞，有证据表明它与中国 CTF 社区和基于普通话的网络钓鱼策略有关。
* **打补丁的紧急呼吁**：研究人员建议立即为所有受影响的系统打补丁，以降低风险，包括远程代码执行、数据泄露和勒索软件攻击。

CloudSEK的上下文人工智能数字风险平台Xvigil发现了Androxgh0st僵尸网络的重大演变，揭示了其对20多个漏洞的利用以及与Mozi僵尸网络的业务整合，预计到2025年中期，网络应用漏洞将至少增加75%。

CISA今年早些时候发布了一份关于Androxgh0st攻击面不断扩大的公告，其中包括思科ASA、Atlassian JIRA和PHP框架，允许未经授权的访问和远程代码执行。

CloudSEK 的研究表明，Androxgh0st 的攻击范围已经超出了最初的 Web 服务器，现在又加入了以物联网为重点的 Mozi 有效载荷。 它正积极利用各种技术中的 27 个漏洞。

这些漏洞包括利用 Cisco ASA 中的 Web 脚本注入漏洞 （CVE-2014-2120），利用路径遍历漏洞 （CVE-2021-26086） 进行远程文件读取，利用本地文件包含漏洞 （CVE-2021-41277） 进行任意文件下载，以及针对 PHPUnit、Laravel、PHP-CGI、TP-Link 路由器、Netgear 设备和 GPON 路由器中的漏洞。

现在还有许多其他漏洞被利用，包括 Sophos Firewall、Oracle EBS、OptiLink ONT1GEW、Spring Cloud Gateway 和各种中国特定软件中的漏洞。 Sophos Authentication bypass 漏洞会在防火墙的 User Portal 及 Webadmin 网页界面导致远程执行代码 （RCE），让未经认证的攻击者执行任意代码。

Oracle E-Business Suite （EBS） 未经验证的任意文件上载也存在此漏洞，攻击者可利用漏洞，以 Oracle 用户身份执行远程代码。 OptiLink ONT1GEW GPON 2.1.11\_X101 Build 1127.190306 亦允许远程执行代码 （已验证）。 最后，PHP CGI 参数注入问题（CVE-2024-4577）是另一个影响 PHP-CGI 的问题。

利用该漏洞可实现未经授权的访问和远程代码执行，给全球网络服务器和物联网网络带来重大风险。 此外，该僵尸网络的共享基础设施、持续的后门策略和 Mozi 有效载荷的加入，都表明其日益复杂。

研究表明，Androxgh0st 和 Mozi 僵尸网络之间存在大量业务重叠，Androxgh0st 部署 Mozi 有效载荷来感染物联网设备，并可能共享指挥和控制基础设施，这表明它们之间存在高度协调或统一的控制结构。

进一步探测发现，Androxgh0st 采用了复杂的策略，如代码注入和文件附加，以保持对被入侵系统的持续访问。 它以 WordPress 安装为目标，使用暴力破解攻击和凭据填充来获取管理访问权限，并经常利用默认密码、弱密码或易猜密码的设备。

虽然明确的归因很复杂，但研究表明，由于针对中国特有的技术和软件，它与中国的 CTF 社区有关联。 这包括在注入的有效载荷和命令基础架构中使用 “PWN\_IT ”字符串，在网络钓鱼诱饵和源代码中使用普通话，以及与中国 Kanxue 主办的 CTF 活动的潜在联系。 成功利用可导致数据泄露、盗窃、系统中断、勒索软件攻击、僵尸网络扩大以及间谍和监视活动。

![Androxgh0st Botnet Targets IoT Devices, Exploiting 27 Vulnerabilities]()
研究人员在博客中详细介绍了设备受影响最严重的国家以及与中国的联系（通过 CloudSec）。

“CloudSEK 建议立即修补这些漏洞，以降低与 Androxgh0st 僵尸网络相关的风险，该僵尸网络以系统性利用和持续后门访问而闻名，”研究人员指出。

本文翻译自hackread [原文链接](https://hackread.com/androxgh0st-botnet-iot-devices-exploit-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302843](/post/id/302843)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/androxgh0st-botnet-iot-devices-exploit-vulnerabilities/)

如若转载,请注明出处： <https://hackread.com/androxgh0st-botnet-iot-devices-exploit-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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