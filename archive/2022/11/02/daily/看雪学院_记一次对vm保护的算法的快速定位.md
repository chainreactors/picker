---
title: 记一次对vm保护的算法的快速定位
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458481114&idx=1&sn=cbce63be2b15d4adcf230a1a3212791d&chksm=b18e415086f9c846e3fedc131da600759ccc9ba2197e283863d61aeb459f0dbc0e72816962db&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-02
fetch_date: 2025-10-03T21:32:52.110648
---

# 记一次对vm保护的算法的快速定位

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6as51hfkIjMYJMZxoEjrQyqQxylS4xVOkfH0kHE29mKm0kpg3CQ7a4g/0?wx_fmt=jpeg)

# 记一次对vm保护的算法的快速定位

lxcoder

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6vaPmkXlnIoibDAOnn4EibeUicmwxRtX9pFUjQ7Ytku0YKCh1m3vsZniceQ/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：lxcoder

在找sgmain相关资料时看到了这个贴子：*https://bbs.pediy.com/thread-267741.htm*

之后对大佬使用的trace工具很感兴趣，对反编译引擎也很感兴趣，不过底蕴不够，反编译引擎之类的也就将就用第三方，只能常试用frida的Stalker改了个类似的trace工具试了下效果也就有了这篇文章。

用到的工具：ida/Ghidra/frida

看的是手淘6.5.82版本的sgmain，因为本身只是对trace工具的一次验证，所以不包含实际的算法分析过程，只谈测试过程中的感受。

快速定位主要依赖的是Stalker，ida和Ghidra主要是用于静态分析。在静态分析上，我这种小菜鸡就不讨论两个反编译引擎的本质哪个优劣，就谈使用的感受。

先上对比，对于sgmain的doCommand方法。

ida的效果：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6hDOt9JZ901ib1vEZfnd6GMHIbKfuXEwSws6z0JvIlYjbf540lSxzlpw/640?wx_fmt=png)

```
__int64 __fastcall sub_2DB50(JNIEnv *param_1,_int64 param_2,int param_3,long param_4){    unsigned int v12 = 0;    long ret = 0;    long* ptr = (long*)malloc(0x20);    if(ptr != nullptr){        ptr[0] = 0LL;        ptr[1] = 0LL;        *(_DWORD *)ptr = param_3 / 10000;        v7 = param_3 % 10000 / 100;        *((_DWORD *)ptr + 1) = v7;        *((_DWORD *)ptr + 2) = param_3 % 100;        ptr[2] = param_1;        ptr[3] = param_4;        ret = sub_2BB3C(param_3 / 10000, v7, param_3 % 100, 1u, ptr, &v12);    }    free(ptr);     if(ret == 0 && v12 != 0){        //throw Exception        sub_E78C0(param_1, v12, 0x20aa97)    }    return ret;}
```

可以很明显看出ida对除法的优化更好一些，ghidra在除法这块就没有ida好，但是我个人更喜欢Ghidra的效果。

这里说句题外话，关于除法，编译器对一个整数进行除法运算时往往会转换成乘一个魔数然后除2的多少次方这种，这个推导过程很复杂，本质上就是把除任意整数变成除2的N次方的数，但过程中存在很多边界问题导致比较复杂，不过如果当ida之类的返编译器在复杂需要手动推导时，网上有种方法可以算出大概的值，不过涉及到符号问题及取模问题，记得好像是有Sub类指令参与的可能就是取模，但没有细究，有兴趣的可以自己编译后对比看看。

一般像这种同时存在乘法、位移0x3F/0x1f取符号位、ASR之类指令时，基本八九不离十就可能是除法。

