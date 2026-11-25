---
title: tuicr：基于 Rust 开发的开源终端代码审查工具，像审 PR 一样审查 AI 写的代码
url: https://blog.einverne.info/post/2026/11/tuicr-terminal-code-review-tool.html
source: Verne in GitHub
date: 2026-11-24
fetch_date: 2026-11-25T10:46:43.665140
---

# tuicr：基于 Rust 开发的开源终端代码审查工具，像审 PR 一样审查 AI 写的代码

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# tuicr：基于 Rust 开发的开源终端代码审查工具，像审 PR 一样审查 AI 写的代码 Vim 键位的终端 Code Review 工具，评论一键交给 AI 智能体或推送到 GitHub、GitLab

Posted on 11/24/2026
, Last modified on 11/24/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-11-24-tuicr-terminal-code-review-tool.md)

自从日常开发大量交给 [[Claude Code]] 和 [[Codex]] 之后，我发现自己的工作重心悄悄发生了变化：写代码的时间越来越少，看代码的时间越来越多。AI 一口气改了十几个文件，我得一个个检查，发现问题之后再用自然语言告诉它「auth.rs 第 42 行那个魔法数字改成常量」「第 50 到 55 行那段可以重构一下」。这个过程其实挺别扭的，`git diff` 只能看不能评论，打开 IDE 又要切换上下文，开个 PR 让自己审查更是多此一举。最近发现了一个专门解决这个问题的工具 [[tuicr]]，它把 GitHub PR 页面那套审查体验搬进了终端，审完之后一键把评论复制给 AI，上手试了一下感觉很顺手，所以来介绍一下。

