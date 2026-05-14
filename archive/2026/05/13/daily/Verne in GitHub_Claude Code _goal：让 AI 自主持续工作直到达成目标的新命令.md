---
title: Claude Code /goal：让 AI 自主持续工作直到达成目标的新命令
url: https://blog.einverne.info/post/2026/05/claude-code-goal-command.html
source: Verne in GitHub
date: 2026-05-13
fetch_date: 2026-05-14T05:45:34.163936
---

# Claude Code /goal：让 AI 自主持续工作直到达成目标的新命令

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

# Claude Code /goal：让 AI 自主持续工作直到达成目标的新命令 设定完成条件，Claude 跨轮次自动工作直到达成

Posted on 05/13/2026
, Last modified on 05/13/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-05-13-claude-code-goal-command.md)

用 [[Claude Code]] 写代码时，一直有一个令人微妙不适的摩擦：每当 Claude 完成一轮工作，控制权就回到了我这里，我需要再次发出指令，告诉它”继续”“再检查一遍”“还有这个文件没改”。对于那种需要跑很多轮才能完成的任务——比如把一个模块从旧 API 迁移到新 API 直到所有测试通过，或者逐文件重构某个目录直到符合统一规范——这个”人类中继”的环节就显得相当机械，本质上我只是在不停地按确认键。

[[Claude Code]] 最新推出的 `/goal` 命令针对的正是这个场景：你描述一个完成条件，Claude 就跨多个 turn 持续工作，每轮结束后由一个独立的小模型来判断条件是否满足，满足则停，否则继续。不再需要人类守在旁边不断催促。

