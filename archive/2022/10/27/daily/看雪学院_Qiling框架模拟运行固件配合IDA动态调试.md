---
title: Qiling框架模拟运行固件配合IDA动态调试
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458478983&idx=1&sn=ff6fcae96ce8db2dff62120a29aa3087&chksm=b18e590d86f9d01b60b98a9832f33c3408a620841e7cb1c92ab17330c20de734969abb1a0488&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-10-27
fetch_date: 2025-10-03T21:01:49.930333
---

# Qiling框架模拟运行固件配合IDA动态调试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m4hJS4Qks6gFK5KBV7vS3Lt10DaIeBTia8VsBibbBFcGK3unlpvEoHviaQ/0?wx_fmt=jpeg)

# Qiling框架模拟运行固件配合IDA动态调试

烧板侠

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mo39CNia16qziaUtsJv1HslIVBFC6HHIOqbAT6EQOvILz9nJKq98Iq8ww/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：烧板侠

### **前言**

###

### 实际分析嵌入式固件过程中，经常会遇到各种非Linux和非常见系统的固件，这类固件往往就是一个"裸"的二进制程序，而不像ELF和PE这些有特定结构的可执行程序，对于这类固件往往很难对它进行动态调试，而只能静态分析。最近一段时间，学习了很强大的Qiling框架，它除了可以模拟运行各种可执行程序，还提供了Debugger接口，于是乎我就想着能不能用Qiling配合IDA动态调试固件。遗憾的是网上关于Qiling的教程大部分都是模拟ELF和PE这些相对来说比较标准的程序，而模拟像这种就一个"裸"的二进制程序的资料却很少，这里分享下我的摸索过程。

###

### 关于Qiling和Unicorn这里就不多介绍了，详见官网：

### Qiling官网: *https://qiling.io/*

### Unicorn官网: https://www.unicorn-engine.org/

###

### 下面以我上个帖子 一个简单的STM32固件分析（https://bbs.pediy.com/thread-274788.htm）用到的固件stm32f103RCT6.bin来介绍如何用Qiling框架模拟运行指定函数并启用Debugger，然后使用IDA进行动态调试。

###

###

### **开始**

###

### 首先时qiling官方github的有一个example（https://github.com/qilingframework/qiling/tree/master/examples）引起了我的注意，如下图，qiling的示例有一个模拟arm下的uboot。uboot据我所知是一个bootloader，它在固件中就是一个"裸"的二进制程序，于是这里面可能就有我想要的样例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mp3gNH1PGCQxj8YOkBcicibSFeuF6thDAybDSZNmhd0zVKwy2cha8b56g/640?wx_fmt=png)

查看hello\_arm\_uboot.py代码，一直拉到最后，如下图，这部分代码就是模拟运行"裸"的二进制程序的一个例子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6ma79K3ictVCl4mqnwZzFVfwZAjq9Bic9OnuutBicnlibDicUFic8fnYnic6ciag/640?wx_fmt=png)

接下来就是照猫画虎，仿照着这个来尝试模拟运行stm32f103RCT6.bin固件中的XTEA函数。这里简单介绍下这个stm32f103RCT6.bin固件，它的加载基地址为0x8000000，从前一篇的分析可以知道它在地址0x800E288有个XTEA函数，这个函数就是接下来需要模拟调试运行的函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6myv3GDQ6bgXXzpnb7lLhlxCx6JQwtbjVc5oCY6gbyJvxxmuV4cO4J3g/640?wx_fmt=png)

首先是导入qiling和unicorn的包。

```
from qiling.core import *from qiling.const import *from qiling.os.const import *from unicorn.arm64_const import *from unicorn import *
```

对照代码样例，读入需要模拟的固件。

```
filepath='stm32f103RCT6.bin'with open(filepath, 'rb') as fp:    fw = fp.read()
```

接下来看原代码的Qiling对象生成方式，第一个code=uboot\_code[0x40:]，剔除了前0x40字节的原因应该是，uboot固件的前0x40字节不加载进内存，这里的stm32固件是整个都加载进内存的，所以可以直接传整个读入的fw。有个参数需要注意的是profile="uboot\_bin.ql"，看起来是还有一个配置文件"uboot\_bin.ql"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mGZYDE749m3lrrT58RtupOCtcjFBNq1ibEQlC6ZbaNRHzFPku9ibtfu3Q/640?wx_fmt=png)

