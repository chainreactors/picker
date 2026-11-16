---
title: 今日速递｜看雪 UROV-Z、Liter8 钥匙串、Cursor 扩展被植后门
url: https://mp.weixin.qq.com/s/9ORV6SvTlCibIqAEWznCfg
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:45:52.179372
---

# 今日速递｜看雪 UROV-Z、Liter8 钥匙串、Cursor 扩展被植后门

# 今日速递｜看雪 UROV-Z、Liter8 钥匙串、Cursor 扩展被植后门

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今日速递 · 2026-11-15

各位工友早。今天主线是看雪上新出的安卓用户层内存读取方案 UROV-Z、Liter8 0.3.1 在无 SEP 环境下把钥匙串做起来，以及 Cursor 把 10 月扩展市场缓存被塞进伪造 Claude Code 扩展的调查更新写清楚；昨稿未越狱砸壳、Frida 17.26.3、Project Zero Full 90 等不重复。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OoI9czGaCkTibusxsmamoUc4PaycmfsxOMASOp4fa7p5G1uFQqLVbAgZaV7EgQaAf9BibcmVPa42nUe7Q4q9scM5YBgC3Xoj60vNFvEXjZTO0/640?wx_fmt=jpeg&from=appmsg)

PART 1

## 第一部分｜国内安全厂商 · 安全网站 · 安全论坛热点

本层以看雪窗口内新帖为主（UROV-Z 内存读取覆盖、真机 so 运行容器、脱敏客户端方法论、Unicorn 在 Windows 64 位上的映射问题，以及 BLA 懒人包）。考证、求助和 CTF 入门写题不进主条；昨稿未越狱砸壳、联通登录加密、单指令 CrackMe 等不重复。

## 1. 看雪｜UROV-Z：同一地址上，执行和读取可以看到不同内容

看雪 Android 安全版作者「安卓逆向test」发了一篇长文，标题是《安卓用户层代码段内存读取欺诈方案——UROV-Z》，按抓取时页面的「10 小时前」回推，约发表于 **2026-11-14 22:53**（Asia/Shanghai）。公开论题很具体：调用一个函数，是让处理器去执行那段指令；把同一个地址交给一次内存读取，则是把这些指令当成普通字节取出来。两种操作可以落在同一虚拟地址上，看到的内容却不必相同。作者把方案叫做 UROV-Z，把这种机制称为「读取覆盖」，把提供给读取者的替代内容称为「影像」；并说明它是挂在 KernelPatch 上的 KPM 模块，讨论范围包括注册代码页、处理读取和跟踪映射。正文从概念讲到实现顺序，篇幅很长。本稿只记问题意识和模块定位，不展开页权限或异常处理细节。

来源

```
https://bbs.kanxue.com/thread-293544.htm
```

**工地点评：**可以把它理解成：有人去读这块内存时，拿到的是一份事先准备的「影像」，CPU 真正执行的仍是原来的代码。对想搞清安卓内核模块和内存观察机制的人，这篇值得点开；它不是一份给应用层直接套用的短教程。

## 2. 看雪｜受 unidbg 启发的安卓 so 真机运行容器

同一版块作者 mb\_lxotxkix 发了《根据unidbg的灵感，开发了一个安卓的so库运行容器。》，约发表于 **2026-11-14 15:53**（Asia/Shanghai）。作者写自己用 unidbg 时觉得还不够「开箱即用」：多线程本质是时间切片，反射不好处理，而且经 QEMU 翻译执行，耗时和内存占用都和真机不一样。新项目的定位是**基于真机、非 root** 去加载并调用 so：默认按当前这台真机的环境跑，不做指令翻译；也可以给 so 提供一套虚构环境，再把调用点做成 HTTP 接口。可见部分还列了文件系统和系统属性相关模块、JNI 拦截、ART/Dalvik 模拟等名称。完整正文需回帖可见，页内未见 GitHub 链接。本稿只依据公开介绍写工具定位，不写环境配置，也不把文中提到的具体 so 当成可复现对象。

来源

```
https://bbs.kanxue.com/thread-293537.htm
```

**工地点评：**在真机上跑 so、还能把调用做成接口，对做安卓动态分析、又嫌模拟器环境和速度对不上的人，方向很有吸引力。目前完整实现和仓库都还没公开，先当预告看，不必急着当成品工具来用。

