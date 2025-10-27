---
title: 记一次攻防样本——shellcode分析
url: https://forum.butian.net/share/3817
source: 奇安信攻防社区
date: 2024-10-22
fetch_date: 2025-10-06T18:45:31.850797
---

# 记一次攻防样本——shellcode分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 记一次攻防样本——shellcode分析

* [安全工具](https://forum.butian.net/topic/53)

书接上文，笔者发的一篇对某红队钓鱼样本分析的文章：《记一次（反虚拟+反监测+域名前置）钓鱼样本分析及思考》
本文主要针对上文中样本使用的shellcode展开分析，非常详细的记录了笔者分析该shellcode过程；以及对其使用的相关技术进行分析拆解；

0x01 背景
=======
书接上文，笔者发的一篇对某红队钓鱼样本分析的文章：[记一次（反虚拟+反监测+域名前置）钓鱼样本分析及思考](https://forum.butian.net/share/3701);
本文主要针对上文中样本使用的shellcode展开分析，非常详细的记录了笔者分析该shellcode过程；以及对其使用的相关技术进行分析拆解；
0x02 分析
=======
对于shellcode我们首先可以通过一些模拟器来查看其内部的大致函数调用情况，然后有针对性的开展分析；
一、自动化模拟分析探虚实
------------
笔者一般使用speakeasy这款工具，`https://github.com/mandiant/speakeasy`
模拟运行的结果如下图：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6f3189b2366f92e3cd6fff62988697fa82955b3c.png)
如上，可以看到这个样本前面做的一些动作，拿到几个关键函数的调用地址，其中比较明显特征的有：CreatFileMappingA、MapViewOfFile，后面也调用了这两个函数，结合我们dump下来的shellcode文件大小（3百多kb），不难看出里面应该是藏了一个pe文件，这里的逻辑是把藏于其中的pe文件从文件格式映射成内存格式，并且还调用了VirtualProtect来修改内存权限属性，应该是要修改相关数据；
在大致知道了这个情况之后，我们可以做一些尝试，比如直接去dump下来的shellcode文件里面找，是否存在相关pe文件：
二、妙计上心头直捣黄龙
-----------
我们在dump下来的shellcode文件里面查可执行文件：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d61207fe40f0b2585cc27ada80067bead60f2d86.png)
上图是我们查看shellcode中pe文件dos头的情况，可以发现有一个`4d5a`开头的地方，但是0x3c偏移，以及后面的pe头都没有，所以大概率不是；也有可能是：是，但是其他数据被加密了，需要动态解密还原出来，然后才去拉伸；所以这里我们尝试走捷径失败；
三、老老实实正常分析
----------
那没办法就直接怼dump的文件把：
如下，可以看到，上来第一部分就是调用`sub\_188e6`（这个地址是内置的一个相对地址+获取的运行时绝对地址拿到的和call $+5,pop 操作类似），然后下面的第二部分就是传入几个参数，调用第一部分返回的rax函数，r8d传入的像是特征码；（和CobaltStrike有点像，但是前面头不符合，并且没有出现pe文件头的特征）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2223660327b169598ff2b92fa0f94bbd3a6db12e.png)
我们跟进`sub\_188e6`,直接ida f5看逻辑（一般来说分析shellcode的时候是没有比较逐字节扣的，能f5直接f5即可，但是有些做了编码壳的shellcode还是需要先简单分析壳逻辑，动态调试脱壳后再f5即可；例如：之前[笔者分析的一个带编码壳的shellcode](https://minhangxiaohui.github.io/2024/07/15/%E6%9F%90%E5%A4%A7%E5%8E%82%E7%BA%A2%E9%98%9F%E9%92%93%E9%B1%BC%E6%A0%B7%E6%9C%AC%E5%88%86%E6%9E%90/) 中的shellcode）
如下图，上来第一部分对一个v13数组变量进行构造赋值操作，然后第二部分调用`sub\_18c66`对v9变量进行赋值：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b4e7f305bf874a4ad84ee30a981d746a81e3a7b7.png)
### 找PE
跟进`sub\_18c66`，其实现如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-c3ae7dca4efe2eb4fe07c38c9c366d4d229b1f88.png)
简单转化下出现数据的编码：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-207229c904ee24ca05b327893ee943a746466ebe.png)
上图，我们可以直观的看出，做了一个递减的循环，寻找当i对应地址的WORD为`YA`的时候，并且其0x3c偏移处的值在`0x40-0x400`之间，并且i+（0x3c偏移处地址的值）的地址对应值的WORD为`0x4a51`(JQ)的时候，i的值；
i的起始取值来自`sub\_18b66`，如下，该函数就是返回函数的返回值；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-17efc61e6dfae32a763dab894cdba9dd961ebcac.png)
所以我们简单总结就知道了v9的赋值函数`sub\_18c66`,其实就是从函数的返回地址开始，往前找，找到一个符合上述分析条件的地址；并且我们稍加留意可以看到条件当中出现了0x3c这个敏感偏移；这不就是回溯找PE文件位置吗，只不过这里攻击者做了特征隐藏，DOS头的MZ到这里变成了AY，PE头的PE到这里变成了QJ；（难怪刚刚我们上面查pe文件的时候没找到）
按照这个逻辑我们再次查看shellcode的二进制文件，如下图可以看到就是在刚开始的地方；（结合上面我们直接分析的开头代码，这里有点像反射dll加载，但是又不全是，因为做了一些改良，往前面头部加了一些lj代码）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ec83b923cb66522995f85a07e35e67ec28d2cd46.png)
然后我们回到`sub\_188E6`的主逻辑上；
如下：先是对v13数组前两个元素做一个条件判断（这个条件肯定是成立的，上面的赋值就是直接这样赋值的，取低32位，比较也成立，所以这里就是一个恒真式），接着调用`sub\_18cf6`传入v13变量地址；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b16d44bb4eddf07b6757b536d62583a7bb9514a2.png)
### peb找函数地址
跟入`sub\_18cf6`函数：
其实现如下：
```php
\\_\\_int64 \\_\\_fastcall sub\\_18CF6(\\_QWORD \\*a1)
{
 int v1; // eax
 \\_\\_int64 result; // rax
 \\_\\_int16 v3; // \[rsp+0h\] \[rbp-68h\]
 unsigned \\_\\_int16 v4; // \[rsp+0h\] \[rbp-68h\]
 \\_\\_int64 v5; // \[rsp+8h\] \[rbp-60h\]
 int v6; // \[rsp+10h\] \[rbp-58h\]
 unsigned int \\*v7; // \[rsp+18h\] \[rbp-50h\]
 int v8; // \[rsp+20h\] \[rbp-48h\]
 int v9; // \[rsp+20h\] \[rbp-48h\]
 \\_\\_int64 \\*i; // \[rsp+28h\] \[rbp-40h\]
 unsigned int \\*v11; // \[rsp+30h\] \[rbp-38h\]
 unsigned int \\*v12; // \[rsp+38h\] \[rbp-30h\]
 unsigned \\_\\_int8 \\*xx\\_address; // \[rsp+40h\] \[rbp-28h\]
 \\_BYTE \\*v14; // \[rsp+48h\] \[rbp-20h\]
 unsigned \\_\\_int16 \\*v15; // \[rsp+50h\] \[rbp-18h\]
​
 for ( i \= \\*(\\_\\_int64 \\*\\*)(\\*(\\_QWORD \\*)(\\_\\_readgsqword(0x60u) + 0x18) + 0x20i64); i; i \= (\\_\\_int64 \\*)\\*i )
{
   xx\\_address \= (unsigned \\_\\_int8 \\*)i\[10\];
   v3 \= \\*((\\_WORD \\*)i + 0x24);
   v8 \= 0;
   do
  {
     v9 \= \\_\\_ROR4\\_\\_(v8, 13);
     if ( \\*xx\\_address < 97u )
       v1 \= \\*xx\\_address;
     else
       v1 \= \\*xx\\_address \- 0x20;
     v8 \= v1 + v9;
     ++xx\\_address;
     \--v3;
  }
   while ( v3 );
   if ( v8 \== 0x6A4ABC5B )
     break;
}
 v5 \= i\[4\];
 v11 \= (unsigned int \\*)(\\*(unsigned int \\*)(\\*(int \\*)(v5 + 0x3C) + v5 + 0x88) + v5);
 v12 \= (unsigned int \\*)(v11\[8\] + v5);
 v15 \= (unsigned \\_\\_int16 \\*)(v11\[9\] + v5);
 v4 \= 6;
 while ( 1 )
{
   result \= v4;
   if ( !v4 )
     break;
   v14 \= (\\_BYTE \\*)(\\*v12 + v5);
   v6 \= 0;
   do
     v6 \= (char)\\*v14++ + \\_\\_ROR4\\_\\_(v6, 13);
   while ( \\*v14 );
   if ( v6 \== 3960360590
     || v6 \== 2081291434
     || v6 \== \-1850750380
     || v6 \== 2034681371
     || v6 \== 122922236
     || v6 \== \-751679228 )
  {
     v7 \= (unsigned int \\*)(v11\[7\] + v5 + 4i64 \\* \\*v15);
     switch ( v6 )
    {
       case \-334606706:
         a1\[2\] \= \\*v7 + v5;
         break;
       case 2081291434:
         a1\[1\] \= \\*v7 + v5;
         break;
       case \-1850750380:
         a1\[4\] \= \\*v7 + v5;
         break;
       case 2034681371:
         a1\[5\] \= \\*v7 + v5;
         break;
       case 122922236:
         a1\[3\] \= \\*v7 + v5;
         break;
       default:
         \\*a1 \= \\*v7 + v5;
         break;
    }
     \--v4;
  }
   ++v12;
   ++v15;
}
 return result;
}
```
可以明显看出，函数`sub\_18cf6`存在两部分，第一部分是一个for循环，第二部分是一个while循环：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d50e521734c29ee7f0a3ef3b45f7888d104d3099.png)
我们先不着急分析详细逻辑，我们先在看下大的方面这个函数大概率是用来干啥的，首先我们从主函数的`sub\_188E6`看，其调用这个`sub\_18cf6`是没有获取其返回值的，其次传入的是一个指针；
然后我们结合`sub\_18cf6`内容，先看下哪里对传入的指针做了处理，如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-1d26dd83d209e569f720de92669a13186474771a.png)
上图中可以看到，在`sub\_18cf6`的第二部分while循环里面，对指针指向的数组的几个元素做了赋值操作；所以分析到这，我们也不难看出这个函数其实就是在给主逻辑函数里面的v13变量（指向数组首地址的指针）赋值；
然后我们再来看`sub\_18cf6` 里面两部分详细逻辑：
第一部分：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6b8f45133edb78d283f0b072272e06b104dda893.png)
上图首先通过fs拿peb拿ldr\\_list,遍历list，拿basedllname
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-91af90450731716fd57f3c6ce5ac9af72a92aca4.png)
接着，计算计算dllbasename的特征码（特征码算法：name，逐位小写转大写累加上次结果，结果循环右移13位），找到结果是`0x6a4abc5b`的这个特征码就结束；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-00b0419d7e96cf5bbf2044db1ae4bad816c7f4de.png)
然后获取dllbase地址和以及获取导出表地址，i\[4\]就是0x20的相对偏移（相对InMemoryOrderLinks内存加载顺序列表），对应的就是dllbase；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-eba29bd72dd26ba8f56dcf6554e56d373a8dcbac.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ca722b81aa4e0676a9f0b4570d663bdc9e0d9a63.png)
接着取导出函数名称表、导出函数序号表：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-c8ba9b9bbcab411101af048039e66e42f9ef4901.png)
![image.png](https://cdn-yg-zzbm.yun.qi...