---
title: 记录一下从编译的角度还原VMP的思路
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458496476&idx=1&sn=0d9aec099c74dcf38b3fd4303d329e12&chksm=b18e9d5686f91440ac727420779fe68cd209b151b970036c1d11e6f2965e07ebda08af3fdae4&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-03-07
fetch_date: 2025-10-04T08:49:27.473813
---

# 记录一下从编译的角度还原VMP的思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hs2UeTibknNTXkSN2BibAcgY7Fc5p4hlqp8xib1WkqUPm5DI4HUKOBWwHSkkN8RWTaSI6ojhw9l7jXA/0?wx_fmt=jpeg)

# 记录一下从编译的角度还原VMP的思路

wx\_御史神风

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hs2UeTibknNTXkSN2BibAcgY5iaHpg6IhujcUY6LkjuQawuKxXp4mZj2N7GN5Ok4tNGXAgYuuJXaSwA/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：wx\_御史神风

#

```
一

摘要
```

##

## **1.1 关于代码优化与还原**

关于还原，我认为难点是工作量大，需要自动化提升效率。

还原和混淆是一对反义词，相同点是保证代码功能相近，不同是一个是使代码更易读，后者则相反。

而代码优化非常类似，也要保证代码功能相近，不同是减少代码的体积或运行速度。

所以我感觉还原和代码优化有很多共通点。然后尝试了一下从编译的角度去做自动化还原，这里分享一下思路，算是画一个不太完美的句号吧。

##

## **1.2 还原流程**

我的还原流程简单来说就三步：

① 识别汇编对应的语义（翻译虚拟机字节码）。

② 虚拟指令转换成C。

③ 二次编译，利用编译器优化。

第三步可以针对性的实现一些优化，因为vmp是一个基于栈的虚拟机，编译器的优化效果有限。

第一步是我做的比较多的一部分，在后面的实现过程会说具体思路。

#

#

```
二

实现过程
```

##

## **2.1 Handler语义识别**

这一步说的是怎么判断Handler对应的虚拟机指令。

###

### 2.1.1 浅谈VMP的CFG

Handler识别首先绕不开一个问题，怎么找到Handler？

关于VMP 3.X的架构这里简单说一下。

在VMP2中会有一个分发器，所有Handler的地址都存在一个数组中，很容易就能把所有Handler找出来；但到了3，分发方式变成从字节码中解码出下一条指令的地址。

###

### 2.1.2 模拟执行输出虚拟指令

目前分析到两种跳转方式：

```
mov regjmp reg
```

或

```
push regret
```

我的思路是模拟执行，遇到jmp reg或者push ; ret时就代表一条Handler已经结束，reg中的是下一条Handler的地址。

所以可以构建一个Handler 虚拟地址到虚拟指令的映射。

模拟执行还有一个好处，对于不同的虚拟指令，在Handler中下断，让Handler自己解密字节码中的内容，然后提取出来。

###

### 2.1.3 Handler识别

关于Handler的语义是什么就省略了。

根据jmp reg或push ; ret把Handler提取出来后，现在就需要识别其对应的虚拟机指令。

两种思路：

正则表达式匹配（速度块）

DAG或者数据流图匹配

####

#### 2.1.3.1 正则匹配

这是我目前正在用的方案，对汇编代码使用正则表达式匹配。

矛盾点是正则规则越严格，漏判越严重，规则越宽松，误判越严重。

缓解方案是对汇编代码先进行一次优化，参考编译原理中的死代码消除，对寄存器的使用进行分析。

以一个加法的Handler为例：

比如优化前的Handler：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlmMBPsLvsUIeRzY3DGfwUGmwFNicAMd7ZPfLQa0vdaAMG8uPoyXBL0kA/640?wx_fmt=png)

其中4、5、10、11行连续对rdi寄存器进行了写入，显然前三条写入是无效的。

优化后的Handler：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlvtljgic04AWLbe1xL1g3ppNM73LhC1Ps7V6siciaEHiaROc1BicPf97dIIQ/640?wx_fmt=png)

正则匹配：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FZfAJlzgym2qq3cobb79jl8Rou4UcALctWnM0cAiaOPaIxE5ibbRUmyibibAORo6O1NzrkD1a2nssdiaw/640?wx_fmt=png)

####

#### 2.1.3.2 DAG匹配

这部分只是做一个尝试。

同样是加法的例子，这是其DAG图（不太严格，因为x86复杂指令集有点麻烦）。

蓝色下划线是从栈获取的操作数。

绿色下划线是将结果和RFLAGS放回栈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlVDVT1HP7agKk6n8TwT5OWiakRZicpc6Uiaej1BXoQ2JtLP7nF9iafgHtjg/640?wx_fmt=png)

###

### 2.1.4 识别结果

模拟执行顺序执行的片段：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlUeJ3wk4bKajZS1oRBZvG8PNvgOUpUHu0jqU4LVXmpaTpcLkZrVdBXg/640?wx_fmt=jpeg)

##

## **2.2 控制流还原**

###

### 2.2.1 虚拟机指令DU分析

先分析每条虚拟机指令对栈的读写，然后构建DU链。

接着利用DU链进行一次简单的优化，包括常量传播，折叠一些变量在VM栈和VM寄存器上的移动，还有简单的MBA表达式优化（简化接下来的判断分支等步骤）。

###

