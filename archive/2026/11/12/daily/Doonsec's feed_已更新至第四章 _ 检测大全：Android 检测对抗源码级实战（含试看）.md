---
title: 已更新至第四章 | 检测大全：Android 检测对抗源码级实战（含试看）
url: https://mp.weixin.qq.com/s/VjOzGUS_GchUrvK3QPGoUg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:37.669440
---

# 已更新至第四章 | 检测大全：Android 检测对抗源码级实战（含试看）

# 已更新至第四章 | 检测大全：Android 检测对抗源码级实战（含试看）

看雪课程
看雪课程

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

-写得一手 Frida 脚本，却屡屡被加固检测拦截？

-网上找来的绕过方案，没过多久直接失效；

-遇到 DexProtect、Promon 这类企业级壳就束手无策；

-只会打地鼠式修补，不知道检测究竟从何而来？

绝大多数教程只教你「怎么绕过」，却从不讲**「为什么会被检测」。**

《检测大全：Android 检测对抗源码级实战》跳出零散特征对抗，直达系统底层根源：从开机启动链、TEE 三绿硬件证明、Linux 内核，到 Frida / LSPosed / KPM 内核模块源码级拆解，完整吃透企业壳全套检测逻辑。

**100+小时教学**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1udAic3461GIpwAvicKhtBlaXyq3zOcczKZ60qaibYUHURNe9IUmozxTvSvPIJ9tCpnWSjQQNWNj9evk0hDEUsqAAfRuA3CGUZ9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K27lrsz2kZ4c2P1n2hDchICAV186Ir3DOic65ibd8dYWy5T43fbaqmaibtia9XT1agWRQ0n3pzyssT6lTtco04XRNYkv7glNr3vM0U/640?wx_fmt=jpeg&from=appmsg)

*限时抢购价：¥4888*

配套三大自研持续更新工具

**扫码免费试看**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0zzzq649NrNDOJtoAGd4ZtMOFqmmqBXNEBicoyjv6ApWAI0DWOpHJ0tYNkMnehY1xzju67yVFZprD949ygBxsicicgWAZEORkIEI/640?wx_fmt=png&from=appmsg)

视频：1-1 Android hook原理

**学员技术储备**

**必备：**Java 与 C 基础语法；了解 Android 应用基本结构；会 adb / 真机调试基本操作；frida 基本使用（能写简单 hook 脚本）。

**建议：**看得懂 ARM64 汇编基本指令；了解 ELF 结构；有一台可 root 的设备（Pixel 系列最佳，课程以 Pixel 6 + Android 14 为基准环境）。

*什么都不满足？01–02 模块就是为你准备的起点，边学边补！*

**一、不是停留在工具使用，而是深入底层原理**

很多 Android 安全学习资料，往往集中在工具使用、脚本编写和常见案例分析。但真正面对复杂的安全检测与工程问题时，仅仅知道如何使用工具，往往是不够的。

这套课程选择了一条更深入的技术路线：

**从 Android 系统启动开始，逐层深入运行时、注入机制、Linux 内核，再延伸到 Frida、LSPosed 的源码与工程实现。**

课程以真实 Android 环境为基础，围绕系统机制、底层原理和工程实践展开，帮助学习者建立完整的技术认知。

你将系统接触：

* Android 启动流程：从 boot.img、ABL 到 Zygote、应用进程启动。
* Android Root 与硬件证明：深入 TEE、硬件证明及相关检测机制。
* Android Hook 与注入：理解 Frida、GOT Hook、ptrace 等底层机制。
* Android Runtime：深入 DEX、ART、ClassLoader 和 Java Hook。
* Linux 内核：掌握进程调度、内存管理、异常中断、VFS、内核调试等基础。
* ARM64：深入指令级 Hook、单步 Trace、硬件断点等技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2S7RAGvMZYcHJ9bqjAPQIfgQwFGS9PMBNGlCmY0rH501BYO5VRZfepfZLbKGsRsIy8ic3zibcrNvrqKewSiaDJ6dKUDlgdJ9lhKA/640?wx_fmt=png&from=appmsg)

*3大自研工具*

*内置最强过检测逻辑，学完即上手！*

**二、五大技术模块，构建完整的 Android 底层技术体系**

整套课程规划了五大核心模块，覆盖 Android 系统、Linux 内核、Frida、KPM 和 LSPosed。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1akmSfbHWc305awx9hgymYibzkpndFtYNhfmjUkTUhA31udOhCa49tN9NxZAoVpYdH6zSVKwtq8MUjmnxPmd3PtMMEx7d4P5NM/640?wx_fmt=png&from=appmsg)

*\*每一课配真机验证记录（Pixel 6 / Android 14），附预期输出，逐条可复现。*

**系统与检测基础：从 Android 启动流程开始**

从 APatch、boot.img 开始，逐步理解 Android 手机的启动过程、硬件证明、Root 检测、Zygote、Linker、ptrace、Hook、注入检测以及 DEX 执行机制。

