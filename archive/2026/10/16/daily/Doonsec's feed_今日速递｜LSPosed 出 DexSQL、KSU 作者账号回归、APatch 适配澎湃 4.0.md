---
title: 今日速递｜LSPosed 出 DexSQL、KSU 作者账号回归、APatch 适配澎湃 4.0
url: https://mp.weixin.qq.com/s/2Odbxmo5LE8d7n7aK_FM0g
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:35:31.936194
---

# 今日速递｜LSPosed 出 DexSQL、KSU 作者账号回归、APatch 适配澎湃 4.0

# 今日速递｜LSPosed 出 DexSQL、KSU 作者账号回归、APatch 适配澎湃 4.0

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

各位工友早。今天工地回到老本行：LSPosed 团队拿出一个用 SQL 查 APK 的新工具，KernelSU / LSPosed 作者的 GitHub 账号回来了，APatch、SukiSU、Zygisk Next 同一天更新；iOS 这边，AI 逆向 IDE Eleven 一天发两版，免越狱调试工具 StikDebug 也在修连接问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OoI9czGaCkQrwZNBiaibWNdeBTGFCaE3nKaBenaK7zDiaHVvKicZuI4Iw1iamfsXWdvZyRqVfib175n909n8jqzKGVBaXP8eBU5e96XvCjdUptaCI/640?wx_fmt=png&from=appmsg)

今日速递

### 1. LSPosed 团队发布 DexSQL：用 SQL 查 APK 和 DEX

北京时间 10 月 15 日 09:01，LSPosed 组织在 GitHub 发布 DexSQL v0.1.0（首个版本）。它不做反编译渲染，而是把 APK / DEX 里的类、方法、字符串和调用关系变成可以用 SQL 查询的数据：比如「找出引用某条日志字符串的方法，再列出它的两层调用者」。

它自带 MCP 服务，可以直接接到 Claude Code、Codex 这类 Agent 上，也能当命令行工具用；APK 在本地解析，不改原文件。官方 README 里用约 372 MiB 的 QQ 9.3.55 安装包，和 JADX、JADX-MCP 等工具比了启动和查询速度。

**工地点评**：做安卓逆向时最费时间的往往是「在几万个类里找到那一个」。DexSQL 走的是「先查询、再看代码」的路线，适合和 jadx 搭配用。目前只有预编译二进制，许可证写的是自定义条款，商用前先看 LICENSE。

GitHub https://github.com/LSPosed/dexsql-release Release https://github.com/LSPosed/dexsql-release/releases/tag/v0.1.0 文档 https://dexsql.lsposed.org/docs

### 2. 【新进展】KernelSU / LSPosed 作者的 GitHub 账号恢复了，模块仓库组织还没回来

昨天我们写过 @realnullptr（Dr-TSNG）的 GitHub 账号被封近一个月。新进展：他在北京时间 10 月 15 日 08:52 发帖说个人账号已经恢复，但 GitHub 仍没有给任何回复，受影响的组织当时对外还不可见。8 分钟后（09:00），他名下的 Zygisk Next 就发了 v1.5.2，修复部分系统上应用崩溃的问题。

我们今早 9:55 用 GitHub API 复查：Dr-TSNG 账号、Kernel-SU、libxposed、LSPosed 三个组织都能正常访问，KernelSU-Module-Repo（模块仓库）仍返回 404。此前 iOS 侧的 LiveContainer 也在 14 日宣布仓库恢复。

**提醒**：模块仓库没恢复期间，别从来路不明的镜像站下 KernelSU 模块，优先认准作者本人的 GitHub Release 和 SHA256。

@realnullptr https://x.com/realnullptr/status/2110534187170349474 ZygiskNext https://github.com/Dr-TSNG/ZygiskNext/releases/tag/v1.5.2 LiveContainer https://x.com/khanhduytran0/status/2110199606156144937

### 3. APatch 11282 提前适配澎湃 4.0，SukiSU Ultra 4.2.1 同日更新

