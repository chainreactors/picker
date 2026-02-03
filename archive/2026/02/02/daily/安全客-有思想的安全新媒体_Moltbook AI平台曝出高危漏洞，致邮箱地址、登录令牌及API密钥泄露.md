---
title: Moltbook AI平台曝出高危漏洞，致邮箱地址、登录令牌及API密钥泄露
url: https://www.anquanke.com/post/id/314663
source: 安全客-有思想的安全新媒体
date: 2026-02-02
fetch_date: 2026-02-03T04:08:22.727519
---

# Moltbook AI平台曝出高危漏洞，致邮箱地址、登录令牌及API密钥泄露

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

# Moltbook AI平台曝出高危漏洞，致邮箱地址、登录令牌及API密钥泄露

阅读量**19622**

发布时间 : 2026-02-02 16:11:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/moltbook-ai-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

由辛烷值人工智能公司（Octane AI）的马特・施利希特于 2026 年 1 月末推出的新晋 AI 智能体社交网络**Moltbook 曝出高危漏洞**，在平台号称拥有 150 万 “用户” 的热度之下，其注册主体的邮箱地址、登录令牌及 API 密钥均遭泄露。

研究人员发现，该平台存在**数据库配置暴露漏洞**，未授权人员可直接访问智能体档案，还能对数据进行批量提取操作。

此次漏洞问题还与平台**账号创建无频率限制**的问题叠加出现 —— 据悉，一个名为 OpenClaw 的智能体（@openclaw）已注册 50 万个虚假 AI 用户，直接戳破了媒体所称平台用户为自然增长的说法。

### 平台运行机制

Moltbook 支持基于 OpenClaw 技术的 AI 智能体发布内容、发表评论，并创建类似 m/emergence 的 “子社群（submolts）”，各类智能体围绕 AI 涌现、报复性信息泄露、索拉纳代币刷量等话题展开互动交锋。

平台目前已涌现超 2.8 万条帖子和 23.3 万条评论，吸引了 100 万名沉默的人类验证者关注。但智能体的实际数量存在造假情况：由于缺乏创建限制，各类机器人程序大肆批量注册账号，为平台营造出病毒式传播的虚假繁荣。

平台存在**暴露的接口端点**，该端点关联着配置不安全的开源数据库，攻击者只需通过`GET /api/agents/{id}`这类简单查询指令，即可实现智能体数据泄露，**全程无需任何身份验证**。

| 泄露字段 | 字段描述 | 影响示例 |
| --- | --- | --- |
| email | 与智能体所有者绑定的邮箱地址 | 针对智能体背后的人类主体发起定向钓鱼攻击 |
| login\_token | 智能体的 JSON Web Token 登录会话令牌 | 完全劫持智能体账号，操控其发布内容、发表评论 |
| api\_key | 对接 OpenClaw / 安索普公司（Anthropic）的 API 密钥 | 向关联服务（邮箱、日历）泄露数据 |
| agent\_id | 可用于枚举遍历的连续编号 ID | 批量爬取 50 万个以上虚假账号的相关数据 |

攻击者可通过枚举 ID 的方式，快速获取数以千计的信息记录。

### 安全风险与专家警示

此次**不安全的直接对象引用（IDOR）/ 数据库信息暴露漏洞**，构成了一套 “致命三重威胁”：AI 智能体可访问私人数据、Moltbook 平台的输入内容未做安全校验（易遭提示词注入攻击）、平台支持智能体外部通信，多重问题叠加下，平台不仅面临凭证被盗风险，还可能遭遇文件删除等破坏性操作。

> Moltbook 当前存在严重攻击漏洞，超 150 万注册用户的邮箱地址、登录令牌、API 密钥等全部信息均可被获取。若有人能帮我联系到 Moltbook 平台的相关工作人员，本人将万分感激。
>
> 推文链接：[pic.twitter.com/xepDh4Dtjn](https://pic.twitter.com/xepDh4Dtjn)
>
> —— 纳格利（@galnagli） 2026 年 1 月 31 日

安德烈・卡帕西将该平台称为 “充满垃圾信息的规模型里程碑”，同时也直言其是 \*\*“计算机安全领域的噩梦”\*\*；比尔・阿克曼则用 “令人胆寒” 形容该平台的安全状况。平台子社群中若出现提示词注入攻击，攻击者可操控智能体泄露宿主设备数据，而 OpenClaw 技术未做沙箱隔离的执行模式，会进一步放大这一风险。

目前**暂无消息证实平台已推出漏洞修复补丁**，Moltbook 官方账号（@moltbook）对漏洞披露信息也未作任何回应。研究人员建议平台用户 / 智能体所有者：**立即吊销相关 API 密钥、为智能体配置沙箱隔离环境、对自身信息泄露情况进行审计核查**。企业用户则需警惕，不受管控的 AI 智能体正在为其带来影子 IT 架构相关安全风险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/moltbook-ai-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314663](/post/id/314663)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/moltbook-ai-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/moltbook-ai-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **990**

* 粉丝
* **6**

### TA的文章

* ##### [明修栈道，暗度陈仓：TA584组织投放“傲娇僵尸程序”并利用隐形注册表项实施攻击](/post/id/314678)

  2026-02-02 16:32:30
* ##### [苹果为十年前iPhone推出史无前例的安全更新，标志着老旧设备支持策略生变](/post/id/314675)

  2026-02-02 16:15:59
* ##### [太空探索技术公司的大胆布局：星链数据中心卫星如何重塑云计算经济格局](/post/id/314671)

  2026-02-02 16:12:53
* ##### [飞塔单点登录配置漏洞暴露企业认证系统核心安全隐患](/post/id/314667)

  2026-02-02 16:12:24
* ##### [签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用](/post/id/314681)

  2026-02-02 16:11:51

### 相关文章

* ##### [明修栈道，暗度陈仓：TA584组织投放“傲娇僵尸程序”并利用隐形注册表项实施攻击](/post/id/314678)

  2026-02-02 16:32:30
* ##### [苹果为十年前iPhone推出史无前例的安全更新，标志着老旧设备支持策略生变](/post/id/314675)

  2026-02-02 16:15:59
* ##### [太空探索技术公司的大胆布局：星链数据中心卫星如何重塑云计算经济格局](/post/id/314671)

  2026-02-02 16:12:53
* ##### [飞塔单点登录配置漏洞暴露企业认证系统核心安全隐患](/post/id/314667)

  2026-02-02 16:12:24
* ##### [签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用](/post/id/314681)

  2026-02-02 16:11:51
* ##### [工业控制系统监控与数据采集漏洞引发拒绝服务攻击，或对工业生产运营造成中断影响](/post/id/314653)

  2026-02-02 16:11:14
* ##### [“修复”实为陷阱：ConsentFix钓鱼攻击借Azure CLI绕过多重身份验证](/post/id/314685)

  2026-02-02 16:11:09

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