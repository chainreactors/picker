---
title: Cloud Mail 邮箱搭建（CF部署无需服务器）
url: https://blog.upx8.com/4839
source: 黑海洋 - Wiki
date: 2025-08-22
fetch_date: 2025-10-07T00:17:57.408669
---

# Cloud Mail 邮箱搭建（CF部署无需服务器）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Cloud Mail 邮箱搭建（CF部署无需服务器）

发布时间:
2025-08-21

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
55576

## ![](https://cdn.skyimg.net/up/2025/8/21/f3ddb4b3.webp)

## 项目简介

只需要一个域名，就可以创建多个不同的邮箱，类似各大邮箱平台 QQ邮箱，谷歌邮箱等，本项目使用Cloudflare部署，Resend推送邮件，无需服务器费用，搭建自己的邮箱服务

**代发模式，安全无屏蔽**

## 功能介绍

* **💰 低成本使用**：无需服务器，部署到 Cloudflare Workers 降低使用成本
* **💻 响应式设计**：响应式布局自动适配PC和大部分手机端浏览器
* **📧 邮件发送**：集成resend发送邮件，支持群发，内嵌图片和附件发送，发送状态查看
* **🛡️ 管理员功能**：可以对用户，邮件进行管理，RABC权限控制对功能及使用资源限制
* **🔀 多号模式**：开启后一个用户可以添加多个邮箱，默认一用户一邮箱，类似各大邮箱平台
* **📦 附件收发**：支持收发附件，使用R2对象存储保存和下载文件
* **🔔 邮件推送**：接收邮件后可以转发到TG机器人或其他服务商邮箱
* **📡 开放API**：支持使用API批量生成用户，多条件查询邮件
* **📈 数据可视化**：使用echarts对系统数据详情，用户邮件增长可视化显示
* **⭐ 星标邮件**：标记重要邮件，以便快速查阅
* **🎨 个性化设置**：可以自定义网站标题，登录背景，透明度
* **⚙️ 功能设置**：可以对注册，邮件发送，添加等功能关闭和开启，设为私人站点
* **🤖 人机验证**：集成Turnstile人机验证，防止人机批量注册
* **📜 更多功能**：正在开发中...

## 技术栈

* **框架**：[Vue3](https://blog.upx8.com/go/aHR0cHM6Ly92dWVqcy5vcmcv) + [Element Plus](https://blog.upx8.com/go/aHR0cHM6Ly9lbGVtZW50LXBsdXMub3JnLw)
* **Web框架**：[Hono](https://blog.upx8.com/go/aHR0cHM6Ly9ob25vLmRldi8)
* **ORM：**[Drizzle](https://blog.upx8.com/go/aHR0cHM6Ly9vcm0uZHJpenpsZS50ZWFtLw)
* **平台：** [Cloudflare workers](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmNsb3VkZmxhcmUuY29tL3dvcmtlcnMv)
* **邮件推送：** [Resend](https://blog.upx8.com/go/aHR0cHM6Ly9yZXNlbmQuY29tLw)
* **缓存**：[Cloudflare KV](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmNsb3VkZmxhcmUuY29tL2t2Lw)
* **数据库**：[Cloudflare D1](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmNsb3VkZmxhcmUuY29tL2QxLw)
* **文件存储**：[Cloudflare R2](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmNsb3VkZmxhcmUuY29tL3IyLw)

## 项目展示

* [在线演示](https://blog.upx8.com/go/aHR0cHM6Ly9za3ltYWlsLmluay8)
* [部署文档](https://blog.upx8.com/go/aHR0cHM6Ly9kb2Muc2t5bWFpbC5pbmsv)
* [小白保姆教程-界面部署](https://blog.upx8.com/go/aHR0cHM6Ly9kb2Muc2t5bWFpbC5pbmsvZ3VpZGUvdmlhLXVpLmh0bWw)
* [Github](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2VvYW8vY2xvdWQtbWFpbA)

[取消回复](https://blog.upx8.com/4839#respond-post-4839)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")