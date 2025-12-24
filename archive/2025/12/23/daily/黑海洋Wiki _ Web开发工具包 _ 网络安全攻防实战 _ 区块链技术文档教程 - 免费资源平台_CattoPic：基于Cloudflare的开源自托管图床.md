---
title: CattoPic：基于Cloudflare的开源自托管图床
url: https://blog.upx8.com/4929
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-23
fetch_date: 2025-12-24T03:22:02.378158
---

# CattoPic：基于Cloudflare的开源自托管图床

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# CattoPic：基于Cloudflare的开源自托管图床

发布时间:
2025-12-23 New Article

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
1864

## CattoPic：轻量自托管图床方案，支持标签管理与格式优化

CattoPic 是一个基于 Cloudflare 技术栈打造的开源图床服务，专为开发者与独立站用户设计，支持图片上传、自动格式转换（WebP/AVIF）、标签归类和公开的随机图片 API。前端采用 Next.js 构建，后端以 Cloudflare Workers 和 Hono 实现无服务器部署，具备快速、稳定、高可用的特性。

![CattoPic：基于Cloudflare的开源自托管图床](https://cdn.skyimg.net/up/2025/12/23/e70e03d8.webp)

### 🚀 支持多种图片格式与自动优化

CattoPic 支持 JPEG、PNG、GIF、WebP、AVIF 等主流图片格式，并在上传后自动生成更优传输效率的 WebP 和 AVIF 版本，有效降低带宽占用。

### 🏷️ 标签系统与批量管理

通过标签系统，用户可以对图片进行分类管理，并支持批量添加、编辑与删除操作，提升资源调取与组织效率。

### 🔀 随机图片API与过滤参数

CattoPic 提供公开的随机图片 API，支持按标签等条件筛选，适合嵌入展示图、社交媒体、博客封面等场景。

---

## 核心架构与技术栈

| 组件 | 技术 | 功能 |
| --- | --- | --- |
| 前端 | Next.js 16, React 19, Tailwind CSS | 上传、管理界面，深色模式支持 |
| API | Cloudflare Workers + Hono | 路由、权限验证、REST API |
| 存储 | Cloudflare R2 | 存储原图及转换后的 WebP/AVIF 版本 |
| 数据库 | Cloudflare D1（SQLite） | 存储元信息、标签、API 密钥 |
| 缓存 | Cloudflare KV | 响应缓存，提高性能 |
| 队列 | Cloudflare Queues | 异步批量处理和删除任务 |
| 处理器 | Cloudflare Images | 图片实时转换与压缩优化 |
| 定时器 | Cron Triggers | 自动清理过期资源 |

---

## 快速开始部署（要求）

* Node.js 18+
* pnpm 包管理器
* Cloudflare 账号
* Vercel 账号（或任意静态托管服务）

---

## 为什么选择 CattoPic？

* 不依赖传统服务器，无需运维成本
* 完全自托管，掌握全部图片资源
* 可扩展性强，便于与前端项目集成
* 极简 UI + 标签系统，提升管理体验

---

## 适用场景

* 博主 & 独立站长图床替代方案
* AI 图像项目的图片素材库
* 图片分发、短链接缩图平台
* 嵌入式展示封面、banner 系统

## CattoPic开源地址

在线体验地址：[https://image-flow-next-js.vercel.app/](https://image-flow-next-js.vercel.app/ "CattoPic 体验地址")

项目开源地址：[https://github.com/Yuri-NagaSaki/CattoPic](https://github.com/Yuri-NagaSaki/CattoPic "CattoPic GitHub")

[取消回复](https://blog.upx8.com/4929#respond-post-4929)

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