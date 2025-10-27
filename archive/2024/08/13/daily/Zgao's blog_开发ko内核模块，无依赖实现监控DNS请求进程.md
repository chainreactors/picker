---
title: 开发ko内核模块，无依赖实现监控DNS请求进程
url: https://zgao.top/%e5%bc%80%e5%8f%91ko%e5%86%85%e6%a0%b8%e6%a8%a1%e5%9d%97%ef%bc%8c%e6%97%a0%e4%be%9d%e8%b5%96%e5%ae%9e%e7%8e%b0%e7%9b%91%e6%8e%a7dns%e8%af%b7%e6%b1%82%e8%bf%9b%e7%a8%8b/
source: Zgao's blog
date: 2024-08-13
fetch_date: 2025-10-06T18:01:19.082634
---

# 开发ko内核模块，无依赖实现监控DNS请求进程

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 开发ko内核模块，无依赖实现监控DNS请求进程

* [首页](https://zgao.top)
* [开发ko内核模块，无依赖实现监控DNS请求进程](https://zgao.top:443/%E5%BC%80%E5%8F%91ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%EF%BC%8C%E6%97%A0%E4%BE%9D%E8%B5%96%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7dns%E8%AF%B7%E6%B1%82%E8%BF%9B%E7%A8%8B/)

[8月 12, 2024](https://zgao.top/2024/08/)

### 开发ko内核模块，无依赖实现监控DNS请求进程

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E5%BC%80%E5%8F%91ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%EF%BC%8C%E6%97%A0%E4%BE%9D%E8%B5%96%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7dns%E8%AF%B7%E6%B1%82%E8%BF%9B%E7%A8%8B/)

监控Linux主机发起DNS请求的进程是应急响应中经常遇到的一个问题。虽然可以通过systemtap或者ebpf的方式实现，但是在实战场景下两者的安装都非常麻烦。

1. ebpf不支持低版本的内核，升级内核又需要重启，真实场景下不太可能实现。并且大部分内核只支持源码编译安装ebpf，过程非常繁琐。
2. systemtap必须安装当前指定内核版本的debuginfo，依赖多个包，动则几百M上G。镜像源都是国外的，在客户现场下载非常耗时。

监控发起DNS请求原本只是非常小的需求，用ebpf和systemtap简直是大材小用。我一直在思考有没有更轻量通用的解决方案。

文章目录

[ ]

* [编写ko内核模块](#%E7%BC%96%E5%86%99ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97 "编写ko内核模块")
  + [解析DNS请求](#%E8%A7%A3%E6%9E%90DNS%E8%AF%B7%E6%B1%82 "解析DNS请求")
  + [获取进程信息](#%E8%8E%B7%E5%8F%96%E8%BF%9B%E7%A8%8B%E4%BF%A1%E6%81%AF "获取进程信息")
  + [完整代码](#%E5%AE%8C%E6%95%B4%E4%BB%A3%E7%A0%81 "完整代码")
* [编写Makefile](#%E7%BC%96%E5%86%99Makefile "编写Makefile")
* [编译ko内核模块](#%E7%BC%96%E8%AF%91ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97 "编译ko内核模块")
* [加载内核模块并输出监控信息](#%E5%8A%A0%E8%BD%BD%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E5%B9%B6%E8%BE%93%E5%87%BA%E7%9B%91%E6%8E%A7%E4%BF%A1%E6%81%AF "加载内核模块并输出监控信息")
* [补充：兼容低版本的内核](#%E8%A1%A5%E5%85%85%EF%BC%9A%E5%85%BC%E5%AE%B9%E4%BD%8E%E7%89%88%E6%9C%AC%E7%9A%84%E5%86%85%E6%A0%B8 "补充：兼容低版本的内核")
* [一键加载ko命令](#%E4%B8%80%E9%94%AE%E5%8A%A0%E8%BD%BDko%E5%91%BD%E4%BB%A4 "一键加载ko命令")

## 编写ko内核模块

### 解析DNS请求

DNS请求是以特定格式在UDP数据包的数据部分发送的。要想通过内核监控DNS的请求，我们需要一个结构体来解析DNS header。

```
struct dnshdr {
    uint16_t id;       // 会话标识
    uint16_t flags;    // DNS 标志
    uint16_t qdcount;  // 问题数
    uint16_t ancount;  // 回答记录数
    uint16_t nscount;  // 授权记录数
    uint16_t arcount;  // 额外记录数
    // 后续为问题记录等
};
```

这里可以参考Linux内核的代码。

<https://github.com/TritonDataCenter/syslinux/blob/master/core/fs/pxe/dnsresolv.c>

### 获取进程信息

在Linux内核中，可以通过`current`宏访问当前运行的进程的`task_struct`结构，该结构包含进程的各种信息，包括进程名（`comm`字段）和进程ID（`pid`字段）。

`hook_func` 是一个内核模块中定义的钩子函数，用于通过 Netfilter 框架在 Linux 内核中拦截网络数据包。

* `priv`: 通常用于传递用户定义的私有数据，但在大多数简单的钩子函数中不使用。
* `skb`: 指向`sk_buff`结构的指针，该结构包含当前正在处理的网络数据包的所有信息。
* `state`: 包含关于钩子点的状态信息，如正在处理的网络设备和协议等。

```
unsigned int hook_func(void *priv, struct sk_buff *skb, const struct nf_hook_state *state) {
    struct iphdr *iph;
    struct udphdr *udph;
    struct dnshdr *dnsh;
    unsigned char *data;
    char domain_name[256];  // 存储域名
    int i = 0, len;

    if (!skb)
        return NF_ACCEPT;

    iph = ip_hdr(skb);
    if (iph->protocol == IPPROTO_UDP) {
        udph = udp_hdr(skb);
        if (ntohs(udph->dest) == 53) { // 检查目的端口是不是53
            dnsh = (struct dnshdr *)((unsigned char *)udph + sizeof(struct udphdr));
            data = (unsigned char *)(dnsh + 1); // 跳过DNS头，到达数据部分

            while (data[i] != 0) { // 域名结束标记为0
                len = data[i]; // 第一个字节是长度
                i++;
                if (len == 0) break; // 零长度表示域名结束
                if (i + len > 255) break; // 防止数组溢出
                strncat(domain_name, data + i, len); // 复制长度指定的字符串
                strcat(domain_name, "."); // 添加点分隔符
                i += len; // 移动到下一个标签
            }
            domain_name[strlen(domain_name) - 1] = '\0'; // 移除最后的点

            printk(KERN_INFO "DNS Query for %s from PID %d (%s)\n", domain_name, current->pid, current->comm);
        }
    }

    return NF_ACCEPT;
}
```

如果 `skb` 为空，函数直接返回 `NF_ACCEPT`，表示放行该数据包，不做任何处理。使用 `ip_hdr(skb)` 宏从 `skb` 中提取 IP 头部信息。

然后检查数据包是否为 UDP 协议（DNS 查询通常使用 UDP协议）。使用 `udp_hdr(skb)` 宏从 `skb` 中提取 UDP 头部。检查 UDP 数据包的目标端口是否为 53（DNS 服务的标准端口）。如果不是端口 53，钩子函数将不进一步处理这个数据包。进一步解析 DNS 数据包中的域名，处理每个标签，并在读取到零长度字节时停止，这表示域名的结束。

最后打印解析出的域名、发起查询的进程 ID (`current->pid`) 和进程名 (`current->comm`)。

### 完整代码

```
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/udp.h>
#include <linux/skbuff.h>

static struct nf_hook_ops nfho;

struct dnshdr {
    uint16_t id;
    uint16_t flags;
    uint16_t qdcount;
    uint16_t ancount;
    uint16_t nscount;
    uint16_t arcount;
};

unsigned int hook_func(void *priv, struct sk_buff *skb, const struct nf_hook_state *state) {
    struct iphdr *iph;
    struct udphdr *udph;
    struct dnshdr *dnsh;
    unsigned char *data;
    char domain_name[256];
    int i = 0, len;

    if (!skb)
        return NF_ACCEPT;

    iph = ip_hdr(skb);
    if (iph->protocol == IPPROTO_UDP) {
        udph = udp_hdr(skb);
        if (ntohs(udph->dest) == 53) {
            dnsh = (struct dnshdr *)((unsigned char *)udph + sizeof(struct udphdr));
            data = (unsigned char *)(dnsh + 1);

            while (data[i] != 0) {
                len = data[i];
                i++;
                if (len == 0) break;
                if (i + len > 255) break;
                strncat(domain_name, data + i, len);
                strcat(domain_name, ".");
                i += len;
            }
            domain_name[strlen(domain_name) - 1] = '\0';

            printk(KERN_INFO "DNS Query for %s from PID %d (%s)\n", domain_name, current->pid, current->comm);
        }
    }

    return NF_ACCEPT;
}

int init_module() {
    nfho.hook = hook_func;
    nfho.hooknum = NF_INET_POST_ROUTING;
    nfho.pf = PF_INET;
    nfho.priority = NF_IP_PRI_FIRST;

    nf_register_net_hook(&init_net, &nfho);
    return 0;
}

void cleanup_module() {
    nf_unregister_net_hook(&init_net, &nfho);
}

MODULE_AUTHOR("https://zgao.top");
MODULE_DESCRIPTION("Extended DNS Request Monitor Module");
MODULE_LICENSE("GPL");
```

## 编写Makefile

内核模块代码开发完成后。要编译并加载一个内核模块（.ko文件），还需要设置内核模块的源代码、适当的Makefile文件，以及安装内核头文件。

```
obj-m += dns_monitor.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

## 编译ko内核模块

切换到包含源文件和Makefile的目录进行编译。

```
make
modinfo dns_monitor.ko
```

![](https://zgao.top/wp-content/uploads/2024/08/image-10-1024x530.png)

## 加载内核模块并输出监控信息

```
insmod dns_monitor.ko
lsmod| grep dns
dmesg -Tw
```

![](https://zgao.top/wp-content/uploads/2024/08/image-11-1024x550.png)

效果非常不错，hook网络请求的代码也没有额外依赖。需要用的时候随时编译加载ko即可，轻量方便。

```
rmmod dns_monitor
```

不需要监控了就直接rmmod即可。

## 补充：兼容低版本的内核

评论区反馈不支持低版本的内核，现在修改了的代码做了兼容。

如果有些centos机器没有安装内核开发包，需要执行下面的命令。

```
# 对于 CentOS/RHEL 7
sudo yum install kernel-devel kernel-headers
sudo yum install kernel-devel-$(uname -r)
# 检查安装是否成功
ls -la /lib/modules/$(uname -r)/build
```

## 一键加载ko命令

```
wget https://zgao.top/download/dns_monitor.tgz && tar xvf dns_monitor.tgz && make && insmod dns_monitor.ko && dmesg -Tw
```

实战场景开箱即用，当然前提是机器上默认有安装gcc可以编译ko代码。

Post Views: 1,770

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 5条评论

###### linux 发布于11:02 上午 - 5月 28, 2025

对内核版本有要求吧？3.10的就编不过

[回复](https://zgao.top/%E5%BC%80%E5%8F%91ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%EF%BC%8C%E6%97%A0%E4%BE%9D%E8%B5%96%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7dns%E8%AF%B7%E6%B1%82%E8%BF%9B%E7%A8%8B/?replytocom=9856#respond)

###### Zgao 发布于11:43 上午 - 5月 28, 2025

这个内核版本没测过，大部分云上Linux服务器是没问题的

[回复](https://zgao.top/%E5%BC%80%E5%8F%91ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%EF%BC%8C%E6%97%A0%E4%BE%9D%E8%B5%96%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7dns%E8%AF%B7%E6%B1%82%E8%BF%9B%E7%A8%8B/?replytocom=9857#respond)

###### Zgao 发布于12:22 下午 - 5月 28, 2025

已修改代码适配...