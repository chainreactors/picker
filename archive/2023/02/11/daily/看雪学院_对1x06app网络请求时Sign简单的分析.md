---
title: 对1x06app网络请求时Sign简单的分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458494504&idx=1&sn=3c841600ff8f2a3133bfbd40fa104da7&chksm=b18e96a286f91fb4b4724c08ac5e56e4f9355bba6d326a4d609d45ccf869bb3860bb53c1db3b&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-02-11
fetch_date: 2025-10-04T06:21:10.213059
---

# 对1x06app网络请求时Sign简单的分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8H5maUPpWGrkoicF4VhkDiaIJy2msPor3pGCRkzicY2y5RqaRaFgkMOA2j8XcTxv0uuSta0vhko3Nd1w/0?wx_fmt=jpeg)

# 对1x06app网络请求时Sign简单的分析

lxcoder

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8H5maUPpWGrkoicF4VhkDiaIJ5KVUZMPSo9DJRHacia7Joibtibg4kiaeI9NN5tZvCpe2BibxBLDG5p7mrpQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：lxcoder

**目标：**找出请求中sign值的来源。

**准备**

1.修改后的专用分析机。

2.准备抓包环境。

3.准备Frida、ida、jadx等分析环境。

简单说一下分析过程中遇到的问题：

1.首先是定位native在so中的位置，这个很简单，方法也很多。

2.使用frida配置主动调用环境，让测试变的更简单一些。

3.对算法核心代码进行定位，定位核心算法的方法很多，各有各的优劣，多尝试，合适的地方使用合适的方法。

(1)Ida的trace功能，这种方法本身是非常好的一种方法，因为大部分的情况下这种方法更有效也更简单，但目前这种方式已知存在一些问题导致这种方式的使用受限。

①慢，ida trace的方式会很慢，所以一般都是在缩小范围后再使用这种trace的方式来操作。

②容易跑偏，跑到系统库里面，这种问题一般配合ida的脚本的DBG\_Hooks进行主动对指令范围进行控制，通过ida\_dbg.enable\_insn\_trace(True)来控制是否开启指令跟踪，不过这种方式没有具体用过所以这里不作评价，我常用的还是缩小范围后再开启trace，或通过trace来找一些异常代码，比如退出指令等，因为这样操作比较简单，可以绕开大部分问题，让日志也更简洁一些。

③ida的trace功能貌似开启后就无法关闭，所谓的关闭只是不再打印日志，实际上trace的功能代码还是在跑，手动操作的时候貌似存在这个问题，没有用脚本试过，所以不清楚脚本的接口关闭会不存在同样的问题。

④碰到特殊指令会导致功能异常，比如这里碰到的问题就是在trace功能开启的状态下STXR/STXRH指令会操作失败，包括在这行指令上F8也会失败，原因在于单步会导致读和写同时存在时写就会失败，目前这个算法里面没有看到被用在反调试功能上，只是在系统库里面大量看到了这种指令。从反调试的角度来说，这个指令其实存在好几个反调试点，对熟悉它的人来说影响不大，但对不熟悉它的人来说可以让人给整懵逼了，比如，算法中穿插着用这个指令进行赋值，根据指令执行结果改变算法流程（这个指令的第一个操作寄存器会被写入执行成功与否的状态），系统库中就是用这个指令配合CBNZ一起使用的，将指令执行结果带入算法中进行计算等等，都是骚操作。

⑤算法中穿插反调试手段的情况，这种比较普遍，这个Sign算法里面就有，这种方式也好解决，碰到了改掉就行，无非就是麻烦一点罢了。

(2)Unidbg，这种方法很强大，它的强大主要体现在无感知hook这块，但这种也不够完善，存在很多问题，主要是在环境这一块，毕竟是一个脱机的环境，补环境这块让人很头疼，不过在指令级追踪这块非常强大，可以对任意指令地址进行日志打印以分析流程，虽然这个也支持调试，但是那种调试还是不太习惯，所以整体来说这个我用的比较少，一般用它大致看看JNI\_OnLoad还不错。

(3)Frida，frida一般配合ida一起使用，这也是我最常用的手段，这种方式也基本上算是一种万能的方法，复杂环境使用这种方式可以让分析变得更轻松一些，基本流程就是ida静态分析一下可疑的关键代码，然后通过Frida进行确认定位以缩小关键代码的范围，之后再对关键代码进行trace日志分析，或进行单步调试分析均可以，同样的，这种方法通用是通用，但是同时也要面对frida和ida存在的共同的问题。

**问题：**说说过程中碰到的问题。

