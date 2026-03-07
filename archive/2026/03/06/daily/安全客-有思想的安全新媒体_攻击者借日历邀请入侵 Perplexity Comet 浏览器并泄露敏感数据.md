---
title: 攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据
url: https://www.anquanke.com/post/id/315044
source: 安全客-有思想的安全新媒体
date: 2026-03-06
fetch_date: 2026-03-07T03:54:37.630163
---

# 攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据

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

# 攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据

阅读量**21088**

发布时间 : 2026-03-06 10:54:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/perplexitys-comet-browser-hijacked/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

只需一封经过恶意构造的**Google 日历邀请**，就能将 Perplexity 的 Comet 浏览器变为攻击武器。Zenity Labs 安全研究人员发现了一个名为 **PerplexedBrowser** 的高危漏洞，该漏洞可诱骗 Comet 的 AI 代理读取本地文件并窃取凭证。

这种**零点击攻击**仅需要用户让 AI 代理处理一条常规会议邀请，就会暴露**智能代理浏览器在处理不可信数据时的底层设计缺陷**。

该漏洞利用流程完全在 Comet 代理内部静默执行，对用户完全不可见。

攻击始于攻击者发送一封看似正常的 Google 日历邀请。在可见的会议信息下方，大量空白区域隐藏了伪造的 HTML 元素与一段 `<system_reminder>` 代码块，用于模仿 Comet 的内部指令。

当用户让浏览器接受会议邀请时，会发生**“意图冲突（Intent Collision）”**：AI 代理将用户的合法请求与攻击者隐藏的恶意载荷合并执行。

根据 Awesome Agents 与 Zenity Labs 的研究，注入的指令会秘密迫使 Comet**在后台访问攻击者控制的网站**。

为绕过以英文为核心的安全防护机制，该恶意站点会使用**希伯来语**下发二次指令。

攻击将文件遍历行为包装成 “游戏任务”，诱导 AI 代理访问 `file://` 协议链接，读取**敏感配置文件与 API 密钥**。

最终，Comet 会将窃取的数据拼接进 URL 并跳转到攻击者服务器，**瞬间完成数据外泄**。

如果用户启用了未上锁的 **1Password 浏览器扩展**，攻击破坏力将进一步加剧。

Comet 可直接搜索密码库、提取单条记录，甚至尝试修改主密码。

尽管多因素认证可阻止账号完全沦陷，但**各类敏感密钥与 API 凭证会被完全暴露**。

---

### 结构性漏洞频发

| 漏洞名称 | 攻击载体 | 影响 |
| --- | --- | --- |
| CometJacking | 基于 URL 的提示词注入 | 内存与关联服务数据泄露 |
| Hidden MCP API | 未公开 MCP API | 任意命令执行 |
| Reddit Injection | 隐藏提示指令 | 邮箱与一次性验证码窃取 |
| UXSS | 扩展配置不当 | 任意浏览器操作 |
| Safety-Check Exfiltration | 滥用 AI 安全护栏 | 内部数据窃取 |

自 2025 年 7 月发布以来，**PerplexedBrowser** 已是 Comet 被发现的**第六个重大安全漏洞**。此前问题包括 CometJacking、可执行任意指令的隐藏 MCP API 等。

此外，研究人员还发现通过恶意 Reddit 评论实施的**提示词注入漏洞**。

Zenity 于 2025 年 10 月上报了最新这一漏洞。然而，Perplexity 花费**120 天**并通过**两次独立补丁**，才从代码层面彻底封禁 `file://` 访问。

Zenity 首席技术官 Michael Bargury 强调，这是**智能代理系统的固有结构性缺陷**，而非简单的软件 Bug。

由于大语言模型在**同一 Token 流**中同时处理可信用户指令与不可信网页内容，模型无法可靠区分二者。

知名 AI 安全专家 Simon Willison 也表达了相同担忧，他认为**智能代理浏览器扩展这一整体设计可能存在致命缺陷**。

在出现架构级修复方案前，建议用户保持密码管理器锁定状态，并严格限制 AI 代理对敏感域名的访问权限。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/perplexitys-comet-browser-hijacked/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315044](/post/id/315044)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/perplexitys-comet-browser-hijacked/)

如若转载,请注明出处： <https://cybersecuritynews.com/perplexitys-comet-browser-hijacked/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1060**

* 粉丝
* **6**

### TA的文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13

### 相关文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13
* ##### [Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包](/post/id/315032)

  2026-03-06 10:52:45
* ##### [Grammarly 从文字纠错转向文学模仿](/post/id/315029)

  2026-03-06 10:52:13
* ##### [Cisco Secure FMC曝出10分高危漏洞 攻击者可获取企业防火墙Root权限](/post/id/315023)

  2026-03-06 10:51:30

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