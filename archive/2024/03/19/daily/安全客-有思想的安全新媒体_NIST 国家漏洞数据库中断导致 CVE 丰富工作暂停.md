---
title: NIST 国家漏洞数据库中断导致 CVE 丰富工作暂停
url: https://www.anquanke.com/post/id/294036
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:47.671880
---

# NIST 国家漏洞数据库中断导致 CVE 丰富工作暂停

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

# NIST 国家漏洞数据库中断导致 CVE 丰富工作暂停

阅读量**96611**

发布时间 : 2024-03-18 11:05:21

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.infosecurity-magazine.com/news/nist-vulnerability-database/>

译文仅供参考，具体内容表达以及含义原文为准。

美国国家标准与技术研究院 (NIST) 正在发生一些神秘的事情，这可能会使许多组织容易受到威胁行为者的攻击。

自 2024 年 2 月 12 日起，NIST 几乎完全停止丰富其国家漏洞数据库 (NVD) 中列出的软件漏洞，NVD 是全球使用最广泛的软件漏洞数据库。

固件安全提供商 NetRise 的首席执行官 Tom Pace 告诉Infosecurity，自该日期以来发布的 2700 个漏洞（称为常见漏洞和暴露 (CVE)）中只有 200 个得到了丰富。

未能丰富 CVE 意味着添加到数据库中的 2500 多个漏洞已上传，而没有关键的元数据信息。

此信息包括对漏洞和可能导致利用的软件“弱点”的描述（称为常见弱点和暴露，或 CWE）、受影响的软件产品的名称、漏洞的关键性评分 (CVSS) 以及漏洞的修补状态。

**NVD 上的浓缩数据上传大幅下降**

该问题首先由软件安全提供商 Anchore 的安全副总裁 Josh Bressers 发现，他于 3 月 8 日发布了一篇博文，显示 NVD 上的浓缩数据自 2 月 12 日左右以来大幅下降。

![来源：锚点]()

来源：锚点

思科威胁检测与响应首席工程师 Jerry Gamblin 分享了另一张图表，显示与 2023 年相比，处于“已分析”状态的 CVE 显着下降，这意味着它们已得到完整记录，而“等待分析”的 CVE 则有所增加。

![来源：思科]()来源：思科

Gamblin 和NetRise的其他帖子表明，富含关键元数据（例如 CWE、通用产品枚举器 (CPE) 和关键性评分 (CVSS)）的已发布 CVE 数量也出现类似下降。

因此，尽管发布了新漏洞，但它们目前并未标记到特定产品，从而使组织无法了解特定漏洞可能影响其环境中的哪些产品和系统。

软件安全提供商 Chainguard 联合创始人兼首席执行官 Dan Lorenc在接受Infosecurity采访时评论道：“NVD 似乎完全放弃了向 CVE 添加 CPE 匹配，这意味着 CVE 条目不包含有关软件的任何元数据实际上受到了影响。”

3 月 13 日，Anchore 的 Bressers 分享了第一张图的更新版本，确认过去 30 天内只有很少的 CVE 得到了丰富。

![来源：锚点]()来源：锚点

**整个网络安全社区的“大问题”**

如果此类问题不能迅速解决，可能会对安全研究人员社区和全球所有组织产生重大影响。

NetRise 的 Pace 解释道：“这意味着你要求整个网络安全社区在一夜之间以某种方式找出操作系统、软件包、应用程序、固件或设备中存在哪些漏洞。这是一项完全不可能完成的任务！”

洛伦克对此表示同意，并称该事件是一个“大问题”。

“我们现在依靠行业警报和社交媒体来确保我们尽快对 CVE 进行分类，”他说。

“扫描仪、分析器和大多数漏洞工具都依赖 NVD 来确定哪些软件受到哪些漏洞的影响，”Lorenc 补充道。“如果组织无法有效地对漏洞进行分类，就会面临更大的风险，并在漏洞管理方面留下重大差距。”

**NIST 暗示成立新 NVD 联盟**

2 月 15 日，国家漏洞数据库网站宣布，用户可能会遇到“分析工作延迟”，因为 NIST“目前正在努力建立一个联盟，以解决 NVD 计划中的挑战并开发改进的工具和方法。”

Aquia 总裁 Chris Hughes 表示，这条消息没有为安全界提供足够的信息。

“这个联盟到底是什么，谁将参与其中，将做出哪些改变，以及当涉及到从最广泛使用的漏洞数据库进行漏洞分析时，我们作为一个行业会看到什么样的延迟？” Hughes在 3 月 11 日 Substack 上的 Resilient Cyber 时事通讯中发表的一篇文章中写道。

当 NetRise 的 Pace 读到 NVD 的公告时，他感到很惊讶。“多年来，我们一直按照相同的流程披露和丰富漏洞，而且效率很高。为什么我们现在需要一个财团？”

截至发稿时，NVD 网站尚未发布任何进一步的公告。

Infosecurity已联系 NIST 和 MITRE（一家负责维护 CVE 的美国非营利组织），但截至撰写本文时，他们尚未回复评论请求。

**解释 NVD 联盟必要性的假设**

这些 NVD 中断的原因或需要建立一个联盟仍不清楚。

Hughes 表示，此前 NVD 利益相关者内部曾讨论过更换 CPE 的问题。这种替代品可以是软件识别 (SWID) 标签，这是可信计算组织 (TCG) 和互联网工程任务组 (IETF) 支持的软件标签标准。

不过，他表示这不太可能发生。“鉴于 SWID 作为业界领先的格式已被排除在有关软件物料清单 (SBOM) 的讨论之外，相反，我们看到来自 OWASP 的 CycloneDX 和来自 Linux 基金会的 SPDX 主导了 SBOM 格式的讨论。”

“另一个有用的说明是，考虑到软件包和开源软件 (OSS) 的普遍使用，目前有一些被称为“SBOM 论坛”的人主张 NVD 也采用软件包 URL (PURL)，但这是否会实现仍有待确定，”休斯补充道。

此类内部讨论可能促使 NVD 围绕新成立的财团进行重组。

不管出于什么原因，洛伦克批评内务部在沟通方面缺乏透明度。他补充说，这并不是安全界第一次严厉批评 NIST 运营的团队。

“特别是在过去的一年里，NVD 受到了行业和那些致力于修复破碎的漏洞生态系统的人们的密切关注。从历史上看，NVD 解决了巨大的可见性差距，但今天，它已经落后了，”Lorenc 解释道。

“因此，我们开始看到其他资源的出现，以及一些国家正在考虑创建自己的资源。这在欧盟的网络弹性法案中最为明显，”他说。

大西洋理事会最近的一项分析显示，中国最近还更新了其漏洞披露生态系统。

**美国联邦政府向承包商发布 NVD 要求**

这一事件恰逢联邦风险和授权管理计划 (FedRAMP Rev. 5) 最新修订版的发布，这是一项美国联邦法律，要求任何想要与联邦政府开展业务的公司使用 NVD 作为事实来源并修复其中所有已知的漏洞。

洛伦茨指出：“感觉 NIST 正试图以某种方式终止或放弃该计划，而政府其他部门却在强制采用该计划。”

除了丰富度下降之外，NVD API 也遇到了前所未有的规模问题，促使漏洞情报提供商 VulnCheck 发布了名为 VulnCheck NVD++ 的免费替代方案。

Infosecurity 已联系 NIST 和 MITRE，但截至撰写本文时，它们尚未回复评论请求。

本文翻译自 [原文链接](https://www.infosecurity-magazine.com/news/nist-vulnerability-database/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294036](/post/id/294036)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/nist-vulnerability-database/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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