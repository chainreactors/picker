---
title: CBCTF 赛博杯新生训练赛 2025 （综合赛道）WriteUp
url: https://www.zhaoj.in/read-9135.html
source: glzjin
date: 2025-12-17
fetch_date: 2025-12-18T03:19:35.476173
---

# CBCTF 赛博杯新生训练赛 2025 （综合赛道）WriteUp

[![glzjin](https://www.zhaoj.in/wp-content/uploads/2016/04/1460635478e753758d45e5fb95f465e8ceaaabe897.png)](https://www.zhaoj.in/ "glzjin")

西兴街道物理安全研究员 | 原学生@北京联合大学 | 信息安全爱好者 | 全栈开发 | OSCP | OSWE | OSEP | OSED | OSCE3 | OSWA | OSWP | OSDA | OSMR | KLCP | CISSP | ASCP | S+ | PMP | 为心中的美好而战

* [上一篇文章](https://www.zhaoj.in/read-9096.html)

* [Glzjin](https://www.zhaoj.in/read-author/glzjin "作者简介")

切换导航

* [首页](https://www.zhaoj.in "首页")
* [Support Me!](https://www.zhaoj.in/support-me "Support Me!")

## [CBCTF 赛博杯新生训练赛 2025 （综合赛道）WriteUp](https://www.zhaoj.in/read-9135.html)

张贴在 [2025年12月17日](https://www.zhaoj.in/read-date/2025/12/17 "CBCTF 赛博杯新生训练赛 2025 （综合赛道）WriteUp") 来自 [Glzjin](https://www.zhaoj.in/read-author/glzjin) in  [技术](https://www.zhaoj.in/read-category/tech "查看技术中的全部文章")

除了那个MISC，其他基本都是机器人做的了。

![](https://www.zhaoj.in/wp-content/uploads/2025/12/176595028227db5c050785cd2fc9f6347f6a13c0cf-1024x476.png)

Table of Contents

Toggle

* [Linux](#Linux)
  + [三剑客](#%E4%B8%89%E5%89%91%E5%AE%A2)
  + [I use Debian btw](#I_use_Debian_btw)
  + [GuessWhat](#GuessWhat)
  + [Coreflag](#Coreflag)
* [Pwn](#Pwn)
  + [EzShellcode](#EzShellcode)
  + [Ceccomp](#Ceccomp)
  + [grub](#grub)
  + [Aegle\_seeker](#Aegle_seeker)
  + [Ԁ()ꓤ](#%D4%80%EA%93%A4)
  + [ret2mmap](#ret2mmap)
  + [i18n-misuse](#i18n-misuse)
* [Misc](#Misc)
  + [C!C!B!](#CCB)
  + [pyjail 1](#pyjail_1)
  + [pyjail 2](#pyjail_2)
  + [pyjail 3](#pyjail_3)
  + [pyjail 4](#pyjail_4)
  + [pyjail 5](#pyjail_5)
  + [pyjail 6](#pyjail_6)
  + [Realworld-HackVcenter](#Realworld-HackVcenter)
  + [EZSqli](#EZSqli)
  + [EZSocialEngineering](#EZSocialEngineering)
  + [strange\_png](#strange_png)
* [Reverse](#Reverse)
  + [大胃袋](#%E5%A4%A7%E8%83%83%E8%A2%8B)
  + [Catch\_Tofv](#Catch_Tofv)
  + [BF6](#BF6)
  + [ez\_reverse](#ez_reverse)
  + [BF5](#BF5)
  + [Welcome](#Welcome)
  + [Strange](#Strange)
  + [Lost\_Key](#Lost_Key)
* [Crypto](#Crypto)
  + [Wilderness](#Wilderness)
  + [RSA\_Shrimp](#RSA_Shrimp)
  + [Chaos](#Chaos)
* [WEB](#WEB)
  + [Realworld-ezNote](#Realworld-ezNote)
  + [ezphp](#ezphp)
  + [ezgroovy](#ezgroovy)
  + [ezxss](#ezxss)
  + [Kill-tomcat-memshell](#Kill-tomcat-memshell)
* [Pentest](#Pentest)
  + [Counter APT 1](#Counter_APT_1)
  + [Counter APT 2](#Counter_APT_2)
  + [大意失荆州](#%E5%A4%A7%E6%84%8F%E5%A4%B1%E8%8D%86%E5%B7%9E)
* [AI](#AI)
  + [GPT5-jail](#GPT5-jail)
* [Forenics](#Forenics)
  + [可恶，有人攻击我-1](#%E5%8F%AF%E6%81%B6%EF%BC%8C%E6%9C%89%E4%BA%BA%E6%94%BB%E5%87%BB%E6%88%91-1)
  + [可恶，有人攻击我-2](#%E5%8F%AF%E6%81%B6%EF%BC%8C%E6%9C%89%E4%BA%BA%E6%94%BB%E5%87%BB%E6%88%91-2)
  + [可恶，有人攻击我-3](#%E5%8F%AF%E6%81%B6%EF%BC%8C%E6%9C%89%E4%BA%BA%E6%94%BB%E5%87%BB%E6%88%91-3)
  + [可恶，有人攻击我-4](#%E5%8F%AF%E6%81%B6%EF%BC%8C%E6%9C%89%E4%BA%BA%E6%94%BB%E5%87%BB%E6%88%91-4)
  + [可恶，有人攻击我-5](#%E5%8F%AF%E6%81%B6%EF%BC%8C%E6%9C%89%E4%BA%BA%E6%94%BB%E5%87%BB%E6%88%91-5)

## Linux

### 三剑客

```
# 三剑客

连上telnet看到有个文本文件叫flag.txt，直接cat发现不行，说有权限问题。用ls -la看了一下，发现flag.txt其实是个符号链接，指向另一个地方。

发现真正的flag文件在/root/flag.txt，但没权限直接读。这时候想到题目说三剑客，应该是要用grep、awk、sed这些工具。

试了用grep来读，发现也不行。然后想到用find命令来找有权限读的文件，发现有个可执行文件叫readflag，运行它就直接把flag打印出来了。

运行readflag：
```
./readflag
```

直接拿到flag。

CBCTF{2679f46b-77b5-4e27-933d-2884be32dfe3}
```

### I use Debian btw

```
# I use Debian btw

连上靶机发现有个`checkme`程序，运行一下看看要干啥。它问了一堆系统相关的问题：系统发行版全称、ctf用户的UID、Jackson的签名、lazygit的路径、lazygit的Build ID。

先看系统发行版：
```bash
cat /etc/os-release
```
看到`PRETTY_NAME="Debian GNU/Linux 13 (trixie)"`，搞定第一个。

查ctf用户的UID：
```bash
id ctf
```
输出`uid=1000(ctf) gid=1000(ctf) groups=1000(ctf)`，UID是1000。

找Jackson的签名，直接cat不了`/home/Jackson/signature`，没权限。发现`grep`命令有点特殊：
```bash
ls -la /usr/bin/grep
```
看到`-rwsr-sr-x 1 root Jackson`，grep有SGID权限还属于Jackson组！直接用grep读：
```bash
grep '' /home/Jackson/signature
```
拿到签名`f0abb284-0554-43c0-beaa-3ebf67bde03c`。

lazygit在`/home/ctf/lazygit`，直接用file命令看Build ID：
```bash
file /home/ctf/lazygit
```
输出里有`BuildID[sha1]=c2d913ebc9b342bfa601bb4296492a46706d0769`。

把所有答案拼起来传给checkme：
```bash
echo -e "Debian GNU/Linux 13 (trixie)\\n1000\\nf0abb284-0554-43c0-beaa-3ebf67bde03c\\n/home/ctf/lazygit\\nc2d913ebc9b342bfa601bb4296492a46706d0769" | checkme
```
直接出flag了。

CBCTF{WoW-u-R-linuX-mASTER}
```

### GuessWhat

```
# GuessWhat

连上 telnet 看了一眼，是个猜数字游戏，要猜一个超大的数字，输错了就直接断开，这咋猜啊

试了几次发现每次数字都不一样，肯定不是手动猜了

上 pwntools 写个脚本自动连

```python
from pwn import *
context.log_level = 'debug'
io = remote('101.37.152.107', 41511)
```

收到欢迎消息和提示 "Give me your answer:"

直接发个数字过去试试，果然错了，连接被关闭

得想办法拿到那个要猜的数字，但数字是从服务器生成的，不在本地

回头看欢迎消息，发现里面直接打印了数字！"The number is: 一个很大的数字"

原来如此，服务器直接把答案告诉我了，我只需要提取出来再发回去就行

写脚本提取数字：

```python
io.recvuntil('The number is: ')
num = io.recvline().strip()
io.recvuntil('Give me your answer:')
io.sendline(num)
```

运行后成功收到 "You are right!" 和 flag

第一次运行的时候没处理好接收，数字没提取完整，调试了一下发现 recvuntil 和 recvline 要配合好

最后 flag 是 `CBCTF{PWNtOO1sS5-Ls_SuCH_A-POw3RfU1-tOol}`
```

### Coreflag

```
# coreflag

连上题目给的telnet，看到有提示说源码丢了，只剩下符号和core文件。让我用debuginfod来获取调试符号。

直接运行程序报错，说缺少libfetch.so.6。用ldd一看，确实没有这个库。

先试试用debuginfod获取符号。设置环境变量：
```bash
export DEBUGINFOD_URLS="https://debuginfod.debian.net"
```

然后运行：
```bash
debuginfod-find core coreflag
```
结果报错，说core文件格式不对。看来得换个方法。

用readelf看core文件的build-id：
```bash
readelf -n core
```
发现build-id是`feb7c5d2bfc7e1e98d2a21c7b072a4c2d5b1e1a2`。

用debuginfod-find获取符号：
```bash
debuginfod-find debuginfo feb7c5d2bfc7e1e98d2a21c7b072a4c2d5b1e1a2
```
返回了路径`/usr/lib/debug/.build-id/fe/b7c5d2bfc7e1e98d2a21c7b072a4c2d5b1e1a2.debug`。

用curl直接下载：
```bash
curl -o debuginfo https://debuginfod.debian.net/download/debuginfo/feb7c5d2bfc7e1e98d2a21c7b072a4c2d5b1e1a2
```
这下拿到了debuginfo文件。

用gdb加载core文件和debuginfo：
```bash
gdb -c core debuginfo
```
在gdb里运行`bt`看backtrace，发现崩溃在`parse_flag`函数。

反汇编`parse_flag`：
```bash
disassemble parse_flag
```
看到函数调了`getenv`和`strcmp`，比较环境变量`FLAG`的值。

在gdb里查看环境变量：
```bash
p (char**)environ
```
找到了`FLAG=CBCTF{FEtcH-dE6uG_sYYYYYYyYYMBoLs_W1tH-dEBuGLNFoD-Is-UsEFUL}`。

搞定！

`CBCTF{FEtcH-dE6uG_sYYYYYYyYYMBoLs_W1tH-dEBuGLNFoD-Is-UsEFUL}`
```

## Pwn

### EzShellcode

```
# EzShellcode

连上题目看看，直接给了源码。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <seccomp.h>
#include <linux/seccomp.h>

void init() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

void sandbox() {
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(close), 0);
    seccomp_load(ctx);
}

int main() {
    init();
    sandbox();
    void *shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (shellcode == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }
    printf("Give me your shellcode: ");
    fflush(stdout);
    read(0, shellcode, 0x1000);
    ((void (*)())shellcode)();
    return 0;
}
```

发现是个简单的shellcode题，给了mmap的可执行内存，直接读shellcode进去执行。但是有个沙箱，只允许exit、exit_group、read、write、open、close这几个系统调用。

用seccomp-tools dump一下确认沙箱规则。

```bash
seccomp-tools dump ./EzShellcode
```

输出是：

```
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x09 0xc000003e  if (A != ARCH_X86_64) goto 0011
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x06 0xffffffff  if (A != 0xffffffff) goto 0011
 0005: 0x15 0x04 0x00 0x00000000  if (A == read) goto 0010
 0006: 0x15 0x03 0x00 0x00000001  if (A == write) goto 0010
 0007: 0x15 0x02 0x00 0x00000002  if (A == open) goto 0010
 0008: 0x15 0x01 0x00 0x00000003  if (A == close) goto 0010
 0009: 0x15 0x00 0x01 0x0000003c  if (A != exit) goto 001...