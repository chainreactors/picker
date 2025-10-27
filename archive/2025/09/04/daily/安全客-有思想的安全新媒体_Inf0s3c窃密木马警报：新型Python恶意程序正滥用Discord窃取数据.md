---
title: Inf0s3c窃密木马警报：新型Python恶意程序正滥用Discord窃取数据
url: https://www.anquanke.com/post/id/311827
source: 安全客-有思想的安全新媒体
date: 2025-09-04
fetch_date: 2025-10-02T19:36:22.360118
---

# Inf0s3c窃密木马警报：新型Python恶意程序正滥用Discord窃取数据

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

# Inf0s3c窃密木马警报：新型Python恶意程序正滥用Discord窃取数据

阅读量**257146**

发布时间 : 2025-09-03 17:39:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/inf0s3c-stealer-a-stealthy-python-malware-is-abusing-discord-to-steal-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Cyfirma的威胁情报团队发布了针对**Inf0s3c Stealer**的技术分析报告。这是一款基于Python的信息窃取工具，旨在从Windows机器中窃取敏感的用户和系统数据。该恶意软件展示了模块化设计、持久化能力和隐秘的数据窃取功能，与其他高级信息窃取家族的特征相符。

报告指出：“**Inf0s3c Stealer**是一款基于**Python**的窃取工具，旨在收集系统信息和用户数据……它系统地收集系统详细信息，包括主机标识符、CPU信息和网络配置，并捕获屏幕截图。”

该窃取工具会构建受害者机器的详细档案，收集以下信息：

1. **系统标识符（主机名、CPU信息、MAC地址）；**
2. **运行进程列表；**
3. **目录结构（桌面、文档、图片、下载等）；**
4. **屏幕截图和网络摄像头图像。**

然后，它将这些数据编译成受密码保护的档案，再发送到攻击者控制的渠道。

除了侦察外，**Inf0s3c**还会主动窃取敏感数据。分析报告称：**“Inf0s3c Stealer**收集密码、Cookie、自动填充数据、浏览历史、电子钱包、Discord令牌和Telegram数据。”

它还针对Roblox、Minecraft和Epic Games等游戏相关账户——这表明它对寻求可变现数字资产的网络犯罪分子具有吸引力。

该恶意软件通过以下技术确保持久化：

1. **将自身复制到Windows启动文件夹；**
2. **绕过用户账户控制（UAC）；**
3. **注入Discord进程以实现持久化和令牌窃取。**

该窃取工具包含反虚拟机检查，以避免沙箱分析，甚至会阻止对防病毒相关域名的访问。它还可以在执行后自行删除（“消融”）以抹去痕迹。

正如Cyfirma所指出的：“混淆技术和模块化代码的存在凸显了其对规避检测和适应性的重视。”

执行开始后，Inf0s3c会静默调用PowerShell命令收集系统信息，然后将结果整理到**%temp%**下的结构化目录中。

报告证实，数据窃取是自动化的：“结果通过Discord交付，包含一个名为**Blank-WDAGUtilityAccount.rar**的RAR档案，其中包含被盗数据。”

这种方法利用Discord作为命令与控制（C2）渠道和数据投放站点，这是现代恶意软件 campaign中日益常见的策略。

有趣的是，Cyfirma分析师发现它与其他公开可用的窃取家族有很强的重叠：“观察到的技术和结构……与同一开发者分享的公开可用项目密切相关，包括Blank Grabber和Umbral-Stealer。”

这表明要么存在共享作者身份，要么恶意软件生态系统中存在代码复用，从而加速了开发和分发。

Inf0s3c Stealer展示了现代信息窃取工具如何结合侦察、凭证窃取和反检测功能以最大化影响。其广泛的目标范围——从密码和令牌到游戏账户——说明了被盗数字身份的商品化。

正如Cyfirma所总结的：“本分析强调了持续监控、及时的威胁情报和全面的端点防御对于检测和应对此类不断演变的恶意软件威胁的重要性。”

本文翻译自securityonline [原文链接](https://securityonline.info/inf0s3c-stealer-a-stealthy-python-malware-is-abusing-discord-to-steal-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311827](/post/id/311827)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/inf0s3c-stealer-a-stealthy-python-malware-is-abusing-discord-to-steal-data/)

如若转载,请注明出处： <https://securityonline.info/inf0s3c-stealer-a-stealthy-python-malware-is-abusing-discord-to-steal-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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