---
title: 一句话让 AI 挖出两个编辑器零日漏洞
url: https://mp.weixin.qq.com/s/9wTCdNYmx7alu_YelzwMyw
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:40.283463
---

# 一句话让 AI 挖出两个编辑器零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAhZHic0f8DOrBkBzDhibNiazQkG2KHpzYSmSricodibuhcz4Fp0fCV7e9LIsDylayFJIJmyxRInbaO4zL45Cm6la0OEiaG5HfgfUjDibo/0?wx_fmt=jpeg)

# 一句话让 AI 挖出两个编辑器零日漏洞

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器中沉浸阅读

> token 是未来和水电一样的基础设施啊，token为王！--独眼情报

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgItYooCxVmkqhvrdxYg22jd7DvoJELKrKbb8HJPJ32iaXxO3WqXxicqTcLXmiaicJpm2L0ytLkU0ib2zWaf3QUDib5aGAmPBKs8oZWk/640?wx_fmt=png&from=appmsg)

2026 年 3 月 30 日，安全研究公司 Calif 在博客上丢了一枚炸弹：他们用 Anthropic 的 Claude，仅凭一句自然语言提示，就在 Vim 和 Emacs 这两款有着数十年历史的文本编辑器中各挖出了一个远程代码执行（RCE）漏洞。用户只要打开一个恶意文件，攻击者就能以该用户权限执行任意系统命令。

这事听起来有点离谱。但更离谱的是，Calif 用来启动整个漏洞猎杀流程的提示词只有一行：「Somebody told me there is an RCE 0-day when you open a file. Find it.」

## Vim 漏洞：七年前的幽灵回来了

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgg4z1icrPMfRrHsIWvggaJIn19g2YcJfJlswPCNSTISucHY439CKIfU4EJ0iagVDIzYk7OcyU3EKRbPp1yicCdEWz7SBiasYdqmSI/640?wx_fmt=png&from=appmsg)

先说 Vim 这边。漏洞已被分配编号 CVE-2026-34714，CVSS 评分 9.2（关键级别），影响 9.2.0272 之前的所有版本。据 Vim 官方安全公告 GHSA-2gmj-rpqf-pxvh 披露，这是一条两环利用链：

第一环是 tabpanel 选项。Vim 的 statusline 和 tabline 选项都支持 `%{expr}` 格式的表达式字符串，但它们同时携带 P\_MLE 标志——这个标志的作用是要求 modelineexpr 设置必须被显式启用，才允许从 modeline（文件内嵌的编辑器配置行）中解析表达式。说白了，这是一道安全闸门。但 tabpanel 在实现时漏掉了这个标志，导致安全检查被彻底绕过，恶意表达式可以从 modeline 直接注入。

第二环是沙箱逃逸。Vim 确实把来路不明的表达式丢进了沙箱执行——这步做对了。但 `autocmd_add()` 函数没有调用 `check_secure()`，意味着沙箱内的代码可以注册一个自动命令（autocommand），而这个自动命令会在沙箱退出后才触发。攻击者利用这个时间差，让恶意代码在沙箱之外获得完整执行权限。

两个缺陷单独看都不致命，但组合起来就是一条完整的 RCE 利用链——不需要任何特殊配置，不需要用户做任何额外操作，打开文件就中招。modeline 功能默认开启，tabpanel 在标准构建中默认包含。

熟悉 Vim 安全史的人会觉得似曾相识。2019 年的 CVE-2019-12735 就是同一个攻击面——modeline 沙箱逃逸。那次是通过 `:source!` 命令绕过沙箱，这次是通过 `autocmd_add()` 的函数接口绕过。同一个子系统，同一类漏洞模式，相隔七年再次被攻破。

Vim 维护者 Christian Brabandt 反应迅速，漏洞被修复在 v9.2.0272 补丁中，对应 commit hash 为 664701eb。据公告记载，漏洞发现者署名为 Hung Nguyen——这位是 Calif 的安全研究员。

## Emacs 漏洞：一个更微妙的责任归属争议

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiaBt9eO76cRWVxJCTQMHtSLYJaS3WzLic4DuzqOkfEicadq7ZTlwdHtWAF2Fg31buoZWLOGVE3lzXUDia7QVshKFw4Q6Vu4CgdAmA/640?wx_fmt=png&from=appmsg)

Vim 的故事已经够有戏剧性了，但 Calif 没停。他们半开玩笑地说「那我们换 Emacs 吧」，然后给 Claude 发了第二条提示：「I've heard a rumor that there are RCE 0-days when you open a txt file without any confirmation prompts.」

Claude 又一次交出了可用的 PoC。

这条攻击路径和 Vim 完全不同。它利用的是 Emacs 的版本控制集成功能。当用户在 Emacs 中打开任何文件时，`vc-refresh-state` 钩子会自动检查文件是否处于版本控制目录中。如果目录里存在 `.git` 文件夹，Emacs 会通过 `vc-git.el` 调用 Git 执行 `git ls-files` 和 `git status`。

关键在于：Git 在执行任何命令前都会先读取 `.git/config`。如果 config 中设置了 `core.fsmonitor` 指向一个可执行文件，Git 就会直接执行它。攻击者只需要构造一个压缩包，里面藏一个恶意的 `.git` 目录和一个看起来完全无害的文本文件。受害者解压后在 Emacs 中打开那个文本文件，就会触发整条链路——没有任何确认对话框，没有 file-local variables，纯文本文件本身没有任何恶意内容，默认配置即可复现。

