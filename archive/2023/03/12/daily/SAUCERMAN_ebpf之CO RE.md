---
title: ebpf之CO RE
url: https://saucer-man.com/machine_learning/1033.html
source: SAUCERMAN
date: 2023-03-12
fetch_date: 2025-10-04T09:22:01.247364
---

# ebpf之CO RE

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)

Previous post
Next post
Back to top
Share post

* [1. bcc怎么实现可移植性](#cl-1)
* [2. BPF CO-RE](#cl-2)* [2.1 BTF](#cl-3)
  * [2.2 Clang/LLVM编译器](#cl-4)
  * [2.3 BPF 加载器](#cl-5)
* [3. golang开发ebpf](#cl-6)* [3.1 安装环境](#cl-7)
  * [3.2 编译代码执行](#cl-8)
  * [3.3 未完待续](#cl-9)
* [4. 参考](#cl-10)

# ebpf之CO RE

2023-03-11

5551

[机器学习](https://saucer-man.com/category/machine_learning/)

> 文章最后更新时间为：2023年03月11日 14:24:08

在文章[ebpf初探](https://saucer-man.com/information_security/1014.html)中，介绍了ebpf的由来，并且通过bcc框架编写了第一个ebpf程序，由于ebpf是运行在内核空间的，所以依赖于内核提供的各种数据结构和内核类型。这也导致了一个问题，不同版本的内核之间会存在数据结构和内核类型的差异，依赖**开发环境本地的内核头文件**编译的 eBPF 程序， 是无法直接分发到其他机器运行，本篇文章来学习一下怎么做到CO RE，即一次编译，到处运行。文章表述中的BPF等同于eBPF。

## 1. bcc怎么实现可移植性

bcc本身既然作为一个BPF开发框架，本身是具有可移植能力的，bcc开发部署的过程如下：

1. 开发：将 BPF C 源码以**文本字符串**形式，**嵌入Python 编写的前端控制应用中**；
2. 部署：将控制应用以源码的形式拷贝到目标机器，并且在目标机器上安装bcc运行环境(包含bcc内置的Clang/LLVM编译环境)
3. 执行：在目标机器上，bcc调用它内置的 Clang/LLVM，然后 include 本地内核头文件 ，然后现场执行编译、加载、运行。

可以看出bcc实现可移植性的方案，就是在运行时使用内置Clang/LLVM进行编译，内置的Clang/LLVM对不同内核的差异做了处理。

BCC 虽然可以做到程序可移植，但从实现方案的角度也可以看出一些问题：

1. **Clang/LLVM 是一个庞大的库**，每一个要运行bcc程序的系统都需要安装这个库
2. 每次运行bcc程序时，都会编译一次 BPF 代码，消耗资源且速度较慢。

所以用bcc工具开发起来比较简单，因为bcc提供了比较简单的接口，但是在部署和分发的时候，比较劝退。理想的方式就是直接分发一个二进制文件，下面就来介绍下新的方式 BPF CO-RE。

## 2. BPF CO-RE

要想了解BPF CO-RE的实现方式，先需要了解下下面几个组件

### 2.1 BTF

BTF (BPF Type Format) 是CO-RE能够实现的核心组件，其实它就是一种元数据格式，定义了 BPF 程序 /map 有关的调试信息，它提供eBPF结构信息，在编译eBPF时，可以根据BTF信息查询linux内核的结构偏移量和其他详细信息，所以eBPF程序不再依赖目标环境的Clang和内核头文件。关于BTF的详细说明可以参考官方文档 <https://www.kernel.org/doc/html/latest/bpf/btf.html>，或者翻译版本[2]

不是所有的内核版本都有这个特性，该选项在[Linux 内核 5.2](https://github.com/torvalds/linux/commit/e83b9f55448afce3fe1abcd1d10db9584f8042a6) 中引入，ubuntu20.10之后默认支持该特性，可以通过以下的命令来查看内核是否支持BTF：

```
root@ubuntu22:~# cat /boot/config-`uname -r` | grep CONFIG_DEBUG_INFO_BTF
CONFIG_DEBUG_INFO_BTF=y
CONFIG_DEBUG_INFO_BTF_MODULES=y

或者也可以根据vmlinux文件来判断
root@ubuntu22:~# ls -la /sys/kernel/btf/vmlinux
-r--r--r-- 1 root root 5177795 Dec 25 05:51 /sys/kernel/btf/vmlinux
```

如果内核不支持这个属性，也可以自行编译内核， 在编译时指定 `CONFIG_DEBUG_INFO_BTF=y`即可。

### 2.2 Clang/LLVM编译器

Clang/LLVM是一个编译器框架，clang是前端，llvm是后端，我们可以将整个框架简称为Clang。

为了让 BPF 加载器将 BPF 程序适配到目标机器所运行的内核上， Clang 增加了几个新的 built-in，它们的功能是导出BTF的重定位信息，例如，如果想访问 `task_struct->pid`，那 clang 将做如下记录：这是一个 **位于结构体 `struct task_struct` 中、类型为 `pid_t`、名为 `pid` 的字段**，于是在编译完成后，BPF加载器就可以根据BTF信息对这些结构体的偏移做适配，从而修改编译完成的二进制文件，完成内核版本的适配。

除了字段重定位，其他一些字段相关的操作，例如判断`字段是否存在`或者 `字段长度`都是支持的。编译器的支持，使得加载器能够基于 BTF 信息来使它们可重定位。

### 2.3 BPF 加载器

这里所说的BPF加载器，基本上都是指的是libbpf(或者由其转化而来)，libbpf和bcc一样，是一个bpf加载器，将bpf程序加载进内核，然后附加到指定的hook点，并且与BPF map进行通信。

但是与bcc不同的是，BPF C程序编译成ELF格式后，**libbpf 会对 BPF ELF程序进行修改，以适配目标机器的内核版本**，它会查看 BPF 程序记录的 BTF 和重定位信息，然后拿这些信息跟当前内核提供的 BTF 信息相匹配，然后更新所有的类型和字段。所以从这个特点也会看出**用libbpf编写的程序，需要运行环境也支持BTF**。

其整个编译装载流程如下：

![2023-03-11T06:16:31.png](https:////saucer-man.com/usr/uploads/2023/03/1409804600.png "2023-03-11T06:16:31.png")

## 3. golang开发ebpf

ebpf的核心程序是通过c编写，clang进行编译的。在编译好ebpf程序后，我们需要将其加载到内核中。目前有很多个项目对ebpf的编写调试运行的流程进行了优化，比较有名的是bcc和libbpf。很多时候我们希望能够更加方便的进行程序编写和部署，也希望程序能够在不同的linux发行版和内核上使用（即BPF CO-RE），libbpf只能使用C/C++进行外部程序的开发。如果想使用go编写，有两个选择：cilium的ebpf项目和libbpf-go，这里我直接使用cilium的ebpf工具<https://github.com/cilium/ebpf>。

### 3.1 安装环境

* golang <https://go.dev/dl/>
* Make C语言编译工具
* Clang/LLVM 10+：可以将eBPF程序编写成BPF bytecode

```
sudo apt install -y make clang llvm

# test clang
clang -v
# test llvm
llc --version

配置环境变量
echo "export BPF_CLANG=clang" >> ~/.bashrc
source ~/.bashrc
```

### 3.2 编译代码执行

```
git clone https://github.com/cilium/ebpf.git
cd ebpf/
cd examples/kprobe
rm *.o
rm bpf_*.go
go generate
go build
```

打印的结果为执行 sys\_execve 的次数，若正确输出则说明环境搭建成功。
![2023-03-11T06:17:39.png](https:////saucer-man.com/usr/uploads/2023/03/4164198437.png "2023-03-11T06:17:39.png")

### 3.3 未完待续

本来是打算自己用golang开发ebpf程序的，但是由于工作原因，耽搁了很多，再继续看时，发现ebpf有很多地方是需要深入研究的，等有时间再慢慢补一下......

## 4. 参考

[1] BPF 可移植性和 CO-RE（一次编译，到处运行）<https://www.ebpf.top/post/bpf_core/>
[2] BPF BTF 详解 <https://www.ebpf.top/post/kernel_btf/>
[3] BPF Type Format (BTF) <https://www.kernel.org/doc/html/latest/bpf/btf.html>
[4] Cilium eBPF 搭建与使用 <https://barryx.cn/cilium_ebpf/>
[5] 使用Go语言开发eBPF程序 <https://tonybai.com/2022/07/19/develop-ebpf-program-in-go/>
[6] Cilium eBPF 搭建与使用 <https://luckymrwang.github.io/2022/08/13/Cilium-eBPF-%E6%90%AD%E5%BB%BA%E4%B8%8E%E4%BD%BF%E7%94%A8/>

1 + 7 =

 回复

快来做第一个评论的人吧~

Copyright © 2025 By [Typecho](https://www.typecho.org) & [saucerman](https://saucer-man.com)

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)