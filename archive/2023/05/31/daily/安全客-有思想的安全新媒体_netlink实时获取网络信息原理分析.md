---
title: netlink实时获取网络信息原理分析
url: https://www.anquanke.com/post/id/288932
source: 安全客-有思想的安全新媒体
date: 2023-05-31
fetch_date: 2025-10-04T11:37:54.382846
---

# netlink实时获取网络信息原理分析

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# netlink实时获取网络信息原理分析

阅读量**350664**

发布时间 : 2023-05-30 15:45:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

最近在做主机侧网络连接相关的调研，发现通过 linux 自带的`netlink`能实时获取网络连接五元组信息，可以用于网络活动可视化、异常连接检测、安全策略优化以及审计等功能，但网络上找到的相关文章不多，因此在此分析下`netlink`实时获取网络连接信息的原理。

# netlink 是什么

`netlink`是什么？官方文档是这样描述的：

> Netlink is used to transfer information between the kernel and user-space processes. It consists of a standard sockets-based interface for user space processes and an internal kernel API for kernel modules.
> Netlink用于在内核和用户空间进程之间传输信息。它由一个面向用户空间进程的标准套接字接口和一个面向内核模块的内部内核API组成。
> <https://man7.org/linux/man-pages/man7/netlink.7.html>

简单来讲`netlink`实现了一套用户态和内核态通信的机制，通过`netlink`能和很多内核模块通信，例如`ss`命令通过 netlink 更快的获取网络信息、hids通过`netlink`获取进程创建信息、`iptables`通过`netlink`配置网络规则等。

关于如何使用`netlink`官方提供了如下使用样例：

```
...
fd = socket(AF_NETLINK, SOCK_RAW, protocol);
bind(fd, (struct sockaddr *) &sa, sizeof(sa));
...
sendmsg(fd, &msg, 0);
...
len = recvmsg(fd, &msg, 0);
...
```

`socket()`的参数`protocol`指定了创建的套接字对应的`netlink`协议，不同的协议可以和不同的内核模块通信，`netlink`支持的协议可以在`include/linux/netlink.h`文件中看到：

```
// include/linux/netlink.h
#define NETLINK_INET_DIAG    4    /* INET socket monitoring*/
#define NETLINK_AUDIT        9    /* auditing */
#define NETLINK_CONNECTOR    11
#define NETLINK_NETFILTER    12    /* netfilter subsystem */
```

这里列举了几个安全常用的协议，通过`NETLINK_INET_DIAG`可以获取网络连接数据，通过`NETLINK_AUDIT`可以获取内核`auditd`数据，通过`NETLINK_CONNECTOR`可以获取进程创建数据。而`NETLINK_NETFILTER`正是本文后续要介绍的能实时获取网络连接信息的协议。

# netlink 初始化

为什么`socket()`指定`AF_NETLINK`之后就能和`netlink`通信了? 需要结合`netlink`的初始化过程来看。

```
// net/netlink/af_netlink.c
core_initcall(netlink_proto_init);
```

`core_initcall`将`netlink_proto_init`注册为一个核心初始化函数，并在内核启动时自动调用，也就是说`netlink`内核模块是默认开启的。我们再来看看`netlink_proto_init`做了什么：

```
// net/netlink/af_netlink.c
static int __init netlink_proto_init(void)
{
    ...
    nl_table = kcalloc(MAX_LINKS, sizeof(*nl_table), GFP_KERNEL);
    ...
    sock_register(&netlink_family_ops);
}

struct netlink_table {
    struct nl_pid_hash hash; // 存储sk_node 单播时会用
    struct hlist_head mc_list; // 存储sk_bind_node 广播时会用
    unsigned long *listeners; // 记录当前加入广播组的客户端
    unsigned int nl_nonroot;
    unsigned int groups; // 广播上限
    struct mutex *cb_mutex;
    struct module *module;
    int registered; // 当前netlink协议是否注册
};
static struct netlink_table *nl_table;
```

`netlink_proto_init`过程需要关注两点：`nl_table`和`sock_register`：`nl_table`记录了`netlink`协议的配置和状态，我们后续讲到注册`netlink`时会再用到`nl_table`；`sock_register`则是将`netlink_family_ops`加入`net_families`中：

```
// net/netlink/af_netlink.c
static struct net_proto_family netlink_family_ops = {
    .family = PF_NETLINK,
    .create = netlink_create,
    .owner    = THIS_MODULE,    /* for consistency 8) */
};

// net/socket.c
int sock_register(const struct net_proto_family *ops)
{
    ...
    net_families[ops->family] = ops;
    ...
}

static const struct net_proto_family *net_families[NPROTO] __read_mostly;
struct net_proto_family {
    int        family;
    int        (*create)(struct net *net, struct socket *sock, int protocol);
    struct module    *owner;
};
```

`net_families`是`net_proto_family`类型的数据，此时`net_families[PF_NETLINK]->create == netlink_create`，到此也就完成了模块初始化过程。

系统调用`socket`时会调用`net_families`中的`netlink_create`：

```
// net/socket.c
SYSCALL_DEFINE3(socket, int, family, int, type, int, protocol)
{
    ...
    retval = sock_create(family, type, protocol, &sock);
    ...
}

int sock_create(int family, int type, int protocol, struct socket **res)
{
    return __sock_create(current->nsproxy->net_ns, family, type, protocol, res, 0);
}

static int __sock_create(struct net *net, ...)
{
    ...
    pf = rcu_dereference(net_families[family]);
    err = pf->create(net, sock, protocol);
    ...
}
```

