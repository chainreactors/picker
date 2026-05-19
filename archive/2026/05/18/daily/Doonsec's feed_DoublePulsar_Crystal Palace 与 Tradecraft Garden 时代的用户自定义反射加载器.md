---
title: DoublePulsar:Crystal Palace 与 Tradecraft Garden 时代的用户自定义反射加载器
url: https://mp.weixin.qq.com/s/dQDFrouR3t9DH6I8vR8xEg
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:35.835322
---

# DoublePulsar:Crystal Palace 与 Tradecraft Garden 时代的用户自定义反射加载器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nShyduQReIAOsZ7nqMzic9kE0ibhYricOYmbApdf72Ao54iaU8EDmr44ZuDATX2EiaFpYm45czTFqknsMBx4J5MWzt4MOO3gVPsnMrSc/0?wx_fmt=jpeg)

# DoublePulsar:Crystal Palace 与 Tradecraft Garden 时代的用户自定义反射加载器

memn0ps
memn0ps

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://memn0ps.github.io/doublepulsar-a-user-defined-reflective-loader-in-the-crystal-palace-and-tradecraft-garden-era/ | memn0ps |

**免责声明：**本文是对 DoublePulsar 的技术解读 —— 这是一个我在个人 GitHub 上构建并维护的开源 User-Defined Reflective Loader。文中讨论的技术均非首创，它们已被安全研究社区公开知晓并记录多年，文中也对开发这些技术的研究者和项目给予了相应致谢。本文并非对任何终端安全产品或商业 C2 框架的评价、比较或批判，也不会对任何专有软件进行逆向工程。文中展示的所有调试器输出、内存转储、调用栈以及静态分析，均针对 DoublePulsar UDRL 本身。Beacon 在全文中始终被视为不透明的加密载荷，从未被检查、反汇编或逆向工程。文中提及具体产品、检测规则或研究成果，仅为致谢已有的公开工作，而非对厂商进行排名或暗示任何产品存在不足。本文的目的是揭示这些技术，并同等地提升所有人 —— 无论是攻击工具构建者还是防御检测工程师 —— 的安全意识。

## 摘要

对手与红队会将其工具直接加载到计算机内存中，而不向磁盘写入文件，这使其对传统基于文件的安全产品不可见。控制这种内存加载过程的组件称为反射加载器 ( reflective loader )。Cobalt Strike 作为使用最广泛的对手模拟框架之一，允许操作者用自定义加载器 —— 即 User-Defined Reflective Loader ( UDRL ) —— 替换其默认加载器，从而完全掌控植入体在内存中的加载与隐藏方式。

DoublePulsar 是一款用 Rust 编写的 UDRL，它添加了多层隐蔽机制：将植入体藏匿于合法系统模块的内存中、在空闲时对其加密、伪造其调用历史以伪装成正常的系统活动，并将其内存分配与进程的其余部分隔离开来。对于防御方而言，仅依赖基于特征码的检测是不够的。本文提供了检测策略、YARA 规则，以及 MITRE ATT&CK 映射，以帮助安全团队识别此类威胁。

## 背景与上下文

Reflective DLL Injection 由 Stephen Fewer 于 2008 年首次发表，引入了一种在不使用 Windows 加载器的情况下完全在内存中加载 DLL 的技术。其关键创新在于将加载逻辑直接编译进 DLL 自身，作为一个名为 `ReflectiveLoader()`的导出函数。位于 DOS 头中的一小段 shellcode 桩会将执行流引向该导出函数，后者随后分配内存、映射 PE 节区、解析导入、应用重定位，并调用入口点。这使得 DLL 具备了自加载与位置无关的特性。

2017 年，Nick Landers 发布了 Shellcode Reflective DLL Injection ( sRDI ),将该理念进一步推进 —— 将加载器与 DLL 完全分离。sRDI 不再将加载器作为导出函数嵌入，而是将位置无关的加载器 shellcode 前置于目标 DLL 之前。这使得任意 DLL 都可以在不修改自身的前提下被转换为可注入的 shellcode。同年，对 DoublePulsar 用户态注入器 —— 一款由 NSA 旗下 Equation Group 开发、并经 Shadow Brokers 泄露的植入体 —— 的分析揭示了类似的前置加载器架构。DoublePulsar 的名称即取自这一植入体。

