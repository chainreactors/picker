---
title: 2025解题领红包之七 Windows高级Writeup
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141771&idx=1&sn=e4e4287f578fb33365c6d94e07492a52&chksm=bd50a6df8a272fc91b0a7ecb71f3fee9274f213257935579a69a9ecb72dc298bcf3632fcb9bb&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2025-02-16
fetch_date: 2025-10-06T20:36:55.987570
---

# 2025解题领红包之七 Windows高级Writeup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZIlHkuUsWIQ0ia6SwBqhgjNSkGaSTROkwPRcaCfI41QcuwW6p2C3dRxayicODf9HicVWWXz8KY7pxFug/0?wx_fmt=jpeg)

# 2025解题领红包之七 Windows高级Writeup

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：Command （排行榜第五名同学）**

### 前言

又过了一年, 终于能做出高级题了, 也马上就要中考了...... 嗯......

顺带发现还有一种答案 (同样提示Correct但交上去不认可...... 后来证实是题目设计不足) 文中也将写到

(就是`客户端只验证key，服务端验证key和生成key的参数，如果本地验证通过，服务端通不过，请检查key参数`这个提示的来源)

### 正常解法

#### 找main函数

拖进IDA, main是这么个东西

```
 复制代码 隐藏代码
int __fastcall main(int argc, const char **argv, const char **envp)
{
  return ((__int64 (__fastcall *)(int, const char **, const char **))off_140026AD8)(argc, argv, envp);
}
```

而`off_140026AD8`如果你直接点进去, 你会发现他指向的是一个虚假的函数`sub_140001390`

```
 复制代码 隐藏代码
mov     eax, 0FFFFFFFFh
retn
```

此时需要要使用IDA的Xrefs(X)寻找`off_140026AD8`的引用,

可以发现在`sub_140001190`进行判断后被重新赋值为`sub_1400017A0`

```
 复制代码 隐藏代码
__int64 sub_140001190()
{
  __int64 result; // rax
  __int64 (__fastcall *v1)(); // rcx

  result = sub_140001C50(0LL, 0LL);
  v1 = off_140026AD8;
  if ( !result )
    v1 = sub_1400017A0;
  // ......底部省略一堆+16
  return result;
}
```

跟进`sub_1400017A0`, 可以发现这才是真正的main函数!

#### 算法分析

> 先说一下椭圆曲线加密的一些知识
>
> 椭圆曲线 y²= x³+ax+b (mod p)
>
> a 和 b 决定了曲线的形状.
>
> p 是素数, 定义了有限域. 所有运算都在该域内进行.
>
> G 是椭圆曲线上的一个特定点, 通常是曲线的"基点". 它是所有其他点的基础, 用于生成公钥, 是一个在曲线上的点, Gx与Gy是已知的.

概括(不想看代码的可以直接看这个):

程序先将UID与整十秒的时间戳(10s后过期)进行异或然后平方并转为字符串 (如果字符串长度超过16就截断)

程序中使用了椭圆曲线加密算法(ECC), 而`sub_1400013B0`(代码中`point_add`)是点加法运算

然后将用户输入的字符串转为数组 (一次6个字符然后parseInt, 数组长度为108/6=18)

并将Gx, Gy (定值) 通过ECC进行加密, 然后将刚才数组中最后两项作为解密时的a, p

并对前16项进行`(char) ((IntArray[i] + -10 * Gy - i * 10202) / Gx)`得到字符串并与UID操作后得到的字符串进行比较 (i为索引, IntArray为数组)

