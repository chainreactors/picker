---
title: Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞
url: https://hackernews.cc/archives/63996
source: HackerNews
date: 2026-04-01
fetch_date: 2026-04-02T04:29:43.702296
---

# Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用](https://hackernews.cc/wp-content/uploads/2026/01/blue-hand-2228501_640.jpg)

# Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-01](https://hackernews.cc/archives/63996 "11:04")
分类: [漏洞](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E)
[暂无评论](https://hackernews.cc/archives/63996#respond)

* 浏览次数 261
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

**通过向 Claude 助手输入简单指令，发现 Vim 和 GNU Emacs 这两款文本编辑器存在漏洞，用户打开文件时就可能导致远程代码执行。**

Claude 助手不仅创建了多个版本的概念验证（PoC）利用代码，还对其进行了优化，并针对这些安全问题提供了解决建议。

Vim 和 GNU Emacs 是可编程文本编辑器，主要供开发者和系统管理员用于代码编辑、基于终端的工作流程以及脚本编写。特别是 Vim，在 DevOps 领域应用广泛，大多数 Linux 服务器发行版、嵌入式系统和 macOS 默认安装该编辑器。

**Vim 漏洞及修复**

Calif 是一家专注于人工智能红队测试和安全工程的小型网络安全公司，其研究员洪・阮（Hung Nguyen）指示 Claude 在这款文本编辑器中寻找由打开文件触发的远程代码执行（RCE）零日漏洞，进而发现了 Vim 中的问题。

Claude 助手分析了 Vim 的源代码，确定在模型行处理过程中存在安全检查缺失及相关问题，导致嵌入文件中的代码在文件打开时得以执行。

模型行是位于文件开头的文本，用于指示 Vim 如何处理该文件。

即便代码本应在沙箱中运行，但另一个问题使其能够绕过限制，并在当前用户环境中执行命令。

该漏洞尚未获得 CVE 编号，影响 Vim 9.2.0271 及更早的所有版本。

阮向 Vim 维护者报告了这一问题，后者迅速在 Vim 9.2.0272 版本中发布了补丁。Vim 团队指出，受害者只需打开特制文件即可触发该漏洞。

公告中称：“攻击者若能将特制文件发送给受害者，就能以运行 Vim 的用户权限执行任意命令。”

**GNU Emacs 与 Git 的关联**

至于 GNU Emacs，该漏洞仍然存在，因为开发者认为这应由 Git 负责解决。

问题源于 GNU Emacs 的版本控制集成（vc – git），打开文件会通过 vc – refresh – state 触发 Git 操作，导致 Git 读取.git/config 文件并运行用户定义的 core.fsmonitor 程序，而这可能被滥用来运行任意命令。

研究人员设计的攻击场景包括创建一个归档文件（例如电子邮件或共享驱动器），其中包含一个隐藏的.git/ 目录，目录中的 config 文件指向一个可执行脚本。

当受害者解压归档文件并打开文本文件时，在 GNU Emacs 默认配置下，有效载荷会在无任何明显提示的情况下执行。

GNU Emacs 维护者认为这是 Git 的问题，而非文本编辑器的问题，因为该环境仅仅是触发 Git 执行危险操作的因素：读取攻击者控制的 config 文件并从中执行程序。

虽然从技术角度看，这一观点是正确的，因为在 GNU Emacs 中没有直接执行任何操作，但由于编辑器会在不受信任的目录中自动运行 Git，且未消除危险选项、未征得用户同意或采取沙箱保护措施，用户仍面临风险。

阮建议 GNU Emacs 可以修改对 Git 的调用，明确阻止 “core.fsmonitor”，这样在打开文件时，任何危险脚本或有效载荷就不会自动执行。

由于该漏洞在 GNU Emacs 最新版本中仍未修复，建议用户在打开来自未知来源或从网上下载的文件时务必谨慎。

---

**消息来源：[bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/claude-ai-finds-vim-emacs-rce-bugs-that-trigger-on-file-open/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Claude](https://hackernews.cc/archives/tag/claude)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用-代码](https://hackernews.cc/wp-content/uploads/2026/02/data-5606639_1920-210x140.jpg)](https://hackernews.cc/archives/63995 "Claude Code 源代码在 NPM 包中意外泄露")

##### [Claude Code 源代码在 NPM 包中意外泄露](https://hackernews.cc/archives/63995 "Claude Code 源代码在 NPM 包中意外泄露")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-01

[![可用——写代码](https://hackernews.cc/wp-content/uploads/2026/02/innovalabs-software-development-6523979_1920-210x140.jpg)](https://hackernews.cc/archives/63984 "Fortinet FortiClient EMS 关键漏洞遭利用，可实现远程代码执行")

##### [Fortinet FortiClient EMS 关键漏洞遭利用，可实现远程代码执行](https://hackernews.cc/archives/63984 "Fortinet FortiClient EMS 关键漏洞遭利用，可实现远程代码执行")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-31

[![可用-恶意软件](https://hackernews.cc/wp-content/uploads/2026/02/geralt-data-theft-9480279_1920-210x140.jpg)](https://hackernews.cc/archives/63968 "Smart Slider 插件文件读取漏洞影响 50 万 WordPress 网站")

##### [Smart Slider 插件文件读取漏洞影响 50 万 WordPress 网站](https://hackernews.cc/archives/63968 "Smart Slider 插件文件读取漏洞影响 50 万 WordPress 网站")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-30

[![可用](https://hackernews.cc/wp-content/uploads/2025/12/ai-generated-9294294_960_720-210x140.png)](https://hackernews.cc/archives/63964 "Citrix NetScaler 关键漏洞遭主动侦察，内存越界读取风险加剧")

##### [Citrix NetScaler 关键漏洞遭主动侦察，内存越界读取风险加剧](https://hackernews.cc/archives/63964 "Citrix NetScaler 关键漏洞遭主动侦察，内存越界读取风险加剧")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-30

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team