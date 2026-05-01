---
title: 从零开始安装/使用Claude Code，CCSwitch管理所有AI模型，绕过登录接入DeepSeek-v4模型
url: https://mp.weixin.qq.com/s/0fUrKq7zOOHKNjvydrsBKg
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:35:13.328941
---

# 从零开始安装/使用Claude Code，CCSwitch管理所有AI模型，绕过登录接入DeepSeek-v4模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LtibzcRx8GjX1MXPliaUkoV6mIYtAQEiaGxxbpFKLAOvYVAJeNlyQmicXRkKvXtZASWWwt462sCDzhjiapdxqqOF7Vb4jia4Xpt3rCJOtWwqkcDkE/0?wx_fmt=jpeg)

# 从零开始安装/使用Claude Code，CCSwitch管理所有AI模型，绕过登录接入DeepSeek-v4模型

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果你也在使用多个AI大模型，比如Claude、GPT、或者其他本地模型，那你一定遇到过这些问题：

不同平台来回切换、API配置繁琐、开发环境割裂，甚至连最基本的模型选择都变得低效。

最近网上有个热门话题。

在本地安装Claude Code，来接入DeepSeek-v4模型。

可能很多人就有疑问了，既然已经安装了 Claude Code，为什么不直接使用默认的Claude模型，而是要额外接入DeepSeek V4？

原因其实非常现实，门槛高：

* 首先是充值和支付门槛，对国内不友好，支付不方便，甚至要折腾外卡或中间渠道
* 其次是账号稳定性，不少用户都出现了账号风控。
* 注册要求也高，比如需要验证手机号，卡邮箱
* 网络环境受阻
* ......

各种原因导致无法使用Claude大模型。

其实想要使用Claude大模型或者其他AI也不是没有办法，要么去找平台买账号，要么就是找AI中转站。

本期内容目标：

具体来说，你将完成三件事：

1. 配置基础运行环境（确保后续工具可以正常安装）
2. 安装并配置 CCSwitch 和 Claude Code
3. 在实际开发中调用不同大模型，完成基本使用闭环

一、环境&工具安装配置

1、安装NodeJS

```
https://nodejs.org/zh-cn/download
```

根据自己对应的操作系统来安装即可，我的操作系统是Windows，安装过程中一路下一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVrcVK7DW1JS6IM1YdEJETwq2kVSzPTfg0oxN8bxSPLuAQ5jmPoiavGb54eL8wwxLGbFZfeGYgkR5fGicvldQKEgjSt9iaCfXzCia0/640?wx_fmt=png&from=appmsg)

终端输入：node -v 和 npm -v 现实版本号即可。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUB3YUNZDhicKgw9zfnfN8Leqt7hsZZC5FJ7icfWPsSjBNTL2flibdIgqsRfOtUBvicwRt8ticLeGMTldDTeYy3daJxMKHCsYMuG7uY/640?wx_fmt=png&from=appmsg)

2、安装Git

