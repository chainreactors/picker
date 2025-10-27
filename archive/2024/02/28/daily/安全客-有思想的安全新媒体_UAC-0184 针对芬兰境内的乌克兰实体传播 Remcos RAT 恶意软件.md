---
title: UAC-0184 针对芬兰境内的乌克兰实体传播 Remcos RAT 恶意软件
url: https://www.anquanke.com/post/id/293466
source: 安全客-有思想的安全新媒体
date: 2024-02-28
fetch_date: 2025-10-04T12:06:10.122197
---

# UAC-0184 针对芬兰境内的乌克兰实体传播 Remcos RAT 恶意软件

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

# UAC-0184 针对芬兰境内的乌克兰实体传播 Remcos RAT 恶意软件

阅读量**160349**

发布时间 : 2024-02-27 11:57:13

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

被追踪为 UAC-0184 的威胁行为者一直在使用隐写术技术，通过名为 IDAT Loader 的相对较新的恶意软件向位于芬兰的乌克兰目标传送 Remcos 远程访问木马 (RAT)。

尽管对手最初针对的是乌克兰境内的实体，但防御措施阻碍了有效载荷的交付。根据 Morphisec 威胁实验室今天的分析，这导致了随后对替代目标的搜索。

虽然 Morphisec 因客户机密而没有透露活动细节，但研究人员指出 Dark Reading据称与 UAC-0148 进行的并行活动有关，该活动使用电子邮件和鱼叉式网络钓鱼作为初始访问媒介，并以乌克兰军事人员为目标，以提供咨询为诱饵。以色列国防军 (IDF) 的角色。

其目标是网络间谍活动：网络犯罪分子使用 Remcos（“远程控制和监视”的缩写）RAT 来未经授权访问受害者的计算机、远程控制受感染的系统、窃取敏感信息、执行命令等。

**IDAT Loader：新的 Remcos RAT 感染例程**
这一特定活动于 1 月份首次发现，利用嵌套感染方法，从带有新颖用户代理标签“racon”的代码开始，该代码获取第二阶段有效负载并执行连接检查和活动分析。

研究人员解释说，Morphisec 将该有效负载识别为 IDAT Loader，又名 HijackLoader，这是一种高级加载程序，已被观察到与多个恶意软件家族一起工作。它于 2023 年末首次被观察到。

IDAT 是指便携式网络图形 (PNG) 图像文件格式中的“图像数据”块。顾名思义，加载程序会定位并提取 Remcos RAT 代码，该代码被走私到嵌入隐写 .PNG 图像的 IDAT 块内的受害计算机上。

隐写术攻击者将恶意负载隐藏在看似无害的图像文件中，以逃避安全措施的检测。即使图像文件经过扫描，恶意有效负载经过编码的事实也使其无法检测到，从而使恶意软件加载程序能够删除图像、提取隐藏的有效负载并在内存中执行它。

研究人员解释说：“用户无意看到 PNG 图像。” “这次特定攻击中使用的图像在视觉上是扭曲的。最初下载的是一个名为 DockerSystem\_Gzv3.exe 的可执行文件，以虚假软件安装包的形式提供。可执行文件的激活导致了后续的攻击阶段。”

**RAT 恶意软件巢穴激增**
Remcos RAT 越来越多地使用创造性技术进行部署。例如，今年早些时候，研究人员发现了一个被追踪为 UNC-0050 的威胁行为者，该行为者因多次使用 Remcos RAT 攻击乌克兰的组织而闻名，并使用罕见的数据传输策略针对该国政府发起了一次新颖的攻击。

与此同时，价格低于 100 美元的廉价恶意软件“套餐”的增加正在推动利用 RAT 的活动增加，这些 RAT 经常隐藏在电子邮件附加的看似合法的 Excel 和 PowerPoint 文件中。

去年，Remcos RAT 间谍软件还被发现利用旧的 Windows UAC 绕过技术来针对东欧的组织，去年 3 月和 4 月在美国报税截止日期之前针对会计师的活动中也发现了 Remcos RAT 间谍软件。

Morphisec 研究人员告诉 Dark Reading：“正如在最新攻击中观察到的那样，威胁行为者越来越多地使用防御规避技术来绕过签名检测和基于行为的端点保护解决方案。” “在这种情况下，我们观察到隐写术和内存注入作为规避技术的结合使用。”

他们补充说，“因此，安全领导者应该考虑威胁形势的这些变化，并考虑采用可以通过减少此类潜在攻击的暴露来增强深度防御的解决方案。”

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293466](/post/id/293466)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**8赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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