---
title: 教你用Ollama本地部署Claude Code：私有化免API
url: https://blog.upx8.com/Ollama-Claude-Code-API
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-05-16
fetch_date: 2026-05-17T05:47:43.019806
---

# 教你用Ollama本地部署Claude Code：私有化免API

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 教你用Ollama本地部署Claude Code：私有化免API

发布时间:
2026-05-16 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
3389

#### ![教你用Ollama本地部署Claude Code：私有化免API](https://cdn.skyimg.net/up/2026/5/16/62c0c91b.webp)

#### Claude Code 到底强在哪里？

很多人第一次接触 Claude Code，都以为它只是"高级聊天工具"。但实际上，它和普通 AI 聊天客户端完全不是一个东西。

传统 AI 是你问一句、它答一句。而 Claude Code 会真正读取整个项目结构，然后自动分析代码、修改文件、安装依赖、执行命令、修复报错、重新运行项目——整个过程更像是 **AI + IDE + Terminal** 的结合体，而不是聊天机器人。这也是为什么很多开发者开始把它称为"AI 开发 Agent"。

![教你用Ollama本地部署Claude Code：私有化免API](https://cdn.skyimg.net/up/2026/5/16/839e2f9a.webp)

#### 为什么要接入 Ollama 本地模型？

Claude 官方 API 并不便宜，尤其在长上下文、大型项目、多轮 Agent 调用、自动修 Bug 等场景下，token 消耗会非常夸张。于是越来越多开发者开始尝试用本地模型接管 Claude Code。

核心工具就是 **CC Switch**——一个 API 转发层，让 Claude Code 以为自己在调用官方 API，实际上请求已被转发到本地 Ollama。

---

#### 本地部署步骤

**第一步：安装环境依赖** 提前安装好 [Git](https://blog.upx8.com/go/aHR0cHM6Ly9naXQtc2NtLmNvbS8)，作为基础环境。

**第二步：安装 Claude Code 桌面版** **【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9jbGF1ZGUuY29tL2Rvd25sb2Fk)】或 【[备用下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy9jYjBjN2NiMzk3Zjc)】**

**第三步：安装 Ollama 客户端** 前往 [Ollama 官网下载](https://blog.upx8.com/go/aHR0cHM6Ly9vbGxhbWEuY29tLw)。模型推荐根据显存大小选择：

* 显存充裕：Qwen 3.6/3.5、Gemma 4
* 推理类：DeepSeek R1
* 国产备选：GLM 系列

**![教你用Ollama本地部署Claude Code：私有化免API](https://cdn.skyimg.net/up/2026/5/16/86383a5b.webp)**

**第四步：下载 [CC Switch](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZhcmlvbjEyMzEvY2Mtc3dpdGNo)** 前往 [GitHub](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZhcmlvbjEyMzEvY2Mtc3dpdGNo) 或【**[打包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy9mMzRmYjk2M2UzMTc)**】，完成后进行如下配置：

![教你用Ollama本地部署Claude Code：私有化免API](https://cdn.skyimg.net/up/2026/5/16/81c0461c.webp)

![教你用Ollama本地部署Claude Code：私有化免API](https://cdn.skyimg.net/up/2026/5/16/bf7c5c6c.webp)

| 配置项 | 值 |
| --- | --- |
| 请求地址 | `http://127.0.0.1:11434/v1` |
| API 格式 | OpenAI Chat Completions |
| 认证字段 | ANTHROPIC\_API\_KEY |

**![教你用Ollama本地部署Claude Code：私有化免API](https://cdn.skyimg.net/up/2026/5/16/11a697b4.webp)**

**第五步：修改 Claude Code 配置** 在桌面版配置文件末尾加入以下注册表命令，让 CC Switch 强行注入模型名称：

```
"inferenceModels"="[\"haiku\",\"sonnet\",\"opus\"]"
```

---

#### 实际体验如何？

**适合场景（表现不错）：** HTML 页面、小型项目、自动化脚本、Docker 配置、VPS 运维。举个例子，直接说一句"帮我生成一个赛博朋克风格的个人主页"，本地模型会依次创建项目、生成网页、添加动画特效、自动运行——整个过程确实有一种"AI 正在真正工作"的感觉。

**明显短板（与官方 Claude Sonnet 仍有差距）：**

* 长上下文理解能力弱
* 大型复杂工程容易逻辑混乱
* 多步骤推理容易出错或修改错误文件
* 上下文过长后容易"遗忘"之前的内容

**多模态兼容性问题：** 虽然 Ollama 已支持不少 Vision 模型，但 Claude Code + CC Switch 这套链路对图片支持并不完整，上传图片后 AI 经常提示"没有看到图片"。根本原因是 Claude Code 本身更偏向代码 Agent，而非多模态聊天客户端，所以编程和自动化体验好，图片/OCR 兼容性一般。

---

#### 总结

Claude Code + Ollama 这套玩法，让人第一次真正感受到 AI 从"聊天工具"变成"生产力工具"的转变。随着 Qwen、DeepSeek、GLM、Gemma 等本地模型持续升级，一个完全本地化、零 API 成本、无 token 焦虑的 AI 开发助手，正在变得越来越可行。

目前阶段，它最适合中小型项目和自动化任务；复杂大型工程仍建议配合官方 Claude Sonnet 使用。

**视频教程：**https://www.youtube.com/watch?v=6iONJKrFs1k

[取消回复](https://blog.upx8.com/Ollama-Claude-Code-API#respond-post-8177)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [便签](https://txt.upx8.com)
* [关于](/about.html)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")