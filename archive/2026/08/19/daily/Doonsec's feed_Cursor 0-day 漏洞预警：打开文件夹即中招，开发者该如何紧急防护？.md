---
title: Cursor 0-day 漏洞预警：打开文件夹即中招，开发者该如何紧急防护？
url: https://mp.weixin.qq.com/s/mm9jwOIAHRdu73zzBZ5vvw
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:51:59.214716
---

# Cursor 0-day 漏洞预警：打开文件夹即中招，开发者该如何紧急防护？

# Cursor 0-day 漏洞预警：打开文件夹即中招，开发者该如何紧急防护？

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

作为当下最火热的 AI 编程辅助工具，Cursor 几乎成了广大程序员日常敲代码的“外挂”。大家习惯了让 AI 帮写函数、重构代码，甚至直接把整个开源仓库拖下来让 AI 顺着逻辑读。然而，当所有人的目光都聚焦在模型的聪明程度和代码生成质量时，安全圈的目光却盯上了它的底层架构。近期，安全机构与独立研究员接连披露了关于 Cursor IDE 的高危漏洞（CVE-2026-63093）。

这起事件给所有开发者敲响了警钟：在享受 AI 带来生产力跃升的同时，你赖以生存的开发环境，可能正成为黑客眼中畅通无阻的突破口。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FjhqtRRgWePVruFa2nAYd7sE8l1qiajgISU4oJQe2FDRiaj8zUUd56SYu5dJ1LXvKjfmSkbv71N1ZSxwpMjga1ial9q2k9libiadY8/640?wx_fmt=webp&from=appmsg)

## 一、 AI 编辑器是效率神器还是隐秘的“特洛伊木马”？

长久以来，大家对开发工具的安全信任度极高。程序员们每天都会从 GitHub 上克隆无数个开源项目，或者解压各种不知名的 Demo 压缩包，然后直接用 IDE 打开。在大多数人的认知里，只要不执行可疑的 .exe 或 .sh 脚本，单纯“看一眼代码”能有什么风险？

然而，现代 IDE 早就不是单纯的文本编辑器了。为了提供诸如自动集成、环境检测、项目索引等高级功能，IDE 会在后台默默执行大量的系统级辅助操作。正是这种为了“智能”而牺牲的边界感，给攻击者留下了温床。研究表明，Cursor 在处理特定项目时，存在严重的二进制种植（Binary Planting）隐患。这意味着，攻击者不需要诱导你点任何运行按钮，甚至不需要任何复杂的 Prompt 注入，只要你把恶意构造的文件夹在 Cursor 中打开，系统底层就可能已经中招了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EMp5o1VuXriaGqhrDMvuSNhTnUvzd6WTWAvrYtD1JiaFEJrMjLAMGCBPKVJNqa2so73icA0uPjwwRQ4JUibNRVIicrq5dbGXgCbO2o/640?wx_fmt=webp&from=appmsg)

## 二、 技术复盘：从 git.exe 到隐蔽的 hatch.exe

为了彻底搞懂这个漏洞，我们需要把目光从高大上的 AI 模型拉回到最基础的操作系统的文件解析逻辑上。最初，安全公司 Mindgard 披露了 Cursor 在查找 git.exe 时的缺陷：当 IDE 启动并加载项目时，为了执行诸如获取顶层目录等初始化操作，它会搜索系统中的 Git 客户端。

由于 Windows 系统的默认进程搜索机制会优先检查当前工作目录，如果攻击者在一个恶意的代码仓库根目录下塞进一个精心伪装的恶意 git.exe，当开发者用 Cursor 打开该目录时，IDE 就会阴差阳错地把这个伪造的二进制文件当作系统的 Git 来执行。在当前用户的权限下，这段恶意代码便大摇大摆地运行起来了。

| 漏洞维度 | 早期公开的 git.exe 路径 | 研究员新发现的 hatch.exe 路径 |
| --- | --- | --- |
| 触发条件 | 仓库根目录下存在伪造的 `git.exe` | 仓库中包含合法的 `pyproject.toml` 配置文件，并配合本地的 `hatch.exe` |
| 用户交互 | 零点击（Zero-click），仅需打开文件夹 | 零点击（Zero-click），仅需打开文件夹 |
| 防御隐蔽性 | 容易被监控到非常规路径的 `git.exe` 调用 | 配置文件极其常规，极难引起安全软件的注意 |

