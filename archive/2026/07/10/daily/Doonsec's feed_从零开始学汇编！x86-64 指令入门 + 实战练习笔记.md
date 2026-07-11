---
title: 从零开始学汇编！x86-64 指令入门 + 实战练习笔记
url: https://mp.weixin.qq.com/s/JMnkW82DiHiYrBjYUNo55A
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:56:33.436650
---

# 从零开始学汇编！x86-64 指令入门 + 实战练习笔记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRw8ba1QkAyE55SqVMl2NCOHheZkTnxdsoCeicFFkwAOswic2sS72SDvibDXANbn7p4KOSvHycAc5qic3bmZ3vUQyfNbVRkvxKVhZhUtfdDwQEU/0?wx_fmt=jpeg)

# 从零开始学汇编！x86-64 指令入门 + 实战练习笔记

原创

00后反骨崽
00后反骨崽

00后反骨崽

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 搞逆向、搞 Pwn、搞底层安全——汇编是绕不过去的基础功。（其实是发现师傅的pwn录播课有点看不懂，正好下个学期有汇编的课程，就准备恶补一下）这篇笔记记录了我从零开始学 x86-64 汇编的过程，包括基础指令、内存操作和两道实战练习，附完整解题代码，建议收藏！👇

# 📌 先搞懂这几条核心指令

汇编看着吓人，其实最常用的指令就那么几条，先把它们吃透：

# mov —— 赋值/复制

最基础的指令，把数据从一个地方搬到另一个地方。

mov rax, rbx    ; rax = rbx

mov rax, 42     ; rax = 42（直接赋数值）

⚠️ 但有几个寄存器不能用 mov 直接操作：

rip

（指令指针）

rsp

（栈指针）

rbp

（基指针）

这几个是"特殊通道"，需要用别的方式（比如 lea）来操作。

# add / sub —— 加减法

add rax, rbx    ; rax = rax + rbx

sub rax, rbx    ; rax = rax - rbx

add rax, 10     ; 也可以直接加数值

# inc / dec —— 自增/自减

inc rax         ; rax = rax + 1

dec rax         ; rax = rax - 1

# 注释语法

和 C 语言类似：

# 单行注释

/\* 多行注释 \*/

# 🧮 Exercise 1：用汇编写斐波那契数列

题目要求：只使用 mov、add、sub、inc、dec 这五条指令，计算斐波那契数列的前几项。

练习网址：https://app.x64.halb.it/

这道题的核心思路就是：每项 = 前两项之和。难点在于寄存器有限，需要巧妙地"倒腾"数据。

# 视频参考解法

思路很直观——每个结果存到不同寄存器里，依次累加：

mov rax, 0          ; fib(0) = 0

mov rbx, rax

inc rbx             ; rbx = 1 → fib(1)

add rbx, rax

mov rcx, rbx        ; rcx = 1 → fib(2)

mov r15, rcx

add r15, rbx

mov rdx, r15        ; rdx = 2 → fib(3)

mov r15, rdx

add r15, rcx

mov rsi, r15        ; rsi = 3 → fib(4)

mov r15, rsi

add r15, rdx

mov r8, r15         ; r8 = 5 → fib(5)

mov r15, r8

add r15, rsi

mov r9, r15         ; r9 = 8 → fib(6)

mov r15, r9

add r15, r8

mov r10, r15        ; r10 = 13 → fib(7)

mov r15, r10

add r15, r9

mov r11, r15        ; r11 = 21 → fib(8)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAyz9NJEuPOn3tBn2xQHV4hU1Xg4s8z1yJeNhol7sG2G1zna7PYb45CR8pfBWAeG9ZqoON1pUfLfB11gSl7mLPq734ribEBq0M90/640?wx_fmt=png&from=appmsg)

> 💡 **小技巧**：这里用 `r15` 当"临时中转站"，因为通用寄存器不够用时，r15 是个好用的帮手。