北京时间 10 月 15 日 16:18，APatch 发布 11282，说明里写明这是为新机内核提前发出的版本：适配最新澎湃 4.0 内核，但部分内核上 SELinux 隐藏和 KPM（内核模块）适配仍有问题；同时修了 KPM 安装/卸载状态不一致、包配置修改崩溃等问题。

3 分钟前（16:15），KernelSU 分支 SukiSU Ultra 发布 v4.2.1：管理器换了新的 Material 界面，能识别 Zygisk Next 1.5.0+ 的 zn-daemon 进程，重新支持 Android 8–11，并同步了上游 KernelSU 的「开机时屏蔽内核模块且不会第一阶段卡死」等改动。

**工地点评**：澎湃 / HyperOS 新机用户可以关注 APatch，但这版官方自己都说是「提前发布」，主力机先观望。两个工具都只在自己的设备上折腾，刷之前备份 boot / init\_boot。

APatch https://github.com/bmax121/APatch/releases/tag/11282 SukiSU https://github.com/SukiSU-Ultra/SukiSU-Ultra/releases/tag/v4.2.1

### 4. Eleven：开源 AI 逆向 IDE，能开 Mac / iOS 二进制和 APK

昨天我们写过 REA（把 Ghidra、IDA 接给 AI 的 MCP 桥）。Eleven 是这周冒出来的「图形界面版」：作者 @chiziaruhoma 13 日晚发布，北京时间 10 月 15 日 16:08 和 17:14 连发 v0.1.5、v0.1.6，GitHub 约 480 星，Apache-2.0 开源。

它能打开 Mach-O（Mac / iOS）、ELF、PE 二进制和 Android APK（含 .xapk / .apks），原生代码通过 REA 调 Ghidra 或用 Rizin 读，安卓用 jadx，装了 apktool 还能看 smali。Agent（Claude、Codex、Gemini、Cursor 等）给出的重命名和补丁都以「建议卡片」形式出现，由你接受或拒绝；补丁只写到副本，不改原文件，还支持两个版本对比和 LLDB 调试。

**注意**：macOS 版目前没有公证，安装脚本会帮你清掉隔离属性，装之前最好先看一眼脚本。只拿来分析自己的程序或公开的学习样本，别碰别人的商业软件。

GitHub https://github.com/Zfinix/eleven 发布帖 https://x.com/chiziaruhoma/status/2110035757691703722 中文介绍 https://x.com/qwerty\_\_cs/status/2110655118282781161

### 5. StikDebug 3.1.15：免越狱的 iOS 设备端调试器继续修连接

北京时间 10 月 15 日 22:31，StikDebug 发布 3.1.15，尝试修复 ServiceNotFound 报错并加了调试输出；12 日的 3.1.14 加入了对 Husk（在 iPhone 上跑部分安卓 APK 的实验项目）的支持。

StikDebug 基于 idevice，在 iOS 17.4 及以上给带 get-task-allow 的侧载应用开 JIT，还能看实时日志、进程列表、模拟定位，首次配对后不再需要电脑。iOS 26 上可用，但要应用开发者适配。它已不在 App Store 上架，只走官方 AltSource 或 GitHub 的 .ipa。

**和咱们有关的一点**：没越狱的新 iPhone 想学 iOS 调试和动态分析，这类「配对文件 + 本地 VPN」的路线是现在的主流选择，比等越狱现实。

https://github.com/StikDebug/StikDebug/releases/tag/3.1.15

---

工具箱补充

和今天新闻相关的工具，版本信息截至北京时间 10 月 16 日 09:55，以官方页面为准。

* **DexSQL v0.1.0（安卓静态分析）**

  ：LSPosed 出品，用 SQL 查询 APK / DEX 的类、方法、字符串和调用关系，内置 MCP。提供 Windows x64、Linux x64 / ARM64、macOS 13+（Apple 芯片）单文件程序。刚发首版，没有已知问题清单，查询语法以官方文档为准。
  https://github.com/LSPosed/dexsql-release https://dexsql.lsposed.org/docs
