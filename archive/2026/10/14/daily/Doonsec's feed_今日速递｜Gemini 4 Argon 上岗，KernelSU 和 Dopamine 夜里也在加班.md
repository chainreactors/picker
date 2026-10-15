---
title: 今日速递｜Gemini 4 Argon 上岗，KernelSU 和 Dopamine 夜里也在加班
url: https://mp.weixin.qq.com/s/tYK_sMDO851yiFHMEng8KA
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:25.303459
---

# 今日速递｜Gemini 4 Argon 上岗，KernelSU 和 Dopamine 夜里也在加班

# 今日速递｜Gemini 4 Argon 上岗，KernelSU 和 Dopamine 夜里也在加班

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

各位工友早。今天工地的大动静是 AI 那边进了一台新设备：Google 的 Gemini 4 Argon。逆向这边没有大工程，只有两个老牌项目在夜里悄悄发了维护版。消息不多，但都是官方一手的，咱们一条条看。

今日必看

### 1. Gemini 4 Argon 正式开放

Google DeepMind 10 月 13 日发文，宣布 Gemini 4 Argon 全面开放。开发者可以在 AI Studio 里通过 Gemini API 调用，Google AI Pro/Ultra 订阅用户可以在 Gemini App 和搜索的 AI Mode 里用。官方主打复杂的多步骤任务，覆盖编程、金融、法律、网络安全和科研。首发优惠价是每百万输入 token 2 美元、输出 10 美元，11 月 30 日之后涨到 4 / 20 美元。

**和咱们有关的一点**：官方说 Argon 已经被用来帮防守方找漏洞、打补丁，也开始给更多 Fairwind Program 合作方开放。同一篇文章还说，它对「写 exploit」这类危险请求的拒绝能力比上一代更强，并且公布了提示注入相关的评测数据。简单说就是：能力上去了，安全约束也在加码。

原文 https://deepmind.google/blog/introducing-gemini-4-argon/ 安全篇 https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/

### 2. KernelSU v3.3.1 发布（Android root）

KernelSU 在 GitHub 发布了 v3.3.1，时间是北京时间 10 月 13 日清晨。按 Release 说明，这一版主要是维护和改进：WebView zygote 的 umount 逻辑改成白名单方式；ksud 新增 SIGSYS 处理；fd wrapper 修好了，可以配合 App Profile 使用；新的版本匹配检测机制，外加内核策略相关修复和多语言翻译更新。

**工地点评**：这一版没有大功能，属于给脚手架拧紧螺丝。在用 KernelSU 的工友可以看完 changelog 再决定升不升，刷机前先备份。

https://github.com/tiann/KernelSU/releases/tag/v3.3.1

### 3. Dopamine 3.0.11 发布（iOS 越狱）

opa334 维护的 rootless 越狱工具 Dopamine 发布了 3.0.11，时间也是北京时间 10 月 13 日清晨。官方说明一共三条：修复 iOS 26.0 beta 1 的支持问题（这是 3.0.1 引入的回归）；修复使用开机 logo 时，sbreload 期间画面卡在旧内容上的问题，现在会正常淡出到黑屏；更新 opainject 和 litehook 两个组件。

**工地点评**：这是维护版，不是新的越狱方式，也没有扩大支持范围。设备和系统能不能用，以官方仓库的说明为准，别信那些「全机型一键越狱」的野链接。

https://github.com/opa334/Dopamine/releases/tag/3.0.11

---

也在发生

* **Frida 17.23.3**

  （10 月 9 日，比 3 天稍早，补一条）：.NET 绑定重写成 frida-net，基于 .NET 9，可以跨 Windows、macOS、Linux 使用。官方提醒 API 还不稳定，后续还会改。
  https://frida.re/news/2026/10/09/frida-17-23-3-released/
* **Hugging Face 博客**

  （10 月 13 日）：Liquid AI 介绍了 LFM2.5-24B-A2B，主打在设备端运行、注重隐私的 Agent。
  https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b
* **反编译工具**

  ：最近 3 天 Ghidra、jadx 都没有新 Release（目前分别是 12.1.4 和 1.5.6）。今天这块没有新料，就不硬凑了。

安全帽提醒：本号只聊公开的版本更新和行业动态，不提供破解、绕过他人 App 安全机制的教程。越狱和 root 请只在自己的设备上折腾，风险自担。

收工。明天想看哪个工具的「深度拆解」？留言告诉小瑶，点赞最多的那个，周末上深度。

预览时标签不可点

作者提示: 内容由AI生成

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/X0YzhUXakZTdgicgpttvPuWe7WMkUVTGkbAoMujqeY8loVMQUKYQXjGOxUnkR1NeL5xLd2iaicJicUptoDgd3pdpbg/0?wx_fmt=png)

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