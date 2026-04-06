---
title: Emulat3：拆解恶意软件的“显微镜”
url: https://mp.weixin.qq.com/s/JtklPLlTx3ZV_fDJEaYAfw
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:41:31.797178
---

# Emulat3：拆解恶意软件的“显微镜”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfYSHnFIFJDzAfK3CgRUN1aQjdcNiaKV8siaT06sbPcFqNB7OFpgIqPvjJDVkygZk330icgHjpn87QibqVcPLeX7df3aTwftvafz4s/0?wx_fmt=jpeg)

# Emulat3：拆解恶意软件的“显微镜”

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> Emulat3是个命令行工具，它能让你一步一步地模拟执行恶意软件PE文件或shellcode，实时看到每执行一条指令时寄存器、栈、内存的变化。这就像给恶意代码解剖过程装上了显微镜。

## 它解决什么问题？

逆向恶意软件时，静态分析只能看代码结构。真想弄明白它在运行时干了什么，比如计算解密密钥、反调试逻辑，就得动态调试。但动态调试又常遇到反调试对抗，或者代码本身是混淆过的、自解压的，跟踪起来特别费劲。

Emulat3提供了一个折中方案——在完全控制的环境里模拟执行。你不用真的运行恶意文件，而是把它的代码扔到模拟器里，一步步看着它跑，每一步发生了什么，都清清楚楚打印给你看。

## 核心功能：像看慢动作一样看代码执行

它用的是一个叫vivisect的引擎，就是FireEye（现在叫Mandiant）的FLOSS工具内部用的那个模拟器。每一步，Emulat3都会给你打印下面这些东西：

* **刚执行完的指令**：反汇编好的那条命令。
* **所有通用寄存器状态**：RAX、RBX这些，加上指令指针RIP和标志寄存器EFLAGS。
* **栈上内容**：显示当前栈指针RSP前后一片内存里的数据。
* **内存写入记录**：这步指令往内存里写了什么。
* **任何异常**：比如段错误、无效指令、触发了断点。

说白了，你把代码喂给它，它会一帧一帧地给你播放执行过程，所有内部状态都是透明的。

## 怎么安装和使用？

先看安装，要求Python 3.12或更高版本。安装命令很简单：

uv sync

接下来看怎么用。它支持两种主要模式：PE文件和原始shellcode。

### 模式一：分析PE文件

假设你有叫`xor.exe`的恶意软件样本。

想从程序入口点开始模拟：

python emu\_stepper.py --pe xor.exe

想模拟某个特定函数，比如虚拟地址是`0x140001010`的那个，最多执行100条指令：

python emu\_stepper.py --pe xor.exe --va 0x140001010 --max 100

想先看看这个文件里都有哪些函数：

python emu\_stepper.py --pe xor.exe --list

想在一个函数里执行时，如果遇到调用（CALL）指令，就跳进被调用的子函数里继续跟踪：

python emu\_stepper.py --pe xor.exe --va 0x1400014c1 --follow-calls

你甚至可以指定只跟进对某个特定地址（比如`0x140001450`）的调用：

python emu\_stepper.py --pe xor.exe --va 0x1400014c1 --follow-va 0x140001450

### 模式二：分析Shellcode

如果你只有一段原始的二进制shellcode文件：

python emu\_stepper.py --shellcode payload.bin

如果shellcode是十六进制字符串编码在一个文本文件里：

python emu\_stepper.py --shellcode encoded.txt --hex

懒得存文件，直接把十六进制字符串作为参数输入：

python emu\_stepper.py --sc-hex "4831c04889c7c3"

用`\x`这种C语言风格写法的字符串也行：

python emu\_stepper.py --sc-hex "\x48\x31\xc0\xc3"

看个参数表更清楚些：

| 参数 (Flag) | 作用 (Description) |
| --- | --- |
| --pe FILE | 要分析的PE文件 |
| --va ADDR | 要模拟的函数的虚拟地址（十六进制） |
| --list | 列出PE文件中所有函数然后退出 |
| --shellcode FILE | Shellcode文件（原始二进制） |
| --sc-hex HEX | 直接内联输入十六进制shellcode字符串 |
| --hex | 把shellcode文件当成十六进制编码文本处理 |
| --base ADDR | Shellcode的基地址（默认：0x690000） |
| --entry OFFSET | 入口点距离基地址的偏移（默认：0） |
| --max N | 最多执行的指令条数（默认：200） |
| --follow-calls | 遇到CALL指令时，跟进调用，而不是跳过 |
| --follow-va ADDR | 只跟进对指定地址的调用 |
| --stack-context N | 每一步显示RSP前后各N个QWORD的栈内容（默认：4，设为0则不显示） |

## 幕后原理和注意事项

这个工具的模拟环境配置得和FLOSS内部一样，就是为了保持一致性。

* 它会分配512KB的栈，用零初始化，并把栈指针RSP放在中间。
* 对那些带`rep`前缀的重复指令，它把最大迭代次数限制在256次，防止模拟器卡住。
* 它移除了vivisect的一些默认API钩子，为的是更“原始”地步进。
* 所有对内存的写入操作，都会通过vivisect的writelog功能记录下来。

这里有个关键点：当你用了`--follow-calls`参数时，它处理CALL指令的方式变了。正常情况下vivisect会直接跳过函数体，只模拟调用指令本身。而开启这个选项后，Emulat3会手动执行这个调用：把返回地址压栈，然后把程序计数器PC设置到目标地址去执行。如果跟进的那个调用执行过程中崩溃了（比如访问了无效内存），模拟器会自动回滚到调用之前的状态，然后切换回让vivisect跳过函数体的默认方式。这个设计挺聪明的，既保证了能深入跟踪，又防止了整个模拟过程因为一个子调用失败就完全中断。

## 优缺点和你该什么时候用它

先说优点吧。最大的好处就是直观和安全。你不用在调试器里和反调试斗智斗勇，也不用担心恶意代码真的在你的机器上搞破坏。所有东西都在沙盒里跑，还能随时看内存细节。对于理解算法逻辑、解密循环、简单的字符串解码，或者验证你的静态分析猜想特别管用。

缺点也明显。模拟不是真实执行，尤其是当恶意代码严重依赖操作系统API（比如调CreateFile、LoadLibrary）的时候，模拟环境里没有这些，代码可能跑不下去或者行为不对。所以它更适合分析那些逻辑自包含、不严重依赖外部环境的代码片段。

还有，复杂混淆或虚拟化保护的代码，模拟起来会很慢甚至不准。

总的来说，Emulat3是个非常棒的分析辅助工具。当你需要深入理解一段代码片段在**内部**是怎么动的时候，它应该在你的工具链里。把它当成一个强大的、能够暂停和检查的代码“计算器”就对了。

**获取方式：私信回复"emulat3"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过