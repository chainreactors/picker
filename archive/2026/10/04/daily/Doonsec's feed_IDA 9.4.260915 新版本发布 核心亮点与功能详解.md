---
title: IDA 9.4.260915 新版本发布 核心亮点与功能详解
url: https://mp.weixin.qq.com/s/-qdXfrQCkBakk17n0uM4uw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:55.421107
---

# IDA 9.4.260915 新版本发布 核心亮点与功能详解

# IDA 9.4.260915 新版本发布 核心亮点与功能详解

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

IDA 9.4.260915 新版本发布

核心亮点与功能详解

01

PART

概述

OVERVIEW

Hex-Rays 正式发布了 IDA 9.4.260915 版本。作为业界领先的二进制分析工具，IDA 9.4 带来了多项重大更新，涵盖 Apple Dyld Shared Cache 工作流重构、Swift ABI 原生识别、全新的 Pathfinder 路径查找器、Git 团队协作支持、ARM SVE2/SME 指令集反汇编、Qualcomm Hexagon 及 MCore 处理器模块、反编译器字符串自动收录、深链接与片段分享等。

02

PART

核心亮点

HIGHLIGHTS

1. Apple Dyld Shared Cache 基础设施重构

IDA 9.4 彻底革新了处理 Apple Dyld Shared Cache（DSC）的方式，解决了长期以来困扰逆向工程师的跨引用断裂（"红地址"）问题。

**按需加载**：不再需要将整个 DSC 加载到数据库中以保持交叉引用完整性。IDA 9.4 支持跨 DSC 组件之间的无缝导航，未加载的部分会在需要时自动引入。

**专用小部件**：新增专门的 DSC 索引小部件，实时显示当前加载内容、可用模块等布局信息。

**专用工作流**：支持加载指定镜像及其依赖链（可指定 N 层深度）、从应用程序提取依赖列表并加载、在 DSC 中定位符号所在的镜像或段、从日志消息直接跳转到 DSC 对应位置等。

**API 支持**：所有 DSC 工具均基于公开 API（dscu.h / ida\_dscu 模块）构建，同时支持 C++ 和 Python 调用，便于人类分析师和自动化 Agent 共同使用。

2. Swift ABI 识别与类型推导

IDA 9.4 迈出了对 Swift 二进制文件更好支持的第一步。反编译器和类型系统现在能够理解 Swift 调用约定，引入三个全新关键字：

| 关键字 | 作用 | 对应寄存器 (ARM64) | 对应寄存器 (x86-64) |
| --- | --- | --- | --- |
| \_\_swiftself | 标记函数参数为 self 指针 | x20 | r13 |
| \_\_swiftasync | 标记异步函数，通过 \_\_swift\_get\_async\_context() 内建函数识别 async context | x22 | r14 |
| \_\_swiftthrows | 标记抛出函数，通过 \_\_swift\_get\_error() / \_\_swift\_set\_error() 内建函数识别错误返回寄存器 | x21 | r12 |

三个关键字均以函数声明为 \_\_swiftcall 为前提。\_\_swiftself 和 \_\_swiftasync 影响被标注函数自身的反编译行为；\_\_swiftthrows 则改变所有**调用者**的反编译行为——它告诉反编译器 x21/r12 并非被调用者保存寄存器，而是携带异常状态。

此外，IDA 9.4 还内置了 Swift 运行时函数的类型签名，使得 swift\_beginAccess、swift\_allocError、swift\_task\_switch 等运行时函数调用处不再是一堆无类型的 \_QWORD，而是具有明确类型和语义的伪代码。对于剥离符号的二进制文件，IDA 还可以自动恢复 \_\_swiftcall 标注、抛出调用和 swiftcall 栈溢出参数。

3. Pathfinder 路径查找器

IDA 9.4 新增的 **Pathfinder** 小部件（Shift-F9，View → Open subviews → Pathfinder）直接回答了逆向工程中最常见的问题："从这里能不能到达那里？"

**多航点路径**：设置有序的航点列表（A → B → C），Pathfinder 会按顺序查找经过每个航点的调用路径，并显示每段之间的节点数和最短路径长度。

**排除噪音函数**：将日志辅助函数、通用包装器等已知噪音函数加入排除列表，自动从所有路径中过滤。拖回航点列表即可重新包含。