```
 复制代码 隐藏代码
__int64 sub_1400017A0()
{
  __int64 a; // r12
  __int64 Gx; // r14
  __int64 Gy; // r15
  int v4; // r13d
  int FlagLength; // ecx
  _BYTE *v6; // rax
  __int64 v7; // rsi
  char *Flag_1; // rdi
  __int64 v9; // rbx
  __int64 v10; // rbx
  __int64 v11; // rdx
  __int64 v12; // rdi
  __int64 v13; // rsi
  __int64 p; // r13
  __int64 v15; // rbx
  __int64 v16; // r8
  __int64 de_p; // r14
  __int64 *v18; // rbx
  __int64 de_a; // r15
  __int64 v20; // r12
  unsigned __int64 x1; // rcx
  __int64 y1; // rax
  __int64 v23; // rbx
  int v24; // eax
  const char *v25; // rcx
  __int64 d; // [rsp+40h] [rbp-C0h]
  __int64 res[2]; // [rsp+48h] [rbp-B8h] BYREF
  __int64 result[2]; // [rsp+58h] [rbp-A8h] BYREF
  char Format[4]; // [rsp+68h] [rbp-98h] BYREF
  char a1[4]; // [rsp+6Ch] [rbp-94h] BYREF
  char v31[4]; // [rsp+70h] [rbp-90h] BYREF
  char v32[4]; // [rsp+74h] [rbp-8Ch] BYREF
  unsigned __int64 UID; // [rsp+78h] [rbp-88h] BYREF
  __int64 IntArray[18]; // [rsp+80h] [rbp-80h] BYREF
  char Str1[32]; // [rsp+110h] [rbp+10h] BYREF
  char Str2[32]; // [rsp+130h] [rbp+30h] BYREF
  _OWORD FlagInput[8]; // [rsp+150h] [rbp+50h] BYREF

  a = ::a;
  Gx = ::Gx;
  Gy = ::Gy;
  d = ::d;
  res[0] = ::p;
  // 上述值在sub_140001000中被sub_140001520初始化; a, d与时间有关
  printf_0_0(::Format);
  printf_0_0(InputYourUID);
  scanf_s_0(::Format, &UID);
  if ( UID - 1 > 0x5F5E0FE )
  {
    printf_0_0(&Error);
    exit(-1);
  }
  UID ^= 60 * (time(0LL) / 60) / 10;
  sprintf_s<32>((char (*)[32])Str2, ::Format, abs64(UID * UID)); // UID与时间取整之后除以10得到的值进行异或然后平方
  Str2[16] = 0;
  memset(FlagInput, 0, sizeof(FlagInput));
  printf_0_0(InputYourKey);
  if ( scanf_s_0(asc_140026AC4, FlagInput, 128LL) )
  {
    v4 = 0;
    FlagLength = 0;
    v6 = FlagInput;
    do
    {
      ++FlagLength;
      ++v6;
    }
    while ( *v6 );
    if ( FlagLength == 108 * (FlagLength / 108) ) // 判断长度是否为108
    {
LABEL_10:
      v7 = 0LL;
      Flag_1 = (char *)FlagInput + 1;
      a1[2] = 0;
      v31[2] = 0;
      v32[2] = 0;
      do
      {
        a1[0] = *(Flag_1 - 1);
        a1[1] = *Flag_1;
        v31[0] = Flag_1[1];
        v31[1] = Flag_1[2];
        v32[0] = Flag_1[3];
        v32[1] = Flag_1[4];
        v9 = 100 * ParseInt(a1);
        v10 = 100 * (v9 + ParseInt(v31));
        Flag_1 += 6;
        IntArray[v7++] = v10 + ParseInt(v32);
      }
      while ( v7 < 18 );                        // 将输入的Key每六个字符一组, 解析数值, 变成一个长度为18的数组(IntArray)
                                                // (ParseInt是10进制, 解析时遇到非数字停止)
      v11 = d;
      v12 = Gx;
      v13 = Gy;
      if ( d == 1 ) // d will never be 1
      {
        v16 = 0LL;
      }
      else
      {
        p = res[0];
        v15 = d - 1;
        result[0] = d - 1;
        do
        {
          point_add(res, v12, v13, Gx, Gy, a, p);// 椭圆曲线加密(ECC), 问deepseek才知道... 加密的是v12, v13 (初始值为Gx, Gy)
          v12 = res[1];
          v13 = res[0];
          --v15;
        }
        while ( v15 );
        v11 = d;
        v4 = 0;
        v16 = result[0];
      }
      de_p = IntArray[17];                      // 此处从数组中下标为16与17的地方读出a与p, 我们需要控制这两个值与上方加密时的a与p相等
      v18 = IntArray;
      de_a = IntArray[16];
      v20 = 0LL;
      res[0] = (__int64)IntArray;
      Str1[0] = 0;
      *(_DWORD *)Format = 25381; // %c
      do
      {
        x1 = v12;                               // 解密后为Gx
        y1 = v13;                               // 解密后为Gy
        if ( v11 != 1 )
        {
          v23 = v16;
          do
          {
            point_add(result, x1, y1, v12, v13, de_a, de_p);// 根据我们传进来的a与p解密刚才加密的Gx, Gy
            x1 = result[1];
            y1 = result[0];
            --v23;
          }
          while ( v23 );
          v18 = (__int64 *)res[0];
        }
        sprintf_s_0_1(&Str1[v4], 2uLL, Format, (unsigned int)(char)((*v18 + -10 * y1 - v20) / x1));// 从数组中开始读数, 向Str1中追加经过处理后的字符
        v11 = d;
        ++v18;
        ++v4;
        res[0] = (__int64)v18;
        v20 += 10202LL;
        v16 = d - 1;
      }
      while ( v20 < 163232 );                   // 共循环16次 (步长10202)
      Str1[16] = 0;
      v24 = strncmp(Str1, Str2, 0x10uLL);       // 比较是否不一致 (注意, 是不一致)
      v25 = Correct;
      if ( v24 )
        v25 = &Error;
      printf_0_0(v25);
      return 0LL;
    }
  }
  // 几个else省略
}
```

