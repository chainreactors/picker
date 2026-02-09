---
title: Letting AI Actively Manage Its Own Context
url: https://blog.xlab.app/p/51d26495/
source: 明天的乌云
date: 2026-02-08
fetch_date: 2026-02-09T04:18:24.349428
---

# Letting AI Actively Manage Its Own Context

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. Foreword](#Foreword)
2. [2. Git-like Tree](#Git-like-Tree)
3. [3. Building Context Awareness](#Building-Context-Awareness)
4. [4. Skill](#Skill)
5. [5. Finally](#Finally)
6. [6. Promotions](#Promotions)

![透明人](/images/logo.png)

透明人

Tmr Blog

[200
日志](/archives/)

[33
分类](/categories/)

[159
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# Letting AI Actively Manage Its Own Context

发表于
2026-02-08

分类于

[AI](/categories/AI/)

阅读次数：

本文字数：
4.8k

阅读时长 ≈
4 分钟

It’s time for context management to become Agentic.

## Foreword

Currently, most context management focuses on what should be put in and how to correctly find the right things to put in—such as RAG, MEM, etc. There is little discussion on how to actively clean it up.

Current cleanup mainly relies on reaching a certain threshold of the context window (e.g., 80%), triggering a compression to achieve cleanup. This was probably first introduced by Claude Code and has now become a basic feature. Of course, there is an art to compression itself.

I feel this isn’t proactive enough. It should be more fine-grained. I first saw the `d-mail` feature in [kimi-cli](https://github.com/MoonshotAI/kimi-cli/blob/main/src/kimi_cli/tools/dmail/dmail.md). When the AI discovers it has performed some low-information-density tasks (like reading a large file where only a tiny bit is useful), it calls `d-mail` for “time travel,” letting the agent return to the context before the read and bringing back a message telling its past self: “I read xxx and found xxx.”

Kimi documentation: <https://github.com/MoonshotAI/kimi-cli/blob/main/src/kimi_cli/tools/dmail/dmail.md>
Internal ByteDance doc: <https://bytetech.info/articles/7571069998476165146>
Public research: <https://leslieo2.github.io/posts/agent-control-via-timetravel-checkpoints/>

Later, I saw [pi agent](https://pi.dev/), which has a complete, transparent, and model-agnostic unified context storage ([session](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/session.md)).

> The author wrote a post on the design philosophy, highly recommended: <https://mariozechner.at/posts/2025-11-30-pi-coding-agent/>
> In case you didn’t know, [openclaw](https://openclaw.ai/) was developed using pi.

At the same time, sessions are stored in a tree format, providing tree operation methods like `/fork` and `/tree` for tree replication and navigation. The [/tree](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tree.md) command can optionally include a summary, which is very similar to `d-mail`.

Of course, many agents now have context storage and jumping functions. Context storage and recovery are basically `/resume`. As for jumping, Claude/Codex use a double-press of `Esc`, while OpenCode doesn’t have it but has a `/fork` command, which might be too obscure as it’s not even mentioned in the docs.

But in short, these are all human-facing, not agent-facing. So the solution is simple: find a way to give `/tree` to the AI.

## Git-like Tree

I think the session tree can easily be compared to a Git workflow:

* Every message is a **commit**.
* Jumping is a **checkout**, which can go to any commit.
* The summarization action is more like submitting an \*\*MR (Merge Request)\*\*—instead of bringing all the “garbage” commits, they are merged into a single **mr-commit**.

For example:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` ├─ user: "Develop feature X" │  └─ assistant: "plan..."                     <- 1. base branch │     ├─ user: "Try method A"                  <- 2. git branch-1 from base │     │  └─ assistant: "work..." │     │     └─ [......] │     │        └─ user: "It doesn't work"      <- 3. After many commits, create an MR to merge to base │     └─ sum: "Tried method A..."              <- 4. Don't submit all commits, condense into one mr-commit │        └─ user: "Try method B"               <- 5. Continue development │           └─ assistant: "..." ``` |

The left side is what `pi tree` provides. Also, every message ID in a pi session is an 8-digit hex. So as long as we add the ID before each message in the tree results, the agent can call `tree` with the target ID.

However, after a long conversation, the session tree becomes massive. If the AI looks at the entire tree, the context will explode. So refinement is mandatory.

## Building Context Awareness

Borrowing the concept of `git tag`, we provide a tool for the AI to actively mark task progress, building a more concise context skeleton based on User messages + Tags.

Thus, I designed three tools:

* `context_tag`: `git tag`, marks task progress.
* `context_log`: `git log`, views the context skeleton.
* `context_checkout`: `git checkout`, jumps along the skeleton.

To help the AI better form a “Build-Perceive-Compress” loop:

Beyond just the skeleton, it should also perceive context usage, conversation depth, and distance from the nearest tag, prompting it to tag in a timely manner. I designed a HUD for this.

The final `context_log` looks something like this:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` [Context Dashboard] • Context Usage:    0.9% (8.2k/1.0M) • Segment Size:     4 steps since last tag 'exp-b-start' --------------------------------------------------- | ba87607d [MODEL_CHANGE] | eacb45e0 [SUMMARY] Experiment A failed. Starting Experiment B. | 2366e20a (tag: exp-b-start) [AI] (system action)   :  ... (2 hidden messages) ... * 25dbfe72 (HEAD) [TOOL] (write) Successfully wrote 23 bytes to experiment.js ``` |

## Skill

The plugin also adds a skill to guide the agent on how and when to use these tools, how to tag, how to checkout, and what constitutes a good checkout message.

I won’t go into more detail, you can check it out directly here: <https://github.com/ttttmr/pi-context>

To be honest, I’m not sure how well it works yet, but feel free to try it out.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` npm install -g @mariozechner/pi-coding-agent pi install npm:pi-context ``` |

## Finally

In theory, this could be migrated to other tools as well, since they all have session storage; one just needs to find a way to edit and reload it.

This is about rolling back context. If combined with a rollback-capable file system, being able to optionally roll back files during a checkout would also be very useful.

## Promotions

I’ve developed other pi extensions, check them out:

* <https://github.com/ttttmr/pi-web-search>
  Directly reuses antigravity/gemini-cli/gemini for searching.
* <https://github.com/ttttmr/pi-wakatime>
  As the name suggests, integrates WakaTime.
* <https://github.com/ttttmr/planning-with-files/tree/master/.pi/skills/planning-with-files>
  Ported the plan skill, which has been merged into the main repo.

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[让AI主动管理自己的上下文](/p/6a966aeb/ "让AI主动管理自己的上下文")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2026

透明人

站点总字数：
351k

Theme NexT works best with JavaScript enabled