可以看到系统调用`socket`最终会调用`net_families[family]->create`，而官方样例中我们是这样`fd = socket(AF_NETLINK, SOCK_RAW, netlink_family)`创建 `netlink socket`的，`include/linux/socket.h`文件中定义`#define PF_NETLINK AF_NETLINK`，因此`net_families[family]->create`调用的正是`netlink_create`！我们再来看看`netlink_create`做了什么：

```
// net/netlink/af_netlink.c
static int netlink_create(struct net *net, struct socket *sock, int protocol)
{
    ...
    err = __netlink_create(net, sock, cb_mutex, protocol);
    ...
}

static int __netlink_create(struct net *net, ...)
{
    ...
    sock->ops = &netlink_ops;
    // 将sk与netlink_proto结构体关联
    sk = sk_alloc(net, PF_NETLINK, GFP_KERNEL, &netlink_proto);
    ...
}

// net/netlink/af_netlink.c
// netlink_socket 对应的 ops 函数
static const struct proto_ops netlink_ops = {
    ...
    .bind =        netlink_bind,
    .setsockopt =    netlink_setsockopt,
    .sendmsg =    netlink_sendmsg,
    .recvmsg =    netlink_recvmsg,
    ...
};
// netlink类型socket的sock结构体
struct netlink_sock {
    struct sock        sk;
    u32            pid;
    u32            dst_pid;
    u32            dst_group;
    u32            flags;
    u32            subscriptions;
    u32            ngroups;
    unsigned long        *groups;
    unsigned long        state;
    wait_queue_head_t    wait;
    struct netlink_callback    *cb;
    struct mutex        *cb_mutex;
    struct mutex        cb_def_mutex;
    void            (*netlink_rcv)(struct sk_buff *skb);
    struct module        *module;
};
```

可以看到`netlink_create`进行了`sock->ops = &netlink_ops`赋值操作，也就是说我们可以通过`socket(AF_NETLINK, SOCK_RAW, netlink_family)`获得一个`socket`,此时该`socket`对应的`bind sendmsg recvmsg`等函数都被替换成了`netlink`协议的对应函数。同时创建了`socket->sk`与`netlink_sock`结构体关联，`netlink_sock`中会存放`netlink`通信过程中需要的`dst_pid、dst_group`等数据。
![]()

# NETLINK\_NETFILTER 初始化

各个内核模块注册`netlink`协议的流程基本相同，本节以后续要分析的`NETLINK_NETFILTER`协议为例分析一下注册`netlink`协议的流程：

```
// net/netfilter/nfnetlink.c
static int __init nfnetlink_init(void)
{
    ...
    nfnl = netlink_kernel_create(&init_net, NETLINK_NETFILTER, NFNLGRP_MAX,
                     nfnetlink_rcv, NULL, THIS_MODULE);
    ...
}

module_init(nfnetlink_init);
```

可以看到`netfilter`并不是默认开启的内核模块，当该模块被加载时会调用`netlink_kernel_create`

```
// net/netfilter/nfnetlink.c
struct sock *
netlink_kernel_create(struct net *net, int unit, unsigned int groups,
              void (*input)(struct sk_buff *skb),...)
{
    ...
    struct socket *sock;
    struct sock *sk;
    unsigned long *listeners = NULL;
    // 为内核模块创建socket
    sock_create_lite(PF_NETLINK, SOCK_DGRAM, unit, &sock)
    __netlink_create(&init_net, sock, cb_mutex, unit)
    sk = sock->sk;
    listeners = kzalloc(NLGRPSZ(groups) + sizeof(struct listeners_rcu_head),
                GFP_KERNEL);
    // 设置回调函数 netlink_rcv 为 nfnetlink_rcv
    if (input)
        nlk_sk(sk)->netlink_rcv = input;
    // 更新协议状态
    nl_table[unit].groups = groups;
    nl_table[unit].listeners = listeners;
    nl_table[unit].cb_mutex = cb_mutex;
    nl_table[unit].module = module;
    nl_table[unit].registered = 1;
    ...
}
```

`netlink_kernel_create`返回给`netfilter`内核模块一个`socket`，并切设置了该`socket`的`netlink_rcv`函数为`nfnetlink_rcv`，最后还更新了`nl_table`设置`NETLINK_NETFILTER`协议为激活状态。

![]()

# 发送接收netlink消息

用户态可以通过`send`向内核态发送`netlink`消息，通过分析这个过程我们可以看到`nfnetlink_rcv`和`nl_table`的作用：

```
// net/socket.c
SYSCALL_DEFINE4(send, int, fd, ...)
{
    return sys_sendto(fd, buff, len, flags, NULL, 0);
}

SYSCALL_DEFINE6(sendto, int, fd,...)
{
    ...
    err = sock_sendmsg(sock, &msg, len);
    ...
}

int sock_sendmsg(struct socket *sock, struct msghdr *msg, size_t size)
{
    ...
    ret = __sock_sendmsg(&iocb, sock, msg, size);
    ...
}

static inline int __sock_sendmsg(struct kiocb *iocb,...)
{
    ...
    return sock->ops->sendmsg(iocb, sock, msg, size);
}
```

`send`最终调用的是`sock->ops->sendmsg`也就是`netlink_sendmsg`

```
// net/netlink/af_netlink.c
static int netlink_sendmsg(struct kiocb *kiocb,...)
{
    ...
    NETLINK_CB(skb).dst_g...