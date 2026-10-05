---
title: IDA 9.5 Beta 发布：三大新反编译器、位域支持、Apple 内核缓存与 FLIRT 2.0
url: https://mp.weixin.qq.com/s/w-NQw38TIF_l-VSsNgwc9w
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:58.262869
---

# IDA 9.5 Beta 发布：三大新反编译器、位域支持、Apple 内核缓存与 FLIRT 2.0

# IDA 9.5 Beta 发布：三大新反编译器、位域支持、Apple 内核缓存与 FLIRT 2.0

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# IDA 9.5 Beta 发布：三大新反编译器、位域支持、Apple 内核缓存与 FLIRT 2.0

Hex-Rays 正式放出了 **IDA 9.5 Beta**。这是一个分量很足的版本：新增 Dalvik、TriCore、Hexagon 三个反编译器，为 C 位域提供原生反编译支持，重写了 AVX/SSE 处理管线，引入 Apple kernelcache 加载器、逐字（verbatim）名称、FLIRT 2.0，以及更聪明的 switch-case 恢复和递归式 “Create C file” 导出。

与此同时，从 9.5 开始，**Malware Analysis、Teams、Lumina、Assist 和 IDA MCP 等附加组件与 IDA 核心版本解耦**，各自独立版本化、独立发布，修复与新能力不再需要等待下一个 IDA 大版本，可直接就地更新到已安装的 IDA 上。

---

## 一、三大新反编译器

### 1. Dalvik 反编译器

IDA 现在可以**把 Android DEX 字节码反编译成 Java 伪代码**。它建立在 DEX 文件的类型化模型之上——类、字段、方法、参数都是真实、可重命名、可改类型的实体，改动任意一个都会贯穿到伪代码中。

* • 新增**类视图（class view）**，列出程序的类及每个声明中的字段与方法，提供伪代码提示和 “Move function to folder”；`Ctrl+Shift+F6` 或在类树中 `Ctrl+双击` 可打开新的类视图。
* • 多 dex 应用中，一次调用能到达另一个 dex 文件里的方法体；虚调用还会引用子类中的覆写实现。
* • 从 DEX 异常表重建 `try`/`catch` 块；使用优化字节码（odex）的方法同样可以反编译。
* • 尽可能恢复被混淆的名称：Kotlin metadata、序列化注解、DEX 调试信息。
* • 输出更接近源码：字符串拼接显示为 `"a" + b`（而不是 `StringBuilder.append()` 链）；嵌套类打印为 `Outer.Inner`；显示泛型、注解 `@Foo(...)` 和匿名类 `new Type() { ... }`；方法参数按 DEX 注解命名。
* • `try`/`catch`/`finally` 通过支配性分析重建，支持嵌套块、catch-all 处理器、以 `return`/`goto` 结尾的 `finally`，以及多出口的 `synchronized` 块。

对脚本和插件而言，新增了**语言无关的类 API**（`get_classes()`、`get_class_info()`、`render_class()`、`render_member()`，C++ 与 IDAPython 均可用），Dalvik 是它的第一个后端。

> **局限**：暂不支持重建 try-with-resources（输出更长但正确），且输出的是 Java 而非 Kotlin。

### 2. TriCore 反编译器

针对 Infineon TriCore，新插件 `hextricore` 可反编译 TriCore 代码，支持 `eabi` 与 `Tasking` 两套 ABI 族。

### 3. Hexagon 反编译器

针对 Qualcomm Hexagon（QDSP6），新插件 `hexqdsp6` 可反编译 DSP 代码。它能对**包（packet）语义**建模——并行读、`.new` 值、谓词执行——并处理硬件循环、复合分支、跳转表、浮点和标量 SIMD 指令；HVX 向量与系统指令以 intrinsics 形式呈现。

* • 包内每条指令读取的都是包开始时的寄存器值，`.new`/`.cur` 操作数可见包自身的结果，谓词指令会转成条件块。
* • 识别变参函数。
* • intrinsics 使用 clang 的 `__builtin_HEXAGON_*` 命名，语义可在 `hexagon_protos.h` 中查证。
* • HVX 向量（`V0`–`V31`、`Q0`–`Q3`）被建模为向量寄存器。

