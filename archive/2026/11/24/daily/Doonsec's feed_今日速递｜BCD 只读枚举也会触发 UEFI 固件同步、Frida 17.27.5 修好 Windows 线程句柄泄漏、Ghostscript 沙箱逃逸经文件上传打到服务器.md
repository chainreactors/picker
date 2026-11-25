---
title: 今日速递｜BCD 只读枚举也会触发 UEFI 固件同步、Frida 17.27.5 修好 Windows 线程句柄泄漏、Ghostscript 沙箱逃逸经文件上传打到服务器
url: https://mp.weixin.qq.com/s/YbsV-NYniazmqBkV0g4zUg
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:33.487405
---

# 今日速递｜BCD 只读枚举也会触发 UEFI 固件同步、Frida 17.27.5 修好 Windows 线程句柄泄漏、Ghostscript 沙箱逃逸经文件上传打到服务器

# 今日速递｜BCD 只读枚举也会触发 UEFI 固件同步、Frida 17.27.5 修好 Windows 线程句柄泄漏、Ghostscript 沙箱逃逸经文件上传打到服务器

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今日速递 · 2026-11-24

周二好，今天从一则「只读枚举也会去同步 UEFI 固件」的分析说起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OoI9czGaCkQ4exb0wgHV5qmwjA7jMs7cxmZgiayuDBKuS0jk1QsMiaEY5iavt1fO9ic9AW30rlVxsecWvcx6gg7YQ78EgmWFiaPMpKJwdHTCKZiaU/640?wx_fmt=jpeg&from=appmsg)

PART 1

## 第一部分｜国内安全厂商 · 安全网站 · 安全论坛热点

以看雪近几天的逆向、固件与样本分析帖为主，只整理公开帖里的课题与项目定位。

## 1. BCD 只读枚举｜关闭系统存储时会向 UEFI 固件同步

看雪作者 Zhan\_Er 于约 2026-11-23（帖子显示「1天前」）写了一篇 Windows 启动配置的逆向笔记。环境是 Windows 11 24H2 x64、GPT/UEFI。他在给 WinPE 添加 BCD 启动项时遇到矛盾现象：bcdedit /set 已经报「指定不存在的设备」，随后的枚举却能打印出刚写入的配置；对 {current} 做 /enum /v 也能完整列出启动项，却在末尾再次报同样的错误，进程退出码为 1。把同一份 BCD 文件用 /store 显式指定后再枚举，错误就消失了。

对照在线/离线存储、再结合 IDA 静态分析和提权后的调试，作者把问题定位到 BCDEdit 关闭系统 BCD 存储时的固件导出过程：当 Description\FirmwareModified=1 时，BiCloseStore 会尝试把启动项同步到 UEFI 固件。处理 {bootmgr} 时，它的 device 元素是 BCD 设备类型 5（界面显示 unknown），BiCreateMergedBootEntry 于是返回 STATUS\_NO\_SUCH\_DEVICE（0xC000000E）。这个错误顺着关闭存储的调用链传回枚举命令，最后变成 Win32 错误 433。作者把 {bootmgr} 的 device 指到 ESP 分区之后，默认的 current、FIRMWARE、ALL 三种枚举都恢复正常。文中的核心判断是：BCDEdit 的「只读枚举」也会在关闭系统存储时触发固件同步；枚举输出成功，并不等于整条命令成功。

来源：看雪安全社区 / Zhan\_Er

```
https://bbs.kanxue.com/thread-293639.htm
```

**点评：**这篇适合做过启动项、WinPE 或 UEFI 调试、却被「明明写进去了还报设备不存在」困扰的人。它把一次像是命令行误报的现象，说清楚是关闭存储时的固件同步，而不是枚举本身读失败。

## 2. 假外挂真窃密｜《逃离塔科夫》Loader 投放的反射注入木马

火绒安全实验室于约 2026-11-23（「1天前」）在看雪发表样本分析：GitLab 上出现伪装成《逃离塔科夫》游戏外挂的仓库，README 宣称具备自瞄、透视、雷达等功能，实际是窃密木马。诱饵仓库创建于 2026-11-15，只放了 eft\_hack.zip 和说明，没有真实外挂源码；更早的载荷托管仓库（skywatch）创建于 2026-10-19，比诱饵早了将近一个月。

