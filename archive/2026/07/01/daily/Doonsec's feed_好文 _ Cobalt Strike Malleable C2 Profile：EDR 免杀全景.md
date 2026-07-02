---
title: 好文 | Cobalt Strike Malleable C2 Profile：EDR 免杀全景
url: https://mp.weixin.qq.com/s/ErOBwK5_tMzYSbP07qNodg
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:55:45.758316
---

# 好文 | Cobalt Strike Malleable C2 Profile：EDR 免杀全景

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqU2RxSgncgicTxia8F8hCZ84OJ7r7Psa0bBbOO7AjhsRxCB6O3naiaEUsEolCUdxXOJPibyRIOgdNalQHgZS5FSmKpVkCngAk4BYBI/0?wx_fmt=jpeg)

# 好文 | Cobalt Strike Malleable C2 Profile：EDR 免杀全景

原创

Jake Mayhew
Jake Mayhew

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

> 本文由 LLM 生成并整理，使用前请人工核校，由三篇英文系列博客合并翻译而成。三篇原文都假设读者已掌握 Malleable C2 的基础知识，目标是构建一个 OPSEC-safe 的 profile。文中所有脚本与最终 profile 均发布在 White Knight Labs 的 GitHub 仓库。本文仅供防御研究、红队建设与教学用途。

---

## 总览：从 CS 4.8 到 4.13 的免杀演进

Cobalt Strike 的 Malleable C2 Profile 赋予了 Beacon 极强的可塑性。这三年间 Fortra 持续向 profile 注入新特性，本系列三篇文章的脉络如下：

| 阶段 | 版本 | 核心主题 |
| --- | --- | --- |
| Part 1 | CS 4.8 | 内存扫描器绕过、静态签名绕过、字符串清理、Rich Header、YARA 规则逐条击破、Sophos EDR 实战 |
| Part 2 | CS 4.9–4.11 | post-ex DLL 字符串清理、BeaconGate、新型进程注入 ObfSetThreadContext、sRDI + PrependLoader、Beacon 字符串 |
| Part 3 | CS 4.12–4.13 | Drip Loading、Check-in Delay、弃用特性、6 款 EDR + YARA 实测零告警 |

---

# Part 1：基础免杀与 CS 4.8 实战（2023）

本章逐项讲解每个 profile 选项的作用，对比默认 profile 与定制 profile 的差异，并在此基础上改进开源 profile，让红队行动更加 OPSEC-safe。测试基于 **Cobalt Strike 4.8**，参考 profile 为 amazon\_events.profile，并使用项目自带的 shellcode 注入代码。

现有 profile 已经足以绕过大多数杀软和 EDR，但要做成 OPSEC-safe 的 profile、并绕过一些最流行的 YARA 规则，仍有许多改进空间。

## 绕过内存扫描器

近几版 Cobalt Strike 让操作者非常容易绕过 BeaconEye、Hunt-Sleeping-Beacons 这类内存扫描器。关键是这一行：

```
set sleep_mask "true";
```

启用该选项后，Cobalt Strike 在 Beacon 睡眠前会对堆和每个镜像区段做 XOR，使 Beacon 内存中不留任何未保护的字符串或数据，因此上述工具都无法检测到它。

![Hunt Sleeping Beacons 执行结果](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqUel906RoEezth2b2Eas35Fkcb5gSDjtdw7fSt60DAbL8M8ibRd1PjHU00htiad7xpBKp1HZKRLp7Dbc7GsCYyGkicPJ5TdUdqC8A/640?wx_fmt=png&from=appmsg)

BeaconEye 同样无法找到这个带睡眠 Beacon 的恶意进程：

![BeaconEye 执行结果](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWRdhia0zjFNj7WbD75zeMQ8wgTWYELMmDibIVabXgRKXp6WR4BibvVEnpDkzUHiaXjibBY7CaURCqBqevLCMc3hqUJic00nLiaj5myWU/640?wx_fmt=png&from=appmsg)

但虽然绕过了内存扫描器，对内存区做交叉引用时，引用直接指向了内存中的 Beacon 载荷：

![指向 shellcode 的内存引用](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqW2Otd8vKRI3OdtYibdrnWIECLibEibvQTXOuSxib2sUQRjuhcoziaxhQQibjt2kVtWnLsZlicIs8ECCkZeXCuTkt0RCiaJO1Hv1tWhCzU/640?wx_fmt=jpeg&from=appmsg)

这说明：由于 Beacon 正是 API 调用的发起方，`WaitForSingleObjectEx` 执行结束后返回地址会落回它这里。引用指向一个内存地址（而非导出函数）本身就是红旗，自动工具和人工分析都能发现。

