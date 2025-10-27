---
title: eBPF入门文献汇总
url: http://blog.nsfocus.net/ebpf/
source: 绿盟科技技术博客
date: 2022-12-09
fetch_date: 2025-10-04T01:00:39.660931
---

# eBPF入门文献汇总

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

# eBPF入门文献汇总

### eBPF入门文献汇总

[2022-12-08](https://blog.nsfocus.net/ebpf/ "eBPF入门文献汇总")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 3,522

## eBPF

2022.9.26之前，我对eBPF一无所知，历史上用于抓包的BPF不算。后来陆续看了很多eBPF文献，算是入了门，写点入门心得。

eBPF最近几年发展迅速，许多新特性挑内核，有些过时的eBPF限制没必要与之较劲，入门时完全可以在较新内核上学习，比较熟了再去生产环境考虑向后兼容性。我在Ubuntu 22.04.1 LTS (Jammy Jellyfish)上测试eBPF，5.15.0-52-generic内核，这个内核版本已经较高，即便如此，仍有一些eBPF新特性未被支持。

## 一、 bpftrace

入门最好从bpftrace开始，遍历如下文献，不要挑着看，全都看一遍，没必要零敲碎打地看其他的。

————————————————————————–
https://github.com/iovisor/bpftrace
https://github.com/iovisor/bpftrace/tree/master/tools

自编译bpftrace
https://github.com/iovisor/bpftrace/blob/master/INSTALL.md
(有讲Disable Lockdown)

The bpftrace One-Liner Tutorial
https://github.com/iovisor/bpftrace/blob/master/docs/tutorial\_one\_liners.md

bpftrace Reference Guide
https://github.com/iovisor/bpftrace/blob/master/docs/reference\_guide.md

bpftrace(8) Manual Page
https://github.com/iovisor/bpftrace/blob/master/man/adoc/bpftrace.adoc

bpftrace(8)
https://manpages.ubuntu.com/manpages/focal/en/man8/bpftrace.bt.8.html

bpftrace Cheat Sheet
https://www.brendangregg.com/BPF/bpftrace-cheat-sheet.html
————————————————————————–

1.1 查看安装版bpftrace版本

$ bpftrace –version
bpftrace v0.14.0

$ bpftrace –info |& grep version
version: v0.14.0

$ dpkg -l bpftrace | grep ^ii
ii bpftrace 0.14.0-1 amd64 high-level tracing language for Linux eBPF

$ apt-cache show bpftrace | grep Version
Version: 0.14.0-1

1.2 自编译bpftrace

遍历

————————————————————————–
https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

《Ubuntu 22上自编译bpftrace》
http://scz.617.cn:8/unix/202210221758.txt
————————————————————————–

自编译的bpftrace支持”(k|u)probe:some+off”

1.3 tracepoint:\*

遍历

bpftrace Reference Guide
https://github.com/iovisor/bpftrace/blob/master/docs/reference\_guide.md

bpftrace -l ‘tracepoint:\*’ | less
bpftrace -l ‘tracepoint:\*’ | wc -l

1607个

还可用perf工具查看

perf list | grep Tracepoint | less
perf list | grep Tracepoint | wc -l

1602个

1.3.1 tracepoint:syscalls:\*

bpftrace -l ‘tracepoint:syscalls:\*’ | less
bpftrace -l ‘tracepoint:syscalls:\*’ | wc -l

686个

$ bpftrace -lv ‘tracepoint:syscalls:sys\_enter\_openat’
tracepoint:syscalls:sys\_enter\_openat
int \_\_syscall\_nr
int dfd
const char \* filename
int flags
umode\_t mode

bpftrace -e ‘tracepoint:syscalls:sys\_enter\_openat
/comm == str($1)/
{printf(“%s (%d) -> %s\n”,comm,pid,str(args->filename))}’ \
cat

cat (97060) -> /etc/ld.so.cache
cat (97060) -> /lib/x86\_64-linux-gnu/libc.so.6
cat (97060) -> /usr/lib/locale/locale-archive
cat (97060) -> /etc/hosts

1.3.2 tracepoint:raw\_syscalls:\*

$ bpftrace -lv ‘tracepoint:raw\_syscalls:\*’
tracepoint:raw\_syscalls:sys\_enter
long id
unsigned long args[6]
tracepoint:raw\_syscalls:sys\_exit
long id
long ret

只有2个

$ grep “\_\_NR\_open” /usr/include/asm/unistd\_64.h
#define \_\_NR\_open 2
#define \_\_NR\_openat 257
#define \_\_NR\_open\_by\_handle\_at 304
#define \_\_NR\_open\_tree 428
#define \_\_NR\_openat2 437

bpftrace -e ‘tracepoint:raw\_syscalls:sys\_enter
/(args->id == 257 || args->id == 437) && comm == str($1)/
{printf(“%s (%d) -> [%d] %s\n”,comm,pid,args->id,str(uptr(args->args[1])))}’ \
cat

cat (97947) -> [257] /etc/ld.so.cache
cat (97947) -> [257] /lib/x86\_64-linux-gnu/libc.so.6
cat (97947) -> [257] /usr/lib/locale/locale-archive
cat (97947) -> [257] /etc/hosts

1.4 kprobe:\*/kretprobe:\*

bpftrace -l ‘kprobe:\*’ | less
bpftrace -l ‘kprobe:\*’ | wc -l

bpftrace -l ‘kretprobe:\*’ | less
bpftrace -l ‘kretprobe:\*’ | wc -l

52464个，”kprobe:\*”比”tracepoint:\*”多多了。

与”tracepoint:\*”不同，无法用”bpftrace -lv”查看”kprobe:\*”的参数，但有其他办法间接知道参数。可以查看相应的”kfunc:\*”，会自动利用BTF；可以借助stap快速查看参数；或直接查看内核源码。

$ bpftrace -lv ‘kfunc:do\_sys\_openat2’
kfunc:do\_sys\_openat2
int dfd
const char \* filename
struct open\_how \* how
long int retval

$ stap -L ‘kernel.function(“do\_sys\_openat2”)’
kernel.function(“do\_sys\_openat2@/build/linux-kQ6jNR/linux-5.15.0/fs/open.c:1199”) $dfd:int $filename:char const\* $how:struct open\_how\* $op:struct open\_flags

“kprobe:do\_sys\_openat2″无法用dfd、filename、how，但可以用arg0、arg1、arg2
访问之。

bpftrace -e ‘kprobe:do\_sys\_openat2
/comm == str($1)/
{printf(“%s (%d) -> %s\n”,comm,pid,str(uptr(arg1)))}’ \
cat

cat (97121) -> /etc/ld.so.cache
cat (97121) -> /lib/x86\_64-linux-gnu/libc.so.6
cat (97121) -> /usr/lib/locale/locale-archive
cat (97121) -> /etc/hosts

单行内容较长时，可以指定较大的BPFTRACE\_STRLEN

BPFTRACE\_STRLEN=200 \
bpftrace -e ‘kprobe:do\_sys\_openat2
{printf(“%s (%d) -> %s\n”,comm,pid,str(uptr(arg1)))}’

1.4.1 BTF

$ grep \_BTF /boot/config-$(uname -r)
CONFIG\_VIDEO\_SONY\_BTF\_MPX=m
CONFIG\_DEBUG\_INFO\_BTF=y
CONFIG\_PAHOLE\_HAS\_SPLIT\_BTF=y
CONFIG\_DEBUG\_INFO\_BTF\_MODULES=y

若有BTF可用，bpftrace可以查看”kfunc:vfs\_open”、”struct path”

$ bpftrace -lv ‘kfunc:vfs\_open’
kfunc:vfs\_open
const struct path \* path
struct file \* file
int retval

$ bpftrace -lv “struct path”
struct path {
struct vfsmount \*mnt;
struct dentry \*dentry;
};

1.4.2 override (修改返回值)

$ grep -E ‘(CONFIG\_BPF\_KPROBE\_OVERRIDE|CONFIG\_FUNCTION\_ERROR\_INJECTION)=’ /boot/config-$(uname -r)
CONFIG\_BPF\_KPROBE\_OVERRIDE=y
CONFIG\_FUNCTION\_ERROR\_INJECTION=y

与stap不同，无法用bpftrace修改devmem\_is\_allowed返回值，按官方文档说法

This feature only works on functions tagged ALLOW\_ERROR\_INJECTION.

1.4.2.1 Inside override

参看

bpf-helpers(7)
https://man7.org/linux/man-pages/man7/bpf-helpers.7.html

底层有个bpf\_override\_return，可以这样用

————————————————————————–
int kprobe\_\_should\_failslab ( void \*ctx )
{
bpf\_override\_return( ctx, -ENOMEM );
return 0;
}
————————————————————————–

对于”kprobe:func”，bpf\_override\_return使得整个函数体被跳过，立即返回指定值。只能用于kprobe，不能用于kretprobe、kfunc、uprobe。

位于某个白名单中的”kprobe:func”才能调用bpf\_override\_return，若不在白名单中，调用bpf\_override\_return时会报错

ioctl(PERF\_EVENT\_IOC\_SET\_BPF): Invalid argument

bpftrace的override()是对bpf\_override\_return的封装。前述白名单对应全局变量
error\_injection\_list

$ grep error\_injection\_list /proc/kallsyms
ffffffffa0075b70 t populate\_error\_injection\_list
ffffffffa0075e00 T within\_error\_injection\_list
ffffffffa0731dd2 t populate\_error\_injection\_list.cold
ffffffffa1ac0c20 d error\_injection\_list

可用crash遍历error\_injection\_list，显示位于白名单范围的内核函数名。

1.4.2.2 connect\_block.bt

练习题，拦截connect系统调用，对pid、comm、ip、mask、port进行过滤，调用override()，达到黑白名单效果，简易应用防火墙。

1.4.3 kprobe:some+off

需要自编译bpftrace，使得”bpftrace –info”看到”bfd: yes”，才能支持”(k|u)probe:some+off”，”bfd: no”不支持。

$ /home/scz/src/bpftrace\_scz/build/src/bpftrace –version
bpftrace v0.16.0-32-gcf34

$ gdb -q -nx –batch -ex ‘x/10i do\_sys\_openat2’ /usr/lib/debug/boot/vmlinux-$(uname -r)
0xffffffff81389920 <do\_sys\_openat2>: call 0xffffffff8108b0a0 <\_\_fentry\_\_>
0xffffffff81389925 <do\_sys\_openat2+5>: push %rbp
0xffffffff81389926 <do\_sys\_openat2+6>: mov %rsp,%rbp
0xffffffff81389929 <do\_sys\_openat2+9>: push %r14
0xffffffff8138992b <do\_sys\_openat2...