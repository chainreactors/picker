---
title: Claude Code 快速上手核心指南
url: https://mp.weixin.qq.com/s/XoTZAtiYNakVNrcHJm9bqQ
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:24.492042
---

# Claude Code 快速上手核心指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7G0tsQw684gtBXDjOpzXoOAUzaUIouOlzPY0tOWe8FZSeJibIEoEGtbhQkHn8GtQsjviaAJzicbus3EjmFJ1KhicsIgiapHp7L5G38495ebuZ6vE/0?wx_fmt=jpeg)

# Claude Code 快速上手核心指南

荒野之木
荒野之木

哈拉少安全小队

![]()

在小说阅读器中沉浸阅读

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/7G0tsQw684hnaqcZiaClxRsLWD6UVqZeo9HUeG9oWtjG8z3ZibxqkkMGywf8ln0OLZ89R3HwJJk4CvuzyWmXQTgxia3s91Fo2GGWgGlicuH3ppQ/640?wx_fmt=png&from=appmsg)

Claude Code 是 Anthropic 官方出品的 AI 原生编码工具,它将大型语言模型的能力直接集成到终端中,让你可以用自然语言与 AI 协作完成编程任务。

不同于传统的代码补全工具,Claude Code 能够理解整个项目的上下文,执行复杂的开发任务——从代码生成到重构、从调试到文档编写,它都能胜任。

---

## 一、快速安装

Claude Code 基于 Node.js 构建,安装前请确保系统已安装 **Node.js 18 或更高版本**。

### 为什么需要 Claude Code

传统开发流程中,开发者需要在编辑器、终端、浏览器和文档之间频繁切换。Claude Code 将这些工作流整合到一个统一的界面中:你可以在同一个终端窗口里编写代码、运行测试、查看文档。

更重要的是,它能理解你的项目结构,记住你的编码习惯,真正成为你的编程助手。

### 安装方式

**方式一:手动安装**

```
```
# 全局安装 Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 验证安装是否成功
claude --version
```
```

> 💡 如果遇到权限问题,可以尝试在命令前加 `sudo`(macOS/Linux)或以管理员身份运行终端(Windows)。

**方式二:让 AI Agent 帮你安装**

如果你已经在使用其他 AI 编程助手(如 Cursor、Windsurf),可以让它们帮你完成安装:

```
```
帮我装 anthropic 的 claude code
```
```

AI Agent 会自动:

1. 检查当前 Node.js 版本
2. 如果不符合要求,提示你升级
3. 执行安装命令
4. 验证安装结果

### 首次启动

```
```
# 进入项目目录
cd /path/to/your/project

# 启动 Claude Code
claude
```
```

首次启动时,Claude Code 会引导你完成:

1. 登录 Anthropic 账户
2. 选择使用计划:免费计划 / Pro 计划 / API Key
3. 同意使用条款
4. 可选:配置 API 密钥

---

## 二、快速开始

安装完成后,建议先做几个小实验来熟悉 Claude Code 的工作方式。

### 实验 1:对话 —— 感受 AI 的理解能力

```
```
你是谁,能做什么?
```
```

```
```
JavaScript 和 TypeScript 有什么区别?
```
```

> 💡 注意 Claude 的回答风格——它通常会先给出核心结论,再展开细节。这种「倒金字塔」式的回答方式非常适合快速获取信息。

### 实验 2:生成 Markdown 文档

```
```
帮我写一份 Git 常用命令的 Markdown 文档
要求:包含命令、说明、示例
```
```

Claude 会:

1. 分析你的需求
2. 规划文档结构
3. 生成内容并格式化输出

**预期输出示例:**

```
```
# Git 常用命令速查表

## 初始化仓库

| 命令 | 说明 | 示例 |
|------|------|------|
| `git init` | 初始化新仓库 | `git init my-project` |
| `git clone` | 克隆远程仓库 | `git clone https://github.com/user/repo.git` |
```
```

### 实验 3:编写并运行游戏

```
```
用 Python 写一个贪吃蛇游戏
要求:
1. 使用 pygame 库
2. 有分数显示
3. 按 ESC 退出
写完后帮我运行它
```
```

Claude 会执行:

1. 检查环境:Python、pygame 是否安装
2. 编写代码:创建游戏文件
3. 运行游戏:启动游戏窗口
4. 后续支持:修复 bug、添加功能

**常见问题:**

| 问题 | 解决方案 |
| --- | --- |
| 没有安装 pygame | Claude 会提示你运行 `pip install pygame` |
| 游戏运行后终端被占用 | 按 ESC 退出游戏 |
| 想换其他语言 | 试试「用 JavaScript 写」、「用 HTML5 Canvas 写」 |

---

## 三、核心技巧

掌握这些技巧,能让你的 Claude Code 使用效率提升数倍。

### 快捷键操作

