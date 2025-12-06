---
title: Cloudflare 拦截史上最大规模 29.7 Tbps DDoS 攻击 幕后为 Aisuru 僵尸网络
url: https://www.anquanke.com/post/id/313618
source: 安全客-有思想的安全新媒体
date: 2025-12-05
fetch_date: 2025-12-06T03:10:12.756869
---

# Cloudflare 拦截史上最大规模 29.7 Tbps DDoS 攻击 幕后为 Aisuru 僵尸网络

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

# Cloudflare 拦截史上最大规模 29.7 Tbps DDoS 攻击 幕后为 Aisuru 僵尸网络

阅读量**14039**

发布时间 : 2025-12-05 17:23:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/cloudflare-aisuru-botnet-ddos-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全与基础设施公司**Cloudflare**发布的一份全面 DDoS 威胁报告显示，2025 年第三季度互联网遭遇了猛烈的网络攻击浪潮。这一时期的攻击主要由名为**Aisuru**的臭名昭著物联网（IoT）僵尸网络主导，它发起了多起史上规模最大的攻击事件。

Aisuru 被认为是由全球**100 万至 400 万台被劫持设备**组成的庞大网络，其攻击力足以出租给任何想要制造混乱的人，租金仅需**数百至数千美元**。

#### Aisuru 的空前攻击规模

Cloudflare 报告称，Aisuru 发起了一场创下世界纪录的 DDoS 攻击，峰值流量达到**29.7 太比特 / 秒（Tbps）** ，数据包速率高达**141 亿包 / 秒（Bpps）** 。

这一流量规模通过**UDP 地毯式轰炸**技术实现，甚至可能导致美国等地区的主要互联网服务提供商（ISP）遭受 “连带性互联网中断”—— 即便这些 ISP 并非主要攻击目标，数百万用户的网络服务仍会出现变慢或中断的情况。

![]()

自 2025 年初以来，Cloudflare 已拦截**2867 起 Aisuru 发起的攻击**，其中仅第三季度就有 1304 起大规模 “超容量型” 攻击，较上一季度激增**54%** 。

值得注意的是，整体来看，Cloudflare 的自动化系统在该季度共拦截了**830 万起 DDoS 攻击**，较去年同期增长**40%** 。有趣的是，两种主要攻击类型呈现出截然不同的趋势：**网络层攻击**激增**87%** ，而**HTTP 攻击**实则下降**41%** 。此外，绝大多数攻击（包括 71% 的 HTTP 攻击和 89% 的网络层攻击）持续时间不足**10 分钟**，这凸显了人工响应时间面临的严峻挑战。

### 地缘政治影响攻击目标

部分行业受到的冲击尤为严重。2025 年第三季度，**信息技术与服务行业**是整体遭受攻击最多的行业，紧随其后的是**电信行业**以及**博彩与赌场行业**。

然而，受现实世界事件影响，部分领域的攻击频率出现急剧飙升。例如，**人工智能（AI）公司**报告遭遇的 DDoS 攻击流量最大，2025 年 9 月攻击量暴涨**347%** —— 这一时间段恰逢公众对 AI 监管的讨论日益升温。

同样，**汽车行业**的攻击增幅最为显著，在受攻击行业排名中跃升**62 位**；紧随其后的是**采矿、矿产与金属行业**，这与欧盟和中国之间日益加剧的贸易紧张局势密切相关。

就受影响国家而言，**马尔代夫（排名上升 125 位）** 和**法国（排名上升 65 位）** 在全国性抗议活动期间的攻击增幅最为突出，这表明威胁行为者更倾向于在社会动荡时期针对目标网站发起攻击。

尽管如此，**中国**仍是受攻击最多的国家，紧随其后的是土耳其、德国、巴西以及**美国（排名上升 11 位）** 。令人意外的是，**印度尼西亚**连续第四个季度成为全球最大的攻击源国，前十大攻击源中有七个位于亚洲。![]()

#### 自动化防御是关键

Cloudflare 得出结论：由于如今大多数攻击 “速度过快，任何人工或按需服务都无法及时响应”，企业在当前数字时代必须更多依赖**自动化系统**才能保障安全。

“网络犯罪分子从各个角度发起攻击，其尝试极为顽固。尽管此次攻击已被成功缓解，但这一事件明确提醒我们：以流量为核心的 DDoS 攻击活动仍在快速演变，其速度远超大多数组织的防御能力，”ESET 全球网络安全顾问**杰克・摩尔（Jake Moore）** 表示。

在评论 Aisuru 僵尸网络的重要性时，摩尔强调：“该僵尸网络的攻击规模及其采用的**高度随机化流量**表明，仅依赖**传统过滤机制**或**静态规则**并不总能奏效；此外，DDoS 攻击是一种巧妙的攻击方式 —— 无需真正入侵网络即可针对企业发起攻击，且攻击者能在很大程度上保持匿名，这使其在破坏方面极具成效。”

“然而，即便有了当前完善的防护措施，威胁行为者的装备每年都在升级，还会大规模使用更多 IP 地址来**淹没（flood）** 系统，这使得防护难度日益增加。企业需要再次持续探索如何构建**具备前瞻性的网络防御体系**，并时刻准备应对各种意外情况，” 他建议道。

本文翻译自hackread [原文链接](https://hackread.com/cloudflare-aisuru-botnet-ddos-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313618](/post/id/313618)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/cloudflare-aisuru-botnet-ddos-attack/)

如若转载,请注明出处： <https://hackread.com/cloudflare-aisuru-botnet-ddos-attack/>

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
* **780**

* 粉丝
* **6**

### TA的文章

* ##### [AI boom 催生全球存储芯片荒 价格将涨三倍至 2027 年](/post/id/313587)

  2025-12-05 17:36:12
* ##### [哈维 AI 完成 7.6 亿美元融资 估值达 80 亿美元](/post/id/313583)

  2025-12-05 17:35:29
* ##### [Cacti 中存在高危漏洞（CVE-2025-66399），通过SNMP团体字符串注入可导致远程代码执行](/post/id/313602)

  2025-12-05 17:34:09
* ##### [“PDF陷阱”：Apache Tika核心组件存在严重漏洞（CVE-2025-66516，CVSS 10.0）](/post/id/313590)

  2025-12-05 17:33:30
* ##### [APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动](/post/id/313606)

  2025-12-05 17:31:23

### 相关文章

* ##### [AI boom 催生全球存储芯片荒 价格将涨三倍至 2027 年](/post/id/313587)

  2025-12-05 17:36:12
* ##### [哈维 AI 完成 7.6 亿美元融资 估值达 80 亿美元](/post/id/313583)

  2025-12-05 17:35:29
* ##### [Cacti 中存在高危漏洞（CVE-2025-66399），通过SNMP团体字符串注入可导致远程代码执行](/post/id/313602)

  2025-12-05 17:34:09
* ##### [“PDF陷阱”：Apache Tika核心组件存在严重漏洞（CVE-2025-66516，CVSS 10.0）](/post/id/313590)

  2025-12-05 17:33:30
* ##### [APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动](/post/id/313606)

  2025-12-05 17:31:23
* ##### [Splunk中存在高危漏洞，因Windows平台上的不当文件权限设置，可导致本地攻击者实现权限提升](/post/id/313598)

  2025-12-05 17:30:23
* ##### [智能可观测平台Dynatrace深化其AWS服务集成，新增多项AI与云原生监控功能](/post/id/313610)

  2025-12-05 17:29:29

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