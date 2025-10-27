---
title: Sophos 揭开樱花 RAT 的神秘面纱：黑客利用后门恶意软件攻击！
url: https://www.anquanke.com/post/id/308146
source: 安全客-有思想的安全新媒体
date: 2025-06-06
fetch_date: 2025-10-06T22:47:54.339860
---

# Sophos 揭开樱花 RAT 的神秘面纱：黑客利用后门恶意软件攻击！

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

# Sophos 揭开樱花 RAT 的神秘面纱：黑客利用后门恶意软件攻击！

阅读量**179068**

发布时间 : 2025-06-05 12:56:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/sophos-unmasks-sakura-rat-hackers-hacking-hackers-with-backdoored-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![樱花 RAT, 黑客恶意软件]()

在最近的一次深潜中,Sophos X-Ops发现了一个复杂的活动,不针对企业或政府,而是其他黑客和游戏作弊者。这一切都始于一个名为Sakura RAT的后门恶意软件。

调查开始时,一位客户询问Sophos他们是否受到保护,可以防止一个名为Sakura RAT的工具,Sakura RAT是GitHub上托管的开源远程访问木马。但是,在检查代码时,Sophos研究人员很快发现,如果构建,这种RAT甚至无法运行 – 许多部分不完整或从其他恶意软件(如AsyncRAT)中窃取。

Visual Basic 项目文件中的隐藏 <PreBuild> 事件,在编译项目时秘密下载并安装恶意软件。

> *“樱花老鼠被后门。该代码旨在针对编制RAT的人,以及信息窃取器和其他RAT。*

Sophos将攻击追溯到GitHub YAML文件中的电子邮件地址:ischhfd83[at]rambler.ru。搜索此标识符和代码片段导致了一个重要的发现——超过141个存储库,其中133个是后门。

![樱花 RAT, 黑客恶意软件]()

恶意存储库之一 – 这个声称是 CVE-2025-12654 的漏洞利用构建器 | 图片: Sophos X-Ops

*“我们发现了141个存储库,其中133个是后门,*其中111个包含PreBuild后门。

这些存储库伪装成从游戏作弊到恶意软件工具的一切,利用脚本小子和想成为黑客的好奇心和贪婪。甚至媒体报道也无意中宣传了这些存储库,进一步传播了陷阱。

感染链非常复杂。Visual Studio 版本:

1. PreBuild脚本悄然删除了。vbs文件。
2. 该脚本编写并执行了 PowerShell 有效载荷。
3. 有效载荷获取了一个包含基于Electron的恶意软件应用程序SearchFilter.exe的7z存档。
4. 在内部,一个庞大的,模糊的JavaScript文件执行了数据窃取,计划任务,Defender绕过[attackers](https://securityonline.info/bitdefender-gravityzone-small-business-security-review-enterprise-grade-protection-without-the-enterprise-headache/),并通过Telegram与攻击者进行通信。

> *“恶意软件收集……用户名,主机名,网络界面……并通过Telegram发送给攻击者。*

除了PreBuild后门之外,研究人员还确定了其他三个:

* 使用Fernet加密的Python后门,并隐藏了空白。
* screensaver (.scr) 文件伪装从右到左覆盖技巧。
* 使用 eval() 和混淆的多级有效载荷的 JavaScript 后门。

[detection](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/)每种变化都采用了独特的混淆和巧妙的技巧来逃避检测并最大化感染。

Sophos还发现了一种自动化模式:通过GitHub Actions自动提交,具有可回收用户名的虚假贡献者(如Mastoask,Maskts和Mastrorz),以及模仿主动开发的YAML脚本。

*“威胁行为者可能希望给人一种错觉,即他们的存储库定期维护,以吸引更多潜在的受害者。*

ischhfd83的身份仍然是一个谜,但这个角色与过去的分布式即服务(DaaS)网络(如Stargazer Goblin)之间出现了联系。嵌入恶意软件中的Telegram机器人指向未知x,这可能是别名。该团队甚至发现了一个可疑的领域——arturshi.ru——曾经托管过一个虚假的网红课程,现在重定向到一个金融诈骗网站。

> *“’未知’是否是实际的别名……还是故意缺席,*尚不清楚。

Sophos 以这个警告结束:

> *“我们怀疑这个故事可能还有更多,*并将继续监测进一步发展。

本文翻译自securityonline [原文链接](https://securityonline.info/sophos-unmasks-sakura-rat-hackers-hacking-hackers-with-backdoored-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308146](/post/id/308146)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sophos-unmasks-sakura-rat-hackers-hacking-hackers-with-backdoored-malware/)

如若转载,请注明出处： <https://securityonline.info/sophos-unmasks-sakura-rat-hackers-hacking-hackers-with-backdoored-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04

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