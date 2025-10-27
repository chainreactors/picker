---
title: Google 的 AI 工具 Big Sleep 在 SQLite 数据库引擎中发现零日漏洞
url: https://www.anquanke.com/post/id/301562
source: 安全客-有思想的安全新媒体
date: 2024-11-06
fetch_date: 2025-10-06T19:16:52.836214
---

# Google 的 AI 工具 Big Sleep 在 SQLite 数据库引擎中发现零日漏洞

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

# Google 的 AI 工具 Big Sleep 在 SQLite 数据库引擎中发现零日漏洞

阅读量**64574**

发布时间 : 2024-11-05 11:10:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html>

译文仅供参考，具体内容表达以及含义原文为准。

谷歌（Google）表示，它利用名为 Big Sleep（前身为 Project Naptime）的大型语言模型（LLM）辅助框架，在 SQLite 开源数据库引擎中发现了一个零日漏洞。

这家科技巨头将这一进展描述为使用人工智能（AI）代理发现的 “第一个真实世界的漏洞”。

Big Sleep 团队在与 The Hacker News 分享的一篇博文中说：“我们相信，这是人工智能代理在广泛使用的现实世界软件中发现以前未知的可利用内存安全问题的第一个公开例子。”

该漏洞是 SQLite 中的堆栈缓冲区下溢，当软件在内存缓冲区开始之前引用内存位置时就会发生下溢，从而导致崩溃或任意代码执行。

“根据常见弱点枚举（CWE）对该漏洞类的描述，这种情况通常发生在指针或其索引被递减到缓冲区之前的位置时，指针运算的结果是在有效内存位置开始之前的位置，或者使用了负索引。”

在负责任地披露后，该缺陷已于 2024 年 10 月初得到解决。值得注意的是，该漏洞是在库的开发分支中发现的，这意味着它在正式发布之前就被标记出来了。

谷歌在 2024 年 6 月首次详细介绍了 “Project Naptime”（Naptime 项目），这是一个用于改进自动漏洞发现方法的技术框架。此后，该项目演变为 Big Sleep，成为谷歌零项目（Project Zero）与谷歌 DeepMind 更广泛合作的一部分。

Big Sleep 的理念是利用 LLM 的代码理解和推理能力，让人工智能代理在识别和展示安全漏洞时模拟人类行为。

这需要使用一套专门的工具，让代理能够浏览目标代码库，在沙盒环境中运行 Python 脚本以生成用于模糊处理的输入，调试程序并观察结果。

我们认为这项工作具有巨大的防御潜力。谷歌说：“在软件发布之前就发现其漏洞，意味着攻击者没有竞争的余地：在攻击者有机会使用这些漏洞之前，漏洞就已经被修复了。”

不过，该公司也强调，这些仍是实验结果，并补充说：“Big Sleep 团队的立场是，目前，针对特定目标的模糊器很可能至少同样有效（发现漏洞）。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301562](/post/id/301562)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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