---
title: 一种对无符号VxWorks固件系统的符号恢复方法研究
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499692&idx=1&sn=a2db5a740083022c15b91dca075288e8&chksm=fa522a12cd25a304a9f4e6e4ba7d04cbf6172d868c581eb12b8587ecbec81b3954ad16366864&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-01-31
fetch_date: 2025-10-04T05:14:33.363493
---

# 一种对无符号VxWorks固件系统的符号恢复方法研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7WiaDk97Q0Wfm0XMictGwgibvBnnwk52WKvXScgfcFeGYzicbeH6NzCV6pQ/0?wx_fmt=jpeg)

# 一种对无符号VxWorks固件系统的符号恢复方法研究

unr4v31

山石网科安全技术研究院

**‍‍‍‍‍‍‍‍‍‍**

在前面两篇关于VxWorks设备固件的提取和VxWorks系统加载地址分析的文章之后，我们对VxWorks函数符号的恢复方法进行了研究，找到了一种对无符号VxWorks固件系统的符号恢复方法。

**1.****符号文件 ‍‍‍‍‍**

首先要知道，VxWorks使用的是一种外部符号文件，它不像我们通常的ELF文件中的符号和ELF共存，VxWorks的符号文件在固件中能找到的话最好不过了，找不到也是没有办法的事情，本来VxWorks也不开源。

如何知道固件系统中VxWorks是否有符号文件？

通过Google我们搜索到了VxWorks的一些开发者手册，在其中找到了一段话：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7lfQ4xpodnKhomT6ZXib83OBRoPo9QY1ibfgzRpuygGQmU1X8icyk0e9SA/640?wx_fmt=png)

这里我们得知usrInit()函数用于初始化栈，可以在binwalk解包出来的文件夹中，查找含有usrInit字符串的文件，如果文件存在，则表示包含外部符号文件，反之则不包含。其他还可以尝试比如bzero、bfill字符串。如果没有符号也不要紧，这正是本篇所要介绍的内容。

非常幸运的是，我们在之前28个不同路由器固件中，发现了ARM和MIPS架构的带符号信息的VxWorks固件，接下来介绍如何利用外部符号文件和IDAPython来恢复符号信息。

符号文件内容如下面两张图，其中包含了一些条目信息，以及函数名称字符串：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7ZhVmpgmww6jkKayL0sZouLNuoEC63szV7u3HW1kj2KfM4Ne9NCrawA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7KSh0CoADMjYRicsdl0srq0rzQAP5icWlM52XZibXzuzWqzIiaC5CQSabfw/640?wx_fmt=png)

接下来探索符号文件的格式。每个外部符号文件的开头4字节表示当前符号文件大小，比如这个符号文件大小为181551字节，用十六进制表示刚好是0x2c52f：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D796Z1LxSn2RrESicBlHBffuZwiaL5ib3dJvniaRXWavFpfwZwMFK877vMmw/640?wx_fmt=png)

紧邻的4字节表示符号条目数，然后每8字节为一个条目信息：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7zbaicVY6CZj5f9OqMV5Kdm56UarE89N3uZHugB2np6A8mXICickiczyIQ/640?wx_fmt=png)

这里说一下条目数是怎么观察来的，每8字节为一个条目信息，我们可以把条目数量乘8，得到条目结束位置，条目结束位置肯定是会有一些与条目信息不同的特征，以此来猜测这个数值就是表示条目数量。首先0x1b5c \* 8 = 0xdae0位置：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7BrLOcfic7DtQgK0lBghHzuRgphb7bXV4A8H7w3bJVLwdqJk2yrn1nfQ/640?wx_fmt=png)

我们跳转到文件中0xdae0位置，观察到明显从之前的条目特征变为字符串特征，这里加上8字节是因为要加上文件开头的8个字节的文件信息，刚好就是函数名称字符串开始的位置：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7O8NGLMeCeFhvVj50aHrVFA1IpWHGcAHia4xK7aibPbduKNVhW24mHlkg/640?wx_fmt=png)

接下来对每个条目信息进行解读。每8个字节被分为3部分，如下图，单字节的0x54，ASCII字符“T”，表示符号类型；紧邻3个字节表示从函数字符串开始位置的偏移；最后四字节表示在VxWorks中的地址，很明显是加上了加载基址后的地址：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D76hKGCdvLovuYvtqrdEwCksR4n658vicJjKrWT33ibd1XxF8uWdTMrIbA/640?wx_fmt=png)

