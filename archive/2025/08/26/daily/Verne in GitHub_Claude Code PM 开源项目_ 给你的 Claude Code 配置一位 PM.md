---
title: Claude Code PM 开源项目: 给你的 Claude Code 配置一位 PM
url: https://blog.einverne.info/post/2025/08/claude-code-pm.html
source: Verne in GitHub
date: 2025-08-26
fetch_date: 2025-10-07T00:12:40.212949
---

# Claude Code PM 开源项目: 给你的 Claude Code 配置一位 PM

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

# Claude Code PM 开源项目: 给你的 Claude Code 配置一位 PM

Posted on 08/25/2025
, Last modified on 08/25/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-08-25-claude-code-pm.md)

在我使用使用 Claude Code 过程中，借鉴 Kiro，我逐渐习惯让 Claude Code 编写一个产品设计书放在 docs 文件夹下， 然后我会仔细地审查这一份产品设计文档， 修改其中的不明确的点， 或者是说 AI 理解错误的内容， 然后再让 Claude Code 通过这一个产品设计书来实现完整的代码。然而今天我看到的一个开源项目 Claude Code PM ，则是将我上面实现的这一套文档驱动的开发流程转变成了更专业的，更符合团队业务需求的流程，并且引入了敏捷开发，项目管理中的重要概念，及时是一个人的项目，通过 Claude Code PM 的流程约束，我发现 Claude Code 的智能程度也提升了不少。

并且项目通过和 GitHub Actions 进行集成，主要使用 GitHub Issues 以及 GitHub Actions 来管理项目整体的进度，通过任务的拆分使得我们可以并行地执行多个 Claude Code 实例，大大提升了 Claude Code 的使用效率。