---

## 二、反编译器支持位域

访问 C 位域成员 时，不再显示成移位与掩码运算，而是显示为成员访问：

* • `(*(_DWORD *)&s >> 3) & 7` 读作 `s.field`
* • `*p = *p & 0xFFFFFF07 | (v << 3) & 0xF8` 读作 `p->field = v`（前提是类型被正确定义并应用）

它覆盖反编译器支持的所有架构，包括 ARM64、PPC、MIPS、RISC-V 专用的 extract/insert 指令。该功能默认开启，可在 **Edit > Plugins > Hex-Rays Decompiler Options > Options 2** 中用 “Decompile bitfield accesses” 关闭。

下面这个 MSVC 的 xor 开关写法很能说明问题：

```
struct s4 { unsigned a : 4; unsigned b : 4; unsigned rest : 24; };
void inc_a(struct s4 *p) { p->a++; }

// 9.4
*(_DWORD *)p ^= ((unsigned __int8)*(_DWORD *)p ^ (unsigned __int8)(*(_DWORD *)p + 1)) & 0xF;

// 9.5
++p->a;
```

更多可识别形态：

```
// 9.4
if ( ControlPc >= ((*((_DWORD *)v1 + 1) >> 6) & 0xFFFFFC) + v1->FuncStart )
if ( (v16 & 0xC0000000) == 0x80000000 )
if ( *((int *)this->m_pDevice + 5442) < 0 )

// 9.5
if ( ControlPc >= 4 * v7->FuncLen + v7->FuncStart )
if ( FunctionEntry->Flags == 2 )
if ( this->m_pDevice->m_TimingCaptureActive != 0 )
```

位分配顺序默认与字节序方向一致，但可针对特定类型翻转。Xbox 360 二进制中这种情况很常见（GPU 寄存器或继承自 Windows 内核的结构使用小端位域顺序），此时可用 `#pragma bitfield_order(lsb_to_msb)` 或 `__invbf` 标注。当存在带完整类型信息的 PDB 时，会据此自动检测位序。

---

## 三、SSE/AVX/AVX2/AVX-512 全面增强

过去 AVX 代码常常反编译成一堆 `__asm` 块。新插件 `avxlifter` 把 AVX、AVX2、AVX-512（F/CD/BW/DQ/VBMI/VNNI/BF16/FP16/VL）以及 VMX 指令转成**原生微码**，让反编译器能够推理它们；否则也转成作用于 `__m128`/`__m256`/`__m512` 的 `_mm*_…` intrinsics，包括掩码 EVEX merge/zero 形式、gather/scatter、compress/expand 和 opmask `k` 寄存器。

* • packed and/or/xor/andnot 变成 C 运算符，符号翻转与绝对值掩码读作 `a ^ signmask`、`a & absmask`，`vxorpd x, x, x` 就是 `0.0`。
* • 标量 FMA 与 min/max 变成 C 数学函数（`fminf`、`fmaxf`），不再是 `_mm_*_ss` intrinsics。
* • 无副作用的 intrinsics 被标记为 pure，死向量计算会被消除。
* • XMM、YMM、ZMM 被建模为同一寄存器的不同视图，legacy-SSE 写入会保留高位；不再出现虚假的未定义 YMM 变量。
* • 向量 union 新增 `__int128` 成员，去掉了 `*(_OWORD *)` 强制转换。
* • SIMD 加载/存储、`memcpy`/`memmove` 和结构体拷贝都是普通赋值，不再残留 `_mm_loadu_si128`/`_mm256_storeu_ps`。
* • 用 `movups`/`movsd`/`mov`/`movzx` 逐段拷贝的字符串字面量（含 UTF-16 和 MSVC 混合宽度拷贝）被识别——这属于分析而非 lifting，因此不装插件也生效。
* • 对齐帧指针的函数（`and rbp, -32`，AVX 代码典型写法）重新拥有栈变量，而不是 `&v3 & 0xFFFFFFFFFFFFFFE0`。