## 3. 看雪｜网易某某老鼠：补环境调试与动调调试长记录

逆向工程版作者「哄鼠杀虫腐」发了《网易某某老鼠逆向记录 —— 补环境调试与动调调试》，约发表于 **2026-11-14 23:53**（Asia/Shanghai），文内整理日期为 2026-11-14。这是一篇已脱敏的长篇方法记录：目标名称、包名、域名、路径和业务标识都做了处理。作者把工作分成并列的两部——「补环境调试」是不挂目标进程，在宿主侧把素材、格式和依赖补齐后离线复算；「动调调试」是挂上进程，取运行时才存在的东西。目录里可以看到 ELF 环境、文件格式、密码学绑定、魔改 Lua VM 等章节名。范围说明写明：不包含漏洞内容、接口清单、PoC，也不包含反作弊对抗或证书校验绕过的可复现流程。本稿只介绍结构和方法论，不复述格式或密码细节。

来源

```
https://bbs.kanxue.com/thread-293545.htm
```

**工地点评：**与其把它当成某款产品的破解手册，不如当成一份「静态怎么补环境、动态怎么观察」的作业笔记。做客户端格式分析和运行时观测的人，看目录和两部划分就值回票价；作者自己也把对抗流程和密钥取值划在范围外了。

## 4. 看雪｜Unicorn 2.1.4 在 Windows 64 位上的 JIT 缓冲区映射问题

茶余饭后版作者 zZhouQing 发了《Unicorn/Qemu在Windows 64位下可能存在的内存映射问题》，约发表于 **2026-11-15 06:53**（Asia/Shanghai）。作者写自己在 Windows 64 位上用 Unicorn 2.1.4 调试混淆样本时遇到 TCG 崩溃：分配 JIT 代码缓冲区时只调用了 `VirtualAlloc(NULL, size, MEM_RESERVE)`，没有限制基址，这块预留内存被分到了过高的地址，触发 x86\_64 TCG 的 32 位相对寻址在 ±2GiB 边界溢出，把字节写到了未映射区域。文中对照了 QEMU 历史上 SPARC64 侧「强制把 code\_gen\_buffer 映到 2GB 以内」的修复思路，并写明 64 位宿主默认缓冲区大小是 1GiB。作者称最终已经修复正常。本稿只写现象和公开成因，不涉及样本本身。

来源

```
https://bbs.kanxue.com/thread-293546.htm
```

**工地点评：**在 Windows 64 位上用 Unicorn 或同类仿真器做去混淆、却突然在 TCG 层崩掉的人，可以先对照这篇的基址和 ±2GiB 限制，再决定要不要给缓冲区换一种分配方式。帖子发在茶余饭后，内容本身是一篇工具链缺陷分析。

## 5. 看雪｜BLA 懒人包，官方同步发了 bla-agents 3.3.2

安全工具版作者 Henglie 发了《【反AI逆向】BLA 程序加固 懒人包 用于对抗AI自动化破解》，约发表于 **2026-11-14 12:53**（Asia/Shanghai）。可见介绍把 BLA 说成开源的 Counter-REA 蓝队向 MCP / CLI「懒人包」，目标是保护作者自己的发布产物、抬高 AI 逆向代理的分析成本，并声称保持运行时等价。完整下载区写「回复或点赞可查看完整内容」，本稿只依据可见介绍和 GitHub。官方仓库随后在 **2026-11-15 02:26:42**（Asia/Shanghai，源 2026-11-14T18:26:42Z）发布了 **bla-agents 3.3.2**。相对昨稿写到的 3.3.1，这一档把可选的 sidecar 纠缠扩展到 SQLite 的 schema 注释（默认关闭），并整理了 REA 内部限额目录；发行说明写测试为 891 passed / 4 skipped，npm 可能未同步发布，目前以 GitHub Release 为准。本稿只写项目定位和窗口内新版本，不写加固或对抗配方。

来源

```
https://bbs.kanxue.com/thread-293536.htm https://github.com/qybaihe/bla/releases/tag/bla-agents-3.3.2
```

**工地点评：**如果你在关注「AI 代理被拿来自动逆向」这件事的防守侧，可以看这个开源项目的定位，以及 3.3.2 相对昨天的小版本差。它不是给攻击者用的配方，点开前先读官方说明和测试口径。

