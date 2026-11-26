---
title: ELF DT_RELR 压缩重定位导致 objdump 审计盲区分析与绕过
url: https://xz.aliyun.com/news/93459
source: 先知安全技术社区
date: 2026-11-25
fetch_date: 2026-11-26T10:13:07.238472
---

# ELF DT_RELR 压缩重定位导致 objdump 审计盲区分析与绕过

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# ELF DT\_RELR 压缩重定位导致 objdump 审计盲区分析与绕过

[![](/images/default-avatar.png)VoidTrace](/users/174402)·2026-11-25 10:59·28 分钟·18·北京·漏洞分析

ELF的DT\_RELR压缩重定位导致objdump -R无法枚举相关地址，攻击者可利用该盲区绕过安全检测执行构造函数。

## 一、RELR 是什么：从 11 和 7 的差说起

ELF 的动态重定位有几套并存的表示：

* `DT_RELA`：显式的 `Elf64_Rela` 数组，每个条目 24 字节，写清 offset、type、addend。
* `DT_REL`：32 位时代的显式数组，每个条目 16 字节。
* `DT_JMPREL`：PLT 的跳转槽重定位，单独一张表。
* `DT_RELR`：只针对相对重定位的压缩表示，每个条目 8 字节，用“基址 + 位图”描述一批地址。

RELR 的存在理由很直接：PIE、静态 PIE、C++ 虚表、函数指针表会产生大量相对重定位，每个都写 24 字节的 `Elf64_Rela` 太浪费。一个 `DT_RELR` 条目能干两件事：偶数条目是一个要重定位的地址；奇数条目是一张 64 位位图，bit 0 是标记位，bit 1 到 bit 63 对应基址开始的 63 个 8 字节槽位。一个位图覆盖 63 个地址，基址再前进 `63 * 8` 字节。

拿`librelr.so` 举例，`readelf -d` 能看到三组标签：

```
$ readelf -dW librelr.so | grep -E 'RELR|RELA|INIT_ARRAY|FINI_ARRAY'
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110615-2d70c0ee-e87d-1.png)

`DT_RELR` 在 `0x538`，大小 24 字节，条目宽度 8 字节。24 字节就是 3 个条目。

`readelf -r` 把这三个条目展开成 4 个地址：

```
$ readelf -rW librelr.so
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110616-2dd072c1-e87d-1.png)

6 个显式 RELA，1 个 PLT，4 个 RELR 地址，一共 11 个。4 个 RELR 地址是 `0x3dc0`、`0x3dc8`、`0x3dd0`、`0x4008`。

再把同一份文件交给 `objdump -R`：

```
$ objdump -RW librelr.so | sed -n '/DYNAMIC RELOCATION RECORDS/,$p'
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110616-2e16c3ea-e87d-1.png)

7 个。`0x3dc0`、`0x3dc8`、`0x3dd0`、`0x4008` 一个都没有。

最反直觉的一点不在“少了 4 个”，而在少掉的这 4 个刚好是加载器真正会写、而且写的是函数指针的 4 个地址。`0x3dc0` 和 `0x3dc8` 是 `.init_array` 的两个槽位，`0x3dd0` 是 `.fini_array` 的槽位，`0x4008` 是 `__dso_handle`。

文件里 `.init_array` 长这样：

```
$ readelf -x .init_array librelr.so
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110617-2e5498d2-e87d-1.png)

两个 8 字节槽位，分别是 `0x1100` 和 `0x1129`，都是链接期地址，不是零。`0x1100` 是 `frame_dummy`，`0x1129` 是本文样本里的 `lib_init`。加载器在运行时把加载基址加上去：

```
$ setarch $(uname -m) -R ./relr_use ./librelr.so
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110617-2e8b2a4f-e87d-1.png)

`init_off=0x1129` 和文件里第二个槽位的值完全对上。`CTOR RAN` 说明构造函数确实执行了，`ctor_ran=1` 说明它真的把状态改了。但在 `objdump -R` 的 7 行输出里，没有任何一行指向 `0x3dc8`。

同一份文件，加载器写了 11 个地址，`objdump -R` 只报告 7 个。差的 4 个，两个是构造函数/析构函数指针，一个是 DSO 句柄。

## 二、从一次加载看完整链路

目录：

```
/root/relr-lab
├── relr_lib.c
├── relr_use.c
├── relr_mem.c
├── relr_scan.py
├── relr_gate.py
├── relr_many.c
├── relr_data.c
└── relr_static.c
```

`relr_lib.c` 是一个带构造函数的共享库，核心只有几行：

```
int ext = 7;
int *p1 = &ext;
int *p2 = &ext;