用结构体表示如下：

```
struct sym_info{
 char type;
 char offset[3];
 unsigned int address;
};
```

符号类型和ELF文件中所表示的符号类型相同，也就是我们使用`readelf -s`也会输出符号类型，所有符号类型表示如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7D5dxRShDKnSL5ndadwuDicXibmY47WNVbVF13VEbxiczDc42yfWZT1p3g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D75a77ibwFcnDcicpWGE9RFk6kYqBvsp7Idd5ISOPRhcu6yGosETPd7NTg/640?wx_fmt=png)

值得注意的是“T”类型、“B”类型和“D”类型在符号文件中是最多的，那么我们只要按照不同的类型进行命名即可。

**2. 符号恢复****‍‍‍‍**

上一步得知了符号文件中信息所表示的意义之后，只需要查阅IDAPython API手册，然后解析出符号，编写脚本即可完成符号解析工作。完整脚本如下：

```
# coding=utf-8
# IDA Pro 7.6
# IDA Python3 API

import ida_ua
import ida_funcs
import idc
import struct
import os

sym_file = "/path/to/symbol/file"
vxworks_file_name = "/path/to/vxworks/file"
load_addr = 0x40205000

file_size = os.path.getsize(vxworks_file_name)
ROM_end_addr = file_size + load_addr

def find_sym_str(offset):
    index = 0
    while True:
        if str_table[offset+index] != 0:
            index += 1
        else:
            break
    return str_table[offset: offset+index]

def u32(data):
    '''Big endian'''
    return struct.unpack(">I",data)[0]

with open(sym_file, 'rb') as f:
    sym_file_contents = f.read()

sym_file_size = u32(sym_file_contents[:4])
sym_count = u32(sym_file_contents[4:8])

sym_table_start = 8
str_table_start = sym_count * 8 + 8

sym_table = sym_file_contents[sym_table_start: str_table_start]
str_table = sym_file_contents[str_table_start: ]

sym_results = []

for i in range(0, sym_count * 8, 8):
    single = sym_table[i: i+8]
    sym_type = single[0]
    sym_str_offset = u32(b'\x00'+single[1: 4])
    sym_func_addr = u32(single[4: ])
    sym_name = find_sym_str(sym_str_offset)

    sym_results.append((sym_type, sym_str_offset, sym_func_addr, sym_name.decode('utf-8')))

def makecode(addr, name, flag):
    ida_ua.create_insn(addr)
    ida_funcs.add_func(addr)
    idc.set_name(addr, name, flag)

def my_parser():
    for sym_type, b, sym_func_addr, sym_name in sym_results:
        if sym_type == ord('T'):
            # global function name
            makecode(sym_func_addr, sym_name, idc.SN_CHECK)
            # pass

        elif sym_type == ord('t'):
            # local function name
            makecode(sym_func_addr, sym_name, idc.SN_LOCAL)
            # idc.set_name(sym_func_addr, sym_name, idc.SN_LOCAL)
            # pass

        elif sym_type == ord('A'):
            pass

        elif sym_type == ord('B'):
            idc.set_name(sym_func_addr, sym_name)
            # pass

        elif sym_type == ord('D'):
            idc.set_name(sym_func_addr, sym_name)
            # pass

        else:
            print(chr(sym_type))

def check_segment():
    address_list = []
    for sym_type, b, address, d in sym_results:
        if sym_type == ord('B'):
            address_list.append(address)

    address_list.sort()

    # check the address
    value = u32(idc.get_bytes(address_list[-1], 4))
    if value != 0xffffffff:
        return

    # calc bss end address
    bss_start = (ROM_end_addr + 0x1000) & 0xfffff000
    bss_end = (address_list[-1] + 0x1000) & 0xfffff000

    # create bss segment
    idc.AddSeg(bss_start, bss_end, 0, 1, idaapi.saRelPara, idaapi.scPub)

if __name__ == "__main__":
    check_segment()
    my_parser()
```

恢复效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7Xevy7Eqbeb75EJ1HVMSjjibpciafib7G1BGFEgcOiczhTQfXd7ZHB9eNyg/640?wx_fmt=png)