**Linux 内核基础：真正理解系统底层**

课程从进程、线程与调度开始，逐步深入内存管理、ARM64 异常与中断、VFS、procfs、内核调试与追踪、BTF、vmlinux、KASLR 等内容。

**Frida 源码详解：从会使用到理解其内部实现**

课程围绕 Frida 的启动、注入、脚本运行、Java.perform、Server IPC、SELinux、默认 Hook、Stalker、线程处理、自定义 Linker 等内容展开。不仅分析 Frida 如何工作，还深入讨论底层结构、运行机制和兼容性工程。

**KPM 内核工程：深入 Linux 内核模块**

包括 KPM 模块设计、装载与生命周期、内核观察面、ARM64 指令 Hook、Text Shadow、内核单步 Trace、硬件断点、Perf 生命周期，以及 SELinux 和 FD 安全扩展等。此外，还涉及 Android Chrome 多进程多开、独立 UID、VPN 隔离以及相关内核工程实践。

**LSPosed 详解：从 Java Hook 到运行时工程**

课程将深入 LSPosed 总体设计、LSPlant Java Hook、多模块回调、DEX 加载、标识泛化、Binder 与 FD 生命周期，以及 Android 14/16 ART/JVMTI 兼容性问题。同时，还涉及侧信道与结构差分检测、跨版本适配和完整的工程验证矩阵。

**三、企业级加固壳实战：把技术放到真实场景中**

理解底层原理只是第一步，真正的技术能力还需要通过实际工程验证。

课程目前已经准备了 DexProtect 完整企业壳实战课程，围绕检测逻辑拆解与对抗展开。后续还将持续更新完整 Promon 课程，以及更多顶级检测壳的分析与实战内容。

课程不以简单展示某个结果为目标，而是希望通过真实工程问题，让学习者理解复杂检测机制背后的实现逻辑，以及如何从底层定位和解决问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2WRVpo5icliajta01jWibor4VBFpqEM0byv7ic4MwSMmjK4rKZow4amtbBLWWvPUOFchANM5H31Onia6axBiaJBmq1CJH5WgA7tsL6I/640?wx_fmt=png&from=appmsg)

**课程收获**

**1. 真正理解"为什么能检测"：**每个检测点拆到观察面、数据与系统机制，从此过检测是必然推论，而不是背特征；

**2. 掌握保值的方法论武器库：**二分法定位特征、检测前自卸载、黑盒分析……面对任何未知新型检测都能独立拆解；

**3. 拿到三大直接可用的自研工具**（自研 Frida 改版 / xiaojia-hide KPM 内核模块 / 魔改 LSPosed），内置最强过检测逻辑，学完即上手；

**4. 吃透硬件证明全链路：**Tricky Store 检测原理与魔改版本、Google 三绿转发，从 TEE 到证书链说清楚"三绿"到底怎么判；

**5. 源码级吃透 Frida / LSPosed / 内核模块三大件：**从"会用"进阶到"会改、会藏、会修"；

**6. 打通系统与内核基础：**手机启动链、root 原理、内核七大子系统，具备向更深层进阶的扎实功底；

**7. 完整打穿企业级壳：**DexProtect 全套检测逻辑实战，建立"理解全套逻辑 > 死记千个检测点"的对抗思维，为 Promon 等后续课程打底；

**8. 获得一套可复现的真机验证体系：**每课验证记录 + 预期输出，每一项技术都亲手跑通过。

**四、课程目录大纲（上下滑动查看）**

*\*最终大纲以上线版为主*

**第一部 · 系统与检测基础（炼气境，14 章）**
     01 APatch 的 root 原理 —— 从 boot.img patch 开始
     02 Android 手机启动过程 —— 从 abl 开始
     03 Android 硬件证明 —— 从 TEE 开始到 Google 三绿（含 Tricky Store 检测原理、Tricky Store   魔改版本、Google 三绿转发）
     04 Android root 检测 —— 结合前面全部内容综合讲解
     05 Android App 启动过程 —— 从 zygote 开始
     06 Android linker 启动过程 —— 从 open so 到 JNI\_OnLoad 执行结束
     07 Android ptrace 原理 —— ptrace 加载 so、ptrace 的特征与检测
     08 Android zygisk 原理 —— 从 fork 到 Activity 完整启动；magisk mount 覆盖   zygote、neozygisk 处理 init 进程
     09 Android hook 原理 —— frida hook、got hook、CFI、绕过 CRC 及对应检测与应用手段
     10 Android frida 源码讲解 —— 从 frida 启动开始
     11 Android 注入检测 —— 如何检测注入痕迹
     12 Android Java Hook 原理 —— Android 的 Java Hook 如何实现
     13 Android IPC 相关内容 —— 常见服务与 Binder
     14 Android dex 详解 —— dex 执行与脱壳核心
     15 Android 自动化 —— u2、scrcpy、事件驱动核心
     16 Android 基础 hook 脚本、检测与算法相关逻辑分析