```
https://git-scm.com/install/windows
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUlt9EkQ7YojR3zQYg0pckTaKLh1XE2iarA5PWeoptkZLC8DJgNjJ8ZUKRicxf18dr3nibFLKibnbarmmZjpl96HqlY6S4xiazuNuxw/640?wx_fmt=png&from=appmsg)

终端输入：git --version 出现版本号即可。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjW2icNFGPYTDmhogM70vyUibn7LDGiaaLeLEBILCgvndB7DgvibYJCKYqpiaSEZzbYmJe3eoJBCndE5ts9x0XZu6iaciaghQfCIyosC04/640?wx_fmt=png&from=appmsg)

3、网络要开代理，否则会拉取内容失败或者卡住，最好是开TUN全局。

二、安装CCSwitch & Claude Code

1、安装CCSwitch

```
https://github.com/farion1231/cc-switch
```

CCSwitch 是一个用于**统一管理和切换多种大模型的本地工具**，核心目标是解决开发过程中“多个AI模型分散使用”的问题。

## 🧩 它主要做什么？

简单来说，CCSwitch 做了三件事：

### 1️⃣ 统一模型入口

把不同来源的模型（如云端API模型、本地模型等）统一接入到一个入口中管理，避免你在多个平台之间来回切换。

### 2️⃣ 快速切换模型

在同一个开发环境中，可以根据任务随时切换不同模型，例如：

* 代码生成用一个模型
* 代码解释用另一个模型
* 调试或优化再换一个模型

👉 不需要改代码结构，只改“使用的模型”。

### 3️⃣ 配置集中管理

将模型的 API Key、地址、参数等配置集中管理，避免散落在不同项目或工具中，提高可维护性。

## 🧠 它解决的核心问题

在没有类似工具之前，使用多个大模型通常会遇到：

* 平台太多，切换麻烦
* 配置重复，维护成本高
* 不同工具体验割裂

CCSwitch 的思路就是一句话：

👉 **把“选模型”这件事，从环境问题变成一个开关问题。**

根据自己的操作系统下载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXzdYs8gRsoCYB7ZiaGicv3MyllBZM5cQQbI9KB9If1M5ibbVVqdYAvibUaKKsxL4ee6BhokkpIABnP7en3lmZGB3nVCJAM93SZepI/640?wx_fmt=png&from=appmsg)

安装完成之后，打开CCSwitch，点击右上方+，添加模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjW2MCVTd7ibv5YDq3cicRO1edo6kkAJRElQm8RV9TJ66uY37ebyqohXLibIicib6wGgSAPicXQQl1GclXesrsVPcvyw8WRuTgrB57kxA/640?wx_fmt=png&from=appmsg)

这里就选择DeepSeek，如果你有其他模型的API Key，可以找找对应的供应商，然后添加就行。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVogccSmjMoBFHO5ef9Fpgmla5eCibXNupHzu94qf833ibadg7Maqr0K3Kjxz9tAMCicPpoenvR5yZKB7uXsG3NDwaiculkfSPhxGM/640?wx_fmt=png&from=appmsg)

将API Key填入这里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWKzVJF7KJxrIhkD7kibuic6LXIhyPaUMYJQTS9f6XgpSnUPeiaicRSvahfqJSeD0tPeSBILnqYVDewN18ic8G6b0pPVAk9pzgmgoicE/640?wx_fmt=png&from=appmsg)

将模型映射都填入 deepseek-v4-pro

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWm3TkPEm8WGerWUeC8WiaQpvIyYz8Nyv8dib3SSg4lkCWrPXDVPyPTZLccH7PI5TrYIibBXUSoD6RJsNAbibic3dLO7bFWwZWQuI7o/640?wx_fmt=png&from=appmsg)

Claude只支持 v4-pro 和 flash，其他的模型不支持。

之后保存，点击启用即可。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXuqNwouXsDu4C62n9ckvBB5kuIuHLibnB5HBKd59oBhrFMG1bN9w1lNXuW8oA76iciciaFOQDmhliaaVaxQEujkK1OicSQ0lcJS6rI0/640?wx_fmt=png&from=appmsg)

2、安装Claude

安装的是 Terminal 终端版本，暂不安装Desktop 桌面版。

以管理员身份运行 PowerShell ，安装之前先执行这个命令：

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

在 Windows 系统中，PowerShell 默认出于安全考虑，会限制脚本的执行权限。这意味着一些由工具自动生成或下载的脚本（例如 npm、Node.js 工具链生成的 `.ps1` 文件）可能无法正常运行。

只对**当前 Windows 用户**生效

### 📌 特点：

* ✔ 不需要管理员权限
* ✔ 只影响你自己的账号
* ✔ 更安全
* ✔ 不影响其他用户

👉 本质是“个人级设置”

如果不加 `-Scope CurrentUser`，修改的可能是整个系统级策略，影响所有用户。

而：

```
-Scope CurrentUser
```

表示：

👉 **只修改当前登录用户的执行策略，不影响系统其他用户或全局设置**

这样做的好处是：

* 不需要管理员权限
* 不影响其他账户
* 更安全、可回滚
* 适合开发环境使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjW0knGGQyymKEAia2RyzaIyzBPQicHgUrHWHnLZdSyHl8nJCEPmJrRXcuDLqvHYuKZg24SayQ7KKZx7JXodY73JZDkSXAH8j8mGA/640?wx_fmt=png&from=appmsg)

然后执行以下命令安装：

```
npm install -g @anthropic-ai/claude-code
```

它是通过 npm 全局安装 CLI 工具。

安装完成之后会输出安装了2个包，记住，不是1个。如果是1个估计是没有安装完。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUcWpaMSJnoJOPMJJTnrrlVGMe1YkLZ7zzP6cjoY2oKUB7cCdklyx7jhFb01ghMOPefibGicrzrkblibka1MlwbDAd7icNiaHZ9dqus/640?wx_fmt=png&from=appmsg)

之后在终端输入 claude 就能进入初始化交互界面了。这就证明安装成功了。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVWgNzVbibKqE8xCpuu9AVqKlibOBVFdyJT24FLogw58S6WElR8HrR80agWgJKdVfb8o8BS1gTJUrhmw9eiaGYGm8r55v2OQSYZjs/640?wx_fmt=png&from=appmsg)

这个界面只是“外观设置”，不是功能配置。

选项包括：

* Auto（自动匹配终端）
* Dark mode（深色）
* Light mode（浅色）
* ANSI / colorblind 等模式

默认就选择  2：Dark mode

操作方式：直接输入对应的数字。

这一步是Claude Code 已经完整启动成功，并进入安全提示阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWm2kK9hMdgTkUSguSP847WdicicCYfqdp4YowTk6YvAB2v4WogUGaDwtfyMicmDolgRvL4tt0C5pP2ne91OUzyOP0W5k8kdSW7aE/640?wx_fmt=png&from=appmsg)

两点内容：

⚠️ 1. 模型可能出错

```
Claude can make mistakes建议你始终检查输出
```

👉 含义：

* AI 可能生成错误代码
* 尤其是运行代码时要谨慎

⚠️ 2. Prompt Injection 风险

```
Only use it with code you trust
```

👉 含义：

* 不要随便让 AI 运行未知代码
* 防止恶意提示注入

说白了这就是个注意提示。

屏幕底部写的很清楚：

```
Press Enter to continue...
```

你只需要按回车 Enter。

之后会进入工作区安全确认。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUjc8wKqxBIh4ZUDYQXKqQ6vDIapluEHSWHx1Tibq1jAWArSVDarpZ7RuXZIydDEw1POo1KIvCWTyDfCicZicibYAKKQpgoQyKqUFw/640?wx_fmt=png&from=appmsg)

它在问：“你是否信任当前目录？”

你当前的路径应该是：C:\WINDOWS\system32

重点问题其实是这个：你现在所在目录是Windows 系统核心目录（System32）。

Claude Code 在提示你：

* 这个目录不是项目目录
* 里面全是系统文件
* AI 可以读 / 写 / 执行（风险很高）

界面有两个选项：

```
1. Yes, I trust this folder2. No, exit
```

## ❌ 强烈不建议选 1（在你当前目录）

原因：

* System32 是系统关键目录
* Claude Code 有读写权限
* 误操作可能影响系统文件

## ✅ 正确选择：2（退出）

👉 然后重新进入你的项目目录

直接输入2，退出当前界面。

推荐专门建一个项目目录：

```
mkdir D:\ai-projectscd D:\ai-projects
```

然后再执行 claude ，这次它会问：Accessing workspace: D:\ai-projects

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWltep2x7oWkkyfmv9uSK9quevTXdYYudklic15xRQhVVd9S6UYrMibEWL1fMS6bTgME0fkkxKdujmSqzKLNpVtlEZGpjIH8onII/640?wx_fmt=png&from=appmsg)

这时候就可以选择 1 。

然后你就到Claude Code的主界面了。可以看到当前所使用的模型是DeepSeek-v4-pro。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjX17x8MgzUMQE11jwPoyURVu6mJMJCTGKChQYNia6xFS1vF0iamRBfCm0frkjU2mWR6sn4iascLGibVuChoeKM8AamtPHT5zjUpkQI/640?wx_fmt=png&from=appmsg)

三、使用 Claude Code

这里我展示两种使用方式：

* 直接在终端（也就是上方图片的界面）
* Visual Studio Code插件（能够更好的交互）

1、终端使用

流程基本就是：

* 先进入某个目录
* 输入 claude 启动
* 信任目录
* 然后在终端使用

在终端输入你的问题就可以使用了。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWeQe9zFouVQ6oPFblzMBd4aoT0Phyp9d4ASIPkic1iaUQbdcickNCibFrWcOTnXjyqAYia9wia6Qw4icxkRFumEmo9ulibRwUC8JObua4/640?wx_fmt=png&from=appmsg)

我让它帮我生成一个简历网页，将需求发给它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWPzmK4oCpfiaCj3lCqibt54q7F6OF2nl1BmhglnMdcwvOGCGMr4Eic3wb5LPrTbTcMicUSiauE62Toj09p6ojiapTMFpaS4BCHT8NJY/640?wx_fmt=png&from=appmsg)

之后就给我输出了代码，然后询问是否创建 resume.html？直接输入 1 ，创建。如果你后边不想让它每次都询问权限，直接输入 2 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjX7wAaNydyKNjYA22nrkcw5fpmEfPSbv48DAGhSgd5WL98KKeIYmiayDsyHJ3KialSc8hBrvKsiaiaoMWmYUNibST9QWBXeCHwQNZ6Q/640?wx_fmt=png&from=appmsg)

可以看到它已经为我创建好了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVUZj8iaibHTwhzThF16EaEVicRQIymMIFenQ2vIQcumRV1CXLHlSGxKFogYVvRMGFWWpBbkN5ibibmjjgDqnfLyGeL9XBWDnO64NG4/640?wx_fmt=png&from=appmsg)

之后我打开它给我做的简历网页，下方视频：

做得还是非常不错的。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_02.png)

那么如何退出这个窗口？

我的建议是直接输入 exit。

它会在最后给你一行命令：

```
claude --resume ***-***-**
```

后边可以执行这个命令恢复这个对话。

二、Visual Studio Code插件使用

在VSCode扩展插件中，输入 Claude ，找到如图对应的插件，然后安装，安装完成之后，右上角会出现 Claude 的图标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjW7guqLnl12v6ib31Dh4uYY0ibvdn1VF4nqxSQjdbd9QuibrHT5nyicwb...