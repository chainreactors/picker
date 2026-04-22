---
title: 4个超强项目，让你的Claude Code直接封神！百万上下文时代效率翻倍
url: https://mp.weixin.qq.com/s/2585nN8b6Nqsnyfuzr6Y5g
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:40:32.927010
---

# 4个超强项目，让你的Claude Code直接封神！百万上下文时代效率翻倍

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJibE6C9CkqBelMiaO3FcLY6jAVz8ORCBIqr37ptnhT9DhQ5lfPr6EwmvTfp1D0yZMkPoWhEkugVvhvsQC0GxxZGLhSHiaU8MTdU4/0?wx_fmt=jpeg)

# 4个超强项目，让你的Claude Code直接封神！百万上下文时代效率翻倍

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年，AI编程已进入百万上下文时代。只懂用Claude Code远远不够，把它配到极致，才是拉开差距的关键。

今天给大家整理GitHub上4个封神级Claude Code生态项目，每一个都能让你的开发效率直接升一个段位。

一、Everything Claude Code｜Anthropic黑客松冠军全家桶

这是全网最顶流的Claude增强套件，Anthropic黑客松冠军出品，Star超140K，堪称完整的Claude Code操作系统。

核心能力拉满：

- 48个生产级Agent

- 183个全能Skill，覆盖开发、营销、创作

- 79条命令，全流程覆盖

- 六大指南：Token优化、内存持久化、持续学习、验证循环、并行化、子代理编排

全平台兼容：Claude Code、Cursor、Codex、OpenCode、Gemini通用。

一句话评价：只收藏一个就选它，新手到大神全程适配。

**安装也很简单，两步搞定：**

```
# 第一步：添加市场并安装插件
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code

# 第二步：安装规则（必需）
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code
npm install
./install.sh --profile full
```

二、CLAUDE.md｜关键词驱动工作流引擎

来自C++ GUI框架GacUI，思路堪称教科书：用第一个词决定AI行为。

它的核心思想是：**用第一个单词决定 Claude 的行为模式**

```
你输入的第一个词 → Claude 自动加载对应的 prompt 文件 → 按流程执行
```

看看这套关键词体系：

| 关键词 | 对应行为 | 场景 |
| --- | --- | --- |
| `scrum` | 加载敏捷开发流程 | 项目管理、sprint 规划 |
| `design` | 加载设计模式 | 架构设计、接口设计 |
| `plan` | 加载规划流程 | 任务拆解、排期 |
| `execute` | 加载执行流程 | 写代码、实现功能 |
| `verify` | 加载验证流程 | 测试、代码审查 |
| `investigate` | 加载调查流程 | 排查问题、分析日志 |
| `code` | 直接写代码 | 默认模式 |
| `kb` | 知识库查询 | 查文档、找参考 |

输入关键词 → 自动加载对应Prompt → 按流程执行：

- scrum：敏捷项目管理

- design：架构与接口设计

- plan：任务拆解排期

- execute：编码实现

- verify：测试与审查

- investigate：问题排查

- code：直接写代码

- kb：知识库查询

支持组合指令与语音输入纠错，复杂流程一键路由。

三、Waza｜工程师极简肌肉记忆技能包

地址：https://github.com/tw93/waza

国内知名开发者Tw93出品，Waza意为“练成本能的招式”，主打少即是多。

这个名字起得就很有味道——作者 Tw93（国内知名前端开发者）想表达的是：**好的工程师习惯应该像肌肉记忆一样自然**