```
LOAD:000000000002DBFC A9 75 91 52+                MOV             W9, #0x68DB8BADLOAD:000000000002DBFC 69 1B AD 72LOAD:000000000002DC04 A9 7E 29 9B                 SMULL           X9, W21, W9LOAD:000000000002DC08 1F 7D 00 A9                 STP             XZR, XZR, [X8]LOAD:000000000002DC0C E8 1B 40 F9                 LDR             X8, [SP,#0x80+p]LOAD:000000000002DC10 2C FD 7F D3                 LSR             X12, X9, #0x3F ; '?'LOAD:000000000002DC14 29 FD 6C 93                 ASR             X9, X9, #0x2C ; ','LOAD:000000000002DC18 20 01 0C 0B                 ADD             W0, W9, W12LOAD:000000000002DC1C 0A E2 84 52                 MOV             W10, #0x2710LOAD:000000000002DC20 EB A3 90 52                 MOV             W11, #0x851FLOAD:000000000002DC24 00 01 00 B9                 STR             W0, [X8]LOAD:000000000002DC28 6B 3D AA 72                 MOVK            W11, #0x51EB,LSL#16LOAD:000000000002DC2C 0A D4 0A 1B                 MSUB            W10, W0, W10, W21LOAD:000000000002DC30 E8 1B 40 F9                 LDR             X8, [SP,#0x80+p]LOAD:000000000002DC34 4A 7D 2B 9B                 SMULL           X10, W10, W11LOAD:000000000002DC38 A9 7E 2B 9B                 SMULL           X9, W21, W11LOAD:000000000002DC3C 4B FD 7F D3                 LSR             X11, X10, #0x3F ; '?'LOAD:000000000002DC40 4A FD 65 93                 ASR             X10, X10, #0x25 ; '%'LOAD:000000000002DC44 41 01 0B 0B                 ADD             W1, W10, W11LOAD:000000000002DC48 01 05 00 B9                 STR             W1, [X8,#4]LOAD:000000000002DC4C 2A FD 7F D3                 LSR             X10, X9, #0x3F ; '?'LOAD:000000000002DC50 28 FD 65 93                 ASR             X8, X9, #0x25 ; '%'LOAD:000000000002DC54 E9 1B 40 F9                 LDR             X9, [SP,#0x80+p]LOAD:000000000002DC58 08 01 0A 0B                 ADD             W8, W8, W10LOAD:000000000002DC5C 8A 0C 80 52                 MOV             W10, #0x64 ; 'd'LOAD:000000000002DC60 02 D5 0A 1B                 MSUB            W2, W8, W10, W21LOAD:000000000002DC64 22 09 00 B9                 STR             W2, [X9,#8]
```

如上面的这种代码，就可以尝试用(1 << XX) / (magicNum - 1)这种方式来算出大概的除数，比如就上面的指令来说：

```
>>> (1 << 0x2c) / (0x68db8bad - 1)10000.000002510205>>> (1 << 0x25) / (0x51eb85ef - 1)99.99998491839733
```

而且在patch后的及时效果上面感觉更好一些，特别是那些br reg,adrp ret之类的跳转识别效果会比ida好，用ida的时候那个JMPOUT很尴尬，即使你使用跳转patch了也不一定能有效f5，可能还得去除中间的一些混淆的乱码才可以。

其次Ghidra也存在一个比较尴尬的问题，就像上面这个代码里面框起来的代码，那个0x2bb3c这个函数（ghidra会自动添加基址，默认是0x100000），在初次打开时，这个函数被识别为了空函数，而且无反回，这也就直接导致下面的那个0xe78c0所在的代码块被直接隐藏了，因为lStack76 != 0被直接视为了不可达分支，修改函数定义后代码也就立刻重新生成了上面的这个效果，修改是及时生效的，效果不错。

现在的一些间接跳转的混淆，不管他怎么变形，实际上很多时候都是常量表达式，而对于常量表达式的这种间接跳有很多种方式处理。

比如0x2bb3c头部的这段代码：