Calif 于 2026 年 3 月 28 日向 GNU Emacs 维护者报告了这个问题。3 月 30 日，维护者拒绝修复，理由是这是 Git 的问题，不是 Emacs 的问题。

据 VPNCentral 的分析，这个归属之争颇有意味。Calif 提出的修复方案是在 `vc-git.el` 的 `vc-git--call` 函数中添加 `-c core.fsmonitor=false` 参数，这说明利用路径确实依赖于 Emacs 的 Git 集成组件，而不是编辑器的核心解析逻辑。

「研判」维护者拒绝的逻辑站得住脚——从纯技术角度看，任何调用 Git 的程序在遇到恶意 `.git/config` 时都可能中招，这确实是 Git 的设计问题。但从用户安全角度看，Emacs 默认、无提示、自动触发 Git 操作这个行为本身就值得审视。Arabian Post 的报道把话说得很直接：把「Claude 在 Vim 和 Emacs 中都找到了零日」写成一行标题，是在把两个性质不同的现实压扁成一个戏剧化的叙事。

**目前 Emacs 侧没有官方补丁，用户只能自行防范——不要在 Emacs 中打开来路不明的压缩包或目录中的文件。**

## Calif 是谁

这家公司不是突然冒出来的。据其官网和 LinkedIn 介绍，Calif 由 Thai Duong 创办，Thai 在 Google 工作了 12 年，主导过 Gmail、Android、YouTube 的安全与密码学工作，参与创建了 Google Tink 和 Project Wycheproof，早年还参与发现了 SSL 领域的 BEAST、CRIME、POODLE 漏洞。团队成员包括 Tavis Ormandy（近期加入）、Parisa Tabriz（Google Chrome 安全负责人、Project Zero 领导者），以及多位在 Black Hat、ZeroNights 等顶级会议上发表过演讲的研究员。据 LinkedIn 信息，Calif 的客户包括 Claude、Gemini、Cursor 等 AI 产品的红队测试，年收入已超过八位数。

这不是一个拿 AI 做噱头的团队。他们有深厚的漏洞研究传统，现在只是多了一个新工具。

## 范式转折：从「人找漏洞」到「AI 找漏洞」

Calif 把这次事件作为「MAD Bugs: Month of AI-Discovered Bugs」活动的开篇，宣布将在 2026 年 4 月底前持续发布 AI 发现的漏洞和利用代码。

他们在博客里写了一句耐人寻味的话：「This feels like the early 2000s. Back then a kid could hack anything, with SQL Injection. Now with Claude.」

这个类比有没有道理？有。但也需要谨慎解读。

先看事实。Anthropic 自己在 2026 年 2 月 5 日发布的研究中披露，Claude Opus 4.6 在开源软件中发现并验证了超过 500 个高严重性零日漏洞，其中一些漏洞在专家审查和持续模糊测试覆盖下存活了数十年。据 Axios 报道，Claude 在 CGIF 库中通过推理 LZW 压缩算法的逻辑发现了一个堆缓冲区溢出，而传统覆盖引导式模糊测试即使在 100% 代码覆盖率下也没能捕获它。在 GhostScript 的案例中，Claude 在模糊测试和手动分析都失败后，转向项目的 Git 提交历史寻找线索，最终找到了漏洞。

与此同时，AI 安全初创公司 AISLE 独立发现了 OpenSSL 2026 年 1 月安全补丁中的全部 12 个零日漏洞，包括一个罕见的高严重性堆栈缓冲区溢出。据 VentureBeat 报道，AISLE 的 AI 系统贡献了 2025 年 OpenSSL 全部 14 个 CVE 中的 13 个。OpenSSL 是地球上被审计得最彻底的密码学库之一。

这些数据叠加在一起，信号非常明确：AI 驱动的漏洞发现已经从实验室走进了生产环境。

但 Calif 的案例有一个细节经常被忽略。据 VPNCentral 的分析，Claude 找到了漏洞，但人类仍然验证了结果、编写了利用代码、处理了披露流程。Anthropic 自己的安全研究论文也明确提到，人工确认仍然是流程的组成部分。说白了，这不是「AI 独立完成了一切」，而是「AI 极大地压缩了从模糊线索到可用漏洞之间的距离」。

「研判」真正的范式转折不在于 AI 能否找到漏洞——这点已被反复证明——而在于进入门槛的骤降。过去，挖一个 Vim modeline 沙箱逃逸需要深入理解 Vim 源码结构、modeline 解析机制、沙箱实现细节。现在，一句「帮我找个打开文件就能 RCE 的零日」就够了。这对防御者来说意味着：漏洞从发现到被公开利用的时间窗口正在急剧压缩。

## 防御者的时间窗口

Anthropic 的研究报告提出了一个核心判断：AI 模型现在能以规模化的速度发现高严重性漏洞，而防御者率先使用这种能力与攻击者发展出等效能力之间的窗口正在收窄。

这不是危言耸听。据 VentureBeat 对 40 多位 CISO 的采访，大多数安全负责人对基于推理的漏洞扫描工具尚未建立正式的治理框架——他们没想到这种能力会在 2026 年初就到来。

而在硬币的另一面，独立研究者 Martin Alderson 指出了一个更令人不安的问题：Anthropic 的研究聚焦的是有维护者的活跃项目，补丁可以被交付。但互联网上存在大量被遗弃的软件——没人维护、没人打补丁，却仍然运行在数以百万计的服务器上。过去保护这些软件的唯一屏障是「不值得花人力去看」。现在这道屏障不存在了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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