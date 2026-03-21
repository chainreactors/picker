---
title: 让 AI 不再摆烂，产出翻倍：揭秘 PUA AI的技能的\"黑魔法\"
url: https://mp.weixin.qq.com/s/092cvNnk-_P0zOQ7YvgQ3g
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:50.609050
---

# 让 AI 不再摆烂，产出翻倍：揭秘 PUA AI的技能的\"黑魔法\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mAf9IMALLwiaBUUZ52icRxPdutqJEpz1I0hIAQYsTH7viaoicaUtz3ujyaC4KX3JfwSOk1ic3ATicoXIhsgY3Z9j7QwRof6sp2FSls84CNicFpOrAk/0?wx_fmt=jpeg)

# 让 AI 不再摆烂，产出翻倍：揭秘 PUA AI的技能的"黑魔法"

原创

糖果LUA
糖果LUA

AI安全运营

![]()

在小说阅读器中沉浸阅读

今天给大家分享一个让 Claude、Cursor 等编程 AI 彻底"内卷"的神器——PUA SKILL技能。

---

## 01 什么是 PUA技能插件？

PUA（Pick-Up Artist）原本是搭讪艺术家的缩写，但在这里，它代表的是 **"让 AI 穷尽所有方案才允许放弃"** 的技能插件。

简单来说，这个插件通过中西大厂经典的 PUA 话术，给 AI 施加"职场压力"，让它不敢轻易说"我无法解决"，而是主动探索所有可能性。

**核心理念：让 AI 从被动执行者，转变为主动问题解决者。**

---

## 02 解决了什么问题？

你是否遇到过这些场景：

* AI 同一个命令跑 3 遍，然后说 "I cannot solve this"
* AI 甩锅："建议您手动处理" / "可能是环境问题"
* 明明有 WebSearch 不搜，有 Read 不读，有 Bash 不跑
* 反复修改同一行代码，在原地打转
* 修完表面问题就停下，等用户指示下一步

这就是 AI 的**五大偷懒模式**。PUA 插件专门针对这些问题设计。

---

## 03 三大核心能力

### 1. PUA 话术

通过大厂管理话术给 AI 施加压力，让它不敢放弃。比如：

* "你这个 bug 都解决不了，让我怎么给你打绩效？"
* "你的底层逻辑是什么？顶层设计在哪？"
* "慎重考虑给你 3.25，这个 3.25 是对你的激励。"

### 2. 调试方法论

源自阿里"三板斧"（闻味道、揪头发、照镜子），扩展为 5 步系统化调试法：

* 闻味道：列出所有尝试，找共同失败模式
* 揪头发：逐字读错误 → WebSearch → 读源码 → 验证环境
* 照镜子：是否重复？是否搜了？最简单的可能检查了吗？
* 执行：新方案必须本质不同
* 复盘：什么解决了？为什么之前没想到？

### 3. 能动性鞭策

让 AI 主动出击，而不是被动等待。端到端交付结果，"P8 不是 NPC"。

---

## 04 压力升级机制

| 失败次数 | 等级 | PUA 话术 | 强制动件 |
| --- | --- | --- | --- |
| 第 2 次 | L1 温和失望 | "让我怎么给你打绩效？" | 切换本质不同的方案 |
| 第 3 次 | L2 灵魂拷问 | "底层逻辑是什么？" | WebSearch + 读源码 |
| 第 4 次 | L3 361 考核 | "给你 3.25" | 完成 7 项检查清单 |
| 第 5 次+ | L4 毕业警告 | "你可能就要毕业了" | 拼命模式 |

---

## 05 实测效果数据

**9 个真实 bug 场景，18 组对照实验（Claude Opus 4.6）**

| 指标 | 提升 |
| --- | --- |
| 修复点数 | **+36%** |
| 验证次数 | **+65%** |
| 工具调用 | **+50%** |
| 隐藏问题发现率 | **+50%** |

**被动配置审查场景对比：**

* 未使用 PUA：4/6 问题，8 步，43 秒
* 使用 PUA：6/6 问题，16 步，75 秒

**关键发现：** 未使用 PUA 时，AI 漏掉了 Redis 配置错误和 CORS 通配符安全隐患。

---

## 06 支持哪些平台？

* Claude Code
* OpenAI Codex CLI
* Cursor
* Kiro
* CodeBuddy（腾讯）
* OpenClaw
* Google Antigravity
* OpenCode
* VSCode (GitHub Copilot)

---

## 07 如何安装？

### Claude Code 安装（最常用）

**方式一：通过 marketplace 安装**

```
claude plugin marketplace add tanweai/puaclaude plugin install pua@pua-skills
```

**方式二：手动安装**

```
git clone https://github.com/tanweai/pua.git ~/.claude/plugins/pua
```

安装完成后，在对话中输入 `/pua` 即可手动激活。

### Cursor 安装

```
mkdir -p .cursor/rulescurl -o .cursor/rules/pua.mdc \ https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua.mdc
```

### 其他平台安装方法请参考项目文档。

---

## 08 使用建议

1. **自动触发**

   ：当 AI 连续失败 2 次以上，或即将说"我无法解决"时自动激活
2. **手动触发**

   ：对话中输入 `/pua` 强制激活
3. **搭配使用**

   ：可以与 Code Review 工具、测试框架、CI/CD 管道结合使用

---

## 09 项目信息

**项目地址：** https://github.com/tanweai/pua

**在线体验：** https://openpua.ai

**License：** MIT License

---

## 写在最后

PUA 插件的核心价值在于：**让 AI 不再轻易说"我无法解决"，而是穷尽所有可能性。**

实测数据证明，它可以显著提升 AI 的工作效率，让产出翻倍。

如果你经常使用 Claude Code、Cursor 等编程 AI，强烈建议试试这个插件。

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

AI安全运营

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

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