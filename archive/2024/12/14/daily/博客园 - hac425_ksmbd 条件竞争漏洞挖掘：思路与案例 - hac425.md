---
title: ksmbd 条件竞争漏洞挖掘：思路与案例 - hac425
url: https://www.cnblogs.com/hac425/p/18535420/ksmbd-condition-competition-vulnerability-mining-thinking-and-case-z9zxjt
source: 博客园 - hac425
date: 2024-12-14
fetch_date: 2025-10-06T19:40:56.310875
---

# ksmbd 条件竞争漏洞挖掘：思路与案例 - hac425

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/hac425/)

# [hac425](https://www.cnblogs.com/hac425)

## 博客迁移自 blog.hac425.top， 部分博文由于新浪图床的限制无法显示图片。pdf 版本：https://gitee.com/hac425/data/tree/master/blog\_pdf

* [首页](https://www.cnblogs.com/hac425/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/hac425)
* 订阅
* [管理](https://i.cnblogs.com/)

# [ksmbd 条件竞争漏洞挖掘：思路与案例](https://www.cnblogs.com/hac425/p/18535420/ksmbd-condition-competition-vulnerability-mining-thinking-and-case-z9zxjt "发布于 2024-12-13 19:04")

# ksmbd 条件竞争漏洞挖掘：思路与案例

[ksmbd 条件竞争漏洞挖掘：思路与案例.drawio](assets/drawio/ksmbd%20%E6%9D%A1%E4%BB%B6%E7%AB%9E%E4%BA%89%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98%EF%BC%9A%E6%80%9D%E8%B7%AF%E4%B8%8E%E6%A1%88%E4%BE%8B.drawio)

　　本文介绍从代码审计的角度分析、挖掘条件竞争、UAF 漏洞思路，并以 ksmbd 为实例介绍审计的过程和几个经典漏洞案例。

　　分析代码版本为：linux-6.5.5

　　相关漏洞在一年前已修复完毕.

## 掌握背景：Linux 内核条件竞争 UAF 常见场景

　　首先我们看一下 Linux 内核下 UAF 漏洞产生的几种常见情况，UAF 的核心原理是 内存被释放了，程序仍让能使用这块内存，导致该现象的常见场景：

* 指针在程序中被拷贝（比如存放到不同的对象中、放到链表中），其中一个指针释放后另一个指针没有被清理
* 程序中并发访问导致内存对象还在使用时被其他线程释放.

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165713428-961877828.png)​

　　对于 Linux 内核/驱动而言，目前最常见的 UAF 是由于条件竞争导致的，即一个线程在使用某块内存时其他线程将其释放了。

　　那么 Linux 内核为什么会有条件竞争问题呢，其根本原因如下：

* Linux 以进程为调度主体，不同的进程可能会同时运行
* 不同的进程实体，通过系统调用进入内核后共用同一个内核里面的资源，比如物理内存、内核堆内存等

> 下图表示一个多核系统上两个进程同时在不同的 CPU 核运行，访问内核中的共享变量，实际上由于调度中断单核情况下也存在并发场景

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165714312-1119905179.png)​

　　并发执行+共享对象 是条件竞争的根因，因此驱动在开发设计时要考虑到并发场景，利用锁、引用计数等机制让资源在并发访问时不出问题.

　　常见的并发场景：

| 并发场景 | 解释 |
| --- | --- |
| 用户进程之间 | 多线程并发系统调用，比如IOCTL、MMAP、READ、WRITE 等 |
| 用户进程与内核线程之间 | 内核线程中访问的共享对象，可能被用户态进程修改、释放 |
| 内核线程之间 | 不同内核线程之间使用共享对象 |

　　以 IOCTL 为例用户态进程通过 SVC 指令进入内核，首先进入 ioctl 系统调用入口，然后在 `vfs_ioctl`​ 里面会调用 f\_op->unlocked\_ioctl 注册的函数指针，进入每个文件/驱动自己实现的回调中。

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165715063-2125155938.png)​

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165715833-27563106.png)​

　　由于多核可以并发 SVC 同时执行系统调用，且从系统调用入口到驱动回调中没有锁保护，所以在各个驱动接口中需要自己实现锁保护并发资源访问。

　　同理以 mmap 回调为例，SVC 进入内核后会进入 vm\_mmap\_pgoff 里面会获取当前进程 mm 对象的写锁，然后才通过 do\_mmap 执行驱动对应的 mmap 回调

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165716574-2049845420.png)​

　　分析系统调用 ---> 驱动回调的调用路径之间锁的使用情况可知：

* 同一个进程的不同线程共享 mm 对象（即使 mm 指针一样）所以线程之间无法并发 mmap，但是 mmap 和其他回调比如 ioctl 是可以互相并发的.
* fork 出来的子进程或者通过 IPC 将 fd 共享给其他进程情况下，可以通过多进程并发同时进入驱动的 mmap 回调中.

挖掘条件竞争漏洞，首先就需要通过分析内核代码，清楚了解目标函数执行上下文中是否已经有锁保护，有哪些锁保护，然后以并发执行的视角分析并发场景下的各个代码时序，判断是否存在 UAF。

## 分析目标：梳理目标软件脉络