1.STXR/STXRH指令的问题以及ida的指令跟踪总是跑到库函数里面等，这些问题直接导致了我trace整个函数的计划失败，后面缩小范围的时候还是会碰到，这时候我使用的方法就是在碰到这种指令时在保证单线程的情况下将这种指令替换为了等价的STR之类的指令进行绕过了，trace也就自然而然的可以了。

2.frida对指令hook的问题，在Hook函数时没有碰到问题，只有在一个函数频繁打印时frida才会异常挂掉，但是在对指令进行hook时，基本上90%的情况下都会异常，比如hook bl x8这样的指令，拿取x8的值时，基本上一hook就挂掉了庆幸的是第一次到来时基本可以拿到地址，不过也有例外情况，有一些就碰到了x8==0x20的情况，跳转到0x20的地址进行执行，汗，然后大致看了下frida对函数头部hook和指令间Hook的差异：

frida在hook函数头部的时候会将头部改写为：

```
ADRP            X16, #0x7F75F8E000BR              X16
```

而在对中间指令进行hook时，确替换了4条指令，比如在hook blr x8指令时将就bl及接下来的三条指令一起替换成了下面的这种指令：

```
LDR             X16, =0x7F75F8AD00BR              X16qword_7F4DA12FE0 DCQ 0x7F75F8AD00
```

对于函数头部的代码来说还好，没什么问题，但是对于指令间Hook的代码来说就存在两种情况：

（1）指令占用空间过大，如果其占用了跳转指令的目标地址的指令导致在执行前有指令跳转到了这4条指令上，那基本上也就异常无疑了。

（2）X16虽然做为保留寄存器存在，正常编译器一般不尽量不用它，但如果刻意使用呢，就会导致环境异常，比如将blr x8这种指令用x16替代

3.混淆，主要碰到了3种混淆，强度都不算太大，解决起来也很简单，这三种混淆主要还是对静态分析造成干扰，对动态分析没感觉到有太大的阻碍，无非就是注意不要跑偏就好

(1)第一种混淆，在函数头部,解决方法也很简单，分析一下函数特征，脚本里面根据特征直接替换就行了，比如上面的混淆整个nop掉，然后直接b sub\_68314即可。

```
LOAD:00000000000682EC                 STP             X0, X30, [SP,#var_10]!LOAD:00000000000682F0                 BL            LOAD:00000000000682F4                 ADR             X0, sub_68314LOAD:00000000000682F8                 MOV             X30, X0LOAD:00000000000682FC                 RET
```

(2)第二种混淆，存在偏移表的这种，观察代码逻辑，直接以w0的值代入表达式算出表中的偏移量，然后取出偏移表中的值算出跳转的最终地址直接跳转过去即可。

```
LOAD:0000000000068394                 STP             X0, X30, [SP,#-0x10]!LOAD:0000000000068398                 LDR             W0, =5LOAD:000000000006839C                 BL              loc_68320LOAD:0000000000068320                 BL              sub_5D6B0LOAD:000000000005D6B0                 STP             X0, X1, [SP,#var_10]!LOAD:000000000005D6B4                 ADD             W0, W0, #1LOAD:000000000005D6B8                 LDR             W0, [X30,W0,UXTW#2]LOAD:000000000005D6BC                 ADD             X30, X30, W0,UXTWLOAD:000000000005D6C0                 LDP             X0, X1, [SP+0x10+var_10],#0x10LOAD:000000000005D6C4                 RET
```

(3)第三种，也有规律可寻，这种我没有处理，直接单步调的，看起来str ldr一大片一大片的，实际上都是一些保存环境和恢复环境的代码，调试的时候基本可以忽略，碰到逻辑上不符合预期的再回头看看就好。而要pass掉这种代码其实也不难，比如下面的这段代码。

```
LOAD:0000000000068438                 MOV             W2, #0x18LOAD:000000000006843C                 STR             X2, [X19,#0x100]LOAD:0000000000068440                 MOV             X4, #0x100LOAD:0000000000068444                 MOV             X21, #0x18LOAD:0000000000068448                 MOV             X25, #0LOAD:000000000006844C                 MOV             X20, #4LOAD:0000000000068450                 MOV             X23, #0x18LOAD:0000000000068454                 B               loc_68614LOAD:0000000000068614                 LDR             X4, [X19,X4]LOAD:0000000000068618                 LDR             X21, [X19,X21]LOAD:000000000006861C                 B               loc_68678LOAD:0000000000068678                 ADR             X0, qword_68688LOAD:000000000006867C                 LDRSW           X20, [X0,X20,LSL#2]LOAD:0000000000068680                 ADD             X20, X20, X0LOAD:0000000000068684                 BR              X20
```