[Claude Code PM](https://github.com/automazeio/ccpm)

## 痛点

在使用 Cloud Code 的过程当中，我们经常会遇到这样的问题

* 会话与会话之间的上下文消失， 这使得我们得不断提醒 AI 去重新查看相关文件
* 当多个 AI agent 开发同一段代码时， 修改同一段代码，并行工作可能会产生冲突
* 在工作当中，有一些决策都是口头规范，并没有约束在书面上，需求也会随之发生变化，AI 无法及时地了解。
* 追踪进度难，除非是 AI 执行到结束，否则我们无法看到执行的进度

面对上面的困境，Claude Code PM 将软件开发拆分成 PRD 文档、Epic 规划、任务拆解、GitHub 同步和并行执行五个阶段。通过 GitHub issues 和 Git worktree，通过 AI Agent 的并行工作，实现了从需求到代码的全链路可追踪。

我们可以通过以下的四个命令来了解一下整个交互执行过程，主要分成如下的几个步骤:

```
# Create a comprehensive PRD through guided brainstorming
/pm:prd-new memory-system

# Transform PRD into a technical epic with task breakdown
/pm:prd-parse memory-system

# Push to GitHub and start parallel execution
/pm:epic-oneshot memory-system
/pm:issue-start 1235
```

## 为什么要使用 Github?

大多数的 Claude Code 的工作流程都是独立运行的， 单个开发人员在其本地环境中与 AI 协作， 这带来了一个根本性的问题， AI 辅助开发变成了一个孤岛。 我们可以通过 GitHub Issues 作为我们的数据库， 这使得我们可以产生真正的团队协作。

* 多个 Claude 实例可以同时处理同一个项目。
* 开发人员可以通过评论实时查看进度。
* 团队的成员可以随时参与，上下文始终可见。
* 代码审查通过后，PR 自动发生。

虽然使用了 Vibe Coding，但严格遵守五阶段的纪律：

* 第一阶段：头脑风暴，在这个阶段，明确地梳理模糊的地方，定义好功能点。
* 第二阶段：文档，编写规范的文档，避免任何模糊的边界条件。
* 第三阶段：计划，具有明确的技术决策，通过专业的架构师角色完成。
* 第四阶段：执行，开始构建指定的内容。
* 第五阶段：追踪，每一步透明。

在每一个阶段当中，Claude Code PM 都设定了快捷命令。

### RPD

PRD 是 Product Requirements Document 产品需求文档，是软件开发生命周期中的核心文档之一。

PRD 是一份全面的、结构化的文档，概述了正在开发的产品的目标、特性、功能和约束条件。它起到了以下的关键作用：

* 项目蓝图，为业务和技术团队提供指导，帮助他们打造、发布或推销产品。
* 沟通桥梁，确保所有相关者在产品的景愿和执行计划上保持一致。
* 规范化工具，将商业需求文档和市场需求文档用更加专业的语言进行描述。

PRD 核心组成部分包括：

1. **问题陈述** 明确产品要解决的问题或机会。
2. **目标和目的** 制定可衡量、可实现的短期和长期目标。
3. **用户故事和用例** 定义目标用户需求，以及用户与产品的交互方式。
4. **功能需求** 描述产品的具体功能和特性。
5. **性能要求** 定义产品的性能标准和约束条件。

## Epic

Epic 是敏捷开发和项目管理中的一个重要概念，指大型功能需求和用户故事。

Epic 的定义是指一个非常大的功能特性，具有以下特征：

* **规模比较大**，通常需要分解成更多的 User Story 才能实现。
* **跨迭代**，一个 Epic 往往需要多个开发迭代 Sprint 才能完成。
* **业务价值高**，通常对应重要的业务目标和用户价值。

在敏捷开发中，按照颗粒度从大到小分成四个层级。

* **Epic** 使用：最大颗粒度的需求，代表重要的产品功能。
* **Feature** 特性：Epic 的细分，具体的功能模块。
* **Story** 用户故事：可在一个迭代中完成的具体需求。
* **Task**：Story 的具体实现，具体的开发任务。

在 Claude Code PM 系统当中，PRD 和 Epic 形成了清晰的转换关系。在 PRD 创建阶段，可以通过深度的头脑风暴产生全面的产品需求。稳打在 Epic 规划阶段，可以将 PRD 转化为技术实施的计划，形成 Epic 任务分解。

在 Epic 任务分解阶段，可以将 Epic 进一步拆分为具体的开发任务。从价值来看，在 PRD 轻型的转换关系中，可以将 Epic 轻型的转换关系中，PRD 文档主要服务于产品规划，从业务角度描述要做什么和为什么做；Epic 主要服务于技术实施，从工程角度的规划如何做和分几步做。

这种文档体系确保了从业务需求到技术实现的完整可追溯性，避免了传统开发中的模糊驱动编程的问题，让每一行代码都能追溯到明确的规范说明。

## 项目结构

```
.claude/
├── CLAUDE.md            # 全局指令与项目元信息
├── prds/                # 产品需求文档 (PRD)
├── epics/               # 实施规划与任务拆解
│   └── [epic-name]/
│       ├── epic.md      # 技术方案与架构决策
│       ├── [task].md    # 具体任务文件
│       └── updates/     # 子 Agent 进度更新
├── agents/              # 专用 AI Agent 执行环境
├── commands/            # pm: 系统命令定义
└── context/             # 上下文与规则文件
```

* **PRD 阶段**：通过  `/pm:prd-new feature-name`，生成结构化需求文档，涵盖愿景、用户故事、验收标准等。
* **规划阶段**：`/pm:prd-parse feature-name`  自动将 PRD 转化为技术实施计划 (epic.md)，明确架构决策和技术栈选择。
* **任务拆解**：`/pm:epic-decompose feature-name`  将 epic 拆分为可验收的子任务，并标注并行执行可能性。
* **GitHub 同步**：`/pm:epic-oneshot feature-name`  或  `/pm:epic-sync feature-name`，将 Epic 与任务推送为 GitHub Issues，结合 gh-sub-issue 插件实现父子关系。
* **并行执行**：通过  `/pm:issue-start 1234`  启动专用 Agent，多个 Agent 针对数据库、业务逻辑、API、UI、测试等独立并行工作，在各自工作树（worktree）中隔离上下文，最后同步合并，无冲突。

更多常用的命令参考

```
/pm:init 安装依赖 并配置 GitHub。
```

PRD Commands

```
# 针对新需求，开展头脑风暴。
/pm:prd-new memory-system

# Review and refine the PRD...

# 将需求文档变成可实施的计划。
/pm:prd-parse memory-system

# 列出所有的 PRD。
/pm:prd-list

# 编辑现有的 PRD。
/pm:prd-edit

# 显示 PRD
/pm:prd-status
```

Epic Commands

```
# 将设计拆分成任务
/pm:epic-decompose

# 将 Epic 推送到 GitHub
/pm:epic-sync

# 拆分任务并完成同步。  decompose and sync
/pm:epic-oneshot memory-system
# Creates issues: #1234 (epic)， #1235， #1236 (tasks)

# 列出所有 Epic
/pm:epic-list

# 列出 Epic
/pm:epic-show

# 标记完成
/pm:epic-close

# 编辑
/pm:epic-edit

# 更新任务的进度
/pm:epic-refresh
```

Issue Commands

```
# Start development on a task
/pm:issue-start 1235
# Agent begins work， maintains local progress

# 将更新推送到 GitHub
/pm:issue-sync 1235
# Updates posted as issue comments

# 显示 Issue
/pm:issue-show

# 查看状态
/pm:issue-status

# 将 issue 标记为完成
/pm:issue-close

# 重新打开 issue
/pm:issue-reopen

# 编辑 Issue
/pm:issue-edit
```

Workflow Commands

```
/pm:next - Show next priority issue with epic context
/pm:status - Overall project dashboard
/pm:standup - Daily standup report
/pm:blocked - Show blocked tasks
/pm:in-progress - List work in progress
```

Sync Commands

```
/pm:sync - Full bidirectional sync with GitHub
/pm:import - Import existing GitHub issues
```

Maintenance Commands

```
/pm:validate - Check system integrity
/pm:clean - Archive completed work
/pm:search - Search across all content
```

## Related Posts

* [Claude Code PM 开源项目: 给你的 Claude Code 配置一位 PM](/post/2025/08/claude-code-pm.html) - 08/25/2025
* [使用 GitHub Actions 构建 Docker 镜像并上传到 GitHub Packages](/post/2024/12/github-actions-docker-image-github-packages.html) - 12/21/2024
* [Github Actions 使用](/post/2020/04/github-actions-usage.html) - 04/12/2020

---

* [← Previous（前一篇）](/post/2025/08/whispering-open-source-offline-speech-text.html "Whispering 开源离线的语音转文字应用")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/08/claude-code-ccusage.html "Claude Code 利用 ccusage 统计使用情况")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/08/claude-code-pm.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [claude-code 13](/tags.html#claude-code)
* [claude-code-pm 1](/tags.html#claude-code-pm)
* [project-management 3](/tags.html#project-management)
* [pm 1](/tags.html#pm)
* [epic 1](/tags.html#epic)
* [prd 1](/tags.html#prd)
* [product 2](/tags.html#product)
* [github 35](/tags.html#github)
* [github-issue 1](/tags.html#github-issue)
* [github-actions 3](/tags.html#github-actions)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").