补查：先知窗口内无新帖，11-13 的 WordPress Core 竞争条件分析（CVE-2026-119977）昨已作延伸阅读。安全客窗口内无新稿，首页最新仍是 11-13 对 Grok 应用未授权访问的转述。嘶吼 RSS / 可见稿仍停在 2026-05。Seebug Paper 首页本次为 HTTP 521，RSS 窗口内无新文。FreeBuf 窗口内有 Cursor 调查更新的转述（已作为第三部分主条来源之一），以及一篇 FBI 对 ARTEX 的再预警（ARTEX 本身 11-09 已写过，不进主条）。绿盟、360 Netlab、奇安信 X 实验室窗口内无新研究稿；微步博客 TLS 失败，腾讯玄造候选址 500，长亭博客 TLS 失败。看雪首页最高线程 293546；另有 293535 学历分享和 293540–293542 三连 BUUCTF 入门写题，不进主条。昨稿未越狱砸壳、csc.sys、Neshta 等不重复。今日是周日，国内站点窗口内够得上实质逆向的新帖主要就是上面 5 条，未再硬凑到昨日常规的 7 条。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OoI9czGaCkTZhen9dNo2Via4Xo0YwRbsQQFRdeP1ElqhljVian4Kb4oEZONJn8x3xHT1nib0NlVJUkH361IE638SB3YiaS1DBWnTFpiaeMa14AicQ/640?wx_fmt=jpeg&from=appmsg)

PART 2

## 第二部分｜X 上的二进制 / 安全 / OS 逆向热点 + 越狱工具

本层先写 Liter8 0.3.0 / 0.3.1 和配套的 appstorectl 1.2.0，再跟 WQFiles 从 0.9.6 升到 0.9.8，并补 OpenBin 的一轮界面更新。bla-agents 3.3.2 已写入第一部分第 5 条，这里不再单列。11-09 已介绍过更早的 Liter8，今天只写这两档新版本；WQFiles 昨已写到 0.9.6，今天只跟 0.9.7 / 0.9.8。不要把社区里「A12 已支持」的说法写成官方范围。

## 1. Liter8｜0.3.0 / 0.3.1：无 SEP 也能用上软件钥匙串

Xplo8E 的 Liter8 在窗口内连发两档。**v0.3.0** 发布于 **2026-11-14 18:48:17**（Asia/Shanghai，源 2026-11-14T10:48:17Z）：`securityd` 会加载一个小型插入层，用软件主密钥包裹钥匙串条目，从而在没有 SEP 的情况下使用系统钥匙串；同时把 iOS 27.3 beta 1（`24C5037i`）和 iOS 27.2.1（`24B156`）写成在 iPhone 11 上已审阅，在 11 Pro / 11 Pro Max 上为实验性，并改进了 `fw provision --check`。**v0.3.1** 发布于 **2026-11-14 20:21:12**（Asia/Shanghai，源 2026-11-14T12:21:12Z），修复新鲜安装 0.3.0 之后每次重启丢失钥匙串（例如 Wi-Fi 密码）的问题：把 l8keychain 主密钥改由 `_securityd` 所有。作者 @Xplo8E 于 2026-11-14 20:33（Asia/Shanghai，源 12:33:32Z）发帖同步了 0.3.1。11-09 速递写过更早版本，这是续更，不是首发。官方范围是 iPhone 11（A13）已审阅、Pro / Pro Max 实验性，**不要写成 A12 已支持**；它也不是面向所有机型的通用 iOS 27 越狱，使用上仍需配合 Mac，社区也有「每次重启要重做」的说明。若已经用 0.3.0 做过新鲜安装，发行说明要求在 SSH ramdisk 里重跑 `fw provision`。

来源

```
https://github.com/Xplo8E/Liter8/releases https://x.com/Xplo8E/status/2121582302803497028
```

**工地点评：**在 iPhone 11 上研究 iOS 27 的人，这档更新的看点是「没有 SEP，钥匙串也能留下 Wi-Fi 密码」。先按官方写明的机型和版本来，不要把实验性机型或网上的 A12 说法扩成已经支持；它依然是受限方案，不是可以随手上手的通用越狱。

## 2. appstorectl｜1.2.0：为 Liter8 补上 iOS 27 的免费应用安装与解密