Cobalt Strike 较早便采用了反射加载方式，并在 4.4 版本 ( 2021 年 ) 中引入了 User-Defined Reflective Loader ( UDRL ) API，以赋予操作者对 Beacon 加载入内存方式的完全控制。UDRL 用操作者提供的代码替换 Cobalt Strike 默认的 `ReflectiveLoader()`,这些代码可以嵌入 Beacon DLL 内部，也可以前置于其之前。Robert Bearsby 的 Revisiting the UDRL 博客系列记录了这两种方法，并提供了 UDRL-VS 开发套件。

![Prepended vs Embedded Reflective Loader](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiajNGCBd2utyfudStZaEUlav6Z8Aia5Zo7r2Hfgr6ibz44t5SdrzVDyLkV8jFfy5eIP2Abyt8WcMFyy2OoXIAk1eHCyWQIEec11Q/640?wx_fmt=png&from=appmsg)

Prepended vs Embedded Reflective Loader

**图 1:***前置式与嵌入式反射加载器架构对比 ( 图示来自 Robert Bearsby / Cobalt Strike 的 Revisiting the UDRL Part 1 )*

相较于 Cobalt Strike 默认加载器，自定义 UDRL 的价值在于控制力。若不使用 UDRL，默认反射加载器会根据 Malleable C2 配置文件中的任意设置创建一块全新的内存分配，这有可能抵消 shellcode 运行器为将载荷送入内存而做出的所有规避工作。这种"套娃"问题正是促使大多数操作者转向编写自定义 UDRL 的原因。默认加载器的行为已被充分记录、特征化并易于检测。UDRL 能够控制内存分配策略、节区权限、导入解析，并可在加载流水线的每个阶段注入规避原语。诸如 Austin Hudson 的 TitanLdr、Kyle Avery 的 AceLdr,以及 Bobby Cooke 的 BokuLoader 等公开 UDRL 表明，操作者可以构建具备 module stomping ( 模块踩踏 )、返回地址伪造、堆隔离与睡眠混淆能力的加载器。IBM X-Force 的反射加载器分析介绍了基础概念。Lorenzo Meacci 基于 Crystal Palace 开展的 EDR 规避研究,以及 RastaMouse 的 Crystal-Kit,演示了一些高级技术，包括借助 `.pdata`注册实现的模块重载 ( module overloading )、`NtContinue`入口转移以及睡眠掩蔽 ( sleep masking )。Crystal Kit 通过挂钩 `BEACON_RDLL_GENERATE`( 使其成为一个 UDRL ),并使用 PICO ( Position-Independent Code Objects，位置无关代码对象 ) 在加载器旁边运行规避技战法，同时通过 `POSTEX_RDLL_GENERATE`支持后渗透 DLL 加载。

### Crystal Palace、Tradecraft Garden 与 UDRL

Cobalt Strike 加载生态系统的最新进展是 Crystal Palace,一款由 Raphael Mudge 维护的开源 PIC 链接器及链接器脚本语言。Tradecraft Garden 提供了示例加载器以及一个共享库 ( `libtcg`),用于 DLL 加载、PICO 运行和调试输出。RastaMouse 的 Crystal-Kit 将这些组件打包为一套开箱即用的 Cobalt Strike 规避套件。

其架构与 TitanLdr、AceLdr 和 DoublePulsar 等传统 UDRL 有相当大的差异。传统 UDRL 编译为 PE，通过 `objcopy`将其`.text`节提取为原始 shellcode，并在一个单体二进制中处理一切:PE 加载、导入解析、重定位、挂钩和规避。Crystal Palace 则采用模块化方式。操作者编写 C 源文件，这些文件编译为 COFF 目标文件 (`.o`),而非 DLL。随后 Crystal Palace 通过规范文件 (`.spec`) 将这些目标文件链接在一起，规范文件控制各组件如何组合、解析哪些函数，以及安装哪些挂钩。`MODULE$Function`模式 ( 例如`KERNEL32$VirtualAlloc`) 在链接期完成动态函数解析，因此操作者无需编写 PEB 遍历或基于哈希的 API 解析代码。Crystal Palace 还提供链接期优化 (`+optimize`)、代码变异 (`+mutate`) 和函数重排序 (`+disco`)。

