---
title: VMPWN的入门级别题目详解（一）
url: https://www.secpulse.com/archives/202880.html
source: 安全脉搏
date: 2023-08-05
fetch_date: 2025-10-04T12:00:18.588093
---

# VMPWN的入门级别题目详解（一）

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

# VMPWN的入门级别题目详解（一）

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-08-04

23,545

# 实验一 VMPWN1

## 题目简介

这是一道基础的VM相关题目，VMPWN的入门级别题目。前面提到VMPWN一般都是接收字节码然后对字节码进行解析，但是这道题目不接受字节码，它接收字节码的更高一级语言：汇编。程序直接接收类似”mov”、”add”之类的指令，可以把这道题目看作是一个执行汇编语言的处理器，相比于解析字节码的VM，逆向难度要大大减小。非常适合入门。

## 题目保护检查

![pCcrZSH.png](https://s1.ax1x.com/2023/07/07/pCcrZSH.png)

只有Partial RELRO保护，这意味着可以修改程序的重定位表；没有开启PIE保护，那么程序每次加载到内存中的地址都不会发生变化。

## 漏洞分析

拖进IDA分析流程

![pCcr1k8.png](https://s1.ax1x.com/2023/07/07/pCcr1k8.png)

程序模拟了一个虚拟机，v5，v6，v7分别是stack段，text段和data段。看到alloc\_mem这个函数

![pCcr8fg.png](https://s1.ax1x.com/2023/07/07/pCcr8fg.png)

Malloc一块小内存ptr，然后参数a1是要分配的内存的大小，一个单位是8字节。根据伪代码中对ptr的赋值可以构造出一个结构体，如下

```
struct seg_chunk
{
  char *seg;
  int size;
  int nop;
};
```

再看到alloc\_mem函数会直观很多

![pCcrYlj.png](https://s1.ax1x.com/2023/07/07/pCcrYlj.png)

但是这样依然有一些难以理解，我们使用GDB打开程序进行调试，看到如下图所示

![pCcrt6s.png](https://s1.ax1x.com/2023/07/07/pCcrt6s.png)

![pCcrNXn.png](https://s1.ax1x.com/2023/07/07/pCcrNXn.png)

存在多个0x20大小的小堆块，堆块中的开头8字节指向下方的大堆块，第8到第12字节则是大堆块的大小的单位数量，比如0x400=0x80\*0x8，单位长度为8字节，后面的0xffffffff暂时不知道作用，可能只适用于占位。因此根据gdb的显示结果，我们重新创建一个结构体，如下

```
struct manage_chunk
{
  unsigned __int8 *chunk;
  unsigned int unit_num;
  int unknow;
};
```

继续看到main函数， 接着会让用户输入程序名

![pCcramq.png](https://s1.ax1x.com/2023/07/07/pCcramq.png)

分配好各个段之后，然后让我们输入指令，先写到一个0x400的缓冲区中

![pCcrDtU.png](https://s1.ax1x.com/2023/07/07/pCcrDtU.png)

然后再写到text段中，store\_opcode函数如下

![pCcryp4.png](https://s1.ax1x.com/2023/07/07/pCcryp4.png)

函数接受两个参数，a1为text段的指针，a2为缓冲区的指针，strtok函数原型如下：

```
char *strtok(char *str, const char *delim)

str -- 要被分解成一组小字符串的字符串。

delim -- 包含分隔符的 C 字符串。

该函数返回被分解的第一个子字符串，如果没有可检索的字符串，则返回一个空指针。
```

程序中的delim为**\n\r\t**，**strtok(a2, delim)**就是以**\n\r\t**分割a2中的字符串

由下面的if-else语句我们可以知道程序实现了**push,pop,add,sub,mul,div,load,save**这几个功能，每个功能都对应着一个opcode，将每一个opcode存储到函数中分配的一个临时data段中(函数执行完后这个chunk就会被free掉)

【---- 帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：yj009991，备注 “安全脉搏” 获取！】
① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

sub\_40144E函数如下：

![pCcr61J.png](https://s1.ax1x.com/2023/07/07/pCcr61J.png)

这个函数是用来将函数中的临时text段的指令转移到程序中的text段的，每八个字节存储一个opcode，每存储一个指令，就会对unknow进行加1的操作。我们将这个函数重名为`set_value`。

需要注意的是，这里存储opcode的顺序和我们输入指令的顺序是相反的(不过也没啥需要注意的，反正程序是按照我们输入的指令顺序来执行的)。

write\_stack函数如下：

![pCcrW0x.png](https://s1.ax1x.com/2023/07/07/pCcrW0x.png)

和store\_opcode函数相比就是去掉了存储opcode的环节，将我们输入的数据存储在stack段中。

我们再看到execute函数

![pCcrf76.png](https://s1.ax1x.com/2023/07/07/pCcrf76.png)

![pCcr71H.png](https://s1.ax1x.com/2023/07/07/pCcr71H.png)

一个很大switch选择语句，看到sub\_4014B4函数

![pCcrXHP.png](https://s1.ax1x.com/2023/07/07/pCcrXHP.png)

将a1中seg内的值给到a2，unknow每次都会减一，而a1是text段的指针，所以这个函数就是从text段中取指令，将其重命名为take\_value。

对于set\_value函数而言，每次会将unknow加1，而对于take\_value而言，每次会将unknow减1，因此我们在这里可以猜测unknow是当前的数据的数量，因此重新定义结构体

```
struct manage_chunk
{
  unsigned __int8 *chunk;
  unsigned int unit_num;
  int num_now;
};
```

看到case0x11对应的函数sub\_401AAC

![pCcrz4S.png](https://s1.ax1x.com/2023/07/07/pCcrz4S.png)

调用了take\_value函数和sub\_40144E函数，sub\_40144E如下

![](https://pic.imgdb.cn/item/64a7ecdd1ddac507cc6ea5eb.png)

将a2放入a1的seg中，和take\_value的操作相反，所以我们将其命名为set\_value。整体看来就是这样子的，如下图所示

![](https://pic.imgdb.cn/item/64a7ecf51ddac507cc6eed0b.jpg)

从stack中取值，然后将值存入data中，所以这里的操作我们可以理解为pop，因此我们将sub\_401AAC重命名为pop。

再看到sub\_401AF8函数

![](https://pic.imgdb.cn/item/64a7ed181ddac507cc6f5c2c.jpg)

从data中取出两个值，然后将这两个值相加存入data中，所以我们将其重命名为add。

看到sub\_401BA5函数

![](https://pic.imgdb.cn/item/64a7ed231ddac507cc6f7d1d.jpg)

很明显就是减法

再看sub\_401C06函数

![](https://pic.imgdb.cn/item/64a7ed2c1ddac507cc6f9e60.jpg)

这个函数是乘法

再看sub\_401C68函数

![](https://pic.imgdb.cn/item/64a7ed361ddac507cc6fba1e.jpg)

这个函数是除法

再看到sub\_401CCE函数

![](https://pic.imgdb.cn/item/64a7ed431ddac507cc6fe487.jpg)

稍微复杂了一点点，从data中取出一个值，然后以这个值为索引，从data中取值，将取出来的值载data中。我们将这个函数命名为load。

最后看到sub\_401D37函数

![](https://pic.imgdb.cn/item/64a7ed4c1ddac507cc700538.jpg)

这里取出两个值a2和v4，以a2为索引，将v4存入a2索引找到的内存中。将其命名为save。

至此，所有的操作都已经分析完毕，那么程序的漏洞在哪？ 注意看到load和save功能

![](https://pic.imgdb.cn/item/64a7ed551ddac507cc702054.jpg)

索引v3是从data段中取出来的，而data段的值是由用户输入的

![](https://pic.imgdb.cn/item/64a7ed621ddac507cc70478e.jpg)

通过push和pop以及加减乘除等操作可以控制data段中的数据，而在load中以data段中的数据为索引时又没有对其进行限制，所以这里存在一个越界读的漏洞，即我们只需要设置好data段中的数据，在使用load功能时就可以将不属于data段中的数据读取到data段中。

除了load中的越界读漏洞，在save操作中也存在漏洞

![](https://pic.imgdb.cn/item/64a7ed6f1ddac507cc706d73.jpg)

Save功能中从data段中取出两个值，然后将其中一个值作为data段的索引，从中取出一个值addr，将从data段中取出的另一个值存入addr指向的内存当中。这里没有对这两个值进行判断，也没有对addr进行任何判断，所以我们可以将任意值写入任意地址中，这里就存在一个越界写漏洞。

所以这个程序一共存在两个漏洞：越界读和越界写漏洞。

静态分析完毕，开始动态分析

存在越界读写的漏洞，该怎么利用？

由于程序没有开启FULL RELRO，所以我们可以复写got表，got中会存放有已经运行过的函数的加载地址，修改某个函数的got表的值就能够修改这个函数最终调用的函数地址。在这个程序中有如下函数

![](https://pic.imgdb.cn/item/64a7ed811ddac507cc709d04.jpg)

在这里我们选择将puts的got表中的值修改system函数的地址，为什么？

![](https://pic.imgdb.cn/item/64a7ed8b1ddac507cc70b181.jpg)

在程序的一开始让我们输入了一个程序名，然后execute运行结束后，会调用puts函数输出程序名，当我们将puts函数的got表的值修改为system函数的地址后，puts(s)就变成了system(s)，而如果我们输入的s的内容为/bin/sh，那么最终就会调用system(“/bin/sh”)。

注意到heap区上方

![](https://pic.imgdb.cn/item/64a7ed941ddac507cc70cf02.jpg)

Heap区上方就是程序的text段，text段中存有got表，有大量的libc的地址

![](https://pic.imgdb.cn/item/64a7edb41ddac507cc713455.jpg)

而程序本身没有输出功能，所以我们需要利用程序提供的功能进行写入加减运算。load和save功能都是在data段进行的，而且存在越界，它们的的参数都是data结构体的指针。

![](https://pic.imgdb.cn/item/64a7edc31ddac507cc716397.jpg)

而对data段进行操作都是通过存储在data结构体中的data段指针进行操作的，只要我们修改了这个指针，data段的位置也会随之改变，所以我们可以利用save的越界写漏洞，将data段指针修改到0x404000附近(也可以直接在data段进行越界读写，毕竟越界读写的范围也没有限定，不过这样计算起来会比较麻烦)。

我们将data段指针改写为stderr下方的一段无内容处，即0x4040d0。

这个操作对应的payload为

...