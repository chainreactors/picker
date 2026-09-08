---
title: 深夜4小时，ChatGPT、Claude、Grok集体宕机：AI的根基正在动摇
url: https://www.anquanke.com/post/id/316083
source: 安全客-有思想的安全新媒体
date: 2026-09-07
fetch_date: 2026-09-08T06:40:02.755996
---

# 深夜4小时，ChatGPT、Claude、Grok集体宕机：AI的根基正在动摇

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

# 深夜4小时，ChatGPT、Claude、Grok集体宕机：AI的根基正在动摇

阅读量**27933**

发布时间 : 2026-09-07 21:16:26

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

ChatGPT、Claude、Grok等主流AI模型集体宕机近4小时，矛头直指云基础设施，AI时代脆弱性第一次暴露在聚光灯下。

深夜的手机震个不停，群里全是同一句话：”你那边AI挂了吗？”9月3日晚间这场事故，不是某个小厂的服务抖动，而是ChatGPT、Claude、Grok、Copilot集体”失联”。从业这么多年，我头一回看到全球主流AI服务在同一时间瘫痪，持续了近4个小时。作为天天靠AI干活的人，那夜我盯着故障面板后背发凉：我们是不是把太多东西，押在了一条随时会断的线上。

# **一、一场”有报告以来最大规模”的AI宕机**

故障从9月3日上午9点半（美东时间）的ChatGPT开始爆发。全球最大服务监测网站Downdetector在20分钟内收到超过12000份用户报告，页面加载失败、对话中断、API调用超时接连出现。几乎同一时刻，Anthropic的Claude、xAI的Grok、微软Copilot、谷歌Gemini相继异常，整个北美的故障地图一片飘红。

波及面远超聊天应用。用Cursor写代码的开发者最先抓狂，底层模型一瘫，代码补全和智能建议直接失效，团队当晚集体”手动加班”。推特热搜#AIdown上，用户自嘲”ChatGPT宕机了、Grok宕机了、我也宕机了”。这场事故累计持续约3小时40分钟，被业界称为”有报告以来最大规模的AI宕机事件”。

# **二、真正的震中在云端：Azure还是Cloudflare？**

这才是安全人该盯住的地方。AI模型不是故障源头，底层基础设施才是。业界把矛头指向两个”元凶”。

一是微软Azure。OpenAI、Anthropic、xAI都深度依赖Azure的算力，而AI大面积瘫痪的同时，Azure自身的故障报告也出现异常激增，时间线高度重合。

二是Cloudflare。事发时段其状态页显示两项异常：影响R2自定义域名的HTTP/3连接问题、部分WARP用户的IP地理位置识别错误。大量AI平台的流量都走Cloudflare中转，这很可能引发的正是”蝴蝶效应”。2024年11月，正是Cloudflare一次故障让Grok栽过跟头。

目前两家都还没给出官方说明。但不管真相是谁，结论已经很明显：主流AI服务的命脉，高度集中在屈指可数的几家云厂商手里。

# **三、单点失效，是AI时代最危险的安全命题**

作为安全从业者，这次事故让我想起一句话：Downtime is the new breach，宕机就是新时代的”事件”。传统安全关注”谁入侵了我”，AI时代更该问的是”我依赖谁活”。

想一想：当你的招标文件、售前方案、核心代码、客户话术全都跑在大模型API上，当你的工具链建立在”上游AI必须在线”的假设上，上游某个机房的抖动，就能让你的整个业务链瞬间停摆。这不是科幻，就是9月3日晚真实发生的事。

更麻烦的是，这种依赖还在加速加深，而我们连故障根因都还在猜。多云容灾成本高，数据合规又绑定了云区域，很多企业明知单点风险，却无路可退。

# **四、给运维和安全的四个立即行动**

别等下次再慌了，现在就能做。

第一，梳理AI供应链清单。哪些业务跑了GPT、Claude还是Gemini，底层落在哪朵云、哪条链路，画清楚依赖地图。灾难恢复的前提，是知道自己在依赖什么。

第二，给关键业务留”降级预案”。AI挂了用什么兜底？人工流程、本地小模型、还是备用API？预案不能只写在PPT里。

第三，盯紧Azure、Cloudflare这类基础设施的状态页，接上心跳告警，别等用户在群里炸了才知道。

第四，把”模型路由+多供应商”纳入架构设计。核心生产链路尽量做多供应商切换，哪怕多付点钱，也比一次集体宕机拖垮全公司划算。

# **五、写在最后：AI的新基建，需要新的安全观**

那夜宕机恢复后，有个AI平台在X平台发文”我们还活着”，成了全网梗图。可笑过之后，每个做安全的同行心里都有数：这次是”断联”，下一次可能就是”失控”。

AI是新时代的水电，但水管很细，电网也不够硬。真正负责的安全团队，不该只盯着模型输出有没有偏见、提示词有没有注入，更要盯住托着AI的那块地基稳不稳。地基一旦塌了，上层的智能再强大，也只是精致而无处安放的废墟。

下个凌晨，当你的告警面板又开始飘红，先问一句：这次断的，是模型，还是命脉？

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/316083](/post/id/316083)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **61**

* 粉丝
* **3**

### TA的文章

* ##### [深夜4小时，ChatGPT、Claude、Grok集体宕机：AI的根基正在动摇](/post/id/316083)

  2026-09-07 21:16:26
* ##### [CISA连夜拉黑7个在野漏洞：黑客正顺着LiteLLM偷你的大模型密钥](/post/id/316075)

  2026-09-04 10:47:46
* ##### [漏洞开始工业化生产：AI让黑客的经验可以复制粘贴了](/post/id/316072)

  2026-09-03 09:20:03
* ##### [Fable 5.1 发布几小时就被"扒光"：27万字提示词泄露，暴露了AI行业最大的软肋](/post/id/316063)

  2026-09-02 14:24:18
* ##### [Aiker World社区 AI 联创基地落地海南东方：从赛场到产业，共建 AI 新生态](/post/id/316048)

  2026-09-01 10:32:25

### 相关文章

* ##### [CISA连夜拉黑7个在野漏洞：黑客正顺着LiteLLM偷你的大模型密钥](/post/id/316075)

  2026-09-04 10:47:46
* ##### [漏洞开始工业化生产：AI让黑客的经验可以复制粘贴了](/post/id/316072)

  2026-09-03 09:20:03
* ##### [Fable 5.1 发布几小时就被"扒光"：27万字提示词泄露，暴露了AI行业最大的软肋](/post/id/316063)

  2026-09-02 14:24:18
* ##### [Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件](/post/id/315903)

  2026-07-31 13:50:09
* ##### [《AI编程工具“塌房”实录：Grok Build整库上传、Claude Code后门暗桩，哪个更让你睡不着？》](/post/id/315858)

  2026-07-28 10:19:37
* ##### [OpenAI智能体逃逸事件是AI时代的分水岭](/post/id/315851)

  2026-07-24 17:52:26
* ##### [Claude 开始自己审自己写的代码了 —— Anthropic 把"安全研究员"塞进了终端](/post/id/315847)

  2026-07-23 18:53:17

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