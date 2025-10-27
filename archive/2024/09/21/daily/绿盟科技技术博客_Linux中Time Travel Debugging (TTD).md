---
title: Linux中Time Travel Debugging (TTD)
url: https://blog.nsfocus.net/linux%e4%b8%adtime-travel-debugging-ttd/
source: 绿盟科技技术博客
date: 2024-09-21
fetch_date: 2025-10-06T18:26:58.154879
---

# Linux中Time Travel Debugging (TTD)

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

# Linux中Time Travel Debugging (TTD)

### Linux中Time Travel Debugging (TTD)

[2024-09-20](https://blog.nsfocus.net/linux%E4%B8%ADtime-travel-debugging-ttd/ "Linux中Time Travel Debugging (TTD)")[绿盟科技](https://blog.nsfocus.net/author/nsfocuser/ "View all posts by 绿盟科技")

阅读： 2,945

## 一、背景介绍

Windows有相当成熟的Time Travel Debugging (TTD)工具，Linux也有类似的，比如rr、UDB等。但GDB原生反向执行算不得TTD，不能脱离目标进程存在，不能反复鞭尸。

本文以同一个测试用例简单演示这三种技术，它们的共同点是，反向执行相关命令几乎一样，尽管实现原理并不相同。

本文假设读者具有GDB调试基础，未做任何前置科普。

## 二、测试用例

这是Frank Tetzel提供的一个测试用例:

————————————————————————–
int main ( int argc, char \* argv[] )
{
unsigned int array[32];
unsigned int i;

for ( i = 0; i < sizeof(array); i++ )
{
array[i] = i;
}
return 0;
}
————————————————————————–

$ gcc -static -Wall -pipe -O0 -g3 -fno-stack-protector -o testcase\_0\_dbg testcase\_0.c

编译时指定-O0，以免优化for循环，指定-fno-stack-protector，刻意破坏RetAddr。

$ ./testcase\_0\_dbg
Segmentation fault (core dumped)

## 三、 GDB原生反向执行

参看

————————————————————————–
Reverse Debugging with GDB
https://www.sourceware.org/gdb/wiki/ReverseDebug

Process Record and Replay
https://www.sourceware.org/gdb/wiki/ProcessRecord

Process Record Tutorial
https://www.sourceware.org/gdb/wiki/ProcessRecord/Tutorial

Recording Inferior’s Execution and Replaying It
https://sourceware.org/gdb/current/onlinedocs/gdb.html/Process-Record-and-Replay.html

Running programs backward
https://sourceware.org/gdb/current/onlinedocs/gdb.html/Reverse-Execution.html
————————————————————————–

$ gdb –version
GNU gdb (Ubuntu 12.1-0ubuntu1~22.04) 12.1

gdb -q -nx ./testcase\_0\_dbg

(gdb) start
(gdb) record
(gdb) c
Continuing.
Process record: failed to record execution log.

Program stopped.
0x0000002700000026 in ?? ()

不知为何提示”Process record: failed to record execution log”，是因为异常停止吗？

本例在start处执行record，开始录制，调试实际目标时，可在任意关注的位置开始record。

(gdb) info record
Active record target: record-full
Record mode:
Lowest recorded instruction number is 1.
Highest recorded instruction number is 775.
Log contains 775 instructions.
Max logged instructions is 200000.

记录了775条指令，若从此处反向执行，将从”Record mode”切换至”Replay mode”，可用”info record”查看。

栈中RetAddr被写成0x2700000026

(gdb) x/1gx $rsp-8
0x7fffffffe0f8: 0x0000002700000026

先禁用硬件数据断点，再对之设数据断点，反向执行，找出谁写的:

(gdb) set can-use-hw-watchpoints 0
(gdb) watch \*0x7fffffffe0f8

缺省情况下，数据断点用硬件断点。但”Replay mode”中无论正向执行、反向执行，硬件数据断点均不工作，设也白设。正确做法是，先禁用硬件数据断点，再设数据断点，如上。

开始反向执行:

(gdb) rc

Watchpoint 2: \*0x7fffffffe0f8

Old value = 38
New value = 4201402
0x000000000040176d in main (argc=1, argv=0x7fffffffe2c8) at testcase\_0.c:15
15 array[i] = i;

找到修改RetAddr的代码，查看i变量:

(gdb) i locals i
i = 38

局部变量i预期最大32，现已38，源代码有问题

(gdb) x/1gx &array[i]
0x7fffffffe0f8: 0x0000000000401bba

这是RetAddr所在，RetAddr应为0x401bba，其原址附近代码如下:

(gdb) x/5i 0x401bba-16
0x401baa <\_\_libc\_start\_call\_main+90>: mov edi,DWORD PTR [rsp+0x14]
0x401bae <\_\_libc\_start\_call\_main+94>: mov rsi,QWORD PTR [rsp+0x18]
0x401bb3 <\_\_libc\_start\_call\_main+99>: mov rax,QWORD PTR [rsp+0x8]
0x401bb8 <\_\_libc\_start\_call\_main+104>: call rax
0x401bba <\_\_libc\_start\_call\_main+106>: mov edi,eax

## 四、rr

1) 编译rr源码

参看

————————————————————————–
Building And Installing rr (Record and Replay Framework)
https://github.com/rr-debugger/rr/wiki/Building-And-Installing
————————————————————————–

