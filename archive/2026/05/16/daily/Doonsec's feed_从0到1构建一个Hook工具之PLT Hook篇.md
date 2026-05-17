---
title: 从0到1构建一个Hook工具之PLT Hook篇
url: https://mp.weixin.qq.com/s/WQ-ofhO88sWULwZb1bhFKA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:17.015299
---

# 从0到1构建一个Hook工具之PLT Hook篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K09ICAXtQHMbbLK2wzewQxXJIKyySvuNGWsEse8Fibcz3ShU9BWI1UqBDZNAO2WkJdmbQpBnfIurLFRjibpfdCFSS1zmLd0ribVTE/0?wx_fmt=jpeg)

# 从0到1构建一个Hook工具之PLT Hook篇

n\_1ng
n\_1ng

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 在前面的几篇文章里，我们已经把注入器和 Java Hook 这两部分大致梳理了一遍。继续往下走，一个比较自然的问题就是：如果目标不再是 Java 方法，而是 so 里的 native 函数，那 Hook 又该怎么做？

##

Native Hook 这件事如果再往下拆，其实又可以分成几条路。最常见的两类，一类是直接改机器码的 Inline Hook，另一类是利用动态链接过程留下来的导入表/重定位信息做 PLT Hook。相较之下，PLT Hook 更适合作为一个 Native Hook 框架的第一步：它不用上来就硬改目标函数入口，而是优先利用 ELF 和动态链接器已经准备好的信息。

**目标**

这篇文章我们先把目标定在实现一个可用的plt hook demo。

项目地址：https://github.com/x1aon1ng/Nook

读完之后，我希望至少能把下面这些问题讲明白：

* PLT Hook 到底 Hook 的是什么？
* 一个导入函数在运行时是如何通过 GOT/PLT 被调用的
* `PLT Hook`

  为什么本质上是“改重定位结果”
* 为什么改一个槽位里的函数指针，就能劫持 native 调用？
* 一次`hook_symbol()`调用在内部究竟经历了哪些步骤？

##

**知道这些基础后会更好理解下文**

### 1. ELF 与 so

在 Android/Linux 里，native 动态库本质上就是 ELF 文件。`libxxx.so`被加载进进程后，并不是简单把文件原样搬到内存里，而是由动态链接器按照 ELF 中的 program header、dynamic segment、relocation 信息等内容完成装载和重定位。

如果只从 Hook 的角度去看，ELF 里最重要的几类信息是：

* 动态符号表`.dynsym`
* 动态字符串表`.dynstr`
* 重定位表，如`.rel.plt`、`.rela.plt`、`.rel.dyn`、`.rela.dyn`
* `PT_LOAD`

  、`PT_DYNAMIC`这些 program header
* SHT：ELF 里除了 Program Header Table，还有一套 Section Header Table，通常简称 SHT，对应着elf的两种描述视角，这里暂时不展开讲，简单理解上面讲的.dynsym、.dynstr都是section，每个section header都描述了一个section的类型、偏移、大小等信息

后面 的 PLT Hook，本质上就是围绕这些信息展开。

### 2.导入函数

导入函数，简单说就是：

当前模块里“要调用，但实现不在自己这个模块里”的函数。 比如 libnative-lib.so 里写了：

```
strcmp(a, b);
malloc(16);
```

如果 strcmp 和 malloc 的实现都不在 libnative-lib.so 自己内部，而是在别的 so 里，比如 libc.so，那对 libnative-lib.so 来说，strcmp、malloc 就是导入函数。

对应的另一边就是导出函数，我理解的概念大概是：如果一个函数定义在某个 so 里，并且它的符号对外可见、能被别的模块链接和调用，那它就是这个 so 的导出函数。

了解这个概念后，我们就可以回答上面的问题：PLT Hook就是在Hook导入函数。

### 3. 动态链接、PLT 和 GOT

当一个 so 调用另一个 so 里的导入函数时，编译器通常不会把调用点直接写成最终的真实地址。原因很简单：编译时还不知道这个函数在目标进程里最终会被映射到哪里。

于是就有了两层非常重要的中间结构：

* `PLT`

  Procedure Linkage Table，可以理解成导入函数调用的跳板
* `GOT`

  Global Offset Table，可以理解成运行时保存目标地址的槽位表

一个很粗略但够用的理解是：

```
调用点
->
PLT stub
->
GOT 槽位
->
真实函数地址
```

一旦动态链接器完成重定位，GOT 里的某个槽位就会被写成对应导入函数的真实地址。此后，调用链就会顺着这个槽位跳到真正的目标函数里。

所以，所谓`PLT Hook`，从运行时视角看，本质上并不是去改 PLT 机器码，而是去改“PLT/GOT 这条调用链最终依赖的那个槽位里的函数指针”。

所以PLT Hook的本质就是在修改重定位的结果。