| 操作 | 快捷键 | 说明 |
| --- | --- | --- |
| 清除输入 | `Esc` | 清除当前正在输入的内容 |
| 回退对话 | `Esc``Esc` | 撤销上一轮对话 |
| 清空历史 | `Esc``Esc``Esc` | 重新开始 |
| 取消操作 | `Ctrl+C` | 停止正在执行的操作 |
| 退出程序 | `Ctrl+C``Ctrl+C` | 完全退出 Claude Code |
| 切换模式 | `Shift+Tab` | 循环切换三种工作模式 |
| 打开编辑器 | `Ctrl+G` | 打开 VS Code 编辑长文本 |
| 后台任务 | `Ctrl+B` | 将任务放入后台运行 |
| 查看上下文 | `Ctrl+O` | 查看压缩后的上下文 |

> ⚠️ **重要**:双击 Esc 回退的是**对话状态**,不是代码修改。如果 Claude 已经修改了文件,需要手动用 `git checkout` 恢复。

### 三种工作模式

![image](https://mmbiz.qpic.cn/mmbiz_png/7G0tsQw684ia51CzURsviaIVU7e5SvYM0jctd8fMxqjzH10hhIu7XXkBscCrwFnroviaJnNxz7FQ3hS06nW8AgoiakI8ttv1ylRLiblLouTPSUmM/640?wx_fmt=png&from=appmsg)

Claude Code 设计了三种工作模式,针对不同的使用场景:

| 模式 | 特征 | 适用场景 | 状态指示 |
| --- | --- | --- | --- |
| **默认模式** | 每次操作前询问 | 需要严格把控代码变更 | `? For shortcuts` |
| **自动模式** | 自动创建和修改文件 | 快速原型开发、已建立信任 | `Accept edits on` |
| **规划模式** | 只聊天不执行文件操作 | 架构重构、重大决策讨论 | `Plan mode` |

**模式切换技巧:**

* 项目初期快速原型:使用自动模式最大化效率
* 项目稳定期精细控制:切换到默认模式
* 面对重大架构决策:先在规划模式充分讨论,确定方案后再执行

### 符号系统

![image](https://mmbiz.qpic.cn/mmbiz_png/7G0tsQw684hPqXBfQTMgodwibIlufV7WfGqxIWA5q0Ip0HumiaHW8etKZTvdIb9uEWI6fk0jkbicndHTPgQLHibsC40oCWCSrPkhrojAcNdWickY/640?wx_fmt=png&from=appmsg)

| 符号 | 用途 | 示例 |
| --- | --- | --- |
| `/` | Slash 命令 | `/help` , `/plan`, `/commit` |
| `@` | 引用文件/目录 | `@src/app.tsx` |
| `!` | 执行终端命令 | `!npm test` |
| `&` | 后台运行 | `&npm run dev` |

### @ 引用文件

显式地引用文件能让 AI 更准确地理解你的意图。

**基本用法:**

```
```
# 与其模糊地说
解释 src/utils.ts 这个文件

# 不如直接引用
@src/utils.ts 解释这个文件
```
```

**高级用法:**

```
```
# 引用目录
@src/components/ 总结一下这个目录下的所有组件

# 引用特定行
@src/utils.ts:45-60 解释这段代码的作用

# 引用多个文件
@src/api/users.ts @src/types/user.ts 分析用户模块的架构
```
```

**使用技巧:**

* Tab 补全:输入 @ 后按 Tab 键显示文件列表
* 相对路径:支持 @./config.json 或 @../shared/types.ts
* 模糊匹配:输入 @utils 会匹配 src/utils.ts

### ! 执行命令

Claude Code 内置了终端命令执行能力,无需离开当前环境。

```
```
!npm test           # 运行测试
!git status         # 查看 Git 状态
!ls -la             # 列出文件
!open index.html    # 在浏览器中打开文件
```
```

**实际场景:**

```
```
# 运行测试并分析失败原因
!npm test
分析一下测试失败的原因,并修复代码

# 查看 Git 差异
!git diff
总结一下这些变更的主要内容

# 组合使用
!npm run dev          # 启动开发服务器
等待几秒让服务器启动...
!open http://localhost:3000  # 在浏览器中打开
```
```

> ⚠️ Claude Code 会询问是否执行某些敏感命令(如 `rm -rf`、`sudo` 等),请谨慎确认。

### 常用 Slash 命令

| 命令 | 功能 | 使用场景 |
| --- | --- | --- |
| `/help` | 显示所有命令 | 忘记命令时 |
| `/init` | 生成 CLAUDE.md | 新项目 |
| `/plan` | 规划模式 | 复杂任务 |
| `/clear` | 清除对话 | 重新开始 |
| `/compact` | 压缩上下文 | 节省 Token |
| `/commit` | Git 提交 | 快速提交 |
| `/review` | 审查变更 | 提交前检查 |
| `/context` | 查看上下文 | 优化消耗 |
| `/cost` | 查看费用 | 关注成本 |
| `/model` | 切换模型 | 选择模型 |
| `/status` | 查看状态 | 确认配置 |
| `/mcp` | MCP 工具管理 | 查看已安装的 MCP |
| `/hooks` | Hook 配置 | 自动化工作流 |
| `/tasks` | 后台任务管理 | 查看后台任务 |
| `/rewind` | 版本回滚 | 回退到历史状态 |
| `/memory` | 编辑 CLAUDE.md | 快速更新配置 |

**/plan 先规划后编码**

对于复杂的开发任务,`/plan` 命令让 Claude 进入规划模式。

```
```
/plan
我想添加用户认证功能,请帮我制定实施计划
```
```

Claude 会:分析需求 → 评估现状 → 制定计划 → 与你讨论确认

**/init 自动生成配置**

```
```
/init
```
```

Claude 会执行:扫描项目结构 → 分析配置文件 → 检查代码风格 → 生成 CLAUDE.md

**/commit 自动提交**

```
```
/commit
```
```

Claude 会:查看变更 → 分析内容 → 生成提交信息 → 执行提交

**/rewind 版本回滚**

```
```
/rewind
```
```

回滚选项:

* 回滚代码和对话
* 仅回滚对话
* 仅回滚代码
* 放弃回滚

> ⚠️ **限制**:只能回滚由 Claude Code 写入的文件,无法回滚终端命令生成的文件(如 `mkdir`、`npm install`)

---

## 四、核心配置

### 配置文件位置与优先级

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/7G0tsQw684h4icK0EHm0YGTGXibQoPUcwWqa857QfggTDib6CfYwgO0E8ZPfFG7B1OCjbdkLsmNpv0BEvzianPLuaNyMTWvF2DwUYlgRbpQG94A/640?wx_fmt=png&from=appmsg)

> 优先级从高到低：本地 > 项目 > 全局。高优先级覆盖低优先级,不冲突的配置项合并生效。

| 位置 | 作用域 | 是否提交 Git |
| --- | --- | --- |
| `.claude/settings.local.json` | 项目本地(个人) | ❌ 否 |
| `.claude/settings.json` | 项目共享(团队) | ✅ 是 |
| `~/.claude/settings.json` | 全局 | ❌ 否 |

**配置合并规则:** 高优先级覆盖低优先级,不冲突的配置项合并生效。

### CLAUDE.md - 项目记忆

`CLAUDE.md` 是 Claude Code 最重要的配置文件,相当于项目的「说明书」。

**最小可用模板:**

```
```
# [项目名称]

## 技术栈
- 框架:React 18 + TypeScript
- 状态管理:Zustand
- 样式:Tailwind CSS

## 常用命令
npm run dev      # 启动开发服务器
npm run test     # 运行测试
npm run build    # 生产构建

## 代码规范
- 组件使用函数组件 + Hooks
- 文件命名:PascalCase(组件)、camelCase(工具函数)
- Git 提交使用 Conventional Commits 规范
```
```

**迭代演进策略:**

1. 项目初期:包含基本信息和技术栈
2. 开发中期:添加常用指令、测试流程
3. 稳定期:补充 PR 编写规范、UI 设计准则
4. 持续优化:当 AI 犯错后,要求它更新 CLAUDE.md 避免重蹈覆辙

> 💡 **技巧**:保持文件精简(约 2.5K tokens),使用 `@` 引用其他详细文档

**快速生成:**

```
```
/init
```
```

### .claudeignore - 节省 Token

告诉 Claude Code 哪些文件不应该被读取到上下文中。

**推荐配置:**

```
```
# 依赖目录
node_modules/

# 构建产物
dist/
build/
.next/

# 日志文件
*.log

# 环境变量
.env
.env.local

# 大型资源文件
*.png
*.jpg
*.mp4
```
```

### 权限配置

通过 `settings.json` 中的 `permissions` 配置,精细控制操作权限。

**权限配置结构:**

```
```
{
  "permissions": {
    "allow": ["Bash(git status)", "Edit(src/**/*.ts)"],
    "ask": ["Bash(git commit:*)", "Edit(package.json)"],
    "deny": ["Bash(rm -rf:*)", "Bash(sudo:*)"]
  }
}
```
```

**配置语法:**

| 操作类型 | 说明 | 示例 |
| --- | --- | --- |
| `Bash` | 执行终端命令 | `Bash(git status)` |
| `Edit` | 编辑文件 | `Edit(src/**/*.ts)` |
| `Read` | 读取文件 | `Read(README.md)` |
| `Write` | 创建新文件 | `Write(src/*.tsx)` |

**危险模式**(慎用):

```
```
claude --dangerously-skip-permissions
```
```

跳过所有权限确认,状态指示器显示 `Bypass Permissions on`。仅适用于个人学习项目,生产环境不推荐。

### Rules 规则目录

大型项目可以使用 Rules 目录进行模块化管理:

```
```
.claude/
├── settings.json
├── CLAUDE.md
└── rules/
    ├── 00-security.md
    ├── 01-coding-style.md
    ├── 10-api.md
    └── 20-testing.md
```
```

---

## 五、核心操作指令

### 文件操作

**读取文件:**

```
```
@src/app.tsx 解释这个文件
@src/utils/helpers.ts 找出潜在的性能问题
```
```

**编辑文件:**

```
```
将 src/utils/date.ts 的 formatDate 函数改为支持中文格式

@src/api/users.ts 重构这个文件:
1. 将重复的错误处理逻辑抽取到统一的 handleError 函数
2. 使用 async/await 替代 Promise 链
```
```

**创建文件:**

```
```
创...