其关键架构概念是 PICO ( Position-Independent Code Object，位置无关代码对象 )。PICO 是 Crystal Palace 在内存中运行 COFF 目标文件的约定，类似于 BOF，但不依赖 Beacon 特定的 API。在 Crystal Kit 中，规避技战法 ( IAT 挂钩、调用栈伪造、睡眠掩盖 ) 存在于一个与加载器并行运行的 PICO 中，而非嵌入到加载器内部。加载器加载 Beacon DLL 和 PICO，调用 PICO 的初始化函数 ( 例如 `setup_hooks`、`setup_memory`),PICO 则通过 spec 文件中的 `addhook`指令在加载时对 Beacon 的导入进行打补丁。这种分离意味着操作者可以更换规避组件而无需重写加载器本身。

Crystal Palace 降低了 PIC 开发的门槛。以往需要理解链接器脚本、节顺序、PIC 字符串处理和手动 API 解析的操作者，现在可以专注于编写 C 代码，让 Crystal Palace 处理位置无关性约束。共享库 `libtcg`开箱即用地提供了 DLL 加载和导入解析。这种易用性使其成为新版 Cobalt Strike 加载器开发中最流行的方式。

然而，规避能力取决于操作者用它构建了什么。Crystal Kit 在发行版中通过 `VirtualAlloc`分配 Beacon 内存 ( 产生无支撑的私有内存 ),使用 128 字节密钥的基于 XOR 的睡眠掩盖，并通过 kernel32 ( `LoadLibraryA`/ `GetProcAddress`) 解析 API。这些是有效的起点，不过操作者也可以在 Crystal Palace 之上构建更高级的技战法，正如 Lorenzo Meacci 所演示的那样。

Crystal Palace 并不阻止操作者编写高级规避能力。Lorenzo Meacci 的工作证明，模块重载、用于栈展开的 `.pdata`注册，以及基于 `NtContinue`的入口转移，在 Crystal Palace 框架内都是可实现的。然而，这些技术并不属于公开发行的 Crystal Kit。Crystal Palace 作为链接器可以支持它们，只是需要在开箱即用的内容之上投入大量额外开发。

像 DoublePulsar 这样的专用 UDRL 采用单体方式：所有内容都编译进一个位置无关的二进制文件中，负责 PE 加载、导入解析、重定位、模块踩踏、基于 NtContinue 的睡眠混淆、堆隔离、CFG 绕过，以及从 `.pdata`展开信息构建合成调用栈。代价在于开发投入:Crystal Kit 让操作者凭借模块化组件迅速上手，而单体式 UDRL 则需要从头编写并维护其中的一切。

还有第三条值得考虑的路径：像 Havoc Professional 这样的框架，由 C2 框架本身通过模块化扩展系统处理规避，从而将加载器开发负担完全从操作者身上移除。下文会进一步展开。

### 在 UDRL 与 Crystal Kit 之间做选择

无论是专用 UDRL 还是 Crystal Kit，最终结果都是一样的:Beacon 被加载到内存中，并应用了规避技战法。两种方式并无本质优劣之分。它们以不同的取舍解决相同的问题，选择哪种取决于开发者是谁、有多少时间、以及需要多大程度的控制权。

| 维度 | 专用 UDRL | Crystal Kit / Crystal Palace |
| --- | --- | --- |
| **架构** | 单体。一切都在一个二进制中：加载器、挂钩、睡眠、伪造 | 模块化。加载器 + 用于技战法的独立 PICO，通过 spec 文件链接 |
| **编译** | 编译为 PE，通过 `objcopy`将 `.text`节提取为 shellcode | C 源码编译为 COFF `.o`文件，由 Crystal Palace 链接 |
| **API 解析** | 手动 PEB 遍历，由开发者编写的 DJB2 / ROR13 哈希解析 | 由 Crystal Palace 通过 `MODULE$Function`DFR 模式和 `libtcg`处理 |
| **PE 加载** | 开发者自行编写或改写：`ParseDLL`、`LoadDLL`、`ProcessImports`、重定位 | 由 `libtcg`共享库开箱提供 |
| **规避技战法** | 直接内建于加载器二进制中 | 存在于独立的 PICO 中，与加载器并行加载 |
| **技法替换** | 修改源码、重新编译 | 在 spec 文件中替换 PICO，重新链接而无需触碰加载器 |
| **链接期特性** | 自带。编译期混淆 ( 不透明谓词、控制流平坦化 )、自定义基于 VM 的混淆器，或操作者掌控的任意工具链 | `+optimize` ( 死代码移除 )、`+mutate`( 代码变异 )、`+disco`( 函数重排序 ),由 Crystal Palace 提供 |
| **工具链** | Rust / C 编译器 + 链接器脚本 + objcopy | MinGW GCC + Crystal Palace JAR ( Java ) + spec 文件 |
| **后渗透加载器** | 编写一个独立的加载器或复用同一个 | `POSTEX_RDLL_GENERATE` 钩子，共享 PICO 技战法 |
| **学习曲线** | 高。必须理解 PIC 约束、PE 格式和 Windows 内部机制 | 较低。Crystal Palace 抽象了 PIC 约束，`libtcg`处理 PE 加载 |
| **控制权** | 完全。每一个字节都归你所有 | 部分。Crystal Palace 控制链接、DFR 和代码布局 |
| **检测响应** | 修补具体代码路径，重新编译，完成 | 可能需要修改 PICO、加载器或 spec 文件，取决于被检测的内容 |
| **团队可扩展性** | 困难。编写者即维护者 | 良好。资深开发者构建加载器，初级操作者按实战替换 PICO |