同一作者 Xplo8E 在 **2026-11-15 02:41:57**（Asia/Shanghai，源 2026-11-14T18:41:57Z）给 appstorectl 打了 **1.2.0** 标签，changelog 写的是增加 iOS 27 支持。作者随后在 X 上说明：配合 Liter8，可在 27.2.1 上从终端安装并解密需要 iOS 17 / 18 / 26 / 27 的免费 App Store 应用。仓库在 https://github.com/appknox/appstorectl ，发行页提供 `com.appknox.appstorectl_1.2.0_iphoneos-arm64.deb`。这是 Liter8 的配套小工具，不是新的越狱方案。

来源

```
https://github.com/appknox/appstorectl/releases/tag/1.2.0 https://x.com/Xplo8E/status/2121692853126791208
```

**工地点评：**已经在 iPhone 11 上跑 Liter8、又想从终端把免费 App 装下来做分析的人，可以直接看 1.2.0 的说明。它只覆盖免费应用，也只是越狱环境里的配套工具，请只用在自己的设备或授权研究里。

## 3. WQFiles｜一天两更：0.9.7 新界面，0.9.8 把 Reset Access Cache 放进设置

kolbicz 的 WQFiles 昨稿写到 v0.9.6，窗口内又连发两档。**v0.9.7** 发布于 **2026-11-14 22:17:48**（Asia/Shanghai，源 2026-11-14T14:17:48Z）：重做了起始页和标签（Home / Apps / Clean / Backups），设置里可以关掉「New Design」回到经典界面。**v0.9.8** 发布于 **2026-11-15 02:14:23**（Asia/Shanghai，源 2026-11-14T18:14:23Z）：把原先只在启动检查失败时出现的 Reset Access Cache，放到了 Settings → Troubleshooting，两种界面都能点到；并写清访问被拦住时日志会说明原因。官方要求仍是 iOS 27，或 iOS 26.0–26.7.2；测试范围包括 27.0.1、27.2.1、26.7.1 和 27.3 beta，侧载需保留 App Group entitlement。今天只跟这两个小版本，不再重讲 worse\_query 的原理。

来源

```
https://github.com/kolbicz/WQFiles/releases
```

**工地点评：**已经在用 WQFiles 的人，可以把版本从昨天的 0.9.6 升到 0.9.8：界面改了可以随时切回去，访问缓存出问题也不必再卡在启动页。新用户先读官方的系统版本和侧载条件，不要把它理解成新的越狱。

## 4. OpenBin｜作者公布函数树、XREF 和可点击 listing

@OpenBinAI（The Open Binary Project）在 **2026-11-14 21:30**（Asia/Shanghai，源 2026-11-14T13:30:00Z）发帖称 OpenBin 更新了一轮界面：Ghidra 风格的函数树（Functions / Imports / Thunks，可按前缀自动分组）、数据交叉引用（可点进每个引用该符号的函数）、带语法着色且可点击的 Program Listing，以及更清楚的伪代码配色。帖文附了界面截图。抓取时互动不高（赞 5、转发 2、曝光约 217）。这是作者自报的窗口内工具更新，不是一次大版本发版，也没有同期的长篇技术说明。

来源

```
https://x.com/OpenBinAI/status/2121596513272922464
```

**工地点评：**已经在跟 OpenBin 这个小项目的人，可以看一眼这次界面是不是更好用。项目体量和讨论都不算大，不必当成今天必须点开的硬料。

## 工具箱补充｜版本与窗口内更新

和今天新闻相关的工具，版本信息以官方页面为准。有新 tag 的单独标出；无更新的也列一行方便对照。Liter8 0.3.1、appstorectl 1.2.0 与 WQFiles v0.9.8 已分别写入第二部分第 1、2、3 条，这里不再展开。bla-agents 3.3.2 见第一部分第 5 条。

**Liter8 0.3.1**／**appstorectl 1.2.0**／**WQFiles v0.9.8**（窗口内新版本）

* Liter8 相对 11-09 已介绍的更早版本，今日新到 0.3.1；appstorectl 为新列入的配套工具；WQFiles 相对昨文 0.9.6 升到 0.9.8。详细更新点见第二部分对应条目。
* 官方：
* https://github.com/Xplo8E/Liter8/releases/tag/v0.3.1
* https://github.com/appknox/appstorectl/releases/tag/1.2.0
* https://github.com/kolbicz/WQFiles/releases/tag/v0.9.8

**bla-agents 3.3.2**（窗口内新正式版，相对昨文 3.3.1）

* 2026-11-15 02:26:42（Asia/Shanghai）发...