![Claude Code /goal 命令](https://pic.einverne.info/images/2026-05-13-09-00-00-claude-code-goal-feature.png)

## /goal 是如何工作的

`/goal` 的核心机制可以用一句话概括：在每轮 Claude 工作结束后，引入一个独立的评估模型来判断”目标是否达成”，未达成则自动触发下一轮，达成则停止并清除目标。

具体来说，整个循环是这样运转的：你输入 `/goal` 加上完成条件的描述，这个命令本身就直接触发第一轮工作，不需要额外再发一条指令。每轮 Claude 完成工作后，目标条件和当前对话内容一起被发给一个小型快速模型（默认是 Haiku），该模型返回两样东西：一个是/否的判断，以及一段简短的理由解释为什么条件达成或还未达成。如果判断是”未达成”，那段理由还会作为下一轮的参考信息传给 Claude，引导它的后续工作方向。

这种设计有一个微妙但重要的含义：**评估和执行是分离的**。做事的模型和判断事情是否做完的模型不是同一个，这避免了 Claude 既当运动员又当裁判时可能产生的自我满足倾向。一个 fresh 的评估模型会更客观地判断条件是否真的满足。

目标激活期间，界面上会显示 `◎ /goal active` 的状态指示，并且记录目标已经运行了多久。每次评估后，最新的评估理由也会出现在状态栏里，让你随时能看到 Claude 当前正在朝哪个方向努力。

## 基本用法

用法很直接，输入 `/goal` 加上你的完成条件就可以：

```
/goal 迁移 auth 模块到新版 API，直到所有相关测试全部通过
```

```
/goal 重构 components/ 目录下所有组件，确保没有 TypeScript 类型错误
```

```
/goal 找出并修复所有导致 CI 失败的问题，直到 CI 全绿
```

同一个 session 里只能有一个 goal 处于激活状态。如果在目标达成前想中途放弃，用 `/goal clear` 清除即可，`stop`、`off`、`reset`、`none`、`cancel` 这些词也都被接受为 `clear` 的别名。

不带参数运行 `/goal` 可以查看当前状态，包括已跑的 turn 数和消耗的 token 数：

```
/goal
```

如果已经有一个 goal 在跑，再次用 `/goal <新条件>` 会直接替换掉旧的目标。通过 `/clear` 开始新对话也会清除当前的 goal。

会话中断后用 `/continue` 恢复时，目标本身会保留，但 turn 计数、计时器和 token 消耗的基线会重置，相当于重新开始计算。

## 与 /loop 和 Stop hook 的对比

Claude Code 里有几种”让 Claude 持续工作”的机制，它们的区别值得理清楚：

`/goal` 在每轮结束后立即触发下一轮，用模型评估条件是否满足来决定是否停止，条件是用自然语言描述的——适合”做到某个状态才算完”的任务。

`/loop` 是按时间间隔触发，你设定一个时间窗口（比如每 5 分钟），Claude 会周期性醒来工作一次，停止的时机是你手动叫停，或者 Claude 自己判断工作已经完成——适合”持续轮询”“定期检查”这类时间驱动的场景。

Stop hook 是最底层的机制，`/goal` 本质上就是对 Stop hook 的高层封装：它在 session 范围内注册了一个 prompt-based Stop hook，每轮结束后调用 Haiku 评估条件。Stop hook 的灵活性最高，可以执行任意 shell 脚本做确定性检查（比如直接跑测试命令），不局限于语言描述的条件，但需要在设置文件里配置，是跨 session 持久的。`/goal` 的优势在于即时性和便捷性，当下想用就用，session 结束自动消失。

| 方式 | 触发时机 | 停止条件 | 典型场景 |
| --- | --- | --- | --- |
| `/goal` | 上一轮结束后立即 | 模型评估条件满足 | 目标导向的多步任务 |
| `/loop` | 设定的时间间隔 | 手动停止或 Claude 自判断 | 定期检查、轮询 |
| Stop hook | 上一轮结束后立即 | 脚本或 prompt 判断 | 确定性验收、复杂条件 |

## 与 auto 模式的配合

`/goal` 和 auto 模式是互补关系，容易让人以为二者重叠。

auto 模式的作用域是单轮内：它自动批准工具调用，Claude 在一轮内不需要你不断点允许就能执行读文件、写文件、运行命令等操作。但一轮结束，控制权就回到你手里。

`/goal` 的作用域是跨轮次：它在每轮结束后决定要不要再启动一轮，解决的是”我需要不断说继续”的问题。

两者组合使用才是最顺滑的体验：auto 模式处理轮内的工具审批，`/goal` 处理轮间的连续性，整个任务从开始到完成可以完全不需要人工干预。

## 使用限制与注意事项

`/goal` 依赖 Claude Code 的 hooks 系统运行，因此有几个前提条件需要满足：当前工作区必须已经通过了 trust 对话框的确认；如果在设置文件里设置了 `disableAllHooks` 或者管理员启用了 `allowManagedHooksOnly`，`/goal` 命令会明确告知你无法使用，而不是静默失效。

在非交互模式和 Remote Control 下，`/goal` 同样可以工作。通过 `-p` 参数启动时，设定了 goal 的调用会一直运行到条件满足才返回：

```
claude -p "/goal 修复所有 lint 错误并确保 build 成功"
```

用 Ctrl+C 可以中途打断非交互模式下正在运行的 goal。

消耗方面需要留意：每轮结束后都会调用 Haiku 做评估，这部分 token 消耗是额外的。对于条件明确的任务问题不大，但如果条件写得模糊、Claude 一直无法满足，goal 可能会运行很多轮积累不少消耗——写清楚、可验证的条件比含糊的目标更能让 goal 高效停止。

## 最后

`/goal` 在功能设计上抓住了一个关键痛点：长任务里最浪费人类注意力的部分，不是看 Claude 工作，而是在每轮结束后判断”是不是还要继续”然后再发一条指令。把这个判断交给独立的评估模型来做，在设计上是合理的——执行和验收分离，减少了”自我感觉良好就停下”的风险。

从 Codex CLI 率先在 v0.128.0 推出 `/goal` 到 Claude Code 跟进实现，这个命令正在成为 AI 编程工具里的标准能力。对于迁移、重构、批量修复这类需要多轮才能完成的开发任务，`/goal` 配合 auto 模式能让整个过程接近”设定目标，等待完成”的体验，让注意力从”督促 AI 执行”转向”验收 AI 结果”——这个方向是对的。

## Related Posts

* [Claude Code /goal：让 AI 自主持续工作直到达成目标的新命令](/post/2026/05/claude-code-goal-command.html) - 05/13/2026
* [本地快速切换 Claude Code 和 Codex CLI 账号的几种方案](/post/2026/05/switch-claude-code-codex-accounts.html) - 05/12/2026
* [cc-switch：在多个 AI 编码工具之间优雅切换](/post/2026/05/cc-switch.html) - 05/04/2026
* [在 OpenClaw 中配置 Longbridge CLI 与 Skill 打造对话式量化交易工作流](/post/2026/04/openclaw-longbridge-cli-and-skill-setup-guide.html) - 04/07/2026
* [Claude Code Agent Teams 是什么，如何使用](/post/2026/04/claude-code-agent-teams.html) - 04/05/2026
* [Obsidian CLI 来了：从终端操控你的知识库](/post/2026/03/obsidian-cli-introduction.html) - 03/21/2026
* [用 Claude Code 的 Remote Control 和 Channels 从手机和聊天软件操控你的终端](/post/2026/03/claude-code-remote-control-discord-telegram.html) - 03/20/2026
* [Atuin：用数据库替换 Shell 历史，跨设备同步不再是难题](/post/2026/03/atuin-shell-history-sync.html) - 03/18/2026
* [Ghostty 终端配置技巧：从入门到舒适](/post/2026/03/ghostty-terminal-tips-and-tricks.html) - 03/17/2026
* [Clawdbot 深度调研：打造完全属于自己的全平台 AI 助手](/post/2026/01/clawdbot-review.html) - 01/25/2026

---

* [← Previous（前一篇）](/post/2026/05/switch-claude-code-codex-accounts.html "本地快速切换 Claude Code 和 Codex CLI 账号的几种方案")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/05/claude-code-goal-command.html)评论。

* [产品体验 230](/categories.html#产品体验)

* [claude-code 33](/tags.html#claude-code)
* [ai-tools 8](/tags.html#ai-tools)
* [productivity 15](/tags.html#productivity)
* [automation 11](/tags.html#automation)
* [anthropic 13](/tags.html#anthropic)
* [cli 38](/tags.html#cli)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").