---
title: Google Gemini漏洞可被攻击者利用获取私人日历数据
url: https://www.anquanke.com/post/id/314409
source: 安全客-有思想的安全新媒体
date: 2026-01-21
fetch_date: 2026-01-22T03:34:34.494906
---

# Google Gemini漏洞可被攻击者利用获取私人日历数据

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

# Google Gemini漏洞可被攻击者利用获取私人日历数据

阅读量**18362**

发布时间 : 2026-01-21 18:09:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Aminu Abdullahi，文章来源：techrepublic

原文地址：<https://www.techrepublic.com/article/news-google-gemini-flaw-private-calendar-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员发现了 Google Gemini 中的一个漏洞，该漏洞允许隐藏在会议邀请中的指令**提取私人日历数据并创建具有欺骗性的日程事件**。

安全研究人员披露，Google Gemini 人工智能助手中存在一处缺陷，攻击者只需在会议邀请中植入精心构造的隐藏文本，就能悄无声息地获取用户的私人日历数据。

该漏洞由网络安全公司 Miggo 发现。该公司称，他们找到了一种绕过 Google 日历隐私控制的方法 —— 在日历事件描述中嵌入隐藏指令。在一篇解释此项研究的博客中，Miggo 指出，这一漏洞揭示了 AI 系统如何通过日常自然语言而非恶意代码被操控。

Miggo 研究主管利亚德・埃利亚胡表示：“这种绕过方式使得攻击者可以在无需用户任何直接交互的情况下，**未经授权访问私人会议数据并创建具有欺骗性的日历事件**。”

### 将 Gemini 的 “乐于助人” 变为攻击用户的工具

Gemini 在 Google 日历中扮演助手角色，可回答用户诸如 “我有哪些会议” 或 “某一天是否有空” 等问题。为此，它会自动读取事件标题、描述、时间及参会者详情。

Miggo 指出，正是这种集成机制成为了安全短板。

Miggo 解释道：“由于 Gemini 会自动导入并解析事件数据以提供帮助，攻击者只要能影响事件字段，就可以植入自然语言指令，供模型后续执行。”

在攻击场景中，攻击者向受害者发送日历邀请，事件描述中隐藏着一段用普通文字编写的提示。这段文字看起来毫无可疑之处，也不需要受害者点击任何链接。

![]()

恶意指令会一直处于休眠状态，直到受害者日后向 Gemini 提出一个正常问题（例如 “我某天是否有空”）时，就足以触发攻击代码的执行。

本文翻译自techrepublic [原文链接](https://www.techrepublic.com/article/news-google-gemini-flaw-private-calendar-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314409](/post/id/314409)

安全KER - 有思想的安全新媒体

本文转载自: [techrepublic](https://www.techrepublic.com/article/news-google-gemini-flaw-private-calendar-data/)

如若转载,请注明出处： <https://www.techrepublic.com/article/news-google-gemini-flaw-private-calendar-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **940**

* 粉丝
* **6**

### TA的文章

* ##### [珠穆朗玛峰勒索软件团伙据称宣称入侵了麦当劳印度系统](/post/id/314403)

  2026-01-21 18:10:24
* ##### [Google Gemini漏洞可被攻击者利用获取私人日历数据](/post/id/314409)

  2026-01-21 18:09:50
* ##### [新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）](/post/id/314414)

  2026-01-21 18:09:24
* ##### [密码学基础被攻破：GNU libtasn1中存在一字节溢出漏洞（CVE-2025-13151）](/post/id/314411)

  2026-01-21 18:08:43
* ##### [Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险](/post/id/314423)

  2026-01-21 18:07:57

### 相关文章

* ##### [珠穆朗玛峰勒索软件团伙据称宣称入侵了麦当劳印度系统](/post/id/314403)

  2026-01-21 18:10:24
* ##### [新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）](/post/id/314414)

  2026-01-21 18:09:24
* ##### [密码学基础被攻破：GNU libtasn1中存在一字节溢出漏洞（CVE-2025-13151）](/post/id/314411)

  2026-01-21 18:08:43
* ##### [Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险](/post/id/314423)

  2026-01-21 18:07:57
* ##### [亚马逊 100 亿美元押注 OpenAI，旨在推动AI驱动零售的变革](/post/id/314435)

  2026-01-21 18:07:21
* ##### [德以两国承诺共建网络安全联盟](/post/id/314401)

  2026-01-21 18:06:40
* ##### [X开源Grok驱动的算法代码，揭秘内容传播机制](/post/id/314428)

  2026-01-21 18:06:03

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