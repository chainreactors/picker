---
title: 本日学习笔记：汇编进阶 + Web 入门实战
url: https://mp.weixin.qq.com/s/tXRNlR42IWwn494YWOQ_6g
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:17.349126
---

# 本日学习笔记：汇编进阶 + Web 入门实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRw8ba1QkAynHnjfgsYJvKsFBbmTDwVxNaXiarCSs51enKsa7KjjgWehtTEL2OqRgtcFWLvKHpTpDLyKzPXS9y4NiaGlNUTOr0qEFiaa4l6dDQ/0?wx_fmt=jpeg)

# 本日学习笔记：汇编进阶 + Web 入门实战

原创

00后反骨崽
00后反骨崽

00后反骨崽

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 今天干了两件事：一是汇编继续往上走，学了系统调用和跳转控制流；二是开了 Bugku 平台的 Web 题，搞了三道入门题。一文打包，干货不少，建议收藏！👇

# 上篇：汇编进阶 —— 系统调用与跳转控制流

# 📡 SYSCALL：让程序和操作系统对话

在 x86-64 汇编中，syscall 是调用 Linux 内核服务的入口。相当于你对操作系统说"帮我干个活"。

调用约定：

| 寄存器 | 作用 |
| --- | --- |
| `rax` | 系统调用号（告诉内核你要调哪个功能） |
| `rdi` | 第 1 个参数 |
| `rsi` | 第 2 个参数 |
| `rdx` | 第 3 个参数 |
| `rcx` | 第 4 个参数 |
| `r8` | 第 5 个参数 |
| `r9` | 第 6 个参数 |

> 💡 比如调用号 1 = write（输出），调用号 60 = exit（退出程序）。完整调用号表参考：https://filippo.io/linux-syscall-table/

# 📝 数据定义：.ascii 与字符串长度计算

.ascii —— 存字符串

.ascii "Hello,World!\n"    ; 把字符串逐字节存入内存

和 .byte 的区别：.byte 是一个字节一个字节手动存；.ascii 直接存一整段字符串。

计算字符串长度

汇编里没有 strlen() 这种现成函数，但可以用汇编器的地址运算：

q1: .ascii "Hello,World!\n"

q1len = . - q1          ; 当前地址 - 起始地址 = 长度

. 表示汇编器当前所在地址，减去字符串起始地址 q1，就得到了字符串的字节数。非常巧妙！

# 🧩 Exercise 3：输出两段字符串 + 用 code 99 退出

题目要求：

把两个字符串输出到终端

用系统调用号 60（exit）退出程序，退出码为 99

完整解法

; === 第 1 次输出 ===

mov rax, 1              ; syscall 1 = write

mov rdi, 1              ; fd = 1 (stdout)

lea rsi, [q1]           ; 缓冲区地址 = q1 的地址

lea rdx, [q1len]        ; 长度 = q1len

syscall                 ; 执行！输出第一段字符串

; === 第 2 次输出 ===

mov rax, 1

mov rdi, 1

lea rsi, [q2]

lea rdx, [q2len]

syscall                 ; 输出第二段字符串

; === 退出程序 ===

mov rax, 60             ; syscall 60 = exit

mov rdi, 99             ; 退出码 = 99

syscall                 ; 程序结束

.data

q1: .ascii "Hello,World!\n"

q1len = . - q1

q2: .ascii "you are so beautiful"

q2len = . - q2

> 💡 **关键点**：每次 syscall 之前都要把 `rax` 重新设为调用号。因为上一次 syscall 执行后，`rax` 的值可能已经被内核修改了。

# 补充：xor 清零技巧

如果不希望程序报错，最后要正确退出。清零寄存器有个经典写法：

xor rdi, rdi            ; rdi 异或自身 = 0（比 mov rdi, 0 更短）

# 🔀 JMP：跳转——让代码不再只能从上往下跑

之前写的代码都是从上往下顺序执行，但真实程序需要分支、循环、函数调用，这就需要跳转指令。

jmp —— 无条件跳转

jmp print1              ; 直接跳到 print1 标签处执行

程序结构示例

用跳转可以写出类似 if-else 的结构：

\_start:

jmp print1          ; 先跳到 print1

exit:

mov rax, 60

mov rdi, 0

syscall             ; 正常退出

print1:

mov rax, 1

mov rdi, 1

lea rsi, q1

lea rdx, q1len

syscall

jmp print2          ; print1 完成后跳到 print2

print2:

mov rax, 1

mov rdi, 1

lea rsi, q2

lea rdx, q2len

syscall

jmp exit            ; print2 完成后跳到 exit

.data

q1: .ascii "Hello"

q1len = . - q1

q2: .ascii "World"

q2len = . - q2

执行流程：

\_start → print1（输出Hello）→ print2（输出World）→ exit（退出）

> 💡 **理解要点**：虽然代码在内存中是按 `_start → exit → print1 → print2` 排列的，但通过 `jmp` 指令，实际执行顺序是 `_start → print1 → print2 → exit`。**代码的存储顺序 ≠ 执行顺序**，这是跳转的核心概念。

