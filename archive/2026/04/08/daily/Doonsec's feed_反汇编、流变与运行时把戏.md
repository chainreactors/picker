---
title: 反汇编、流变与运行时把戏
url: https://mp.weixin.qq.com/s/qQu6skKXbMnoYvG-uSgxDg
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:28:50.723448
---

# 反汇编、流变与运行时把戏

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSjePtSA1JwNhGuMR7Enk2AdDlsyhe3NuflauZSjx2GjM54S71dWUAGtfCwhcUELWsf24l4da84dJFia2JWib26MDLhZbicktDT6tw/0?wx_fmt=jpeg)

# 反汇编、流变与运行时把戏

f00crew
f00crew

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://f00crew.org/0x4a | f00crew |

今天直接裸奔——堕落恶意软件开发者视角，不加任何滤镜。

我们要整一个自包含的变形引擎——内置 ARM64 反汇编器、活跃性分析器、代码生成器和多种变异算法，还带反射加载、数据收集和外泄能力。

在 2026 年值得折腾吗？说实话可能不值。但我觉得这玩意儿挺牛逼的。

上周末有点空闲，就把搁了有一段时间的代码片段 **Aether**写成了文章。你可以在这里找到它：

github.com/0xf00sec/Aether

大部分是 x86 的，混了点 ARM，但 ARM 那块做得很不完整，压根没整完。为什么呢？一是 x86 花了我大部分精力，二是我从来没真正下决心把 ARM 实现的部分做完。

所以我就想，这是个不错的借口来补齐它——搞个完整的 ARM 版本，在这个过程中对架构有更深入的理解，也能把之前留下的毛糙的地方都整干净。

写这篇文章的时候，这东西已经在 macOS 26.2 上测过了，

我们这里讨论的是一个 macOS 植入物，目的是攻入目标机器然后从中偷数据。没啥突破性的创新，也没啥黑魔法——就是瞎折腾、看看这些东西是怎么运作的。

在 macOS 上，实现主要围绕 **Mach-O**可执行文件格式展开。我们不是把它当成黑匣子，而是直接操纵其结构——解析它、修改二进制，让代码能在保持有效性和可执行性的前提下自我改造。

变形引擎的核心是一个 N 代变异循环，内置了 ARM64/x86-64 反汇编器和活跃性分析器。每次执行时，通过垃圾指令插入、等价指令替换和基本块重排序来变换代码。每一代都用 AES 密钥链加密，然后在内存中反射加载，全程不落盘。

> 所谓变形，简单说就是程序在保持相同行为的前提下重写自身，想看教科书定义的话，Wikipedia 管够：Metamorphic code - Wikipedia

引擎在执行前会校验运行环境，包括域名、网络和硬件 UUID。一旦环境不匹配，立刻自毁。反分析层负责检测调试器，并通过加密的进程名哈希值扫描 macOS 上的安全工具。对于依赖 LaunchDaemon 的工具，用 SIGSTOP 将其挂起；其他进程则直接用 SIGTERM 或 SIGKILL 干掉。字符串在栈上动态构建以防止静态提取，再加上激进的内存擦除来清除痕迹。

持久化方面，利用 .zshenv 钩子实现分阶段执行——先休眠、再侦察、最后外泄。外泄机制采用死信箱式 C2 架构，配合 RSA+AES 加密，通过 Spotlight 收集文件，并以指数退避策略降低被检测的风险。

怎么构建的？

## Mach-O

这个引擎所做的一切都围绕 Mach-O 展开。它是 macOS 上的可执行文件格式——一个容器，装着你的代码、数据、符号，以及内核和 dyld 将二进制文件映射进内存并运行所需的全部内容。要在运行时变异代码、把自身重写回磁盘，或是不经 dyld 就反射加载新镜像，你需要在字节层面彻底理解这个格式。

Apple 在 <mach-o/loader.h> 里记录了所有数据结构，那是你的出发点。我们引用的每个结构体都在里面；内核源码 (xnu/bsd/kern/mach\_loader.c) 则精确展示了加载器是如何验证和映射这些结构的。想搞清楚能做到什么程度，值得仔细读一读。

Mach-O 二进制文件按顺序排列：头部、加载命令，然后是原始数据。没有索引表，没有间接引用，线性遍历即可。

```
┌──────────────────────┐  offset 0
│  mach_header_64      │  32 bytes
├──────────────────────┤
│  load command 0      │  variable size
│  load command 1      │
│  ...                 │
│  load command N      │
├──────────────────────┤  page-aligned boundary
│  __TEXT segment data │  (code lives here)
├──────────────────────┤
│  __DATA segment data │
├──────────────────────┤
│  __LINKEDIT          │  (symbols, strings, fixups)
└──────────────────────┘
```

头部告诉你后面跟着多少加载命令及其总大小。每个加载命令描述一个段（segment），段里包含节（section）。

