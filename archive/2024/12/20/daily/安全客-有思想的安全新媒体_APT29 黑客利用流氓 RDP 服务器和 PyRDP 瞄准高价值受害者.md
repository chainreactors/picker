---
title: APT29 黑客利用流氓 RDP 服务器和 PyRDP 瞄准高价值受害者
url: https://www.anquanke.com/post/id/302852
source: 安全客-有思想的安全新媒体
date: 2024-12-20
fetch_date: 2025-10-06T19:35:51.953391
---

# APT29 黑客利用流氓 RDP 服务器和 PyRDP 瞄准高价值受害者

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

# APT29 黑客利用流氓 RDP 服务器和 PyRDP 瞄准高价值受害者

阅读量**86993**

|评论**1**

发布时间 : 2024-12-19 11:21:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html>

译文仅供参考，具体内容表达以及含义原文为准。

据观察，与俄罗斯有关联的 APT29 威胁行为体在利用恶意远程桌面协议（RDP）配置文件进行网络攻击时，重新使用了合法的红队攻击方法。

趋势科技在一份报告中称，这一活动的目标是政府和武装部队、智库、学术研究人员和乌克兰实体，需要采用 Black Hills Information Security 曾在 2022 年记录的 “流氓 RDP ”技术。

研究人员费克-哈克博德（Feike Hacquebord）和斯蒂芬-希尔特（Stephen Hilt）说：“这种技术的受害者会将其机器的部分控制权交给攻击者，从而可能导致数据泄露和恶意软件安装。”

网络安全公司正在追踪这个名为 “Earth Koshchei ”的威胁组织，并称该组织早在 2024 年 8 月 7 日至 8 日就开始了活动的准备工作。乌克兰计算机应急响应小组（CERT-UA）、微软和亚马逊网络服务（AWS）也在 10 月份对 RDP 活动进行了关注。

鱼叉式网络钓鱼电子邮件旨在欺骗收件人启动附在邮件中的恶意 RDP 配置文件，使他们的机器通过该组织的 193 个 RDP 中继站之一连接到国外的 RDP 服务器。据估计，一天之内就有 200 名知名受害者成为攻击目标，这表明了该活动的规模。

Black Hill 概述的攻击方法需要在实际由对手控制的 RDP 服务器前使用一个名为 PyRDP 的开源项目（被描述为基于 Python 的 “中间怪兽（MitM）工具和库）”，以最大限度地降低被发现的风险。

这样，当受害者从电子邮件中打开代号为 HUSTLECON 的 RDP 文件时，就会向 PyRDP 中转站发起一个向外的 RDP 连接，然后将会话重定向到恶意服务器。

研究人员说：“建立连接后，流氓服务器会模仿合法 RDP 服务器的行为，并利用会话开展各种恶意活动。主要的攻击载体包括攻击者在受害者的机器上部署恶意脚本或更改系统设置。”

除此之外，PyRDP 代理服务器还能让攻击者访问受害者的系统、执行文件操作和注入恶意有效载荷。攻击的最终结果是，威胁者利用被入侵的 RDP 会话，通过代理服务器外泄敏感数据，包括凭证和其他专有信息。

值得注意的是，这种攻击是通过恶意配置文件进行数据收集的，无需部署任何定制恶意软件，从而使威胁行为者能够在不被察觉的情况下进行攻击。

另一个值得一提的特点是使用匿名层（如 TOR 出口节点）来控制 RDP 服务器，以及使用住宅代理提供商和商业 VPN 服务来访问合法的邮件服务器，这些服务器被用来发送鱼叉式网络钓鱼电子邮件。

研究人员补充说：“PyRDP 等工具可以拦截和操纵 RDP 连接，从而增强攻击效果。PyRDP可以自动抓取受害者重定向的共享驱动器，并将其内容保存在攻击者机器的本地，从而实现无缝数据外渗。”

“Earth Koshchei 在间谍活动中不断使用新方法。他们不仅密切关注有助于他们获得初始访问权的新旧漏洞，还关注红色团队开发的方法和工具。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302852](/post/id/302852)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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