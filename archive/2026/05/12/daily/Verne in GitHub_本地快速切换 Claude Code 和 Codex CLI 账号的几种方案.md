---
title: 本地快速切换 Claude Code 和 Codex CLI 账号的几种方案
url: https://blog.einverne.info/post/2026/05/switch-claude-code-codex-accounts.html
source: Verne in GitHub
date: 2026-05-12
fetch_date: 2026-05-13T05:45:53.180912
---

# 本地快速切换 Claude Code 和 Codex CLI 账号的几种方案

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

# 本地快速切换 Claude Code 和 Codex CLI 账号的几种方案 告别每次 logout/login 的繁琐，用 profile 机制一键切换

Posted on 05/12/2026
, Last modified on 05/12/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-05-12-switch-claude-code-codex-accounts.md)

同时维护个人项目和工作项目的时候，最让我头疼的不是代码本身，而是工具的账号管理。[[Claude Code]] 和 [[Codex]] 这类 AI 编程工具，我在公司有一套账号，个人订阅又是另一套。每次在项目之间切换，都要 `claude auth logout` 再 `claude auth login`，不仅耗时，还经常忘了当前用的是哪个账号，写了半天才发现额度消耗到错误的账号上去了。

这个问题在社区里也有不少人反映。[[Claude Code]] 的 GitHub issue #261 从 2025 年初提出原生 multi-account 支持，到现在积累了几十个 upvote，还有一个 issue 描述有人花了 40 分钟才搞定账号切换，可见这不是个小众需求。好消息是，虽然官方没有内置完善的 profile 系统，社区已经摸索出了几套成熟的方案。

