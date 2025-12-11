---
title: CloudMeet：基于 Cloudflare 的免费开源会议预约工具
url: https://blog.upx8.com/4922
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-10
fetch_date: 2025-12-11T03:23:22.873412
---

# CloudMeet：基于 Cloudflare 的免费开源会议预约工具

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# CloudMeet：基于 Cloudflare 的免费开源会议预约工具

发布时间:
2025-12-10 New Article

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
2117

## CloudMeet：无需服务器的免费会议调度工具

CloudMeet 是一款完全免费、开源的会议预约调度系统，定位为 Calendly 的替代方案。它基于 Cloudflare 的免费服务构建，无需传统服务器即可部署，支持 Google Calendar 和 Outlook Calendar 双向同步，为个人与团队提供高效、可靠的日程管理体验。

![CloudMeet：基于 Cloudflare 的免费开源会议预约工具](https://cdn.skyimg.net/up/2025/12/10/dcb2c560.webp)

### 🌐 核心功能概览

* **双日历支持**：集成 Google 和 Microsoft Outlook 日历，支持单独或联合使用。
* **智能会议链接生成**：自动为会议生成 Google Meet 或 Microsoft Teams 会议链接。
* **灵活的时间配置**：可自定义工作时间与可预约时间段，支持多种会议类型（如 30 分钟、1 小时）。
* **邮件通知系统**：支持预定确认、取消提醒等多种邮件通知，全部可配置。
* **后台管理面板**：可视化控制邮件通知启用与禁用，集中管理预约配置。
* **一键部署更新**：基于 GitHub Actions，支持快速部署与自动同步更新。
* **Cloudflare 原生部署**：整个应用运行于 Cloudflare Pages 和 Workers 的免费资源之上，低成本高可用。

### ⚙️ 快速部署指南

CloudMeet 的部署过程简洁高效，主要分为以下步骤：

* 创建 Cloudflare API Token 与 D1 权限；
* 配置 Google OAuth 授权信息；
* 使用 GitHub 模板创建仓库并配置机密变量；
* 一键运行 GitHub Actions，即可完成部署；
* 可选支持自定义域名绑定与自动更新同步。

👉 **体验演示地址**：[meet.klappe.dev/cloudmeet](https://meet.klappe.dev/cloudmeet "CloudMeet 体验地址")

### 📩 邮件提醒功能

CloudMeet 默认启用自动会议提醒功能，基于 Cloudflare Workers 实现定时执行，支持在会议前24小时与1小时自动发送邮件提醒，进一步提升用户参与率。

> 为增强安全性，建议配置 `CRON_SECRET`，防止接口被非授权访问。

### 🔄 Outlook Calendar 支持（可选）

除 Google Calendar 外，CloudMeet 也支持通过 Microsoft OAuth 集成 Outlook Calendar，并可自动生成 Teams 会议链接。启用方式为：

* 在 Azure 注册新应用；
* 获取 Client ID 和 Secret；
* 配置 Microsoft Graph API 权限；
* 添加至 GitHub Secrets 并重新部署。

用户可在 Dashboard 内选择连接 Outlook 账户，并设定可用日历范围与会议提供商偏好。

### 👨‍💻 本地开发支持

支持开发者在本地运行 CloudMeet 实例，调试与二次开发：

```
cp .env.example .dev.vars
npm install
npm run db:init
npm run dev
```

### 🌟 开源地址

GitHub 项目主页：[github.com/dennisklappe/CloudMeet](https://github.com/dennisklappe/CloudMeet "CloudMeet 开源地址")

CloudMeet 是一款极简、高效、低成本的会议调度解决方案，适合自由职业者、远程团队、开源项目组或希望自托管日程系统的用户。结合 Cloudflare 强大的边缘计算能力，无需服务器运维即可构建可靠的会议预约系统。

[取消回复](https://blog.upx8.com/4922#respond-post-4922)

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