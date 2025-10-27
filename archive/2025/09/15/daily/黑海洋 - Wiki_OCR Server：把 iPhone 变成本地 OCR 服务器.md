---
title: OCR Server：把 iPhone 变成本地 OCR 服务器
url: https://blog.upx8.com/4849
source: 黑海洋 - Wiki
date: 2025-09-15
fetch_date: 2025-10-02T20:10:00.692598
---

# OCR Server：把 iPhone 变成本地 OCR 服务器

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# OCR Server：把 iPhone 变成本地 OCR 服务器

发布时间:
2025-09-14

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
17687

## 什么是 OCR Server

OCR Server 是一款基于 Apple Vision Framework 的 iOS 应用，可将 iPhone 变成局域网内可访问的本地 OCR 服务器。它提供网页上传与 JSON API，支持多语言自动检测与高速识别，所有处理在设备端完成，无需依赖云端，数据不出本机。

![](https://cdn.skyimg.net/up/2025/9/14/4b09ebc2.webp)

## OCR Server核心能力

* **高精度文字识别**：基于 Vision 的 `VNRecognizeTextRequest`，对图像进行文字定位与提取，适用于常见场景的文本抽取。
* **多语言自动检测**：自动识别多语种内容，减少手动切换语言的成本。
* **网页与 API**：在同一网络内，通过应用显示的 IP 用浏览器上传图片并获取识别结果；同时提供返回 JSON 的 Web API，便于系统集成与自动化。
* **边界框与结构化结果**：新版在 JSON 中加入文字位置等信息，便于二次标注与可视化。
* **100% 本地处理与隐私保护**：处理过程在 iPhone 上完成，不上传云端，适合对合规与保密有要求的场景。

## 适用场景

* **开发测试**：为移动或后端应用提供局域网 OCR 测试环境。
* **团队协作**：在办公室/工作室内共享 OCR 服务，统一入口、减少账号与配额管理。
* **离线处理**：网络受限或禁止外连的环境下完成文字识别。
* **批量/集群**：用多台 iPhone 组成轻量 OCR 集群，提升吞吐。

## OCR Server如何使用

### 基本步骤

1. 打开应用，内置服务器自动启动。
2. 在同一 Wi-Fi/局域网内，用任意设备访问屏幕上显示的 IP。
3. 通过网页上传图片，数秒内返回识别文本与结构化结果；或以 API 方式对接业务。

### 稳定运行建议

需要长时间不间断服务时，可启用 **iOS 引导式访问（Guided Access）**，锁定在当前应用并管理自动锁屏行为，减少误触与待机中断。设置路径见 Apple 支持文档。

## OCR Server下载地址

GitHub地址：[https://github.com/riddleling/iOS-OCR-Server](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3JpZGRsZWxpbmcvaU9TLU9DUi1TZXJ2ZXI "OCR Server GitHub地址")

App Store下载地址：[OCR Server](https://blog.upx8.com/go/aHR0cHM6Ly9hcHBzLmFwcGxlLmNvbS91cy9hcHAvb2NyLXNlcnZlci9pZDY3NDk1MzMwNDE)

[取消回复](https://blog.upx8.com/4849#respond-post-4849)

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