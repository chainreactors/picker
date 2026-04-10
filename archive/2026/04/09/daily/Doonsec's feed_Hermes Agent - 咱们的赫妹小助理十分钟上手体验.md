---
title: Hermes Agent - 咱们的赫妹小助理十分钟上手体验
url: https://mp.weixin.qq.com/s/brxTyYDWMgwaUul-YKYB4A
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:43:24.680082
---

# Hermes Agent - 咱们的赫妹小助理十分钟上手体验

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BowImrBK4tL6Gfib1ncFyJia25vsicWaq23z7JWCgr0jeysSSNdEkArTPlCmcnO7Epdp79icSTZPdicnbChOGFIZxhzOhibONCvw6YVg0p6pVpYd8/0?wx_fmt=jpeg)

# Hermes Agent - 咱们的赫妹小助理十分钟上手体验

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器中沉浸阅读

> 最近一款说是超越 openclaw 的工具应运而生，上次咱们也分析了两者的不同，下面咱们重点演示下

## 安装

其他不多说了，直接上安装方法：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

一条命令即可，安装完成后执行

```
hermes claw migrate
```

即可一键完成 openclaw 配置的迁移，你在 openclaw 中的配置信息都会迁移到 hermes 配置下面，**并且还会把你的 openclaw 配置清除掉，这个实在是，两者仅留之一啊！**

## 使用

使用起来就比较方便了，和 openclaw 有些类似，不同的是他还没有那么完美的生态，还是需要人工配置飞书接入啥的，和 openclaw 的配置一样，若是你的 openclaw 配置过飞书，配置在迁移的时候直接就过来了，当然你的飞书机器人就会连接的是赫妹，不是龙虾了

首先先了解对话对斜杠命令，这个输入`/commands`即可查看，对于龙虾使用比较熟悉的应该不会陌生，有一些命令是相似的，有一些有些区别，用的最多的`/new`等是一样的

主要的有一下这些：

`/new`-- Start a new session (fresh session ID + history) (alias: `/reset`)

`/retry`-- Retry the last message (resend to agent)

`/undo`-- Remove the last user/assistant exchange

`/title [name]`-- Set a title for the current session

`/branch [name]`-- Branch the current session (explore a different path) (alias: `/fork`)

`/compress`-- Manually compress conversation context

`/btw <question>`-- Ephemeral side question using session context (no tools, not persisted)

`/queue <prompt>`-- Queue a prompt for the next turn (doesn't interrupt) (alias: `/q`)

`/status`-- Show session info

`/model [model] [--global]`-- Switch model for this session

`/provider`-- Show available providers and current provider

`/personality [name]`-- Set a predefined personality

## 使用体验

最近把我的龙虾上自动写文章的技能迁移到了赫妹上，我就是一句话，读取文件夹下面的文件，它做了自动识别，并且知道我这个文件夹就是为了自己写文章素材用的，自动帮我创建了一个技能，而且把我的龙虾的脾气和性格全带过来了，我仅仅是一句话而已。

**可以这么说，做到了无感切换**

### 基础配置

它的配置没有 openclaw 的复杂，所有的配置信息写入`.env` 文件下面即可，包括你用到的 APIkey、openrouterkey、githubtoken 等等直接，不像 openclaw.json 那么复杂，就是 key=value 形式 ![[Pasted image 20260409182016.png]]

### 记忆系统

Hermes 会自动记忆：你的偏好（比如喜欢简洁回答还是详细解释）、项目结构和环境信息、过去解决过的问题。

对比 openclaw，需要每次提醒它要记忆，要全局记忆还是今天记忆。

**你可以主动告诉它要记住什么：**

`记住：我工作区在 ～/.hermes/workspace，喜欢用 bun 而不是 npm`

它会把这条信息存在长期记忆里，下次对话自动用。

### 技能系统

这个是最核心的，它会**自动**把重复任务做成技能，不用你主动提醒做成技能包。

## 总结

Hermes Agent 最大的魅力在于**它真的在学习**。刚开始可能觉得和别的 AI Agent 差不多，但用得越久，它越懂你，效率越高。

如果你：

* 想要一个真正能「长大」的 AI 助手
* 需要一个能全天候在线的私人助理
* 对 AI Agent 自进化技术感兴趣

那非常值得花点时间搭起来玩玩看。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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