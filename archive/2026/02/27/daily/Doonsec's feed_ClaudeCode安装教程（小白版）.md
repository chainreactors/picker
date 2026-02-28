---
title: ClaudeCode安装教程（小白版）
url: https://mp.weixin.qq.com/s/rJT0VnAFc46OGstGqKIl-g
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:57:38.795079
---

# ClaudeCode安装教程（小白版）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6EuqF9cSY2nbBbzUEk4nmQpejGHribDbBsNmciaXrnY9KevuQOt7dicBoiazBFia1BicWEcfozCamGeHzvX10lenXCibXX2pPQ0yAB4WC7PE5wEhIg/0?wx_fmt=jpeg)

# ClaudeCode安装教程（小白版）

原创

xiejava
xiejava

fullbug

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2kHMV3tLBfUYOO5twABFytaZwibECDZEWIfrE7ic5nQ2WPMJOIgopex7FZQI3VMm5eibNib35J6OoUKVcVeB5cKOLicZRphiceQdaBLA/640?wx_fmt=png&from=appmsg)

## 什么是 Claude Code？

Claude Code 是一个智能编码助手，它可以在你的**命令行终端**中运行。你可以像和真人聊天一样，用自然语言告诉它你想做什么（比如”帮我写一个函数”、”修复这个bug”），它会自动帮你完成代码编写、调试、重构等任务。

**主要特点：**

* 在终端中直接对话，无需切换窗口
* 自动读取和理解你的项目代码
* 可以直接修改文件、执行命令
* 支持 GLM Coding Plan（智谱 AI 的模型）

---

## 前置准备

### 1. 安装 Node.js（必需）

Claude Code 需要 Node.js 18 或更高版本。

#### 检查是否已安装 Node.js

打开终端（Terminal），输入：

|  |
| --- |
| ``` node --version npm --version ``` |

* 如果显示版本号（如 `v18.x.x` 或 `v20.x.x`），说明已安装，可以跳过这一步
* 如果提示”命令未找到”，需要先安装 Node.js

#### 安装 Node.js

**Mac 用户推荐方式：使用 nvm（版本管理器）**

nvm 可以让你在同一台电脑上安装和管理多个 Node.js 版本。

1. 安装 nvm：

   |  |
   | --- |
   | ``` curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash ``` |
2. 重新打开终端，或执行以下命令使 nvm 生效：

   |  |
   | --- |
   | ``` export NVM_DIR="$HOME/.nvm" [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" ``` |
3. 安装最新的 Node.js LTS 版本：

   |  |
   | --- |
   | ``` nvm install --lts nvm use lts ``` |
4. 设置为默认版本：

   |  |
   | --- |
   | ``` nvm alias default lts/* ``` |

**Mac 用户备用方式：使用 Homebrew**

|  |
| --- |
| ``` # 如果没有安装 Homebrew，先安装它 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  # 安装 Node.js brew install node ``` |

**Windows 用户：**

1. 访问 Node.js 官网
2. 下载 LTS 版本（长期支持版）
3. 运行安装程序，一路”下一步”即可

**同时安装 Git for Windows（Windows 用户必需）：**

1. 访问 Git 官网
2. 下载并安装，使用默认设置即可

---

## 安装 Claude Code

### 方式一：npm 命令行安装（推荐）

1. 打开终端（Mac/Linux）或 PowerShell/CMD（Windows）
2. 执行安装命令：

   |  |
   | --- |
   | ``` npm install -g @anthropic-ai/claude-code ``` |
3. 验证安装是否成功：

   |  |
   | --- |
   | ``` claude --version ``` |

如果显示版本号（如 `2.0.14`），说明安装成功！

### 方式二：使用 Cursor 编辑器引导安装

如果你有 Cursor 编辑器但不熟悉命令行：

1. 打开 Cursor
2. 按 `Cmd + L`（Mac）或 `Ctrl + L`（Windows）打开聊天面板
3. 输入：`Help me install Claude Code`
4. Cursor 会引导你完成安装过程

---

## 配置国内模型

Claude Code需要接入大模型才能发挥作用，对于国内环境各个模型大厂都推出了Coding Plan套餐，以下以智谱AI的为例，安装完成后，需要配置智谱 AI 的 API Key 才能使用GLM-5模型。

### 获取 API Key

1. 访问 智谱 AI 开放平台
2. 注册/登录账号
3. 进入”API Key”管理页面
4. 创建新的 API Key 并复制保存

### 配置方式

1. 启动 Claude Code：

   |  |
   | --- |
   | ``` claude ``` |
2. 首次启动会提示配置 API，选择”Manual setup”或手动配置
3. 配置环境变量：

   |  |
   | --- |
   | ``` export ANTHROPIC_API_KEY="你的API_Key" ``` |

**Windows PowerShell 用户：**

|  |
| --- |
| ``` $env:ANTHROPIC_API_KEY="你的API_Key" ``` |

4. 永久保存配置（推荐）：

创建或编辑配置文件 `~/.claude/settings.json`（Mac/Linux）或 `%USERPROFILE%\.claude\settings.json`（Windows）：

|  |
| --- |
| ``` { "env": { "ANTHROPIC_API_KEY": "你的API_Key", "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/paas/v4/"   } } ``` |

---

## 开始使用

### 1. 启动 Claude Code

进入你的项目目录，然后运行：

|  |
| --- |
| ``` cd /path/to/your/project claude ``` |

