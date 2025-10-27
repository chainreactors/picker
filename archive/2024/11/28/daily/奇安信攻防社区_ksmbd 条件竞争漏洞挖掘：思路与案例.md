---
title: ksmbd 条件竞争漏洞挖掘：思路与案例
url: https://forum.butian.net/share/3900
source: 奇安信攻防社区
date: 2024-11-28
fetch_date: 2025-10-06T19:15:37.493487
---

# ksmbd 条件竞争漏洞挖掘：思路与案例

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### ksmbd 条件竞争漏洞挖掘：思路与案例

ksmbd 条件竞争漏洞挖掘：思路与案例
本文介绍从代码审计的角度分析、挖掘条件竞争、UAF 漏洞思路，并以 ksmbd 为实例介绍审计的过程和几个经典漏洞案例。
分析代码版本为：linux-6.5.5
相关漏...

ksmbd 条件竞争漏洞挖掘：思路与案例
====================
本文介绍从代码审计的角度分析、挖掘条件竞争、UAF 漏洞思路，并以 ksmbd 为实例介绍审计的过程和几个经典漏洞案例。
分析代码版本为：linux-6.5.5
相关漏洞在一年前已修复完毕.
掌握背景：Linux 内核条件竞争 UAF 常见场景
--------------------------
首先我们看一下 Linux 内核下 UAF 漏洞产生的几种常见情况，UAF 的核心原理是 内存被释放了，程序仍让能使用这块内存，导致该现象的常见场景：
- 指针在程序中被拷贝（比如存放到不同的对象中、放到链表中），其中一个指针释放后另一个指针没有被清理
- 程序中并发访问导致内存对象还在使用时被其他线程释放.
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-472d9aa178cee85d297dcbf60975cb5f38225ad1.png)
对于 Linux 内核/驱动而言，目前最常见的 UAF 是由于条件竞争导致的，即一个线程在使用某块内存时其他线程将其释放了。
那么 Linux 内核为什么会有条件竞争问题呢，其根本原因如下：
- Linux 以进程为调度主体，不同的进程可能会同时运行
- 不同的进程实体，通过系统调用进入内核后共用同一个内核里面的资源，比如物理内存、内核堆内存等
> 下图表示一个多核系统上两个进程同时在不同的 CPU 核运行，访问内核中的共享变量，实际上由于调度中断单核情况下也存在并发场景
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ecedc385694e34e1683cc79ccafd67df660545e1.png)
并发执行+共享对象 是条件竞争的根因，因此驱动在开发设计时要考虑到并发场景，利用锁、引用计数等机制让资源在并发访问时不出问题.
常见的并发场景：
| 并发场景 | 解释 |
|---|---|
| 用户进程之间 | 多线程并发系统调用，比如IOCTL、MMAP、READ、WRITE 等 |
| 用户进程与内核线程之间 | 内核线程中访问的共享对象，可能被用户态进程修改、释放 |
| 内核线程之间 | 不同内核线程之间使用共享对象 |
以 IOCTL 为例用户态进程通过 SVC 指令进入内核，首先进入 ioctl 系统调用入口，然后在 `vfs\_ioctl`​ 里面会调用 f\\_op-&gt;unlocked\\_ioctl 注册的函数指针，进入每个文件/驱动自己实现的回调中。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bfb91390a4eef34783ec516b230b8cd348957134.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2430168137443cfe2ecdd563cb23e77d8776e5ea.png)
由于多核可以并发 SVC 同时执行系统调用，且从系统调用入口到驱动回调中没有锁保护，所以在各个驱动接口中需要\*\*自己实现锁保护并发资源访问\*\*。
同理以 mmap 回调为例，SVC 进入内核后会进入 vm\\_mmap\\_pgoff 里面会获取当前进程 mm 对象的写锁，然后才通过 do\\_mmap 执行驱动对应的 mmap 回调
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bd6a1e40e7ba2004789c4eee7556369b23bd7b10.png)
分析系统调用 ---&gt; 驱动回调的调用路径之间锁的使用情况可知：
- 同一个进程的不同线程共享 mm 对象（即使 mm 指针一样）所以线程之间无法并发 mmap，但是 mmap 和其他回调比如 ioctl 是可以互相并发的.
- fork 出来的子进程或者通过 IPC 将 fd 共享给其他进程情况下，可以通过多进程并发同时进入驱动的 mmap 回调中.
\*\*挖掘条件竞争漏洞，首先就需要通过分析内核代码，清楚了解目标函数执行上下文中是否已经有锁保护，有哪些锁保护，然后以并发执行的视角分析并发场景下的各个代码时序，判断是否存在 UAF。\*\*
分析目标：梳理目标软件脉络
-------------
分析 ksmbd 的背景是去年偶然间看到一篇介绍通过 syzkaller fuzz ksmbd 协议的文章：[Tickling ksmbd: fuzzing SMB in the Linux kernel](https://pwning.tech/ksmbd-syzkaller/) ，其核心原理是新增一个伪系统调用 syz\\_ksmbd\\_send\\_req 用来将 syzkaller 生成的数据喂给内核的协议中解析
```c
#define KSMBD\_BUF\_SIZE 16000
static long syz\_ksmbd\_send\_req(volatile long a0, volatile long a1, volatile long a2, volatile long a3)
{
int sockfd;
int packet\_reqlen;
int errno;
struct sockaddr\_in serv\_addr;
char packet\_req[KSMBD\_BUF\_SIZE]; // max frame size
debug("[\*]{syz\_ksmbd\_send\_req} entered ksmbd send...\n");
sockfd = socket(AF\_INET, SOCK\_STREAM, IPPROTO\_TCP);
memset(&serv\_addr, '\0', sizeof(serv\_addr));
serv\_addr.sin\_family = AF\_INET;
serv\_addr.sin\_addr.s\_addr = inet\_addr("127.0.0.1");
serv\_addr.sin\_port = htons(445);
errno = connect(sockfd, (struct sockaddr\*)&serv\_addr, sizeof(serv\_addr));
// prepend kcov handle to packet
packet\_reqlen = a1 + 8 > KSMBD\_BUF\_SIZE ? KSMBD\_BUF\_SIZE - 8 : a1;
\*(unsigned long\*)packet\_req = procid + 1;
memcpy(packet\_req + 8, (char\*)a0, packet\_reqlen);
if (write(sockfd, (char\*)packet\_req, packet\_reqlen + 8) < 0)
return -4;
if (read(sockfd, (char\*)a2, a3) < 0)
return -5;
if (close(sockfd) < 0)
return -6;
debug("[+]{syz\_ksmbd\_send\_req} successfully returned\n");
return 0;
}
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-186a7af7f4ae8a53ebbd2acee2c61ee238515196.png)
通过分析这篇文章可以得到一些信息：
- 定位 ksmbd 处理数据包的入口，即 ksmbd\\_conn\\_handler\\_loop
- 还存在一些简单的内存越界漏洞，代表可能还会存在一些较复杂、或者隐藏较深的漏洞
基于这些信息开始对 ksmbd 的源码进行分析，分析思路：
- 从入口出追踪客户端发送的网络数据流，梳理出请求处理过程中的数据流过程、校验逻辑.
- 分析数据解析过程，尝试挖掘内存越界、溢出等漏洞
- 分析请求处理时的一些上下文约束，比如是否可并发、是否有锁，对象生命周期管理，尝试挖掘条件竞争、UAF漏洞
从 ksmbd\\_conn\\_handler\\_loop 往上追踪，这是在 ksmbd\\_tcp\\_new\\_connection 创建的内核线程回调函数
```c
static int ksmbd\_tcp\_new\_connection(struct socket \*client\_sk)
{
t = alloc\_transport(client\_sk);
csin = KSMBD\_TCP\_PEER\_SOCKADDR(KSMBD\_TRANS(t)->conn);
KSMBD\_TRANS(t)->handler = kthread\_run(ksmbd\_conn\_handler\_loop,
KSMBD\_TRANS(t)->conn,
"ksmbd:%u",
ksmbd\_tcp\_get\_port(csin));
```
其调用路径：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c6f3ec9332c0c88e18f88ace7699f96f39b0af8c.png)
因此可以知道每当有一个客户端连接 445 端口时，ksmbd\\_kthread\\_fn 就会通过 ksmbd\\_tcp\\_new\\_connection 创建一个内核线程，然后 ksmbd\\_conn\\_handler\\_loop 里面处理每个 socket 请求的业务.
在 ksmbd\\_tcp\\_new\\_connection --&gt; alloc\\_transport 会为每一个连接创建两个关键的对象（`ksmbd\_transport`​ 和 `ksmbd\_conn`​），用于管理 tcp 连接下的各种协议状态
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7a7e8baeea186750b06a6e3bba753fdf30c55019.png)
两个对象互相保存对方的指针，方便从一个对象中拿到另一个对象进行操作，对象的大概作用：
- ksmbd\\_transport：负责链路数据的收发，比如从网络连接中读取数据
- ksmbd\\_conn：管理整个 smb 连接的状态，比如登录、文件操作，会话密钥等，\*\*每个 TCP 连接对应一个 conn 对象\*\*
其中 ksmbd\\_conn 是非常核心的对象，在 SMB 请求处理的各个环节都能看到， ksmbd\\_conn\\_handler\\_loop 的大概处理流程如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e0aa71608b9322c0702f7dfc71b009812dac7c5d.png)
conn 下每收到一个请求都会新建一个 work，然后把 work 放到 ksmbd\\_wq， workqueue 会动态分配到不同 worker 执行。这边在介绍一下内核的 workqueue 机制，workqueue 和 work 的关系如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b87cc2ada19c4a6d5cb37b6df90c802458eefca2.png)
核心概念是：work 先注册到 workqueue ，然后具体由 worker 执行，在代码中每个 worker 对应一个 work\\_thread 内核线程，\*\*一个 workqueue 里面会存在多个 worker，这些 worker 之间并发执行\*\*.
因此\*\*同一时刻可能会有 handle\\_ksmbd\\_work 实例访问同一个 conn 对象，这样就有了 RACE 的可能\*\*.
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fb41f22d73f9c908bdd2b334b79809ea2c081151.png)
继续分析 handle\\_ksmbd\\_work 的大体逻辑：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2e8fb58dbc698aae3b9905a1effb925a242545af.png)
handle\\_ksmbd\\_work 主要逻辑就是解析 work-&gt;request\\_buf 中的网络报文数据，根据里面的请求类型、参数调用对应的请求处理函数进行处理（`conn->cmds`​），同时可以看到 cmds-&gt;proc 执行时上\*\*下文是没有锁的\*\*，因此如果 cmd 里面如果有访问到共享变量就需要\*\*自行加锁避免并发\*\*.
cmds 中可用的回调函数如下
```c
static struct smb\_version\_cmds smb2\_0\_server\_cmds[NUMBER\_OF\_SMB2\_COMMANDS] = {
[SMB2\_NEGOTIATE\_HE] = { .proc = smb2\_negotiate\_request, },
[SMB2\_SESSION\_SETUP\_HE] = { .proc = smb2\_sess\_setup, },
[SMB2\_TREE\_CONNECT\_HE] = { .proc = smb2\_tree\_connect,},
[SMB2\_TREE\_DISCONNECT\_HE] = { .proc = smb2\_tree\_disconnect,},
[SMB2\_LOGOFF\_HE] = { .proc = smb2\_session\_logoff,},
[SMB2\_CREATE\_HE] = { .proc = smb2\_open},
[SMB2\_QUERY\_INFO\_HE] = { .proc = smb2\_query\_info},
[SMB2\_QUERY\_DIRECTORY\_HE] = { .proc = smb2\_query\_dir},
[SMB2\_CLOSE\_HE] = { .proc = smb2\_close},
[SMB2\_ECHO\_HE] = { .proc = smb2\_echo},
[SMB2\_SET\_INFO\_HE] = { .proc = smb2\_set\_info},
[SMB2\_READ\_HE] = { .proc = smb2\_read},
[SMB2\_WRITE\_HE] = { .proc = smb2\_write},
[SMB2\_FLUSH\_HE] = { .proc = smb2\_flush},
[SMB2\_CANCEL\_HE] = { .proc = smb2\_cancel},
[SMB2\_LOCK\_HE] = { .proc = smb2\_lock},
[SMB2\_IOCTL\_HE] = { .proc = smb2\_ioctl},
[SMB2\_OPLOCK\_BREAK\_HE] = { .proc = smb2\_oplock\_break},
[SMB2\_CHANGE\_NOTIFY\_HE] = { .proc = smb2\_notify},
};
```
这些回调函数就会根据请求和 conn 对象实现 smb 协议的业务逻辑，之后就可以对这些回调函数进行审计，这里再次回顾一下这些回调函数执行的上下文状态：
- 回调函数会在不同的 worker 线程中被调用，存在并发性
- 同一个连接的不同请求可能并发处理，处理时会访问同一个 conn 对象
经过...