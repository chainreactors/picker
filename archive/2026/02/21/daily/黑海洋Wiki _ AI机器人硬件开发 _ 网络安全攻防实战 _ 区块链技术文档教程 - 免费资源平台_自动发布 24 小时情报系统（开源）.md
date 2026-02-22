---
title: 自动发布 24 小时情报系统（开源）
url: https://blog.upx8.com/24
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-02-21
fetch_date: 2026-02-22T04:10:12.312948
---

# 自动发布 24 小时情报系统（开源）

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 自动发布 24 小时情报系统（开源）

发布时间:
2026-02-21 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
2193

## 📺 界面预览

![自动发布 24 小时情报系统（开源）](https://cdn.skyimg.net/up/2026/2/21/d6902b4a.webp)

---

## ✨ 功能特性

|  |  |
| --- | --- |
| 🔍 多平台数据采集   * **GitHub Trending** - 热门开源项目 * **Twitter/X** - 实时热点动态 * **Reddit** - 社区讨论话题 * **HackerNews** - 技术前沿资讯 * **小红书** - 生活消费热点 | 🤖 AI 智能生成   * **6-Skill 工作流** - 选题→调研→结构→写作→封装→发布 * **去 AI 味** - 有观点、有经验、可操作 * **语义去重** - ChromaDB 向量相似度检测 * **一键推送** - 微信 PushPlus 通知 |

---

## ⚡ 快速开始

### 🌐 在线体验（无需安装）

|  |  |
| --- | --- |
| [![Hugging Face Spaces](https://camo.githubusercontent.com/1317ddca4d7bdf1cd0fa1f2e3b9c0ac50103ce137a83221470e107a2c6987dbe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d2545372541422538422545352538442542332545342542442539332545392541412538432d626c75653f7374796c653d666f722d7468652d6261646765)](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9zcGFjZXMveXVndTg4L2h1bnRlci1haS1jb250ZW50LWZhY3Rvcnk)  **一键打开，直接使用** | [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://blog.upx8.com/go/aHR0cHM6Ly9jb2Rlc3BhY2VzLm5ldy9QYW5ndS1JbW1vcnRhbC9odW50ZXItYWktY29udGVudC1mYWN0b3J5P3F1aWNrc3RhcnQ9MQ)  **在线开发环境，可修改代码** |

### 💻 本地部署

**空白电脑双击即可运行，自动下载 Python + 所有依赖！**

```
# Mac / Linux
bash run.sh

# Windows（双击运行）
run.bat
```

> 首次运行需下载环境约 3-5 分钟，之后秒启动

### 配置 API Key

启动后在 Web UI 的「⚙️ 配置」中填入 [Gemini API Key](https://blog.upx8.com/go/aHR0cHM6Ly9haXN0dWRpby5nb29nbGUuY29tL2FwaWtleQ)，点击保存即可。

---

## 📋 五种内容模板

| 模板 | 数据源 | 输出 | 适用场景 |
| --- | --- | --- | --- |
| `github` | GitHub Trending | 公众号长文 | 技术博主 |
| `pain` | Twitter + Reddit | 诊断报告 | 产品经理 |
| `news` | 5 平台汇总 | 资讯快报 | 科技媒体 |
| `xhs` | 小红书热门 | 种草文章 | 生活博主 |
| `auto` | 全平台采集 | AI 生活黑客 | 全栈创作 |

```
# CLI 运行
uv run hunter run -t github    # GitHub 模板
uv run hunter run -t pain      # 痛点诊断
uv run hunter run --dry-run    # 试运行，不推送
```

---

## 🏗️ 核心架构

```
┌─────────────────────────────────────────────────────────────────┐
│                     Hunter AI 6-Skill 数据流                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Topic ──→ Research ──→ Structure ──→ Write ──→ Package ──→ Publish
│   选题判断    深度调研     结构设计      内容写作    封装优化     发布推送
│                                                                 │
│   数据源 ──────────→ AI 分析 ──────────→ 内容输出 ──────────→ 推送
│   GitHub/Twitter/     Gemini 2.0        Markdown        PushPlus
│   Reddit/HN/小红书     Flash             公众号文章       微信通知
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ 配置说明

### 最小配置

```
# config.yaml
gemini:
  api_key: "你的 Gemini API Key"
```

### 各模板所需配置

| 配置项 | github | pain | news | xhs |
| --- | --- | --- | --- | --- |
| `gemini.api_key` | ✅ | ✅ | ✅ | ✅ |
| `github.token` | 可选 | - | - | - |
| `twitter.cookies_path` | - | ✅ | ✅ | - |
| `xiaohongshu.cookies` | - | - | - | ✅ |
| `pushplus.token` | 可选 | 可选 | 可选 | 可选 |

**完整配置示例**

```
# AI 大模型配置（必填）
gemini:
  api_key: "你的 API Key"
  model: "gemini-2.0-flash"

# GitHub 配置
github:
  token: "ghp_xxx"      # 可选，提高配额
  min_stars: 200

# Twitter 配置
twitter:
  cookies_path: "data/cookies.json"

# 小红书配置
xiaohongshu:
  cookies: ""           # 浏览器 F12 复制

# 推送配置
pushplus:
  token: "你的 Token"
  enabled: true

# 公众号人设
account:
  name: "AI技术前沿"
  tone: "专业且引人入胜"
  niche: "AI技术"
```

---

## 📁 工程结构

```
hunter-ai-content-factory/
├── src/
│   ├── intel/          # 📡 数据采集层
│   ├── templates/      # 📋 内容模板
│   ├── factory/        # 🏭 内容生产
│   └── utils/          # 🔧 工具函数
├── data/               # 数据存储
├── output/             # 输出目录
└── config.yaml         # 配置文件
```

---

## 🛠️ 技术栈

| 组件 | 技术选型 |
| --- | --- |
| AI 模型 | Gemini 2.0 Flash |
| HTTP 客户端 | httpx |
| 浏览器自动化 | Playwright |
| 向量数据库 | ChromaDB |
| 关系数据库 | SQLite |
| 包管理 | uv |

---

## 项目地址：[https://github.com/Pangu-Immortal/hunter-ai-content-factory](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1Bhbmd1LUltbW9ydGFsL2h1bnRlci1haS1jb250ZW50LWZhY3Rvcnk)

[取消回复](https://blog.upx8.com/24#respond-post-6176)

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