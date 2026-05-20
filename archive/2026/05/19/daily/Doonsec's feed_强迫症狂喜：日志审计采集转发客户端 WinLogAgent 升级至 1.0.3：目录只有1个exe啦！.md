---
title: 强迫症狂喜：日志审计采集转发客户端 WinLogAgent 升级至 1.0.3：目录只有1个exe啦！
url: https://mp.weixin.qq.com/s/ICUKSjNP0E6C6EF5LQpkXQ
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:00:05.636562
---

# 强迫症狂喜：日志审计采集转发客户端 WinLogAgent 升级至 1.0.3：目录只有1个exe啦！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Q71mAqQaURP7rngRicw2z2cexibs817Ewpd437yHLPWrX50UjwbiaphOo3BROiamdkWkuCSDswrrR8KGTiabGicSEaOh4ST6TR2hexAnStqibFlzFs/0?wx_fmt=jpeg)

# 强迫症狂喜：日志审计采集转发客户端 WinLogAgent 升级至 1.0.3：目录只有1个exe啦！

原创

张百川
张百川

游侠安全网

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WinLogAgent 是一款永久免费的 Windows 日志采集与转发客户端。它支持图形化采集系统、应用、安全三类日志，告别手动修改 YAML/XML 配置文件的繁琐操作。界面现代漂亮，内置仪表盘实时监控事件速率与错误率。可一键转发至 GreenLogAudit、福瑞日志审计或任意 SOC/SIEM（支持 Syslog/HTTP 等协议）。资源占用低，完全免费。

![](https://mmbiz.qpic.cn/mmbiz_png/Q71mAqQaUROU0mMThvt7lOjtuXJjHibvcZKianfV8U2ia2KwRjxG17uvxN6ctOFyCfCya7gWGKr7UWExF5CvffcDJHwz7icIFMOibvDk0tV876Fw/640?wx_fmt=png&from=appmsg)

发布日期：2026-05-17

**适用版本：v1.0.3**

**下载地址：https://github.com/youxia029/WinLogAgent/releases/**

---

### 🎉 这次升级，可能是你见过最“干净”的日志客户端

如果你之前被 WinLogAgent 1.0.2 的 UI 白屏问题困扰过，或者嫌目录里文件太多、看着心烦——

**1.0.3 版本就是为你准备的。**

这不是一次小修小补，而是一次 **“洁癖式重构”**。

---

### ✨ 1.0.3 升级亮点

#### 1️⃣ 解决 UI 显示异常（WebView 某些场景下白屏、空白仪表盘）

* 修复了部分环境下（尤其是 Windows Server 2022、某些精简版系统）仪表盘加载失败、显示空白的问题。
* 现在打开软件，**事件总数、速率趋势图、最近事件列表** 统统秒出，不再“等了个寂寞”。

#### 2️⃣ 目录结构极度简化 —— 强迫症狂喜

旧版本可能有一堆 DLL、配置文件、依赖库，看着头大。

**1.0.3 整个目录只剩下 4 个东西：**

![](https://mmbiz.qpic.cn/mmbiz_png/Q71mAqQaURNc4EfWUsOt15X741MAmVkdYuzuM9h2vpMTPODzFB5Ej0y3MNiahaSoCMZFtISSDkl4tcISDRjYMCK3bicm5HPicXjicn2fZIsTlUQ/640?wx_fmt=png&from=appmsg)

没有多余的 `.dll`、没有乱七八糟的缓存文件夹，**清爽得像一张白纸**。

#### 3️⃣ 一个 exe 走天下，杜绝“点错程序”的尴尬

* 以前有一堆文件，.dll 和 .json等，你得去找 `WinLogAgent.exe`。
* 现在**只有一个可执行文件**：`WinLogAgent.exe`。以管理员权限打开它，一切开始。
* 安装服务、开机自启、日志采集……全部由这个 exe 统一管理，**再也不会误操作**。

#### 4️⃣ 保持所有核心功能，稳定如初

* 依然支持采集 `System`、`Application`、`Security` 日志（安全日志需管理员权限）
* 依然支持 `UDP`/`TCP`/`TLS`/`HTTP(S)` 转发
* 依然支持 `RFC3164`、`RFC5424`、自定义 Headers、JSON 格式
* 依然支持“当前用户”开机自启和 Windows 服务模式
* 依然可以一键转发至 **GreenLogAudit**、**福瑞多源平台** 或任何 SOC/SIEM

---

### 📦 本次发布的包

**“标准版”和“离线版”** —— 如果是在内网，建议下载 WinLogAgent-v1.0.3-win-x64-webview2fixed.zip ，因为有 MicrosoftEdgeWebView2RuntimeInstallerX64.exe 运行环境，如果在互联网机器，那么直接下载更简洁的 WinLogAgent-v1.0.3-win-x64.zip 即可。

---

### 📥 WinLogAgent下载

* **GitHub Release 主页**：https://github.com/youxia029/WinLogAgent/releases
* **直接下载 1.0.3**：https://github.com/youxia029/WinLogAgent/releases/tag/v1.0.3
* **项目主页**：https://github.com/youxia029/WinLogAgent

---

### 🙏 最后说两句

WinLogAgent 依然**永久免费**，不藏收费陷阱，不开会员。

我们希望做一个 **“打开就能用、用了就回不去”** 的 Windows 日志客户端。

如果你觉得好用，请给 GitHub 项目点个 ⭐️

如果你遇到问题，请邮件 baichuan.zhang@foxmail.com 我们会认真对待每一个反馈。

**让日志采集，回归简单。**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bgkwFOXObJpyJMF6qbW4AlsQrwQUrZ6nIvql5pwiciaiatSSWcKc7qKIRDsy7baaScKe4VpVibesiaJ66FbOzCmdx4g/0?wx_fmt=png)

游侠安全网

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bgkwFOXObJpyJMF6qbW4AlsQrwQUrZ6nIvql5pwiciaiatSSWcKc7qKIRDsy7baaScKe4VpVibesiaJ66FbOzCmdx4g/0?wx_fmt=png)

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