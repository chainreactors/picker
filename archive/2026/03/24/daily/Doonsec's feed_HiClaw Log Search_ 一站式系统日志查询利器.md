---
title: HiClaw Log Search: 一站式系统日志查询利器
url: https://mp.weixin.qq.com/s/5TC5fXnHSRYVIizY18zv5g
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:12:56.723132
---

# HiClaw Log Search: 一站式系统日志查询利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnSia9Y4Ar8NWECk7opNjv8iabXjDw5VicJXm6cBB1ics1GYYTBpkJ65xIIia1UmlSlia5YedkCYj0r0fhURsI7pmFtC0xMY3Vib3vUEU/0?wx_fmt=jpeg)

# HiClaw Log Search: 一站式系统日志查询利器

Nil
Nil

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

# HiClaw Log Search: 一站式系统日志查询利器

在复杂的微服务架构中，日志排查是开发和运维工作中最耗时的环节之一。当系统出现异常，我们需要在多个组件、多个日志文件之间来回切换，效率极低。

今天给大家介绍一个开源工具——HiClaw Log Search，专为 HiClaw 系统设计的日志查询服务，让你轻松掌控 12+ 组件的日志流。

## 项目背景

HiClaw 是一个企业级 AI Agent 协作平台，由 Manager 容器和多个 Worker 容器构成。系统运行时会产生大量分散的日志：

• Higress 网关日志

• Matrix 服务器日志

• MinIO 存储日志

• Manager Agent 日志

• 各类 Worker 日志

传统的日志查看方式需要 SSH 到服务器，手动 `tail -f` 多个文件，既繁琐又低效。

HiClaw Log Search 应运而生——一个轻量级的 Web UI，让日志查询变得简单高效。

## 核心功能

### 🔍 多组件日志查询

支持 12+ 个系统组件，一站式查看所有日志：

| 组件 | 说明 |
| --- | --- |
| higress-gateway | Higress 网关日志 |
| higress-controller | Higress 控制器日志 |
| higress-pilot | Higress Pilot 日志 |
| higress-console | Higress 控制台日志 |
| higress-apiserver | Higress API Server 日志 |
| manager-agent | Manager Agent 日志 |
| mc-mirror | MinIO 同步日志 |
| minio | MinIO 服务日志 |
| tuwunel | Matrix 服务器日志 |
| nginx-access | Nginx 访问日志 |
| nginx-error | Nginx 错误日志 |
| supervisord | Supervisor 日志 |

### 🎨 日志级别过滤

快速定位问题，支持按级别筛选：

• ERROR - 错误日志，优先排查

• WARN - 警告日志，潜在问题

• INFO - 信息日志，运行状态

• DEBUG - 调试日志，详细信息

### 🔎 关键词搜索

实时搜索日志内容，快速定位关键信息：

• 搜索错误关键词：`timeout`、`failed`、`exception`

• 搜索请求 ID：追踪完整请求链路

• 搜索时间戳：定位特定时间段的日志

### 🔄 自动刷新

3 秒自动刷新，实时监控日志流，无需手动刷新页面。

### 🌙 深色主题

专为开发者设计的深色 UI，长时间查看不伤眼。

## 技术亮点

### 零依赖后端

后端使用 Node.js 原生 HTTP 模块，无需安装任何 npm 依赖：

// 启动服务
node server.js

启动速度快，资源占用低，适合在生产环境长期运行。

### 响应式前端

前端使用 HTML + Tailwind CSS 构建：

• 响应式布局，适配各种屏幕

• 深色主题，护眼设计

• 流畅的交互体验

### 网关集成

支持 Nginx 和 Higress 网关路由：

http://<ip>:18080/log-search/

可无缝集成到现有的 HiClaw 管理界面。

## 快速部署

### 1. 克隆项目

git clone https://github.com/nillikechatchat/hiclaw-log-search.git
cd hiclaw-log-search

### 2. 安装服务

./scripts/install.sh /opt/log-search

### 3. 配置 Nginx

cp skill/nginx.conf /etc/nginx/conf.d/log-search.conf
nginx -s reload

### 4. 配置 Higress 路由（可选）

./scripts/setup-higress.sh

### 5. 访问界面

打开浏览器访问：

http://<your-ip>:18080/log-search/

## REST API

除了 Web UI，还提供 REST API 供程序调用：

### 健康检查

GET /log-search/api/health
# 响应: {"status": "ok", "time": "2024-03-24T14:00:00.000Z"}

### 获取组件列表

GET /log-search/api/components
# 响应: {"components": [...]}

### 查询日志

GET /log-search/api/logs?component=higress-gateway&lines=200&level=ERROR&search=timeout

参数说明：

• `component` - 组件 ID（必填）

• `lines` - 返回行数（默认 200，最大 1000）

• `level` - 日志级别过滤

• `search` - 关键词搜索

## 自定义配置

日志文件路径可在 `skill/server.js` 中修改：

const COMPONENTS = {
  "higress-gateway": {
    name: "Higress Gateway",
    file: "/var/log/hiclaw/higress-gateway.log"
  },
  // 添加你的自定义组件...
};

## 开源信息

• GitHub : https://github.com/nillikechatchat/hiclaw-log-search

• License : MIT

• 技术栈 : Node.js + HTML + Tailwind CSS

---

## 总结

HiClaw Log Search 是一个轻量、实用的日志查询工具，主要特点：

✅ 支持 12+ 组件日志查询
✅ 日志级别快速过滤
✅ 关键词实时搜索
✅ 3 秒自动刷新
✅ 深色主题护眼 UI
✅ 零依赖，启动快

如果你也在使用 HiClaw 或类似的微服务架构，不妨试试这个工具，让日志排查变得更高效！

欢迎 Star ⭐ 和 PR！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

爱唠叨的Nil

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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