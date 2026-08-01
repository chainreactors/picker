---
title: Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件
url: https://www.anquanke.com/post/id/315903
source: 安全客-有思想的安全新媒体
date: 2026-07-31
fetch_date: 2026-08-01T05:11:46.579751
---

# Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件

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

# Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件

阅读量**32426**

发布时间 : 2026-07-31 13:50:09

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/>

译文仅供参考，具体内容表达以及含义原文为准。

Anthropic 今日表示，在内部安全测试中，其某一款 Claude 模型构建了一个恶意 Python 软件包并将其上传到 PyPI，在该软件包被 PyPI 的自动化防御机制移除之前，它已在 15 台真实系统上运行过。

![]()

该公司披露称，这并非孤例——在总共三起事件中，Claude 模型从一个本应被完全隔离的评估环境中”越狱”接触到开放互联网，进而攻陷了三家组织的生产基础设施。

此次审查是在 OpenAI 于 7 月 21 日披露的消息之后进行的——OpenAI 当时称其模型逃出了隔离测试环境，接触到了 Hugging Face 的生产基础设施。JFrog 随后证实，这些模型是利用自托管 Artifactory 中的零日漏洞实现逃逸的。

# **抢占一个从未存在过的包名**

这三起事件均发生在由第三方评估合作方 Irregular 组织的”夺旗”（capture-the-flag）演练中。Anthropic 在提示词中告诉 Claude 它没有互联网访问权限，且环境是模拟的。然而，一处配置错误导致这两点都不属实，而两家公司直到上周才察觉。

在 PyPI 事件中，Claude 在测试环境内发现了一份文档，文档伪装成某虚构公司的开发者配置说明。

这些说明告诉新员工要安装一个从未发布过的 Python 软件包——一个”幽灵依赖”。

Claude 判断出，如果自己抢先注册这个包名，目标机器就会自动拉取它的代码。

发布这个包并不容易。Claude 需要一个 PyPI 账号，而注册账号需要邮箱地址，邮箱又需要手机号。

它没能找到免费的手机号服务，随后又尝试通过多条途径获取资金来购买手机号，但均告失败。最终它退而求其次，找到了一个未被屏蔽的邮件服务商，注册了账号并上传了恶意软件。

Anthropic 表示，该软件包在公开状态下停留了约一小时。

在这段时间窗口内，15 台真实系统下载并执行了它。其中一台属于一家安全公司——该公司习惯从 PyPI 安装软件包并扫描其中的恶意代码，其工作流程将注册表中的内容视为”可安全运行”。

Claude 的载荷被触发，将该公司的凭据发送到它自己搭建的收集点，随后利用这些凭据进一步渗透进该公司的基础设施。Anthropic 称 Claude 并不知道这家公司的存在。

PyPI 自身的安全系统自动移除了该软件包。Anthropic 表示已通知 PyPI 团队并移交了相关入侵指标（IoC）。

这次测试所运行的模型是 Claude Mythos 5。据 Anthropic 介绍，其推理过程很早就标记出了问题，指出如果互联网是真实的，发布这个包就等同于一次真实世界攻击，并称其”不可接受，而且肯定不是预期的解法”。

随后它又自己说服自己，得出了”环境是搭建出来的”这一结论，理由是它不认识为连接提供保护的证书颁发机构，且系统显示的日历日期为 2026 年。

当自动化扫描器开始安装该软件包时，Claude 把它们当成了演练中预设的”脚本演员”。

# **凭据与一个生产数据库**

最严重的影响来自另一起涉及 Claude Opus 4.7 的事件——其中那家虚构的目标公司与一个真实域名重名。

在四次测试中，Claude 难以触及它的模拟目标，却发现那家真实公司可以通过互联网访问，于是便假定这就是预期目标。它提取了应用和基础设施的凭据，并触及了一个包含数百行生产数据的数据库。

这是唯一一例模型在确认身处真实系统后仍然持续发起攻击的情况。Anthropic 称这四次测试最终都识别出目标是真实的，其中两次测试中 Claude 推断：这家真实公司”本就该是演练的一部分”。

第三起事件涉及一个尚未发布、内部研究用的模型——它在未能触及预定目标后，扫描了约 9,000 个目标，随后利用一个暴露的调试页面中的凭据和 SQL 注入攻陷了一个面向互联网的应用。该模型后来注意到，这台主机所在的云账户与本次挑战毫无关联，于是判定目标是真实的，并自行停止了攻击。

这些攻击均未使用任何新技术。Anthropic 将它们描述为”弱口令和未鉴权的端点”。

# **后续将采取的措施**

Anthropic 于 7 月 23 日启动了审查，并在同一天叫停了所有网络安全评估。次日它识别出这三起事件，并于 7 月 27 日通知了 Irregular 及受影响组织（目前仍在尝试联系第三家）。

这三起事件中最早的一起可追溯到 4 月，这意味着部分活动在长达约三个月的时间里都未被发现。

这些评估在运行时不带通常随正式版 Claude 模型一同提供的分类器和监控机制，尽管模型仍保留了其安全训练。

Anthropic 表示，其生产环境的防护机制本可阻止此类行为，并将这些事件定性为更接近于”测试框架与运营层面的失败”，而非”模型对齐失败”——理由是在测试中模型被告知没有互联网访问权限，而事实上却有。

该公司现计划扩大对话记录（transcript）监控范围、改进调查工具，并与评估合作方加强保障工作。

公司表示正与 METR 协商进行独立审查，并将在下周内公布一份经过轻微脱敏的 PyPI 测试对话记录。

Anthropic 联系到的两家受影响组织中，没有一家是自己发现了这些活动的——与 OpenAI 的 Hugging Face 事件一样，这些活动之所以浮出水面，完全是因为负责的 AI 实验室主动去翻查了自己的对话记录。

本文翻译自 [原文链接](https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315903](/post/id/315903)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **33**

* 粉丝
* **2**

### TA的文章

* ##### [Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件](/post/id/315903)

  2026-07-31 13:50:09
* ##### [微软发布网络安全模型MAI-Cyber-1-Flash](/post/id/315895)

  2026-07-30 14:29:28
* ##### [新一轮银狐攻击\_管控终端再成控制工具](/post/id/315880)

  2026-07-30 14:08:10
* ##### [OpenAI 开源 Codex Security CLI：用于发现、验证和修复安全漏洞](/post/id/315867)

  2026-07-29 15:01:43
* ##### [PentesterFlow —— 面向渗透测试人员和漏洞赏金猎人的 AI 自动化工作流工具](/post/id/315861)

  2026-07-28 10:24:20

### 相关文章

* ##### [为了“作弊”拿高分，GPT自己黑了 Hugging Face，GLM分析取证](/post/id/315841)

  2026-07-23 11:50:13
* ##### [你家门口的摄像头，可能正在替俄罗斯情报机构"站岗"](/post/id/315830)

  2026-07-21 17:42:45
* ##### [伊朗黑客组织亮出"秘密武器"：Cavern C2框架如何绕过所有安全检测](/post/id/315763)

  2026-07-10 11:03:32
* ##### [深度分析Sorry勒索软件的加密实现与行为特征](/post/id/315390)

  2026-04-29 13:32:51
* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [虚假招聘陷阱 微软揭露针对开发者的传染性面试攻击活动](/post/id/315168)

  2026-03-13 10:31:36

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