**第二部 · 内核基础（筑基境，K01–K07）**
     K01 Linux 进程、线程与调度 ——   task\_struct、fork/clone/exec、runqueue、cgroup、cred
     K02 Linux 内存管理 —— VMA、页表、fault、COW、物理页、分配器、TLB
     K03 ARM64 异常、中断与信号 —— vector、pt\_regs、syscall、IRQ、signal、debug trap
     K04 VFS、文件系统与 procfs —— fd、file、inode、mount namespace、seq\_file、sysfs
     K05 Linux 内核调试与追踪 —— printk、ftrace、tracepoint、kprobe、perf、pstore
     K06 BTF、vmlinux 与内核类型 —— Image/vmlinux、DWARF、BTF、CO-RE、offset
     K07 内核符号、KASLR 与运行地址 —— System.map、kallsyms、export、KMI、MODVERSIONS

**第三部 · Frida 详解：源码与兼容工程（化神境，F01–F11）**
     F01 Frida 整体启动、进程注入与 Zygote 门控 —— frida-tools、server/HostSession、ptrace/bootstrap/loader、zygote/USAP、子进程   agent、mapper 与自卸载改动
     F02 Frida 第一个脚本运行时机 —— create\_script、load\_script、GumJS、QuickJS/V8、JS   调度线程
     F03 Frida Java.perform 原理 —— Java VM   attach、ActivityThread、LoadedApk、ClassLoader、pending VM ops
     F04 Frida server IPC 逻辑 ——   WebService、Socket、DBusConnection、ControlService、HostSession、AgentSession
     F05 Frida server 与 Android SELinux —— patch policy、frida\_file、pipe   socket、zygote ptrace、setcontext
     F06 Frida 默认 Hook —— pthread registry、module   registry、signal/sigaction、ExitMonitor、child gating
     F07 Frida Stalker 原理与修复 —— follow/infect、ExecCtx、basic block 翻译、slab、event   sink、arm64 near allocation
     F08 Frida 线程名称处理 —— GLib/Gum 线程命名、/proc/self/task、comm、Thread-N 规范化
     F09 Frida 自定义 linker ——   agent-mapper、PT\_LOAD、relocation、init\_array、agent\_base/agent\_size
     F10 Frida 线程结构体处理 —— bionic pthread\_internal\_t、start\_routine、libc   decoy、pthread list 清洗
     F11 当前工程隐藏与兼容处理总表 —— maps 过滤、linker 账本、CFI shadow、Gum ELF   匿名映射、Instruction.parse 可读性

**第四部 · 内核模块详解：KPM 内核工程（化神境，M01–M07）**
     M01 KPM 模块设计、装载与生命周期 —— KPM ELF、编译重定位、符号与 offset、安装/卸载顺序、退出回收
     M02 内核观察面与基础检测处理 —— maps/smaps/map\_files、mountinfo/statx、syscall   table、调试状态、USB/VPN/netlink/Binder 只读观测
     M03 ARM64 指令 Hook 与 Text Shadow —— trampoline 重定位、BTI、PTE 双   PFN、fault/GUP、fork/mprotect、rmap/RSS
     M04 ARM64 内核单步 Trace —— MDSCR\_EL1、SPSR.SS、CPU 亲和性、step   hook、双缓冲、workqueue、二进制解析
     M05 硬件断点 Hook 与 Perf 生命周期 —— register\_user\_hw\_breakpoint、pt\_regs.pc、inherit、ptrace   regset、task/perf/退出回收
     M06 SELinux 与 FD 安全扩展 —— task\_ext、avc\_denied、inode/file/socket   SID、f\_security、FD\_\_USE、xattr/SO\_PEERSEC 长度 ABI
     M07 Android Chrome 多进程多开 —— OEM Custom Profile、AMS/zygote、独立 UID/CE/DE、Chrome   child process、CDP、每-user VPN、KPM 与事务回滚

**第五部 · LSPosed 详解：运行时工程（化神境，L01–L10）**
     L01 LSPosed 总体设计与进程进入 —— Zygisk pre/post specialize、进程筛选、framework   DEX、Binder、Main.forkCommon
     L02 LSPlant Java Hook 原理 —— ArtMethod、动态桩类、trampoline、backup、entrypoint、原方法调用
     L03 多模块回调与去优化 —— HookItem、modern/legacy callback、priority、并发发布、JIT   inline、deopt
     L04 模块 ClassLoader 与 DEX 生命周期 —— 委派顺序、SharedMemory、file-backed   DEX、dexElements、资源与 native library
     L05 标识泛化与字符串源头治理 —— native 编译期常量、DEX IR 重写、类前缀、模块入口元数据、JNI 映射
     L06 Binder、FD 与 linker 账本收口 —— bridge detach、mmap/FD   生命周期、link\_map、solist、sonext、module counter
     L07 Android 16 ART/JVMTI 根因修复 —— generated class 枚举、dex method index、隔离   ArtMethod backup、反射 Method 包装
     L08 Androi...