在同级目录下，可以找到这个uboot\_bin.ql，那么接下来，需要简单理解下这个配置文件的各个参数的意义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mkWhWKqPrjFEQ923KkScKXYDyW9Jyo27R39WEbHUPkv36yenOBs7PDQ/640?wx_fmt=png)

源码中搜索"heap\_size"，如下图，可以在qiling/loader/blob.py（*https://github.com/qilingframework/qiling/blob/master/qiling/loader/blob.py*）中找到关于这几个参数的含义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mEBpVUNyq8RiaDIJ3eMfPIaW2j9zkgcbfbApibYxvHJmMSaVLf2NaT5hA/640?wx_fmt=png)

根据上面代码可画出下图内存映射，"entry\_point"这里为内存加载地址"load\_address"而不是代码入口点，Qiling会根据entry\_point和ram\_size大小分配一块内存，然后将代码code写入，需要注意的是默认初始栈寄存器SP指向这块内存end\_address - 0x1000的位置，如果模拟运行前不做修改，需要将ram\_size预留出一定的栈空间的大小，不然往栈内存写数据时会覆盖code内存数据。堆内存heap的起始地址就是entry\_point + ram\_size，下图虚拟线表示默认不会直接映射堆内存，如果需要使用这块内存，需要先执行ql.os.heap.alloc(size)来使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mAkf8AoOzUo641nRqZn9cMfdpxt7OyTQF1CibgzDwxldZZicEOH9am7IQ/640?wx_fmt=png)

接下来就可以生成配置文件了，代码如下：

```
# 加载地址load_addr=0x8000000 # 栈大小stack_size = 0x20000 # 堆大小heap_size = 0x20000 # 计算固件大小 0x1000对齐fw_size = math.ceil(len(fw)/0x1000)*0x1000 # 初始分配的内存大小包括 固件和栈空间大小，+0x1000是为了使可用的栈大小与stack_size保持一致ram_size = fw_size + stack_size + 0x1000 cfg_str = f"""[CODE]ram_size = {ram_size}entry_point = {load_addr}heap_size = {heap_size}[MISC]current_path = /"""# 保存配置文件with open('ql-config.ql', 'w') as fp:    fp.write(cfg_str)
```

接着，仿照样例生成Qiling对象，代码如下，因为这里模拟运行的用到了thumb指令，所以需要指定参数thumb=True。因为这里默认模拟的是小端序，而固件恰好是小端序固件，所以可以不指定端序，但是如果模拟的为大端序的固件，则需要指定参数endian=QL\_ENDIAN.EB。更多参数用法详见官方文档。

```
ql = Qiling(code=fw, archtype="arm", ostype="blob", profile="ql-config.ql", thumb=True)
```

定义模拟运行的起始地址和终止地址，这里因为只模拟运行sub\_800E288函数，所以设为sub\_800E288函数起始地址和终止地址即可。

