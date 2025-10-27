---
title: eCapture旁观者支持Golang tls/https加密明文捕获
url: https://www.cnxct.com/ecapture-supported-golang-tls-plaintext-captured/
source: CFC4N的博客
date: 2023-03-12
fetch_date: 2025-10-04T09:21:59.855613
---

# eCapture旁观者支持Golang tls/https加密明文捕获

Toggle navigation

[CFC4N的博客](https://www.cnxct.com/ "CFC4N的博客")
记住一个人的好，总强过记住一个人的坏!

* 作品
  + [eCapture旁观者–HTTPS/TLS抓包](https://ecapture.cc "eCapture旁观者--HTTPS/TLS抓包")
  + [Golang eBPF Manager](https://github.com/gojue/ebpfmanager "Golang eBPF Manager")
  + [eBPF技术精选资料](https://github.com/gojue/ehids-slide "eBPF技术精选资料")
  + [League Of legends启动器](https://github.com/cfc4n/lol_launcher "League Of legends启动器")
  + [eBPF HIDS主机入侵检测](https://github.com/gojue/ehids-agent "eBPF HIDS主机入侵检测")
* [归档](https://www.cnxct.com/archives/ "归档")
* [关于我](https://www.cnxct.com/about/ "关于我")
* [工作机会](https://www.cnxct.com/jobs/ "工作机会")

# eCapture旁观者支持Golang tls/https加密明文捕获

[2023/03/122023/03/12](https://www.cnxct.com/ecapture-supported-golang-tls-plaintext-captured/)  [CFC4N](https://www.cnxct.com/author/admin/)

### 文章目录

1. [前言](#ftoc-heading-1)
2. [适用场景](#ftoc-heading-2)
3. [使用方法](#ftoc-heading-3)
4. [下载地址](#ftoc-heading-4)
5. [以下内容，为功能实现原理，若你只是使用，可跳过。](#ftoc-heading-5)
   1. [技术原理](#ftoc-heading-6)
      1. [Probe参数获取](#ftoc-heading-7)
      2. [Probe参数选择](#ftoc-heading-8)
   2. [扩展阅读](#ftoc-heading-9)

### 前言

云原生生态中，golang语言开发的项目越来越多，例如Docker和K8s、etcd等。作为SRE、RD，偶尔需要在生产环境抓网络通讯包，用来分析排查故障。很多时候，都是tls/https加密协议，如何在不重启业务保留现场，不改为自定义CA证书的情况下，分析明文通讯内容呢？

![](https://image.cnxct.com/2023/01/10001.jpg)

### 适用场景

eCapture 0.5.0版本在2023年3月12日发布，支持了go语言编写的软件的tls/https明文抓包。只需要root权限，即可捕获并保存为pcapng格式，使用wireshark即可打开查看。

![](https://image.cnxct.com/2023/03/ecapture_releases_tag_v0.5.0.png)

### 使用方法

gotls模块的`e`参数用来设定golang编译的可执行文件路径，可以通过`ecapture gotls -h`来查看使用说明。

```
bin/ecapture gotls -h
NAME:
    gotls - capture golang tls/https text content without CA cert for ELF compile by Golang toolchain

USAGE:
    ecapture gotls [flags]

DESCRIPTION:
    use eBPF uprobe/TC to capture process event data and network data. also support pcap-NG format.
    ecapture gotls
    ecapture gotls --elfpath=/home/cfc4n/go_https_client --hex --pid=3423
    ecapture gotls --elfpath=/home/cfc4n/go_https_client -l save.log --pid=3423
    ecapture gotls -w save_android.pcapng -i wlan0 --port 443 --elfpath=/home/cfc4n/go_https_client

OPTIONS:
  -e, --elfpath=""    ELF path to binary built with Go toolchain.
  -h, --help[=false]    help for gotls
  -i, --ifname="" (TC Classifier) Interface name on which the probe will be attached.
      --port=443    port number to capture, default:443.
  -w, --write=""  write the  raw packets to file as pcapng format.

GLOBAL OPTIONS:
  -d, --debug[=false]       enable debug logging
      --hex[=false]     print byte strings as hex encoded strings
  -l, --log-file=""       -l save the packets to file
      --nosearch[=false]    no lib search
  -p, --pid=0           if pid is 0 then we target all pids
  -u, --uid=0           if uid is 0 then we target all users
```

**举个例子**

比如`/path/elf_filepath_compiled_by_go`是一个go写的web服务，并且开启了https加密，代码如下：

```
package main

import (
    "crypto/tls"
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {

    b, e := GetHttp("https://github.com")
    if e == nil {
        fmt.Printf("response body: %s\n\n", b)
    } else {
        fmt.Printf("error :%v", e)
    }
}

func GetHttp(url string) (body []byte, err error) {
  // 开启TLS密钥记录，用于跟eCpature捕获的密钥对比。
    f, err := os.OpenFile("/tmp/go_master_secret.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0600)
    if err != nil {
        panic(err)
    }
    defer f.Close()
    c := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{InsecureSkipVerify: true, KeyLogWriter: f},
        }}
    resp, e := c.Get(url)
    if e != nil {
        return nil, e
    }

    defer resp.Body.Close()
    body, err = io.ReadAll(resp.Body)
    return body, err
}
```

可以使用如下命令，捕获明文通讯。 不用重启这个服务进程，也不需要做其他任何配置，就跟使用`tcpdump`一样。

```
./ecapture gotls -e=/path/elf_filepath_compiled_by_go -w a.pcapng -i eth0
```

![](https://image.cnxct.com/2023/03/ecapture-gotls.png)

![](https://image.cnxct.com/2023/03/gotls-masterkey.png)

**Wireshark打开网络包**

![](https://image.cnxct.com/2023/03/ecapture-gotls-wireshark.png)

### 下载地址

eCapture Github仓库：<https://github.com/gojue/ecapture/releases/tag/v0.5.0>

韩国GitHub镜像：[https://ghproxy.com/https://github.com/gojue/ecapture/releases/tag/v0.5.0](https://ghproxy.com/https%3A//github.com/gojue/ecapture/releases/tag/v0.5.0)

## 以下内容，为功能实现原理，若你只是使用，可跳过。

---

### 技术原理

#### Probe参数获取

Golang的ABI不同于C，自定义了ABI机制。并且在go 1.17之前，使用的是栈方式传递调用参数；1.17以以后使用了寄存器方式传递调用参数。你可以阅读[Register-based Go calling convention](https://go.googlesource.com/proposal/%2B/refs/changes/78/248178/1/design/40724-register-calling.md) 了解更多知识。

这里有一张Golang的函数参数、返回值的寄存器传递布局，供参考。更多内容可以在线阅读[《Go语言高级编程》](https://chai2010.cn/advanced-go-programming-book/ch3-asm/ch3-04-func.html)中文版

![](https://image.cnxct.com/2023/03/ch3-10-func-arg-01.ditaa_.png)

eCapture的参数获取实现，可以阅读[kern/go\_argument.h](https://github.com/gojue/ecapture/blob/master/kern/go_argument.h)

#### Probe参数选择

笔者这里hook的是Golang源码目录下`crypto/tls/common.go`文件中的`writeKeyLog`函数。用来捕获tls的master secret的label类别、clientRandom、密钥值等。

![](//image.cnxct.com/2023/03/carbon.png)

**Golang函数参数传递**

有个需要注意的地方，比如`writeKeyLog`函数的第一个参数是`string`类型，第二、三个参数是`slice`类型。在Golang里，也都是一个结构体，如下代码：

```
// runtime/string.go
type stringStruct struct {
    str unsafe.Pointer
    len int
}

// runtime/slice.go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

以`string`类型为例，在Go 的参数传递时，不光传递字符串的`str unsafe.Pointer`指针地址，也还会传递`len int`到寄存器上。所以，在获取参数时，需要注意参数所在位置。

eCapture的实现：

```
lab_ptr = (void *)go_get_argument(ctx, is_register_abi, 2);
lab_len_ptr = (void *)go_get_argument(ctx, is_register_abi, 3);
cr_ptr = (void *)go_get_argument(ctx, is_register_abi, 4);
cr_len_ptr = (void *)go_get_argument(ctx, is_register_abi, 5);
secret_ptr = (void *)go_get_argument(ctx, is_register_abi, 7);
secret_len_ptr = (void *)go_get_argument(ctx, is_register_abi, 8);
bpf_probe_read_kernel(&lab_len, sizeof(lab_len), (void *)&lab_len_ptr);
bpf_probe_read_kernel(&cr_len, sizeof(lab_len), (void *)&cr_len_ptr);
bpf_probe_read_kernel(&secret_len, sizeof(lab_len), (void *)&secret_len_ptr);
```

**Golang uretprobe**

在eCapture的文本模式中，需要在加密之前、解密之后拿到明文，对应的两个函数分别是`crypto/tls.(*Conn).writeRecordLocked`和 `crypto/tls.(*Conn).Read`。加密之前的获取只需要使用eBPF uprobe HOOK即可实现。而解密之后，则需要`uretprobe`，但Golang里，`uretprobe`的实现机制，会破坏他的堆栈，导致Golang程序进程崩溃。

这个问题，在`iovisor/bcc`社区也有讨论:[BCC issue: Go crash with uretprobe #1320](https://github.com/iovisor/bcc/issues/1320)，包括火焰图、eBPF的领导者[Brendan Gregg](https://github.com/brendangregg)，对这个问题也没有太好的办法。[Gianluca Borello](https://github.com/gianlucaborello)给了间接的解决方案，相对来说还是比较繁琐的，也有一定的crash风险，有兴趣的同学可以去看看。

eCapture里，加密之前的`uprobe` 已经完成hook，实现https/tls的请求内容明文捕获。但解密后的内容，暂时无法实现。笔者也在尝试其他思路，比如找到`Read`返回值的调用函数，在哪里使用`uprobe`实现，但这点逻辑比较偏业务层，调用者比较多，不太方便过滤。如果你有更好的办法，也欢迎提出来。

### 扩展阅读

[Hooking Go from Rust – Hitchhiker’s Guide to the Go-laxy](https://metalbear.co/blog/hooking-go-from-rust-hitchhikers-guide-to-the-go-laxy/)

[BCC issue: Go crash with uretprobe #1320](https://github.com/iovisor/bcc/issues/1320)

[Interface method calls with the Go register ABI](https://eli.thegreenplace.net/2022/interface-method-calls-with-the-go-register-abi/)

[eCapture旁观者官网](https://ecapture.cc)

[eCapture旁观者 Github仓库](https://github.com/gojue/ecapture)

[![知识共享许可协议](//www.cnxct.com/attachments/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)CFC4N的博客 由 [CFC4N](http://www.cnxct.com) 创作，采用 [署名—非商业性使用—相同方式共享 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans) 进行许可。基于[https://www.cnxct.com](http://www.cnxct.com)上的作品创作。转载请注明转自：[eCapture旁观者支持Golang tls/https加密明文捕获](https://www.cnxct.com/ecapture-supported-golang-tls-plaintext-captured/)

相关文章:

1. [eCapture：无需CA证书抓https网络明文通讯](https://www.cnxct.com/what-is-ecapture/ "eCapture：无需CA证书抓https网络明文通讯")
2. [eCapture旁观者：Android HTTPS明文抓包，无需CA证书](https://www.cnxct.com/ecapture-for-android/ "eCapture旁观者：Android HTTPS明文抓包，无需CA证书")
3. [如何使用Delve和eBPF更快地调试Go程序](https://www.cnxct.com/how-debugging-go-prog...