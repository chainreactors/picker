---
title: Claude Desktop被曝秘密写入浏览器后门文件
url: https://mp.weixin.qq.com/s/gbKAUhz_v2IvZs8tIoJwKA
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:43:45.468197
---

# Claude Desktop被曝秘密写入浏览器后门文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrMq2YWYJGoWrqn6TH3RuXicNABOZubE8bQv6wPHzdGBdXM9VBu0QYGy1jLct3p1JgyM9z4YGicLVAAnBCX4Lu8TW6fOtIBib5YXU/0?wx_fmt=jpeg)

# Claude Desktop被曝秘密写入浏览器后门文件

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026 年 4 月 ，一位专注于隐私和网络安全的研究者 Alexander Hanff 发布了一篇重磅文章，揭露了 AI 公司 Anthropic 的一个行为。

当用户安装 Claude Desktop 桌面应用时，该应用会在用户完全不知情的情况下，向电脑中所有基于 Chromium 内核的浏览器写入一个特殊文件。这个文件相当于一个预先授权的后门，一旦配合特定的浏览器扩展使用，就能获得对用户浏览器的完全控制权。

## 什么是 Native Messaging，它为什么危险

##

要理解这个问题的严重性，我们首先需要了解一个技术概念 Native Messaging。这是 Chromium 浏览器提供的一种机制，允许浏览器扩展与用户电脑上的本地程序进行通信。

与普通的浏览器扩展不同，通过 Native Messaging 调用的本地程序运行在浏览器沙箱之外。它拥有与当前登录用户完全相同的系统权限。这意味着它可以访问用户电脑上的几乎所有文件和资源，而不受浏览器安全限制的约束。

正常情况下，Native Messaging 的使用流程应该是这样的。用户首先安装一个浏览器扩展，然后这个扩展会提示用户是否允许它与本地程序通信。用户明确同意后，相关的配置文件才会被创建。

但 Anthropic 的做法完全打破了这个正常流程。

Alexander Hanff 在调试自己编写的一个 Native Messaging 辅助工具时，意外发现了一个不属于自己的文件。

这个文件位于 Brave 浏览器的 NativeMessagingHosts 目录下，文件名是 com.anthropic.claude\_browser\_extension.json。

```
~/Library/Application Support/BraveSoftware/Brave-Browser/NativeMessagingHosts/com.anthropic.claude_browser_extension.json
```

经过检查，这个文件的内容显示，它预先授权了三个特定的 Chrome 扩展 ID。只要这三个扩展中的任何一个出现在用户的浏览器中，浏览器就会自动允许它们调用 Claude Desktop 安装目录下的一个名为 chrome-native-host 的二进制程序。

```
{  "name": "com.anthropic.claude_browser_extension",  "description": "Claude Browser Extension Native Host",  "path": "/Applications/Claude.app/Contents/Helpers/chrome-native-host",  "type": "stdio",  "allowed_origins": [    "chrome-extension://dihbgbndebgnbjfmelmegjepbnkhlgni/",    "chrome-extension://fcoeoabgfenejglbffodgkkbkcdhcgfn/",    "chrome-extension://dngcpimnedloihjnnfngkgjoidhnaolf/"  ]}
```

Hanff 强调，他从未安装过任何 Anthropic 的浏览器扩展。他只安装过 Claude Desktop 桌面应用。这意味着，是 Claude Desktop 在他完全不知情的情况下，主动向他的浏览器写入了这个配置文件。

为了验证这个发现，Hanff 在另一台机器上进行了全面的审计。

结果如下：

Claude Desktop 不仅向 Brave 浏览器写入了配置文件，还向 Google Chrome、Microsoft Edge、Arc、Chromium、Vivaldi 和 Opera 这七个基于 Chromium 内核的浏览器都写入了完全相同的文件（1e927a9e7796d0175a2a1f30028f4baa）。

```
$ find ~/Library/Application\ Support -name "com.anthropic.claude_browser_extension*"~/Library/Application Support/Arc/User Data/NativeMessagingHosts/com.anthropic.claude_browser_extension.json~/Library/Application Support/BraveSoftware/Brave-Browser/NativeMessagingHosts/com.anthropic.claude_browser_extension.json~/Library/Application Support/Chromium/NativeMessagingHosts/com.anthropic.claude_browser_extension.json~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.anthropic.claude_browser_extension.json~/Library/Application Support/Microsoft Edge/NativeMessagingHosts/com.anthropic.claude_browser_extension.json~/Library/Application Support/Vivaldi/NativeMessagingHosts/com.anthropic.claude_browser_extension.json~/Library/Application Support/com.operasoftware.Opera/NativeMessagingHosts/com.anthropic.claude_browser_extension.json
```

