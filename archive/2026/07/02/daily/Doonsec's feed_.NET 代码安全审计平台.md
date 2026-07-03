---
title: .NET 代码安全审计平台
url: https://mp.weixin.qq.com/s/kvm9w53GYikZ4DH7Gk5n2Q
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:37.710419
---

# .NET 代码安全审计平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aKMWaIAibDdxq1G0fYpFxibzPJ2gOuc6FpfwznRHjnf4Pgib6RTTR8hKKU28zHXuD9J1ACz8h6dlMLRA9Q8hMibSpvVTq03mMneKf6j2y9P0xtY/0?wx_fmt=jpeg)

# .NET 代码安全审计平台

原创

wulala520
wulala520

wulala520

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# .NET 代码安全审计平台 · v2.0

靛蓝主题 · 毛玻璃质感 · Light/Dark 双模式

2026 年 7 月 2 日更新

因为之前的UI实在太丑了，因此，对**.NET 代码安全审计平台**的前端进行了一次彻底的视觉升级。告别 shadcn/ui 默认的灰黑色调，换上了专业企业级的**靛蓝主题**，搭配**毛玻璃质感**、**明暗双模式**和**响应式三断点布局**。地址：https://github.com/ZMR0zhangmouren/DOT.NET-Code-Security-Audit-Platform/tree/main

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aKMWaIAibDdyhzTZsXSXFX6f8aYp78NiakCnbr5jfFllFrzg2SoKeAJcNPSiaAwpnLXP6vicQ2phonicDvuagwv1X8ubcG0E7vVNFNt55G5cnlzI/640?wx_fmt=gif&from=appmsg)

## 🎨 设计体系

|  |  |
| --- | --- |
| 主色调  靛蓝 Indigo  243 75% 59% | 字体  Inter + JetBrains Mono  正文 / 代码 |
| 语义色 · Severity | 语义色 · Status |

## ✨ 毛玻璃 + 三区布局

三档毛玻璃（Glassmorphism）

|  |  |  |
| --- | --- | --- |
| `glass-surface` | blur 16px | 侧边栏 / Header |
| `glass-card` | blur 10px | 内容卡片 |
| `glass-popover` | blur 8px | 弹窗 / 下拉 |

响应式三断点布局

|  |  |  |
| --- | --- | --- |
| 🖥️ Desktop | ≥ 1024px | 完整侧边栏 可折叠 |
| 💻 Tablet | 768-1023px | 图标模式 自动折叠 |
| 📱 Mobile | < 768px | Overlay 抽屉 + 遮罩 |

## 🧩 组件体系

SeverityBadgeStatusBadgeStatCardPageHeaderEmptyStateThemeToggleTopBarSidebarGlass Cards

9 个自研业务组件 + 15 个 shadcn/ui 组件

## 📄 页面全景（13 → 17 页）

|  |  |
| --- | --- |
| 🔄 重构页面 | 🆕 新增页面 |
| 登录页 · Dashboard · 项目列表 | 漏洞实例列表（/scans/.../:vulns） |
| 项目详情 · 扫描详情 · 报告页 | 漏洞实例详情（/scans/.../:vulnId） |
| Agent Trace · Scan Diff | 跨版本漏洞对比（/vuln-library/compare） |
| 漏洞库 · 设置 · 用户管理 | 审计日志（/admin/audit-log） |
| 系统配置 · VulnLibrary 详情 | React.lazy 代码分割 |

## 🔒 安全加固 + 性能优化

HttpOnly Cookie

accessToken 存内存
refreshToken 走 Cookie
静默刷新 + 轮换 + 吊销

代码分割

React.lazy 17 页面
Suspense 骨架屏
ErrorBoundary 容错

AuthGuard

未登录自动跳转
localStorage 凭据检测
双重校验机制

Bug 修复

lazy() 不可在 render 内调用
路由切换失效根因
登录守卫缺失

## 📊 质量门禁

58

Web 测试全过

464

全量测试通过

17

页面组件化

15

次 Commit

✅ TypeScript 全绿 · ✅ ESLint 0 错误 · ✅ Prettier 干净
✅ Light / Dark 双模式 · ✅ Desktop / Tablet / Mobile 响应式

## 🔗 开源仓库

GitHub: DOT.NET-Code-Security-Audit-Platform

由 Claude Code 协助构建 · 2026-07-02

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ueZE1klS6sRheyePOtzUrsEvFrapxAmyuPQ9u1uCyHJibZI8FyCrk5c7Hx1gd9AAu2gcUGvS9g7mlQaic5oM8FWA/0?wx_fmt=png)

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