```
begin =0x800E288end = 0x800E296
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mMib21lhCl7yibZSmjBv7w3yBxPzuOYAWWHiaMvrRpUDAb4O8ASYnHbpPg/640?wx_fmt=png)

因为模拟的sub\_800E288函数有3个参数，所以还需要给函数传参。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mliab1gS6NukiciaiaaN8Z7nxQDUSJ94Y3BtsWaKxLICeJIt2uZqicYrZ09Q/640?wx_fmt=png)

这里简单介绍下ARM中常见的函数传参规范：对于函数参数不超过4个参数时用r0，r1，r2，r3寄存器来传参，对于函数参数超过4个参数时，前4个依旧用r0，r1，r2，r3寄存器传参，往后的参数以压入栈的方式传参。类似地函数如果有返回值，约定以r0寄存器返回。这些规范主要是为了不同程序或模块之间相互调用各自的函数而不出错，因为是规范，所以也就可以不遵循这个规范，比如说你自己用汇编写的程序的话，想怎么传参就怎么传参，只要你自己不限入混乱，程序不出错即可。

废话不多说，回到正题，这里获取unicorn对象来为函数传参（unicorn对象可以读写各个寄存器）。从上面可知，需要模拟的函数的3个参数都是指针，所以需要给r0，r1，r2 这3个寄存器写入3个内存地址，而初始SP寄存器（栈寄存器）和heap之间有块0x1000的内存没有用到，因此这里可以用sp+0x100，sp+0x200，sp+0x300，这3个地址作为函数参数传入。不过单单将3个地址写入r0，r1，r2寄存器还不够，还要在相应地内存写入数据，这样才是完整的传参过程。因为第3个参数是加密结果的输出，所以可以不往该地址写数据。如下代码，为r0传入密钥"BA 2F 96 A9 BA 2F 96 A9 BA 2F 96 A9 BA 2F 96 A9"，为r1传入明文"10 BE 62 F8 E8 DC 34 46"。

```
sp = ql.arch.regs.sp uc=ql.uc #为第1个参数key传参uc.reg_write(UC_ARM_REG_R0, sp+0x100)uc.mem_write(sp+0x100, bytes.fromhex("BA 2F 96 A9 BA 2F 96 A9 BA 2F 96 A9 BA 2F 96 A9")) #为第2个参数in传参uc.reg_write(UC_ARM_REG_R1, sp+0x200)uc.mem_write(sp+0x200, bytes.fromhex("10 BE 62 F8 E8 DC 34 46")) #为第3个参数out传参uc.reg_write(UC_ARM_REG_R2, sp+0x300)
```

然后是启用debugger，Qiling默认是不启用debugger的，如下代码，启用gdb debugger并监听相应IP和端口。详细说明见官方文档：*https://docs.qiling.io/en/latest/debugger/*

```
ql.debugger = 'gdb:0.0.0.0:9999'
```

在qiling-1.4.4中，设置了debugger后且ostype为"blog"的情况下，直接运行ql.run会报"AttributeError: 'QlOsBlob' object has no attribute 'fs\_mapper'"错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mZ90mCficA1gn1RLb6RzYYMNMM7g9SVP1FvJ7UHociaYB1wHBvpnwlhMQ/640?wx_fmt=png)

在源码中找到了相应的描述，如下图，QlOsBlob类中有几个函数还没有实现，详见：qiling/os/blob/blob.py（*https://github.com/qilingframework/qiling/blob/master/qiling/os/blob/blob.py*）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6micNUS89YNQswmUrnHdVrqrqHQWtm4tfGhMB12XoxeMca1D2p5LrJk2g/640?wx_fmt=png)

不过好在，经过测试，在执行ql.run之前，可以按以下方式，规避下这个问题。这段代码作用很简单，就是给个空壳给ql.os.fs\_mapper。Python一个非常好的特性就是可以像下面这样，可以很容易地对各种库进行动态修改，而不用去修改库的原文件。下面这部份代码，等以后Qiling有相应的函数实现后就不在需要了。

```
class MyMapper:    def add_fs_mapping(self, ql_path, real_dest):        pass ql.os.fs_mapper = MyMapper()
```

重新运行后，出现如下信息，说明成功模拟运行，并启用了debugger并监听了相应的IP和端口。需要注意的是，如果在生成Qiling对象是指定了参数verbose=QL\_VERBOSE.OFF，那么运行时不会有任何log信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mUVeZFLkicCll9pLetrc34HF6VIDdHhrmFbTgH05JIkNt5nl6KpDdtIw/640?wx_fmt=png)

接下来，介绍IDA中如何连接到这个server进行动态调试。

IDA中选择Debugger > Select debugger或者快捷键F9，选择Remote GDB debugger。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mTsdcA1xS2UhwZuBDUfibvhjbbricUJaaNSDibVU2fYephsv5XLlMy9JmA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m0kiccWlXTSqVaYaMcHc2peFI2ibEustoNcbUNbe7q9oWINA13fdmJU1A/640?wx_fmt=png)

选择Debugger > Process options。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m3QRtGDPXSXavAd4fv1UlDC6eKLgJVPsYa36O9DdHNIuw2LlE3VC4UA/640?wx_fmt=png)

输入运行Qiling机器的IP和端口，如果运行Qiling和IDA是同一机器同一系统内，则IP填127.0.0.1即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mJ33Jpo5HugZze8WmgMWj4rs4BEdU09XW0RAApZdsSfaQkXPWJQGf6A/640?wx_fmt=png)

接着选择Debugger > Debugger options。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mBia6s5qTJdDne6YZibmeNN7MlsDeKLVIq36CZTJ4QY398W4rfmXTOqng/640?wx_fmt=png)

勾选如下两个即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mKbYrRWLjibKNZYaI36fxlViahFyibwicbEACaY2YNlCZREEXIGWf0NwV3g/640?wx_fmt=png)

然后选择Debugger > Manual memory regions。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mMFG284SibNUh05cglza9boLTR3uJo6ENwCRwox4xZdY8ibyDDD8ib1xVQ/640?...