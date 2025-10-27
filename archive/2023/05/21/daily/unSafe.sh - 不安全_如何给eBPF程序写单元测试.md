---
title: 如何给eBPF程序写单元测试
url: https://buaq.net/go-164734.html
source: unSafe.sh - 不安全
date: 2023-05-21
fetch_date: 2025-10-04T11:36:58.310152
---

# 如何给eBPF程序写单元测试

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

![](https://8aqnet.cdn.bcebos.com/33ef4b1b0b1d033fae214d8cdf005d32.jpg)

如何给eBPF程序写单元测试

前言eBPF程序还很年轻，周边质量建设体系还刚起步，常用于Linux内核上的监控跟踪，本身比较底层，测试成本很高。对于常写eBPF的同学，特别头疼的是快速迭代的项目，如何保证功能正常。如何给eBPF
*2023-5-20 20:0:40
Author: [www.cnxct.com(查看原文)](/jump-164734.htm)
阅读量:27
收藏*

---

## 前言

eBPF程序还很年轻，周边质量建设体系还刚起步，常用于Linux内核上的监控跟踪，本身比较底层，测试成本很高。对于常写eBPF的同学，特别头疼的是快速迭代的项目，如何保证功能正常。如何给eBPF程序写单元测试呢？译者看到一篇文章，分享给大家。本文使用openAI翻译，如有错误，请看原文：[Unit Testing eBPF Programs](https://who.ldelossa.is/posts/unit-testing-ebpf/ "Unit Testing eBPF Programs")

当然，原文在 **[Hacker News](https://news.ycombinator.com/item?id=35989911 " Hacker News")**上也被热烈讨论，[大佬Daniel](https://github.com/danobi/ "大佬Daniel")给出自己的看法，文章质量也很高，推荐看看。

> BPF\_PROG\_RUN很棒，但不幸的是它依赖于正在运行的内核版本。为此，我编写了`vmtest`（[https://dxuuu.xyz/vmtest.html），它专门用于BPF\_PROG\_RUN的使用场景](https://dxuuu.xyz/vmtest.html%EF%BC%89%EF%BC%8C%E5%AE%83%E4%B8%93%E9%97%A8%E7%94%A8%E4%BA%8EBPF_PROG_RUN%E7%9A%84%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF)。

## eBPF的单元测试

无论你喜欢与否，编写单元测试几乎已经成为你的代码的必需品。在进行更改时，它们为你提供了一个安全网，并在更改后全部通过时给你一种愉悦、温暖的感觉。

在处理内核补丁时，我不得不研究为 eBPF 程序编写单元测试。事实证明，内核开发人员已经考虑到这一点，并已存在基础设施来实现它。

我将提供一个实际的例子，演示如何对一个 `TC eBPF` 程序进行单元测试。在这个测试中，我们希望确认查找一个发送到外部 IP 地址的数据包的路由是否会选择默认网关。我们将完全控制测试所运行的网络命名空间。如果你对这其中的任何概念一无所知，别担心，我将介绍的概念同样适用于测试其他类型的 eBPF 程序。

## 测试环境

在本文中，我假设你知道如何使用`clang`、`bpftool`编译你的eBPF程序，并且知道如何生成一个`vmlinux.h`文件。

话虽如此，我们确实需要在你的编程环境中进行一些基础设置，并安装我们需要的工具。

你必须拥有：

1. bpftool – 除了生成vmlinux.h文件之外，还将用于为你编译的eBPF程序生成一个"骨架"加载器。
2. clang – 我们需要它来编译eBPF程序。
3. make – 用于运行我的修改过的Makefile。

此外，你的机器上必须具有`CAP_SYS_ADMIN`特权，如果你不知道是什么意思，99%的情况下以root身份运行将满足此要求。

我还假设你使用的是Linux系统，你可能会认为这是一个多此一举的说法，但[Windows eBPF](https://github.com/microsoft/ebpf-for-windows "Windows eBPF")在快速迭代。

好了，最后一个假设，你已经正确安装了`libbpf`，并且`clang/gcc`能够找到它并编译你的eBPF程序。

## 介绍BPF\_PROG\_RUN命令

我们想要重点关注用于单元测试eBPF程序的核心功能，这个功能就是一个名为`BPF_PROG_RUN`的eBPF命令。

这个命令从`BPF_PROG_TEST_RUN`改名而来，这个标识符可能是可以互换使用的。`命令`是一个枚举值，可以传递给Linux暴露的bpf系统调用。然而，libbpf通常会为了方便和健壮性而封装bpf系统调用的使用。

因此，我们将重点关注使用libbpf封装的`BPF_PROG_RUN`命令，即`bpf_test_run_opts`。

让我们来看一下它的[前向声明](https://elixir.bootlin.com/linux/v6.2.11/source/tools/lib/bpf/bpf.h#L454 "前向声明")：

```
struct bpf_test_run_opts {
    size_t sz; /* size of this struct for forward/backward compatibility */
    const void *data_in; /* optional */
    void *data_out;      /* optional */
    __u32 data_size_in;
    __u32 data_size_out; /* in: max length of data_out
                  * out: length of data_out
                  */
    const void *ctx_in; /* optional */
    void *ctx_out;      /* optional */
    __u32 ctx_size_in;
    __u32 ctx_size_out; /* in: max length of ctx_out
                 * out: length of cxt_out
                 */
    __u32 retval;        /* out: return code of the BPF program */
    int repeat;
    __u32 duration;      /* out: average per repetition in ns */
    __u32 flags;
    __u32 cpu;
    __u32 batch_size;
};
#define bpf_test_run_opts__last_field batch_size

LIBBPF_API int bpf_prog_test_run_opts(int prog_fd,
                      struct bpf_test_run_opts *opts);
```

如果我们来看实现，我们会发现`bpf_prog_test_run_opts`简单地将提供的opts复制到一个内核将拥有的结构体中，对opts结构体进行一些合理性检查，然后直接调用bpf系统调用。

libbpf函数的参数接受一个eBPF程序文件描述符和一个opts结构体。

eBPF程序文件描述符表示加载到内核中的eBPF程序，我们将在本文后面演示一种方便获取此文件描述符的方法。

opts结构体既提供模拟数据，也提供函数的选项。虽然某些字段标注为**可选**，但我们将了解到这实际上取决于你正在测试的eBPF程序类型，这些字段到底是可选还是必需的。

在本文中，我们将使用以下重要字段：

`sz`始终是必需的，它只需设置为`sizeof(bpf_test_run_opts)`。

`data_in`、`data_size_in`允许您向传递给eBPF程序的ctx提供模拟数据，对于**TC程序**而言，就是模拟的IPv4数据包。

`ctx_in`、`ctx_size_in`允许您传入一个模拟的ctx，对于**TC程序**而言，就是模拟的`__sk_buff`结构，它是eBPF对内核套接字缓冲区的表示。

## 测试用例和Skeleton加载器

现在介绍了`bpf_test_run_opts`，让我们开始编写我们的eBPF测试用例。

我们还将使用bpftool生成一个Skeleton加载器，它是一个带有函数的头文件，用于将我们编译的eBPF程序加载到内核，并为我们提供一个对已加载程序的句柄。

该句柄可用于获取加载的eBPF程序的文件描述符，并在内核运行时与其交互。我们的测试用例的目标是确保源自主机、目标为外部节点的数据包选择默认路由，并转发到正确的接口。

为了测试这一点，我们将利用eBPF辅助函数`bpf_fib_lookup`。我们不需要详细了解这个辅助函数的工作原理，简单来说，我们提供一个传入数据包的源地址和目的地址，它将返回一个接口（如果有的话），该数据包将被转发到该接口。

在我们的测试用例中，我们希望上述接口是网络命名空间的默认网关。我们的测试数据包的源地址将为`127.0.0.1`，目的地址将为`8.8.8.8`。

由于我们运行的是单元测试，实际上不会发送任何数据，并且主机之外不会产生任何副作用。请记住，这个测试有点人为，主要是为了展示测试基础设施的一些特点，我们更倾向于**演示**而不是**实用**。

好的，让我们来看看我们的测试eBPF程序：

```
// fib_lookup.bpf.c

#include "../vmlinux.h"
#include <bpf/bpf_helpers.h>

#define TC_ACT_OK       0
#define TC_ACT_SHOT     2
#define TC_ACT_REDIRECT     7

#define AF_INET             2   /* Internet IP Protocol     */

struct bpf_fib_lookup fib_params = {0};

int fib_lookup_ret = 0;

SEC("tc")
int fib_lookup(struct __sk_buff *skb)
{
        struct iphdr *ip = 0;

        bpf_printk("performing FIB lookup\n");

        bpf_printk("fib lookup original ret: %d\n", fib_lookup_ret);

        fib_lookup_ret = bpf_fib_lookup(skb, &fib_params, sizeof(fib_params),
                    0);

        bpf_printk("fib lookup ret: %d\n", fib_lookup_ret);

    return TC_ACT_OK;
}

char _license[] SEC("license") = "GPL";
```

如您所见，测试非常简单。我们导入必要的头文件，然后定义两个全局变量，并将它们都设置为零。

通过将这些变量定义为全局变量并将其设置为零，实际上使其通过我们的骨架在用户空间中可用。让我们使用以下Makefile来编译并生成此eBPF程序的骨架。

```
# makefile
CFLAGS += -g3 \
          -Wall

LIBS = bpf

all: fib_lookup.bpf.o fib_lookup.skel.h

fib_lookup.bpf.o: fib_lookup.bpf.c
    clang -target bpf -Wall -O2 -g -c $<

fib_lookup.skel.h: fib_lookup.bpf.o
    bpftool gen skeleton $< > [email protected]

test: test.c
    gcc $(CFLAGS) -l$(LIBS) -o [email protected] $<

.PHONY:
clean:
    rm -rf fib_lookup.bpf.o
    rm -rf fib_lookup.skel.h
    rm -rf test
```

现在先忽略测试二进制文件，我们将在下一部分编写测试运行器。

如果我们检查文件`fib_lookup.skel.h`，我们会遇到一个有趣的结构。

```
// fib_lookup.skel.h

struct fib_lookup_bpf {
    struct bpf_object_skeleton *skeleton;
    struct bpf_object *obj;
    struct {
        struct bpf_map *bss;
        struct bpf_map *rodata;
    } maps;
    struct {
        struct bpf_program *fib_lookup;
    } progs;
    struct {
        struct bpf_link *fib_lookup;
    } links;
    struct fib_lookup_bpf__bss {
        struct bpf_fib_lookup fib_params;
        int fib_lookup_ret;
    } *bss;
    struct fib_lookup_bpf__rodata {
    } *rodata;

#ifdef __cplusplus
    static inline struct fib_lookup_bpf *open(const struct bpf_object_open_opts *opts = nullptr);
    static inline struct fib_lookup_bpf *open_and_load();
    static inline int load(struct fib_lookup_bpf *skel);
    static inline int attach(struct fib_lookup_bpf *skel);
    static inline void detach(struct fib_lookup_bpf *skel);
    static inline void destroy(struct fib_lookup_bpf *skel);
    static inline const void *elf_bytes(size_t *sz);
#endif /* __cplusplus */
};
```

这是我们加载的eBPF程序的句柄，当我们调用Skeleton加载器时，它会返回给我们。

```
static inline struct fib_lookup_bpf *
fib_lookup_bpf__open_and_load(void)
```

在这个文件里，我感兴趣的在这

```
struct fib_lookup_bpf__bss {
    struct bpf_fib_lookup fib_params;
    int fib_lookup_ret;
} *bss;
```

注意，我们可以在bss字段中访问到全局的零初始化变量。

这使得用户空间程序能够加载eBPF程序，并检索其句柄，然后在调用`bpf_test_run_opts`之前和之后**注入**和**读取**全局变量的值。

这正是我们的测试运行器要做的事情。

## 编写测试运行器

如上所述，我们希望我们的测试运行器执行以下操作：

1. 将eBPF测试程序加载到内核中，并获得在`bpf_lookup.skel.h`中定义的`fib_lookup_bpf`结构的句柄。
2. 在运行测试之前，向测试中注入一个模拟的`bpf_fib_lookup`参数结构。
3. 利用libpf的`bpf_test_run_opts`函数在用户空间中运行我们的测试。
4. 读取生成的`fib_lookup_bpf`和`fib_lookup_ret`以确定是否使用了默认网关。

由于我们控制测试运行的网络命名空间，因此我们可以硬编码表示默认网关的接口ID（ifindex），使得我们的测试运行器更简单。

让我们来看一下测试运行器：

```
// test.c
#include <bpf/bpf.h>
#include <bpf/libbpf.h>
#include <stdio.h>
#include <bpf/bpf_endian.h>
#include "fib_lookup.skel.h"
#include "net/ethernet.h"
#include "linux/ip.h"
#include "netinet/tcp.h"

#define TARGET_IFINDEX 2

// in our test, we only care that the packet is the correct size,
// since our test does not touch any packet data.
char v4_pkt[(sizeof(struct ethhdr) + sizeof(struct iphdr) + sizeof(struct tcphdr))];

// create an empty skb as mock data, our tests do not touch any skb fi...