更离谱的是，在这台测试机器上，Edge、Arc、Chromium、Vivaldi 和 Opera 这五个浏览器根本就没有安装。Claude Desktop 竟然提前创建了这些浏览器的配置目录，并写入了后门文件。

```
$ ls /Applications/ | grep -iE "chrome|brave|safari|edge|opera|vivaldi|arc|chromium|firefox|tor"Brave Browser.appGoogle Chrome.appSafari.appTor Browser.app
```

所有配置文件的最后修改时间都指向 2026 年 4 月 16 日深夜。这表明 Claude Desktop 会在每次运行时重新写入这些文件。用户即使手动删除了它们，下次启动 Claude Desktop 时，这些文件又会自动恢复。

```
$ stat -f "birth:%SB  mod:%Sm  %N" ~/Library/Application\ Support/*/NativeMessagingHosts/com.anthropic.claude_browser_extension.json \                                   ~/Library/Application\ Support/*/*/NativeMessagingHosts/com.anthropic.claude_browser_extension.jsonbirth:Jan 19 08:19:15 2026  mod:Apr 16 23:42:19 2026  .../Arc/User Data/NativeMessagingHosts/...birth:Jan 19 08:19:15 2026  mod:Apr 16 23:42:19 2026  .../BraveSoftware/Brave-Browser/NativeMessagingHosts/...birth:Jan 19 08:19:15 2026  mod:Apr 16 23:42:19 2026  .../Chromium/NativeMessagingHosts/...birth:Dec 20 04:18:42 2025  mod:Apr 16 23:42:18 2026  .../Google/Chrome/NativeMessagingHosts/...birth:Jan 19 08:19:15 2026  mod:Apr 16 23:42:19 2026  .../Microsoft Edge/NativeMessagingHosts/...birth:Jan 19 08:19:15 2026  mod:Apr 16 23:42:19 2026  .../Vivaldi/NativeMessagingHosts/...birth:Jan 19 08:19:15 2026  mod:Apr 16 23:42:19 2026  .../com.operasoftware.Opera/NativeMessagingHosts/...
```

通过检查 Claude Desktop 的日志文件，Hanff 发现了 31 次 "Native host installation complete" 的记录。这证实了这个行为是 Claude Desktop 的一个内置功能，内部代号为 Chrome Extension MCP。

```
$ grep -c "Native host installation complete" ~/Library/Logs/Claude/main.log ~/Library/Logs/Claude/main1.log~/Library/Logs/Claude/main.log:7~/Library/Logs/Claude/main1.log:24
```

macOS 系统的文件来源元数据也明确显示，这些配置文件确实是由 Claude Desktop 创建的。该辅助二进制文件是一个通用的 Mach-O 可执行文件。它使用 Anthropic PBC 的开发者 ID 应用程序证书（团队标识符Q6L2SF6YDW）进行代码签名。该签名包含一个符合 RFC 3161 标准的安全时间戳，时间为 2026 年 4 月 16 日 18:39:18，由 Apple 时间戳机构提供。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDq7w4lUw6iaJ9U5UE5tq4ZWV8ia3S4SG6oiakrc7PTXx3uqDxdGqj5HWvyjh20rpbZ7RMK8oSaHqaAjiaUZukibTxxEia1UEQl5WzNCo/640?wx_fmt=png&from=appmsg)

##

根据 Anthropic 自己公开的文档，这个 chrome-native-host 程序为 Claude 提供了以下强大的浏览器控制能力：

* 打开新标签页并共享用户的浏览器登录状态。这意味着 Claude 可以访问用户已经登录的任何网站，包括银行、税务、医疗、企业管理后台等敏感系统。
* 实时调试。读取浏览器控制台错误和 DOM 状态，然后修复导致问题的代码。
* 数据提取。从网页中提取结构化信息并保存到本地。
* 任务自动化。自动执行重复性的浏览器任务，如数据输入、表单填写或多站点工作流。
* 会话录制。将浏览器交互记录为 GIF 文件，用于记录或分享发生的事情。

简单来说，一旦这个后门被激活，Claude 就可以完全代替用户在浏览器中进行任何操作。它可以看到用户能看到的所有内容，也可以做用户能做的所有事情。

