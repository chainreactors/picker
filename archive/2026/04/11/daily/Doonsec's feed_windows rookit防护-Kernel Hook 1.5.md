---
title: windows rookit防护-Kernel Hook 1.5
url: https://mp.weixin.qq.com/s/bLx-4_zOSLWTiteR4V3fOw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:41:53.819150
---

# windows rookit防护-Kernel Hook 1.5

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bz5OjA3RpuicXpPYyHXj7aFo8Un5Ovw6rtOJaiawTVoRDB8HIv1ywwt5ZLWeCYHCTnGWUkYkhVEJngvtfNyJP99zicNu5ZBhZdOjLJgdWzMMZ8/0?wx_fmt=jpeg)

# windows rookit防护-Kernel Hook 1.5

原创

joe1sn
joe1sn

不止Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

之前一篇写了 inline hook和ssdt两种方式，但是相关的的某些东西没讲清楚。

TL,DR：介绍驱动加载的方法，PatchGuard**简介**，如何在测试中关闭/开启KVAS保护（Shadow SSDT中的`KiSystemCall64Shadow`相关），完整的ssdt/shadow hook方法，最后内容是Shadow SSDT枚举（KiSystemCall64/KiSystemCall64Shadow开始）。

## Ring3 加载一个sys文件

首先有一个hello world的驱动，尝试使用命令行加载他（使用管理员权限）

```
sc create <使用的名称> type= kernel start= demand binPath="/??/<驱动文件路径，这里应该用的是描述符格式>"
sc start <使用的名称>sc stop <使用的名称>sc delete <使用的名称>
```

![image-20260407135338908](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpu8jgzpxLVLAmQKd6FEyrM6sZ0NMWRjDpvsqFFtDichQEP3chMvCEvsjk88UyEgzgQW3hBmspMT429h5rvWIPFeuK0cBN7hWZMx4/640?wx_fmt=png&from=appmsg)

`sc`是Service Control的简称，本质是操作 Windows 的 SCM（服务控制管理器），这里的加载驱动本质上是创建一个 kernel类型的服务，然后启动。

> 服务控制管理器（SCM）在系统启动时启动。 它是远程过程调用 （RPC） 服务器，以便服务配置和服务控制程序可以作远程计算机上的服务。
>
> 服务函数为 SCM 执行的以下任务提供接口：
>
> * 维护已安装服务的数据库。
> * 在系统启动时或按需启动服务和驱动程序服务。
> * 枚举已安装的服务和驱动程序服务。
> * 维护运行服务和驱动程序服务的状态信息。
> * 将控制请求传输到正在运行的服务。
> * 锁定和解锁服务数据库。
>
> https://learn.microsoft.com/zh-cn/windows/win32/services/service-control-manager

那么sc是如何完成这一过程的呢？对应的代码在附录的《简单的ring3驱动加载器》

![image-20260407140946416](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpu83wO5qicicda2ZnoZzTtI5BpItu6YspERpljFdtfJiazSII3SKtUPwXNd07MoteCynibSIiaReM4ZZMLUECMMib9Cficn5b9jPotSe7o/640?wx_fmt=png&from=appmsg)

## Ring0 加载一个sys文件

正常做法就是先注册表`HKLM\SYSTEM\CurrentControlSet\Services\<service name>`

然后调用`ZwLoadDriver` API

```
UNICODE_STRING regPath;RtlInitUnicodeString(    &regPath,    L"\\Registry\\Machine\\System\\CurrentControlSet\\Services\\MyDriver2");
NTSTATUS status = ZwLoadDriver(&regPath);
```

