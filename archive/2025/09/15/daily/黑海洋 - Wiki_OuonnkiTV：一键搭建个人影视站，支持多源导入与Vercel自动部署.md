---
title: OuonnkiTV：一键搭建个人影视站，支持多源导入与Vercel自动部署
url: https://blog.upx8.com/4854
source: 黑海洋 - Wiki
date: 2025-09-15
fetch_date: 2025-10-02T20:09:59.481088
---

# OuonnkiTV：一键搭建个人影视站，支持多源导入与Vercel自动部署

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# OuonnkiTV：一键搭建个人影视站，支持多源导入与Vercel自动部署

发布时间:
2025-09-14

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
18644

## OuonnkiTV概览

OuonnkiTV 是一个由 React + Vite + TypeScript 构建的现代化前端，用于聚合搜索与播放网络视频资源。项目在 LibreSpark/LibreTV 的基础上重构与增强，带来更清晰的模块化架构、更顺手的交互体验和更稳健的状态管理。支持跨端播放、搜索与观看历史、按需配置多个视频源，并可在 Vercel 上快速部署个人影视站。

### 适用人群

* 希望零后端一键搭建个人影视站的站长
* 需要聚合多视频源并统一搜索/播放的开发者
* 关注前端性能优化与状态管理实践的学习者

**在线演示**：[https://tv.ouonnki.site/](https://blog.upx8.com/go/aHR0cHM6Ly90di5vdW9ubmtpLnNpdGUv "OuonnkiTV 演示地址")

**GitHub 源码**：[https://github.com/Ouonnki/OuonnkiTV](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL091b25ua2kvT3Vvbm5raVRW "OuonnkiTV GitHub地址")

## OuonnkiTV核心特性

* **实时搜索提示**：支持历史记录与联想建议，提升检索效率。
* **流畅播放体验**：基于 xgplayer，支持 HLS / MP4。
* **清晰内容页**：标题、封面、简介结构化呈现。
* **自动历史追踪**：观看与搜索历史自动保存，可一键清理。
* **多源批量导入**：文件、JSON 文本、URL 三种方式导入视频源。
* **个性化设置**：主题与偏好可配置。
* **性能优化策略**：代码分割、缓存与按需加载协同提速。
* **响应式适配**：移动与桌面端自适应布局。
* **稳健状态管理**：基于 Zustand，数据结构清晰、维护成本低。

## 视频源导入与管理

### 支持的导入方式

* **本地文件导入（📁）**：拖拽或选择 JSON 文件，自动校验格式。
* **JSON 文本导入（📝）**：直接粘贴配置，提供实时语法检查与多行格式化。
* **URL 导入（🌐）**：从远程地址获取配置，支持 GitHub、Gitee 等代码托管平台，并自动处理网络请求。

### JSON 基本格式

```
[
  {
    "id": "source1",
    "name": "示例视频源",
    "url": "https://api.example.com/search",
    "detailUrl": "https://api.example.com/detail",
    "isEnabled": true
  }
]
```

#### 字段说明

* **id**：源的唯一标识符（可选，系统可自动生成）
* **name**：视频源显示名称（必需）
* **url**：搜索 API 地址（必需）
* **detailUrl**：详情 API 地址（可选，默认与 `url` 相同）
* **isEnabled**：是否启用该源（可选，默认 `true`）

#### 支持的 JSON 形态

* 单个对象：`{"name":"源名称","url":"API地址"}`
* 对象数组：`[{"name":"源1","url":"API1"},{"name":"源2","url":"API2"}]`
* 多行格式化 JSON 与紧凑单行 JSON

### 导入流程

1. 进入设置页（右上角设置图标）
2. 点击“导入源”
3. 按需选择：文件导入 / 文本导入 / URL 导入
4. 点击“开始导入”
5. 查看结果提示：展示成功导入数量并自动关闭弹窗

### 导入体验优化

* **自动去重**：重复源会被过滤
* **数据验证**：校验 JSON 格式和必需字段
* **错误提示**：提供可定位问题的详细信息
* **Toast 通知**：实时反馈导入进度与结果
* **批量处理**：一次导入多个视频源

## 技术栈与性能

* **前端栈**：React + Vite + TypeScript
* **播放器**：xgplayer（HLS / MP4）
* **状态管理**：Zustand
* **性能策略**：代码分割、缓存命中与按需加载，配合响应式布局，带来更快的首屏与交互响应

## OuonnkiTV部署与演示

**在线演示**：[https://tv.ouonnki.site/](https://blog.upx8.com/go/aHR0cHM6Ly90di5vdW9ubmtpLnNpdGUv "OuonnkiTV 演示地址")

**GitHub 源码**：[https://github.com/Ouonnki/OuonnkiTV](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL091b25ua2kvT3Vvbm5raVRW "OuonnkiTV GitHub地址")

**部署建议**：支持在 Vercel 自动部署，适合个人快速上线与迭代

[取消回复](https://blog.upx8.com/4854#respond-post-4854)

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