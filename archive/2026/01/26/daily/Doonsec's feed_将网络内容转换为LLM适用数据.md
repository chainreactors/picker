---
title: 将网络内容转换为LLM适用数据
url: https://mp.weixin.qq.com/s/Qu-TTZ-i5LguH8EgQ5z7Mg
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:35:29.460671
---

# 将网络内容转换为LLM适用数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4Ln7j9YplYm01GtFd3BJ4ib31gvw2Kf1tE3ueFic1nkTNS6BRCjHxquicvsXH8OUxl0HOSuGaXrCWYic0ktlEpfCeg/0?wx_fmt=jpeg)

# 将网络内容转换为LLM适用数据

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器中沉浸阅读

🕷️ WaterCrawl 是一个功能强大的 Web 应用程序，它使用 Python、Django、Scrapy 和 Celery 来抓取网页并提取相关数据。

## 🚀 快速入门

1. 🐳快速入门
2. 💻开发**（欢迎贡献）**

### 🐳 快速入门

要在本地 Docker 上构建和运行 WaterCrawl，请按照以下步骤操作：

1. 克隆仓库：

   ```
   git clone https://github.com/watercrawl/watercrawl.gitcd watercrawl
   ```
2. 构建并运行 Docker 容器：

   ```
   cd docker cp .env.example .env docker compose up -d
   ```
3. 使用 open http://localhost访问应用程序

> **⚠️重要提示**：如果您要部署在除 localhost 以外的域名或 IP 地址上，则必须更新 .env 文件中的 MinIO 配置：
>
> ```
> # Change this from 'localhost' to your actual domain or IPMINIO_EXTERNAL_ENDPOINT=your-domain.com# Also update these URLs accordinglyMINIO_BROWSER_REDIRECT_URL=http://your-domain.com/minio-console/ MINIO_SERVER_URL=http://your-domain.com/
> ```
>
> 如果未更新这些设置，将导致文件上传和下载失败。更多详情，请参阅DEPLOYMENT.md 文件。

> **重要提示：**部署到生产环境之前，请务必使用`.env`正确的配置值更新配置文件。此外，请确保设置并配置数据库、MinIO 以及任何其他必需的服务。更多信息，请参阅部署指南。

### 💻 开发（欢迎贡献）

如需参与本地发展或做出贡献，请遵循我们的贡献指南🤝

## ✨ 特点

* **🕸️ 高级网页爬虫和抓取**- 提供高度可定制的网站爬虫选项，包括深度、速度和目标内容抓取。
* **🔍 强大的搜索引擎**- 通过多种搜索深度（基本、高级、终极）查找网络上的相关内容
* **🌐 多语言支持**- 可按国家/地区定向搜索和抓取不同语言的内容
* **⚡ 异步处理**- 通过服务器发送事件 (SSE) 监控爬取和搜索的实时进度
* **🔄 基于 OpenAPI 的 REST API** - 包含详细文档和客户端库的综合 API
* **🔌 丰富的生态系统**- 与 Dify、N8N 和其他 AI/自动化平台集成
* **🏠 自托管 & 开源**- 完全掌控您的数据，并提供便捷的部署选项
* **📊 高级结果处理**- 下载并处理带有自定义参数的搜索结果

查看我们的API 概述，了解有关这些功能的更多信息。

## 🛠️客户端SDK

* ✅ **Python 客户端**- 功能齐全的 SDK，支持所有 API 端点
* ✅ **Node.js 客户端**- 完整的 JavaScript/TypeScript 集成
* ✅ **Go Client** - 功能齐全的 SDK，支持所有 API 端点
* ✅ **PHP客户端**- 功能齐全的SDK，支持所有API接口
* 🔜 **Rust客户端**- 即将推出

## 🔌 集成

* ✅ Dify 插件（源代码）
* ✅ N8N 工作流节点（源代码）
* ✅ Dify 知识库
* 🔄 Langflow（拉取请求 - 尚未合并）
* 🔜 Flowise（即将推出）

## 🔧 插件

* ✅ WaterCrawl 插件
* ✅ OpenAI 插件

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

网络安全民工

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

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