更令人担忧的是，Anthropic 自己在发布 Claude for Chrome 时承认，该功能仍然存在严重的安全漏洞。特别是 prompt injection 攻击，在没有任何缓解措施的情况下成功率高达 23.6%。即使有了当前的防御措施，成功率仍然有 11.2%。这意味着大约每九次攻击中就有一次能够成功绕过 Anthropic 的安全防护。

Hanff 在文章中详细分析了 Anthropic 这种行为带来的多重风险。

### 安全风险

1. 供应链攻击风险。三个预先授权的扩展 ID 中，只要有任何一个被攻击者控制，攻击者就能立即获得对用户电脑的远程代码执行权限。这可能通过多种方式发生，包括 Anthropic 内部账户被入侵、恶意扩展更新被推送到 Chrome 应用商店，或者企业策略强制安装恶意扩展。
2. prompt injection 攻击风险。如果攻击者在用户访问的网页中隐藏了恶意指令，就有可能通过 prompt injection 漏洞控制 Claude，进而通过这个后门获得对用户浏览器和电脑的控制权。
3. 浏览器安全模型被破坏。许多用户选择使用 Brave 等浏览器，正是因为它们提供了更强的安全和隐私保护。但 Anthropic 在这些浏览器中秘密安装后门的行为，实际上削弱了这些浏览器的安全优势。
4. 无法审计。无论是 macOS 系统、浏览器本身还是 Claude Desktop 应用，都没有提供任何用户界面来显示已经注册的 Native Messaging 主机。普通用户根本无法发现这个后门的存在。
5. 未来功能扩展风险。Anthropic 可以随时更新 chrome-native-host 程序，增加更多的功能。而用户对此完全不知情，也无法阻止。

### 隐私风险

1. 认证会话暴露。Claude 可以访问用户在所有网站上的登录状态，这意味着它可以读取用户的私人邮件、社交媒体消息、银行账户信息等所有敏感数据。
2. DOM 内容访问。Claude 可以读取网页上的所有内容，包括那些不会出现在 URL 或网络日志中的信息。例如用户正在输入的密码、信用卡号码、双因素验证码等。
3. 跨配置文件关联。Native Messaging 主机是在浏览器级别注册的，而不是针对每个用户配置文件。如果用户使用不同的浏览器配置文件来隔离个人、工作和研究活动，这种隔离在这个后门面前将完全失效。
4. 无效的用户同意。即使未来用户主动安装了 Claude for Chrome 扩展并给予了同意，这种同意也不能追溯到之前秘密安装的后门。用户实际上是在不知情的情况下，已经给予了 Anthropic 远超他们想象的权限。

##

Hanff 在文章中明确表示，这就是预先安装的间谍软件能力。它被秘密地放置在用户的电脑上，处于休眠状态，等待被激活。

Anthropic 可能会辩称，这个二进制程序目前没有做任何有害的事情。但这种论点站不住脚。危险的不是程序当前在做什么，而是它被赋予的能力以及它被安装的方式。

如果你已经安装了 Claude Desktop，你可以采取以下步骤来检查和移除这个后门：

1. 打开终端应用。
2. 运行以下命令来查找所有 Anthropic 安装的 Native Messaging 配置文件：

```
find ~/Library/Application\ Support -name "com.anthropic.claude_browser_extension*"
```

3. 对于找到的每个文件，使用 rm 命令将其删除。
4. 请注意，每次启动 Claude Desktop 时，这些文件都会被重新创建。如果你想彻底阻止这种行为，你可能需要卸载 Claude Desktop，直到 Anthropic 修复这个问题。

##

Anthropic 一直以来都将自己定位为最注重安全和负责任的 AI 公司，一个真正注重安全和用户隐私的公司，不应该在用户不知情和未同意的情况下，秘密安装具有如此强大能力的后门。

AI 技术的发展必须建立在信任的基础上。如果用户不能相信 AI 公司会尊重他们的隐私和安全，那么无论 AI 技术多么先进，都难以获得广泛的接受。

原帖可自行前去校验：

https://www.thatprivacyguy.com/blog/anthropic-spyware/

往期：

[针对以色列水处理和海水淡化设施系统的新型工业恶意软件](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186449&idx=1&sn=236e11c1a3ae2be6e472635338201c66&scene=21#wechat_redirect)

更多有趣👇

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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
，轻点两下...