　　分析 ksmbd 的背景是去年偶然间看到一篇介绍通过 syzkaller fuzz ksmbd 协议的文章：[Tickling ksmbd: fuzzing SMB in the Linux kernel](https://pwning.tech/ksmbd-syzkaller/) ，其核心原理是新增一个伪系统调用 syz\_ksmbd\_send\_req 用来将 syzkaller 生成的数据喂给内核的协议中解析

```
#define KSMBD_BUF_SIZE 16000
static long syz_ksmbd_send_req(volatile long a0, volatile long a1, volatile long a2, volatile long a3)
{
	int sockfd;
	int packet_reqlen;
	int errno;
	struct sockaddr_in serv_addr;
	char packet_req[KSMBD_BUF_SIZE]; // max frame size

	debug("[*]{syz_ksmbd_send_req} entered ksmbd send...\n");
	sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

	memset(&serv_addr, '\0', sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	serv_addr.sin_port = htons(445);
	errno = connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));

	// prepend kcov handle to packet
	packet_reqlen = a1 + 8 > KSMBD_BUF_SIZE ? KSMBD_BUF_SIZE - 8 : a1;
	*(unsigned long*)packet_req = procid + 1;
	memcpy(packet_req + 8, (char*)a0, packet_reqlen);

	if (write(sockfd, (char*)packet_req, packet_reqlen + 8) < 0)
		return -4;

	if (read(sockfd, (char*)a2, a3) < 0)
		return -5;

	if (close(sockfd) < 0)
		return -6;

	debug("[+]{syz_ksmbd_send_req} successfully returned\n");
	return 0;
}
```

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165717417-797988402.png)​

　　通过分析这篇文章可以得到一些信息：

* 定位 ksmbd 处理数据包的入口，即 ksmbd\_conn\_handler\_loop
* 还存在一些简单的内存越界漏洞，代表可能还会存在一些较复杂、或者隐藏较深的漏洞

　　基于这些信息开始对 ksmbd 的源码进行分析，分析思路：

* 从入口出追踪客户端发送的网络数据流，梳理出请求处理过程中的数据流过程、校验逻辑.
* 分析数据解析过程，尝试挖掘内存越界、溢出等漏洞
* 分析请求处理时的一些上下文约束，比如是否可并发、是否有锁，对象生命周期管理，尝试挖掘条件竞争、UAF漏洞

　　从 ksmbd\_conn\_handler\_loop 往上追踪，这是在 ksmbd\_tcp\_new\_connection 创建的内核线程回调函数

```
static int ksmbd_tcp_new_connection(struct socket *client_sk)
{
	t = alloc_transport(client_sk);
	csin = KSMBD_TCP_PEER_SOCKADDR(KSMBD_TRANS(t)->conn);
	KSMBD_TRANS(t)->handler = kthread_run(ksmbd_conn_handler_loop,
					      KSMBD_TRANS(t)->conn,
					      "ksmbd:%u",
					      ksmbd_tcp_get_port(csin));
```

　　其调用路径：

* kthread = kthread\_run(ksmbd\_kthread\_fn, (void \*)iface, "ksmbd-%s",ksmbd\_kthread\_fn

  1. kernel\_accept(iface->ksmbd\_socket, &client\_sk,
  2. ksmbd\_tcp\_new\_connection(client\_sk);

　　因此可以知道每当有一个客户端连接 445 端口时，ksmbd\_kthread\_fn 就会通过 ksmbd\_tcp\_new\_connection 创建一个内核线程，然后 ksmbd\_conn\_handler\_loop 里面处理每个 socket 请求的业务.

　　在 ksmbd\_tcp\_new\_connection --> alloc\_transport 会为每一个连接创建两个关键的对象（`ksmbd_transport`​ 和 `ksmbd_conn`​），用于管理 tcp 连接下的各种协议状态

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241108165718276-1715935146.png)​

　　两个对象互相保存对方的指针，方便从一个对象中拿到另一个对象进行操作，对象的大概作用：

* ksmbd\_transport：负责链路数据的收发，比如从网络连接中读取数据
* ksmbd\_conn：管理整个 smb 连接的状态，比如登录、文件操作，会话密钥等，每个 TCP 连接对应一个 conn 对象

　　其中 ksmbd\_conn 是非常核心的对象，在 SMB 请求处理的各个环节都能看到， ksmbd\_conn\_handler\_loop 的大概处理流程如下

* ksmbd\_conn\_handler\_loop --> 每个连接都会创建一个内核线程执行该函数

  + while (ksmbd\_conn\_alive(conn))

    1. char hdr\_buf[4] = {0,};
    2. size = t->ops->read(t, hdr\_buf, sizeof(hdr\_buf), -1);
    3. pdu\_size = get\_rfc1002\_len(hdr\_buf);

       - return be32\_to\_cpu(\*((\_\_be32 \*)buf)) & 0xffffff;
    4. conn->request\_buf = kvmalloc(size, GFP\_KERNEL);
    5. memcpy(conn->request\_buf, hdr\_buf, sizeof(hdr\_buf)); // 设置 rfc1002\_len 到新的 req\_buf
    6. size = t->ops->read(t, conn->request\_buf + 4, pdu\_size, 2);
    7. default\_conn\_ops.process\_fn --> ksmbd\_server\_process\_request --> queue\_ksmbd\_work

       1. work = ksmbd\_alloc\_work\_struct(); // conn 的每个请求都启动一个 work 处理？
       2. work->request\_buf = conn->request\_buf;
       3. INIT\_WORK(&work->work, handle\_ksmbd\_work);
       4. ksmbd\_queue\_work(work); // 调度 work 执行

          - queue\_work(ksmbd\_wq, &work->work);

　　conn 下每收到一个请求都会新建一个 work，然后把 work 放到 ksmbd\_wq， workqueue 会动态分配到不同 worker 执行。这边在介绍一下内核的 workqueue 机制，workqueue 和 work 的关系如下：

​![image](https://img2023.cnblogs.com/blog/1454902/202411/145...