**强烈建议**用 Artifact Kit 启用「stack spoof（栈欺骗）」来消除这个 IOC。虽然它不属于 malleable profile，但即便如此也值得启用——通过把第五个参数设为 true 来开启欺骗机制：

![Artifact Kit 栈欺骗示例](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqUzib1ia7NSWqNRCFNsJDwxGicWyicaDmZMgcdHjcFk4VPLebnXX7TIZHVWK7jOS035XibxHuEgdIJooEnGnkbbFOtTxZr5xquhSOHQ/640?wx_fmt=png&from=appmsg)

编译时会生成一个 .CNA 文件，导入 Cobalt Strike 后，新生成的载荷就会应用这些改动。再次分析 Beacon：

![被欺骗的线程栈](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqXlwYK5K04olic2IThGWuZFM3s95HsddZPzV7OaSJOiaUaiaHXmSFn6jiaTuPFSpfG5eibxyRxu2pg3SdYKcufoxzXbFkY4jzJVGFyE/640?wx_fmt=jpeg&from=appmsg)

差异非常明显：线程栈被欺骗，不再留有任何内存地址引用的痕迹。

补充说明：Cobalt Strike 在 2021 年 6 月把栈欺骗加入了 arsenal kit，但实测发现这种调用栈欺骗只对用 Artifact Kit 生成的 exe/dll 产物生效，对通过 shellcode 注入到线程里的 Beacon 无效，因此难以在内存中隐蔽 Beacon。

## 绕过静态签名

接下来测试 Beacon 对静态签名扫描器的表现。开启下面这项会移除 Beacon 堆中存储的大部分字符串：

```
set obfuscate "true";
```

把 profile 应用到 Cobalt Strike 后，生成 raw shellcode 放进 shellcode loader 代码，编译出 EXE 后对比存储的字符串差异：

![raw 载荷（右）与定制载荷（左）字符串差异 1](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqU0KpNkgdTDZicib9vFZAKgor5IhlT5p2BjhVF85aPY3gdTcKEN4DX3IruRdjfUlBhetNiaz4Y5zibBUHMeAVM1P2jDyWhD9qKuqhE/640?wx_fmt=jpeg&from=appmsg)

![raw 载荷（右）与定制载荷（左）字符串差异 2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqVxaHtibe2xibXIF7IiaxwSDwmo72ONOl8R5dX2kQLUR6z3ZPpPGl3ZRy8RtggcBBogmYiaKL43icrgU9PMGe1sQibUnmIvVZbD636ng/640?wx_fmt=jpeg&from=appmsg)

在大量测试中我们发现：即便用了高度定制的 profile（含 `obfuscate`），Beacon 仍会被检测。用 ThreadCheck 发现 `msvcrt` 字符串被识别为「坏字节」：

![字符串检测示例 "msvcrt"](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWItFPPsVGYare6xsD4VCxGZ6HN6aSbFibSPE2nNML6RXT56BugGicUBo9gKYuHnQeZaYfiaX8ibJa5nMp8fqAsBMiaRbbvkAZsIeqw/640?wx_fmt=png&from=appmsg)

这确实是 Beacon 堆里的字符串，`obfuscate` 并未彻底移除所有可能的字符串：

![Beacon 堆中存储的恶意字符串](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqX1djL9l5ykLjU5xicM2uL5PgYjINmoHcicuMcL1xzhv6RNChMjfplhibJRca8LboMkHJDkmqhtrBwxoDEZmCfaqI7pQBIyesMTt8/640?wx_fmt=png&from=appmsg)

于是稍微修改 profile 移除这些可疑字符串：

```
strrep "msvcrt.dll""";
strrep "C:\\Windows\\System32\\msvcrt.dll""";
```

但帮助不大，堆里仍能找到这些字符串，得换个思路。

## Clang++ 救场

不同编译器有各自的优化和标志位，可以按需裁剪输出。试验不同编译器，往往能获得更好的性能、并可能绕过更多 AV/EDR。

例如 Clang++ 提供若干优化标志可缩减编译产物体积，而 GCC（G++）以高性能优化著称。用不同编译器能得到一个独特的可执行文件，从而规避检测：

![Mingw（左）与 Clang++（右）编译的 stub 差异](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqUbzotCdhQ94MyP6ISiaLm80LXYImoyU1sJauKO97IkALmfxR4C6H3N0s2SLZgqrGmPjicAzKiaP392ZxOqnmA2iaXy5iaBRIxhUHJc/640?wx_fmt=png&from=appmsg)