---

## 四、Apple Kernel Cache 加载器

IDA 9.5 对 Apple kernelcache 做的事，正如 9.4 对 dyld shared cache 所做：**kernelcache 是一组 KEXT 的集合**，IDA 现在把它当作一个整体处理，而不是单个巨大的 Mach-O。一个链接后的 kernelcache（系统或辅助）会与它引用的 boot KC 一起作为连贯集合处理：单一布局，符号与引用跨链接解析。

* • **KC Index** 部件列出当前集合中的所有 KEXT，可按来源过滤，并按需映射——内核优先，其余在访问时映射。
* • 从 `OSMetaClass` 重建 C++ 运行时——类层次、带完整签名的虚方法、metaclass vtables——并按缓存 OS 版本匹配的 XNU 类型库为 `OSDynamicCast` 结果、`kalloc_type` 描述符和类型化分配赋予类型。
* • **Locate > Symbol / String / Address** 直接从文件搜索整个缓存，因此你从未加载过的 KEXT 也能像其他 KEXT 一样被搜索；在被完全 strip、没有任何符号表的缓存上，字符串搜索依然有效。
* • Functions 列表中每个 KEXT 或缓存镜像一个文件夹，按 bundle id（`com/apple/iokit/...`）嵌套；`kcu.cfg`/`dscu.cfg` 中的 `FUNC_FOLDER_FORMAT` 控制布局，设为 `""` 则保持扁平。
* • 附带示例插件可将某个 KEXT 或 dyld 缓存镜像提取为独立 Mach-O（KC/DSC Index 中的 “Extract Mach-O image to file...”，`Ctrl+Alt+Shift+M`）。结果可分析但不可运行，因为它不含 rebase/bind 信息。

---

## 五、逐字函数名与类型名

现代语言（Rust、Go、Swift、重度模板化的 C++）用 C 标识符非法的字符命名。IDA 不再把它们篡改成 ASCII 安全形式：**符号名、类型名、成员名现在按原样保留**，来自符号表、demangler 和调试信息即是如此。

```
// 9.4
__core::fmt::ArgumentV1_
struct mut_ref_dyn_core::fmt::Write

// 9.5
&[core::fmt::ArgumentV1]
struct &mut dyn core::fmt::Write
```

* • 新数据库默认显示 demangled 名称。
* • `A::B::C` 这类限定名在反汇编、伪代码和打印原型中都会作为整体高亮、选中和交叉引用。
* • FLIRT 签名可携带原始（未改编）名称，Go/Rust/Swift 命名全程保留。
* • 非 C 类型名与成员名可经由 Edit-type 对话框忠实往返。
* • 经典行为可按数据库通过 `GarbleNames` 策略保留（在数据库创建时固定）；已有数据库保持现状。

> **迁移提示**：该策略在数据库创建时固定。9.5 之前创建的数据库仍会篡改名称，因此在既有脚本下名称不会发生变化。

---

## 六、FLIRT 2.0

经典 FLIRT 依靠字节识别库函数，但函数内部调用的目标会被链接器重定位，FLIRT 只能把这些字节当作通配符，也就丢掉了它们指向谁——一个自身没有可靠特征的 helper 便始终无名。

**FLIRT 2.0 签名（v11 格式）额外记录每个库模块引用了什么。** 一旦 `library_function` 被匹配、它的调用落到了某个地址，IDA 就知道那里的函数是 `hidden_helper`。自动分析之后，一个延迟 pass 会为这类由已识别代码到达的函数命名，并用同样的证据在字节完全相同的候选中做出选择。

在一个 strip 过的静态链接 sqlite3 上，正确命名的函数数量对比：