**那么使用手动加载呢？**这里需要PE 文件格式的基础，可以看：[PE文件格式解析](https://mp.weixin.qq.com/s?__biz=Mzk0MTY5NDg3Mw==&mid=2247483797&idx=1&sn=0d463a5a823050cfc33287970ac1f17f&scene=21#wechat_redirect)

这里修改下，就可以的得到内核手动映射，不过这个暂时过不了`__security_cookie`的检测，所以得自己设置`AddressofEntry`的值或者改写`cookie`，代码在附录的《手动映射SYS》，注意修改

* `main`中的文件路径
* `ExecuteMappedDriver`中的entry偏移
* `FixImportTable`中`while`循环中的IAT个数大小

## PatchGuard

具体的分析可能会后续重新写一篇文章，如果实在想提前了解可以参考

https://blog.tetrane.com/downloads/Tetrane\_PatchGuard\_Analysis\_RS4\_v1.01.pdf

基本上所有的入门介绍都或多或少参考了这个PDF

本质上，它是内核的重要组成部分，与内核的其他部分一样在 Ring 0 中运行。它并非某种对 Ring 0 代码拥有更大权限的 Ring -1 机制（至少本文讲的范围内没有）。它的主要目的是检查关键的内核结构和代码，确保它们没有被篡改。如果检测到任何未经授权的修改，它会触发蓝屏死机，并附带错误代码`CRITICAL_STRUCTURE_CORRUPTION`和错误检查代码`0x109`，从而避免任何错误或混淆。它明确地表明 Ring 0 中某些不应该被修改的内容已被修改。

并且由于PG的异步机制，因此无法确定它何时会检查关键结构和代码。

主要检测的内容有

* IDT（中断描述符表）和 GDT（全局描述符表）

+ **GDT**：是IA-32和x86-64架构特有的二进制数据结构。它包含向CPU提供有关内存段的条目。
+ **IDT**：是一种专用于 IA-32 和 x86-64 架构的二进制数据结构。它是保护模式和长模式下与实模式中断向量表 (IVT) 对应的机制，用于告知 CPU 中断服务例程 (ISR) 的位置（每个中断向量对应一个 ISR）。

* **MSR**（模型特定寄存器）：CPU 寄存器，用于控制高级行为，例如功能、限制和执行流程管理。
* **SSDT**（系统服务描述符表）：一个包含指向实现系统调用（例如`NtCreateFile`，、`NtOpenProcess`等）的内核函数的指针的表。
* **内核栈**
* **内核结构**
* **全局变量**
* **KPP引擎**

## 关于KVAS保护

> KVAS全称是Kernel Virtual Address Shadow，它的出现与MeltDown（CVE-2017-5754）和TotalMeltDown（CVE-2018-1038）有关。
>
> 我的描述不一定准确，大致上来说这两个漏洞利用了CPU的乱序执行技术，即CPU在执行时不一定会按照流程执行。当我们访问一个不能被用户模式访问的内存页时，CPU会执行该语句然后将其缓存到内存中，等到发现不能访问后返回错误，但是该数据依旧存在于缓存当中。利用这种思路就可以完全读取内核中的数据，实现权限提升等。
>
> 微软为了缓解该漏洞，从用户页表中隔离出内核页表，让用户态访问到的内核页表也是经过映射的，并且会将用户页表自动标记为NX，让我们的shellcode无法执行

笔者在这里遇到了很有趣的一点就是在最新的`AMD Ryzen9 8945HX`上

```
    DbgPrint("Driver Loaded\n");    DriverObject->DriverUnload = DriverUnload;
    DWORD64 dmsr = __readmsr(0xC0000082);    DbgPrint("KiSystemCall64 at %p\n", dmsr);
```

无法让结果是**`KiSystemCall64Shadow`**（Shadow SSDT依旧是存在的！），反倒是在`Intel i5 9300H`的CPU上成功实现了。

**所以这里只讲在受影响的Intel CPU上如何实现的**

Windows内核缓解机制使用了Kva Shadow内存，尝试将其关闭

在注册表`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management`

创建两个DWORD值：`FeatureSettingsOverride``FeatureSettingsOverrideMask`，设置如下后重启

![image-20260411103229487](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibrhP695Le7lQ6foiaJlmUicXASKib2R92uMuJWic6AaEib2ClY7ufdwWpC1IlJIowRvz4JJfJQMGFD1H8LDR2uPkZ8hoFcEsDYTNns/640?wx_fmt=png&from=appmsg)

设置值为3，然后重启

![image-20240118140220468](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpu92UagFgtohKJQlnCoJmbHTMfd0okLU4vdrNzJoqqboibeS5iaCDibRrO1wDA50UkiceT5prRDabSibRSGlzHRY4Rc30q8K3661PHos/640?wx_fmt=png&from=appmsg)

**这两个值存在并且值正确的时候，关闭KVAS，**使用的就是`KiSystemCall64`，找到的是`SSDT`

![image-20260410205731607](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu9zIYkRE3W5dT7hnPPEmrkem3rogldZ9Agic4vEic6BuLPw1N3Ho8q9necZJMHQqL9JXBJcyIBhsc6u9PQ5NqvV6HfatH6ef84SY/640?wx_fmt=png&from=appmsg)

![image-20260410205814991](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuicBn7yZXFebhiaev1R7hf1jvkbbazqbBD9pr5Wia51jIqicMw7n62juUyLlXF2nIRJuIlYpJ7mFAibOKFtlpSoO2ibflsUWSVfKxWF4/640?wx_fmt=png&from=appmsg)

**删除这两个，开启KVAS**的时候就为`KiSystemCall64Shadow`

![image-20260411205104804](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibUEZ7482FAriahNBOdLkkDawcAnBI5QjricxY9Gib01t447LbKk6zhr21wxSzcC9u2ViaYCib80CqrmKhP7P1VZTHanWvK7w5BFVrk/640?wx_fmt=png&from=appmsg)

![image-20260411204856925](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibiadRoibTjzL4Kkzhqcs9iahNEZkavMl5VTjsZzpvukYjjgVcsJ5HCbDk8qRdae8ZtInXgNsIvXnQhV0yfI1InmicGJrHG0eWJgGk/640?wx_fmt=png&from=appmsg)

![image-20260411204910559](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu8r73AgCpUq3s4IfgFFichkbLQibQ6pVRg1lWvO1P2cRF2wwcl9534x6lkrKhxH4R2JVwbaE1cicmyTgz1cv9mPGdBKoOsQex3w5c/640?wx_fmt=png&from=appmsg)

## 完整 SSDT Hook

[上一篇文章提到](https://mp.weixin.qq.com/s?__biz=Mzk0MTY5NDg3Mw==&mid=2247484460&idx=1&sn=fd8381acfbf291e762353005f5e9ce56&scene=21#wechat_redirect)主要的问题是在64位系统上根据 ssdt 的算法，不能直接将新的函数的地址直接转为数组的下表（**寻址范围太小**）

![image-20260411142643283](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuibBGaSc7JdJYDANiclPnKM8erKFVPLV857Jx3nxtyKp2tOyIpEDbuULLXymRc8aw5nT4TA0icMPktII5VYMn4LxLZTOgaIzmwmcg/640?wx_fmt=png&from=appmsg)

1. 找到临近的空位内存并申请

   我手动调试找到了一块合适的位置进行测试，这一过程可以被自动化

   我选择了在`ntoskrl.exe`的`.text`最后一部分，根据RVA找到位置，而且调试后发现距离`ssdt->table`仅有`0x04ff189`

   ![image-20260411142739249](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuicS8cQvdSjwQfyytoN4f3nqAOkFgrC8sQnYxujUJk3MQllfuKvL345ibUkympMgBibRuYib3lxU1QiaibHRrOfUSoiabZIFics9v7f2Ds/640?wx_fmt=png&from=appmsg)

   ![image-20260411143034601](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpuibjh7tIr6DLQarnxsyPOtlprpLFGVduIdOQWuZDicj46apH5icobdib2qdttrt924oyickXE9TepiaB8USKrK3QaP5byEs8ITdXeFDw/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuicyJT8oTmVVBibtiaAeGfEVvhIfDrH7icibmFBNM3NibMia35L2FJic0wo2hNR6h95y7c8MsNXfzE5zibfTsMuiacVrPJ8BK3O3tu6kbozY/640?wx_fmt=png&from=appmsg)
2. 在新申请的临近位置内编写`trampoline`，跳转到新的函数

   ![image-20260411144059555](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuibPyKqyowuu73xTXYXXj6AIEgNZqLMUg1ohyFSELBEgsLBD1GV7dbNK8jvYARDD2YjxsA5R5ozdxcaAUBRiaDB0NXe8ia7xzg9Ig/640?wx_fmt=png&from=appmsg)

   最后的效果：

![](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu8Ey7zXXfVHcmkfGeQ6wBG7N8fTDPiazSEib0KT6t3icdFqCGJkDz8aTPwCHDud5iab0ibIic2mhYS2CGQW56sGQcPDiakC30V6gjUfw4/640?wx_fmt=png&from=appmsg)

实现代码在附录《完整SSDT Hook》部分

## 枚举Shadow SSDT

由于前文关于KVAS保护中所提到的内容，这里要分两种情况进行探讨了

1. 从`KiSystemCall64`到Shadow SSDT（我使用AMD CPU）
2. 从`KiSystemCall64Shadow`到Shadow SSDT（我使用Intel CPU）

### 从KiSystemCall64开始

回顾[前文](https://mp.weixin.qq.com/s?__biz=Mzk0MTY5NDg3Mw==&mid=2247484460&idx=1&sn=fd8381acfbf291e762353005f5e9ce56&scene=21#wechat_redirect)

> 然后继续向下查到`KiSystemServiceRepeat`，主要是为了拿到`KeServiceDescriptorTable`或者`KeServiceDescriptorTableShadow`的值，在这里就是
>
> `35 05 9F 00`和`AE B6 8E 00`
>
> [图片]
>
> https://mp.weixin.qq.com/s/tg6ah6UD7q8wDCrWP7-vMQ

我们只需要改特征值找到`KeServiceDescriptorTableShadow`

```
    for (size_t i = 0; i < 0x1000; i++)    {        if (*(tempptr + i) == 0x4c && *(tempptr + i + 1) == 0x8d && *(tempptr + i + 2) == 0x1D) {            offset = *((PLONG)(tempptr + i + 3));            table = (PSYSTEM_SERVICE_TABLE)(tempptr + i + 7 + offset);            break;        }    }
```

![image-20260411150221090](https://mmbiz.qpic.cn/sz_mmbiz_p...