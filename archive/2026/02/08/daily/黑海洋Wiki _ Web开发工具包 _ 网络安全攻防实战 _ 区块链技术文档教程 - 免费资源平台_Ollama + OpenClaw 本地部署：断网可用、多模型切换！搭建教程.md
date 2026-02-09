---
title: Ollama + OpenClaw 本地部署：断网可用、多模型切换！搭建教程
url: https://blog.upx8.com/Ollama-OpenClaw
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-02-08
fetch_date: 2026-02-09T04:18:35.892441
---

# Ollama + OpenClaw 本地部署：断网可用、多模型切换！搭建教程

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Ollama + OpenClaw 本地部署：断网可用、多模型切换！搭建教程

发布时间:
2026-02-08 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
6516

![Ollama + OpenClaw 本地部署：断网可用、多模型切换！搭建教程](https://www.freedidi.com/wp-content/uploads/2026/02/20260208_1770540945-scaled.webp)

基于Ollama和OpenClaw实现**100%本地化部署AI助手**的完整指南，涵盖环境准备、模型部署、多模型切换及Telegram对接，确保**免费、断网可用、灵活扩展**的特性。内容综合多篇实践文档，关键步骤均附引用来源。

### 一、核心优势与架构

1. **完全本地化**
   * 数据无需上传云端，隐私零泄露，断网环境下仍可运行。
   * 通过Ollama管理本地模型（如Qwen3、GPT-OSS等），OpenClaw负责任务调度，形成闭环链路。
2. **多模型自由切换**
   * 支持主流开源模型（Qwen3、GLM-4.7、GPT-OSS等），通过修改配置文件即可切换。
3. **硬件友好**
   * 最低配置：16GB内存（MacOS）或GPU服务器（如NVIDIA显卡）；推荐32GB以上内存+GPU加速。

### 二、前期环境准备

#### 1. 安装基础工具

* **Git**（Windows管理员权限执行）：

```
winget install git.git
# 若报错，调整执行策略：
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

* **Ollama客户端**：
  官网下载安装包（[https://ollama.com/download](https://blog.upx8.com/go/aHR0cHM6Ly9vbGxhbWEuY29tL2Rvd25sb2Fk)）或命令行安装（Linux）：

```
curl -fsSL https://ollama.com/install.sh | sh
```

#### 2. 模型选择与下载

![Ollama + OpenClaw 本地部署：断网可用、多模型切换！搭建教程](https://www.freedidi.com/wp-content/uploads/2026/02/20260208_1770541228.webp)

* **推荐模型**（需64k以上上下文窗口）：

  | 模型名称 | 特点 | 下载命令 |
  | --- | --- | --- |
  | `qwen3-coder` | 编码任务优化 | `ollama pull qwen3-coder` |
  | `gpt-oss:20b` | 平衡性能与速度 | `ollama pull gpt-oss:20b` |
  | `glm-4.7` | 通用能力强 | `ollama pull glm-4.7` |

### 三、OpenClaw部署与配置

#### 1. 安装OpenClaw

* **通用命令**：

  ```
  curl -fsSL https://openclaw.ai/install.sh | bash
  ```

* **Windows专用**：

  ```
  iwr -useb https://openclaw.ai/install.ps1 | iex
  ```

#### 2. 连接本地模型

* **启动服务**：

  ```
  ollama launch openclaw
  ```
* **配置文件修改**（关键步骤）：

### 四、多模型切换与验证

1. **切换模型**：
2. **验证部署**：
   访问`http://localhost:18789?token=配置中的token`，输入问题测试回复是否来自本地模型。

### 五、对接Telegram机器人

1. **创建Bot**：
   通过`@BotFather`申请新机器人，获取Token（如`8123121125:AAExamegv-0FQCfhfbazmp4405V0XAJCKfk`）[用户提供]。
2. **配对OpenClaw**：
   在Powershell中执行（替换配对码）：![Ollama + OpenClaw 本地部署：断网可用、多模型切换！搭建教程](https://www.freedidi.com/wp-content/uploads/2026/01/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE-2026-01-30-210735.webp)

   ```
   openclaw pairing approve telegram DLW7HQ69
   ```
3. **重启服务**：

   ```
   ollama launch openclaw
   ```

### 六、常见问题与优化

* **GPU加速**：若使用NVIDIA显卡，需安装`nvidia-container-toolkit`并配置Docker。
* **性能调优**：调整`contextWindow`和`maxTokens`参数以匹配硬件能力。
* **安全部署**：建议Docker容器以非root用户运行，挂载只读文件系统。

[取消回复](https://blog.upx8.com/Ollama-OpenClaw#respond-post-5833)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")