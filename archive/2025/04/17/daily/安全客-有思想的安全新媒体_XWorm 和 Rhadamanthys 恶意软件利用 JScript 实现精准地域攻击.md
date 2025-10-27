---
title: XWorm 和 Rhadamanthys 恶意软件利用 JScript 实现精准地域攻击
url: https://www.anquanke.com/post/id/306590
source: 安全客-有思想的安全新媒体
date: 2025-04-17
fetch_date: 2025-10-06T22:02:48.228152
---

# XWorm 和 Rhadamanthys 恶意软件利用 JScript 实现精准地域攻击

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

# XWorm 和 Rhadamanthys 恶意软件利用 JScript 实现精准地域攻击

阅读量**46830**

发布时间 : 2025-04-16 11:01:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/malicious-jscript-loader-jailbreaked/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一条复杂的多阶段攻击链，该攻击链利用 JScript 脚本语言来投放危险的恶意软件负载。

这种攻击采用了复杂的混淆技术，最终会根据受害者所在的地理位置投放 XWorm 或 Rhadamanthys 恶意软件。

这个加载器通过精心设计的执行流程来运作，从 JScript 开始，过渡到 PowerShell，最后投放无文件恶意软件。

攻击通常通过计划任务或者涉及虚假验证码（CAPTCHA）的 ClickFix 攻击来发起。

攻击者会向受害者发送一个 mshta.exe 命令，该命令会执行经过混淆处理的 JScript 代码，而 JScript 代码又会生成 PowerShell 命令。

这种技术使攻击者能够利用 Windows 系统的合法组件来执行恶意代码，从而绕过传统的安全防护措施。

最初的感染途径显示出攻击者在利用系统信任关系方面的老练手段。

一旦执行，JScript 加载器会通过巧妙地将随机排序的数组元素重新组合成连贯的脚本来创建一个 PowerShell 命令。

然后，这个脚本会通过查询外部应用程序编程接口（API）来进行地理位置检查，以确定受害者是否位于美国，并据此引导攻击流程。

Sophos 的研究人员认为，这种地理围栏式的投放策略是一种有意针对特定地区的尝试，同时减少不必要的暴露。

研究人员指出，这种基于地理位置的负载投放方式代表了有针对性的恶意软件传播技术的一种演进，使威胁行为者能够根据地理位置因素定制攻击。

该恶意软件实施了全面的反取证措施，包括终止与之竞争的进程，并从系统的各个目录中删除潜在的证据文件。

它在保持低调以逃避安全防护解决方案检测的同时，还创建了持久的感染路径。

****执行流程分析****

这种恶意软件最引人注目的方面是其复杂的执行流程。在最初的 JScript 执行之后，加载器会启动一个多阶段的去混淆过程。

一个 PowerShell 代码示例揭示了其复杂性：

# 定义执行块

#{{E}={

# 定义类型和方法名称

${T} = [char[]]@(‘A’, ‘.’, ‘B’)

${M} = [char[]]@(‘C’)

# 从已加载的程序集中获取类型和方法

${Y} = $I.GetType((${T} -join ”))

${N} = ${Y}.GetMethod((${M} -join ”))

这段代码片段展示了恶意软件如何使用 PowerShell 反射来动态加载恶意组件，同时逃避检测。

加载器将十进制编码的数据转换为可执行代码，然后将其注入到像 RegSvcs.exe 这样的合法 Windows 进程中。

最终的负载会因地理位置而有所不同。美国的受害者会收到 XWorm，这是一种远程访问木马，能够执行分布式拒绝服务（DDoS）攻击和劫持加密货币的剪贴板。

非美国的受害者会感染上 Rhadamanthys，这是一种复杂的基于 C++ 的信息窃取程序，它使用人工智能驱动的图像识别技术来识别加密货币钱包的助记词。

这项分析凸显了现代恶意软件传播技术的演进，将复杂的混淆技术与有针对性的投放机制相结合，以最大限度地提高感染成功率，同时最小化被检测到的可能性。

建议安全专业人员实施强大的检测机制，重点识别可疑的 PowerShell 执行链和无文件注入技术。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/malicious-jscript-loader-jailbreaked/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306590](/post/id/306590)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/malicious-jscript-loader-jailbreaked/)

如若转载,请注明出处： <https://cybersecuritynews.com/malicious-jscript-loader-jailbreaked/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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