`msvcrt.dll` 字符串不再出现，Windows Defender 被绕过：

![移除字符串后 ThreatCheck 执行结果](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqX942pFuib8441TicIXbGic9TkhxfF5wHQ1npb6sOTsoORbgcQWhTa9WeQoibd0RuGotpZ87U3dpYuM5WtcVJvTzDdiaMMVeeoD8tHM/640?wx_fmt=png&from=appmsg)

对多款杀软测试后结果令人鼓舞（注意：这里用的是未加密 shellcode）：

![Antiscan.me 结果示例](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqW7GC16RjMsUMsgFRzB0lgYkibsQJJMWfH5Ot6sLqluAFctHzO0FtjvlXOuVgeAbQtyic38Lm2xAo8TqmwkW7WIIDOSTLTKia0xtA/640?wx_fmt=png&from=appmsg)

## 光移除字符串还不够

虽然 profile 里开了 `obfuscate`，在 Beacon 栈里仍能检测到大量字符串：

![Beacon 栈中存储大量字符串的片段](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqUB9h7mg6UnwDv6z2pPLORiciaqiaJRMdcjfQia7wMic0dHrAQeKqDFe7yJH5o9iauia1weAbUpqEKzBLtPLGlH02sfwM4nub3XgMf7HI/640?wx_fmt=png&from=appmsg)

我们加了以下选项来移除上述全部字符串：

```
transform-x64 {
    prepend "\x90\x90\x90\x90\x90\x90\x90\x90\x90"; # prepend nops
    strrep "This program cannot be run in DOS mode"""; # Remove this text
    strrep "ReflectiveLoader""";
    strrep "beacon.x64.dll""";
    strrep "beacon.dll"""; # Remove this text
    strrep "msvcrt.dll""";
    strrep "C:\\Windows\\System32\\msvcrt.dll""";
    strrep "Stack around the variable""";
    strrep "was corrupted.""";
    strrep "The variable""";
    strrep "is being used without being initialized.""";
    strrep "The value of ESP was not properly saved across a function call.  This is usually a result of calling a function declared with one calling convention with a function pointer declared""";
    strrep "A cast to a smaller data type has caused a loss of data.  If this was intentional, you should mask the source of the cast with the appropriate bitmask.  For example:""";
    strrep "Changing the code in this way will not affect the quality of the resulting optimized code.""";
    strrep "Stack memory was corrupted""";
    strrep "A local variable was used before it was initialized""";
    strrep "Stack memory around _alloca was corrupted""";
    strrep "Unknown Runtime Check Error""";
    strrep "Unknown Filename""";
    strrep "Unknown Module Name""";
    strrep "Run-Time Check Failure""";
    strrep "Stack corrupted near unknown variable""";
    strrep "Stack pointer corruption""";
    strrep "Cast to smaller type causing loss of data""";
    strrep "Stack memory corruption""";
    strrep "Local variable used before initialization""";
    strrep "Stack around""corrupted";
    strrep "operator""";
    strrep "operator co_await""";
    strrep "operator<=>""";

    }
```

问题解决，栈里再无这些字符串。

## Prepend 操作码（Prepend OPCODES）

该选项会把你在 profile 中写的操作码追加到生成的 raw shellcode 开头，因此必须构造一段完整可用的 shellcode，否则执行时会崩掉 Beacon。基本思路是写一段不影响原始 shellcode 的垃圾汇编代码，可以直接用一串 `0x90`（NOP），或更佳的，从下面这些指令中动态组合：

```
incesp
inceax
decebx
incebx
decesp
deceax
nop
xchgax,ax
nopdwordptr [eax]
nopwordptr [eax+eax]
nopdwordptr [eax+eax]
nopdwordptr [eax]
nopdwordptr [eax]
```

挑一个独特组合（打乱顺序或增删指令），最后转成 `\x` 格式以适配 profile。这里直接按原顺序取用，转成正确格式后的垃圾 shellcode 如下：

```
transform-x64 {
        ...
        prepend "\x44\x40\x4B\x43\x4C\x48\x90\x66\x90\x0F\x1F\x00\x66\x0F\x1F\x04\x00\x0F\x1F\x04\x00\x0F\x1F\x00\x0F\x1F\x00";
        ...
}
```

我们还用一段简单 Python 脚本把整个流程自动化，随机生成可用于 `prepend` 选项的垃圾 shellcode：

```
import random

# Define the byte strings to shuffle
byte_strings = ["40", "41", "42", "6690", "40", "43", "44", "45", "46", "47", "48", "49", "", "4c", "90", "0f1f00", "660f1f0400", "0f1f0400", "0f1f00", ...