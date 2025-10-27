---
title: ARM64 目前主流的反混淆技术的初窥
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589932&idx=1&sn=f9c212ce96c0b70d92601e5b50343a77&chksm=b18c2a6686fba370e3fd01889d932cc166d6acf487469e12d6cd4e6738d88e35fcb48ca615a1&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-25
fetch_date: 2025-10-06T20:37:52.232265
---

# ARM64 目前主流的反混淆技术的初窥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYdKoJhriakFguSiauu2VTeQF05hVNA1GjZhofJKPJh5dLXlOZDXO5Ngyg/0?wx_fmt=jpeg)

# ARM64 目前主流的反混淆技术的初窥

method

看雪学苑

随着混淆技术和虚拟化的发展，我们不可能很方便的去得到我们想要的东西，既然如此，那只能比谁头更铁了，本文列举一下在逆向某一个签名字段中开发者所布下的铜墙铁壁，以及我的头铁方案，本文更多的是分析思路，而不是解决方案，所以样本自己找。

```
一，

BR reg
```

#

在ARM64 中 寄存器跳转只剩下BR 指令了，由于ida 为了 br的准确性(cs:ip跳转)，ida会识别成函数跳转，但是这却给开发者带来了天大的便利，于是一个贼好用的anti 反编译器函数分析方案横空出世。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYibGsEZxPAm3eYI631SslDgcNelz06yoiaaXzFeSp59BpT1pdGjP9vLfA/640?wx_fmt=png&from=appmsg)

让我们回到汇编：

```
.text:000000000008D1E8                 BL              sub_8D1F8
.text:000000000008D1EC                 MOV             X1, X0
.text:000000000008D1F0                 ADD             X1, X1, #0x38 ; '8'
.text:000000000008D1F4                 BR              X1
```

可以看到 X1的值是由sub\_8D1F8 返回值加上 0x38 ，而sub\_8D1F8一看地址 不对啊，为什么这么近。我们再看看sub\_8D1F8的汇编。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYdXHickHsbR6h3etAMH7RXBFibVU9ArP8vphq0Fu0ePU4laUuI4iaUj5GQ/640?wx_fmt=png&from=appmsg)

如果经常看汇编的小伙伴已经懂了：

```
.text:000000000008D1FC                 STP             X29, X30, [SP]
.text:000000000008D200                 LDR             X0, [SP,#8]
```

sub\_8D1F8的返回值 被x30 也就是lr寄存器赋值 所以 X1 = sub\_8D1F8返回地址 +0x38 = 0x8D1EC + 0x38 = 0x8d224。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYOB54ldw3qINpuvRQcCOAialrG6w8KosI6dXWWpoETIiauxeX5yvveaTg/640?wx_fmt=png&from=appmsg)

既然如此直接改跳转吧，写个脚本模式匹配下：

```
def antiBR1(start,end):
    addr = start
    while addr < end :
        insn = idc.print_insn_mnem(addr)
        op0 = idc.print_operand(addr,0)
        op1 = idc.print_operand(addr,1)
        # .text:000000000008B03C                 BL              loc_8B04C
        # .text:000000000008B040                 MOV             X1, X0
        # .text:000000000008B044                 ADD             X1, X1, #0x38 ; '8'
        # .text:000000000008B048                 BR              X1
        # match 4 instructions
        if insn == "BL" and (idc.print_insn_mnem(addr + 0xc).find("BR") != -1 or idc.print_insn_mnem(addr + 0x8).find("BR") != -1):
            # find add
            addr1 =addr
            while 1:
                str = get_instruction_at_address(addr1)
                if str != None:
                    if str.find("ADD") != -1:
                        break
                addr1 = addr1 + 4
            opeValue = idc.get_operand_value(addr1,2)
            print("find add: %x" % opeValue)
            # patch addr B (addr +4 + opeValue)
            code,count =ks.asm("B "+ hex(addr + 4 + opeValue),addr)
            print(hex(addr))
            ida_bytes.patch_bytes(addr, bytes(code))
        addr = addr + 4
```

修复后：

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYLSyxU9vYFtcI7j4PkUnJ1eZibRQpAZg8YE3aPf7Z5jlqb83N4BWf6aA/640?wx_fmt=png&from=appmsg)

#

```
二

花指令
```

可以看到一排奇怪的东西：

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYK9JNfBrp3zQ5hicSka5SgXQe5SQv5riacT8icIQ2mYIUBkEbrnq2ibPrlA/640?wx_fmt=png&from=appmsg)

正常程序怎么会有呢，看看汇编：

```
.text:000000000008D53C loc_8D53C                               ; CODE XREF: sub_8D170:loc_8D530↑j
.text:000000000008D53C                 MRS             X1, NZCV
.text:000000000008D540                 MOV             X0, XZR
.text:000000000008D544                 CMP             X0, XZR
.text:000000000008D548                 MSR             NZCV, X0
.text:000000000008D54C                 B.NE            loc_8D558
.text:000000000008D550                 CLREX
.text:000000000008D554                 BRK             #3
.text:000000000008D558
.text:000000000008D558 loc_8D558                               ; CODE XREF: sub_8D170+3DC↑j
.text:000000000008D558                 MSR             NZCV, X1
```

MSR NZCV, X0  x0 = 0 所以zf位为0

所以B.NE 恒成立，所以啥事没干。所以可以直接nop。

