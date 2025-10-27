---
title: KnightCTF 2023 write-ups (RE category)
url: https://buaq.net/go-146499.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:08.202440
---

# KnightCTF 2023 write-ups (RE category)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/3094f2583d364ac2f63c82a5b9bf6fe9.jpg)

KnightCTF 2023 write-ups (RE category)

On Friday/Saturday (yeah, right about when layoff news hit) I played a CTF for fun/to relax with som
*2023-1-22 08:12:41
Author: [gynvael.coldwind.pl(查看原文)](/jump-146499.htm)
阅读量:54
收藏*

---

On Friday/Saturday (yeah, right about [when layoff news](https://blog.google/inside-google/message-ceo/january-update/) hit) I played a CTF for fun/to relax with some friends. Our choice was [KnightCTF 2023](https://ctftime.org/event/1792)and here are some writeups of the tasks I solved or helped solve (Reverse Engineering category only for now).

* [[RE 100] Help Jimmy](#helpjimmy)
* [[RE 150] The Activator](#theactivator)
* [[RE 200] KrackMe 1.0](#krackme)
* [[RE 250] Fan](#fan)
* [[RE 250] Take RISC five times](#riscv)

## [[RE 100] Help Jimmy](#helpjimmy)

Help Jimmy was a 64-bit Linux ELF binary, with a simple "game" implementation where the player had the choice to venture either into the Jungle or into the Sea. Regardless of the chosen path, it ended with Jimmy getting attacked by tigers or pirates and not getting the flag.

The game part was actually a distraction, as the actual purpose of the task was to notice that on the very top of the main() function there is something like this:

`int x = 5;
int y = 5;
if (x != y) {
some_function();
}`

While this is quite easy to spot in assembly, some decompilers (e.g. Ghidra) optimized out that branch and never showed it, thus making it easy to be missed.

![Screenshot from Ghidra showing assembly with the visible function call just after a comparison, and decompiler view with the if and function call missing.](https://gynvael.coldwind.pl/img/kctf23_helpjimmy.png)

Anyway, since this is a "just NOP the check" type of reverse engineering challenge (basically a classical *crackme*), the easiest way to solve is to either swap the comparison or NOP it out. This time around I've done the latter using GDB:

`break *0x0000555555555629
r
set *(unsigned char*)0x555555555653 = 0x90
set *(unsigned char*)0x555555555654 = 0x90
c`

Flag: **KCTF{y0u\_may\_ch00s3\_to\_look\_7h3\_other\_way\_but\_y0u\_can\_n3v3r\_say\_4gain\_that\_y0u\_did\_n0t\_know}**

## [[RE 150] The Activator](#theactivator)

Actually this was a super similar task to Help Jimmy – i.e. it was also a classic *crackme*. In this case we were greeted in the main() function with with a whole set of complicated checks, which eventually just set one single flag (as in a boolean value denoting whether the input was deemed acceptable). This flag was then checked, and when true, the CTF flag was displayed.

`if (checks_ok) {
show_flag();
} else {
std::cout << "Invalid Key." << std::endl;
}`

This time around, instead of NOPing out the check, I just set RIP just before the show\_flag() call:

`KnightOS License Checker.
Enter KnightOS Activation Key: ^C
Program received signal SIGINT, Interrupt.
0x00007ffff7b52992 in __GI___libc_read ...
(gdb) finish
Run till exit from #0 0x00007ffff7b52992 in __GI___libc_read ...
asdf
...
Value returned is $1 = 5
(gdb) set $rip=0x555555555bce
(gdb) c
Continuing.
KCTF{Th47_License_ch3cker_w4S_similar_t0_Wind0ws_95_OSR_Activator_Right?}
munmap_chunk(): invalid pointer
Program received signal SIGABRT, Aborted.`

## [[RE 200] KrackMe 1.0](#krackme)

KrackMe 1.0 was actually solved in 99% by my friends and I just jumped in in the last moment to help with the final step. In general the task consists of a flag being split into four 9-character parts. Then each part was XORed with – effectively – a constant byte, and compared to static hardcoded values.

The issue we faced was with the 3rd part of the flag – for some reason we were getting the constant wrong. But, since the constant was just one byte, we eventually just brute forced it. Here's the script:

`` v13 = "mer`]MtGeaUG9UeDoU"
v14 = "(G~Ty_G{(v}QlOto|s"
v17 = "You don't have access to KrackMe 1.0 !"
v18 = "Since you are here let me ask you something..."
v15 = "Please enter the flag : "
v16 = "Oh My God ! What is that ?"
v20 = "Did you know, Bangladesh has the longest natural beach?..."
v13r = "mer`]MtGeaUG9UeDoU"
v14r = "(G~Ty_G{(v}QlOto|s"
for m in range(0,255):
flag = ""
for i in range(9):
flag += (chr((ord(v13r[i]) ^ ord(v20[14]) ^ ord(v16[8])) & 0xff))
for i in range(9):
flag += (chr((ord(v13r[i + 9]) ^ ord(v17[1]) ^ ord(v13r[1])) & 0xff))
mid = ""
for i in range(9):
mid += (chr((ord(v14[i]) ^ m) & 0xff))
flag += mid
for g in range(9):
flag += (chr((ord(v14r[g + 9]) ^ ord(v17[11]) ^ ord(v17[1])) & 0xff))
if "_" in mid: # Output filtering by guessing there will be _ in this part.
print(flag) ``

And the flag:

`$ python go.py
KCTF{kRaCk_M3_oNe_(G~Ty_G{(xs_bAzar}
KCTF{kRaCk_M3_oNe_#Lu_rTLp#xs_bAzar}
KCTF{kRaCk_M3_oNe_0_fLaG_c0xs_bAzar}
KCTF{kRaCk_M3_oNe_ f_uX~fZ xs_bAzar}
KCTF{kRaCk_M3_oNe_
cZp]{c_
xs_bAzar}
KCTF{kRaCk_M3_oNe_aXr_ya]xs_bAzar}
KCTF{kRaCk_M3_oNe__0 #(0
_xs_bAzar}`

## [[RE 250] Fan](#fan)

In Fan we got the text output of Python's *dis* run on a program that outputted the flag. Given that I know Python bytecode pretty well (in the past I've even written a chapter for a reverse-engineering book about Python bytecode-level obfuscation), I immediately liked the task. Initially I thought about writing a small "compiler" for the text bytecode, but rejected this idea in favor of just re-implementing the function in Python. To keep myself honest I've done this while having the provided text file side-by-side with a console running python -m dis on my re-implementation. I do have to note that since I was using a different Python version, compilation artifacts were a little different – e.g. my version of Python didn't use the SETUP\_LOOP opcode to setup for loops.

The whole thing took maybe 20 minutes. One place I initially changed however were calls to eval() – I replaced them with calls to my own fake\_eval() which basically just printed the code to be executed. There turned out to be nothing interesting there however, but it's always good to check.

Re-implementation:

`def define_false(s):
lstr = []
u = 0
packed = ''
for c in s:
if c == '[':
lstr.append((u, packed))
packed = ''
u = 0
continue
if c == ']':
num, prev_string = lstr.pop()
packed = prev_string + packed * num
continue
if c.isdigit():
u = u * 10 + int(c)
continue
packed += c
return packed
def define_true(p):
res = ''
for packed in p:
res += str(len(packed)) + '[:]' + packed
return res
def fake_eval(x):
return eval(x)
def define_both(p):
unpacked = []
for i in p:
packed = i.split(')')
char = ''
for j in packed:
if j == '':
break
j += ')'
char += fake_eval(j)
unpacked.append(char)
return unpacked
if __name__ == '__main__':
s = [
'chr(103)chr(48)chr(79)chr(97)chr(116)chr(125)',
'chr(105)chr(115)',
'chr(109)chr(69)chr(51)chr(115)chr(115)chr(105)',
'chr(115)chr(105)chr(85)chr(85)chr(85)',
'chr(75)chr(67)chr(84)chr(70)chr(123)'
]
s = s[::-1] # Initially I got the array ordering wrong.
print(define_false(define_true(define_both(s))))`

And the flag: **KCTF{:::::siUUU::::::mEssi::::::::::::::::::::::::::::::::is::::::gOat}**

## [[RE 250] Take RISC five times](#riscv)

In this task we basically got an RISC-V assembly file (as in: text file) with one function. While I've implemented a small [RISC-V emulator](https://github.com/google/google-ctf/blob/master/other/re-risky/directors-cut/spoilers_and_source/src/riscv-emu.c) in the past, I honestly remember nothing about the architecture. Thankfully, it turned out that's not needed!

Since the assembly file turned out to be pretty well formatted, I decided to try to assemble it and link it with a minimal C program. A...