| Runtime | 9.4 | 9.5 |
| --- | --- | --- |
| glibc amd64 | 1279 | 1846 |
| glibc i386 | 1424 | 1826 |
| glibc arm64 | 1434 | 1815 |
| glibc armhf | 776 | 1204 |
| glibc riscv64 | 288 | 933 |
| glibc s390x | 1398 | 1739 |
| MSVC /MT x64 | 565 | 698 |
| MSVC /MT x86 | 458 | 561 |
| MSVC /MT arm64 | 0 | 753 |
| MSVC /MT arm | 0 | 622 |

* • 识别 32 位 VC 14.39–14.52 二进制，ARM/ARM64 MSVC 运行时签名覆盖 VC11 至 VC 14.52。
* • `main`/`wmain` 与 `WinMain`/`wWinMain` 依据二进制中的证据区分；startup 签名会命名其 entry module 引用的函数与数据。
* • 签名可携带原始未改编名称：Go 运行时签名保留 `runtime.(*mheap).alloc`（旧的改编版以 `*_legacy.sig` 形式随附）。
* • 签名加载更快（批量缓冲读取）。

> **迁移提示**：sigmake 现在总是写 v11。IDA 9.5 能读取旧 `.sig`，但 IDA 9.4 及更早版本会拒绝 v11，因此用 9.5 FLAIR 工具构建的签名无法在 9.4 中加载。

---

## 七、更精确的 switch-case 恢复

* • 被编译器拆成二分查找分派的 switch 会被重新拼合：嵌套在相等/范围守卫下的 switch 合并进父级，被这类守卫隔开的两个 switch 合二为一。
* • 建立在 pivot 相减选择子（`switch (x - C)`）上的跳转表会被重基到原始值，从而恢复真实的 case 标签。
* • 更好地从 if 链恢复 switch，包括 case 会 fall-through 的分派树，以及从外层循环离开的 getopt 风格树。
* • case 按值排序，共享主体的 case 合并，仅跳入另一 case 的 case 折入其中。

共享 case 尾部现在以 fall-through 呈现：

```
// 9.4                     // 9.5
case0u:                   case0u:
  result = 1;                result = 1;
goto LABEL_3;            case1u:
case1u:                     ++result;
LABEL_3:                   case2u:
  ++result;                  ++result;
goto LABEL_4;            case3u:
case2u:                     ++result;
LABEL_4:                     break;
  ++result;
  ...
```

在 x86、ARM、MIPS、RISC-V、PPC、ARC、V850 和 Dalvik 等所有架构上，反编译器现在**用自己对微码的数据流分析**来查找跳转表，而不再复用反汇编器的 switch 信息。反汇编器漏掉的 switch（“switch analysis failed”）得以恢复，重复的 switch 被合并，许多以前反编译错误的现在正确了：

```
// 9.4
if ( v67 <= 8 )
  switch ( (unsigned int)(a3 + 7) >> 3 ) { ... }

// 9.5
switch ( v67 ) { ... }
```

---

## 八、递归式 “Create C file”

**File > Produce file > Create C file...**（`Ctrl+F5`）现在在 “All functions”（或选中项）之外新增了 **“Current function and its callees recursively”**。被调用者会先被反编译，自叶子向上，因此每个函数都在它调用的函数之后处理，恢复出的原型会改善调用者的伪代码。

* • 会沿 `.plt` 与 stub thunk 跟进到真实函数；跳过导入；根函数始终包含，仅对其被调用者过滤。
* • 对话框提供 “Skip debugger segments”、“Skip library functions”（默认开启）和 “Decompile to cache only”（不写文件，仅报告反编译了多少函数）；选项在会话间记忆。

---

## 九、上层语言支持

### 反汇编器恢复 Swift 字符串

Swift 编译器把字符串表示为两个 64 位立即数：小字符串直接内嵌，大字符串字面量是带标签指针，指向前方固定偏移处。IDA 9.5 内建了这套解码逻辑，解码 Swift 字符串\*\*并把它们加入 String 窗口（Shift-F12）\*\*便于引用，背后由新的 Synthetic Strings API 支撑，插件也可使用。

```...