以上是对于有符号文件的恢复方式，对于无符号的恢复，需要借助Rizzo插件。Rizzo插件是由devttys0编写的一款专用于VxWorks系统的启发式函数恢复插件。

查阅其源码，其实现逻辑是通过已有符号的VxWorks文件，经过Python的pickle库将地址、对应的函数名称等信息序列化之后，输出为\*.riz文件。当需要识别函数的时候，通过Rizzo插件加载riz文件，将地址、对应的函数名称信息反序列化，然后通过IDA Python的接口对函数重命名，以此来达到恢复函数名称的目的。下图是通过符号表恢复后的VxWorks，生成riz文件后再用Rizzo进行符号恢复的效果：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTPSTS6iavndPEuZw4JVr4D7exo6BfEt9cDbRGClf4a3KqLmA12Eaz7G6ttvh3nrmf2gTxKoDnSUFg/640?wx_fmt=png)

可以看到的是基础函数例如strcpy、strcmp等函数都已经恢复得比较好了，对于我们漏洞挖掘是完全够用了。

而Rizzo并不是万金油工具，经过我们的尝试，不同架构间的VxWorks文件无法使用Rizzo来进行函数符号恢复，虽然VxWorks中函数的CFG图变化不大，但ARM只能用于ARM，MIPS只能用于MIPS架构的符号恢复，这就需要我们手上需要准备好一个有符号的MIPS或ARM架构的VxWorks，当然架构越多越好。

**3. 研究过程中尝试过的方法** **‍‍‍‍**

我们在研究过程中，在没有发现带符号的VxWorks之前，花费了大量时间，尝试了多种可能有用的方法，并得到一些结论：

\* IDA flair插件无法使用于此场景，原因为：无法找到VxWorks源码然后通过FLIRT生成sig文件来进行恢复。此插件只适用于标准的windows或Linux系统库函数的识别。

\* 经过测试，aliyun IDA Finger插件无法完成此功能，无法对函数进行识别，甚至无法识别ARM架构下已有的符号信息，只适用于标准库函数的识别。

\* 这里尝试了一种方法，通过buildroot编译不同的交叉编译工具，然后利用泄露的VxWorks 5.5.1代码对某些函数进行编译，来和固件中的汇编代码进行比对查看差异，试图通过这张方式来恢复函数名称。这里尝试了gcc 4.5.x 到 gcc 10.x 版本的工具，结果不尽人意，高低版本的gcc只存在栈的差异，汇编指令都是相同的，和固件中的汇编指令差异太大，无法通过这种方式来达到目标。并且这种方式就算是可行，但也过于依赖源码，对于没有泄露的VxWorks版本没有任何办法。

其他可能有用的识别方法：

\* 初步研究过程中，只需要对一些如memset、memcpy、strcpy、printf等基础函数的识别，可以通过其参数特征和返回值特征对其进行判断。这里举个两个例子，比如strcpy会将参数二位置的内容拷贝到参数一所在的内存，并且以0作为循环结束标识，返回一个字符串指针，通过这三个条件总结出约束条件，再通过泄露的源码对约束条件进行修饰，比如变量个数的准确性，参数的准确性等等，再通过模拟执行等方式，将整个函数块通过unicorn模拟，执行结束后判断参数一是否等于参数二的内容，那么就可以断定此函数是strcpy。printf函数作为可变参数的函数，其内部实现比较复杂，并且模拟执行可能不会像正常函数那样输出一些字符串到终端，但可以肯定的是，printf必须带有一个字符串参数，即参数一，在printf内部判断字符串结尾必定以0结束，并且字符串可能是格式化字符串带有“%”等特征，因此只需要判断函数是否符合printf可变参数长度特征，并且包含字符串特征，但不排除一些其他特征来进行识别。

\* 通过VxWorks错误代码编号来确定报错位置，确定报错函数，然后通过报错函数的上下文进行分析，找到打印输出函数，以此方法进行识别。错误代码参考此链接：https://ppiazi.tistory.com/entry/Vxworks-Error-Codes ，识别效果还需要试验考量。

**Reference** **‍**

https://www.uio.no/studier/emner/matnat/fys/FYS4220/h11/undervisningsmateriale/laboppgaver-rt/vxworks\_architecture\_supplement\_6.2.pdf

https://www.hex-rays.com/products/ida/support/idapython\_docs/

https://github.com/fireundubh/IDA7-Rizzo

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib6...