Loader 启动后会弹出 Checking for updates，向 Pastebin 拉取远程配置，再按配置下载后续组件并启动。木马会窃取浏览器里的敏感信息、加密货币钱包和即时通讯数据，并通过 Telegram 频道描述获取控制端地址。报告还特别写到，它会采集 Claude Code、Codex CLI 等开发工具的本地配置，以及 OneNote 和相关 VPN 工具的连接信息——这些文件里一旦存了 API 密钥，影响的就不只是个人账号。火绒称产品侧已对该行为做了拦截。

来源：看雪安全社区 / 火绒实验室

```
https://bbs.kanxue.com/thread-293646.htm
```

**点评：**对分析样本的人，这条链路的价值在于「先抛诱饵仓库、载荷通道提前就位」的时间线，以及它会翻开发工具本地配置。对普通用户更直接的提醒是：来路不明的「游戏辅助」不要下、不要跑。

## 3. 魔改 IL2CPP｜标准 metadata 头对不上，表偏移要按运行时还原

看雪作者 New对象处于约 2026-11-23（「1天前」）写了一篇 Unity IL2CPP 对照笔记。他先从标准 global-metadata.dat 讲起：文件头是 Il2CppGlobalMetadataHeader，前 8 字节常见为 sanity 0xFAB11BAF 加上版本号，后面是字符串、方法、字段、类型等表的偏移和大小；方法的原生代码在 SO 里，只靠 metadata 拿不到完整实现。标准 libil2cpp.so 也能看到语义明确的导出函数。

对照样本是一份被深度改过运行时的 so（文中写作 libxxxxshen.so）。作者观察到，标准 Il2CppDumper 无法直接处理这份文件：部分表偏移并不写在本地文件头的固定位置，而要按运行时里对头字段的运算才能还原，例如 typeDefinitions 等字段会先取出一个值再做一次加减。文中还区分了 CodeRegistration（方法对应哪段原生代码）和 MetadataRegistration（类型如何表示、对象如何布局）。整篇按「先看标准格式，再看改了哪一层」展开，不涉及具体玩法修改。

来源：看雪安全社区 / New对象处

```
https://bbs.kanxue.com/thread-293642.htm
```

**点评：**适合已经会用 Il2CppDumper、却第一次碰到「头对不上、工具直接失败」的人。它把魔改点落在元数据头和注册表这一层，比笼统说「引擎被改过」要清楚得多。

## 4. 华为万兆光猫 HN8145X6N｜Dopra 宿主域与 OpenWrt 容器域的分层

看雪作者哈吉米（账号 mb\_tkndfqkv）于约 2026-11-23（「1天前」）连发上下两篇技术手记，目标是华为电信定制万兆光猫 OptiXstar HN8145X6N。文中给出的硬件是海思 SD5182H 双核 ARMv7，软件基线为 Dopra Linux V500R023C00SPC162。作者把这台设备画成双层结构：宿主域跑 Dopra Linux（内核版本写的是 5.10.0 SMP ARMv7）和受限维护壳 srv\_clid（UID 3030）；容器域是跑在 LXC 里的 OpenWrt 用户态，核心特权守护进程是 /sbin/appmgr，通过 D-Bus 系统总线与维护壳通信。外围维护接口是裁剪过的 Dopra CLI，命令解析按白名单匹配。

上篇主要做架构测绘，并记录了民间常见维护脚本可能让 PON 链路和驱动出现异常的现象；下篇转向 appmgr 的消息调度，以及与内核模块装载相关的结构观察。两篇都是已公开的设备研究笔记，篇幅很长，适合先建立「这台网关到底分成几层、特权进程在哪」的图景。

来源：看雪安全社区 / 哈吉米（mb\_tkndfqkv）

```
https://bbs.kanxue.com/thread-293634.htm https://bbs.kanxue.com/thread-293635.htm
```

**点评：**想了解运营商定制网关现在长什么样，这两篇的架构图很有用：不是单一的 OpenWrt 盒子，而是 Dopra 宿主加容器里的应用管理器。建议先读分层，再按自己的研究方向决定要不要看下篇的细节。

## 5. 车机 AIDL 审计｜权限校验写在客户端，等于门上没锁

看雪作者 kysl 于 2026-11-24（帖子显示「5小时前」）分享了一套车机 AIDL 接口的审计思路。文中的服务名、接口名和权限名都做了脱敏，示例代码只用来说明位置问题，作者写明不讨论具体漏洞的利用细节。入手时他先按移动端习惯翻 Manifest，发现真正干活的 vendor 服务并不在那里，后来改为从 ServiceManager 和 dumpsys 对照出已注册的服务，再去系统或 vendor 分区里找 .aidl，或从反编译后的 Stub 类里读 TRANSACTION\_\* 常量当方法清单。有些服务开机时还没注册，只看开机瞬间的快照会漏。

