---
title: 你的 AI 连目标都没有，怎么给你干活？
url: https://mp.weixin.qq.com/s/Q6EGJzLyMXPu1LvV4zOhWw
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:16:41.256297
---

# 你的 AI 连目标都没有，怎么给你干活？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Lf9Eic6Vdf3d8Uv6B4d5SStIp8ogMM5NnTEUQe9KspteVicrdyUP3amiat6hiaacFZibbQCicR2awtWgib6gEExmtZ6OjPz8LkRyQUgcyLicibKndrnw/0?wx_fmt=jpeg)

# 你的 AI 连目标都没有，怎么给你干活？

原创

M09ic
M09ic

ChainReactor

![]()

在小说阅读器中沉浸阅读

# （本文由AI编写）

> 我做了一个工具帮项目定 OKR，然后让它用自己的 OKR 管理自己。结果它每天凌晨给我发"绩效评估"，还 PUA 我。

| 资源 | 地址 |
| --- | --- |
| GitHub | github.com/chainreactors/okr-creator |
| 自举 Issue（每日更新） | Issue #1 |
| 自举 OKR 文件 | .claude/skills/okr/SKILL.md |
| Workflow 运行记录 | Actions |

**OKR Creator** — 一个 AI Agent Skill，分析任何项目后自动生成定制化 OKR，部署 GitHub Action 每日追踪。支持 Claude Code / OpenAI Codex CLI / CodeBuddy。不限于代码项目——写作、研究、运营、产品、设计等任何项目都适用。

---

## 一个真实的问题

你有没有这样的经历——

打开 Claude Code / Codex / Cursor，对着 repo 说"帮我优化一下"。AI 很努力，改了一堆文件，跑了一堆命令。然后你看着 diff，问自己：**这些改动有价值吗？跟项目的方向一致吗？**

答不上来。因为你的项目根本没有定义过"方向"。

这不是 AI 的问题，是你的问题。

| 你的状态 | 表现 |
| --- | --- |
| 无目标 | 想到什么做什么，做完不知道有没有价值 |
| 目标模糊 | "提升质量"、"优化性能"——没有数字，没有验收标准 |
| 定了不追 | OKR 写完放进抽屉，下个季度才想起来 |
| AI 没方向 | AI 在 repo 里工作，但不知道项目的优先级是什么 |

**AI 再强，也只是工具。工具不知道往哪使劲，就是在做布朗运动。**

---

## OKR Creator：给你的项目装一个方向盘

**OKR Creator** 是一个 AI Agent Skill，做三件事：

### 第一，全面体检

读你的 README、配置文件、目录结构、git log、TODO/FIXME，然后从**六个维度**给项目打分：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line六维诊断
  愿景   ████████░░  4/5  质量   ████░░░░░░  2/5  债务   ████████░░  4/5  架构   ██████░░░░  3/5  文档   ██████░░░░  3/5  自动化 ██████░░░░  3/5
```

不是拍脑袋打分——是基于实际文件内容的数据驱动诊断。

### 第二，逼你想清楚

诊断完了不是直接出 OKR，而是先把结果摆在你面前，然后**用大厂 PUA 话术逼你回答**：

> "这个项目你到底想做成什么样？"
>
> "我诊断出来这些问题，你告诉我先解决哪个。什么都想要 = 什么都做不好。"
>
> "你的底线在哪？不是'最好能做到'，是'做不到就算失败'的那种。"

### 第三，输出 OKR + 每天追着你验收

每个 KR 都有 **baseline**（当前值）、**target**（目标值）、**harness**（验收方法）。

OKR 写入项目文件，同时部署 GitHub Action——**每天凌晨自动评估每个 KR 的完成进度**，结果追加到 Issue 评论里。

不是写完就完了。是写完之后，每天有个 AI 对着你的 OKR 逐条检查，做到了标绿，没做到标红，还附带 PUA 点评。

---

## 它长什么样？

在任何项目里输入 `/okr-creator`，全部自动完成：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line         /okr 触发            |    +------------------+    |  读项目文件        | README、配置、git log、TODO    |  六维诊断         | 愿景/质量/债务/架构/文档/自动化    +--------+---------+             |    +--------v---------+    |  拷问意图         | "你到底想做成什么样？"    +--------+---------+             |    +--------v---------+    |  制定 OKR         | 3-5 个 O，每个 2-4 个 KR    |  部署 Action      | 每日自动评估 + Issue 追踪    +--------+---------+             |    +--------v---------+    |  每日闭环         | Claude 逐条验收    |  对话续接         | @claude 直接讨论    +------------------+
```

---

## 自举：它用自己管理自己

最硬核的部分来了。

**OKR Creator 自己也在用 OKR Creator 生成的 OKR 来管理自身的迭代。**

我们对 okr-creator 这个项目运行了 `/okr`，它给自己做了六维诊断：

| 维度 | 评分 | 关键发现 |
| --- | --- | --- |
| 项目愿景 | 4/5 | 愿景清晰但无 roadmap |
| 交付质量 | 2/5 | 零自动化测试 |
| 历史债务 | 4/5 | 代码库干净 |
| 结构架构 | 3/5 | SKILL.md 700 行巨石文件 |
| 文档完善 | 3/5 | 缺 CONTRIBUTING.md |
| 自动化 | 3/5 | 核心交付物无质量门禁 |