`struct mach_header_64`是 32 字节，对我们来说关键字段如下：

```
struct mach_header_64 {
    uint32_t magic;       // MH_MAGIC_64 = 0xFEEDFACF
    cpu_type_t cputype;   // CPU_TYPE_ARM64 or CPU_TYPE_X86_64
    cpu_subtype_t cpusubtype;
    uint32_t filetype;    // MH_EXECUTE, MH_DYLIB, MH_BUNDLE
    uint32_t ncmds;       // number of load commands
    uint32_t sizeofcmds;  // total size of all load commands
    uint32_t flags;       // MH_PIE, MH_NOUNDEFS, etc.
    uint32_t reserved;
};
```

`magic`是最基本的合法性校验。`0xFEEDFACF`表示 64 位本机字节序；`0xCFFAEDFE`表示字节倒序；如果看到 `0xFEEDFACE`，那是 32 位——你走错年代了。在投放器里，解密完成后我们立即验证这个字段，确认解出了有效的二进制文件。

```
uint32_t magic = *(uint32_t *)decrypted;
if (magic != 0xfeedfacf && magic != 0xcffaedfe) {
    memset(decrypted, 0, dec_len);
    free(decrypted);
    return 1;
}
```

`filetype`在从零构建 Mach-O 时很重要。`MH_EXECUTE`是独立可执行文件；`MH_DYLIB`是共享库；`MH_BUNDLE`是可加载插件（dlopen 期望的类型）。包装变异后的代码时我们用 `MH_DYLIB`，因为它对反射加载的灵活性最高。

`flags`控制链接器和加载器行为。`MH_PIE`启用 ASLR；`MH_NOUNDEFS`告诉 dyld 没有未定义符号；`MH_DYLDLINK`将文件标记为动态链接。构建包装器时我们同时设置这三个：

```
mh->flags = MH_NOUNDEFS | MH_DYLDLINK | MH_PIE;
```

好，加载命令怎么处理？好问题，兄弟——每个命令都以相同的两个字段打头：

```
struct load_command {
    uint32_t cmd;      // command type (LC_SEGMENT_64, LC_MAIN, ..)
    uint32_t cmdsize;  // total size of this command including any trailing data
};
```

遍历方式是每次迭代前进 `cmdsize`个字节，内核的做法也一样——没有随机访问，只有线性迭代：

```
uint8_t *ptr = data + sizeof(struct mach_header_64);

for (uint32_t i = 0; i < mh->ncmds; i++) {
    struct load_command *lc = (struct load_command *)ptr;

    if (lc->cmd == LC_SEGMENT_64) {
        struct segment_command_64 *seg = (struct segment_command_64 *)ptr;
        // handle segment
    }

    ptr += lc->cmdsize;
}
```

我们关心的命令：

`LC_SEGMENT_64`描述一块内存区域，包含虚拟地址、虚拟大小、文件偏移、文件大小和保护标志。内核把从 `fileoff`开始的 `filesize`字节映射到 `vmaddr`，再零填充到 `vmsize`。这就是 BSS 的工作原理——`vmsize > filesize`，差值部分被清零。

`LC_MAIN`给出入口点，表示为相对 `__TEXT`的偏移。老版本二进制文件用 `LC_UNIXTHREAD`，它嵌入了一个完整的线程状态结构体，指令指针已预先设置好。

`LC_SYMTAB`和 `LC_DYSYMTAB`指向 `__LINKEDIT`中的符号表。为反射加载构建有效 Mach-O 时必须包含它们——dyld 会验证其存在，哪怕是空表。

`LC_SEGMENT_64`后面紧跟零个或多个内联的 `section_64`结构体，段的 `nsects`字段告诉你有多少个：

```
struct segment_command_64 *seg = (struct segment_command_64 *)ptr;
struct section_64 *sections = (struct section_64 *)(seg + 1);

for (uint32_t j = 0; j < seg->nsects; j++) {
    // sections[j].sectname  - e.g. "__text", "__stubs", "__cstring"
    // sections[j].segname   - parent segment name
    // sections[j].addr      - virtual address
    // sections[j].size      - size in bytes
    // sections[j].offset    - file offset to raw data
}
```

标准布局有三个段：

`__PAGEZERO`是地址 0 处的零长度映射，用于捕获 NULL 指针解引用。`vmsize`通常是一页（ARM64 上为 0x4000），`filesize`为 0，没有实际数据。

`__TEXT`包含可执行代码和只读数据，保护属性为 `r-x`。内部的 `__text`节存放实际机器码，`__stubs`和 `__stub_helper`处理懒绑定，`__cstring`存放 C 字符串字面量。`__text`节就是我们提取、反汇编、变异再写回的目标。