作者认为最常见的问题不是「完全没写校验」，而是写错了地方：客户端调用前做了 checkSelfPermission，服务端 Stub 里却谁来都能进。另一种情况是校验了，但用的不是原来的调用方——Binder.getCallingUid() 在 clearCallingIdentity() 之后拿到的是系统自己，身份被换掉后再判断，门等于没锁。可靠的写法是把 enforceCallingPermission 放在服务端入口，并且先保存真实的 calling uid。

来源：看雪安全社区 / kysl

```
https://bbs.kanxue.com/thread-293656.htm
```

**点评：**做车机或 vendor 系统服务审计的人，可以把「校验在不在 Stub 里」当成第一眼要看的点。这篇没有对着某款真实产品写利用，读起来更像一份检查清单。

## 6. C/C++ 特征码搜索｜Sunday、SSE2、AVX2 按 CPU 自动选择

看雪作者 wtujoxk（文中开发者署名ご听雨づ）于约 2026-11-21（帖子显示「3天前」，早于 11-22）分享了一套可单独拷贝使用的 C/C++ 特征码搜索代码，也可下附件。入口 PatternFindEx 会按当前 CPU 自动在 Sunday、SSE2、AVX2 之间选择，也可以直接调用 SundayPatternFind、SSE2PatternFind 或 AVX2PatternFind。搜索范围可以是当前进程的某个模块，也可以指定起止地址；特征串支持通配符，格式如 "?5 ?? 77 ?8 ?? AA BB"。

帖子里给出了最小调用示例，并说明 searchNum 为 0 时会搜完整模块。这是一份写给自己用的内存模式匹配工具，用来在已加载模块里定位已知字节序列。

来源：看雪安全社区 / wtujoxk

```
https://bbs.kanxue.com/thread-293625.htm
```

**点评：**做 Windows 逆向时经常要在内存里找一段特征字节，这一份把三种常见算法收在同一套接口里，需要的话可以直接拿来对照或改。日期早于 11-22，今天补收。

## 7. Ghidra + Joern 流水线｜先收敛范围，再反编译和污点分析

看雪作者于约 2026-11-20（「4天前」，早于 11-22）介绍开源项目 binary-audit-pipeline（仓库 SpiralRise/binary-audit-pipeline）。场景是手里只有去掉符号的 so 和固件里的可执行文件：以往要分别跑 capa、cwe\_checker，再进 Ghidra 反编译，用 Semgrep 扫伪代码，最后才用 Joern 做污点分析，五种输出还得手工合并。

作者把并行改成漏斗：先用 capa 和 cwe\_checker（并过滤掉几乎每个二进制都会出现的 CWE676）圈出候选文件，Ghidra 只反编译这些文件；Semgrep 对伪代码做初筛后，Joern 只在命中范围内建图。项目提供 Docker 镜像 ghcr.io/spiralrise/binary-audit-pipeline:1.1.0，一条命令输出「高风险点清单」和分目录保存的原始 JSON。作者写明它不是漏洞扫描器，不会直接给出「存在某某漏洞」的结论，加壳样本和尚未解包的固件镜像也不在覆盖范围内。

来源：看雪安全社区；GitHub / SpiralRise/binary-audit-pipeline

```
https://bbs.kanxue.com/thread-293613.htm https://github.com/SpiralRise/binary-audit-pipeline
```

**点评：**做固件审计、却被「全量反编译几千个函数」拖住的人，可以看它怎么把范围一步步收窄。输出按步骤分目录保存，也方便事后复查。日期早于 11-22，今天补收。

PART 2

## 第二部分｜X 上的二进制 / 安全 / OS 逆向热点 + 越狱工具

本日以 Frida 新版本、CCS 同期 SURE 2026 的几篇逆向论文，以及 KernelSU 模块与样本改造分析为主。

## 8. Frida 17.27.5｜修好 Windows 线程句柄泄漏和安卓二次本地会话崩溃

Frida 官方于 2026-11-23（UTC，香港时间 2026-11-24）发布 17.27.5，是一版缺陷修复。发布说明里大部分工作来自 @kkuehl（Kirby）：从 17.25.0 起，Windows 上的 agent 改为映射进目标进程，而不是走系统加载器；每次附加都会在目标里留下七八个已退出线程的句柄，因为 GLib 要等加载器的线程分离通知才会清理，映射进去的映像收不到这个通知。现在由 GLib 自己启动的线程在退出时自行清理，其他线程的私有数据则改走光纤本地存储，和 POSIX 后端用 pthread key 的做法对齐。映射失败时 attach() 不再一直不返回；对已经退出、但句柄还在的进程，错误提示也和「PID 不存在」一致。ARM64 上，Windows 11 26H1 映射带静态 TLS 的映像会中止，识别加载器 TLS 例程的启发式已改成按行为判断，并在多个版本的 ntdll（含 ARM64EC 和 CHPE）上做过核对。映射进去的 dbghelp 现在也能加载符号服务器所需的 symsrv.dll。