![图片](https://mmbiz.qpic.cn/mmbiz_png/wibWVO7K9ltZvcT5PKul7YmU5qj47X05HWXJZ6TOEPQcibPSeEx4POKT2jIC8CthicvvoajYGEJfCMwCv6sp7PNvicMfj7I9p2j7YQyRbNnBUYM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0)

Waza 提供 8 个精心打磨的 Skill，每一个都对应一个工程师的核心习惯：

| Skill | 触发场景 | 干什么 |
| --- | --- | --- |
| `/think` | 动手写代码之前 | 挑战问题本身，压力测试设计，先验证架构 |
| `/design` | 做前端界面 | 产出有风格的 UI，拒绝千篇一律的默认样式 |
| `/check` | 完成任务、合并之前 | 审查 diff，自动修复安全问题，标记危险命令 |
| `/hunt` | 遇到 bug | 系统性 debug，先确认根因再动手修 |
| `/write` | 写文档/文案 | 重写文字，让中英文都自然流畅 |
| `/learn` | 进入陌生领域 | 六阶段研究流程：收集→消化→大纲→填充→打磨→自审 |
| `/read` | 读任何 URL 或 PDF | 智能路由：GitHub、PDF、微信、飞书都有特殊处理 |
| `/health` | 审计 Claude Code 配置 | 检查 CLAUDE.md、规则、技能、钩子、MCP，按严重级别报告问题 |

它还附带两个实用工具：

**状态栏**——一行命令搞定 Claude Code 的资源监控：

```
curl -sL https://raw.githubusercontent.com/tw93/Waza/main/scripts/setup-statusline.sh | bash
```

8个核心Skill，覆盖工程师关键习惯：

- /think：先验证架构再写码

- /design：拒绝千篇一律AI审美

- /check：合并前自动审查Diff

- /hunt：先找根因再修Bug

- /write：文案自然化润色

- /learn：六阶段研究流程

- /read：智能解析URL/PDF

- /health：配置安全审计

安装也极简：

```
# Claude Code
npx skills add tw93/Waza -a claude-code -g -y

# Codex
npx skills add tw93/Waza -a codex -g -y
```

自带资源状态栏与英语纠错教练，安装极简，克制产生复利。

![](https://mmbiz.qpic.cn/mmbiz_png/TVljsu2eAicJkibTE9qr3z0icSIdYcK71V2l9PaGY05pbYQ32cOiaQ8PfJicG7JVVOLXA0Rmw0EekGic96oNyd2LbpucJuuS8qhZPU8NzaUe1gQq8/640?wx_fmt=png&from=appmsg)

四、Ars Contexta｜给Agent装一个“第二大脑”

地址：https://github.com/agenticnotetaking/arscontexta

专治AI“会话失忆症”，让Claude Code拥有持久记忆。

**运行 `/arscontexta:setup` 后，你会得到：**

* **一个知识库**：纯 Markdown + Wiki Link 构成的知识图谱，无数据库，无云端，无锁定
* **处理管道**：自动提取洞察、发现关联、更新旧笔记
* **自动化钩子**：写入时校验结构、自动 git commit、会话状态保存
* **导航系统**：多层级的 Maps of Content（MOC）
* **模板系统**：带 `_schema` 校验的笔记模板
* **用户手册**：7 页针对你领域的专属文档

Setup 流程是 6 个阶段的对话：

| 阶段 | 做什么 |
| --- | --- |
| 检测 | 检测 Claude Code 环境和能力 |
| 理解 | 2-4 轮对话，描述你的工作领域 |
| 推导 | 将信号映射到 8 个配置维度 |
| 提案 | 展示将要生成的内容和原因 |
| 生成 | 生成所有文件：上下文、模板、技能、钩子、手册 |
| 验证 | 检查 15 个核心原语，运行管道冒烟测试 |

整套系统基于**三空间架构**：

| 空间 | 用途 | 增长速度 |
| --- | --- | --- |
| `self/` | Agent 持久心智——身份、方法论、目标 | 慢（几十个文件） |
| `notes/` | 知识图谱——系统存在的意义 | 稳定（每周 10-50 个） |
| `ops/` | 运营协调——队列状态、会话 | 波动 |

最硬核的是它背后有 **249 条互联的研究论断**（methodology/），涵盖 Zettelkasten、Cornell 笔记法、Evergreen Notes、PARA、GTD、认知科学、网络理论等。每一个配置决策都有学术依据，你可以直接问它为什么这么做。

安装方式：

```
# 添加市场
/plugin marketplace add agenticnotetaking/arscontexta

# 安装
/plugin install arscontexta@agenticnotetaking

# 重启 Claude Code 后运行
/arscontexta:setup
```

运行setup即可获得：

- 纯Markdown知识图谱，无数据库不锁数据

- 自动提取洞察、更新笔记

- 三空间架构：self/notes/ops

- 基于249条学术研究支撑

适合知识工作者与PKM爱好者，让AI真正“记住你”。

快速选型指南

- 一步到位全能党 → Everything Claude Code

- 复杂流程团队 → CLAUDE.md关键词路由

- 极简工程师 → Waza技能包

- 知识管理重度用户 → Ars Contexta

先用Waza入门，再上Everything全面武装，最后搭配Ars Contexta做记忆持久化，这套组合足以让你在AI编程时代遥遥领先。

![](https://mmbiz.qpic.cn/mmbiz_png/TVljsu2eAicLGwq0Bv4vZyGOR8Wb6Ql5SwgmZYsrPTy8u0C0JbwSa8UNzjOySXUVxruWUogAoqSurLBVwwwPIrSjw9DwdJLFzOiaAnfrR7pGA/640?wx_fmt=png&from=appmsg)

网友总结

看完这4个神器，你的Claude Code才算真正用对。

参考：

```
https://mp.weixin.qq.com/s/mxkNxjQ7YjuKhHhVOODOFQhttps://mp.weixin.qq.com/s/-BuLSPZbxUwjSevjAYrXsghttps://mp.weixin.qq.com/s/mW84aJ48kQ0JT18LHtjCvA
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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