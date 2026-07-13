---
title: Claude Code 指令保姆级教程——新手从零上手
url: https://mp.weixin.qq.com/s/13xdCsyovJtL-oEArgElhQ
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:28:43.851123
---

# Claude Code 指令保姆级教程——新手从零上手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/52TtyVpD62M0QrKrPGF16ljHicoDVITFicZIQHic78B8EZVQIbTskt4FiajWAHfdjComI2Trw6wwicfmyFngjtFD70E9zDkib419SsVt5oiapyJay0/0?wx_fmt=jpeg)

# Claude Code 指令保姆级教程——新手从零上手

天黑说嘿话

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于土豆哥的 AI 实战笔记
，作者鼠标土豆

![](http://wx.qlogo.cn/mmhead/PdibpV1sFDHc4iakRt3Mm7WbJ3gjDDdUwnvPyJjKobJAYTpRW3hAoqobnghRw7MT2tTLZBFKVDngM/0)

**土豆哥的 AI 实战笔记**
.

分享 AI 工具、自动化、独立开发和出海实践。少讲概念，多讲实战，记录普通人如何用 AI 提升效率、验证想法、做出自己的产品。

![cover](https://mmbiz.qpic.cn/sz_mmbiz_png/52TtyVpD62NQ5JguJgxnDAxbicOK49QJE3W5aQEzfIhVCZ73Y5EKBXtmbQENTXad6DfXxicVweCmtPfvweqXDNKRAfkpWGHxFb2HfOjl2lwM8/640?from=appmsg)

> 本文写给刚装好 Claude Code 、打开终端不知道从哪里开始的新手。

---

先说结论：

Claude Code 不是聊天机器人。

它更像一个坐在你项目目录里的 AI 编程同事。

你可以让它读代码、改文件、跑命令、写测试、做 review 。

但你要先学会控制它。

不然它很聪明，也很容易聪明过头。

---

## 一、什么是斜杠指令？

Claude Code 里有两种输入。

一种是普通 prompt ：

```
帮我把这个函数重构一下
```

这是让 Claude 干活。

另一种是斜杠指令，以 `/` 开头：

```
/model /compact /plan
```

这些不是让 AI 写代码的需求。

**这些是你控制 Claude Code 工作方式的按钮**。

一句话区分：

> **prompt 是需求，指令是开关**。

搞清楚这点，后面就不乱了。

---

## 二、先记住 3 个常识

**第一个：忘了指令，直接输入 `/`**

在对话框输入一个 `/`，会弹出当前可用的指令列表。继续输入字母可以过滤。

每个人看到的列表可能不一样，取决于你的版本和配置。以本地弹出的列表为准。

**第二个：指令必须单独输入**

```
/compact 帮我总结一下刚才的改动
```

这样是对的。

```
你能 /compact 一下吗
```

这样 Claude 只会把 `/compact` 当成普通文字读。

**第三个： CLAUDE.md 是写给 Claude 的项目入职手册**

你第一次进项目， Claude 对你的代码库一无所知。 CLAUDE.md 是你提前写好的项目规则， Claude 每次开 session 都会自动读它。

写什么进去？项目技术栈、不能改的目录、提交前要跑什么测试。

一次写好，长期复用。

---

## 三、新手必掌握的 10 条指令

别一上来背一堆。先把这 10 条用熟，你就能完成 90% 的日常开发任务。

### 1. `/init`

第一次进项目时用。

![/init 指令：输入 / 后弹出指令列表，/init 初始化 CLAUDE.md 文件](https://mmbiz.qpic.cn/sz_mmbiz_png/52TtyVpD62NCp27OVJVZ4we4J3Z3ib65wlRQkuIZRaTzJOTfRibVS5fNRr1GZJITBLTr9DTzjykrl1XaqxNcugUL5Hkribd1M2k8Jt1AZ1wpkY/640?from=appmsg)

```
/init
```

Claude 会扫描你的项目结构，生成一份 `CLAUDE.md` 脚手架。

![/init 执行结果： Claude 扫描项目后自动生成 CLAUDE.md ，列出 npm 脚本、 Prisma 命令和发布流程](https://mmbiz.qpic.cn/sz_mmbiz_png/52TtyVpD62NlU1Rb2CAKTYfPtP8xN6qrg7e7CedNdV1uE4hWkEicDqQ7QictywiaLzDWNCKeK7HEdqfbbuD4QSBsGzF3s5C0QN76zd8mCcTQlI/640?from=appmsg)

生成后最好自己补几句：

```
技术栈：Next.js + TypeScript + PostgreSQL 包管理：pnpm（不要用 npm 或 yarn） 不要修改 dist/ 目录 提交前必须跑：pnpm test
```

这几句很值钱。你不用每次都重新教育 Claude 。

### 2. `/cost`

不知道这次对话花了多少 token ？敲它。

![/cost 输出：$50.09 ， 2h 58m API 时间， 5282 行代码增删， Haiku $1.91 + Sonnet $48.18](https://mmbiz.qpic.cn/sz_mmbiz_png/52TtyVpD62Ovs7BmMlY488rXVDgpgk94MEUCmXOJdTl5OlZK8cEKOKRzbkTJpAzQzahFTZ8RUvlRr3nG5CUKWibzxcPKXRyV5MXBwN3xxzgw/640?from=appmsg)

```
/cost
```

它会显示当前 session 的 token 消耗和费用估算。

什么时候用？

•你感觉对话太长，想知道现在有多贵

•想对比 `/compact` 前后的成本差距

•跑完一个大任务，想知道花了多少

新手建议多敲几次，建立一个直觉：什么操作贵，什么操作不贵。

### 3. `/model`

```
/model
```

弹出模型选择器。三档：

| 模型 | 适合 |
| --- | --- |
| **Haiku** | 简单查找、格式整理、文件搜索 |
| **Sonnet** | 日常写代码、功能开发、 code review （最佳平衡） |
| **Opus** | 复杂架构设计、难 bug 、陌生代码库分析 |

一句话原则：**小活别烧钱，大活别省钱**。

Haiku 比 Opus 便宜约 60 倍。大多数任务 Sonnet 就够了。

### 4. `/plan`

大任务不要直接让 Claude 动手。先让它想清楚。

```
/plan 重构用户认证模块，支持 OAuth2
```

Claude 会读相关文件，给出方案，等你确认。

你确认后，输入：

```
/exitplan
```

它才开始写代码。

**越大的任务，越要先 `/plan`**。

对齐一次的成本，比写错了重来便宜得多。

### 5. `/compact`

和 Claude 聊久了，对话越来越长。每条消息 Claude 都要重读全部历史，越聊越慢、越聊越贵。

```
/compact
```

它会把前面的对话压缩成摘要，继续当前任务。

注意：`/compact` 不是清空。它是压缩历史、继续当前话题。

如果要彻底换任务，用 `/clear`。

建议固定的操作习惯：大约每 40 条消息手动跑一次 `/compact`。

### 6. `/clear`

彻底清空当前 session ，从头开始。

```
/clear
```

换新任务时用。上一个任务的所有历史都不会带过来。

区分：

•任务没结束、对话变长 → `/compact`

•任务完成、要换话题 → `/clear`

### 7. `claude --resume`

昨天的任务没做完，今天回来继续。

```
claude --resume
```

或者简写：

```
claude -r
```

它会打开历史 session 列表，选中上次那条，直接接着做，不用重新解释背景。

适合：跨天任务、长时间 debug 、分阶段开发。

### 8. `/review`

Claude 改完代码后，让它切换成 reviewer 视角再检查一遍。

```
/review
```

它会重点看：有没有 bug 、有没有边界条件漏掉、有没有缺测试、有没有安全风险。

推荐在提交代码前固定跑一次。

### 9. `/memory`

Claude Code 有跨 session 的记忆系统。

```
/memory
```

查看和管理 Claude 记住的内容。你可以让它记住你的偏好：

```
记住：我的项目都用 pnpm，不用 npm 记住：写代码不要加注释，除非逻辑真的非常反直觉
```

下次开新 session ，这些偏好依然有效。

### 10. `/doctor`

Claude Code 跑不起来、连接有问题、不知道哪里配错了？

```
/doctor
```

它会检查你的环境配置，列出问题和修复建议。

新手遇到奇怪报错，第一反应就是 `/doctor`。

---

## 四、两个模式： Plan Mode 和 Headless 模式

### Plan Mode （ Shift+Tab 触发）

在对话框按 `Shift+Tab`，进入 Plan Mode 。

这时候 Claude 只会思考和规划，不会直接改你的代码。

适合大任务开始前：让它先读清楚、想清楚，你确认方向对了再放手。

等同于 `/plan`，但快捷键更方便。

### Headless 模式（`claude -p`）

不想开交互 session ，只想问一个问题或跑一个单次任务：

```
claude -p "这个 repo 当前的 release 版本是什么？"
```

比交互模式省约 60% 的 token ，因为没有 session 启动开销。

CI/CD 脚本里特别好用：

```
claude -p "给 staged 的改动写一条 commit message" --model haiku  claude -p "最后一次 commit 有没有明显的 bug？" --model sonnet
```

---

## 五、第一次用 Claude Code ，照着这个流程走

**第一步：进项目目录**

```
cd your-project claude
```

**第二步：初始化项目说明**

```
/init
```

补充几行你的项目规则到生成的 CLAUDE.md 。

**第三步：先让它读项目，不要直接改**

```
读一下这个项目的整体结构，告诉我主要模块是什么
```

**第四步：大任务先计划**

```
/plan 我想做 XX 功能，帮我想一下方案
```

**第五步：确认方案后再让它改**

```
/exitplan 好，按这个方案做
```

**第六步：查看真实改动**

```
/review
```

或者直接看 git diff ：

```
git diff
```

**第七步：提交前审查**

```
/review
```

**别一上来就全自动。先让它读，再让它想，再让它改，最后你验收**。

---

## 六、写好 CLAUDE.md ， Claude 才不会每次都像新员工

`/init` 只是生成脚手架。真正有价值的是你写进去的规则。

一个好用的 CLAUDE.md 示例：

```
## 技术栈 - Next.js 15 + TypeScript - PostgreSQL + Prisma ORM - 包管理：pnpm（不要用 npm 或 yarn）  ## 目录规则 - 不要修改 dist/ 和 .next/ - 新 API 放在 app/api/ 下 - 数据库 schema 改动必须写 migration  ## 提交规则 - 提交前必须跑：pnpm test && pnpm lint - commit message 格式：feat/fix/chore: 简短描述  ## 编码规范 - 不加注释，除非逻辑真的反直觉 - 函数命名用动词开头
```

这东西很重要。

你不要每次都重新告诉 Claude ：我们用 pnpm 、不要改 dist 、提交前要跑测试。

全写进 CLAUDE.md ，一次写好，长期复用。

**这才是把 Claude Code 从聊天工具变成项目同事的关键**。

---

## 七、常见疑问

**Q1 ： Claude Code 会不会乱改我的代码**？

主要取决于三件事：你的 prompt 是否清楚、你有没有先用 `/plan` 对齐、你有没有看改动。

新手不要一上来让它全自动跑。先用 Plan Mode ，确认方案后再动手。

**Q2 ：`/compact` 会不会让 Claude 忘掉重要信息**？

会压缩细节。如果担心关键信息丢失，可以这样写：

```
/compact 重点保留：当前正在修复的 bug 描述和已尝试的方案
```

**Q3 ： CLAUDE.md 越详细越好吗**？

不是。 CLAUDE.md 每次 session 开始都全量加载。写太长，每次开对话都在付这笔账。

原则：只写值得 Claude 每次重读的内容。不超过 200 行。

**Q4 ： Claude Code 和直接用 Claude 网页版有什么区别**？

网页版是远程顾问，你要把代码贴给它。

Claude Code 是坐在你项目目录里的同事，它能直接读文件、改文件、跑命令、看 diff 。

**Q5 ：改完代码我应该做什么**？

固定三步：`/review` → `git diff` 看真实改动 → 跑测试。

不要只看 Claude 的总结，总结会漏， diff 不会。

---

## 八、最后给新手的使用口诀

进项目先 `/init`，让 Claude 认识项目。

大任务先 `/plan`，确认方向再动手。

对话长了跑 `/compact`，别等上下文爆掉。

改完必须看 diff ，`/review` 再提交。

查消耗用 `/cost`，小活用 Haiku ，大活用 Opus 。

跨天回来用 `--resume`，不用重新解释背景。

环境有问题用 `/doctor`，不用自己瞎猜。

记住一句话：**别一上来把方向盘交给 AI**。

让 Claude 坐上副驾，帮你看路、查地图、修车。必要的时候，再让它替你开一段。

你现在用 Claude Code ，最卡在哪里？评论告诉我。

##

关注我，获取 AI 前沿、技术、管理、产品、英语和硅谷生活见闻。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/X0IJicBiaSvwUndPM1oiaUlc9LFiccxcQqRhqic4mIR6vPGOkM5pEVp8wrP7YUwDSYB0a97thV89Axdv6Xehuk9rJKw/0?wx_fmt=png)

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