`__DATA`包含可写数据——全局变量、静态变量、Objective-C 元数据，保护属性为 `rw-`。

`__LINKEDIT`存放符号表、字符串表、代码签名和修复链，内部没有节，只有原始数据，由其他加载命令引用。

这就是核心操作。每次需要变异代码时，我们遍历加载命令找到 `__TEXT.__text`：

```
static struct section_64 *find_text(uint8_t *data) {
    struct mach_header_64 *mh = (void *)data;
    if (mh->magic != MH_MAGIC_64) return NULL;
    uint8_t *p = data + sizeof(*mh);
    for (uint32_t i = 0; i < mh->ncmds; i++) {
        struct load_command *lc = (void *)p;
        if (lc->cmd == LC_SEGMENT_64) {
            struct segment_command_64 *seg = (void *)p;
            if (!strcmp(seg->segname, "__TEXT")) {
                struct section_64 *s = (void *)(p + sizeof(*seg));
                for (uint32_t j = 0; j < seg->nsects; j++)
                    if (!strcmp(s[j].sectname, "__text")) return &s[j];
            }
        }
        p += lc->cmdsize;
    }
    return NULL;
}
```

找到节之后，代码字节位于 `data + section->offset`，`section->size`给出字节数。ARM64 上每条指令固定 4 字节，`size / 4`即为指令数量。x86-64 上指令长度可变，那是另一个问题了。

### 读取自身二进制文件

自我修改从玩弄自身开始 [PAUSE!]。`_NSGetExecutablePath()`（来自 `<mach-o/dyld.h>`）返回当前运行二进制文件的路径：

```
char path[1024];
uint32_t size = sizeof(path);
_NSGetExecutablePath(path, &size);

FILE *f = fopen(path, "rb");
fseek(f, 0, SEEK_END);
size_t len = ftell(f);
fseek(f, 0, SEEK_SET);

uint8_t *self = malloc(len);
fread(self, 1, len, f);
fclose(f);
```

这样，`self`就是堆内存里你自己 Mach-O 的逐字节副本。解析它，找到 `__text`，把代码字节交给反汇编器，变异，就可以开始了。

### 从零构建 Mach-O

变异完成后，我们需要把转换后的代码包装进有效的 Mach-O，供反射加载使用。这意味着手动构建整个结构——头部、段、节、符号表。包装器构建的是一个最小化的 dylib：

```
uint8_t *wrap_macho(const uint8_t *code, size_t code_sz, size_t *out_sz) {
    // header + load commands | __text code | __LINKEDIT
    // Everything page-aligned (0x4000 on ARM64)

    size_t code_off = PG_ALIGN(header_size);
    size_t code_aln = PG_ALIGN(code_sz);
    size_t link_off = code_off + code_aln;
    size_t total    = link_off + PG;

    uint8_t *buf = calloc(1, total);
    // ... fill in header, segments, sections, symtab ...
    memcpy(buf + code_off, code, code_sz);
    return buf;
}
```

页对齐这事搞错不得。ARM64 macOS 用的是 16KB 页（0x4000），不是 x86-64 的 4KB。对不齐，内核直接拒绝映射你的二进制文件。`PG_ALIGN`宏负责向上取整：

```
#define PG 0x4000
#define PG_ALIGN(x) (((x) + PG - 1) & ~(PG - 1))
```

构建的 Mach-O 必须包含：`__PAGEZERO`、带 `__text`节的 `__TEXT`、至少有空 symtab/strtab 的 `__LINKEDIT`，以及指向它们的 `LC_SYMTAB`/`LC_DYSYMTAB`命令。

少了任何一个，dyld 或内核都会拒绝加载该镜像。我们还加入了字段全零的 `LC_DYLD_INFO_ONLY`——即使没有实际的修复信息，dyld 也会检查它是否存在。

简单来说：变异引擎不是在抽象代码上运作，而是直接操作真实的 Mach-O 二进制文件。每一代读取一个 Mach-O，提取 `__text`，转换指令，把结果包装进新的 Mach-O，再反射加载。格式是变异与执行之间的接口：解析出错，代码被损坏；构建出错，加载器拒绝；对齐出错，内核让你的进程崩溃。

总之，麻烦透了。

原始 Apple 文档——因 Apple 已下架，使用的是存档版，但仍然是 `mach-o/loader.h`结构体最完整的参考资料。

* Apple's OS X ABI Mach-O File Format Reference
* Exploring Mach-O, Part 3
* Snake&Apple I - Mach-O files on ARM64
* MACH-O(5) man page
* loader.h source
* Mac Hacker's Handbook

## 反汇编

想变异代码，你得先理解代码。不是源码层面的理解——编译出来之后源码早没了。你必须在指令层面搞懂每个 4 字节字或变长字节序列到底干了什么：读了哪些寄存器？写了哪些？碰没碰标志位？有没有分...