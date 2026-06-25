---
title: AI Coding Agent 时代，我自己最常用的 4 个终端工具
url: https://mp.weixin.qq.com/s/xxjE8XVMg43SsOZk40LzKw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:58.531905
---

# AI Coding Agent 时代，我自己最常用的 4 个终端工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5naxUv4nJVIl1WN5xQMsicIibXZegxYnHmczMYePMJQYXlh7HF3fj9vibpvr5a9dbVtpqgZvkribsL3eqqjialzaO6ZKTHick71o3w1uFlB62lIWI/0?wx_fmt=jpeg)

# AI Coding Agent 时代，我自己最常用的 4 个终端工具

原创

crossoverjie
crossoverjie

crossoverJie

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5naxUv4nJVLjEWVYcnIJEFg2MGKt7hWOtK9pKto4iaQ24EWwjDKWCIWGMxZ5j9nXlnSOmBNdJlVTciboxw8HSm6UrprfKFPcdLYuKvksnvtUI/640?wx_fmt=png&from=appmsg)

# 背景

以前学 linux 命令行，常见路线是记住一堆 `grep`、`find`、`sed`、`awk`，然后自己在代码库里定位问题、筛选文件、拼接命令。

但进入 Coding Agent 时代后，我觉得人和终端的分工变了。

代码搜索、读取配置、分析调用链、运行测试，这些工作本来就是 Agent 擅长的。面对一个仓库，Claude Code、Codex 之类的 Agent 会自己判断该用 `rg`、`git diff`、`jq` 还是别的工具；我不需要为了"指挥 Agent"而把这些命令全学一遍。

我更常用的，是另一类命令：

* 快速进入正确项目；
* 把准确的文件路径交给 Agent；
* 从大量文件里选出我想让它看的那个；
* 跑长任务时，避免 Mac 睡眠导致 Agent 中断。

下面是我目前最常用的一套。

---

## 1. `realpath`：跨项目引用文件时，给 Agent 一个准确的地址

用 Agent 的时候，大部分情况下你不需要操心路径——Agent 自己会 `cd` 进项目目录，该读什么文件它自己会找。

但有一个场景例外：**你在 A 项目里工作，需要参考 B 项目的文件**。

比如你正在 A 项目里做重构，想让 Agent 参考 B 项目里的一个实现。这时候你没法直接在 A 项目里 `@` B 的文件，因为它们不在同一个仓库目录下。

我最常见的做法是：切到 B 项目的终端，`realpath` 一下目标文件，把绝对路径复制过来，告诉 Agent 去读。

```
realpath ~/Code/project-b/src/service/payment.go
```

输出：

```
/Users/aurora/Code/project-b/src/service/payment.go
```

然后回到 A 项目的 Agent 对话里：

> 请阅读 `/Users/aurora/Code/project-b/src/service/payment.go`，参考它的重试逻辑，帮我在 A 项目里实现类似的功能。

这样 Agent 就能跨项目读取文件，不受当前工作目录的限制。

### 我会把它封装成 `rp`

![](https://mmbiz.qpic.cn/mmbiz_png/5naxUv4nJVJc3EHUNCB1r6TRDAt5upnThQrKufqsaIticWPmCkKoqsq5cXcrQnfktEwD70a0HqRtf9471MqHVeQ1U1NOSxIzFXVVROTNE0wc/640?wx_fmt=png&from=appmsg)

跨项目引用是高频操作，所以我做了一个小函数：输出路径、自动复制到剪贴板、再告诉我复制成功。

```
rp() {
  local p

  p=$(realpath "$@") || return
  printf '%s' "$p" | pbcopy
  printf 'Copied: %s\n' "$p"
}
```

放进 `~/.zshrc` 后，重新加载：

```
source ~/.zshrc
```

之后切到 B 项目终端，只需要：

```
rp src/service/payment.go
```

终端会显示：

```
Copied: /Users/aurora/Code/project-b/src/service/payment.go
```

然后切回 A 项目的 Agent 对话，直接粘贴路径，告诉它要参考什么。

这比手动拼路径或者在两个终端之间来回切换要顺畅很多。

---

## 2. `zoxide`：不用记路径，只要记得项目大概叫什么

项目多起来以后，最烦的不是打开终端，而是进入正确目录。

传统方式可能是：

```
cd ~/Code/company/backend/payment-service
```

路径长、层级深，而且每个项目的目录结构不一样。更常见的情况是，你只记得项目大概叫 `payment`，但不记得它放在 `~/Code`、`~/Workspace` 还是某个 worktree 目录下。

`zoxide` 的思路很简单：它会根据你的访问记录，为目录建立使用频率和最近访问的排序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5naxUv4nJVJWanSTkzGP1wgdMgWxOboIZn9ZSZABuicBMce85DYpt3mTvuXibF2J0b5ZjcFpSbz2HiaGBXLz5cSdrNiaCA3vqZAD5rjkUkXTqRw/640?wx_fmt=png&from=appmsg)

安装后，常见用法是：

```
z pulsar
```

它会跳到最符合 `pulsar` 的常用目录。

