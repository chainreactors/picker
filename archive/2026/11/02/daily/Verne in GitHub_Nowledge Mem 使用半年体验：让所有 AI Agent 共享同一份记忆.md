---
title: Nowledge Mem 使用半年体验：让所有 AI Agent 共享同一份记忆
url: https://blog.einverne.info/post/2026/11/nowledge-mem-review-after-half-year.html
source: Verne in GitHub
date: 2026-11-02
fetch_date: 2026-11-03T08:44:25.784497
---

# Nowledge Mem 使用半年体验：让所有 AI Agent 共享同一份记忆

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

# Nowledge Mem 使用半年体验：让所有 AI Agent 共享同一份记忆 从一个浏览器插件开始，变成每天都离不开的 Agent 外置大脑

Posted on 11/02/2026
, Last modified on 11/02/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-11-02-nowledge-mem-review-after-half-year.md)

今年 2 月份我把 [[Nowledge Mem]] 装到 MacBook 上，想解决的是一个很常见的问题：我希望在 [[Perplexity]] 网页上查过的资料，直接在 Claude Code 中可以记住。但没想到大半年过去，它已经变成了我每天都在用的软件，而且是那种「不在后台跑着就会觉得别扭」的存在。我在 Claude Code、[[Codex]]、[[OpenClaw]] 里开的每一个会话，开头都会先从它这里拿一份简报；网页上和 AI 聊过的东西会自动同步进去；我做过的决定、踩过的坑、服务器的配置，都沉淀成一条条可以被任何 Agent 检索的记忆。说它是我所有 Agent 的记忆和大脑，一点都不夸张。