* **Eleven v0.1.6（AI 逆向 IDE）**

  ：Apache-2.0。支持 macOS 14+（Apple 芯片）、Windows x64、Linux x64。0.1.5 加了 Mac 菜单栏和 Agent 完成通知，0.1.4 加了完整的安卓应用读取和 Windows / Linux 版本。已知限制：macOS 版未公证；Android 的 smali 视图需要另装 apktool。
  https://github.com/Zfinix/eleven/releases https://eleven.chizi.app
* **APatch 11282（root）**

  ：基于 KernelPatch 的内核级 root，支持 APM 模块和 KPM 内核模块。只支持 ARM64，内核 3.18–6.12，需要 CONFIG\_KALLSYMS=y。已知问题（官方写明）：部分内核 SELinux 隐藏有问题，KPM 适配性仍有问题。SuperKey 权限高于 root，务必用强密码。
  https://github.com/bmax121/APatch/releases/tag/11282 https://apatch.dev
* **SukiSU Ultra v4.2.1（root）**

  ：KernelSU 分支，支持非 GKI 和 GKI 1.0、KPM、内置 susfs 管理。架构支持 arm64-v8a、armeabi-v7a（基础）和部分 x86\_64；用 KPM 需要 CONFIG\_KPM=y。本版修了 Android 8–11 上管理器无法运行的问题。
  https://github.com/SukiSU-Ultra/SukiSU-Ultra/releases/tag/v4.2.1 https://sukisu.org
* **Zygisk Next v1.5.2（root 配套）**

  ：给 KernelSU 提供 Zygisk API，也可替代 Magisk 自带 Zygisk。要求 KernelSU 10940+ / ksud 11575+，或 Magisk 26402+ 且关闭内置 Zygisk；不能同时装多个 root 方案。注意：自 v4-0.9.2 起不再是 GPL，禁止修改和再分发。
  https://github.com/Dr-TSNG/ZygiskNext/releases/tag/v1.5.2
* **Magisk v31.0（root，GitHub 标为预发布）**

  ：9 月 4 日发布：App 用 Jetpack Compose 重写，内置终端，可直接从 OTA 链接提取 boot 镜像，Zygisk 支持 Android 17。最新正式版仍是 v30.7。issue 区有小米 14 上 preinit 软链接失败的报告。新版界面有问题可先用 legacy 版。
  https://github.com/topjohnwu/Magisk/releases/tag/v31.0
* **Dopamine 3.0.11（iOS 越狱）**

  ：rootless 半不完美越狱。支持范围：arm64e 为 iOS 15.0–17.3.1；A12 / A13 为 iOS 15.0–18.7.1 和 26.0–26.0.1；arm64 为 iOS 15.0–18.7.1。15 日之后没有新版本；3.0.11 修了 iOS 26.0 beta 1 支持和开机 logo 卡屏。只从官方渠道下载。
  https://github.com/opa334/Dopamine/releases https://ellekit.space/dopamine/
* **palera1n v2.4 / v3.0.0-beta.2（iOS 越狱）**

  ：基于 checkm8 硬件漏洞，只支持 A8–A11 设备（iPhone 6s 到 iPhone X 等）和部分 T2 Mac，iOS / iPadOS / tvOS 15.0 及以上，需要 macOS 或 Linux 电脑。正式版仍是 v2.4（7 月），3.0 测试版加了图形界面里从 DFU / PongoOS 启动。已知限制：A11 设备越狱状态下必须关闭锁屏密码。
  https://github.com/palera1n/palera1n/releases https://palera.in
* **StikDebug 3.1.15（iOS 调试）**

  ：iOS 17.4–18.x 完整支持，26.0+ 可用但要应用适配，17.3 及以下不支持。需要配对文件、SideStore / AltStore 和本地回环 VPN（如 LocalDevVPN）。
  https://github.com/StikDebug/StikDebug

安全帽提醒：本号只聊公开发布的版本、功能和学习思路，不提供攻击步骤、exploit 或绕过教程，也不涉及盗版破解。逆向工具只用来分析自己的程序或公开学习样本；越狱和 root 请只在自己的设备上折腾，风险自担。

收工。想看哪个工具的上手实测（DexSQL / Eleven / APatch 澎湃 4.0）？留言告诉我，周末排期。

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