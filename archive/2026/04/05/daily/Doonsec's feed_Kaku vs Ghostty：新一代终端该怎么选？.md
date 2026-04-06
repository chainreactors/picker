---
title: Kaku vs Ghostty：新一代终端该怎么选？
url: https://mp.weixin.qq.com/s/HZthjI-t1bsetQYreAu24g
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:58.553468
---

# Kaku vs Ghostty：新一代终端该怎么选？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BowImrBK4tLEUqFiazEDKiaAIxE4gdHZAqwtJ9lca7KOhHber7oFhQFMQzJlKibtYJA9PIwYsqtbwt9VY1PCFd99ruoibtjIg2kxN3W34kwIqFs/0?wx_fmt=jpeg)

# Kaku vs Ghostty：新一代终端该怎么选？

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器中沉浸阅读

> 最近两款终端工具一直在纠正选择哪个，对于我来说，有新的神器一定要尝试下的原则，终端又是日常使用最频繁的，从iterm2到warp，ghostty，Kitty等等，最近由于mole工具关注到了tw93，发现他也有个终端工具。

---

## 01 / 两款终端，两种思路

最近终端圈也因为这个挺热闹，先是 Ghostty 1.0 正式发布引爆社区，后有基于 WezTerm 的 Kaku 异军突起，主打 AI 原生体验。

很多人问我：这俩到底选哪个？

其实答案很简单：**它们从根上就是两种产品**。

### Ghostty：极致性能的通用终端

Ghostty 是用 Zig 语言从零写的跨平台终端，目标就是做「最快的终端」。

* • **核心卖点**：GPU 加速渲染，启动时间不到 100ms，内存占用极低
* • **技术架构**：客户端/服务器分离架构，流畅不卡顿
* • **平台支持**：macOS + Linux，追求原生 UI 体验
* • **开源免费**：完全开源，无闭板云服务，隐私友好

Ghostty 打的是传统终端（iTerm2、Konsole）的市场，用现代技术重新做一遍，把性能拉满。

### Kaku：AI 原生的场景化终端

Kaku 不是从零造轮子，它基于 WezTerm 做二次开发，主打 **AI Coding 场景优化**。

* • **核心卖点**：开箱即用的多任务协作，Agent 并行支持，AI 开发流天然适配
* • **技术架构**：基于 WezTerm（Rust + Lua），底层成熟稳定
* • **平台支持**：目前主要面向 macOS 用户
* • **设计哲学**：不纠结底层性能，专注产品层体验优化

Kaku 切入的是「AI 编程」这个新场景，把多终端、多 Agent 协作这些刚需提前做好了。

## 02 / 核心维度对比

我们来直接对比下关键特性：

| 对比维度 | Kaku | Ghostty |
| --- | --- | --- |
| **开发语言** | 基于 WezTerm (Rust) | 纯 Zig 从零开发 |
| **核心定位** | AI Coding 场景化终端 | 通用高性能终端 |
| **跨平台** | macOS 优先 | macOS + Linux |
| **GPU 加速** | ✅ (继承自 WezTerm) | ✅ (原生深度优化) |
| **启动速度** | 快 | 更快 |
| **AI 协作优化** | ✅ 原生支持 | 需要自行配置 |
| **开箱即用** | ✅ 预设配置完整体验 | 需要手动调教 |
| **社区生态** | 新兴 | 已经火爆 |

### 性能到底差多少？

根据第三方测试，Ghostty 在启动速度和渲染性能上确实略胜一筹，毕竟是全新架构。

但 Kaku 基于 WezTerm，性能也不差——**日常使用感知不到区别**。

真正的差距不在性能，而在**定位**。

## 03 / 到底该选谁？

一句话结论：

* • **如果你主要用终端写代码，日常需要和多个 AI Agent 协作** → 选 **Kaku**
* • **如果你追求极致流畅，就是想要一个更快的通用终端** → 选 **Ghostty**

### 适合 Kaku 的同学

* • 每天用 Cursor、Windsurf 这类 AI 编辑器
* • 需要同时开多个终端会话处理不同任务
* • 喜欢开箱即用，不想自己折腾 WezTerm 配置
* • macOS 用户，对 AI 工作流有强需求

### 适合 Ghostty 的同学

* • 对终端性能有极致追求，感官党
* • 想要替换老旧的 iTerm2/ GNOME Terminal
* • 喜欢折腾配置，自己定制工作流
* • 重视隐私，拒绝云同步数据

> 💡 **我的使用方式**：Ghostty 当主力终端跑日常命令，Kaku 专门开给 AI 编码会话，场景分开用最舒服。

## 04 / 总结

Kaku 和 Ghostty 不是谁取代谁的关系，它们代表了新一代终端的两个发展方向：

* • **一条路**：用新技术重构传统终端，把性能体验拉满（Ghostty）
* • **另一条路**：基于现有成熟底层，针对新场景做产品层优化（Kaku）

没有绝对的好坏，只有适合不适合。

如果你和我一样，一半时间传统编码，一半时间 AI 协作——其实可以都装，按场景切换使用。

**👇 关注我，获取更多工具选择干货**

---

##

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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