```
LOAD:000000000002BB3C                 SUB             SP, SP, #0x1B0LOAD:000000000002BB40                 STP             X28, X27, [SP,#0x1A0+var_50]LOAD:000000000002BB44                 STP             X26, X25, [SP,#0x1A0+var_40]LOAD:000000000002BB48                 STP             X24, X23, [SP,#0x1A0+var_30]LOAD:000000000002BB4C                 STP             X22, X21, [SP,#0x1A0+var_20]LOAD:000000000002BB50                 STP             X20, X19, [SP,#0x1A0+var_10]LOAD:000000000002BB54                 STP             X29, X30, [SP,#0x1A0+var_s0]LOAD:000000000002BB58                 ADD             X29, SP, #0x1A0LOAD:000000000002BB5C                 MRS             X26, #3, c13, c0, #2LOAD:000000000002BB60                 MOV             W23, W1LOAD:000000000002BB64                 MOV             W24, W0LOAD:000000000002BB68                 MOV             W10, #0x2710LOAD:000000000002BB6C                 MOV             W12, #0x64 ; 'd'LOAD:000000000002BB70                 LDR             X14, [X26,#0x28]LOAD:000000000002BB74                 MUL             W15, W24, W10LOAD:000000000002BB78                 MUL             W12, W23, W12LOAD:000000000002BB7C                 MOV             W22, W2LOAD:000000000002BB80                 MOV             W13, #0xC600LOAD:000000000002BB84                 ADD             W10, W15, W12LOAD:000000000002BB88                 MOV             W8, #0x96LOAD:000000000002BB8C                 SUB             X9, X29, #-var_70LOAD:000000000002BB90                 MOVK            W13, #0x53E,LSL#16LOAD:000000000002BB94                 ADD             W10, W10, W22LOAD:000000000002BB98                 MOV             X21, X4LOAD:000000000002BB9C                 ADD             W13, W10, W13LOAD:000000000002BBA0                 STUR            X14, [X29,#var_58]LOAD:000000000002BBA4                 STUR            W8, [X29,#var_70]LOAD:000000000002BBA8                 ADR             X27, loc_2BBACLOAD:000000000002BBACLOAD:000000000002BBAC loc_2BBAC                               ; DATA XREF: sub_2BB3C+6C↑oLOAD:000000000002BBAC                 LDRSW           X4, =0xFFFFFE62LOAD:000000000002BBB0                 MOV             X20, #0xABLOAD:000000000002BBB4                 EOR             X4, X4, X20LOAD:000000000002BBB8                 ADD             X4, X4, #0x88LOAD:000000000002BBBC                 MVN             X4, X4LOAD:000000000002BBC0                 LDRSW           X10, [X9]LOAD:000000000002BBC4                 EOR             X4, X4, X10LOAD:000000000002BBC8                 ADD             X27, X27, X4LOAD:000000000002BBCC                 MOV             X8, #0x62 ; 'b'LOAD:000000000002BBD0                 BR               X27
```

代码看起来有点复杂，各种运算，还有间接地址访问，而且每个函数头部都有这种间接跳，且貌似每个表达式都不一样，但实际上这种处理起来也相当简单，分静态和动态两种情况。

动态的情况不用说，单步或trace来获取对应的跳转地址即可，对于Ghidra，也不需要特别处理，它会自动帮你把这些常量表达式计算出来，在进行反编译时会自动使用它计算出的结果进行代入。

比如下面的是Ghidra的汇编显示：

```
                     LAB_0013dd1c                                    XREF[1]:     0013dd00(j) 0013dd1c e8 03 00 90     adrp       x8,0x1b90000013dd20 08 01 11 91     add        x8,x8,#0x4400013dd24 08 09 40 f9     ldr        x8,[x8, #0x10]=>DAT_001b9450                     = 000000000013DC94h0013dd28 08 71 02 91     add        x8,x8,#0x9c0013dd2c 00 01 1f d6     br         x8=>LAB_0013dd30
```

而如果你要说就用ida，不开启动态调试的情况下也简单，用ida的脚本使用unicorn进行模拟执行一下结果就跑出来了：

![](ht...