如果候选目录不止一个，可以使用交互模式：![](https://mmbiz.qpic.cn/sz_mmbiz_png/5naxUv4nJVKQlFicm522LPibc1Jia3icFCXyFjicyLsqJ3a6cGFIiaXcSbztIFg8XCzOZibzriaogFLhIicl2vfDibSjcOCRGibKictvJym5dzSygWviaf1c/640?wx_fmt=png&from=appmsg)

```
zi
```

或者：

```
zi starr
```

然后通过模糊搜索选择目标目录。

对于日常 Agent 工作流，`zoxide` 的意义并不只是"替代 `cd`"，而是更快回答一个问题：

> 我应该在哪个项目、哪个 worktree 里启动这个 Agent？

比如你平时有：

```
~/Code/my-app
~/Code/my-app-fix-login
~/Code/my-app-refactor
~/Code/my-app-release
```

你不需要回忆完整路径，只需要：

```
zi my-app
```

选中正确工作区后，再启动 Agent。

对于经常并行处理多个项目、多个分支、多个 worktree 的人来说，这个体验很容易形成习惯。

---

## 3. `fzf` + `fp`：从文件列表中选中目标，并把绝对路径直接交给 Agent

`fzf` 是一个终端里的模糊选择器。

它可以用于命令历史、目录、Git 分支、进程列表等很多场景，但我自己最常用的用途只有一个：

> 当我知道"我想让 Agent 看一个文件"，但不想手动输入完整文件名时，用它选中并复制路径。

我给它配了一个 `fp` 函数，意思是 file path：

```
fp() {
local file
local path

  file=$(fzf) || return
  path=$(realpath "$file") || return

printf'%s'"$path" | pbcopy
printf'Copied: %s\n'"$path"
}
```

使用时只需要在项目目录里输入：

```
fp
```

然后输入几个关键词，例如：

```
feature
```

`fzf` 会实时筛选文件。选中后按回车，完整绝对路径就已经进了剪贴板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5naxUv4nJVJ5aJuyiaAVuh4TLZfFsRaCiaCOQicUykkcbCDWTdsWqibFhs2TMRag4EnficImpm0pjYlpbk4durJXpK8ZxWpz0Kzm4KRlGGWH3Vxk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/5naxUv4nJVIp69msaKxiaDnRjnXvgzphAnrJQBhqj8iaIibC9yw02xoM9EMc0DPSMETibFor2H7LESysjcpegv96CEoFfB2WIjtFVqWHFKgMsIk/640?wx_fmt=png&from=appmsg)

接下来可以直接对 Agent 说：

> 请阅读我刚刚复制的这个文件，先解释它的作用，再帮我确认是否存在兼容性风险。

这个流程特别适合下面几类场景：

* 你在 Finder、IDE 或终端中看到一个文件，但路径很深；
* 项目里有很多同名或近似命名的配置文件；
* 你知道文件名的一部分，但不想手动补完整；
* 你想精确限制 Agent 的阅读范围；
* 你准备让 Agent 修改一个文件，希望先明确告诉它目标路径。

### 给 `fzf` 开启 Shell 集成

如果你使用 zsh，可以把下面这行放进 `~/.zshrc`：

```
source <(fzf --zsh)
```

重新加载配置：

```
source ~/.zshrc
```

除了 `fp`，这还会带来几个很实用的快捷键：

```
Ctrl-R：模糊搜索历史命令
Ctrl-T：选择文件或目录，插入当前命令行
Alt-C：选择目录并切换过去
```

但对我来说，`fp` 才是最贴近 Agent 协作的一个封装：

> 选中一个文件 → 转成绝对路径 → 自动复制 → 交给 Agent。

---

## 4. Otty 的保活机制：让长时间 Agent 任务不被 Mac 睡眠打断

AI Agent 任务经常比普通命令跑得久。

例如：

* 让 Agent 分析一个大型仓库；
* 跑完整测试集；
* 做跨模块重构；
* 生成升级兼容性报告；
* 等待多个子任务完成；
* 长时间运行 Claude Code、Codex 或其他本地 Agent。

这时一个很现实的问题是：Mac 可能进入显示器休眠或系统休眠，导致终端任务暂停，Agent 的执行也被打断。

如果你使用 Otty，可以开启它的：

```
Prevent Sleep While Processing
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5naxUv4nJVJqfJ18lRlBNgz5BK26j9wEStq0u0h9h6Ilug8Ork4gZwRkkBvdsP7wtIw5Gx2S5ug5e3HicTySb0PwVg6pHhPqAJQbSRvciawZk/640?wx_fmt=png&from=appmsg)

打开后，Otty 会在 Agent 正在处理任务时保持 Mac 唤醒；当 Agent 进入空闲状态后，又会自动释放这个保活状态。

这比手动执行一个长期保活命令更符合 Agent 工作流，因为它只在真正需要时保持机器唤醒。

我会把它理解为 Agent 任务的"运行保险"：

> 不是让 Mac 永远不睡，而是确保一个正在执行的重要任务不会因为系统休眠而半途停止。

尤其是晚上跑长任务、挂着多个 Agent、暂时离开电脑时，这个设置很值得打开。

---

## 一套很简单的 Agent 协作流程

这几个工具并不是替代 Agent，而是让你更好地把任务交给 Agent。

一个典型流程大概是这样：

```
# 1. 快速进入项目或 worktree
zi my-project

