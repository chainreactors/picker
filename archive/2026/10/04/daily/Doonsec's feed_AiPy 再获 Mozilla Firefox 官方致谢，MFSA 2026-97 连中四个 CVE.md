---
title: AiPy 再获 Mozilla Firefox 官方致谢，MFSA 2026-97 连中四个 CVE
url: https://mp.weixin.qq.com/s/__ix_iMaDlKLwwl7HoAKNg
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:53:34.956658
---

# AiPy 再获 Mozilla Firefox 官方致谢，MFSA 2026-97 连中四个 CVE

# AiPy 再获 Mozilla Firefox 官方致谢，MFSA 2026-97 连中四个 CVE

原创

知道创宇
知道创宇

知道创宇

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AI智赋未来 · 安全守护信息化

近日，Mozilla 发布安全公告 **MFSA 2026-97**（2026 年 9 月 29 日），修复了 Firefox 157 中的多个安全漏洞。知道创宇自研开源 AI Agent 产品 AiPy（章鱼哥）在本次公告中获得 **4 个 CVE 编号**，其中 2 个为 high 级别。

这是 AiPy 在 Firefox 安全研究中获得的又一次官方认可。从 MFSA 2026-74 的 5 个 CVE、MFSA 2026-82 的 2 个 CVE，到本次 MFSA 2026-97 的 4 个 CVE，AiPy 在 Gecko 引擎中的安全研究已经形成稳定、持续的产出节奏。

01

四项漏洞：覆盖音视频、布局与 WebGPU

本次 AiPy 发现的四个 CVE 分布在 Firefox 的三个不同子系统中：

CVE-2026-100783：Audio/Video 组件未初始化内存

组件：Audio/Video

影响等级：**high**

描述：音频/视频处理模块中的未初始化内存问题

参考：Bug 2069804

音视频模块负责媒体流的解码、渲染与同步，是浏览器中处理外部数据最密集的模块之一。未初始化内存问题可能导致程序读取到未定义的数据，在特定条件下可能被利用来泄露内存内容或影响程序控制流。

CVE-2026-100784：Layout: Text and Fonts 组件 Use-after-free

组件：Layout: Text and Fonts

影响等级：**high**

描述：文本与字体布局模块中的释放后使用问题

参考：Bug 2070264

文本与字体布局是浏览器渲染引擎的核心环节，涉及复杂的字体解析、文本排版与内存对象生命周期管理。Use-after-free 属于内存安全类中的高危缺陷，攻击者若能控制释放后的内存内容，可能实现任意代码执行。

CVE-2026-100799：Graphics: WebGPU 组件未初始化内存

组件：Graphics: WebGPU

影响等级：**moderate**

描述：WebGPU 图形渲染模块中的未初始化内存问题

参考：Bug 2056217

CVE-2026-100802：Graphics: WebGPU 组件未初始化内存

组件：Graphics: WebGPU

影响等级：**moderate**

描述：WebGPU 图形渲染模块中的未初始化内存问题

参考：Bug 2057833

WebGPU 是新一代 Web 图形与计算标准，允许网页直接访问 GPU 能力。该模块涉及 GPU 内存分配、缓冲区管理与跨进程数据传输，内存管理复杂度较高。本次在两个不同的 Bug 中均发现未初始化内存问题，说明该模块的内存初始化流程存在需要系统性梳理的环节。

02

从内存安全切入：Firefox 研究的技术纵深

本次四个 CVE 中，三个属于“未初始化内存”问题，一个属于 use-after-free。这两类缺陷同属内存安全范畴，也是浏览器引擎中最具利用价值、同时最难以通过常规测试发现的漏洞类型。

未初始化内存问题通常源于内存分配后未正确清零，程序在后续使用中读取到了残留数据。这类问题在正常功能测试中往往不会暴露，需要针对性的内存分析手段才能触发。而 use-after-free 则涉及对象生命周期的精确管理，往往需要构造特定的时序条件才能复现。

在 Firefox 这样经过多年高强度审计的代码库中，能够持续发现此类缺陷，说明 AiPy 的分析并不停留在代码模式匹配层面，而是能够深入理解对象生命周期与内存状态流转。

03

持续深耕，跨平台战绩持续积累

从 Mozilla Firefox 的多轮致谢，到 F5 NGINX 的堆缓冲区溢出、OpenVPN 的四连击、PostgreSQL 18.6 的六项 CVE、Google Chrome 的高危漏洞、QEMU 的虚拟化缺陷，以及 Apple macOS 的两次官方致谢——AiPy 已经横跨浏览器、应用交付、VPN、数据库、虚拟化平台和操作系统等多个关键领域。

每一次致谢背后，都是真实的技术产出。具备安全基因的 AI Agent，正在实战中持续证明自己的价值。

知道创宇将继续推动**可信 AI 技术**与**安全能力**的深度融合，以自主可控的 AI 安全方案，为更多关键基础设施组件和底层系统安全提供保障，致力于成为各行业、全场景可信赖的**AI 安全伙伴**。

参考资料

https://www.mozilla.org/en-US/security/advisories/mfsa2026-97/（点击“阅读原文”可跳转查看）

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdgEibMcFiamrCzHlWTqmZF2GaPXS4Zz6YQjpF0dymHF6kmomjo3CnKITtEic9QXWIqLpZWOxuf73sdPXkxxI1xyFw2jYvpAdBUgd4/640?from=appmsg)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oan15mBs7fOYe1ETMicrrK5eEreO2UU1sxFQL4Eebn6tthroecicEQrsbZ8qRzV2xMGpvCyU3lWjJwASBPD5QpBg/0?wx_fmt=png)

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