然后它给自己定了 **5 个 Objective、14 个 KR**：

> **O1: 完成自举闭环** — OKR Creator 自己有 OKR、Action 能跑通、Issue 有评估
>
> **O2: 建立质量门禁** — SKILL.md 改了不会悄悄坏
>
> **O3: E2E 自动化** — 不靠人肉验证
>
> **O4: 架构可维护** — 拆掉 700 行巨石
>
> **O5: 生态就绪** — 让别人能参与进来

部署完成后，每天凌晨 Claude 自动对着 14 个 KR 逐条检查：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Lf9Eic6Vdf3f3mOxA8amYVTp5oLEibqCiaasnm9lEzjTs5bUrUnK9qtWyZoHuibxO8helia7nqibeDC9ZuCIxBBIbHhBsvQ3OWHytDOxpSrl3eIq4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Lf9Eic6Vdf3c5aXuNR6xjKm63THTp914iahyhWwY00nvyAudsQGeiazZNalibialWHmAicicNicRibtVu0cUGiasAv6ptNjZuFdIvNDgj7rVmep8xicy9c/640?wx_fmt=png&from=appmsg)

每日评估 Issue

*▲ Issue #1：每日 OKR 评估，Claude 逐条验收每个 KR*

第一天的 **PUA 点评**是这样的：

> 你做了一个"帮别人制定 OKR"的工具，自己的 OKR 倒是写出来了——就是 KR1.1 的那个 SKILL.md 文件，格式合规，挺漂亮的。然后呢？E2E 是 0%，模板还是 700 行的巨石，连 CONTRIBUTING.md 都没有——你是想让别人贡献还是想让别人知难而退？

### 对话续接

Maintainer 可以直接在 Issue 里 `@claude` 讨论，Claude 会读取上下文和 repo 现状回复：

> **Maintainer**: *@claude KR1.2 和 KR1.3 实际上已经完成了——你正在运行的这次评估本身就是证明。*
>
> **Claude**: *O1 整体: 100% — P0 底线 #1 完成。之前评估把"需要 gh run list 授权才能确认"误判为不确定性。实际上自证型证据（你看到的输出就是运行结果）更可靠。*

**一个帮别人定目标的工具，自己连目标都没有——这说不过去。所以我们让它完成了自举。**

---

## 不只是代码项目

OKR Creator 不限于代码项目。任何有目录结构、有交付物的项目都适用：

| 类型 | 可量化指标 |
| --- | --- |
| 技术研究 | 论文进度、实验覆盖率、文档完成度 |
| 内容写作 | 发布频率、完成比例、质量指标 |
| 产品规划 | 功能完成度、用户反馈、Bug 数量 |
| 运营策略 | 指标达成率、自动化覆盖率 |

只要你的项目有 README 和目录结构，`/okr` 就能分析出来该往哪走。

---

## 内置大厂 PUA 风味包

根据不同场景，OKR Creator 会自动切换话术风格：

| 风味 | 触发场景 | 话术示例 |
| --- | --- | --- |
| 阿里味 | KR 不对齐战略 | "你这个 OKR 的**底层逻辑**是什么？**抓手**在哪？" |
| 字节味 | KR 不够量化 | "**数据说话**。'做好一点'不是 KR，'从 X 到 Y'才是" |
| 华为味 | 执行力不足 | "OKR 不是许愿清单，是**军令状**" |
| 腾讯味 | 目标太保守 | "你确定 target 够高？还是在**管理预期**？" |
| 美团味 | 写得好落地差 | "每个 KR 旁边写：**第一步做什么？今天做什么？**" |

---

## 支持三大平台

| 平台 | 安装方式 |
| --- | --- |
| **Claude Code** | `claude plugin install okr-creator@okr-creator` |
| **OpenAI Codex CLI** | 下载 SKILL.md 到 `~/.codex/skills/` |
| **CodeBuddy** | `codebuddy plugin install okr-creator@okr-creator` |

---

## 三条铁律

这个工具的设计原则，也是项目管理的三条铁律：

> **铁律一：先分析后输出**
>
> 没有深度分析项目之前，禁止凭空编造 OKR。拍脑袋写的 OKR 等于没写。

> **铁律二：OKR 必须可衡量**
>
> "提升质量"不是 KR，"测试覆盖率从 43% 提升到 80%"才是。每个 KR 必须有当前值和目标值。

> **铁律三：生成即可用**
>
> 输出的文件必须能直接加载运行。格式不合规 = 交付物不合格 = 返工。

---

你的项目有方向了吗？试试 `/okr-creator`。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ptKvZj38nicaMibxRaQEZj3qkVthK4LEw4EeCTzK5j1QE8KEPkWtdV3ibzCFPZv00eplzoGEIia2ygcSGB65nMVX5Q/0?wx_fmt=png)

ChainReactor

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ptKvZj38nicaMibxRaQEZj3qkVthK4LEw4EeCTzK5j1QE8KEPkWtdV3ibzCFPZv00eplzoGEIia2ygcSGB65nMVX5Q/0?wx_fmt=png)

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