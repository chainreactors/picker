---
title: Claude Code 源代码在 NPM 包中意外泄露
url: https://hackernews.cc/archives/63995
source: HackerNews
date: 2026-04-01
fetch_date: 2026-04-02T04:29:45.981570
---

# Claude Code 源代码在 NPM 包中意外泄露

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-代码](https://hackernews.cc/wp-content/uploads/2026/02/data-5606639_1920.jpg)

# Claude Code 源代码在 NPM 包中意外泄露

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-01](https://hackernews.cc/archives/63995 "10:56")
分类: [AI安全](https://hackernews.cc/archives/category/ai%E5%AE%89%E5%85%A8),[安全快讯](https://hackernews.cc/archives/category/messages)
[暂无评论](https://hackernews.cc/archives/63995#respond)

* 浏览次数 217
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

人工智能公司 Anthropic 表示，**其意外泄露了 Claude Code 的源代码，该代码本为闭源。不过公司称，没有客户数据或凭证因此暴露。**

尽管 Anthropic 承诺支持开源社区，但 Claude Code 一直保持闭源状态，至少在今天之前是如此。今天的一次更新意外包含了内部源代码。

Anthropic 在向 BleepingComputer 发布的声明中证实了此次泄露事件，并表示没有个人或敏感信息被公开。

Anthropic 告诉 BleepingComputer：“今天早些时候，一次 Claude Code 发布包含了一些内部源代码。没有敏感的客户数据或凭证卷入或暴露。这是由人为失误导致的发布打包问题，并非安全漏洞。我们正在采取措施防止此类事件再次发生。”

泄露的源代码首先被寿超凡（@Fried\_rice）发现，随后在 GitHub 和其他存储平台上广泛传播。

**泄露详情**

今天早些时候，Anthropic 在 NPM 上短暂发布 Claude Code 2.1.88 版本时，不慎泄露了源代码。

这个版本包含一个 60MB 的文件 cli.js.map，其中包含最新版本的全部源代码。

源映射文件是一种调试文件，它将编译后的 JavaScript 代码与原始源代码关联起来。

如果映射文件包含一个名为 “sourcesContent” 的字段，该字段会将原始源文件的全文直接嵌入到映射中，那么就有可能从该文件重建整个源代码树。

这就是为什么在公共包中包含一个大的.map 文件可能会导致大量代码暴露的原因。

重建后的源代码包含大约 1900 个文件、50 万行代码，以及 Claude 的一些独有功能细节。

虽然源代码已在网上传播，但 Anthropic 已开始发出数字千年版权法案（DMCA）侵权通知，尽可能将其下架。

**开发者的发现与分析**

开发者们已开始分析源代码，寻找未记录的功能，并了解该应用程序的工作原理。

据亚历克斯・芬恩称，Anthropic 正在测试一种名为 “主动模式” 的新功能，在这种模式下，Claude 将全天候为你编写代码。这个模式在 Claude Code 源代码中被发现。

还有另一个有趣的功能引起了我们的注意。

它被称为 “梦想” 模式，在这种模式下，Claude 可以在后台持续思考，拓展思路，完善你当前的计划，并在你离开时尝试解决问题。

**关于 Claude Code 使用限制的问题**

另外，用户声称 Claude 悄悄降低了使用限制。这意味着，无论你是使用专业版计划还是最高级计划（5 倍用量），都会更快达到 Claude 的使用限制。

我个人在使用 Claude Personal（每月 20 美元）时就观察到了这种情况。在 Claude Code 终端向 Claude 发送几条消息后，我的用量就飙升至 30%，仅仅几分钟的交互后，用量就达到了 100%。

这并非预期的情况，尤其是考虑到交互内容量并不大，因为我才刚开始与 Claude 交流。

事实证明，这个问题很普遍，Anthropic 已确认正在调查一个导致使用限制更快耗尽的漏洞。

Anthropic 的莉迪亚・哈利在 X 平台上发文称：“我们知道大家在 Claude Code 中达到使用限制的速度比预期快得多。正在积极调查，有最新进展会及时分享。”

截至美国东部时间 3 月 31 日下午 2 点，该问题仍未解决，Anthropic 发布了以下最新消息：

“（我们）仍在处理这个问题。这是团队的首要任务。我知道这给很多人带来了困扰。一有消息就会尽快告知大家。”

一些用户认为，鉴于 Claude 在过去几周的受欢迎程度不断上升，这可能是 Anthropic 的有意之举，但在没有该公司提供更多细节的情况下，我们无法确定这是否是有意为之。

---

**消息来源：[bleepingcomputer.com](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Claude](https://hackernews.cc/archives/tag/claude)[源代码](https://hackernews.cc/archives/tag/%E6%BA%90%E4%BB%A3%E7%A0%81)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用](https://hackernews.cc/wp-content/uploads/2026/01/blue-hand-2228501_640-210x140.jpg)](https://hackernews.cc/archives/63996 "Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞")

##### [Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞](https://hackernews.cc/archives/63996 "Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-01

[![vickygharat-cyber-5316972_1920](https://hackernews.cc/wp-content/uploads/2026/02/vickygharat-cyber-5316972_1920-210x140.jpg)](https://hackernews.cc/archives/62875 "Claude 桌面扩展零点击远程代码执行漏洞曝光，超万名用户面临远程攻击风险")

##### [Claude 桌面扩展零点击远程代码执行漏洞曝光，超万名用户面临...](https://hackernews.cc/archives/62875 "Claude 桌面扩展零点击远程代码执行漏洞曝光，超万名用户面临远程攻击风险")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-02-10

[![可用-AI安全](https://hackernews.cc/wp-content/uploads/2026/02/techmanic-digital-art-8420361_1920-210x140.jpg)](https://hackernews.cc/archives/62817 "Claude Opus 4.6 在主流开源库中发现 500 余个高危安全漏洞")

##### [Claude Opus 4.6 在主流开源库中发现 500 余个高危安全漏洞](https://hackernews.cc/archives/62817 "Claude Opus 4.6 在主流开源库中发现 500 余个高危安全漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-02-09

[![可用-人工智能](https://hackernews.cc/wp-content/uploads/2025/01/artificial-intelligence-3382507_1280-210x140.jpg)](https://hackernews.cc/archives/61537 "实测六大 AI 模型安全防线：对抗性提示可诱骗生成危险内容")

##### [实测六大 AI 模型安全防线：对抗性提示可诱骗生成危险内容](https://hackernews.cc/archives/61537 "实测六大 AI 模型安全防线：对抗性提示可诱骗生成危险内容")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2025-11-14

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team