![tuicr 终端代码审查工具示意图](https://pic.einverne.info/images/2026-11-24-15-30-00-tuicr-terminal-code-review.png)

## tuicr 是什么

[tuicr](https://github.com/agavra/tuicr) 是一个用 [[Rust]] 编写的终端代码审查工具（TUI），官网是 [tuicr.dev](https://tuicr.dev/)。名字是 TUI 和 CR（Code Review）的组合，作者在 README 里注明它读作「tweaker」。项目 2026 年 1 月 8 日才创建，到现在不到一年的时间已经积累超过 3600 个 Star，迭代速度也非常快。项目采用 MIT 协议开源，还拿到了 [[CodeRabbit]] 的赞助，后者本身就是做 AI 代码审查的公司。

tuicr 的核心定位：在终端里像审查 GitHub Pull Request 一样审查任何 diff。这个 diff 可以是你自己还没提交的改动、一段提交区间、同事提的 PR，或者是 AI 编程智能体刚刚生成的代码。审查完之后有两个动作：一是把评论导出成带编号的 Markdown，直接粘贴给 AI 让它修改；二是把真正的行内评论提交到代码托管平台上，目前支持 [[GitHub]]、[[GitLab]]、[[Gitea]]、Bitbucket Cloud、Azure DevOps 和 Gerrit 六个平台。

除了 Git 之外，tuicr 还支持 [[Jujutsu]]（jj）和 Mercurial（hg），这在同类工具里比较少见。对于已经开始用 jj 的朋友来说，这一点应该挺有吸引力。

## 为什么需要一个终端里的审查工具

在 AI 编程时代之前，代码审查主要发生在 PR 页面上，那是团队协作的交汇点。但现在情况变了，大量代码在进入 PR 之前，就已经需要人来审查一遍了。AI 生成的代码，总不能看都不看就提交吧？于是出现了一个新的审查环节：在本地、在提交之前、审查 AI 的产出。这个环节的需求和传统 PR 审查很像，需要连续浏览所有改动、在具体的行上留下意见、追踪哪些文件已经看过，但现有的工具都不太合适。

`git diff` 加 [[delta]] 之类的美化工具，看起来很舒服，但只能看，不能评论。IDE 的 diff 视图功能强大，但对于常驻终端的人来说切换成本不小，而且评论功能通常也和 PR 绑定。`gh pr review` 可以在命令行提交审查，但只能提交整体的批准或者请求修改，不能写行内评论。tuicr 的 README 里专门有一张对比表，把自己和 hunk、lumen、`gh pr review`、`git diff` 做了对比，它是唯一一个同时具备 Vim 键位、能把行内评论推送到 GitHub 以外的平台、支持 Mercurial、并且能导出给 AI 用的 Markdown 的工具。

我觉得 tuicr 最聪明的地方在于它想清楚了「审查结果给谁看」这个问题。传统审查工具的读者是人，所以评论散落在代码各处，靠界面来呈现上下文。而 tuicr 的导出格式是为 AI 设计的：每条评论带编号、带文件路径和行号，开头还有一句「I reviewed your code and have the following comments. Please address them.」，粘贴给任何智能体都能直接理解并逐条处理。

## 核心特性

第一个让我喜欢的设计是「一条连续的 diff」。所有改动过的文件在同一个视图里依次滚动，就像在 GitHub PR 页面上一样，左侧边栏是文件列表，标题栏会显示当前文件的增删行数。用 `j` / `k` 逐行滚动，`{` / `}` 在文件之间跳转，`[` / `]` 在 hunk 之间跳转，`Ctrl-d` / `Ctrl-u` 翻半页，`/` 搜索，基本就是 Vim 的肌肉记忆。另外，像 lock 文件这类自动生成的文件默认是折叠的，按空格才展开，避免一个 `Cargo.lock` 的改动刷掉好几屏。

这里顺便解释一下 hunk 这个词，它不是 tuicr 自创的概念，而是 diff 的通用术语，指 diff 中一块连续的改动区域。一个文件里如果有几处相隔较远的改动，diff 就会把它们切成几个 hunk，每个 hunk 只包含改动的行和前后少量未改动的上下文，中间大段没动的代码不显示。每个 hunk 以 `@@ -1,6 +1,10 @@` 这样的头部开始，意思是旧文件从第 1 行起的 6 行，在新文件中变成了从第 1 行起的 10 行。在 tuicr 里，hunk 是比文件更细一级的操作单位，可以按 hunk 跳转，也可以按 hunk 标记审查进度，一个大文件改了很多处的时候，一块一块地审查会比整个文件一次性看完更不容易遗漏。

第二个是 PR 风格的评论。按 `c` 在当前行添加评论，按 `C` 对整个文件评论，按 `v` / `V` 进入可视模式选中一段范围再评论，还可以按 `s` 提出代码修改建议，效果类似 GitHub 的 suggestion。如果团队有评论分类的习惯，可以在配置里定义 `comment_types`，比如把 `issue` 定义为「合并前必须修复」，导出时会自动带上 `[ISSUE]` 这样的标签。

第三个是审查进度追踪。按 `r` 把整个文件标记为已审查，按 `R` 只标记当前 hunk，侧边栏会显示「Files · 1/2」这样的进度。这些标记和评论都会持久化保存，下次打开同一个审查目标的时候还在。对于一次改动几十个文件的大型变更，这个功能非常实用，不用再靠脑子记哪些文件看过了。

第四个是和 AI 智能体的深度集成，这也是我认为它和其他 diff 工具拉开差距的地方。除了前面说的 Markdown 导出，它还提供了一个 `tuicr review` 子命令，可以在不打开 TUI 的情况下列出、读取、添加和删除评论，输出都是 JSON 格式。项目仓库里还自带一个 [tuicr Skill](https://github.com/agavra/tuicr/blob/main/skills/tuicr/SKILL.md)，智能体可以借助它在 cmux、Rex、tmux、Zellij 或者 [Herdr](https://blog.einverne.info/post/2026/07/herdr.html) 中打开一个分屏面板启动 tuicr，等你审查完之后再读取你的评论。这个 Skill 写得很讲究，明确区分了「用户审查 AI 的代码」和「AI 审查 AI 的代码」两种工作流，前者要求智能体不能自己添加评论，更不能冒充用户的评论。

## 安装

macOS 和 Linux 上最简单的是官方安装脚本或者 [[Homebrew]]：

```
curl -fsSL tuicr.dev/install.sh | sh
# 或者
brew install tuicr
# Arch Linux
sudo pacman -S tuicr
```

Rust 用户可以直接 `cargo install tuicr`，另外也支持 [[mise]]（`mise use github:agavra/tuicr`）、Nix 和 Home Manager。不想装包管理器的话，[GitHub Releases](https://github.com/agavra/tuicr/releases) 里有预编译的二进制，覆盖 macOS（Apple Silicon 和 Intel）、Linux（x86\_64 和 aarch64，分别提供 GNU 动态链接和 musl 静态链接两个版本）和 Windows。我下载的 macOS Apple Silicon 版本解压后是一个 11MB 的单文件，没有任何运行时依赖。之后升级执行 `tuicr update` 即可，它会识别你是通过哪种方式安装的，然后调用对应的包管理器去升级，对于 pacman 或 Home Manager 这类它不便代劳的安装方式，会直接提示你该用什么命令。

## 实际体验

常用的快捷键，修改完代码之后执行 `tuicr -w` 审查未提交的改动，启动速度非常快。界面左侧是修改的文件列表，文件前面是未审查的空心方框，右侧是连续的 diff，标题栏显示 `git:master · staged + unstaged`，表明它把暂存和未暂存的改动合在一起展示了，这个细节很贴心。

接着我按 `/` 搜索关键字，光标会直接定位关键字那一行，按 `c` 可以进入评论模式。按 Enter 或者 ctrl-s 保存评论，`esc cancel` 退出。保存之后文件标题上立刻出现了「1 comment」的标记，再按 `r` 标记文件已审查，侧边栏进度变成了 1/2，这个文件也自动折叠了起来。

然后我测试了一个更有意思的场景：在 TUI 还开着的时候，从另一个终端用 `tuicr review` 命令模拟智能体的操作。`tuicr review list --repo .` 返回了当前活跃的会话，带有 `"active": true` 标记，还能看到评论数和文件数；`tuicr review comments` 读到了我刚才在 TUI 里写的那条评论，包含精确的行号、作者和创建时间；接着我用 `tuicr review add --username claude` 以智能体的身份在第 7 行加了一条关于日志泄露用户名的评论。最后回到 TUI 执行 `:wq` 退出，导出的 Markdown 是这样的：

```
## Session: repo@master/staged-and-unstaged/ff76c49

I reviewed your code and have the following comments. Please address them.

Reviewing staged + unstaged changes

## Local tuicr Comments

1. `auth.rs:7` - println in a retry loop leaks the username to logs
2. `auth.rs:9` - Do not hardcode the password; read it from config
```

可以看到，通过 CLI 添加的评论也被包含进来了，并且两条评论按行号自动排好了序。这意味着人和智能体可以在同一个审查会话里协作，比如让 AI 先过一遍给出初步意见，你再补充自己的看法，最后统一导出交给另一个智能体去修改。审查会话保存在 macOS 的 `~/Library/Application Support/tuicr/reviews/sessions/` 目录下，每个会话是一个 JSON 文件，想用脚本处理也很方便。

按照文档，`tuicr pr` 会自动找到当前分支对应的 PR，也可以用 `tuicr pr 125` 或者直接传 PR 链接；在 PR 审查中执行 `:submit` 会弹出一个选择器，可以选择 Comment、Approve、Request changes 或者 Draft，行内评论会落到对应的代码行上，整体评论则作为审查摘要。各个平台的认证方式不同，GitHub 依赖 `gh auth login`，GitLab 依赖 `glab`，Gitea 依赖 `tea`，Azure DevOps 和 Gerrit 则需要配置环境变量，而且后两者还要求本地有仓库的克隆。

## 使用技巧与建议

常用的几种打开方式值得记一下：直接执行 `tuicr` 会打开一个目标选择器，让你选择要审查的提交；`tuicr -w` 审查未提交的改动并跳过选择器；`tuicr -r main..HEAD` 审查一段提交区间，对于 jj 用户则是传入 jj 的 revset 语法；`-p` 可以把 diff 过滤到某个文件或目录。还有一个容易被忽略的 `--file` 参数，它可以在没有版本控制的情况下直接打开一个文件或目录进行批注，适合给 AI 生成的文档或者配置文件写意见。

配置文件在 macOS 和 Linux 上位于 `~/.config/tuicr/config.toml`，下面是一个我觉得比较实用的起步配置：

```
theme = "catppuccin-mocha"   # 内置 24 套主题，也可以自定义
diff_view = "side-by-side"   # 并排显示，默认是 unified
editor = "nvim"              # 按 e 或 :edit 时打开的编辑器
leader = ";"                 # leader 键，;p 可以按路径跳转文件

[[comment_types]]
id = "issue"
color = "red"
definition = "must fix before merge"
```

如果你主要是和 AI 智能体配合使用，有几点建议。第一，可以用 `tuicr --stdout` 把导出结果直接打印到标准输出而不是剪贴板，这样在 tmux 或者通过 SSH 远程使用时不会遇到剪贴板不可用的问题。第二，导出格式里那些开场白和标题都可以在配置的 `[export]` 部分改写或者删掉，只保留编号评论，如果你习惯用中文和 AI 交流，可以把那句英文开场白改成中文，把某一项设为空字符串则会连同后面的空行一起省略：

```
[export]
intro = "我审查了你的代码，请逐条处理下面的意见。"
scope_line = false
comments_header = "## 审查意见"
```

这个配置只影响复制到剪贴板和 `--stdout` 输出的 Markdown，不影响通过 `:submit` 提交到平台的评论。第三，如果仓库里有不想审查的文件，可以在根目录放一个 `.tuicrignore` 文件，语法和 `.gitignore` 一样，支持 `!` 取反，匹配的文件会从审查 diff 中完全排除，而 `.gitignore` 里的规则 tuicr 本身就会自动遵守。第四，如果你让智能体通过 Skill 自动打开 tuicr，记得在同一个仓库里只保留一个活跃会话，Skill 文档里特别提醒过，同一个仓库可能同时存在工作区和提交区间两个会话，把评论加到错误的会话里命令也会正常返回，很难察觉。

最后提一个使用习惯上的建议：不要只把 tuicr 当成审查 AI 代码的工具。每次自己提交之前用 `tuicr -w` 过一遍改动，按 `r` 一个个标记文件，这个过程会强迫你真正把每个改动看一遍，比 `git add -p` 更系统，也比提交之后再在 PR 页面上自查要早得多。

## 最后

试用下来，我最大的感受是它准确地抓住了 AI 编程时代一个被忽视的环节：人类审查 AI 代码的那一步。以前这一步要么被跳过，要么在 IDE、终端和聊天窗口之间来回切换，现在可以在终端里一气呵成地完成浏览、评论、追踪进度，再一键把结构化的意见交回给 AI。Rust 带来的单文件、零依赖、启动快，加上完整的 Vim 键位，对常驻终端的开发者来说几乎没有学习成本。

当然它也还很年轻，版本号还没到 1.0，每个版本都有大量的修复，文档和实际行为偶尔会有出入，比如我遇到的评论保存快捷键。但从迭代速度和设计的细致程度来看，作者显然很认真地在打磨它。如果你也和我一样，每天花大量时间审查 AI 写的代码，强烈推荐试试 tuicr。至少下次 AI 改完代码之后，你不用再对着 `git diff` 的输出手打「第几行第几行有问题」了。

## Related Posts

* [Herdr 使用技巧，把一群 Coding Agent 用出花来](/post/2026/09/herdr-tips-and-tricks.html) - 09/02/2026
* [Claude Code 环境变量完全指南：解锁隐藏特性与效率配置](/post/20...