分为三个部分，一是赋值部分一大片的mov常量，然后一个B跳转，第二部分可以算是干扰部分，将前面的赋值部分代入后实际上也是一个赋值代码，可以替换第一部分的相关赋值指令，不过需要注意位置会不会有影响，第三部分就是一个跳转表，大致意思就是jmp table + (table + index 4)
最终结果就是：

```
MOV W2,#0x18STR X2, [X19,#0x100]MOV X25,#0MOV X23,#0x18LDR X4,[X19,#0x100]MOV X21,[X19,#0x18]jmp qword_68688 + *(qword_68688 + #4 * 4)
```

如果只是追求逻辑修复能F5的话这样就可以了。

最后附上字符串解密还原的代码，代码量比较少，比较简单，示例代码还原后与代码中的一致，调试的时候忘截图了，只记录了参数和结果，所以这里没有ida里面的截图，结果为字符串“sec.umeng.com”：

```
void decode(){    printf("start decode data.\r\n");     const char key[] = "DcO/lcK+h?m3c*q@";    unsigned char buf[] = {0xE9, 0xAD, 0x2F, 0x3C, 0x8D, 0x32, 0xF4, 0x7B, 0x1E, 0x01, 0x97, 0x32, 0xA9};     unsigned char S[0x100] = {0};    unsigned char T[0x100] = {0};     for(int i = 0; i < 0x100; i++){        S[i] = (unsigned char)i;        T[i] = key[i % 0x10];    }     //打乱数组    int w12 = 0;    for(int i = 0; i < 0x100; i++){        unsigned int w13 = S[i];        w12 = w13 + w12 + T[i];        unsigned int w14 = w12 + 0xFF;        if(w12 >= 0){            w14 = w12;        }        w12 = w12 - (w14 & 0xFFFFFF00);    //还原的时候在这里踩了个坑，"-"与"&"同级，不加括号会先算减号        int w15 = S[w12];        S[i] = w15;        S[w12] = w13;    }     int i = 0;    int k = 0;    char outbuf[0x100] = {0};    char* pOut = (char*)outbuf;    char* pIn = (char*)buf;     int nLen = sizeof(buf);    while(nLen--){        i = (i + 1) & 0xFF;        char tmp = S[i];        k = (tmp + k) & 0xFF;        S[i] = S[k];        S[k] = tmp;        *(char*)pOut++ = S[(S[i] + S[k]) & 0xFF] ^ *pIn++;    }    printf("%s\r\n", outbuf);}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G5icgbRIHx66a4Sb9aQYuSZo4bCPepNSdXwY6mQEUV62micqBwXxgUT0ibxP9B4OD5QicEwL0XW8kvzg/640?wx_fmt=png)

**看雪ID：lxcoder**

https://bbs.kanxue.com/user-home-719948.htm

\*本文由看雪论坛 lxcoder 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FlWUVBM0O8466wPsF4d5cAcBrRibibpkmsvQnLTZt8OM3wicpjyGhVAz2bT9oxEqtZG7bYyGkqgZ1RQ/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493061&idx=3&sn=cc1dbe7f57aef52ac2772e9f17a47249&chksm=b18e900f86f919195d56b2a252efee20734b4b494c3e6e7e53a47d429b2df5fafec28b1ab33a&scene=21#wechat_redirect)

**#****往期推荐**

1、[地图浏览器-vip分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458494114&idx=1&sn=a46d04c3cfa67b29678f87399c4f7a77&chksm=b18e942886f91d3ea31d1fe067d6efee3a8ebaa5d0b1d65b84e4aaa9e2b02bc8693ced06dfbd&scene=21#wechat_redirect)

2、[车服务平台-ios版本分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458494081&idx=1&sn=acc6fdadd1d944878e63db5ddb70e548&chksm=b18e940b86f91d1d46da47264ad1d4e639b9da67f0b5bcc4b98e8122de7fb44153a616c956e4&scene=21#wechat_redirect)

3、[STL容器逆向与实战](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458494026&idx=1&sn=66ef0d159bc60c1d926af4185b4aebb0&chksm=b18e94c086f91dd6fb185eca30dc420820b2ba7e04fa70f5ecd6a3ce98458647e8fb882739d5&scene=21#wechat_redirect)

4、[RCTF2022-MyCarsShowSpeed 题目分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493925&idx=1&sn=9205954527b62f7dd04a028bbd3e401f&chksm=b18e936f86f91a79d37166f1ed5761ba4e58818b...