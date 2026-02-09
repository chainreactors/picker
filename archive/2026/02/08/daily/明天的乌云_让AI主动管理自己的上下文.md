---
title: 让AI主动管理自己的上下文
url: https://blog.xlab.app/p/6a966aeb/
source: 明天的乌云
date: 2026-02-08
fetch_date: 2026-02-09T04:18:24.505445
---

# 让AI主动管理自己的上下文

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

1. [1. 前言](#%E5%89%8D%E8%A8%80)
2. [2. git-like tree](#git-like-tree)
3. [3. 构建上下文感知](#%E6%9E%84%E5%BB%BA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%84%9F%E7%9F%A5)
4. [4. Skill](#Skill)
5. [5. 最后](#%E6%9C%80%E5%90%8E)
6. [6. 广告](#%E5%B9%BF%E5%91%8A)

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

# 让AI主动管理自己的上下文

发表于
2026-02-08

分类于

[AI](/categories/AI/)

阅读次数：

本文字数：
2.8k

阅读时长 ≈
3 分钟

是时候让上下文管理也Agentic起来了

## 前言

目前来说大部分的上下文管理都是关注里面应该放什么，怎么正确的找到合适的东西放进去，比如RAG，MEM之类的，少有如何清理的讨论

目前的清理主要是靠达到上下文窗口的某个阈值，比如80%，触发一次压缩，从而实现清理，最早可能还是claude code引入的，如今已经成为基本功能，当然压缩有压缩的学问

我觉得不够主动，应该更加细粒度，最早应该是在kimi-cli上看到的d-mail功能，当ai发现做了一些低信息密度的事情时，比如读了一个大文件，其实有用的只有一点点，此时调用d-mail进行时间回溯，让agent回到之前读之前的上下文，并带一条消息，告诉之前的自己，读了xxx发现了xxx

kimi文档 <https://github.com/MoonshotAI/kimi-cli/blob/main/src/kimi_cli/tools/dmail/dmail.md>
字节内网文档 <https://bytetech.info/articles/7571069998476165146>
公开研究资料 <https://leslieo2.github.io/posts/agent-control-via-timetravel-checkpoints/>

再之后看到了[pi agent](https://pi.dev/)，有完整、透明、且模型无关的统一上下文存储（[session](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/session.md)）

> 作者这篇写了设计思路，推荐一读 <https://mariozechner.at/posts/2025-11-30-pi-coding-agent/>
> 以防你不知道，[openclaw](https://openclaw.ai/)就是用pi开发的

同时session以树的形式存储，并提供了树操作方法，提供`/fork`和`/tree`，实现了树的复制和跳转，其中[/tree](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tree.md)命令可选带上一个summary，这一点就和d-mail很像了

当然目前很多agent都有上下文存储和跳转功能，上下文存储和恢复基本都是`/resume`，至于跳转，claude/codex都是按两下esc，opencode则没有，但是有`/fork`命令，可能过于冷门了，文档上甚至都没有介绍fork命令

但总之这都是面向人类的，不是面向agent的，那么很简单，想办法把`/tree`交给ai

## git-like tree

我觉得session tree很容易类比为git workflow

* 每条消息都是一个commit
* 跳转就是checkout，可以跳到任意一个commit
* 总结的动作更像是提交mr，不带上全部垃圾commit，而是合并为一个mr-commit

举个例子

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` ├─ user: "开发一个X功能" │  └─ assistant: "plan..."                     <- 1. base分支 │     ├─ user: "尝试用A方法开发"                 <- 2. 在base分支新建分支git branch-1 │     │  └─ assistant: "work..." │     │     └─ [......] │     │        └─ user: "不太行"                <- 3. 产生了一堆commit后，此时创建一个mr合并到base │     └─ sum: "尝试了A方法..."                   <- 4. 不以全部commit提交，而是精简为一个mr-commit │        └─ user: "尝试用B方法开发"               <- 5. 继续开发 │           └─ assistant: "..." ``` |

左边的就是pi tree提供的结果，同时pi session中每条message id也是8位hex，那么只要在tree的结果中，把每个消息前把ID加上，agent带着目标ID调一下tree就可以了

但是在产生了一堆对话之后，session tree会非常巨大，AI看一眼tree上下文就炸了，所以必定要做精简

## 构建上下文感知

借用`git tag`的概念，提供一个工具让AI主动的标记任务进度，基于用户消息+Tag构建更加精简的上下文骨架

于是设计了3个工具

`context_tag`：`git tag`，标记任务进度
`context_log`：`git log`，查看上下文骨架
`context_checkout`：`git checkout`，在骨架上跳转

为了能让AI更好的形成“构建-感知-压缩“循环

出了上下文骨架之外，还应该感知上下文占用情况、对话深度，离最近的tag有多远，提醒打即使打tag，前置设计了一个HUD

最终的`context_log`大概是这样

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` [Context Dashboard] • Context Usage:    0.9% (8.2k/1.0M) • Segment Size:     4 steps since last tag 'exp-b-start' --------------------------------------------------- | ba87607d [MODEL_CHANGE] | eacb45e0 [SUMMARY] Experiment A failed. Starting Experiment B. | 2366e20a (tag: exp-b-start) [AI] (system action)   :  ... (2 hidden messages) ... * 25dbfe72 (HEAD) [TOOL] (write) Successfully wrote 23 bytes to experiment.js ``` |

## Skill

插件还补充了一个skill，指导agent如何使用，何时使用，怎么打tag，怎么checkout，什么是好的checkout message

不多介绍了，都放在这里可以直接看 <https://github.com/ttttmr/pi-context>

说实话，我也不知道效果好不好，欢迎试用

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` npm install -g @mariozechner/pi-coding-agent pi install npm:pi-context ``` |

## 最后

理论上也可以迁移到其他的工具上，毕竟都有session存储，想办法编辑和重载即可

这是回滚上下文，如果结合可回滚的文件系统，在checkout时能可选回滚文件应该也很有用

## 广告

我开发了其他的pi扩展，欢迎使用

* <https://github.com/ttttmr/pi-web-search>
  直接复用antigravity/gemini-cli/gemini做搜索
* <https://github.com/ttttmr/pi-wakatime>
  不多说，接入wakatime
* <https://github.com/ttttmr/planning-with-files/tree/master/.pi/skills/planning-with-files>
  移植了plan skill，已经合入主仓库

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[时间过得既快又慢](/p/606eb4ce/ "时间过得既快又慢")

[Letting AI Actively Manage Its Own Context](/p/51d26495/ "Letting AI Actively Manage Its Own Context")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2026

透明人

站点总字数：
351k

Theme NexT works best with JavaScript enabled