### 2. 首次启动

* Claude Code 会询问是否信任该目录，选择 **“Trust”** 或 **“Yes”**
* 这样 Claude Code 才能读取和修改你的项目文件

### 3. 基本使用

启动后，你可以直接输入自然语言命令：

**示例：**

|  |
| --- |
| ``` > 帮我写一个 Python 函数，计算斐波那契数列 > 解释这个函数的作用 > 找出代码中所有的 console.log 并删除 > 运行测试用例 ``` |

**常用命令：**

* `/help`

  - 查看帮助信息
* `/status`

  - 查看当前配置和状态
* `/exit`

  - 退出 Claude Code

---

## 切换模型（可选）

Claude Code 支持多种智谱 AI 模型，你可以手动切换。

### 修改配置文件

编辑 `~/.claude/settings.json`：

|  |
| --- |
| ``` { "env": { "ANTHROPIC_API_KEY": "你的API_Key", "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/paas/v4/", "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air", "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.7", "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5"   } } ``` |

**模型说明：**

* `glm-4.5-air`

  ：轻量级模型，响应快速，适合简单任务
* `glm-4.7`

  ：主力模型，平衡性能和质量
* `glm-5`

  ：最新模型，能力最强，适合复杂任务

### 验证配置

重新启动 Claude Code，输入 `/status` 查看当前使用的模型。

---

## 常见问题

### Q1: npm install 提示权限错误（Mac/Linux）

**解决方案：**

|  |
| --- |
| ``` # 使用 sudo 安装（不推荐，但最简单） sudo npm install -g @anthropic-ai/claude-code  # 或配置 npm 全局目录（推荐） mkdir ~/.npm-global npm config set prefix '~/.npm-global' echo'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc source ~/.bashrc npm install -g @anthropic-ai/claude-code ``` |

### Q2: 配置文件修改后不生效

**解决步骤：**

1. 关闭所有 Claude Code 窗口
2. 重新打开终端
3. 再次运行 `claude` 启动
4. 如果问题仍存在，删除 `~/.claude/settings.json`，重新配置

### Q3: 如何升级到最新版本？

|  |
| --- |
| ``` # 检查当前版本 claude --version  # 升级到最新版本 claude update ``` |

推荐使用最新版本以获得最佳体验。

### Q4: Windows 下提示找不到 claude 命令

**解决方案：**

1. 确保 npm 全局安装路径在系统 PATH 中
2. 查找 npm 全局路径：`npm config get prefix`
3. 将该路径下的 `bin` 目录添加到系统环境变量 PATH 中
4. 或使用 PowerShell 重新安装：`npm install -g @anthropic-ai/claude-code`

### Q5: 如何在项目中使用？

进入任何项目目录后启动：

|  |
| --- |
| ``` cd /path/to/your/project claude ``` |

Claude Code 会自动扫描并理解项目结构，可以帮你完成：

* 代码生成和补全
* Bug 修复和调试
* 代码重构和优化
* 添加注释和文档

---

## 推荐工作流

### 日常开发流程

1. **启动项目**

   |  |
   | --- |
   | ``` cd my-project claude ``` |
2. **描述需求**

   |  |
   | --- |
   | ``` > 帮我创建一个用户登录页面，使用 HTML + CSS + JavaScript ``` |
3. **迭代优化**

   |  |
   | --- |
   | ``` > 给登录按钮添加 hover 效果 > 添加表单验证功能 ``` |
4. **调试问题**

   |  |
   | --- |
   | ``` > 为什么点击登录后没有反应？帮我检查代码 ``` |

### 团队协作

* Claude Code 可以读取整个项目代码库
* 可以帮你理解别人的代码
* 可以协助 Code Review
* 可以生成文档和注释

---

## 进阶配置

### 配置视觉 MCP 服务器（图片识别）

如果你需要让 Claude Code 识别和分析图片，可以配置视觉 MCP 服务器。

参考文档：视觉MCP服务器

### 配置搜索 MCP 服务器（联网搜索）

如果你需要让 Claude Code 搜索最新信息，可以配置搜索 MCP 服务器。

参考文档：搜索MCP服务器

### 配置网页读取 MCP 服务器

如果你需要让 Claude Code 读取网页内容，可以配置网页读取 MCP 服务器。

参考文档：网页读取MCP服务器

---

## 总结

安装 Claude Code 只需要三步：

1. ✅ 安装 Node.js 18+
2. ✅ 运行 `npm install -g @anthropic-ai/claude-code`
3. ✅ 配置智谱 AI API Key

安装后，在任何项目目录运行 `claude` 即可开始使用！

---

## 参考资源

* Claude Code 官方文档
* 智谱 AI 开放平台
* GLM Coding Plan 文档
* Node.js 官网
* nvm GitHub

---

作者博客：http://xiejava.ishareread.com/

“fullbug”微信公众号

关注：微信公众号,一起学习成长！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6cNzMD9ovmPQDhxzubx0Hbicg3tUKoQSdEX1ZsXHCL3QBrKaPlbvPK0boZA7WH0KJrxWWUsDAwq7GJOfF0lBq1Q/0?wx_fmt=png)

fullbug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6cNzMD9ovmPQDhxzubx0Hbicg3tUKoQSdEX1ZsXHCL3QBrKaPlbvPK0boZA7WH0KJrxWWUsDAwq7GJOfF0lBq1Q/0?wx_fmt=png)

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