# 我的解法（用减法恢复前值）

思路不太一样——我通过 sub 把上一个值"减回来"，恢复出更早的那一项：

mov rax, 0          ; fib(0) = 0

mov rbx, rax

inc rbx             ; rbx = 1 → fib(1)

add rbx, rax

mov rcx, rbx        ; rcx = 1 → fib(2)

sub rcx, rbx        ; 恢复 fib(0) 的值到 rcx...

add rdx, rcx        ; 继续累加

mov rsi, rdx

sub rdx, rcx        ; 再恢复

; 以此类推...

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAzjI91micMBlVseibJXQjiaae9ibn0OAa7W57cJic1mYMQHZYVicHPMF9Hia9rmCsG8vLeFrAW9vaRsDiansQYnHRrp0eF85bEp3iciaickzE/640?wx_fmt=png&from=appmsg)

对比两种解法：视频解法用 r15 做中转更优雅；我的方法更"笨"但能帮助理解数据在寄存器之间是怎么流动的。学汇编最重要的是理解数据流向，方法不唯一！

# 💾 内存操作：.data 段与 lea 指令

## 基本概念

64 bits = 8 bytes = 1 QUAD WORD = 4 WORDs

在.data段以下，我们可以定义内存中的数据：

| 指令 | 大小 | 说明 |
| --- | --- | --- |
| `.byte` | 1 字节 | 最小单位 |
| `.word` | 2 字节 |  |
| `.long` | 4 字节 |  |
| `.quad` | 8 字节 | 一个完整寄存器的大小 |
| `.skip` | 自定义 | 跳过指定字节数，可赋初始值 |

# lea —— 加载有效地址

lea 是汇编里非常重要的指令，它不取数据，只取地址：

lea rbx, [reg16]    ; rbx = reg16 这个标签在内存中的地址

add rbx, 8          ; 地址 +8，指向下一个 quad word

> 💡 **lea vs mov 的区别**：`mov` 是把内存里的**值**取出来；`lea` 是把内存的**地址**取出来。搞懂这个区别，后面学栈操作就通透了。

# 🔬 寄存器家族：大小嵌套关系

x86-64 的寄存器是有"父子关系"的：

rax  →  8 字节（完整寄存器）

└─ eax  →  4 字节（rax 的低 4 字节）

└─ ax  →  2 字节（eax 的低 2 字节）

├─ ah  →  高 1 字节（ax 的高位）

└─ al  →  低 1 字节（ax 的低位）

⚠️ 写代码时注意：修改 al 会影响 ax，修改 eax 会把 rax 的高 4 字节清零（不是保留！）。这个坑初学者很容易踩。

# 🧩 Exercise 2：操作内存数据

题目要求：把栈指针 rsp 指向指定地址，并向内存中写入特定数据：

地址 0-7：0x00375a02ffc0d713

地址 8-15：0xa4cdce6be1935500

地址 16-23：0x081cc7258d50c28b

地址 24-26：三个 0x1a

# 视频参考解法（.data 定义 + lea 定位）

最优雅的方式——直接在 .data 段定义好数据，然后用 lea 把 rsp 指过去：

lea rsp, [q1]         ; rsp 指向 q1 的地址

.data

q1: .quad 0x00375a02ffc0d713, 0xa4cdce6be1935500

.quad 0x081cc7258d50c28b

.skip 0x1a1a1a       ; 跳过 0x1a 字节（填充）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAxSaubzeOs7Sdlib0h5wx7tTLce0bkBjYgzLUFRgOHydC27elN4ra9oEiauZvBTqeic8be7GbPdpeyAaRD1CwflonLsbGcYKIlOIo/640?wx_fmt=png&from=appmsg)

# 视频方法 2（手动逐字节写入）

不依赖 .data 预定义，通过寄存器逐个写入：

lea rsp, [mem]

lea rsi, [mem]

mov rax, 0x375a02ffc0d713

