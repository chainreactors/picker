---
title: 腾讯一口气出了两只「龙虾」，QClaw 和 WorkBuddy 到底在抢什么？
url: https://mp.weixin.qq.com/s/a9K-6rCP32TLgBiZqsCJtg
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:03:23.493727
---

# 腾讯一口气出了两只「龙虾」，QClaw 和 WorkBuddy 到底在抢什么？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZVYP60vud5OxXZt49t9ricYMN50YMJq8OHNo4yvrzibkOh7iaS0STu2dIba9ibRXtCzHRs9ZzzN6U42ibutdgDIaCTMSfEibcRraVS4hZL6I8Xv00/0?wx_fmt=jpeg)

# 腾讯一口气出了两只「龙虾」，QClaw 和 WorkBuddy 到底在抢什么？

零知实验室

![]()

在小说阅读器中沉浸阅读

# 腾讯一口气出了两只「龙虾」，QClaw 和 WorkBuddy 到底在抢什么？

3 月初，深圳腾讯大厦楼下出现了一条奇特的队伍。

几百人在室外排队，等着领一个免费的 AI 安装名额。一小时内抢光。现场有人问：装的是什么？回答是：OpenClaw，就是那个「小龙虾 AI」。

马化腾在朋友圈转发了那条新闻，配了一句话：**「没想到会这么火。」**

三天后，腾讯放出了两款自己的产品——QClaw 和 WorkBuddy。

---

## 先说说，「小龙虾」究竟是什么来头

故事要从 2025 年底讲起。

一个奥地利的退休程序员，写了一个让 AI 直接操控电脑桌面的脚本——能看屏幕、点鼠标、敲键盘。他随手画了一只红色龙虾当图标，起名叫 OpenClaw，传到了 GitHub。

结果这只「虾」炸了。两个月内，GitHub Star 数突破 25 万，成为全球有史以来获星最快的开源项目。

热度来自一个朴素的原因：过去所有的 AI，包括 ChatGPT、Kimi、豆包，都是「嘴强王者」——问一个问题，给你一段回答，然后你自己去干。OpenClaw 不一样，它是真的帮你**动手**。告诉它「整理桌面文件」，它就自己去整理，不是教你怎么做，是直接做。

春节期间，猎豹移动 CEO 傅盛用 OpenClaw 搭了一个 AI 团队，产出了公众号 10 万+ 文章和 Twitter 百万浏览。「养龙虾」这个词，从极客圈一路烧到了大众社交网络。

![小龙虾AI爆火，全网掀起](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZVYP60vud5PMiaNZpa7bxSIaR7oIZyw8JXu9nSXYicpsOGJVIh2zhqlPKG9SHAM00aZuQwjk5FJcCO8VeeM5cBuicvFWIzGcDxnGX9RPicGEb5s/640?wx_fmt=jpeg "小龙虾AI爆火，全网掀起")

但原版 OpenClaw 有个硬伤：**门槛太高**。要配 Python 环境，要调试 API，要处理依赖报错，要写配置文件。懂代码的人能玩，普通人基本放弃。

这个缺口，就是腾讯看到的机会。

---

## 腾讯的两步棋

3 月 9 日，腾讯发布了两款产品，定位截然不同。

### QClaw：让普通人装进微信的小龙虾

QClaw 出自腾讯电脑管家团队，本质上是 OpenClaw 的**本地一键启动包**。

不需要懂代码，不需要配环境，下载安装完直接用。内置 Kimi、MiniMax、GLM、DeepSeek 等国产大模型，不用自己找 API。最关键的一步：**扫码绑定微信**，完成。

绑定之后，你手机上的微信就变成了遥控器。出门在外，打开微信给 QClaw 发一条消息：「帮我把桌面上这周的文件整理一下」，家里的电脑就开始动了。任务完成，结果直接发回到你的手机。

腾讯的野心写在这个设计里：让 AI Agent 钻进 14 亿人每天都在用的聊天框。你不用下新 App，不用学新界面，就是发条消息。

目前 QClaw 以邀请制内测形式开放，支持 Windows 和 macOS，访问 qclaw.qq.com 可申请资格。

