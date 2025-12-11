---
title: Claudable：开源AI Web构建器，秒级生成可部署应用
url: https://blog.upx8.com/4921
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-10
fetch_date: 2025-12-11T03:23:24.162721
---

# Claudable：开源AI Web构建器，秒级生成可部署应用

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Claudable：开源AI Web构建器，秒级生成可部署应用

发布时间:
2025-12-10 New Article

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
2862

## Claudable：AI驱动的开源Web构建平台

Claudable 是一款免费开源的 Web 构建器，结合 Claude Code、Codex、Cursor Agent、Qwen Code 等本地 CLI AI 编程代理，只需用自然语言描述你的想法，平台便会自动生成可运行的 Next.js 应用，并提供实时预览、Vercel 一键部署和 Supabase 数据库集成等功能，让构建现代 Web 产品变得前所未有地简单。

---

## 核心特性

### 🚀 自然语言生成代码

只需一句话描述：“我想做一个带夜间模式的任务管理工具”，Claudable 即可生成完整代码，配合热重载功能，即时查看修改效果。

### 🧠 多模型智能代理支持

支持 Claude Code（推荐）、Codex CLI（OpenAI GPT-5）、Cursor CLI（多模型）、Qwen Code（阿里开源）、Z.AI GLM-4.6（智谱AI）等。用户可根据项目需求灵活切换。

### 🌐 零配置即用体验

无需 API Key、无需复杂数据库设置，也不需要本地环境准备，使用 npm 安装后即可启动。

### 🎨 美观UI生成

借助 Tailwind CSS 和 shadcn/ui，Claudable 自动生成美观、响应式的前端界面，省去繁琐的设计工作。

### 📦 一键部署与集成

* **Vercel**：支持一键部署，无需手动配置。
* **Supabase**：集成生产级 PostgreSQL 数据库，并包含用户身份认证模块。
* **GitHub**：自动版本控制与持续部署流程配置。

### 🖥️ 桌面应用支持

提供 Electron 版本，适配 macOS、Windows 和 Linux 系统。

![Codex CLI Demo](https://github.com/opactorai/Claudable/raw/main/assets/gif/Claudable_v2_codex_1_1080p.gif "Claudable：开源AI Web构建器，秒级生成可部署应用 2")

---

## 快速上手指南

### 前置条件

* Node.js 18+
* 已登录的 Claude Code 或 Cursor CLI
* Git

### 本地运行步骤

```
git clone https://github.com/opactorai/Claudable.git
cd Claudable
npm install
npm run dev
```

访问：`http://localhost:3000`
系统将自动分配可用端口并创建 `.env` 文件。

---

## 常见问题与运维命令

* 重置数据库：`npm run db:reset`
* 备份数据库：`npm run db:backup`
* 清理依赖：`npm run clean` → 然后重新安装

注意：如遇端口冲突或权限问题，请根据提示调整用户权限或清理依赖环境。

---

## 社区与发展路线

项目完全遵循 MIT 开源协议，未来将加入：

* 模型上下文协议（MCP）原生支持
* 聊天/代码状态保存与恢复
* AGENTS.md 支持的多代理系统
* 网址克隆项目功能
* 更多社区贡献与优化

---

## 适合人群

* AI 编程初学者：无需手写代码，语义描述即可生成应用
* 独立开发者 & 黑客松参赛者：快速构建 MVP、提交演示项目
* 技术团队：原型设计、快速测试新功能或界面
* 教育机构：用于教学演示或编程启蒙课程

---

## 项目地址

GitHub：**[https://github.com/opactorai/Claudable](https://github.com/opactorai/Claudable "Claudable on GitHub")**

[取消回复](https://blog.upx8.com/4921#respond-post-4921)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2025 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")