简单的看下逻辑：

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUY4nbwhpVUORjAfcibbP70D5b7rjPzcqKicZFicO1Bb14GdgKIXkvM9VcHg/640?wx_fmt=png&from=appmsg)

0x8d240 在这个函数内，所以不是代码自解码，就是校验。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYEexrIvsyVByiacLFy8KzjBdTiaNHDlUMfhyMYG5yFnI4VY8bHxH03cqA/640?wx_fmt=png&from=appmsg)

查看sub\_13C704：

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUY9iaajQYTNXe2vI2ynfnmYrq7DyksBS8cvztiaWVDKctn1c4gHNYPM1xw/640?wx_fmt=png&from=appmsg)

那就是检验咯，不管。下一个函数 sub\_13DC3C

修复后发现f5没东西：

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYoqzjYhlxJkOK9yMibkSUia8daxT5pIUglbrKyROM0oquK6ETrK2v9QoQ/640?wx_fmt=png&from=appmsg)

这怎么可能，切换到汇编，研究后：

```
.text:000000000013DCE4 000              MOV             X30, X17
.text:000000000013DCE8 000               SUB             SP, SP, #0x50 ; 'P'
.text:000000000013DCEC 050              STP             X29, X17, [SP,#0x50+var_10]
.text:000000000013DCF0 050              ADD             X29, SP, #0x50+var_10
.text:000000000013DCF4 050              STUR            X0, [X29,#-0x10]
.text:000000000013DCF8 050              STUR            X1, [X29,#-0x18]
.text:000000000013DCFC 050            STR             X0, [SP,#0x50+var_30]
```

```
.text:000000000013DD94 050              LDR             X9, [SP,#0x50+var_30]
.text:000000000013DD98 050              LDR             X10, [SP,#0x50+var_38]
.text:000000000013DD9C 050              STR             X9, [X10,#8]
```

var\_38 = x29 x29指向存放 x29 x30的栈地址 所以STR X9, [X10,#8] 等价于 x30 = x9 x0 是参数 所以回上一个函数。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYlGeyrklEhUqgQib5v1GYLpdCqria8hKo2NreYVuAPhIRCObJwmt0qqsQ/640?wx_fmt=png&from=appmsg)

去看看吧 sub\_8d5c8

```
三

OLLVM
```

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYJNgHnpl2kTjbXEW075oeqUByKUM5wUERx6MGrQPqXUMxX8QGU92orA/640?wx_fmt=png&from=appmsg)

####

#### 标准控制流平坦化

这里简单介绍什么是控制流平坦化

源代码

```
if(temp){
    print("ok");
    return 1
}
else{
    print("no");
     return 2
}
```

经过平坦化后

```
var flowState = 0;
while(1)
{
    switch(flowState):
        case 0:
            if(temp){
                flowState = 1
            }
            else{
                flowState = 2
            }
            break
        case 1:
            print("ok");
            flowState = 3
        case 2:
            print("no");
            flowState = 4
        case 3:
            return 1
        case 4:
            return 0
}
```

可以看到一个 while switch 的结构，其中flowState 负责控制整个流程，这个就是平坦化的基本原理。可以看到8行普通的代码被膨胀到了23行，假如我再平坦化 一次呢，我们会发现随着平坦化的越来越多，肉眼阅读的能力也越来越困难。

下面介绍一个我从国外看到的方案 https://hex-rays.com/blog/hex-rays-microcode-api-vs-obfuscating-compiler

###### 1.计算支配节点

下面画一个简单的cfg图

```
0
                |
                1
              /   \
            2       3
          /  \     /  \
         4      5      6
```

如果走到某一个节点2 必须经过另外一个节点1 那么 2 被 1 支配 1 是 2的支配节点。

通过bitset 可以快速计算出来

0: 0
1: 1
2:0,1
3: 0,1
4:0,1,2
5:0,1,2,3
6:0,1,3

将其反转，可得0 是所有节点的支配节点。

有什么用？仔细看平坦化的代码，可以发现 while 会被所有节点支配，所以控制流分发快，必定被所有节点支配，由此定位到了分发块。

###### 2.路径计算

我们来看，如果从0要走到5，有几种路径
0125
0135

将cfg填充内容

```
0
            flowState = 0
                |
                1
              /   \
            2       3
    flowState = 1  flowState=2
          /  \     /  \
         4      5      6
         |      |       |
         1      1       1
```

可以得到 0125 flowState = 1， 0124 flowState = 2，那么如果计算支配节点的所有路径，是不是可以得到所有 flowState 的状态。

###### 状态指向计算

通过switch，可以轻松得到状态指向的地址

######

###### 修改控制流

将每一个状态所对应的地址，连接

#####

##### 死代码消除

检查每一个没有前继节点的节点，删除，反编译器自动优化

######

###### 活跃变量分析

假设0节点 flowState = 0 1，节点flowState参与，2节点中 flowState = 1 ，那么 flowState 1节点将被删除，反编译器自动优化。

#### 反混淆

接下来回到这个demo

将他转换成cfg
![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fm5LDGBg63J3rC9p25bMUYvjwTovElFld1N8HOic0Iuv3cOGENriczsq6Aq4f2MCG5JZU3Aprgndng/640?wx_fmt=png&from=appmsg)

###### 计算支配节点

计算支配节点 为0

######

###### 路径状态计算

...