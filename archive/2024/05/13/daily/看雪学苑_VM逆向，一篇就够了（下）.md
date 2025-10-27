---
title: VM逆向，一篇就够了（下）
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458554406&idx=1&sn=09b1307e73fc9a5575095895864e3799&chksm=b18da0ac86fa29ba72ab127bd2c86148921e21a605844b7d1a7ba8f60361215107dc3f67f5fd&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-13
fetch_date: 2025-10-06T17:15:01.776851
---

# VM逆向，一篇就够了（下）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhlIanAl9SBuaY5tZMGy465suXh96lnFaBrBbDV1VeR3rLsqVQfxvjPQ/0?wx_fmt=jpeg)

# VM逆向，一篇就够了（下）

马先越

看雪学苑

接着上一篇文章（https://bbs.kanxue.com/thread-281119.htm），我们继续了解一些不一样vm。

```
一

实战三
```

**d3sky**

这一题需要了解一些TLS相关知识。

### TLS回调函数

TLS（Thread Local Storage，线程局部存储）是各线程的独立的存储空间，TLS回调函数是指，每当创建或终止进程的线程时会自动调用执行的函数，且调用执行优先于EP代码，该特征使它可以作为一种反调试技术使用。

为什么要讲这东西呢，因为一开始分析main函数时感觉静态分析比较吃力就想着动态调试分析一下，然后就停在了这里,这是触发了一个访问异常，sub\_4C1050是由线程回调函数（TlsCallback\_0）调用的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhTe1ZJxbPP9LnibicYn3iazjibpia50SSKO6TGL4UyPvzGiashZpVo8QaiceWA/640?wx_fmt=other&from=appmsg)

指令在尝试读取地址0x00处的数据，导致程序不能正常长运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhq3Px0qqJESbL44iao4kAicrA8pXQMRKnicOEq9T85UuJNkqk2PnGye63w/640?wx_fmt=other&from=appmsg)

汇编页面长这个样子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhiajSYToqNBThoyPlv2PXAFlBoibUhSxWaw7KBfFXiacFCqXulTobVsceQ/640?wx_fmt=other&from=appmsg)

圈起来的那里是判断程序是否处于调试状态，如果是调试状态则执行下面的`mov ecx,[eax]`指令。如果不是处于调试状态则走另一个分支，触发一个除零异常，跳转到处理函数之后程序正常运行。对抗方法很简单，直接在IsDebuggerPresent结束之后修改eax的值，将1修改为0。

踩了个坑大家注意一下，如果修改的是跳转逻辑也就是将jz改为jnz，在调试状态程序也是不能正常运行的，因为IsDebuggerPresent的返回值被存储在了[ebp+var1C]处，下面的idiv 除指令除的就是这个位置，试想我们修改了跳转逻辑成功避开了那段会触发访问异常的指令，但是往下运行却没能触发除零异常，自然不能跳转到程序原本的执行流程上去。

### 分析main函数

这个VM题和前两个又很大的区别，他没有类似mov、xor、push、pop这样的操作，只有一条与非指令opcode[v6] = ~(opcode[v7] & opcode[v8])，而通过与非指令可以实现所有的逻辑运算。出题师傅的博客有详细的介绍d3sky出题小记 - 云之君's Blog (https://www.yunzh1jun.com/2023/05/02/d3sky/)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhWZVA89kqL98YmCxS61dgex1Gf144nG7Ee4kKv4NbqDTzRYTC7bYVcA/640?wx_fmt=other&from=appmsg)

乍一看很唬人，跟着动调几轮就能理清逻辑了，opcode[2]、opcode[7]、opcode[19]是三个标志位。

通过动态调试很容易判断出当opcode[2]为1时，会在控制台输出，当opcode[7]为1时会读取输入，在读取完所有的数据之前，opcode[19]不会为1，结合puts("wrong")可以推测出他是flag检测位。

后面这一组着重分析一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhmdw7DR4MC8127Zlic008TIdJBOUiaydYsSqM0BA4sX7eMr1gUODpZ5eA/640?wx_fmt=other&from=appmsg)

注释解释的应该很清楚了，RC4\_back是RC\_4的加/解密部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhmdw7DR4MC8127Zlic008TIdJBOUiaydYsSqM0BA4sX7eMr1gUODpZ5eA/640?wx_fmt=other&from=appmsg)