#### 解题

如果要解密被ECC加密后的Gx与Gy, 我们需要让a和p与加密时的相等 (即: `IntArray[16] == ::a && IntArray[17] == ::p`)

那么我们就得想办法获取到加密时的a与p, 还要得到Gx与Gy的值, 这里我选择用IDAPython直接Hook

如果要Hook, 选哪里呢? 我们不难注意到开头有这样一段代码

```
 复制代码 隐藏代码
a = ::a;
Gx = ::Gx;
Gy = ::Gy;
d = ::d;
res[0] = ::p;
```

```
 复制代码 隐藏代码
; 这是上面那段代码对应的汇编
mov     r12, cs:a
mov     r14, cs:Gx
mov     r15, cs:Gy
mov     [rsp+200h+d], rax
mov     rax, cs:p
mov     [rsp+200h+res], rax  ; 我选择在这里Hook, 获取寄存器值, 此时rax为p, r12为a, r14为Gx, r15为Gy, 完美!
```

这里正好有我们所需要的a, Gx, Gy, p, 还相当好Hook

于是可以得到如下代码

```
 复制代码 隐藏代码
import idaapi
import idc
import time

# s是最后需要在解密时得到的字符串
def build_str(s: str, Gx: int, Gy: int) -> str:
    res = ''
    for i, v20 in zip(s, range(0, 163232, 10202)): # 步长10202模拟代码中v20 += 10202LL
        res += str(ord(i) * Gx + v20 + 10 * Gy).zfill(6) # 补齐6位
    return res

class MyDbgHook(idaapi.DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        if ea == 0x1400017F8:
            UID = 1354181  # 此处写UID
            UID ^= int(60 * (int(time.time()) // 60 / 10))
            # r14: Gx, r15: Gy, r12: a, rax: p
            print(build_str(str(UID * UID)[:-1] if len(str(UID * UID)) == 17 else str(UID * UID), idc.get_reg_value("r14"), idc.get_reg_value("r15")) + str(idc.get_reg_value("r12")).zfill(6) + str(idc.get_reg_value("rax")).zfill(6))
        return 0

hook = MyDbgHook()
hook.hook()
idc.add_bpt(0x1400017F8)  # 刚才那行汇编的地址
```

### 意料之外的解法

#### 先说一下

第一遍做完之后提交了好几次, 都提示不对, 但本地就是`correct`，然后发了个站务帖.

H大后来的回复 (嗯, 不算错但也不对...?)

> 找到原因了，算题目设计不足，你看下主题中昨天的提醒，主要还是让你找到程序自己的私钥，你改了私钥不行，服务端这边有验证，bin这边倒是没验证。  还在和作者沟通，看看是修复bin的验证还是增加一个说明。
>
> ---
>
> 不算错，只是还差一点点，加油哈~

后来服务端就修复了, 应该是加了个提示(?)

#### 我当时的想法

一开始做题我并没有和现在一样对ECC有一定的了解, 也不知道要解出那俩参数 (甚至没看提示直接莽)

不过我发现了一点点规律......

同样是那段代码:

```
 复制代码 隐藏代码
de_p = IntArray[17];                      // 此处从数组中下标为16与17的地方读出a与p
v18 = IntArray;
de_a = IntArray[16];
v20 = 0LL;
res[0] = (__int64)IntArray;
Str1[0] = 0;
*(_DWORD *)Format = 25381; // %c
do
{
  x1 = v12;                               // 解密后甭管是啥, 总之10s内, 输入相同a, p的话这个值不会变 (rcx)
  y1 = v13;...