mov [rsi], rax           ; 写入第 1 个 quad

add rsi, 8               ; 地址 +8

mov rax, 0xa4cdce6be1935500

mov [rsi], rax           ; 写入第 2 个 quad

add rsi, 8               ; 地址 +8

mov rax, 0x081cc7258d50c28b

mov [rsi], rax           ; 写入第 3 个 quad

add rsi, 8               ; 地址 +8

mov al, 0x1a

mov [rsi], al            ; 写入 0x1a

inc rsi

mov [rsi], al            ; 再写一个 0x1a

inc rsi

mov [rsi], al            ; 再写一个 0x1a

.data

mem: .skip 1024, 0xff    ; 预留 1024 字节空间

![](https://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAxoRsv3lyJIUho1bmbSMRZsheicLO7Fug8BhXqJ9wYzhx87425cnQIoiaUEfI7xCaTXlIDE1BmpuwWGf0L4Jkps5zVbrjMkYicQnQ/640?wx_fmt=png&from=appmsg)

> 💡 **关键点**：`mov [rsi], rax` 这种写法是**间接寻址**——方括号表示"把数据写到 rsi 指向的地址处"，而不是写到 rsi 寄存器本身。

# 我的解法（给每个值分配独立标签）

因为刚开始学的时候地址和值之间还有点混乱，所以给每个数据块都单独分配了标签：

lea rsp, [q1]

lea rsi, [q1]

lea rdi, [q2]

lea r8,  [q3]

lea r9,  [q4]

lea r10, [q5]

lea r11, [q6]

mov rax, 0x00375a02ffc0d713

mov [rsi], rax

mov rbx, 0xa4cdce6be1935500

mov [rdi], rbx

mov rcx, 0x081cc7258d50c28b

mov [r8], rcx

mov dl, 0x1a

mov [r9],  dl

mov [r10], dl

mov [r11], dl

.data

q1: .skip 8, 0xaa

q2: .skip 8, 0xbb

q3: .skip 8, 0xcc

q4: .skip 1, 0xdd

q5: .skip 1, 0xee

q6: .skip 1, 0xff

q7: .skip 1024, 0x00

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRw8ba1QkAzA8lWGrPGk8ZHyyNpB5YWn4PuslDcGOdM11HzYrEzB6D9yAlYTInJXQVoXvxmNeFe2XwS84rRGD6HVvoiaJ18WHUwiaPDZbONhY/640?wx_fmt=png&from=appmsg)

> 🤔 **复盘**：这种方法虽然"笨"，但好处是每个数据块的地址独立可控，不会互相覆盖。不过实际开发中显然视频方法更简洁高效。学习嘛，先理解原理再追求优雅！

# 📝 学习心得

汇编不难，就是繁琐—— 没有高级语言的便利，每一条指令都要手动管理数据和地址，但正因如此才能真正理解计算机底层在干什么。

寄存器是稀缺资源—— 通用寄存器就那么几个，怎么分配、怎么中转，是写汇编的核心技能。

lea 是理解内存的钥匙—— 搞清楚"取地址"和"取值"的区别，后面学栈帧、函数调用就顺了。

多写多练—— 看视频能看懂，但自己动手写的时候才发现地址和值的对应关系有多容易搞混。Exercise 2 的三种解法就是最好的例子。

> 🔗 **练习平台**：https://app.x64.halb.it/
>
> 💬 对 CTF 逆向感兴趣的同学欢迎关注我们的公众号，一起学习交流！

QQ群：1051436928

7月11号以后可能会保持日更，比赛的话当天会分享WP，11号有要去参加TRAE的一个线下活动，结束后给大家分享一下

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAyLaO7jbGn1micB35COoXcRibmHnX88t5OF2rgjK2lGzoyQLUiao99b5CNQ8n639PFAGicoBia82RXK4ZZaZUaJAJg2fWiayktHaF7Gg/0?wx_fmt=png)

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