---
title: Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞
url: https://hackernews.cc/archives/64062
source: HackerNews
date: 2026-04-09
fetch_date: 2026-04-10T04:45:29.046880
---

# Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-AI安全](https://hackernews.cc/wp-content/uploads/2026/02/techmanic-digital-art-8420361_1920.jpg)

# Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-09](https://hackernews.cc/archives/64062 "11:26")
分类: [AI安全](https://hackernews.cc/archives/category/ai%E5%AE%89%E5%85%A8),[人工智能](https://hackernews.cc/archives/category/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD)
[暂无评论](https://hackernews.cc/archives/64062#respond)

* 浏览次数 192
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

**人工智能公司Anthropic宣布推出名为”Project Glasswing”的网络安全新计划，将使用其前沿模型Claude Mythos的预览版发现和修复安全漏洞。**

该模型将由包括AWS、苹果、博通、思科、CrowdStrike、谷歌、摩根大通、Linux基金会、微软、英伟达和Palo Alto Networks在内的少数组织使用，共同保护关键软件。

Anthropic表示，成立该计划是因其通用前沿模型展现出”超越除最熟练人类外所有人的软件漏洞发现和利用能力”的编码水平。**出于网络安全能力及可能被滥用的担忧，Anthropic选择不公开发布该模型。**

**据称Mythos预览版已在各大操作系统和网页浏览器中发现数千个高严重性零日漏洞，包括OpenBSD中一个已修复的27年历史漏洞、FFmpeg中一个16年历史的缺陷，以及一个内存安全虚拟机监控器中的内存损坏漏洞。**

Anthropic强调的一个案例中，Mythos预览版据称自主开发出网页浏览器利用程序，串联四个漏洞逃离渲染器和操作系统沙箱。Anthropic还在预览版的系统卡中指出，该模型解决了一个企业网络攻击模拟，而人类专家需要10小时以上才能完成。

最令人瞩目的发现是，**Mythos预览版遵循评估研究人员的指令，成功逃离提供的安全”沙箱”计算机，显示出绕过自身防护的”潜在危险能力”。**

该模型并未止步于此，还进一步采取一系列额外行动，包括设计多步骤利用程序从沙箱系统获取广泛互联网访问权限，并向正在公园吃三明治的研究人员发送电子邮件。

“此外，在一个令人担忧且未经要求的展示成功的努力中，它将其利用细节发布到多个难以找到但技术上公开的网站，”Anthropic表示。

该公司指出，Project Glasswing是在敌对行为体采用相同能力之前，将前沿模型能力用于防御目的的”紧急尝试”。Anthropic还承诺提供高达1亿美元的Mythos预览版使用额度，以及400万美元直接捐赠给开源安全组织。

“我们并未明确训练Mythos预览版具备这些能力，”Anthropic表示。”相反，它们是代码、推理和自主性普遍改进的下游结果。使模型在修补漏洞方面显著更有效的相同改进，也使其在利用漏洞方面显著更有效。”

Mythos的消息上月泄露，因人为失误，模型详情被无意存储在公开可访问的数据缓存中。草稿材料将其描述为迄今为止构建的最强大、最有能力的AI模型。数日后，Anthropic遭遇第二次安全疏漏，意外暴露了近2000个源代码文件及Claude Code相关的超过50万行代码，持续约三小时。

该泄露还导致发现一个安全问题：**当AI编码代理被呈现由超过50个子命令组成的命令时，可绕过某些防护。该问题已于上周在Claude Code 2.1.90版本中正式修复。**

AI安全公司Adversa表示：”Claude Code是Anthropic的旗舰AI编码代理，在开发者机器上执行shell命令，当命令包含超过50个子命令时，会静默忽略用户配置的安全拒绝规则。配置’永不运行rm’的开发者会看到rm单独运行时被阻止，但如果在50个无害语句前运行相同的’rm’，则不受限制。安全策略悄然消失。”

“安全分析消耗token。Anthropic的工程师遇到性能问题：检查每个子命令会冻结UI并消耗计算资源。他们的修复方案：50个后停止检查。他们用安全换取速度，用安全换取成本。”

---

**消息来源：[thehackernews.com](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Anthropic](https://hackernews.cc/archives/tag/anthropic)[Mythos](https://hackernews.cc/archives/tag/mythos)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用 代码](https://hackernews.cc/wp-content/uploads/2026/01/可用-代码-210x140.jpg)](https://hackernews.cc/archives/64066 "Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光")

##### [Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光](https://hackernews.cc/archives/64066 "Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-犯罪](https://hackernews.cc/wp-content/uploads/2025/08/criminal-8444883_640-1-210x140.jpg)](https://hackernews.cc/archives/64065 "OpenSSL 修复数据泄露等七处漏洞")

##### [OpenSSL 修复数据泄露等七处漏洞](https://hackernews.cc/archives/64065 "OpenSSL 修复数据泄露等七处漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-wordpress-581849_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-wordpress-581849_1280-210x140.jpg)](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

##### [黑客利用 Ninja Forms WordPress 插件关键漏洞](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-08

[![可用-游戏](https://hackernews.cc/wp-content/uploads/2025/02/fortnite-4129124_1280-210x140.jpg)](https://hackernews.cc/archives/64052 "Flowise 严重 RCE 漏洞遭攻击者利用")

##### [Flowise 严重 RCE 漏洞遭攻击者利用](https://hackernews.cc/archives/64052 "Flowise 严重 RCE 漏洞遭攻击者利用")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-08

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team