# 📦 预告：CALL、RET 与栈

跳转之外，汇编还有几个重要概念将在后续学习中涉及：

| 指令 | 作用 |
| --- | --- |
| `CALL` | 调用子程序（跳到目标地址，同时把返回地址压栈） |
| `RET` | 从子程序返回（从栈中弹出返回地址，跳回去） |
| `STACK` | 内存中的一系列字节，用于存储函数调用的上下文 |

这三个配合起来，就能实现函数调用——这是写出复杂程序的基础。下一篇继续！

# 下篇：Web 入门 —— Bugku 平台三题全解

# 题目一：本地管理员 —— IP 伪造 + Base64 解码

# 🎯 考点

HTTP 请求头伪造、Base64 编码

# 🔍 解题过程

打开网站，看到一个管理员登录界面。先用admin/test123试试——果然不对，提示：

> "IP禁止访问，请联系本地管理员登录，IP已被记录"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAwdDTTDfxqwydLKTJBOzrRvLEiaCHv9mzw1hxS62xiay14tia6L6e2oQCznVnT6hnhJHoZQ5Gb4ldkWf7VkroYvzg6ECGfKhDJ66k/640?wx_fmt=png&from=appmsg)

页面底部还藏了一段密文：dGVzdDEyMw，Base64 解码后得到 → test123，确认了密码。但重新登录还是 IP 禁止提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAwEVHwHictFV2BwKvFM3VPSYpZ5vAMmMqYQSI6V0rS1HZvhDNWyicOSiaRQYFOrturmmkTMwvofVJxn5HZic3RskAEEdsDCnrT7To0/640?wx_fmt=png&from=appmsg)

关键线索：题目叫"本地管理员"，说的是 IP 限制。需要让服务器以为你是从本机（127.0.0.1）访问的。

# 💡 突破口：X-Forwarded-For

用抓包工具拦截登录请求，添加请求头：

X-Forwarded-For: 127.0.0.1

![](https://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAyQPqe40tDB98wveakpyIibDhIicYzu0EdvkQ6vftbDicskCZqUzENdrbbkNbkL7JtpDiarNMDibFiaqRBSZeHnicvlhm0IrEFEsNrqsA/640?wx_fmt=png&from=appmsg)

重新发包 → 直接拿到 flag！

flag{c55e8a06ff14a6dbc242d229422001ff}

> 📖 **知识点**：`X-Forwarded-For` 是代理服务器用来记录客户端原始 IP 的头，如果后端只信任这个头而不校验，就可以被伪造。

# 题目二：game1 —— 游戏分数篡改 + 加密分析

# 🎯 考点

抓包分析、参数篡改、Base64 编码识别

# 🔍 解题过程

题目是一个盖楼小游戏。正常玩几把，观察游戏失败时发送的请求包：

score=50&ip=111.194.76.212&sign=zMNTA===

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAyW7EibicEMrkTSgHhSu7zMhcBlv4ZMZfBRQfibfD2icgKDUfCFYDprUVzdCfYibUVhjnXSt40deUxQeY3j3fdu022WyuDzO2MnZgsQ/640?wx_fmt=png&from=appmsg)

score=75&ip=111.194.76.212&sign=zMNzU===

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAzwZLq0O3cnAS36GsBRpGv2ticYmLJnzHAkkdQ7SELHg4TGfT4AibmxM2YEQcWqwWLBuYsoEe9yJUt09g3r2sxUbf2x1Y4Aoe9YA/640?wx_fmt=png&from=appmsg)

score=25&ip=111.194.76.212&sign=zMMjU===

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAyAVINm3KWNicKz6kicmRFYffJZO1xARQPjrUOcVhyuwBkJeemYEibsgg4zgpCOuhB385qoUtWp9SHbn3x8C4fH2n0BWJj7Yjj6pw/640?wx_fmt=png&from=appmsg)

第一步：直接改 score 为超大值 → 还是失败，说明分数不是唯一判定条件。

第二步：分析 sign 参数。发现 zM 前缀不变，后面的部分尝试 Base64 解码：

![](https://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAycmbU64aMvTsBniceiaM7CNufXerrwFeYLp5HAx2VCC1RpeWp5xNcRFe5Eua6T55WjBqicHQZB6aYGiawJQIwTyCVjialurGRacgf4/640?wx_fmt=png&from=appmsg)

NTA= → 50  ✓

NzU= → 75  ✓

MjU= → 25  ✓

确认了！sign 中 zM 后面的部分就是分数的 Base64 编码。

第三步：把 999999999999999 做 Base64 编码，替换 sign 中对应部分，同时 score 也改成匹配值：

score=999999999999999&ip=111.194.76.212&sign=zMOTk5OTk5OTk5OTk5OTk5==

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAwgiagB0qf5sZVJm821iaFYhZo9WWUPHT8do1FEthWJDoE4OicXD0XLx1GnKIUsdH8olGv8ciavECbplyzMTsOuzytCRj2jmThicL94/640?wx_fmt=png&from=appmsg)

