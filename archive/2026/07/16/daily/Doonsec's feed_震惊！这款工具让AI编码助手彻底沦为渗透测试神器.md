---
title: 震惊！这款工具让AI编码助手彻底沦为渗透测试神器
url: https://mp.weixin.qq.com/s/eWb-hSNjEEY4_WsUcY_y6g
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:36.809647
---

# 震惊！这款工具让AI编码助手彻底沦为渗透测试神器

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UqOhHwF6jPxqcVpaQN502bXINrwSiaJRbZyia8URqoQrB4ibN47pH9kZ73hZacQfDdNBJDudEsdyordxDibsoTpdBrkcnqgZJ50RMc/0?wx_fmt=jpeg)

# 震惊！这款工具让AI编码助手彻底沦为渗透测试神器

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：本文仅做技术分享，使用该工具时需遵守相关AI平台的服务条款和安全政策，严禁将其用于任何未经授权的渗透测试、安全攻击或任何非法活动。使用者需自行承担一切风险。

## 重点导读简介

Codex Session Patcher 是一款针对主流 AI 编码工具会话进行深度修改与上下文注入的专用工具。该项目精准聚焦于安全测试/CTF 竞赛场景下 AI 工具频繁拒绝安全操作请求这一核心痛点，通过会话内容替换与配置文件注入两大技术路径，实现对 Codex CLI、Claude Code、OpenCode 三平台会话的全面掌控。

## 重点导读核心能力

### PART 01会话清洗

当 AI 编码工具在安全测试场景下产生拒绝回复时，该工具能够自动完成以下操作：

智能检测拒绝内容：采用两级检测策略——强短语全文精确匹配与弱关键词前缀匹配相结合，有效降低误报率

自动替换拒绝回复：调用 LLM（支持 OpenAI、Ollama、OpenRouter 等兼容接口）根据对话上下文生成符合语境的配合性替换内容，确保会话语义连贯

批量处理能力：可一次性处理会话中所有拒绝回复，而非仅处理最后一条

推理内容擦除：彻底删除 Reasoning/Thinking block 等加密推理内容，消除潜在痕迹

安全兜底机制：当检测到只有 `event_msg` 的历史 Codex 拒绝记录或 AI 返回问号乱码时，自动回退到预设安全默认文本

备份与还原：清理前自动创建时间戳备份，支持保留最近 5 个历史版本并随时一键还原

Diff 对比视图：提供清理前后的 Side-by-side 可视化对比

### PART 02CTF/渗透测试提示词注入

该工具支持在配置层面从源头降低被拒绝概率，涵盖三平台多种注入模式：

Codex Profile 模式：创建独立 `ctf.config.toml` profile，仅在 `codex -p ctf` 启动时生效，完全不影响正常开发会话

Codex 全局模式：注入全局配置，所有新会话自动继承 CTF 上下文

Claude Code 工作空间：创建专用 CTF 工作空间 `~/.claude-ctf-workspace`，通过项目级 CLAUDE.md 注入提示词

OpenCode 工作空间：创建专用 CTF 工作空间 `~/.opencode-ctf-workspace`，通过 AGENTS.md 注入提示词

提示词自定义：Web UI 内直接编辑注入提示词，支持模板保存与切换

AI 提示词改写：结合已注入的 CTF 系统提示词，AI 智能改写用户请求使其更易被接受

## 重点导读架构设计

### PART 03模块划分

核心库位于 `codex_session_patcher/` 目录：

`cli.py`：CLI 入口，负责参数解析与主流程调度

`core/formats.py`：多平台格式策略层，抽象出 `FormatStrategy` 基类，分别实现 CodexFormatStrategy、ClaudeCodeFormatStrategy、OpenCodeFormatStrategy 三种格式处理逻辑

`core/parser.py`：会话解析器，负责 JSONL 与 SQLite 格式的解析与反序列化

`core/detector.py`：拒绝检测器，基于关键词字典实现中英文拒绝内容识别

`core/patcher.py`：清理逻辑执行器，协调各组件完成会话内容替换

`core/sqlite_adapter.py`：OpenCode SQLite 专项适配器，处理数据库格式转换