__attribute__((noinline)) static void ctor(void)
{
    static const char msg[] = "CTOR RAN\n";
    write(1, msg, sizeof(msg) - 1);
}

__attribute__((constructor)) static void lib_init(void)
{
    ctor();
}
```

`p1`、`p2` 指向可被外部符号插入的 `ext`，链接器会给它们生成显式的 `R_X86_64_64`，留在 `.rela.dyn` 里。`lib_init` 是本地函数，它的 `.init_array` 槽位是相对重定位，正好是 RELR 的压缩对象。

`relr_use.c` 负责 `dlopen`、打印构造函数状态、拿到加载基址：

```
void *h = dlopen(path, RTLD_NOW | RTLD_LOCAL);
int (*get_ran)(void) = (int (*)(void))dlsym(h, "get_ctor_ran");
void *(*get_addr)(void) = (void *(*)(void))dlsym(h, "get_init_addr");
dl_iterate_phdr(cb, NULL);
printf("ctor_ran=%d\n", get_ran ? get_ran() : -1);
printf("init_addr=%p\n", get_addr ? get_addr() : NULL);
printf("lib_base=%p\n", (void *)lib_base);
printf("init_off=0x%lx\n", (unsigned long)((uintptr_t)get_addr() - lib_base));
```

`relr_mem.c` 更直接：给定库名和一个节内偏移，`dlopen` 之后读那个槽位，打印值和“值相对加载基址的偏移”。

编译命令：

```
$ gcc -O0 -shared -fPIC -Wl,-z,pack-relative-relocs -o librelr.so relr_lib.c
$ gcc -O0 -shared -fPIC -o librela.so relr_lib.c
$ gcc -O0 -o relr_use relr_use.c -ldl
$ gcc -O0 -o relr_mem relr_mem.c -ldl
```

第一条带 `-Wl,-z,pack-relative-relocs`，让链接器把相对重定位压进 `DT_RELR`。第二条不带，得到一份全部走 `.rela.dyn` 的对照库 `librela.so`。

第一步，看动态标签。`DT_RELR`、`DT_RELRSZ`、`DT_RELRENT` 三个标签同时出现，说明这份文件里有压缩重定位。前面已经贴过输出，这里只记结论：`DT_RELR=0x538`，`DT_RELRSZ=24`，`DT_RELRENT=8`。

第二步，看 `readelf -r`。`.relr.dyn` 三个条目展开成四个地址：`0x3dc0`、`0x3dc8`、`0x3dd0`、`0x4008`。`readelf` 还把每个地址配了一个“Symbolic Address”。这里有一个容易踩的坑：`0x3dc8` 那一行写的是 `__frame_dummy_init_array_entry + 0x8`，看起来像 `frame_dummy` 的尾巴，实际槽位里存的是 `lib_init` 的地址 `0x1129`。`readelf` 解析的是“槽位地址落在哪个符号里”，不是“槽位里的值指向哪个符号”。这两个不是一回事。

第三步，看 `objdump -R`。7 行，四个 RELR 地址全部缺席。`objdump -R` 枚举的是 `.rela.dyn`、`.rel.dyn`、`.rela.plt` 这些显式表，`DT_RELR` 是一条动态标签加一段位图，不在它的枚举路径里。

第四步，看文件里的 `.init_array`。`0x1100` 和 `0x1129`，两个链接期地址，不是零。一个只读文件、不加重定位的扫描器，会把 `0x1129` 当成一个绝对指针；这个地址在没有加载基址的情况下根本不在任何映射里。但加载器知道它该加什么。

第五步，跑起来：

```
$ setarch $(uname -m) -R ./relr_use ./librelr.so
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110617-2ec352eb-e87d-1.png)

`setarch -R` 关掉 ASLR，所以两次运行得到同一组地址。`0x7ffff7fba129 - 0x7ffff7fb9000 = 0x1129`，和文件里的第二个槽位一致。

第六步，直接读运行时槽位：

```
$ setarch $(uname -m) -R ./relr_mem ./librelr.so 3dc8
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110618-2efc6acc-e87d-1.png)

`value_off=0x1129`，就是 `lib_init`。同一个工具读 `0x3dd0` 和 `0x4008`：

```
$ setarch $(uname -m) -R ./relr_mem ./librelr.so 3dd0

$ setarch $(uname -m) -R ./relr_mem ./librelr.so 4008
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110618-2f3f1158-e87d-1.png)

`0x3dd0` 的 `value_off=0x10c0` 是 `__do_global_dtors_aux`；`0x4008` 的 `value_off=0x4008` 是 `__dso_handle` 指向自己。

把这条链拆开看，一共五步：

