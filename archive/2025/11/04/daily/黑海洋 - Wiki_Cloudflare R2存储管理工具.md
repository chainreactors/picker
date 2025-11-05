---
title: Cloudflare R2存储管理工具
url: https://blog.upx8.com/4893
source: 黑海洋 - Wiki
date: 2025-11-04
fetch_date: 2025-11-05T03:11:23.747961
---

# Cloudflare R2存储管理工具

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Cloudflare R2存储管理工具

发布时间:
2025-11-04 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
4527

# ![](https://cdn.skyimg.net/up/2025/11/4/4aef245c.webp)

# S3 Manager

S3 Manager 是一款易用的 S3 兼容的存储管理工具（目前支持 Cloudflare R2、阿里云 OSS）。

## 注

* 本项目fork自 [https://github.com/jlvihv/R2Uploader](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2psdmlodi9SMlVwbG9hZGVy) ，在其基础上进行了管理能力和操作逻辑的优化

## 特性

* **易用性：** 简单直观的用户界面，轻松上手。
* **多文件上传：** 支持同时上传多个文件。
* **大文件处理：** 针对大文件上传进行了优化。
* **跨平台：** 跨平台桌面应用程序。

## 技术栈

* **前端：** Svelte
* **构建工具：** Bun
* **后端：** Rust, Tauri

## 环境要求

* **Rust:** 确保您的电脑上已安装 Rust。
* **Bun:** 确保您的电脑上已安装 Bun。

## 开发

1. 克隆代码库到本地。
2. 使用 `bun tauri dev` 命令进行快速开发。

## 构建

1. 使用 `bun tauri build` 命令构建可执行文件。
2. 构建后的可执行文件位于 `src-tauri/target/release/bundle` 目录下。

**下载地址：[https://github.com/jooler/s3manager/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2pvb2xlci9zM21hbmFnZXIvcmVsZWFzZXM)**

[取消回复](https://blog.upx8.com/4893#respond-post-4893)

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