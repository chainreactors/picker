---
title: TLDW 开源 AI 工具：把 1 小时 YouTube 长视频压缩成 5 分钟的结构化学习笔记
url: https://blog.upx8.com/4901
source: 黑海洋 - Wiki
date: 2025-11-22
fetch_date: 2025-11-23T03:26:59.810982
---

# TLDW 开源 AI 工具：把 1 小时 YouTube 长视频压缩成 5 分钟的结构化学习笔记

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# TLDW 开源 AI 工具：把 1 小时 YouTube 长视频压缩成 5 分钟的结构化学习笔记

发布时间:
2025-11-22 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
1941

## TLDW概览

TLDW（Too Long; Didn’t Watch）是一款面向 YouTube 等长视频内容用户的开源工具。只需粘贴视频链接，系统便会基于视频结构、AI 模型与字幕生成“高亮片段”、主题摘要、问题建议与引用摘录，让用户在几分钟内消化原本需耗费数小时观看的内容。

* 在线体验：[https://tldw.us](https://blog.upx8.com/go/aHR0cHM6Ly90bGR3LnVzLw "TLDW 体验地址")
* GitHub：[https://github.com/SamuelZ12/TLDW](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1NhbXVlbFoxMi9UTERX "TLDW GitHub开源地址")

### 能做什么

* 自动生成 **高亮片段**：支持 Smart（质量优先）与 Fast（速度优先）两种模式，可一键连续播放与按主题再生成。
* 并行呈现 **快捷预览、结构化摘要、推荐问题、金句**，快速扫清知识盲区。
* **AI 对话** 基于转录内容检索，返回结构化 JSON 答案，附时间戳与降级兜底策略。
* **转录联动播放器**：句粒度同步，点击即可跳转或一键收录引用。
* **个人笔记工作区**：支持跨视频聚合回顾的 `/all-notes` 面板。
* **登录功能**：保存分析、收藏视频、查看使用上限与偏好同步。匿名与登录用户采用不同的速率限制与缓存策略。

### 适合谁

* 想高效扫完课程、演讲、技术大会视频的学习者与创作者
* 需要做读书笔记式“视频要点卡片”的知识博主、团队培训者
* 希望在编辑台获得时间戳证据与引用片段的剪辑/解说作者

## TLDW核心能力

* **高亮片段与主题生成**：Smart/Fast 模式、主题再生成、Play All 连播。
* **结构化理解**：并行输出摘要、问答、引用金句与快捷预览。
* **可溯源回答**：聊天结果带时间戳与转录证据。
* **笔记与资料库**：按视频与跨视频两种维度管理，支持收藏与快速恢复进度。
* **性能与体验**：Turbopack 加速开发迭代，Aggressive Caching 复用历史分析，后台刷新保障结果新鲜度。
* **安全与可靠性**：CSP/HSTS、CSRF 保护、请求体大小限制、匿名哈希 IP 限流与 Supabase 侧速率限制。

## TLDW使用方式

1. 打开 [https://tldw.us](https://blog.upx8.com/go/aHR0cHM6Ly90bGR3LnVzLw "TLDW 体验地址")，粘贴 YouTube 视频链接。
2. 选择 Smart 或 Fast 模式，生成高亮与摘要。
3. 通过时间戳预览关键片段，必要时与 AI 对话查缺补漏。
4. 将要点写入笔记区，保存或收藏，便于跨视频复盘。
5. 登录后可同步偏好与历史记录；匿名用户会受到更严格的调用限制。

## TLDW技术与架构

* **前端**：Next.js 15 App Router、React 19、TypeScript、Tailwind CSS v4、shadcn/ui、lucide-react、sonner。
* **后端运行时**：Next.js Serverless 路由，结合 withSecurity 中间件（CSRF、输入校验 Zod、速率控制）。
* **AI 管线**：xAI Grok 4 Fast（默认）/ 可选 Google Gemini；提供提供者无关的提示模板、结构化输出、降级与转录分片。
* **转录与元数据**：Supadata 提供转录；轻量 oEmbed 拉取标题与缩略图。
* **持久化与认证**：Supabase（Auth + Postgres）存储 video\_analyses、user\_videos、user\_notes、profiles、rate\_limits。
* **页面与 API**：
  + Pages：`/`、`/analyze/[videoId]`、`/my-videos`、`/all-notes`、`/settings`
  + API：视频摄取（info/transcript/cache/analysis/save/update/link）、生成类（topics/summary/preview/questions/top-quotes）、对话与配额（chat/check-limit）、笔记（notes）、安全（csrf-token）。

## 隐私与安全

项目在全局中间件中加入 CSP/HSTS 头、CSRF 校验与请求体大小限制，并以匿名哈希 IP 与 Supabase 表进行限流与配额区分。

## TLDW在线体验与源码

体验地址：[https://tldw.us](https://blog.upx8.com/go/aHR0cHM6Ly90bGR3LnVzLw "TLDW 体验地址")

GitHub：[https://github.com/SamuelZ12/TLDW](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1NhbXVlbFoxMi9UTERX "TLDW 开源地址")

支持本地开发与自部署：Node.js 18+、配置 XAI/Gemini/Supadata/Supabase 等环境变量，一键 `npm run dev` 启动。

[取消回复](https://blog.upx8.com/4901#respond-post-4901)

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