![在两个终端窗口中同时运行不同账号的 Claude Code](https://pic.einverne.info/images/2026-05-12-14-30-00-switch-ai-accounts.png)

## Claude Code 的账号存储机制

在讨论切换方案之前，先理解 Claude Code 的认证数据存在哪里。默认情况下，所有配置、认证 token、会话历史都存放在 `~/.claude/` 这一个目录里。这个目录结构大致如下：

```
~/.claude/
├── settings.json          # 配置文件（不含凭证）
├── sessions/              # 会话历史
├── plugins/               # 插件数据
└── cache/                 # 缓存
```

OAuth token 通过 `claude auth login` 登录后存储在系统中，与 `~/.claude/` 绑定。切换账号的本质，就是让 Claude Code 指向一个不同的配置目录，从而读取不同账号的认证数据。

[[Claude Code]] 支持一个关键环境变量：`CLAUDE_CONFIG_DIR`，它允许你指定 Claude Code 使用的配置目录，而不是默认的 `~/.claude/`。一切账号切换方案都围绕这个环境变量展开。

## Claude Code 切换方案

### 直接使用环境变量（最简单）

最直接的方式是在启动 Claude Code 时临时指定配置目录：

```
# 使用工作账号
CLAUDE_CONFIG_DIR=~/.claude-work claude

# 使用个人账号
CLAUDE_CONFIG_DIR=~/.claude-personal claude
```

第一次用某个目录启动时，Claude Code 会自动创建该目录并引导你登录，之后该目录就保存了那个账号的认证信息。这种方式零依赖，但每次都要手动输入变量名，比较麻烦。

### Shell 函数封装（推荐的手动方案）

把环境变量封装进 Shell 函数，添加到 `~/.zshrc` 或 `~/.bashrc` 里，就能用简短命令切换：

```
claude() {
  local profile="personal"
  local claude_args=()

  while [[ $# -gt 0 ]]; do
    case $1 in
      -p|--profile)
        if [[ -n "$2" && "$2" != -* ]]; then
          profile="$2"
          shift 2
        else
          echo "Error: -p requires a profile name" >&2
          return 1
        fi
        ;;
      *)
        claude_args+=("$1")
        shift
        ;;
    esac
  done

  echo "Claude Code profile: $profile"
  CLAUDE_CONFIG_DIR="$HOME/.claude-$profile" command claude "${claude_args[@]}"
}
```

这样就可以用 `claude -p work` 启动工作账号，`claude` 不带参数则用个人账号（默认值 `personal`）。这个方案来自社区，简洁有效，缺点是第一次设置需要手动登录每个 profile。

这里有一个注意点：`CLAUDE_CONFIG_DIR` 需要绝对路径，写 `~/.claude-work` 在某些上下文下可能无法展开，用 `$HOME` 更安全。

### claude-switch 工具（功能最完整）

[claude-switch](https://claudeswitch.dev/)（GitHub: `Abhishek21k/claude-switch`）是一个专门为 Claude Code 多账号设计的工具，核心命令是 `cswitch`：

```
# 安装（npm 或 brew）
npm install -g claude-switch

# 把当前已登录的账号保存为 work profile
cswitch add work

# 登录一个新账号并保存为 personal profile
cswitch login personal

# 使用某个 profile 启动 Claude
cswitch use work
cswitch use personal

# 查看所有 profiles
cswitch list

# 打开交互式 TUI 菜单
cswitch
```

它的机制和上面的 Shell 函数一样，本质上都是把 profiles 存在独立目录（`~/.claude-switch/profiles/<name>/`），切换时通过 `CLAUDE_CONFIG_DIR` 告诉 Claude Code 用哪个。工具的亮点在于：第一次运行时会检测你当前已登录的 session，可以选择直接复制而无需重新登录；支持同时在不同终端窗口运行不同账号；支持把常用 profiles 设置为 Shell alias（比如 `claude-work`、`claude-personal`）。

macOS 上认证 token 存储在 Keychain 里，每个 profile 完全隔离。

### direnv 按目录自动切换（最适合多客户场景）

如果你同时服务多个客户或多个团队，每个客户的项目放在不同目录下，[direnv](https://direnv.net/) 方案可以做到进入目录就自动切换账号，无需任何手动操作：

```
~/personal/.envrc           ← 个人项目父目录
~/personal/blog/
~/personal/open-source/
~/work/company/.envrc       ← 公司项目父目录
~/work/company/webapp/
~/clients/acme/.envrc       ← 客户 Acme 项目父目录
~/clients/acme/api/
```

每个 `.envrc` 文件只需一行：

```
# ~/personal/.envrc
export CLAUDE_CONFIG_DIR="$HOME/.claude-profiles/personal"

# ~/work/company/.envrc
export CLAUDE_CONFIG_DIR="$HOME/.claude-profiles/org/company"

# ~/clients/acme/.envrc
export CLAUDE_CONFIG_DIR="$HOME/.claude-profiles/clients/acme"
```

安装 direnv 并允许这些 `.envrc` 文件后（`direnv allow`），每次 `cd` 进某个目录，对应的 `CLAUDE_CONFIG_DIR` 就会自动生效，离开目录时自动还原。这个方案还有一个额外的好处：MCP 服务器的认证信息也跟着隔离了，不同客户的 GitHub、Slack、Linear 凭证不会互相混淆。

## Codex CLI 的账号存储机制

[[Codex]] CLI 的认证存储比 Claude Code 更直接：`~/.codex/auth.json` 这个文件就是当前账号的全部认证数据，包含 OAuth token 或 API key。`~/.codex/config.toml` 是配置文件，支持 profiles 功能（通过 `-p` 参数选择）。

```
~/.codex/
├── auth.json              # 当前认证（权限 600）
├── backup_auth.json       # 认证备份
├── config.toml            # 配置文件
└── sessions/              # 会话历史
```

理解了这个结构，切换方案就很清晰了：只要把不同账号的 `auth.json` 保存起来，需要时替换，就完成了切换。

## Codex CLI 切换方案

### codex-profiles 工具

[codex-profiles](https://github.com/midhunmonachan/codex-cli-profiles) 是一个专门管理 Codex CLI 账号的工具，把切换 `auth.json` 的操作封装成简洁命令：

```
# 安装
npm install -g codex-profiles

# 保存当前账号为 work
codex-profiles save --label work

# 保存当前账号为 personal
codex-profiles save --label personal

# 查看所有 profiles
codex-profiles list

# 加载 work 账号
codex-profiles load --label work --force
```

Profiles 存储在 `~/.codex/profiles/` 目录下，每个 profile 就是一份 `auth.json` 的副本。切换时 `load` 命令把对应的 `auth.json` 复制覆盖到 `~/.codex/auth.json`，下次启动 `codex` 就会使用那个账号。数据完全本地，不会上传到任何地方。

### 内置 –auth-profile 参数

Codex CLI 在较新版本（commit `2ac14d1`）添加了内置的 `--auth-profile` 参数，专门为 multi-account 场景设计：

```
# 用指定 auth profile 启动
codex --auth-profile work

# 登录并保存为指定 profile
codex login --auth-profile personal
```

这是官方原生方案，如果你的 Codex CLI 版本足够新，优先使用这个。用 `codex --version` 确认版本，然后 `codex --help` 看看 `--auth-profile` 是否出现在参数列表里。

### 环境变量方案

对于使用 API key 认证的场景（推荐用于 CI/CD 或脚本化工作流），最简洁的方式是直接通过环境变量切换：

```
# 个人账号
export OPENAI_API_KEY="sk-personal-xxxx"
codex

# 工作账号
export OPENAI_API_KEY="sk-work-xxxx"
codex
```

结合 `direnv` 同样可以实现进入项目目录自动切换 API key，适合多项目环境。

## 限制与注意事项

几个使用时需要留意的地方：

对于 Claude Code，`CLAUDE_CONFIG_DIR` 的隔离并不是百分之百完整。`~/.claude/CLAUDE.md` 这个全局指令文件，无论 `CLAUDE_CONFIG_DIR` 指向哪里，都会被加载。此外 `~/.local/state/claude/` 这个状态目录在所有 profiles 间共享，IDE 插件（如 JetBrains）可能也存在兼容性问题。但最关键的认证数据和会话历史是完全隔离的，日常切换已经够用。

对于 Codex，`codex-profiles` 导出的 bundle 文件包含认证 token，妥善保管，不要提交到 Git 或存放在共享位置。

## 最后

Claude Code 目前最成熟的方案是 `cswitch` 工具加上 Shell 函数封装，两者都基于 `CLAUDE_CONFIG_DIR` 环境变量，原理清晰、易于理解和排障。如果你经常在多个客户项目之间切换，`direnv` 方案可以彻底解放双手，进目录即自动切换，离开即还原。Codex CLI 则优先看你的版本是否支持内置的 `--auth-profile` 参数，不支持的话 `codex-profiles` 是很好的替代选择。

这些方案的共同思路都是：不修改官方工具本身，而是通过环境变量或配置目录隔离来实现多账号共存。一旦理解了这个核心机制，遇到其他 CLI 工具需要多账号切换时，也可以举一反三地应用。

## Related Posts

* [Claude Code /goal：让 AI 自主持续工作直到达成目标的新命令](/post/2026/05/claude-code-goal-command.html) - 05/13/2026
* [本地快速切换 Claude Code 和 Codex CLI 账号的几种方案](/post/2026/05/switch-claude-code-codex-accounts.html) - 05/12/2026
* [codex-lb：用负载均衡的思路管理多个 ChatGPT 账号](/post/2026/05/codex-lb-chatgpt-account-load-balancer.html) - 05/12/2026
* [cc-switch：在多个 AI 编码工具之间优雅切换](/post/2026/05/cc-switch.html) - 05/04/2026
* [CLIProxyAPI 把 Claude Code、Gemini CLI、Codex 订阅包装成统一 API 的开源神器](/post/2026/04/cliproxyapi-unified-ai-gateway-for-cli-subscriptions.html) - 04/07/2026
* [Obsidian CLI 来了：从终端操控你的知识库](/post/2026/03/obsidian-cli-introduction.html) - 03/21/2026
* [Atuin：用数据库替换 Shell 历史，跨设备同步不再是难题](/post/2026/03/atuin-shell-history-sync.html) - 03/18/2026
* [Ghostty 终端配置技巧：从入门到舒适](/post/2026/03/ghostty-terminal-tips-and-tricks.html) - 03/17/2026
* [推荐我使用的 Agent Skills](/post/2026/01/recommended-agent-skills.html) - 01/19/2026
* [Vibe Kanban：当 AI 开始并行协作，我们的开发方式变了](/post/2026/01/vibe-kanban-parallel-ai-worktree.html) - 01/01/2026

---

* [← Previous（前一篇）](/post/2026/05/socat-command-usage.html "socat：比 netcat 更强大的网络瑞士军刀")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2026/05/claude-code-goal-command.html "Claude Code /goal：让 AI 自主持续工作直到达成目标的新命令")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/...