1. 链接器把 `lib_init` 的 `.init_array` 槽位、`__do_global_dtors_aux` 的 `.fini_array` 槽位、`__dso_handle` 的相对重定位压缩成 `DT_RELR` 位图。
2. 动态段里留下 `DT_RELR=0x538`、`DT_RELRSZ=24`、`DT_RELRENT=8`。
3. 加载器展开位图，得到四个地址。
4. 加载器把“加载基址 + 文件里的链接期地址”写进这四个槽位。
5. 构造函数从 `.init_array` 被调用，打印 `CTOR RAN`。

审计侧看到的却是另一条链：`objdump -R` 枚举显式表，得到 7 个地址，没有 `0x3dc8`，于是 gate 判 PASS。

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110619-2f76acd3-e87d-1.svg)

这一步证明的是：加载器写的地址集合和 `objdump -R` 报告的地址集合不是同一个集合；少的 4 个不是随机的，正好是 `init_array`、`fini_array` 和 `__dso_handle`。

## 三、取证视角：四个地址，六种看法

同一个文件，从六个角度看，会得到六组不同的“事实”。

**动态标签视角。** `readelf -d` 告诉你 `DT_RELR` 存在，大小 24 字节，条目 8 字节。它不告诉你四个地址分别是什么，但它是第一个信号：这份文件用了压缩重定位。

**重定位表视角。** `readelf -r` 把位图展开成四个地址，并且给每个地址配一个符号。这个视角最完整，但有一个符号解析的坑：`Symbolic Address` 列写的是槽位地址的符号，不是槽位里的值。`0x3dc8` 那一行是 `__frame_dummy_init_array_entry + 0x8`，实际值是 `lib_init`。要确认这一点，得再看符号表：

```
$ readelf -sW librelr.so | grep -E 'lib_init|frame_dummy'
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110619-2fb31723-e87d-1.png)

`lib_init` 在 `0x1129`，和 `.init_array` 第二个槽位的值一致。`readelf -r` 的符号列只是把槽位地址 `0x3dc8` 归到了 `0x3dc0` 那个数组符号的 `+0x8` 上。

**objdump 视角。** `objdump -R` 只给 7 个地址。它不会提示“还有 4 个在 DT\_RELR 里”，也不会在输出末尾写一句“RELR not shown”。这是一次静默的省略。

**文件字节视角。** `readelf -x .init_array` 显示 `0x1100` 和 `0x1129`。这两个值是链接期地址，不是运行时地址。一个把文件值当绝对指针的扫描器，会把 `0x1129` 当成一个无效地址；一个只看节内容的审计，会认为这里“有两个看起来像代码地址的值”，但不知道它们会在加载时被改写。

**运行时视角。** `relr_mem` 读 `0x3dc8`，得到 `base+0x1129`。这是唯一能直接证明“加载器确实写了这个槽位”的视角。

**LLVM 视角。** LLVM 的 `llvm-readelf` 和 GNU readelf 一样能看到 `.relr.dyn`：

```
$ llvm-readelf -r librelr.so | sed -n '/.relr.dyn/,$p'
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110619-2fefeebd-e87d-1.png)

但 LLVM 的 `llvm-objdump -R` 和 GNU objdump 一样只给 7 个：

```
$ llvm-objdump -R librelr.so | grep -cE '^[0-9a-f]{16}'
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110620-3024c959-e87d-1.png)

```
$ python3 relr_scan.py librelr.so | grep -E 'DT_RELR|DT_RELA|DT_JMPREL|all dynamic|objdump -R offsets|targets missing'
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20261125110620-3065a8e1-e87d-1.png)

缺的 4 个是 `0x3dc0`、`0x3dc8`、`0x3dd0`、`0x4008`。`relr_scan.py` 的完整模式把三张表合成一个集合，`objdump -R` 只给显式表，差值就是 RELR 的地址。

这不是 GNU 一家的问题，也不是 readelf 一家的问题。`readelf` 这一支（GNU 和 LLVM）都能展开 `DT_RELR`，`objdump` 这一支（GNU 和 LLVM）都只枚举显式表。分界线在工具的实现路径，不在编译器或发行版。

把六个视角压成一张证据表：

|  |  |  |
| --- | --- | --- |
| 顺序 | 行为 | 可观察证据 |
| 1 | 链接器把四个相对重定位压成三个 RELR 条目 | `DT_RELR=0x538`、`DT_RELRSZ=24`、`DT_RELRENT=8`；`readelf -r` 显示 3 entries relocate 4 locations |
| 2 | `objdump -R` 只枚举显式表 | 7 个 offset；`0x3dc0`、`0x3dc8`、`0x3dd0`、`0x4008` 缺席 |
| 3 | 文件里的 `.init_array` 存链接期地址 | `r...