`ctf_config/installer.py`：三平台 CTF 配置安装器，复杂度最高，支持 profile 模式与全局模式、追加与替换两种注入方式

`ctf_config/templates.py`：内置提示词模板库

`ctf_config/status.py`：配置状态检测与查询

### PART 04Web 层

`web/backend/`：FastAPI 后端，提供 RESTful API 与 WebSocket 实时日志推送

`web/frontend/`：Vue 3 + Naive UI 前端，实现会话列表、可视化清理、Diff 对比、多语言界面

### PART 05会话格式支持

| 平台 | 会话清理 | CTF 注入 | 会话格式 |
| --- | --- | --- | --- |
| Codex CLI | ✅ | ✅ Profile + 全局 | JSONL |
| Claude Code | ✅ | ✅ 专用工作空间 | JSONL |
| OpenCode | ✅ | ✅ 专用工作空间 | SQLite |

## 重点导读核心技术实现

### PART 06拒绝检测算法

检测器维护中英文拒绝关键词字典，支持用户自定义扩展。检测时将内容转为小写后遍历所有关键词进行模糊匹配，命中即标记。该算法时间复杂度为 O(m \* k)，其中 m 为内容长度，k 为关键词数量。

### PART 07格式策略模式

通过策略模式解耦不同平台的数据格式差异。每种策略实现四个核心接口：`get_assistant_messages` 提取助手消息、`get_thinking_items` 提取推理项、`extract_text_content` 提取纯文本、`update_text_content` 替换文本内容。这种设计确保新增平台支持时无需修改核心逻辑。

### PART 08备份机制

备份文件命名格式为 `{原文件名}.{timestamp}.bak`，自动保留最近 5 个版本。清理旧备份时按修改时间降序排列，删除超出配额的旧文件。

## 重点导读使用方式

### PART 09Web UI

生产模式启动：

```
bash./scripts/start-web.sh
```

访问 `http://localhost:8080` 即可进入可视化操作界面，支持会话列表浏览、过滤、可视化清理与 Diff 对比。

### PART 10CLI

```
bash# 预览模式（不修改文件）
codex-patcher --dry-run --show-content

# 清理最新会话
codex-patcher --latest

# 指定会话格式
codex-patcher --latest --format claude-code

# CTF 配置安装
codex-patcher --install-ctf-config
codex-patcher --install-claude-ctf
codex-patcher --install-opencode-ctf

# 查看 CTF 配置状态
codex-patcher --ctf-status
```

## 重点导读配置管理

配置文件位于 `~/.codex-patcher/config.json`，CLI 与 Web UI 共用。主要配置项包括：

| 配置项 | 说明 | 默认值 |
| --- | --- | --- |
| `mock_response` | 默认替换文本 | 配合性回复 |
| `ai_enabled` | 启用 AI 改写 | `false` |
| `ai_endpoint` | LLM API 地址 | — |
| `ai_key` | API Key | — |
| `ai_model` | 模型名称 | — |
| `custom_keywords` | 自定义拒绝检测关键词 | `{}` |
| `ctf_prompts` | 各平台自定义 CTF 提示词 | 内置模板 |

## 重点导读局限性

该工具无法突破平台最高安全策略，对于明确违规的请求仍可能被拒绝。模型版本更新可能影响清理与注入效果。OpenCode 无 profile 机制，CTF 注入依赖工作空间目录启动。清理后需手动执行 `resume` 继续上下文。

## 重点导读项目地址

本公众号非项目作者，仅做技术分享。

```
https://github.com/ryfineZ/codex-session-patcher
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrET5mJzBvhCRIGN5FZTKSKFNcwP7exVxDbDnIOzenpLU3dW72F5TfzZXk33jbmbVNKfoibbBl0Uic90GaYvwoIfdjNLV3cekuuY/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrH6K6Fx8AXnDCpDNyZEe1KK5sPPlu6RSbfDQDyjzZjDTCXM8vZTFp1Biag5lKoHg4uIN7xahTBN4yqt7LfT67Ca7Fm10HCOhq0/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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