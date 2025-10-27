---
title: Lazarus Group 使用 CookiePlus 恶意软件以核工业为目标
url: https://www.anquanke.com/post/id/302948
source: 安全客-有思想的安全新媒体
date: 2024-12-25
fetch_date: 2025-10-06T19:34:24.015251
---

# Lazarus Group 使用 CookiePlus 恶意软件以核工业为目标

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

# Lazarus Group 使用 CookiePlus 恶意软件以核工业为目标

阅读量**109008**

发布时间 : 2024-12-24 10:08:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/lazarus-group-nuclear-industry-cookieplus-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

**要点概述**

* **重点转向核工业**： 与朝鲜有关联的拉扎罗斯集团已将目标转向核工业，这标志着其从早期关注国防、航空航天和加密货币可能升级。
* **虚假职位发布策略**： 2024 年 1 月观察到他们的攻击，利用虚假招聘信息（Operation DreamJob）发送伪装成工作评估的恶意文件，从而进入受害者的系统。
* **高级恶意软件技术**： 该团伙使用 Ranid Downloader 等先进工具和一种新型插件式恶意软件 “CookiePlus”，该插件在内存中运行，使安全系统难以发现。
* **利用漏洞**： Lazarus 继续改进其策略，利用谷歌浏览器零日等漏洞，并利用 macOS 上的 “RustyAttr ”等创新恶意软件。
* **需要警惕**： Lazarus 集团的复杂性和活动性不断增加，这凸显了加强网络安全措施的必要性，尤其是在敏感行业。

卡巴斯基的 Securelist 发布了最新威胁情报报告，重点关注臭名昭著的 Lazarus 黑客组织的活动。

根据 Securelist 的研究，拉扎罗斯组织最近已将重点转移到针对核工业内的个人。这表明他们的行动即将升级，因为他们之前主要集中在国防、航空航天和加密货币等领域。

报告写道：“我们观察到一次类似的攻击，Lazarus 集团在一个月内向至少两名与同一核相关组织有关的员工发送了包含恶意文件的归档文件。”

![Lazarus Group Targets Nuclear Industry with CookiePlus Malware]()
在受害者主机上创建的恶意文件（通过安全列表）

卡巴斯基观察到的攻击发生在 2024 年 1 月，其模式是使用虚假招聘信息，这是一种被称为 DeathNote 活动或 “Operation DreamJob ”的策略。

这包括创建虚假招聘启事，并以诱人的职业机会吸引潜在受害者。在 “面试 ”过程中，会巧妙地引入恶意文件，通常伪装成合法的评估测试。

攻击从伪装成知名公司工作评估的初始文件开始，该文件包含一个 ZIP 压缩包，其中有恶意可执行文件或木马化的合法工具（如 VNC 查看器）。

执行后，木马会提示受害者通过单独的通信渠道（如信使应用程序）输入攻击者提供的 IP 地址。这样，攻击者就可以在未经授权的情况下访问被入侵的机器，从而在网络中横向移动，并有可能窃取敏感数据或破坏关键操作。

根据 IP 地址生成的 XOR 密钥可解密 VNC 可执行文件的内部资源并解压数据。解压后的数据会被 Ranid Downloader 下载，后者会获取更多恶意有效载荷，如 MISTPEN、RollMid、LPEClient、Chamel Loader、ServiceChanger 和 CookiePlus。有效载荷类型（DLL 或 shellcode）由数据结构中的标志决定。这些插件的执行结果会被加密并发送到 C2 服务器。

最近这些攻击的一个关键创新是引入了 “CookiePlus”，这是一种基于插件的新型恶意软件。这种下载程序主要在内存中运行，动态加载恶意有效载荷。这种规避技术使传统的安全解决方案更难检测和减轻威胁。

CookiePlus 的开发表明，Lazarus 集团一直在努力改进其工具并躲避检测。通过引入新的模块化恶意软件和调整战术，他们的目标是在目标网络中保持持久存在并实现其目标。

该组织最近尤为活跃。11 月，Group-IB 发现了 Lazarus 集团的新木马 “RustyAttr”，它将恶意代码隐藏在 macOS 系统的扩展属性中；10 月，该集团利用谷歌 Chrome 浏览器的零日漏洞，针对加密货币投资者推出了一款欺骗性的 NFT 游戏。这就要求我们不断提高警惕，保护自己的数字资产。

本文翻译自hackread [原文链接](https://hackread.com/lazarus-group-nuclear-industry-cookieplus-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302948](/post/id/302948)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/lazarus-group-nuclear-industry-cookieplus-malware/)

如若转载,请注明出处： <https://hackread.com/lazarus-group-nuclear-industry-cookieplus-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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