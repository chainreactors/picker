---
title: Flowise 严重 RCE 漏洞遭攻击者利用
url: https://hackernews.cc/archives/64052
source: HackerNews
date: 2026-04-08
fetch_date: 2026-04-09T04:30:43.275384
---

# Flowise 严重 RCE 漏洞遭攻击者利用

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-游戏](https://hackernews.cc/wp-content/uploads/2025/02/fortnite-4129124_1280.jpg)

# Flowise 严重 RCE 漏洞遭攻击者利用

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-08](https://hackernews.cc/archives/64052 "10:34")
分类: [漏洞](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E)
[暂无评论](https://hackernews.cc/archives/64052#respond)

* 浏览次数 150
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

**黑客正在利用开源平台Flowise中的最高严重性漏洞CVE-2025-59528执行任意代码。**Flowise用于构建自定义大语言模型应用和代理系统。

该漏洞允许在无任何安全检查的情况下注入JavaScript代码，去年9月公开披露时警告称，成功利用可导致命令执行和文件系统访问。

问题出在Flowise的CustomMCP节点，该节点允许配置设置连接外部模型上下文协议（MCP）服务器，并不安全地评估用户的mcpServerConfig输入。在此过程中，它可在未先验证安全性的情况下执行JavaScript。

开发者在Flowise 3.0.6版本中修复了该问题。最新当前版本为3.1.1，两周前发布。

Flowise是一款开源低代码平台，用于构建AI代理和基于大语言模型的工作流。它提供拖放界面，让用户将组件连接成驱动聊天机器人、自动化和AI系统的管道。

其用户群体广泛，包括从事AI原型开发的开发者、使用无代码工具集的非技术用户，以及运营客户支持聊天机器人和知识库助手的公司。

漏洞情报公司VulnCheck安全研究员Caitlin Condon在LinkedIn宣布，其Canary网络检测到CVE-2025-59528的利用活动。

Condon警告：”今天清晨，VulnCheck的Canary网络开始首次检测到CVE-2025-59528的利用活动，这是Flowise（开源AI开发平台）中CVSS评分10分的任意JavaScript代码注入漏洞。”

虽然活动目前看似有限，源自单一Starlink IP，但研究人员警告称，目前约有1.2万至1.5万个Flowise实例暴露于互联网。

然而，尚不清楚其中有多少比例是易受攻击的Flowise服务器。

Condon指出，观察到的CVE-2025-59528相关活动之外，还涉及CVE-2025-8943和CVE-2025-26319——两者同样影响Flowise，且均已观察到野外主动利用。

目前，VulnCheck仅向其客户提供利用样本、网络签名和YARA规则。

建议Flowise用户尽快升级至3.1.1版本，或至少3.0.6版本。如无需外部访问，还应考虑将实例从公共互联网移除。

---

**消息来源：[bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/max-severity-flowise-rce-vulnerability-now-exploited-in-attacks/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Flowise](https://hackernews.cc/archives/tag/flowise)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)

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

[![可用-AI安全](https://hackernews.cc/wp-content/uploads/2026/02/techmanic-digital-art-8420361_1920-210x140.jpg)](https://hackernews.cc/archives/64062 "Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞")

##### [Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞](https://hackernews.cc/archives/64062 "Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-wordpress-581849_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-wordpress-581849_1280-210x140.jpg)](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

##### [黑客利用 Ninja Forms WordPress 插件关键漏洞](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-08

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team