# 2. 找到你想让 Agent 重点看的文件
fp

# 3. 粘贴路径，告诉 Agent 要做什么
# 例如：
# 请检查 /Users/aurora/Code/my-project/configs/prod/app.yaml
# 重点分析生产环境风险，并给出最小修改方案。

# 4. 如果任务会很久，打开 Otty 的 Prevent Sleep While Processing
```

跨项目引用时，流程稍有不同：

```
# 1. 切到 B 项目终端，复制目标文件路径
rp src/service/payment.go

# 2. 回到 A 项目的 Agent 对话，粘贴路径
# 例如：
# 请阅读 /Users/aurora/Code/project-b/src/service/payment.go
# 参考它的重试逻辑，帮我在 A 项目里实现类似的功能。
```

---

## 我不再刻意学习的命令

像 `rg`、`fd`、`jq`、`ast-grep` 当然都是很好的命令行工具。

但在我的工作流里，它们更偏向 Agent 的执行工具，而不是我必须熟练掌握的工具。

我关心的是：

* Agent 在哪个目录运行；
* 它应该看哪个文件；
* 我如何快速把目标路径交给它；
* 多个项目之间怎样切换；
* 长任务能不能稳定跑完；
* 完成后我如何回到结果验证。

换句话说：

> Agent 负责在仓库内部探索和执行；我负责把正确的项目、正确的目标和正确的约束交给它。

这也是我理解的 AI Coding Agent 时代终端分工。

终端不再只是"人手工敲命令的地方"，它更像是一个控制台：

* 用 `zoxide` 找到正确工作区；
* 用 `fzf` 从大量文件中选定目标；
* 用 `realpath + pbcopy` 把准确地址交给 Agent；
* 用 Otty 保证长任务不中断。

不需要掌握几十个复杂命令。

先把这几个高频动作做得足够顺手，就已经能明显改善和 Coding Agent 协作时的体验。

# 总结

AI Coding Agent 时代，人和终端的分工发生了变化。Agent 负责在仓库内部探索和执行，而我负责把正确的项目、正确的目标和正确的约束交给它。

这套工具链的核心思路就四个字：**精准投喂**。

| 工具 | 解决的问题 | 核心动作 |
| --- | --- | --- |
| `realpath + rp` | 跨项目引用文件，Agent 没法直接 @ | 跨项目路径 → 绝对路径 → 剪贴板 |
| `zoxide` | 项目多了记不住路径 | 模糊关键词 → 跳转到正确目录 |
| `fzf + fp` | 文件太多不想手动输入 | 模糊搜索 → 选中文件 → 复制路径 |
| Otty 保活 | 长任务被 Mac 睡眠打断 | 自动检测任务状态 → 按需防休眠 |

不需要掌握几十个复杂命令，先把这几个高频动作做得足够顺手，就已经能明显改善和 Coding Agent 协作时的体验。

[1]

`zoxide`: *https://github.com/ajeetdsouza/zoxide*

[2]

`fzf`: *https://github.com/junegunn/fzf*

[3]

Otty: *https://docs.otty.sh/agents/parallel-tasks#keep-macos-awake*

往期推荐

[从 Warp 换到 cmux：一个更适合 AI Agent 的终端](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488967&idx=1&sn=00f0be02383159c662abf1b10b49a1bf&scene=21#wechat_redirect)

[我做了一个 AI 版的 StarRocks 升级风险扫描工具，直接帮我定位到一个风险](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488952&idx=1&sn=45187814f74f0432df8a01976e4bb16d&scene=21#wechat_redirect)

[Claude Opus 4.8 发布 + 650 亿融资：Anthropic 这两周太猛了](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488917&idx=1&sn=cee066764e3b1d5b5641051236fc8c82&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5naxUv4nJVKogBUel4kXpevTj3aWxDCMmFnmN3EkIH8VhCzXtmHsdn2szz1tTnvB4ZN85eyQVxene7scSuAbiacnbonRWCddkcQnHeJEA8RQ/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5naxUv4nJVLEXgMUOARlDiaXno8ib5FtX1PwweGqZRiaf2AHxBLTyxFY8pibBricvRLVl7X0rErmu2XgZhmJV4ic1ISNCib4veshybVyHzr2A2hicXY/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/5naxUv4nJVLJCUibJKSETf5y2uadXSf3JbJJtmAvvC3j9PJAowHiarMqBWgicFYCWBbWI03tI22qGCEgrL6Iics9SwxWgN7xnO1geruzdqkaJVw/640?wx_fmt=gif&from=appmsg)

**点点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5naxUv4nJVJQ6XrQbRJSTr2go9iaRNx7bWmbMay0SIg5cnmiam1qJId8icVsCcqBqqWQluYYPV6OSgib9uzk0fggz7nAQbacay1Q42INhl6sVU0/640?wx_fmt=gif&from=appmsg)

**点在看**

预览时标签不可点

...