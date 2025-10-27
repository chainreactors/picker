---
title: Ubuntu 22上自编译bpftrace
url: http://blog.nsfocus.net/ubuntu-22bpftrace/
source: 绿盟科技技术博客
date: 2022-10-27
fetch_date: 2025-10-03T21:00:58.838555
---

# Ubuntu 22上自编译bpftrace

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Ubuntu 22上自编译bpftrace

### Ubuntu 22上自编译bpftrace

[2022-10-26](https://blog.nsfocus.net/ubuntu-22bpftrace/ "Ubuntu 22上自编译bpftrace")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,206

参看 https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

aptitude install libbpfcc-dev libbpf-devaptitude install bison cmake flex g++ git libelf-dev zlib1g-dev libfl-dev systemtap-sdt-dev binutils-dev libcereal-dev llvm-12-dev llvm-12-runtime libclang-12-dev clang-12 libpcap-dev libgtest-dev libgmock-dev asciidoctor

cd /home/scz/src
git clone https://github.com/iovisor/bpftrace
git config –global –unset http.postBuffer
cp -R bpftrace bpftrace\_scz
mkdir bpftrace\_scz/build
cd bpftrace\_scz/build
cmake -DCMAKE\_BUILD\_TYPE=Release -DALLOW\_UNSAFE\_PROBE:BOOL=ON ..
make -j8
make install (可以不做)

最近git clone不挂代理时下载速率还可以，此时无需配置http.postBuffer，好像只在挂代理时才碰上那个问题。

$ /home/scz/src/bpftrace\_scz/build/src/bpftrace –versionbpftrace v0.16.0-32-gcf34

$ /home/scz/src/bpftrace\_scz/build/src/bpftrace –info |& grep bfd:
bfd: yes

“bfd: yes”支持”(k|u)probe:some+off”的语法，对应HAVE\_BFD\_DISASM宏，参看

bpftrace/src/build\_info.cpp

“-DALLOW\_UNSAFE\_PROBE:BOOL=ON”会对CMakeLists.txt产生影响

————————————————————————–
if (ALLOW\_UNSAFE\_PROBE)
set(BPFTRACE\_FLAGS “${BPFTRACE\_FLAGS}” HAVE\_UNSAFE\_PROBE)
endif(ALLOW\_UNSAFE\_PROBE)
————————————————————————–

最终会在编译命令中出现”-DHAVE\_UNSAFE\_PROBE”。该宏真正起作用的地方只有一处

————————————————————————–
/\*
\* bpftrace/src/attached\_probe.cpp
\*/
static void check\_alignment(std::string &path,
std::string &symbol,
uint64\_t sym\_offset,
uint64\_t func\_offset,
bool safe\_mode,
ProbeType type)
{
…
// If we did not allow unaligned uprobes in the
// compile time, force the safe mode now.
#ifndef HAVE\_UNSAFE\_PROBE
safe\_mode = true;
#endif
————————————————————————–

cmake -DCMAKE\_BUILD\_TYPE=Release ..

相当于

cmake -DCMAKE\_BUILD\_TYPE=Release -DALLOW\_UNSAFE\_PROBE:BOOL=OFF ..

即默认未定义HAVE\_UNSAFE\_PROBE宏，safe\_mode被强制赋值true，此时不允许在单条指令中间位置安装Hook，这真是没事找事的需求。

Ubuntu 22目前安装的0.14.0版bpftrace没有启用HAVE\_UNSAFE\_PROBE宏，也没有启用HAVE\_BFD\_DISASM宏，后者的缺失对功能限制太大。

————————————————————————–
Q: 如何安全判断bpftrace是否启用HAVE\_BFD\_DISASM宏？

A:

“bpftrace –info |& grep bfd:”报yes时表示启用HAVE\_BFD\_DISASM宏，报no表示未启用。

$ objdump –prefix-addresses –show-raw-insn –disassemble=\_\_open /lib/x86\_64-linux-gnu/libc.so.6 | less
…
0000000000114690 <\_\_open> f3 0f 1e fa endbr64
0000000000114694 <\_\_open+0x4> 41 54 push %r12
0000000000114696 <\_\_open+0x6> 41 89 f2 mov %esi,%r10d
0000000000114699 <\_\_open+0x9> 41 89 f4 mov %esi,%r12d
000000000011469c <\_\_open+0xc> 55 push %rbp
000000000011469d <\_\_open+0xd> 48 89 fd mov %rdi,%rbp
00000000001146a0 <\_\_open+0x10> 48 83 ec 68 sub $0x68,%rsp
00000000001146a4 <\_\_open+0x14> 48 89 54 24 40 mov %rdx,0x40(%rsp)
00000000001146a9 <\_\_open+0x19> 64 48 8b 04 25 28 00 00 00 mov %fs:0x28,%rax
00000000001146b2 <\_\_open+0x22> 48 89 44 24 28 mov %rax,0x28(%rsp)
…

用如下命令测试，不报错表示启用HAVE\_BFD\_DISASM宏，报错表示未启用。

/home/scz/src/bpftrace\_scz/build/src/bpftrace -e ‘uprobe:libc:open+4 /comm == str($1)/ {printf(“%s (%d)\n”,comm,pid)}’ cat
————————————————————————–
Q: 如何安全判断bpftrace是否启用HAVE\_UNSAFE\_PROBE宏？

A:

用如下命令测试

/home/scz/src/bpftrace\_scz/build/src/bpftrace –unsafe -e ‘uprobe:libc:open+5 /comm == str($1)/ {printf(“%s (%d)\n”,comm,pid)}’ cat

报”WARNING: Unsafe uprobe in the middle of the instruction”，但仍继续运行，表示启用HAVE\_UNSAFE\_PROBE宏。

报”ERROR: Could not add uprobe into middle of instruction”，结束运行，表示未启用HAVE\_UNSAFE\_PROBE宏。
————————————————————————–

为使用”uprobe:addr”，必须启用HAVE\_BFD\_DISASM宏，但与HAVE\_UNSAFE\_PROBE宏关系不大，除非addr不在正常指令边界上。

启用HAVE\_BFD\_DISASM宏有意义，启用HAVE\_UNSAFE\_PROBE宏没啥意义啊，谁吃饱了撑得去单条指令中间安装Hook？

注意到奇特的现象，即使已启用HAVE\_UNSAFE\_PROBE宏，仍然有

$ /home/scz/src/bpftrace\_scz/build/src/bpftrace –info |& grep “unsafe uprobe:”
unsafe uprobe: no

$ cd /home/scz/src/bpftrace\_scz/build

$ grep -RI “unsafe uprobe:”
src/build\_info.cpp: << ” unsafe uprobe: ”

在build\_info.cpp中查看附近代码

————————————————————————–
<< ” unsafe uprobe: ”
#ifdef HAVE\_UNSAFE\_UPROBE
<< “yes” << std::endl;
#else
<< “no” << std::endl;
#endif
————————————————————————–

此处判断是否启用HAVE\_UNSAFE\_UPROBE宏，整个项目中该宏只在此处出现，显然这是一处笔误

HAVE\_UNSAFE\_PROBE // 正确写法
HAVE\_UNSAFE\_UPROBE // 笔误

若无此笔误，”-DALLOW\_UNSAFE\_PROBE:BOOL=ON”之后应该有”unsafe uprobe: yes”。这解释了为什么满世界放狗，都看不到”unsafe uprobe: yes”，我被这个笔误坑得死去活来。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport43/)

[Next](https://blog.nsfocus.net/realtime-robust-malicious-traffic-detection-via-frequency-domain-analysis/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)