在Ubuntu 22中执行:

apt-get install ccache cmake make g++-multilib gdb \
pkg-config coreutils python3-pexpect manpages-dev git \
ninja-build capnproto libcapnp-dev zlib1g-dev

git clone https://github.com/rr-debugger/rr.git rr

mkdir rrobj && cd rrobj
cmake -DCMAKE\_BUILD\_TYPE=Release ../rr
make -j8
ls -l ./bin/rr
./bin/rr help

make -j8 test

test不要求root权限，就用普通用户好了，个别失败无关紧要。

2) 检查rr可用性

若在虚拟机中使用rr，有必要检查rr可用性，检查Guest环境是否符合要求。参看

————————————————————————–
https://github.com/rr-debugger/rr/wiki/Building-And-Installing
https://github.com/rr-debugger/rr/wiki/Will-rr-work-on-my-system
————————————————————————–

要求Guest内核版本大于等于4.7，用”uname -r”确认。以root身份执行

perf stat -e br\_inst\_retired.conditional true |& grep br\_inst\_retired

若br\_inst\_retired为0，表示Guest环境不符合要求。

3) 测试rr

针对testcase\_0\_dbg进行录制:

$ \_RR\_TRACE\_DIR=/tmp /path/rrobj/bin/rr record ./testcase\_0\_dbg
rr: Saving execution to trace directory `/tmp/testcase\_0\_dbg-0′.
Segmentation fault

上述命令相当于Windows的TTD.exe或tttracer.exe。

调试rr录制结果:

$ /path/rrobj/bin/rr replay /tmp/testcase\_0\_dbg-0

0x0000000000401620 in \_start ()
(rr) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
0x0000002700000026 in ?? ()

(rr) x/1gx $rsp-8
0x7ffcca701928: 0x0000002700000026
(rr) set can-use-hw-watchpoints 0
(rr) watch \*0x7ffcca701928
(rr) rc (一次rc)
Continuing.

Program received signal SIGSEGV, Segmentation fault.
0x0000002700000026 in ?? ()
(rr) rc (二次rc)
Continuing.

Watchpoint 1: \*0x7ffcca701928

Old value = 38
New value = 4201402
0x000000000040176d in main (argc=1, argv=0x7ffcca701b08) at testcase\_0.c:15
15 array[i] = i;
(rr) i locals i
i = 38
(rr) p/x &array[i]
$1 = 0x7ffcca701928
(rr) x/1gx &array[i]
0x7ffcca701928: 0x0000000000401bba

相比GDB原生反向执行，rr的优势是可保存录制结果，可反复鞭尸。但就本例而言，rr没有优势，比GDB原生反向执行慢。

## 五、UDB

参看

————————————————————————–

> [Undo Free Trial](https://undo.io/udb-free-trial/)

https://docs.undo.io/

Getting started with UDB
https://docs.undo.io/GettingStartedWithUDB.html

Using the LiveRecorder tool
https://docs.undo.io/UsingTheLiveRecorderTool.html
————————————————————————–

/path/UDB/Undo-Suite-x86-8.0.0/live-record \
-q \
–tmpdir-root /tmp \
–disable-aslr \
–record-on entry \
–save-on always \
-o /path/testcase/0/testcase\_0\_dbg.record \
/path/testcase/0/testcase\_0\_dbg

上述命令相当于Windows的TTD.exe或tttracer.exe。复杂目标的录制结果可能很大，应指定适当的–tmpdir-root与-o参数。

UDB与rr、TTD.exe有个不同，既可用live-record直接录制，也可在调试过程中用”urecord+usave”录制保存，后一种方式可针对某个区段精确录制，此处未演示。

$ ls -lh /path/testcase/0/testcase\_0\_dbg.record
-rw-r–r– 1 scz scz 1016K Sep 14 16:05 /path/testcase/0/testcase\_0\_dbg.record

/path/UDB/Undo-Suite-x86-8.0.0/udb \
-q \
–checkupdates never \
–keyfile /path/UDB/Undo-Suite-x86-8.0.0/key \
–tmpdir-root /tmp \
-nx \
-ex “set history save off” \
–sessions no \
–load /path/testcase/0/testcase\_0\_dbg.record

0x0000000000401620 in \_start ()

The debugged program is at the beginning of recorded history. Start debugging
from here or, to proceed towards the end, use:
continue – to replay from the beginning
ugo end – to jump straight to the end of history
start 1> ugo end
0x0000002700000026 in ?? ()
end 3,874> x/1gx $rsp-8
0x7fffffffdfc8: 0x0000002700000026

UDB有个last命令，跳至指定表达式最后一次变动的代码所在:

end 3,874> last \*0x7fffffffdfc8
Searching backward for changes to 0x7fffffffdfc8-0x7fffffffdfcc for the
expression:
\*0x7fffffffdfc8

Was = 38
Now = 4201402
0x000000000040176d in main (argc=1, argv=0x7fffffffe1a8) at testcase\_0.c:15
15 array[i] = i;
97% 3,784> i locals i
i = 38

last命令省了”watch+rc”，一步到位。

UDB也可像GDB、rr那样，watch+rc，此处未演示。与GDB原生反向执行及rr不同，UDB反向执...