opcode[0]可以看作是虚拟机的pc指针，而每次循环都会解密三个单位的指令（这里第一次RC4理解为解密更符合逻辑一点，也就是将原始的opcode认为是加密处理过的）。取出来之后，pc指针加三，可以理解为每条指令长度为3。之后会将opcode进行复原。然后执行核心的与非指令。

在调试的过程中通过十六进制窗口那里能得到输入存储的位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrh8f8BnicZRniaW8WBicEsLznDEDOGiayNtWkZleTrrB7hhj19uZGic2LGLLw/640?wx_fmt=other&from=appmsg)

查看这个地址，可以看到他在tls回调函数里就被初始化了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhBzicJ6ot92ATMCJ8Mia3n5BO9UFoictkxw8lTxXk2s7ichXYLLpPVDV3Bw/640?wx_fmt=other&from=appmsg)

###

### 翻译

接下来就是翻译了，和前面两个题目一样，我们需要做的是打印下来，而打印又有两种思路，一是将代码直接copy过来，编译执行一下，打印出所有的与非逻辑。二是借助idapython，由于之前都是用的第一种方法，这道题目就使用idapython来打印指令了。

想要实现的效果就是

```
opcode[11]=~(opcode[20]&opcode[20])      opcode[11]=~( 1 & 1 )
```

根据汇编代码编写idapython脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhfYDuazaJPwfCEaicWrSUJ9L2McHSfhUbm1MjXnoH1hUFAoaOVOEJkKw/640?wx_fmt=other&from=appmsg)

```
import idc
var_8=-8
var_C=-0x0C
v6=idc.get_reg_value('eax')
ebp_=idc.get_reg_value('ebp')
v7=idc.get_wide_word(ebp_+var_8)
v8=idc.get_wide_word(ebp_+var_C)

opcode_base=0xBE4018
value0=idc.get_wide_word(opcode_base+v7*2)       #这里需要注意，v7要乘2，因为opcode是word数组
value1=idc.get_wide_word(opcode_base+v8*2)
print('opcode[%d]=~(opcode[%d]&opcode[%d])'%(v6,v7,v8),'     opcode[%d]=~( %d & %d )'%(v6,value0,value1))
```

我们只关心对输入的判断，所以前面的逻辑不用理会，使用idapython在输入结束时提醒。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GI89YLObhqC8xGnamkzMrhmT5cFhbU4Qowzjx5KGladvtiaenrUTZCHDSk6E6iaaP6ico4yWvj2eTHw/640?wx_fmt=other&from=appmsg)

```
import idc
var_24=-0x24
ebp_=idc.get_reg_value('ebp')
num=idc.get_wide_word(ebp_+var_24)
if(num==0x24):
   print('-------------------------------------END-------------------------------------')
   print('-------------------------------------END-------------------------------------')
   print('-------------------------------------END-------------------------------------')
```

输入：123456789012345678901234567890123456~

输出如下：

```
-------------------------------------END-------------------------------------
opcode[7]=~(opcode[8]&opcode[8])      opcode[7]=~( 126 & 126 )
opcode[2808]=~(opcode[7]&opcode[7])      opcode[2808]=~( 65409 & 65409 )
opcode[11]=~(opcode[2772]&opcode[2772])      opcode[11]=~( 49 & 49 )      //取反
opcode[11]=~(opcode[2773]&opcode[11])      opcode[11]=~( 50 & 65486 )
opcode[12]=~(opcode[2773]&opcode[2773])      opcode[12]=~( 50 & 50 )
opcode[12]=~(opcode[2772]&opcode[12])      opcode[12]=~( 49 & 65485 )
opcode[17]=~(opcode[12]&opcode[11])      opcode[17]=~( 65534 & 65533 )
opcode[11]=~(opcode[2774]&opcode[2774])      opcode[11]=~( 51 & 51 )
opcode[11]=~(opcode[2775]&opcode[11])      opcode[11]=~( 52 & 65484 )
opcode[12]=~(opcode[2775]&opcode[2775])      opcode[12]=~( 52 & 52 )
opcode[12]=~(opcode[2774]&opcode[12])      opcode[12]=~( 51 & 65483 )
opcode[18]=~(opcode[12]&opcode[11])      opcode[18]=~( 65532 & 65531 )
opcode[11]=~(opcode[17]&opcode[17])      opcode[11]=~( 3 & 3 )
opcode[11]=~(opcode[18]&opcode[11])      opcode[11]=~( 7 & 65532 )
opcode[12]=~(opcode[18]&opcode[18])      opcode[12]=~( 7 & 7 )
opcode[12]=~(opcode[17]&opcode[12])      opcode[12]=~( 3 & 65528 )
opcode[18]=~(opcode[12]&opcode[11])      opcode[18]=~( 65535 & 65531 )
opcode[11]=~(opcode[2809]&opcode[2809])      opcode[11]=~( 36 & 36 )
opcode[11]=~(opcode[18]&opcode[11])      opcode[11]=~( 4 & 65499 )
opcode[12]=~(opcode[18]&opcode[18])      opcode[12]=~( 4 & 4 )
opcode[12]=~(opcode[2809]&opcode[12])      opcode[12]=~( 36 & 65531 )
opcode[19]=~(opcode[12]&opcode[11])      opcode[19]=~( 65503 & 65535 )
```