**搜索选项**：支持包含数据交叉引用（默认开启）、仅最短路径、限制最大搜索深度。

**结果可视化**：路径结果可以展开为交叉引用树（支持正向和反向两种视角），也可以在 Xrefs Graph 中以专用配色高亮路径骨干和航点。

**持久化**：航点、排除列表和选项随桌面布局保存至数据库，重新打开 IDB 时路径自动重新计算。

**快捷添加**：在反汇编或伪代码视图中，Ctrl-Shift-F9 即可将当前光标所在函数添加为航点。

4. Jump Anywhere 成为默认跳转

IDA 9.4 中，按下 G 键默认打开的是全新的 **Jump Anywhere** 对话框，取代了传统的跳转地址对话框。

**统一搜索**：一次输入同时搜索函数（含库函数和导入函数）、名称（数据、字符串、自动生成的标签）、局部类型、函数注释、段等所有内容，并按匹配度排序，高亮匹配字符。

**实时预览**：在结果列表中移动时，预览窗格以反汇编、伪代码（已反编译的函数）或十六进制视图显示目标位置，预览模式会被记住。

**跳转历史**：对话框打开时自动选中上次跳转位置，G → Enter 两步即可返回。使用方向键可浏览更早的历史记录。

**表达式支持**：支持 IDC/Python 表达式（如 cpu.EIP）、段内偏移、C 风格算术（$ 表示当前地址）等。

**兼容旧版**：如需恢复旧版跳转对话框，可在 Options → Feature Flags 中切换。新对话框仍可通过 Jump 菜单中的 Jump Anywhere 操作访问。

5. Git 团队协作支持

IDA Pro 的 "Teams" 附加组件现在支持 Git 后端，用户可以直接使用 GitHub、GitLab、Bitbucket 或自托管 Git 服务器进行团队协作。无需部署额外服务器，无需创建新凭证，直接克隆、分析、提交、推送即可。

git ida 命令可在终端中直接使用，通过自动管理的全局 Git 配置。

团队状态栏信息可在设置中开关（默认开启）。

提供了从 Vault 迁移到 Git 的详细教程、Gitea 自托管设置指南以及日常操作指南。

6. ARM SVE2/SME 指令集反汇编与 MTE 反编译

ARM SVE2 和 SME 扩展已完全支持反汇编。同时，ARM MTE（Memory Tagging Extension）相关指令已支持反编译。这在分析现代 ARM 架构的 HPC、机器学习和高性能加密场景中尤为重要。

7. Qualcomm Hexagon 处理器模块

全新的 Hexagon（QDSP6）处理器模块使得分析 Qualcomm DSP 固件成为可能。配套提供了 Qualcomm MBN 启动镜像加载器，支持 SBL/XBL 容器、多 ELF 文件和哈希验证。该模块支持基于包的执行模型（packet-based execution）、广泛的 ISA 覆盖以及处理器特定的显示选项。

8. MCore / CSkyV1 处理器模块

新增 MCore（即 CSky V1）架构处理器模块，支持栈指针跟踪、自动栈变量创建，并改进了反汇编输出质量和指令解码准确性。

9. ARM64 Windows 原生构建

IDA 现在提供原生 ARM64 的 Windows 构建版本，可在 Windows-on-ARM 设备上原生运行。

10. 反编译器字符串自动收录

反编译器在反编译过程中恢复的字符串，现在会自动出现在字符串列表中。该列表采用惰性填充（lazy filling），仅包含已被反编译过的函数中的字符串，避免不必要的性能开销。

11. IDB 深链接与片段分享

支持通过深链接（Deep Links）导航到数据库中的特定位置，并可通过新的本地 IPC 通道在已运行的 IDA 实例中打开链接。外部工具（如 HCLI）也可以利用此 IPC 通道。右键菜单中新增"复制链接"和"跳转到链接"操作。

12. IDA Domain API v0.5.0

新版 IDA Domain API 增加了微码和伪代码访问能力，以及对象存储/检索 API。

03

PART

高级语言支持

LANGUAGE SUPPORT

Rust

在输出头部显示检测到的 Rust 版本和使用的 crate 列表

类型化 panic 位置

新增 CM\_CC\_RUST 调用约定

Go