### 2.2.2 判断是否为分支

进行到这里就可以判断是jmp还是jcc。

jmp的例子（左边是每条指令起始时VM字节码指针和VM栈指针）：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlnKq7RGfcDAwicSXwoYTibtvmtVROic6OxnSJSRMHMHHbwPpAB2ZSib7SLw/640?wx_fmt=jpeg)

jcc的例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlq8ibUSm5wHIkIIh0mb8qSvWIkSn2ib1Cn0l1EBtM6WvPjcpskHRY6Igw/640?wx_fmt=jpeg)

区别就是RET之前的一条语句PUSH的是否为一个立即数（依赖前面的常量传播优化）。

###

### 2.2.3 获取分支去向

接下来就可以通过DU链，获取分支的两条去向分别是什么。

依据是VMP的分支跳转伪代码为：

```
mask = -1 + flaga1 = mask & FAddra2 = ~mask & TAddrjmp = a1 + a2
```

这里是识别的例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlFKx5LqU6QDv2fYiaXQGUz4oPDkhrQK4WGrzfhHhmGiamUicpd22b8H3zQ/640?wx_fmt=jpeg)

###

### 2.2.4 获取分支条件（未完善）

这里我大致分成了两步：

识别判断的rflags标志位

识别~(~x+y)

一个比较标准的test x-y，然后判断CF的例子。

绿色框是上一步的跳转地址计算。

黄色框是rflags标志位的判断。

红色框是计算x-y的rflags。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlv68lS4pFQIlEghs4JbgEpf01AxVNSDr4uric1AcpG8MWibPWFxZbicvIw/640?wx_fmt=jpeg)

一个and x, x，判断是否为0的例子。

绿框是上一步的跳转地址计算。

黄框是判断其ZF位。

红框是读取内存，然后获取其and x, x的rflags，没识别到。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlfhnC63rlwgjEYvgV12SCOA0iax4zEVBd4iaqrZ2TVyicMU3ETJ0E2sbkw/640?wx_fmt=jpeg)

###

### 2.2.5 控制流还原杂谈

在前面Handler语义识别的时候，难免会有错漏，出现识别不了的语句。

在模拟执行还原控制流时，妥协做法是停止该分支的分析。

这里截取了一段控制流。

每个圈圈是一个虚拟指令基本块。

这里绿色箭头的是前面flag=1分支、红色箭头是前面flag=0的分支。

红色圈圈的是遇到未知虚拟指令或模拟执行错误，停止分析的块。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlYkWL2YuvtUfsnicVOPcyVib6ibGYib4eRW1TumjF2arMRR7Qs4yOKeDqDw/640?wx_fmt=jpeg)

##

## **2.3 还原成C（做的不太好）**

这一步随便水水了，只做了一部分，主要工作量太大了。

将虚拟指令输出成对应的C语言代码，然后上编译器编译。

给个加法的例子吧：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlyGic1I6P4W3CNxWpP5hm0wwj2eCicjb1iasb6N26Ay7q9MulDvicbdsl5g/640?wx_fmt=jpeg)

#

#

```
三

结尾（欢迎指教）
```

##

## **3.1 收获**

比较喜欢写代码，vmp代码还原的自动化又是个需要写很多代码的工程，就比较感兴趣，断断续续大学花了不少时间在这上面。

最大的收获是经验，写的时候花了很多时间在debug上，实际写的时间根本没多少。

我也明白，先设计好再写代码可以减少很多写代码和debug的时间，但缺乏还原经验，设计的时候无从入手，也考虑不周全，只能边写边想。算是积累了一些经验。

然后实践了一下编译原理的入门知识，一个非常有意思的领域，希望以后有机会继续深入学习下去。

##

## **3.2 关于分析深度和还原难度**

在还原的过程中，我发现对虚拟机架构的分析越多，获得更多关于壳的信息，就能写出更容易实现、更有针对性、更有效果的优化。

有点类似窥孔优化的思路，牺牲通用性，以便实现和提高效果。

#

#

# **相关链接**

VMP架构与虚拟机指令：

VMProtect 2 - Detailed Analysis of the Virtual Machine Architecture // Back Engineering（*https://back.engineering/17/05/2021/#vm-handlers-specifications*）

虚拟机分支分析：

VMP学习笔记之万用门（七）（*https://bbs.kanxue.com/thread-254445.htm*）

vmp3.5模拟x86分支指令je、jne、jge和jl的分析（*https://bbs.kanxue.com/thread-274637.htm*）

编译原理（哪本书不记得了）：

基本块的有向无环图表示

DU链

加密与解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlXRTYiaoXsKBRLibg6ia8mIp7EayoeUA5q75RKOuZzw3r2cUhXuhaHWjpA/640?wx_fmt=png)

**看雪ID：wx\_御史神风**

https://bbs.kanxue.com/user-home-907036.htm

\*本文由看雪论坛 wx\_御史神风 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FJVH3PGSiaY563SLhIPrI0tKsReH9ARfAoZb9ibj7MGPKOXiceialNsOGKPTYRKxcFMlibNjcdZml6dmw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493150&idx=3&sn=0a4ba5f62fe6fc295c3d4569edb34516&chksm=b18e905486f91942323e5185759dd19a811000d1248844b1bafb0deef364d6b8408a64fa97ec&scene=21#wechat_redirect)

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E...