观察输出不难发现（49、50、51、52，正是前四个输入1234的ascii），应该是把我们的输入按照四字节一组进行加密的。也能看出,我们的输入存储在从opcode[2772]这个位置。

与非运算十六进制观察更方便一些。

```
-------------------------------------END-------------------------------------
opcode[7]=~(opcode[8]&opcode[8])      opcode[7]=~( 7e & 7e )
opcode[2808]=~(opcode[7]&opcode[7])      opcode[2808]=~( ff81 & ff81 )      //保存最后一位输入至opcode[2808]

opcode[11]=~(opcode[2772]&opcode[2772])      opcode[11]=~( 31 & 31 )       //opcode[11]=~(input[0]&input[0])
opcode[11]=~(opcode[2773]&opcode[11])      opcode[11]=~( 32 & ffce )       //opcode[11]=~(input[1]&opcode[11])
opcode[12]=~(opcode[2773]&opcode[2773])      opcode[12]=~( 32 & 32 )       //opcode[12]=~(input[1]&input[1])
opcode[12]=~(opcode[2772]&opcode[12])      opcode[12]=~( 31 & ffcd )       //opcode[12]=~(input[0]&opcode[12])
opcode[17]=~(opcode[12]&opcode[11])      opcode[17]=~( fffe & fffd )       //opcode[17]=~(opcode[12]&opcode[11])

opcode[11]=~(opcode[2774]&opcode[2774])      opcode[11]=~( 33 & 33 )       //opcode[11]=~(input[2]&input[2])
opcode[11]=~(opcode[2775]&opcode[11])      opcode[11]=~( 34 & ffcc )       //opcode[11]=~(input[3]&opcode[11])
opcode[12]=~(opcode[2775]&opcode[2775])      opcode[12]=~( 34 & 34 )       //opcode[12]=~(input[3]&input[3])
opcode[12]=~(opcode[2774]&opcode[12])      opcode[12]=~( 33 & ffcb )       //opcode[12]=~(input[2]&opcode[12])
opcode[18]=~(opcode[12]&opcode[11])      opcode[18]=~( fffc & fffb )       //opcode[18]=~(opcode[12]&opcode[11])

opcode[11]=~(opcode[17]&opcode[17])      opcode[11]=~( 3 & 3 )             //opcode[11]=~(opcode[17]&opcode[17])
opcode[11]=~(opcode[18]&opcode[11])      opcode[11]=~( 7 & fffc )          //opcode[11]=~(opcode[18]&opcode[11])
opcode[12]=~(opcode[18]&opcode[18])      opcode[12]=~( 7 & 7 )             //opcode[12]=~(opcode[18]&opcode[18])
opcode[12]=~(opcode[17]&opcode[12])      opcode[12]=~( 3 & fff8 )          //opcode[12]=~(opcode[17]&opcode[12])
opcode[18]=~(opcode[12]&opcode[11])      opcode[18]=~( ffff & fffb )       //opcode[18]=~(opcode[12]&opcode[11])

//注意下面是进行比较
opcode[11]=~(opcode[2809]&opcode[2809])      opcode[11]=~( 24 & 24 )       //opcode[11]=~(cpdata...