![QClaw：微信直连，远程操控本地电脑](https://mmbiz.qpic.cn/mmbiz_jpg/ZVYP60vud5MELD3zEUFI3vicAlO5EvShicJkLnqbIiaLFJmN6NwXoOq6l9b8Hj5g7VCcX1ribFEGzsPRMzAufCNuC53p0ibtumJWZxpVZfpia5q1o/640?wx_fmt=jpeg "QClaw：微信直连，远程操控本地电脑")

---

### WorkBuddy：冲着办公场景去的「AI 一号员工」

如果说 QClaw 是 C 端入口，WorkBuddy 就是腾讯在 B 端的正式答卷。

WorkBuddy 由腾讯云 CodeBuddy 团队打造，3 月 9 日正式上线，面向职场和企业用户。

它不是把 OpenClaw 包一层，而是完全兼容 OpenClaw 生态的独立开发产品，号称\*\*「你的第一个 AI 员工」\*\*。

几个核心数字：

* **2000+**：上线前，腾讯内部已有超过 2000 名不同岗位员工参与内测，覆盖 HR、运营、销售、行政
* **1 分钟**：从下载安装到连接企业微信，最快 1 分钟完成
* **5000 Credits**：上线即送，直接用于 AI 执行任务，零成本体验

WorkBuddy 支持的场景比 QClaw 更深：数据处理与分析、本地知识库搭建、文案创作、海报生成、自动化审批流……并且打通了企业微信、QQ、飞书、钉钉等主流办公工具。

两款产品合起来，腾讯的意图就很清晰：QClaw 抢用户入口，WorkBuddy 抢工作流入口。

---

## 它们到底抢的是什么？

很多人看这场竞争，还是停留在「又来了两个聊天机器人」的层面。

这个判断低估了这场战争的本质。

大厂抢的不是对话框，而是三层入口：

**第一层：用户发出第一句指令的地方。** 微信？飞书？钉钉？还是一个陌生的新 App？谁在这里，谁就拿到了用户的注意力入口。QClaw 把这个入口锁在了微信里。

**第二层：工作流发生的地方。** 用户每天处理的不是「聊天」，而是文档、表格、审批、日程、知识库、周报……谁能把 AI 嵌进这些高频动作，谁就不是工具，是基础设施。WorkBuddy 瞄准的正是这里。

**第三层：真正动手执行的地方。** 能调用工具、改文档、查数据、跨应用传递上下文——这才是「会干活的 AI 同事」，而不是「会聊天的 AI 助理」。

腾讯用两个产品，同时布局了这三层。

---

## 行业格局：这只是一场更大战争的开场

腾讯出手之后，其他厂商并没有缺席。

阿里巴巴开源了桌面 Agent 工具 CoPaw，把 AI 的记忆、工具调用、定时任务做了深度解耦，面向开发者和企业的可定制场景。

字节跳动的火山引擎上线了 ArkClaw，走云端 SaaS 路线，打开网页就能用，再通过飞书插件深度接入日程、文档、群聊上下文。

Kimi 推出了 Kimi Claw，国内第一个云端托管的 OpenClaw 服务，1 分钟创建，连配置都免了。据悉 Kimi K2.5 发布不到一个月，近 20 天收入已超过 2025 年全年总收入。

每家打法都不一样，但目标高度一致：成为用户和 AI 之间那个**默认的中转站**。

谁能拿到这个位置，谁就掌握了下一个时代的流量分配权。

---

## 写在最后

OpenClaw 是一个奥地利退休程序员在空闲时间写出来的。他大概没想到，一只红色龙虾图标会在一年内引发中国科技公司最密集的产品战之一。

腾讯发布 QClaw 和 WorkBuddy，不是在做「AI 功能跟进」，而是在抢一个比模型更重要的东西：**用户打开 AI 的那个入口**。

模型会越来越像水和电——不可或缺，但无从垄断。
真正的护城河，是用户习惯。
是那个让你每天早上第一句话说给 AI 听的地方。

腾讯选择了微信。这可能是这场战争里最重的一张牌。

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5N1yD1WgdHm2D8koFa6Qm87eZVxluosiaFakickibH5ic5pI9Sm6VYH7SQVXEJ3xOMJsNPGWxAXvGrxxiaAAb5hVhuYY8SmuITelsmc/0?wx_fmt=png)

零知实验室

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5N1yD1WgdHm2D8koFa6Qm87eZVxluosiaFakickibH5ic5pI9Sm6VYH7SQVXEJ3xOMJsNPGWxAXvGrxxiaAAb5hVhuYY8SmuITelsmc/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过