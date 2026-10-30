---
title: Aside AI 浏览器介绍：既能自己干活，也能接入 Agent
url: https://blog.einverne.info/post/2026/10/aside-ai-browser.html
source: Verne in GitHub
date: 2026-10-29
fetch_date: 2026-10-30T07:54:14.161399
---

# Aside AI 浏览器介绍：既能自己干活，也能接入 Agent

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

# Aside AI 浏览器介绍：既能自己干活，也能接入 Agent 把 Agent 装进你每天在用的浏览器里，再给它配一个看不到密码的保险箱

Posted on 10/29/2026
, Last modified on 10/29/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-10-29-aside-ai-browser.md)

前两天整理了一篇 [AI 浏览器自动化方案怎么选](https://blog.einverne.info/post/2026/10/ai-browser-automation-landscape.html)，把 Playwright、MCP、Agent 专用浏览器、WebMCP 这些路线梳理了一遍。在那篇文章里我提到，「内置 Agent 的 AI 浏览器」这一类里我最看好的是 [Aside](https://myaltbox.com/BDOqQbPjJlW-aside)，原因是它的密码管理器设计得很用心，但篇幅有限没有展开。今天就单独写一篇，聊聊这个浏览器到底能做什么、和 [[Comet]]、[[Dia Browser]] 有什么不一样，以及我现在是怎么用它的。如果你看完想试试，可以用我的邀请链接 <https://aside.com/r/UpYKnv9ziq> 注册，注册后会额外获得 100 Credits。

![Aside 浏览器：在已登录的网站里替你干活的 AI Agent](https://pic.einverne.info/images/2026-10-29-14-05-00-aside-ai-browser.png)

## Aside 是什么

Aside 是一款基于 [[Chromium]] 的 AI 浏览器，官方口号是 “Anything you do in browser, Aside can do for you”。背后的公司 Aside Computer Inc. 是 Y Combinator 2025 年秋季批次（YC F25）的项目，团队只有 8 个人左右，三位联合创始人都来自韩国的移动归因公司 Airbridge。有意思的是，他们最早做的是给 B2B 销售用的实时通话助手，后来才转向浏览器。产品在 2026 年 6 月下旬正式发布，9 月推出 Windows 版，10 月的版本内核已经升级到 Chromium 154，并支持 Windows ARM64，迭代速度非常快，几乎每周都有新版本。

Aside 在自己的宣言里有一个判断我很认同：AI 的操作系统其实已经存在了，就是浏览器。工资、银行、报税、设计、项目管理，现在绝大多数工作都发生在网页应用里，「现代软件大多只是一个标签页」。既然工作都在浏览器里，那承载工作的浏览器理所当然应该能帮你把活干完。这个思路和很多 Agent 产品不太一样，后者通常要你一个个接第三方集成，或者在云端开一个干干净净、没有任何登录态的浏览器，Agent 每做一步都要问你要账号、要背景、要授权。

Aside 的做法是把 Agent 直接放到浏览器里，复用你已有的 Cookie、登录状态和浏览历史。用官方的话说，就是把你的账号当作工具，把浏览历史当作记忆。你能在浏览器里登录的网站，理论上 Agent 都能替你操作，不需要任何额外配置。

## 和其他 AI 浏览器有什么不同

过去一年我陆续用过 [Dia](https://blog.einverne.info/post/2025/08/dia-browser.html) 和 [Comet](https://blog.einverne.info/post/2025/09/comet-browser.html)，再往前还写过 [Arc 的初体验](https://blog.einverne.info/post/2022/09/arc-browser-first-impression.html)。Dia 更像是把 AI 对话做进了浏览器，擅长围绕当前页面聊天和辅助写作；Comet 以 Perplexity 的 AI 搜索为核心，问答体验很好，但长流程的自主任务一直不是它的强项。OpenAI 的 [[ChatGPT Atlas]] 更是在 2026 年 8 月就停止了服务，能力并回了 ChatGPT 桌面应用。

Aside 的重心明显不在「聊天」，而在「任务」。一个任务可以跨多个网站，持续几分钟甚至几个小时，中途可以暂停等你输入、请求审批，然后继续。官方给的示例几乎全是那种「登录之后才能做」的杂事：从 Rippling 下载工资单、收集各个平台的账单发票、从合同里提取日期、把仪表盘上的内容整理成待办。这些恰好是传统 RPA 脚本写起来麻烦、而通用聊天机器人又碰不到的工作。

另外还有一个非常值得一提的是 Aside 专门为 Agent 设计了一款密码管理器 — Aside Vault，Agent 可以利用认证但又不会暴露密码，另外 Aside 可以直接阅读的 Markdown 记忆，还给开发者准备了 CLI 和 [[MCP]] 服务。

## Aside Vault 让 Agent 能登录但看不到密码

让 AI 替你操作已登录的网站，最大的心理障碍其实是安全：我愿意让它帮我下载发票，但我不愿意把密码交给一个大模型。Aside Vault 的思路是把「登录这个动作」和「知道密码」拆开。任务走到登录页时，Aside 先检查目标 URL 是否匹配、访问策略是否允许，满足条件就由浏览器直接把凭据自动填进网页，整个过程模型拿不到明文密码。

围绕这个核心，Vault 还做了一整套配套机制。解锁可以用 macOS 的 Touch ID 或 Windows Hello，加密依赖 Secure Enclave 这类硬件能力。Agent 的访问策略分为 Always allow、While unlocked、Never 三档，导入的条目还可以单独覆盖全局策略，比如银行账号直接设成 Never。无痕会话里 Agent 完全不能使用密码库。每一次凭据使用都会记录审计日志，支付、发帖、发消息这类敏感操作会停下来等你确认。遇到 MFA、验证码或身份验证，Aside 也不会去尝试绕过，而是交给人来完成。

我之前的整理文章中对比过，着是目前为止我能看到的最用心的安全设计，尽可能隔离 Agent 和密码，Aside Vault 是我看到的最棒的使用设计。

## 本地记忆和 Routines

Aside 会根据浏览历史、聊天和任务记录生成记忆，这样每次交代任务时不用重复解释背景。和很多产品把记忆藏在云端黑盒里不同，Aside 的记忆就是本地的一堆 Markdown 文件，又继承了 OpenClaw 的精髓。在 Mac 上，位于 `~/.aside/u/0/memory/` 目录下，根目录有 `MEMORY.md`（通用的操作规则）、`USER.md`（用户画像和偏好）和一个 `TAXONOMY.md`。这个 TAXONOMY 文件很有意思，它定义了记忆的分类和归档规则：语义记忆按「当前状态加历史」的结构存放，情景记忆按日期追加写入 `episodic/` 目录，根目录的两个文件则由它们提炼而来，并且要求足够小，方便每次加载进提示词。任务结束后，一个叫 Dreaming 的后台过程会负责整理和更新这些文件。

这种透明度我很喜欢，用 [[Obsidian]] 打开就能看到 AI 记住了你什么，不放心还可以在设置里关掉记忆，或者给情景记忆设置 30 天、90 天的保留期。需要说明的是，我刚装上不久，目前这几个文件里还只有模板，没有积累出什么内容，记忆的实际效果还需要用一段时间再评价。

Routines 则是定时任务，比如「每天早上 9 点生成一份简报」「每周一检查某个后台的数据」。它可以手动创建，Aside 也会扫描你的重复性工作，主动给出 Routine 草稿让你确认。免费版最多 3 个活跃的 Routine，Pro 不限数量。

## 给编程 Agent 用的浏览器

作为一个整天使用 [[Claude Code]] 的人，Aside 可以直接被 Agent 使用。它附带一个 CLI，安装后可以直接添加 CLI，也可以通过如下的方式安装：

```
curl -fsSL https://releases.aside.com/install.sh | bash
```

装好之后可以直接在终端里给 Aside 的 Agent 派任务：

```
aside "Open localhost:3000 and run a smoke test"
aside --account u1 "Check unread Slack notifications"
aside session steer <id> "Switch to Google Flights"
```

如果需要精确控制页面、截图或读取 DOM，可以用 `aside repl` 运行 [[Playwright]] 风格的 JavaScript。更方便的是 `aside skills install`，它会把一个 aside-browser Skill 装进 Claude Code、[[Codex]]、Cursor、OpenCode 这些编程工具里。我现在的 Claude Code 里就有这个 Skill，它的内容很克制，只是让 Agent 先执行 `aside guide` 去读取最新的使用说明，CLI 升级后说明也会跟着更新，不会出现 Skill 文档过时的问题。如果你更习惯 MCP，配置一行就能接入：

```
{"mcpServers":{"aside":{"command":"aside","args":["mcp"]}}}
```

除了浏览器操作，CLI 还内置了一批站点 Skill，执行 `aside skills list` 能看到 Gmail、Google Docs、Google Sheets、Notion、Slack、LinkedIn、YouTube 等，部分读取操作甚至不需要打开浏览器标签页。另外 `aside memory search` 可以让外部 Agent 直接检索 Aside 的记忆，不用再反复问你背景。这样一来，Aside 就不只是一个浏览器，而是一个「带着你的登录态和个人上下文」的浏览器后端，任何编程 Agent 都可以调用它，思路上和我之前介绍的 [[Ego Lite]] 有点接近，只是 Aside 自己也带了一个能独立干活的 Agent。

## 模型和价格

Aside 支持三种模型来源。第一种是订阅附带的 Aside 自有模型，按 Credits 计费；第二种是用 OAuth 登录你已有的 [[ChatGPT]] Plus/Pro、[[Claude]] Pro/Max 或 [[GitHub Copilot]] 订阅；第三种是填入 Anthropic、OpenAI、[[OpenRouter]]、xAI 等服务商的 API Key。后两种方式的费用由对应服务商计算，不消耗 Aside 的 Credits，所以如果你已经有 ChatGPT 或 Claude 的订阅，免费版基本就够日常使用了。

| 计划 | 价格 | 主要内容 |
| --- | --- | --- |
| Free | $0 | 每月 500 Credits，最多 3 个 Routine，Aside Vault，个性化记忆，可接入自己的订阅 |
| Pro | $20/月 | 3 倍于免费版的用量，Ultrabrowse 深度研究，不限 Routine，远程控制，云端接力 |
| Max | $200/月 | 40 倍于免费版的用量，抢先体验计划 |
| Enterprise | 联系销售 | 团队共享 Profile 和 Vault，从内部工具或 Cron 触发 Agent |

按年付费可以打 8 折。通过 [我的邀请链接](https://aside.com/r/UpYKnv9ziq) 注册会额外获得 100 Credits，对于先试水的用户来说，加上每月 500 的免费额度，足够跑一批真实任务看看效果了。

关于性能，Aside 宣称在 Online-Mind2Web、BU-Bench-V1、Odysseys 三个浏览器 Agent 基准上排名第一，Online-Mind2Web 上的成绩是 99.0%（300 个任务完成 297 个），并且把测试结果公开在了 GitHub 上。不过这些都是自测自评，评分也由大模型自动判定，主要成绩还是用 gpt-5.5 跑出来的，参考一下就好，最可靠的办法还是拿自己的任务去试。

## 使用建议和需要注意的地方

首次启动时，Aside 会让你从现有浏览器导入历史、Cookie 和书签。我的建议是不要一股脑全部导入，尤其不要把主力浏览器的 Profile 原样搬过去。Aside 支持多 Profile，可以单独建一个工作用的 Profile，只导入任务真正需要的那几个网站，银行和主邮箱这种高价值账号暂时不要放进去，或者在 Vault 里把它们的 Agent 访问策略设成 Never。

任务权限也值得时间设置一下。Aside 的任务有 Read only、Guard、Full access 三档，Guard 是默认值，只能在批准的文件夹里工作，访问其他目录前会询问。新任务我建议先用只读跑一遍，确认 Agent 理解对了再放开。写任务描述时尽量说清楚「哪个网站、哪个账号、要什么结果、放到哪里、哪些事不要做」。尽量避免模糊的指令。

还有几个使用注意事项。首先，「本地优先」指的是数据存储，模型推理依然调用云端大模型，任务所需的页面内容还是会作为上下文发给模型服务商，切记敏感的内容一定做安全保护。其次，Aside 产品很新，不免偶尔有 BUG，尤其是有人反馈过和 [[1Password]] 的集成会出问题，Vault 在保存新生成的密码时也不够稳定。最后，目前不支持 Linux 和移动端，macOS 需要 15.0 以上。至于让 Agent 带着真实登录态长时间自主运行，本身就存在提示注入和误操作的风险，涉及付款、对外发消息的操作一定要保留人工确认这一步。

## 最后

在我看来，Aside 是 2026 年这一波 AI 浏览器里思路最清晰的一个。它没有满足于在侧边栏放一个聊天框，而是认真回答了「如何让 Agent 安全地使用你的登录态」这个问题：Vault 把登录和密码拆开，记忆以 Markdown 的形式留在本地，权限和审批机制层层叠加，再加上 CLI 和 MCP，让它既能给普通用户当日常浏览器，又能给 Claude Code 这样的编程 Agent 当浏览器后端。

我目前的用法是把它当作编程 Agent 的「手」，让 Claude Code 通过 aside-browser Skill 去处理那些需要登录的网页步骤，获取网页内容，日常浏览还没有完全切过去。Aside 还很年轻，稳定性和基准测试的可信度都需要时间验证。如果你也经常在浏览器里做重复、需要登录的杂事，或者想给自己的 Agent 找一个带登录态的浏览器，不妨[试试](https://aside.com/r/UpYKnv9ziq)。

## 相关链接

* [Aside 官网](https://aside.com/)
* [Aside 在 MyAltBox 上的介绍](https://myaltbox.com/BDOqQbPjJlW-aside)
* [Aside 的替代品](https://myaltbox.com/BDOqQbPjJlW-aside/alternatives)
* [CLI、MCP 与 REPL 文档](https://docs.aside.com/help/developers)
* [Aside 宣言](https://aside.com/manifesto)
* [基准测试仓库 at-inc/aside-benchmarks](https://github.com/at-inc/aside-benchmarks)

## Related Posts

* [呆呆面板 MCP 配置教程：让 Claude、Cursor 用自然语言管理定时任务](/post/2026/10/daidai-panel-mcp.html) - 10/19/2026
* [Executor：多 Agents 和外部世界之间的统一代理层](/post/2026/09/executor-integration-layer-for-ai-agents.html) - 09/07/2026
* [Claude Code 环境变量完全指南：解锁隐藏特性与效率配置](/post/2026/07/claude-code-environment-variables-guide.html) - 07/23/2026
* [Headroom：让 AI Agent 少花冤枉钱的上下文压缩工具](/post/2026/06/headroom-ai-context-compression-tool.html) - 06/26/2026
* [Claude Code 的 Dynamic Workflows 让模型自己写编排脚本](/post/2026/06/claude-code-dynamic-workflows.html) - 06/08/2026
* [CC Switch：在多个 AI 编码工具之间优雅切换](/post/2026/05/cc-switch.html) - 05/04/2026
* [AI C...