### 4. 重定位条目是什么

如果说 GOT 槽位是最终要改的目标，那么 relocation entry 就是“告诉你该改哪里”的索引。

一个重定位条目里，最关键的通常是三个字段：

* 符号索引，说明这条 relocation 对应哪个导入符号
* relocation type，说明这条 relocation 属于哪一类修正
* relocation offset，说明最终要修正的目标位置在哪里

对`PLT Hook`来说，最核心的问题其实就是：

* 先找到目标符号对应的 relocation
* 再拿到它的 offset
* 然后把这个 offset 换算成进程里的真实地址
* 最后在那个地址上把原函数地址替换掉

当地址被替换掉后，自然的就走到了我们的Hook逻辑的，这就是PLT Hook的核心。

### 5. 文件里的 offset 不等于内存里的地址

`ELFIO`解析的是磁盘上的 ELF 文件，而真正的 Hook 动作发生在已经加载到进程内存中的 so 映像上。文件里的 relocation offset 只是“相对于 ELF 映像布局”的偏移，不是可以直接拿来写内存的真实地址。

所以中间必须经过一步 runtime bias 换算。最常见的一种写法是：

```
slot_address = runtime_bias + relocation_offset
```

而`runtime_bias`的求法，通常要结合`PT_LOAD`段和运行时模块基址一起算出来：

```
runtime_bias = runtime_module_base + p_offset - p_vaddr
```

### 6. 为什么要临时 mprotect

GOT/PLT 对应的内存页在运行时往往不是天然可写的，很多时候只有读权限，甚至还会带执行权限。想要在上面改指针，就得先把对应页临时改成可写：

* 先查当前页权限
* `mprotect`

  成可写
* 写入 replacement
* 恢复原来的页权限

### 7. PLT Hook 和 Inline Hook 的区别

这两类 Hook 最大的区别不在“Hook 的函数都是 native 函数”，而在“改的是哪一层”。

`PLT Hook`改的是导入调用链路上的目标槽位，特点是：

* 不直接改目标函数机器码
* 更依赖 ELF 和重定位信息
* 只能影响经过导入槽位发起的调用

`Inline Hook`改的是函数入口处的机器码，特点是：

* 直接劫持目标函数执行流
* 不依赖导入表
* 能覆盖的场景更广
* 但实现难度和风险也更高

**从一个最小例子理解 PLT Hook**

假设有一个目标模块`libnative-lib.so`，它内部调用了`strcmp`。编译和链接完成后，运行时这个调用大致会依赖某个 relocation 对应的 GOT 槽位。

一开始，槽位里装的是原始的`strcmp`地址：

```
libnative-lib.so
->
strcmp 对应的 GOT 槽位
->
libc.so:strcmp
```

如果我们把这个槽位改成自己的`hooked_strcmp`：

```
libnative-lib.so
->
strcmp 对应的 GOT 槽位
->
hooked_strcmp
```

那么后续只要`libnative-lib.so`仍然通过这条导入链路调用`strcmp`，执行流就会先进到`hooked_strcmp`。

而如果在改写前，我们先把槽位里原本保存的函数地址读出来存到`original`，后续在`hooked_strcmp`里就还可以继续调用原始`strcmp`。

**当前项目中 PLT Hook 的整体结构**

先看一下当前项目里和 PLT Hook 相关的目录划分：

```
include/nook/
  NookPltHook.h
  NookNativeHook.h

src/framework/
  NookPltHook.cpp
  NookNativeHook.cpp

src/native_hook/core/
  module_info.cpp
  module_match.cpp
  native_hook_dispatcher.cpp
  runtime_patch.cpp

src/native_hook/plt_hook/
  plt_hook_impl.cpp
  elfio_image_parser.cpp
  elf_reader.cpp
  elf_hash.cpp
```

这几层各自负责的事情大概是：

* `include/nook/NookPltHook.h`

对外暴露 PLT Hook API

* `src/framework/NookPltHook.cpp`

`负责参数校验、初始化、策略装配`

* `src/framework/NookNativeHook.cpp`

当前只是把 Native Hook 门面转到 Plt Hook

* `src/native_hook/core`

放模块定位、路径匹配、通用调度、内存 patch

* `src/native_hook/plt_hook`

放 ELF 元数据解析

##

**一次 PLT Hook 调用链**

先把整条调用链串起来，再分别讲细节。一次`hook_symbol()`大致会经历下面这些步骤，这只是针对当前项目，一个简单的PLT Hook实际并不需要这么复杂：

* 用户调用`NookNativeHookHookSymbol()`
* 它直接转发到`NookPltHookSymbol()`
* `NookPltHookSymbol()`

  组装依赖并进入统一调度器