支持 Go 1.18+ 的 buildinfo 模块依赖解析

改进 PIE ELF 二进制文件的 pclntab 发现

从 runtime.newobject 的 RTYPE 参数推导返回类型

DWARF：为 Go 泛型函数注入隐藏字典参数

改进栈参数（vs 溢出空间）检测和标准参数/返回类型识别

新增配置变量 GOLANG\_MAX\_ANON\_NAME\_SIZE

移除 Go 结构体中的零大小字段

改进 duffcopy/duffzero 调用的转换

Objective-C

支持显示/隐藏 Objective-C ARC 函数，识别 iOS 16+ 的 ARC 辅助函数

类型化 \_objc\_{retain,release}\_x<N> ARC 桩函数为 \_\_usercall

04

PART

反编译器改进

DECOMPILER

新增 **Edit type...** 动作（热键 e），可直接在反编译器中选择并编辑类型

调用点渲染参数名称提示（Edit → Plugins → Hex-Rays Decompiler Options → Options 3 → Argument name hints 可配置/禁用）

交互式界面支持折叠代码块（左侧折叠箭头 chevron）

支持反转 if-else 语句（invert then-else）

更激进的数组检测和分散变量应用

更好的大函数参数识别（UDT、Go/Rust 中的数组）

识别 IEEE 754 符号位操作中的 fabs/取反

折叠常量 rol/ror/bswap 操作

将 0/1 转换为 true/false（布尔上下文），0 转换为 nullptr（HO\_CPP\_CONSTANTS 启用时）

对非布尔条件优先使用显式与零比较

将 phi-arm 菱形合并结构化为 if-then-else 而非 goto

将短 if (cond) goto L; ...; L: 前向跳转反转为正常结构

将 memcpy() 调用转换为简单赋值（当可能时）

折叠 try/catch 体内的尾随 v = x; return v;

解引用对只读内存的引用

微码视图支持寄存器、栈/局部变量和块的交叉引用

微码视图中提示描述光标下的子指令

新增基础 C-Tree 查看器

05

PART

反汇编器

DISASSEMBLER

**ARM**：SVE2/SME 反汇编支持、SVE/SME 架构检测与 UI 选项、改进的现代主机 SDK switch case 识别

**TriCore**：全新寄存器查找器、完整类型系统支持、支持 byte/word 寄存器（通过 tricore.cfg）、新增重定位支持、switch 处理时尊重内存映射、tc45x/tc48x/tc49xN/tc4Dx 寄存器映射、改进寄存器对和 16 位子寄存器的 def/use 分析

**RISC-V**：支持 Hazard3 (RP2350) 扩展、Zcmp/Zcmt/Zclsd 压缩指令、Soteria 扩展、shXadd 跳转表检测、c. 前缀打印压缩指令、修复大量解码错误

**V850**：识别更多 switch 模式

**MCore**：栈指针跟踪和自动栈变量创建、改进反汇编输出质量和指令解码

06

PART

加载器

LOADER

ELF：支持紧凑相对重定位（DT\_RELR）

COFF/OMF/PSX：按编译单元在目录树中分组函数

ELF：识别并改进 Linux 内核模块加载，添加 modinfo 到列表头部

ELF/ARM：从 .ARM.attributes 的 Tag\_ABI\_VFP\_args 推断硬件浮点 ABI

07

PART

调试器

DEBUGGER

**GDB**：全面现代化 GDB 远程协议实现——启动时从远程获取已加载库、改进暂停/单步处理、修复内存读取（首字节 0xE0-0xEF 范围）、修复模块重复/空模块、修复超时、修复 vCont/qSupported 探测、修复 qGetTIBAddr 错误处理、修复 swbreak/hwbreak 处理、修复 Windows 上 gdbserver 崩溃、支持库加载停止原因、从 TIB 获取镜像基址、从镜像推断段位宽、使用 fs\_base/gs\_base 寄存器导航等大量修复

**RISC-V**：新增 GDB 后端的 RISC-V 调试支持

**Win32/WinDbg**：修复 TEB 段标签，新增 PEB 段

08

PART

插件、SDK 与 API

PLUGIN SDK API

**IDA Domain API**：v0.5.0 发布，增加微码和伪代码访问、对象存储/检索

