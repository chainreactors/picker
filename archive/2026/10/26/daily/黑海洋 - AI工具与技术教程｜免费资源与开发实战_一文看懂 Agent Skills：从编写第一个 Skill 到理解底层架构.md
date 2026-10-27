---
title: 一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构
url: https://blog.upx8.com/Agent-Skills-Skill
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-26
fetch_date: 2026-10-27T07:04:45.493554
---

# 一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[开发](https://blog.upx8.com/code)
/
一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构

# 一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构

[开发](https://blog.upx8.com/code)
10-26
·
约 15 分钟
·
黑海洋
·

2,269

![一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构](https://cdn.skyimg.net/up/2026/10/26/268e1d09a5c56b730df3be45700cf16e.webp)

> 想让 AI 帮你自动清理电脑、分析股票或者发日报？你需要给它编写一个 Skill（技能）。本文从零开始，手把手教你写一个标准的 Skill，再深入聊聊 Skills 的底层逻辑——它到底是什么、怎么跑起来的、以及为什么有些模型跑不好它。

---

## 一、写一个 Skill 并不难：它本质上就是"配置文件 + 一段代码"

每个 Skill 的入口文件（通常叫 `SKILL.md`），由"身份证"（YAML）和"躯干"（文件结构）组成。下面分三步走：写好 YAML、摆好目录、写对代码。

### 1. YAML 头部元数据（Frontmatter）

文件最开头必须有一段被三根短横线 `---` 包裹的内容，这叫 YAML Frontmatter。通俗地说，这就是给 AI 看的身份证——AI 通过它来知道这个技能叫什么、能干什么。

一个标准的"身份证"长这样：

```
---
name: system-cleaner
description: "清理电脑里的垃圾文件，释放C盘空间"
tags: ["清理", "系统", "优化"]
version: 1.0.0
---
```

每个字段的含义：

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | String | 是 | 技能 ID。建议使用 kebab-case（小写短横线），如 `git-helper` |
| description | String | 是 | 核心 Prompt。智能体依靠这句话来理解技能用途，建议包含具体动词（如"清理"、"生成"） |
| tags | Array | 是 | 关键词列表，用于模糊匹配和分类检索 |
| version | String | 否 | 版本号，遵循语义化版本（Major.Minor.Patch） |

### 2. 文件夹怎么放？推荐"三抽屉"结构

写代码最怕乱。就像把衣服、裤子、袜子分开放进不同抽屉，找起来才快：

```
my-skill/                  # 你的技能总文件夹
├── SKILL.md               # [身份证] YAML 就放这里
├── scripts/               # [工具箱] 所有代码脚本放这里
│   ├── main.ps1           # 比如 PowerShell 脚本
│   └── utils.py           # 比如 Python 脚本
├── config/                # [设置] 配置文件放这里
│   └── settings.json      # 比如让用户设置"清理哪个盘"
└── data/                  # [仓库] 存放运行结果
    └── logs/              # 日志生成在这里
```

### 3. 代码实战：编写 "Hello World" Skill

光有配置是不够的，Skill 的灵魂在于代码。**Skill 的本质是命令行工具（CLI）**——智能体通过命令行调用你的脚本，并读取打印的输出。

脚本代码 `scripts/main.py`：

```
import argparse
import sys

# 1. 设置参数解析（让脚本能听懂 AI 的指令）
# AI 会以 `python main.py --name "LO"` 的方式调用
parser = argparse.ArgumentParser(description="Greeter Skill")
parser.add_argument("--name", type=str, required=True, help="要问候的名字")

# 2. 解析参数
args = parser.parse_args()

# 3. 执行逻辑（这里可以写任何业务逻辑）
greeting = f"👋 你好，{args.name}！Skill 运行成功！"

# 4. 输出结果（这是 AI 唯一能看到的东西！）
# 必须使用 print 输出，AI 会捕获 stdout 作为执行结果
print(greeting)
```

**进阶技巧：健壮性与反馈**

AI 看不到报错弹窗。如果出错，必须打印错误信息并以非 0 状态码退出：

```
try:
    # 业务逻辑...
except Exception as e:
    print(f"❌ 发生错误: {str(e)}")
    sys.exit(1)  # 告诉 AI 任务失败
```

如果用了第三方库，请在根目录创建 `requirements.txt`。

### 4. 核心连接：配置与交互

**读取外部配置**——不要把参数写死在代码里：

```
import json
import os

# 动态找到 config 文件夹（不管用户把 Skill 放在哪）
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "..", "config", "settings.json")

# 读取配置
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

print(f"✅ 读取到配置: {config}")
```

**与用户对话**——有时候需要问用户"确定吗？"：

```
# 1. 打印问题（AI 会展示给用户）
print("❓ 确认执行操作吗？(y/n)")

# 2. 等待输入（脚本会暂停）
user_input = input().strip().lower()

if user_input == 'y':
    print("🚀 以此执行...")
else:
    print("🛑 操作取消")
```

### 5. 新手避坑指南（千万别踩这些雷！）

YAML 看起来简单，但脾气很怪。很多新手写代码一次过，却在 YAML 上卡半天。

* **它是"空格控"，严禁使用 Tab 键！** YAML 依靠缩进分层级。正确做法：老老实实按空格键，一般 2 下或 4 下。
* **冒号后面必须有空格。** ❌ `name:my-skill` ／ ✅ `name: my-skill`。
* **路径别写死（No Absolute Paths）。** 不要写 `D:\我的项目\scripts` 这种绝对路径，别人的电脑可能只有 C 盘。建议使用相对路径。
* **幂等性（Idempotency）。** 脚本应支持重复运行，比如创建文件夹前先检查它是否已存在。
* **自测（Self-Test）。** 提交给 AI 之前，先自己在终端跑一遍：`python scripts/main.py --name "Test"`，确保没有报错。

**总结：写 Skill 其实就三句话**

1. 写好 YAML 身份证，注意冒号后要空格；
2. 把代码和配置分开放，保持目录整洁；
3. 代码里多打印进度提示，方便 AI 理解。

---

## 二、Skills 的底层逻辑：从提示词到架构模式

学会怎么写了，我们再往深看一层：Skills 的本质到底是什么？

> 学不会？没事，学中干，干中学。没必要非要知道原理，只要会用即可！

### 1. 什么是 Skills？

**Skills 的本质：Agent 时代的通用架构模式。**

Skills 不属于任何模型，不属于 MCP，也不属于任何一家科技巨头。它是 Agentic AI（智能体 AI）发展过程中诞生的一种**通用设计模式（Design Pattern）**。

抛开所有无用的内容，Skills 的核心逻辑可以用一个永恒的公式概括：

> **Skills = System Prompt（系统提示词） + Trigger（自动触发器） + Executable（可执行文件）**

### 2. 手动模式 vs 自动模式

当你想要 AI 帮你审查代码时，你通常会输入："你现在是一个资深 Python 架构师，精通设计模式和性能优化。请帮我审查这段代码……"

在这个瞬间，你输入的对话，其实就是在**手动执行一个 Skill**——你通过手动输入，给 AI 设定了角色（Role）和上下文（Context）。

所谓的 Skills，就是把这个过程"代码化"或"自动化"了：

* 用户将这段"资深 Python 架构师"的设定（Prompt）封装成一个独立的模块；
* 系统告诉模型："如果用户问代码问题，你就自动加载这个模块，不需要用户每次都手敲。"

### 3. 为什么系统提示词（System Prompt）也能调用 Skills？

模型是怎么知道你有这些 Skills 的？这就涉及 System Prompt 的隐形机制。

在对话开始之前，IDE 已经在后台偷偷做了一件事：**它把所有可用 Skills 的名字和描述，写进了发给模型的第一条系统提示词里。**

这就像考试前老师给学生塞了一张小纸条：

> "考试须知：如果你遇到不懂的代码题，你可以申请查阅'Python 架构师手册'（即调用 skill: python-architect）。"

正因为系统提示词里预埋了这些指令，模型才能在遇到问题时理直气壮地"调用" Skills。所以，System Prompt 不仅是 Skills 的载体，更是 Skills 的"目录"和"导航"。

### 4. 进阶：Skill 包的解剖学（Scripts & Assets）

很多高级 Skill（比如 ui-ux-pro-max-skill）不仅仅是一个 Markdown 文件，而是一个文件夹：

```
my-complex-skill/
├── SKILL.md        # 大脑：提示词和指令
├── scripts/        # 手脚：Python/Node.js 脚本
│   ├── audit.py
│   └── generate.js
└── assets/         # 素材：图片、模板
    └── logo.png
```

当 AI 决定调用这个 Skill 时，它不仅会读取 SKILL.md，还会获得执行 `scripts/` 下脚本的权限。比如，AI 可能会运行 `python scripts/audit.py` 来扫描你的代码，而不是自己瞎猜。

### 5. 环境悖论：没有 Node 环境会怎样？

这是一个非常现实的问题："如果我在 Skills 中设定了调用 Node.js 脚本，但我电脑上没有安装 Node，Skills 会自动下载吗？"

**答案是：通常不会。** Skills 是运行在你本地环境（Local Environment）中的。

* Skill 就像一张游戏光盘；
* 你的电脑就像游戏机；
* Node/Python 环境就像操作系统。

如果你买了游戏光盘（下载了 Skill），但没买游戏机（没装 Node），游戏是跑不起来的。Agent 尝试运行 `node script.js` 时，会直接收到系统报错：`command not found: node`。

虽然现在的 Agent 很聪明，可能会检测到报错并建议你安装，但它通常不敢（也不应该）擅自帮你下载安装这种系统级的 Runtime，因为这涉及巨大的安全风险和兼容性问题。

**怎么保证 Skills 能"下载" Node 环境？**

这里有一个专业术语：**Runtime Bootstrapping（运行时引导）**。你不应该简单地说"下载 Node"，而应该在 Skill 的定义中加入一段"自愈式（Self-Healing）"的指令。

专业的话术建议：

> **"Prerequisite Check & Environment Setup"（前置检查与环境搭建）**
> "在执行任何脚本之前，请先运行 `node -v` 验证运行时环境。如果环境缺失，请不要直接报错，而是根据用户的操作系统（Windows/macOS/Linux），生成对应的安装命令（如 `winget install` 或 `brew install`），并引导用户完成安装。"

这样做，你的 Skill 就从一个"会报错的脚本"，变成了一个"会照顾用户的智能体"。这也是为什么 ui-ux-pro-max-skill 会有那么多人使用——因为作者在 Skill 中照顾到了所有群体：没有环境，那就下环境。

### 6. 核心辨析：Skills vs MCP vs RAG

在 Agent 的架构中，很多人容易混淆这三个概念。其实它们构成了智能体的"能力铁三角"：

| 概念 | 本质 | 人体比喻 | 作用 |
| --- | --- | --- | --- |
| RAG | 数据（Data） | 记忆/书本 | 告诉 AI 它不知道的事实（如公司规章、私有文档） |
| MCP | 接口（I/O） | 手和脚 | 让 AI 连接外部世界（如读取数据库、操作 GitHub、发送 Slack） |
| Skills | 方法论（Behavior） | 大脑皮层 | 教 AI 处理问题的专业思维（如代码审计流程、苏格拉底教学法） |

一句话总结它们的关系：

> 一个强大的 Agent，会用 Skills（专业思维）去指挥 MCP（手脚），并参考 RAG（记忆）来完成任务。**Skills 往往是那个指挥官**——它定义了流程，而 MCP 是它调用的工具。

### 7. 痛点：为什么有些模型（如 GLM-4.7）跑 Skills 效果不好？

这其实是目前 Agent 开发中最大的坑：**Skills 对模型是有门槛的。**

你可能会发现，同样的 Skill，在 Gemini 3 Flash 上跑得行云流水，但在 GLM-4.7 或 DeepSeek 上却经常"卡壳"或"乱答"。原因主要有三点：

**A. Function Calling（工具调用）的微调差异**

Skills 的触发依赖于模型输出极其精准的 JSON 格式指令。

* Claude/Gemini：经过了海量的 Tool Use 专项微调，它们知道什么时候该"闭嘴去调工具"；
* 普通模型：往往有"抢答"的毛病。它们看到了 Skill 的描述，却选择直接用自己的通用知识去回答用户，而不是去调用 Skills。

**B. System Prompt 的权重问题**

Skills 的指令通常写在 System Prompt 里。有些模型在训练时过分强调了 User Prompt（用户输入）的权重，导致它忽略了 System Prompt 里的设定。

结果就是：你明明加载了"资深架构师"的 Skill，它却还是像个"普通客服"一样回答你。这也是为什么在国内模型中需要设定很严格的提示词规则。

**C. 复杂推理链（Reasoning Chain）的断裂**

执行一个 Skill 往往需要多步操作（思考 → 选工具 → 看结果 → 再思考）。很多模型在第一步之后就"累"了，或者丢失了上下文，导致 Skill 执行到一半就中断了。

**结论：** Skills 是一种高级玩法，它需要 Agentic Model（代理级模型）的支持，而不仅仅是 Chat Model（聊天模型），并且上下文够长才能支持得更好。

### 8. Skills 是如何跑起来的？

这个模式的成功，依赖于现代 LLM（大语言模型）进化出的两个通用素质：

**A. Tool Use / Intent Recognition（意图识别能力）——这是 Skills 的开关**

模型必须具备一种元能力：不仅仅是"回答问题"，而是能"判断该用什么方法回答问题"。当模型意识到"用户的问题超出了我的通用知识，我需要激活 python-architect 这个专业模块"时，Skill 就被触发了。

**B. Long Context / In-Context Learning（上下文学习能力）——这是 Skills 的容器**

当 Skill 被激活时，系统会瞬间将几千字甚至上万字的专业指令（即那个封装好的 Prompt）注入到对话流中。模型必须有足够大的容量来接纳这些新规则，并立即改变自己的行为模式。

### 9. 最后的最后

Skills 是 Prompt Engineering（提示词工程）走向 Software Engineering（软件工...