安卓一侧，关闭本地会话再开下一个会崩溃：本地后端会在宿主进程里创建 Java 虚拟机，会话结束时把它毁掉，但 ART 不允许在同一进程里创建第二台虚拟机。现在这个辅助进程按进程级启动并在会话之间共用。iOS 上，设备在擦除后启动或刚打开开发者模式时，若两秒内没有给出 IPv6 地址，NCM 驱动可能被丢下不管，重试再开新的，地址帧常常落到被放弃的驱动里，设备会一直不可达，直到重启 idund；现在会关掉被放弃的驱动。macOS 上，Gadget 和 frida-inject 监视脚本目录改走 FSEvents，写入已有文件也能被看到。发布说明还写到关闭 DeviceManager 时的偶发挂起已定位。

来源：Frida 官方博客

```
https://frida.re/news/2026/11/23/frida-17-27-5-released/
```

**点评：**在 Windows 上长时间挂着 agent、或在安卓里以嵌入方式反复打开本地会话的人，这版值得尽快更新。功能没有大改，修的都是用久了才会撞上的泄漏、崩溃和设备不可达。

## 9. HermesLoader｜把 React Native 的 Hermes 字节码抬进 Ghidra P-Code

ACM CCS 2026 在海牙同期举办的 SURE 2026（Software Understanding and Reverse Engineering）工作坊于本周宣讲一组逆向论文。其中 Fraunhofer SIT / ATHENE 的 Martin Renze 与 Florian Magin 介绍了 HermesLoader：一个 Ghidra 扩展，用来加载 React Native 应用里的 Hermes 字节码，并把它抬到 Ghidra 的 P-Code 中间表示，从而走常规的反汇编、反编译、导航和交叉引用。

扩展包含一份针对 Hermes 字节码版本 96 的 SLEIGH 规格、把字节码容器重建为带类型的程序对象的加载器，以及针对字符串、字段访问链、聚合字面量和部分函数引用的补充分析。作者在多种配置编译出的样本上做了评估：版本 96 的 206 条操作码均已实现，测试语料覆盖了其中 199 条，与官方 hermesc 反汇编大体一致；主要限制是部分由表驱动的控制流目标还恢复不完整。结论是：Hermes 字节码可以作为 Ghidra 里可交互分析 React Native 的基础，而不必只盯着原生日志或手工对照反汇编。

来源：SURE 2026 接收论文列表（Renze / Magin）

```
https://sure-workshop.org/papers/
```

**点评：**分析 React Native 应用时，逻辑常常打成 Hermes 字节码，主流工具一直不太接得住。这篇把「能不能在 Ghidra 里当普通程序翻」这件事往前推了一步，想跟进实现细节可以直接看工作坊论文页。

## 10. DRTTI｜从 Delphi 的 RTTI 里重建类层次、字段布局和虚表

同一场 SURE 2026 上，于默奥大学的 Anton Degerfeldt、Sylvain Fontaine 和 Alexandre Bartel 介绍了开源 Ghidra 插件 Drtti（读音接近 dirty）。它从 Delphi 程序里自带的运行时类型信息出发，自动重建类层次、字段布局和虚方法表，也可以从 Interactive Delphi Reconstructor（IDR）导入标准库符号。论文还尝试了一些不依赖 IDR 的轻量启发式，例如用 x87 浮点指令指纹给数学相关代码做保守提示。

评估覆盖 10 个 Delphi 应用，包含 Delphi 4 与 Delphi 8 及以后的虚表布局。标准 Ghidra 分析平均把 57.57% 的可执行内存标成已验证的数据或指令；只用 Drtti 时是 61.15%，再加上可选的 IDR 符号则到 87.66%。作者把两个效果分开写：Drtti 本身在 Ghidra 里做不依赖 IDR 的结构恢复，IDR 符号则主要补库函数命名和数据上下文。仓库在 GitHub 的 software-engineering-and-security/Drtti，作者于 2026-11-24 在 X 上也发了介绍。

来源：SURE 2026 论文；GitHub / software-engineering-and-security/Drtti；X / software\_ses

...