**专用 UDRL 适合以下情形：**

* 你是独立操作者或具有深厚 Windows 内部机制知识的小团队
* 你需要对加载过程的方方面面拥有完全控制，从内存分配策略到精确的 API 调用序列
* 你希望通过修补被标记的精确代码路径来快速响应新的检测规则，而无需等待上游工具链更新
* 你正在构建超出加载范畴的私有工具 ( 自定义睡眠链、自定义调用栈伪造、针对你操作需求的特定堆隔离策略 )
* 你不希望依赖外部工具链 ( Crystal Palace 是一个 Java 应用程序 ) 或别人的链接约定
* 你乐于编写并维护 PIC 代码、手动 API 解析、PE 解析和重定位处理

**Crystal Kit 与 Crystal Palace 适合以下情形：**

* 你处于一个技能水平参差不齐的团队中，需要让操作者在不理解 PIC 内部细节的情况下部署规避技战法
* 你在某次实战中受时间所限，需要快速获得一个可用的加载器，而无需从零开始编写 PE 加载和导入解析
* 你希望通过替换 PICO ( 挂钩、睡眠掩盖、调用栈伪造 ) 来试验不同的规避技术，而无需重写加载器
* 你希望获得链接期优化 ( `+optimize`移除未使用的代码，`+mutate`提供多态性，`+disco`随机化函数顺序 ),而不必自行实现
* 你既需要一个 Beacon 加载器 ( `BEACON_RDLL_GENERATE`),又需要一个后渗透加载器 ( `POSTEX_RDLL_GENERATE`),且两者共享同一套技战法组件
* 你希望以 Tradecraft Garden 的示例加载器作为起点，而非从零搭建
* 相比应对 PIC shellcode 开发的种种约束 ( 没有 `.data`节，没有字符串字面量，没有 CRT ),你更习惯编写 C 代码

**实践中的取舍：**Crystal Kit 凭借模块化组件让操作者在数小时内就能上手。专用 UDRL 则需要数周乃至数月才能构建完成，但能让开发者对代码拥有完全所有权。当一条新的检测规则出现时 ( 例如与 DoublePulsar 同月出现的 Elastic 调用栈模式规则 ),UDRL 开发者可以在自己的代码中修补具体的 gadget 源码、具体的栈帧布局或具体的字节模式并重新编译。Crystal Kit 操作者则可能需要等待上游 PICO 更新，或自行编写一个新的 PICO —— 而这恰恰需要该框架本意要抽象掉的那套 PIC 开发技能。

两者最终都能产出可工作的、具备规避能力的加载器。选择关键在于你是谁、需要什么。

像 Havoc Professional 这样的集成框架代表了第三条路径：由 C2 开发者在框架层面处理规避，降低操作者构建或维护独立加载器的需要。这回应了现实状况：咨询公司受时间所限，C2 许可证价格不菲，在一个本就昂贵的框架之上再写一个自定义加载器是额外的研发投入，并非每个团队都能承担。这并不能消除所有定制工作，操作者仍可能需要应对特定场景，但它将加载器开发的负担完全从操作者身上移除。

DoublePulsar 完全用 Rust 编写，是首批公开发布、达到此种规避能力水平的 Rust 编写的概念验证 UDRL 之一。同样的技术和原语适用于任何语言。用 Rust 进行 PIC 开发的公开文档较少，在...