* 调度器通过`/proc/self/maps`找到目标模块的运行时基址和磁盘路径
* 尝试`ELFIO`解析主路径
* 最终定位到某个 relocation 对应的 slot 地址
* 通过统一的 runtime patch 逻辑改写该地址里的函数指针
* 同时把原始函数地址保存到`original`

也就是说，对外看起来只是一个：

```
api.hook_symbol("libnative-lib.so",
"strcmp",
reinterpret_cast<void*>(hooked_strcmp),
                &original);
```

但内部实际上完成了“模块定位 -> 文件解析 -> 重定位筛选 -> 地址换算 -> 内存页修改 -> 指针改写”这一整套动作，即：

```
  NookPltHookSymbol
-> HookSymbolWithFallback
-> get_module_info
-> TryPltHookWithElfio
-> LoadFromFile
-> ComputeRuntimeBias
-> CollectRelocationsForSymbol
-> PatchPointerAtAddress
-> 失败时 TryPltHookWithElfReader
```

##

**样式对外接口层：NookPltHook 做了什么**

先看公开头文件：

```
NookStatus NookPltHookInitialize(void);
NookStatus NookPltHookIsAvailable(int* available);
NookStatus NookPltHookSymbol(constchar* module_name,
constchar* symbol_name,
void* replacement,
void** original);
```

对外 API 非常薄，真正的核心在`NookPltHookSymbol()`里。

它做的事情主要有三类：

* 参数校验
* 懒初始化
* 组装 primary/fallback 依赖

对应代码：

```
NookStatus NookPltHookSymbol(constchar* module_name,
constchar* symbol_name,
void* replacement,
void** original) {
if (module_name == nullptr || module_name[0] == '\0' ||
        symbol_name == nullptr || symbol_name[0] == '\0' ||
        replacement == nullptr || original == nullptr) {
return NOOK_STATUS_INVALID_ARGUMENT;
    }

    *original = nullptr;
if (!g_plt_hook_initialized) {
const NookStatus status = NookPltHookInitialize();
if (status != NOOK_STATUS_OK) {
return status;
        }
    }

#if defined(__ANDROID__) || defined(__linux__)
const NookNativeInternal::FallbackHookDependencies dependencies = {
            &ResolveModuleInfo,
            &NookNativeInternal::TryPltHookWithElfio,
            &NookNativeInternal::TryPltHookWithElfReader,
nullptr};

return NookNativeInternal::HookSymbolWithFallback(
            module_name, symbol_name, replacement, original, dependencies);
#else
return NOOK_STATUS_NOT_IMPLEMENTED;
#endif
}
```

可以看到，这一层本身完全不碰 ELF 头、不碰 relocation，也不碰`mprotect`。它只负责把这次 Hook 需要的策略拼起来，然后把执行权交给内部调度器。

**模块定位：如何从 /proc/self/maps 找到目标 so**

在真正解析 ELF 之前，首先得回答一个问题：目标模块当前在进程里到底被加载到了哪里？这个问题其实在之前的文章中也多次提到，这里再简单讲一下。

当前的做法很传统，也很直接，就是扫描`/proc/self/maps`。

`get_module_info()`的核心逻辑可以概括成：

* 打开`/proc/self/maps`
* 逐行读取映射记录
* 从每一行里解析出起始地址、权限、路径
* 用`module_path_matches()`判断这行是不是目标模块
* 命中后返回`map_start`作为运行时模块基址，同时把路径保存下来

代码逻辑大致如下：

```
while (std::fgets(buffer, sizeof(buffer), maps_file)) {
if (std::sscanf(buffer,
"%lx-%lx %4s %*x %*x:%*x %*d %127s",
                    &map_start,
                    &map_end,
                    perms,
                    so_name) != 4) {
continue;
    }

if (!module_path_matches(so_name, module)) {
continue;
    }

    *module_base = reinterpret_cast<void*>(map_start);
    *module_path = so_name;
return true;
}
```

##

**主路径一：ELFIO 负责解决什么问题**

到了这一步，我们已经拿到了两份非常关键的信息：

* 运行时视角下的`module_base`
* 文件视角下的`module_path`

接下来`ELFIO`路径要解决的问题就比较纯粹了：只从磁盘上的 ELF 文件里，把“这个符号对应哪些 relocation”找出来。

`ElfioImageParser`负责的事情大致可以拆成三件：

* 从`.dynsym`找到目标符号的动态符号索引
* 遍历所有`SHT_REL/SHT_RELA`section，找出引用该符号的 relocation
* 从首个`PT_LOAD`段计算 runtime bias

### 1. 查找动态符号索引

它会先拿到`.dynsym`，然后逐项遍历：

```
ELFIO::section* dynsym = elf_file_.sections[".dynsym"];
ELFIO::symbol_section_accessor symbols(elf_file_, dynsym);

for (ELFIO::Elf_Xword index = 0; index < symbols.get_symbols_num(); ++index) {
if (!symbols.get_symbol(index,
     ...