发包 → 成功拿到 flag！

> 📖 **知识点**：`sign` 参数常用于防篡改，但如果编码方式太简单（如直接 Base64），等于没加密。分析思路：**观察变化规律 → 猜测编码方式 → 验证猜测 → 构造请求**。

# 题目三：源代码 —— URL 编码解码 + 代码审计

# 🎯 考点

HTML 源码查看、URL 编码（%xx）解码、JavaScript 代码审计

# 🔍 解题过程

题目描述就一句话："看看源代码"。页面上有一个输入框和 submit 按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAwKpDia4vpVFs9u7zPt21wgIRrsn5Sf12lJNaC5RfgC8DjGd75FXYFdX4XuWwXobichjakC8ZxSA1wBPu4qlXIUOe6LPVLwhmiafU/640?wx_fmt=png&from=appmsg)

按 F12 查看页面源码，发现两段 URL 编码的变量：

var p1 = '%66%75%6e%63%74%69%6f%6e...';

var p2 = '%61%61%36%34%38%63%66%36...';

eval(unescape(p1) + unescape('%35%34%61%61%32' + p2));

手动 URL 解码后拼接，得到完整的 JavaScript：

function checkSubmit(){

var a = document.getElementById("password");

if("undefined" != typeof a){

if("67d709b2b54aa2aa648cf6e87a7114f1" == a.value)

return !0;

alert("Error");

a.focus();

return !1;

}

}

document.getElementById("levelQuest").onsubmit = checkSubmit;

# 🔥 本周学习笔记：汇编进阶 + Web 入门实战

> 这周干了两件事：一是汇编继续往上走，学了系统调用和跳转控制流；二是开了 Bugku 平台的 Web 题，搞了三道入门题。一文打包，干货不少，建议收藏！👇

# 上篇：汇编进阶 —— 系统调用与跳转控制流

# 📡 SYSCALL：让程序和操作系统对话

在 x86-64 汇编中，syscall 是调用 Linux 内核服务的入口。相当于你对操作系统说"帮我干个活"。

调用约定：

表格

| 寄存器 | 作用 |
| --- | --- |
| `rax` | 系统调用号（告诉内核你要调哪个功能） |
| `rdi` | 第 1 个参数 |
| `rsi` | 第 2 个参数 |
| `rdx` | 第 3 个参数 |
| `rcx` | 第 4 个参数 |
| `r8` | 第 5 个参数 |
| `r9` | 第 6 个参数 |

> 💡 比如调用号 1 = write（输出），调用号 60 = exit（退出程序）。完整调用号表参考：https://filippo.io/linux-syscall-table/

# 📝 数据定义：.ascii 与字符串长度计算

.ascii —— 存字符串

.ascii "Hello,World!\n"    ; 把字符串逐字节存入内存

和 .byte 的区别：.byte 是一个字节一个字节手动存；.ascii 直接存一整段字符串。

计算字符串长度

汇编里没有 strlen() 这种现成函数，但可以用汇编器的地址运算：

q1: .ascii "Hello,World!\n"

q1len = . - q1          ; 当前地址 - 起始地址 = 长度

. 表示汇编器当前所在地址，减去字符串起始地址 q1，就得到了字符串的字节数。非常巧妙！

# 🧩 Exercise 3：输出两段字符串 + 用 code 99 退出

题目要求：

把两个字符串输出到终端

用系统调用号 60（exit）退出程序，退出码为 99

完整解法

; === 第 1 次输出 ===

mov rax, 1              ; syscall 1 = write

mov rdi, 1              ; fd = 1 (stdout)

lea rsi, [q1]           ; 缓冲区地址 = q1 的地址

lea rdx, [q1len]        ; 长度 = q1len

syscall                 ; 执行！输出第一段字符串

; === 第 2 次输出 ===

mov rax, 1

mov rdi, 1

lea rsi, [q2]

lea rdx, [q2len]

syscall                 ; 输出第二段字符串

; === 退出程序 ===

mov rax, 60             ; syscall 60 = exit

mov rdi, 99             ; 退出码 = 99

syscall                 ; 程序结束

.data

q1: .ascii "Hello,World!\n"

q1len = . - q1

q2: .ascii "you are so beautiful"

q2len = . - q2

> 💡 **关键点**：每次 syscall 之前都要把 `rax` 重新设为调用号。因为上一次 syscall 执行后，`rax` 的值可能已经被内核修改了。

# 补充：xor 清零技巧

如果不希望程序报错，最后要正确退出。清零寄存器有个经典写法：

xor rdi, rdi            ; rdi 异或自身 = 0（比 mov rdi, 0 更短）

# 🔀 JMP：跳转——让代码不再只能从上往下跑

之前写的代码都是从上往下顺序执行，但真实程序需要分支、循环、函数调用，这就需要跳转指令。

jmp —— 无条件跳转

jm...