更严峻的是，最新的安全研究表明，这种威胁远不止于一个 git.exe1。研究人员发现，当项目目录中存在一个看似人畜无害的 pyproject.toml 配置文件时（例如包含标准的 [build-system] 构建后端声明），Cursor 在后台处理时会尝试寻找并调用 hatch.exe1。攻击者只需要如法炮制，在仓库中放置同名的恶意程序，就能复现同样的远程代码执行（RCE）效果1。这种“触发文件+恶意二进制”的组合，把攻击面扩大到了许多常规的构建和包管理工具上。

## 三、 深度剖析：为什么“零点击”漏洞如此致命？

在这类漏洞的讨论中，“Zero-click（零点击）”是一个让人脊背发凉的词。在传统的钓鱼攻击中，黑客还需要费尽心思诱导受害者点击链接、下载附件，甚至运行安装包。但在 Cursor 的这个案例中，受害者唯一需要做的动作，仅仅是在编辑器里打开一个文件夹。

究其根源，部分 AI 辅助工具在设计之初为了追求极致的丝滑体验，往往默认关闭或弱化了严格的“工作区信任（Workspace Trust）”机制。

相比之下，其他某些 IDE 默认会弹出严厉的警告提示，询问用户是否信任当前目录，从而拦截自动执行；而早期版本的 Cursor 则在默认配置下允许许多项目特性直接加载。虽然在舆论发酵和披露前夕，官方悄悄在最新版本中打上了修复补丁并分配了 CVE 编号，但这也暴露出一个深层次问题：

软件厂商在追求产品迭代速度时，往往对供应链和本地文件处理的安全边界缺乏足够的敬畏。

## 四、 实战防御：中国开发者与企业的安全落地指南

面对层出不穷的开发工具零日漏洞与供应链威胁，身处一线的中国开发者和企业安全团队绝不能被动等待官方补丁。

结合国内开发环境的实际场景，我们建议采取以下全方位的防御措施：

1. 保持客户端实时更新：鉴于官方已经对二进制搜索路径及文件处理逻辑进行了静默修复，所有使用 Cursor 的开发者应立即检查并升级到最新版本，从源头上堵住漏洞[1]。
2. 谨慎克隆与打开未知的外部仓库：不要随意从不知名的论坛、社交媒体或不可信的 GitHub 仓库中下载源码包并在本地用 AI 编辑器直接打开。对于包含复杂构建配置的项目，建议先在沙箱环境或虚拟机中审阅文件。
3. 强化终端进程监控（EDR/SIEM 联动）：企业安全运维人员应当在终端防护策略中加入针对开发工具的异常行为监控。例如，编写规则检测 `Cursor.exe` 是否从非标准路径（如用户临时目录、下载目录等）调用子进程（如 `git.exe`、`hatch.exe` 等）。以下是一条常用的微软 Sentinel / Defender 检索参考逻辑：

   ```
   DeviceProcessEvents
   | where InitiatingProcessFileName =~ "Cursor.exe"
   | where FileName in~ ("git.exe", "hatch.exe")
   | where FolderPath !has @"AppData\Local\Programs"
   ```
4. 推行“工作区信任”最佳实践：在团队内部推行安全规范，无论使用何种 IDE，只要涉及非内部核心代码，务必手动开启并严格核对“工作区信任”弹窗，绝不盲目授予完全执行权限。

## 五、 总结与互动

安全没有绝对的零风险，AI 工具的普及在大幅解放生产力的同时，也把攻击者的视野引向了开发者最核心的阵地——本地集成开发环境。从早期的编辑器插件投毒到如今的底层二进制种植，攻击手段正变得越来越隐蔽和自动化。

各位同行、各位同行开发者，你在日常使用 AI 编程工具时，是否注意过安全隔离？你们团队又是如何防范开发环境供应链污染的？

欢迎在评论区留言分享你的实战经验。如果你觉得这篇文章对你有启发，别忘了点个赞和在看，并转发给身边的每一位程序员朋友，让我们共同筑牢开发安全的铜墙铁壁！

---

参考：

https://screetsec.com/blog/another-cursor-0-day-arbitrary-code-execution-beyond-git-exe

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Gkz51VswJibNsnqQib7QVoKpqIHAvr9ClNG8T25h5fP8mLjUic5oHB1Y1cIj2ib8XItribwmf7QiaWBRpvL5XiaibQouNLjQr2OicfcLMI/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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