**IDAPython**：检测/支持 uv/anaconda/homebrew 管理的 Python，警告 libpython/venv 版本不匹配，暴露 ida\_loader.import\_module()、ida\_lines.add\_sourcefiles 批量 API、ida\_indexer API（Jump Anywhere 后端）

**idalib**：安装时自动激活，支持异步事件处理和 execute\_sync()，随 IDA Home 打包，修复 gen\_disasm\_text、parse\_tagged\_line\_sections 等 API 可用性

**SDK**：新增 dscu.h 头文件（ida\_dscu 模块）用于程序化访问 DSC 基础设施；大量新的基于 EA 的 API（避免 IDA 分配指针）；新增 user\_minsn\_t、user\_minsn\_action\_t、minsn\_locator\_t 等微码 API；新增 ev\_query\_unmapped\_address、ev\_load\_unmapped\_address、ev\_sanitize\_name、ev\_should\_handle\_switch、ev\_get\_stkarg\_parts 等事件；新增 codegen\_t::should\_handle\_switch() 钩子；新增 function\_item\_iterator\_t、function\_parent\_iterator\_t、function\_tail\_iterator\_t 等迭代器类

09

PART

UI/UX 改进

UI UX

**统一脚本窗口**：取代旧的"执行脚本"/"Snippets"对话框，整合四个垂直标签页——执行脚本/Snippets（IDB 驻留代码片段，以树形展示）、最近脚本（外部脚本路径，合并单子文件夹链，显示 extlang 图标）、示例（IDAPython 内置示例）、搜索（跨以上三个来源搜索）

**Xrefs Graph 重新设计**：新增图形管理器（dockable 小部件，按文件夹管理已保存图形，含实时节点计数）；节点头部信息（注释、书签、断点、缺失引用）；重新设计的设置面板（更少杂乱、更合理分组）；Sugiyama 风格分层布局；Pathfinder 路径高亮；Pathfinder 图形自动归档到专用 Paths 文件夹

**编译单元文件夹**：函数可按编译单元在函数列表中分组（从 COFF/PSX/OMF/TDS/DWARF/PDB/GO 以及任何调用 add\_sourcefile() 的用户加载器重建）

**深链接**：通过本地 IPC 通道在已运行的 IDA 中打开特定数据库位置的链接；右键菜单新增"复制链接"和"跳转到链接"图标操作

首次启动时显示发布说明

改进浮动许可借用工作流

多项暗色主题修复（树视图展开/折叠箭头、macOS 提示弹窗标题、合并视图详情面板文字、Windows 11 风格适配）

导航栏点击数据地址可从伪代码视图切换到 IDA-View 并跳转

调试器下双击栈变量跳转到对应栈内存位置

10

PART

性能优化

PERFORMANCE

DWARF：加速加载（含行号导入）并减少大型 DWARF 文件的内存使用

内核：加速添加大量名称（如 Dyld Shared Cache）的加载

B-Tree：减少缓存和空闲页清理开销

帧分析加速、新增写入交叉引用缓存

加速 MSVC PE 二进制文件（大量使用 C++ 异常处理）的加载

Swift：增量标记 swiftcall 调用者，而非每次分析波重新扫描

热路径跳过 32 位高位标志获取

11

PART

总结

SUMMARY

IDA 9.4.260915 是一次涵盖面广、深度十足的更新。从 Apple 生态的 DSC 工作流重构，到 Swift ABI 的原生识别，再到 Pathfinder 和 Jump Anywhere 带来的导航体验提升，每一项改进都直击逆向工程师的日常痛点。新增的 Hexagon 和 MCore 处理器模块进一步拓宽了 IDA 的硬件覆盖范围，反编译器字符串自动收录、深链接与片段分享、Xrefs Graph 重新设计等细节改进则大幅提升了日常工作流的效率。Git 团队协作支持和 IDA Domain API 的持续演进让 IDA 在团队协作和自动化分析方面更加成熟。对于所有逆向工程师而言，IDA 9.4 是一次值得关注的重要升级。

种子链接

```
magnet:?xt=urn:btih:9abff06f074734094e5a241bbd83d33b279508e2&dn=ida94sp1&xl=3682681299&tr=udp%3A%2F%2Ftracker.corpscorp.online%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=https%3A%2F%2Ftracker.7471.top%3A443%2Fann...