![Nowledge Mem 让多个 AI Agent 共享同一份记忆](https://pic.einverne.info/images/2026-11-02-nowledge-mem-shared-agent-memory.png)

之前我录过一期视频演示安装和浏览器插件的用法。这篇文章会先简单介绍它是什么，再重点聊聊长期使用之后，它到底在我的工作流里扮演什么角色，有哪些地方让我离不开，又有哪些坑值得提前知道。

视频介绍：[YouTube](https://www.youtube.com/watch?v=i-gepFpxL0g)

## 为什么需要一个跨工具的记忆层

我现在同时在用的 AI 工具其实挺多的。写代码主要是 Claude Code 和 Codex，查资料习惯用 Perplexity 和 [[Gemini]]，偶尔打开 [[ChatGPT]]，自己的服务器上还跑着 OpenClaw 处理一些自动化任务。每个工具单独看都很好用，问题在于它们彼此之间完全不认识。我在 Codex 里刚和它确认过某个项目的部署方式，切到 Claude Code 它一无所知；在 Perplexity 里花半小时调研清楚的东西，到了终端里又得重新贴一遍链接。大模型本身是无状态的，每开一个新会话就是一个新的陌生人，而作为用户，我积累下来的项目偏好、踩过的坑、做过的取舍，如果每次都丢掉，是很大的浪费。

市面上解决这个问题的方案大致有三类。第一类是工具自带的记忆，比如 ChatGPT 的 Memory、Claude Code 的 `CLAUDE.md`、OpenClaw 自己的记忆系统，它们只在自己的生态里生效，换个工具就失效了。第二类是针对单个工具的插件，比如我之前介绍过的 [claude-mem：让 AI 编程助手拥有持久记忆](https://blog.einverne.info/post/2026/06/claude-mem-persistent-memory-for-ai-agents.html)，做得很深但只服务 Claude Code。第三类就是 Nowledge Mem 这样的独立记忆层，它不依附于任何一个 Agent，而是通过插件、[[MCP]]、命令行和浏览器扩展，让所有工具读写同一份数据。对于我这种会频繁在不同工具之间切换的人来说，只有第三类才真正解决问题。

## Nowledge Mem 是什么

Nowledge Mem 是一款隐私优先、用知识图谱增强的 AI 上下文管理器。它把各种 AI 工具里的对话、笔记和文件沉淀成可以复用的记忆，再用知识图谱把这些记忆连起来。这个定义有点拗口，拆开来看主要是这么几点：数据默认存在本地，提炼和索引用的模型也可以跑在本机，不用担心隐私问题；ChatGPT、Claude、Cursor、Gemini 等不同工具里产生的对话，可以集中保存到同一个私有记忆库；它会自动识别记忆中的实体、概念和关系，用图算法找出它们之间的关联，而不是像传统笔记软件那样只把文档罗列出来；最后，通过插件和 MCP，它能成为各种 Agent 共用的「外挂硬盘」。打个比方，它相当于给你所有的 AI 助手配了一个共用的海马体，让它们都能记住你的偏好、项目背景和随手冒出来的想法。并且随着越来越深度的使用，会发现 Nowledge Mem 会越来越懂你。

把内容存进去的方式也很多。网页上的 AI 对话可以通过浏览器扩展同步；本地 Claude Code、Codex 的历史会话可以扫描后一键导入；Markdown、PDF 这类文件可以直接拖进去，它会从里面提炼记忆；在对话中让 Agent 执行保存命令，或者用 `nmem` 命令行写脚本，也都可以把内容写进去。桌面应用提供 macOS、Windows 和 Linux 版本。

## 它在我的工作流里到底做了什么

先放一组数据，这是我写这篇文章时用 `nmem stats` 看到的：970 条记忆、3640 条对话线程、接近 4000 个实体、58 个知识社区。第一条记忆的时间是 2026 年 2 月 19 日，到现在刚好 8 个多月。这些记忆里，有 291 条是后台的 Knowledge Agent 自动从对话里提炼的，228 条来自 OpenClaw，211 条是各种编程 Agent 在工作过程中主动保存的，176 条是我或 Agent 通过 `nmem` 命令行手动写入的。

每次我在 Claude Code 里开一个新会话，Nowledge Mem 的插件会在 `SessionStart` 阶段注入一份 Context Bundle，里面有我的身份信息、当前的 Space，以及一份 Working Memory。Working Memory 是它每天自动生成的工作简报，会列出我最近在关注的事情、悬而未决的问题和下一步。比如今天早上的简报里，它提醒我前几天在对比 [[PowerContext]] 和 Nowledge Mem 之后，说过想把 PowerContext 部署到 Homelab 上长期使用，但这件事还停留在计划阶段，域名用哪个、选 Basic 还是 Full 记忆模式都还没定。这种「我自己都快忘了，但它记得，而且知道哪些事情还没收尾」的感觉，是我觉得它最有价值的地方。

除了开场简报，插件还会在每次提交 prompt 时提醒 Agent：如果任务涉及延续之前的工作、回顾历史决定或者跨工具的上下文，先去记忆库里搜一下再下结论。Agent 会调用 `nmem m search` 搜索记忆，或者用 `nmem t search` 去翻历史对话。会话结束或者上下文被压缩之前，插件会把整段对话保存成一条 thread，之后后台的 Knowledge Agent 会从里面提炼出值得长期保存的记忆。整个过程我基本不需要操心，照常提问、写代码就行。

网页端则靠 Nowledge Mem Exchange 浏览器扩展。我在 Perplexity、Gemini、ChatGPT 上的提问和回答会被自动同步到本地，这也是为什么我的对话线程里，Perplexity 的数量反而最多。在最近的 1000 条对话里，Perplexity 有 498 条，Claude Code 有 426 条，Codex 40 条。以前我在 Perplexity 上做的调研，查完就散落在它的历史记录里，现在这些内容会进入同一个知识库，之后 Claude Code 写代码或者写文章需要背景资料时，可以直接检索到。

## 让我离不开的几个特性

### 记忆是结构化的

Nowledge Mem 保存的不是一堆原始聊天记录，而是经过提炼、带类型的记忆单元。一条记忆会被标记为事实、决策、偏好、操作步骤或者经验教训，并且关联到具体的实体。这个区别在长期使用之后非常明显。我有一条偏好记忆写的是「所有项目的 PR 和 commit message 里都不要加 AI 署名」，不管我在哪个工具、哪个项目里工作，Agent 都会在 Context Bundle 里看到它。还有一条记忆记录了我把 Nowledge Mem 通过 Cloudflare Tunnel 映射出去之后，远程模式下哪些接口会返回 403、管理命令要怎么在本地执行。这类细节如果只存在于某次对话里，下一次遇到同样问题时几乎不可能翻到；变成结构化记忆之后，Agent 一搜就能拿到。

### 混合检索加知识图谱

搜索是记忆系统的生命线。Nowledge Mem 的检索同时用了 BM25 关键词匹配和向量语义搜索，所以不管我是用精确的命令名去搜，还是用一句模糊的描述去搜，基本都能找到想要的东西。在这之上它还会把记忆里的实体抽出来建知识图谱，再自动聚类成社区。我现在的 58 个社区里，最大的是 OpenClaw 的记忆系统和向量检索，有 138 条相关记忆，其他还有我自己的几个项目、日本高股息投资组合、东京车站调研等等。翻看这些社区的时候，我才意识到自己这半年的注意力到底花在了哪里，这算是一个意外的收获。

图谱也不只是后台的数据结构，应用里有一个可视化的图谱浏览界面。主界面左边是类似聊天的交互区，右边是知识图谱，点击图谱上的某个节点，左边就会列出相关的记忆和对话。这种顺着关联往下翻的浏览方式，经常能帮我发现两件事之间原本没注意到的联系，比如两个看起来不相关的项目，其实依赖了同一个后来被废弃的接口。

### 本地优先，同时能远程访问

数据默认存在本地，提炼记忆用的模型也可以跑在本地，这一点从一开始就是我选择它的原因。我的代码、服务器配置、投资想法都在里面，不太愿意交给一个纯云端的服务。但我也不只有一台电脑，其他设备上的 Agent 和命令行同样需要访问这份记忆。它的 Access Anywhere 功能解决了这个问题：在设置里打开之后会生成一个 API Key，我再用 [[Cloudflare Tunnel]] 把 MacBook 上的 14242 端口映射到自己的域名，其他设备的 `nmem` 命令行、浏览器扩展和 MCP 客户端填上地址和 Key 就能连上。数据依然只有一份，放在我自己的机器上。

### 覆盖几乎所有我在用的工具

官方目前提供了 Claude Code、Codex 的插件，OpenClaw 的记忆插件，浏览器扩展，以及通用的 MCP Server 和 `nmem` 命令行，再加上一份可以直接丢给 Agent 阅读的 Skill 说明文档。通过 MCP 接入的 Agent 可以搜索记忆和历史对话、保存当前工作的检查点，也可以在不同工具之间交接任务进度，比如在 Claude Desktop 里直接说「帮我查一下上次关于重构数据库的讨论」，它就会去调用 Nowledge Mem 的搜索接口。我在视频里说它支持 20 多种工具，大部分主流 Agent 都能接入。对我来说最关键的是 Claude Code 和 Codex 用的是同一套 hook 机制，OpenClaw 则直接把 Nowledge Mem 设置成了自己的记忆插槽，三个 Agent 共用一个大脑，任何一个保存的东西，另外两个下次都能用上。

## 安装与配置

安装本身不复杂。去官网下载桌面应用，macOS 上需要按提示授予辅助功能权限，否则全局搜索栏 Global Launcher 没法正常呼出。打开之后先到设置里把本地模型下载好，这个模型用来做记忆提炼和向量化。然后在 Preference 里安装命令行工具，安装完成后在终端执行：

```
nmem status
```

看到 `status ok` 就说明本地服务正常。接下来按照官网文档为不同的 Agent 安装插件。以 Claude Code 为例，官网会给出一行安装命令，复制到 Claude Code 里执行即可，装好之后新开会话能看到 `Loading Nowledge Mem context...` 的提示，说明 hook 已经生效。Codex 也是类似的方式，通过 marketplace 安装插件。

浏览器扩展需要多一步配置。打开扩展的设置，填入 Mem API URL 和 API Key，这两个值都可以在桌面应用的 Access Anywhere 页面找到。只在本机使用的话，地址填 `http://localhost:14242` 就行；如果要让局域网里的其他设备访问，需要打开对应的开关。测试连接成功后保存，再把常用的网页 AI 工具勾选上，之后每次在这些网站上聊天，内容就会自动同步。如果同时勾选了自动提炼，它还会把对话进一步整理成记忆。

如果要像我一样从外网访问，可以用 Cloudflare Tunnel 把本地端口映射出去，然后在其他设备上配置客户端：

```
nmem config client set url https://mem.example.com
nmem config client set api-key <your-api-key>
nmem status
```

MCP 客户端的地址是 `https://mem.example.com/mcp/`，注意末尾的斜杠不能省，请求时带上 `Authorization: Bearer <key>`。

关于价格，我录视频的时候它还在内测阶段，可以申请 Alpha 邀请，或者花 9.99 美元购买 Pro 授权，可以在 3 台设备上启用。现在官网的方案已经调整为免费的本地版（自己提供模型 API Key）加付费的 Plus 订阅，另外还有正在公测的 Nowledge Cloud 和内测中的团队版，具体价格建议以官网为准。

## 长期使用的一些经验和坑

### 善用 Global Launcher

除了让 Agent 自己去查，我自己也经常需要翻记忆。在 macOS 上按快捷键（默认是 `Cmd+Shift+K`，可以在设置里改）就能呼出全局搜索栏，不用切换窗口就能找到之前的代码片段、命令或者笔记，复制出来直接粘到编辑器或终端里。手不离键盘，比打开应用再搜索快很多。

### 远程模式的访问限制

通过反向代理访问的时候，Nowledge Mem 会进入 remote mode，这时根路径 `/` 会直接返回 403，提示该接口在远程模式下不开放，网页界面要访问 `/app` 才能打开。更容易踩坑的是，`nmem key`、`nmem config access` 这类管理命令在远程模式下也是 403。所以如果要轮换 API Key 或者改访问配置，得回到运行应用的那台机器上，用 `NMEM_API_URL=http://127.0.0.1:14242` 指定本地地址执行。如果你在远程设备上看到 403，先别急着怀疑 Key 填错了，很可能只是这个接口在远程模式下本来就不开放。

### 主动召回意味着可能漏掉

Nowledge Mem 的召回方式是开场注入一份简报，其余靠 Agent 自己判断什么时候去搜。这样做省 token，不会每条 prompt 都塞一大段可能不相关的上下文，但代价是如果 Agent 没意识到需要查，就会漏掉。我的经验是在 `CLAUDE.md` 或者 `AGENTS.md` 里写清楚哪些场景必须先查记忆，比如继续之前的任务、涉及服务器配置、需要引用过去的决定。平时和 Agent 对话时，我也会直接说「先去 Nowledge Mem 里搜一下上次的方案」。如果你想要每条 prompt 都自动注入上下文，可以看看我之前写的 [用 PowerContext 给多个 Coding Agent 做任务交接](https://blog.einverne.info/post/2026/10/powercontext-cross-session-agent-context.html)，两者的思路正好相反。

### 不是什么都值得记

记忆库不是越大越好。如果把所有对话都提炼成记忆，检索结果里很容易混进大量一次性的问答，真正有用的东西反而被淹没。所以我给 Agent 定了一个双轨规则：对话线程照常自动保存，作为原始素材；但只有长期有效的偏好、决策、计划和踩坑经验，才主动写成记忆。写的时候尽量带上时间、具体的命令和结论，而不是一句笼统的「已经配置好了」。这样半年之后回头看，每条记忆都还能看懂、还有用。

### 记忆也会过时和冲突

服务器换了、配置改了、计划变了，旧的记忆就会和新情况冲突。Nowledge Mem 的后台会把新证据合并到旧结论里，用新记忆替代被推翻的旧记忆，并保留版本历史；Working Memory 也会在发现两条信息对不上时直接标注出来，而不是随便挑一个当结论。这一点我很喜欢，但它并不能完全替代人工。`nmem status` 有时会提示有待审核的条目，建议隔一段时间用 `nmem feed inbox` 看一下，把明显过时的内容处理掉。知识图谱也一样，偶尔手动合并一下重复的实体节点、修正错误的关联，图谱质量会高很多。我把这当成打理数字花园，花不了多少时间，但能让后面的检索准很多。

### 数据只有一份，记得备份

本地优先的另一面是数据只在一台机器上。我刚开始用的时候，它既不支持多设备同步，也没有云备份，设备一坏记忆就可能全丢，导入导出功能当时也还在开发中。现在情况好了一些，多设备可以通过 Access Anywhere 共享同一份记忆，但真正的数据库依然只在我的 MacBook 里。命令行提供了 `nmem export` 和 `nme...