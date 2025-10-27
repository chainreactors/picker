---
title: 强网杯2024 ez_vm 手撕VM + DFA Attack Whitebox AES
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587796&idx=1&sn=5de696fc1e5824f4f7ab11824bc841b9&chksm=b18c221e86fbab080ca78c02ab1916310c9ec38c8e6955f6eadb9d2d3f83739db17910f49f90&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-28
fetch_date: 2025-10-06T19:39:05.393218
---

# 强网杯2024 ez_vm 手撕VM + DFA Attack Whitebox AES

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8El0Ez7PG2GXWMuh1xOTJlOibIlic4z3KHATqdgLmvYNOhZILUojDSClLs9yiaUjDcoAyy76luteQEpw/0?wx_fmt=jpeg)

# 强网杯2024 ez\_vm 手撕VM + DFA Attack Whitebox AES

SleepAlone

看雪学苑

```
一

题目思路
```

首先这道题是一个栈虚拟机+JIT，在栈虚拟机中完成白盒AES加密过程。所以做出这道题需要：

1. 逆向虚拟机的handler

1. 写出对应的parser，将handler转换成等价的x64汇编指令
2. 将x64汇编指令汇编交给ida分析（二次逆向）
3. 为了更好分析，为b.中的分析文件添加VM的结构体信息
4. 其中有一个极为特殊的handler，为JIT的实现。

2. 对白盒AES进行DFA攻击

1. 确定最后一次列混淆的时机，多patch几次，恢复last round key
2. 根据last round key恢复初始密钥

3. aes解密

总之，要工程量有工程量，要难度有工程量。

```
二

题目背景
```

```
chal.exe 3766323862633565396633663134393532356365646630626636363036636630
:)
```

一个exe程序 接收一个参数（flag）

flag正确输出:)

flag错误输出:(

```
三

剖析bytecode格式
```

##

首先在sub\_14009A760中，发现了一个巨大的swicth case，在sub\_14009A760调用的前有寄存器保存，后有寄存器恢复，显然sub\_14009A760就是vm\_dispatcher,在switch中的case就是不同的handler了。

bytecode就相当于VM中的二进制代码一样，而handler就是bytecode的解释器，可以理解为vcpu，

下面拿case 0来剖析bytecode的格式。

### case 0 - push imm8/16/32/64

```
switch ( (char)_RAX )
    {
      case 0:
        __asm { tzcnt   eax, ebx; jumptable 000000014009A7F8 case 0 }
        v86 = _RAX;
        switch ( v86 )
        {
          case 0LL:
            v87 = *(unsigned __int8 *)v10;
            v88 = a1;
            goto LABEL_260;
          case 1LL:
            v87 = *(_WORD *)v10;
            v88 = a1;
LABEL_260:
            push_16(v88, v87);
            break;
          case 2LL:
            push_32(a1, *v10);
            break;
          case 3LL:
            push_64(a1, *(_QWORD *)v10);
            break;
          case 4LL:
            JUMPOUT(0x14009A190LL);
        }
```

可以看到大switch中还有个小switch，细看小switch中每个case的逻辑都相同只不过操作数的大小不同，其中push\_16的代码为：

```
__int64 __fastcall sub_14009A6B0(__int64 a1, __int16 a2)
{
  __int64 result; // rax

  result = *(_QWORD *)(a1 + 8); // vrsp
  if ( result == *(_QWORD *)(a1 + 536) )
    BUG();
  *(_QWORD *)(a1 + 8) = result - 2;
  *(_WORD *)(result - 2) = a2;
  return result;
}
```

可以看出来是内存模拟push的操作，最后写入内存的是2字节的数据，所以是push\_16其他以此类推。

`你可能疑问，为什么没有push8，这里我的理解为：本来x84_64架构中，只有16位/32位/64位，即使在16位下，push 1，实际上也是压入2个字节，即压栈时会根据CPU模式扩展到对应位数`

调试查看case 0 + case 3 bytecode的内容为：

```
00 08 20 00 00 00 00 00 00 00
```

op opsize [operand]

| 寄存器指向 | bytecode格式 | 内存大小 | 注释 |
| --- | --- | --- | --- |
| rdi→ | op | 1 byte | 大swicth |
|  | opsize | 1 byte | 小switch |
| [rsi]→ | operand | 取决于op和opsize | if exist |
|  | operand2 | operand决定 | if exist |

在这个例子中 就存在operand 为 20 00 00 00 00 00 00 00，长度为8 byte，与opsize=08对应。

存在operand2的例子会在后面讲到，这里先埋个坑。

```
四

handler逆向
```

### case 0

根据前面的分析。总之，这就是一个push imm的指令，注意这是在栈虚拟机的实现，在虚拟机中有大量的push，pop，这些数push进去后面又pop出来拿来用，翻译x64等效指令就是：

```
mov reg, imm
```

`为什么等效？mov reg, imm 其实就是占用一个reg存放imm（reg_index+1），对应于栈虚拟机的栈空间。相应的pop时候，释放栈空间，翻译时reg_index需要减1。（reg_index的动态加减其实就像模拟了rsp的移动）`

### case 1 : load

```
case 1:
        v89 = (__int16 *)pop_64(a1);
        __asm { tzcnt   ecx, ebx }
        v91 = _RCX;
        switch ( v91 )
        {
          case 0LL:
            v13 = *(unsigned __int8 *)v89;
            goto LABEL_5;
          case 1LL:
            v13 = *v89;
            v8 = a1;
            goto LABEL_6;
          case 2LL:
            v58 = *(_DWORD *)v89;
            goto LABEL_289;
          case 3LL:
            v138 = *(_QWORD *)v89;
            goto LABEL_317;
        }
```

可以看出时load8/16/32/64的操作，对应的操作可以简化为push(\*pop())，所以对应的x64指令为：

```
mov reg, [reg]
```

### case 3，5，6 :store

```
case 5:
        _RAX = (_QWORD *)pop_64(a1);
        v75 = _RAX;
        if ( (_DWORD)_RBX == 4 )
        {
          *_RAX = (unsigned int)pop_32(a1);
        }
        else
        {
          __asm { tzcnt   eax, ebx }
          v130 = _RAX;
          switch ( (unsigned __int64)v130 )
          {
            case 0uLL:
LABEL_155:
              *v75 = pop_16(a1);
              break;
            case 1uLL:
LABEL_158:
              *(_WORD *)v75 = pop_16(a1);
              break;
            case 2uLL:
LABEL_156:
              *(_DWORD *)v75 = pop_32(a1);
              break;
            case 3uLL:
LABEL_157:
              *(_QWORD *)v75 = pop_64(a1);
              break;
          }
        }
```

case 3，5，6都为store操作，只有细微的差别，这里拿case 5来分析。

操作可以简化为\*push() = pop(),翻译为x64指令：

```
mov [reg],reg
```

###

### case 7,8,0xb,0xd,0xe,0xf

```
case 7:
        __asm { tzcnt   eax, ebx; jumptable 000000014009A7F8 case 7 }
        v77 = _RAX;
        switch ( v77 )
        {
          case 0LL:
            v78 = pop_16(a1);
            v79 = pop_16(a1);
            v80 = v79 + v78;
            v81 = *(_QWORD *)(a1 + 0x210) & 0x3F77D7LL;
            if ( v79 < 0 )
            {
              if ( v80 < 0 || v78 >= 0 )
                goto LABEL_103;
            }
            else if ( v80 >= 0 || v78 < 0 )
            {
LABEL_103:
              v82 = v81 & 0x3F7F17;
              v83 = v81 | 0x80; //SF
              if ( v80 >= 0 )
                v83 = v82;
              v84 = v83 & 0x3F7F92;
              v85 = v83 | 0x40;// ZF
              if ( v80 )
                v85 = v84;
              *(_QWORD *)(a1 + 0x210) = v85 & 0x3F7FD2 | (unsigned __int64)(unsigned __int8)((4 * !__SETP__(v80, 0)) | ((unsigned __int8)v80 < (unsigned __int8)v79));//PF
              v13 = (unsigned __int8)v80;
              goto LABEL_5;
            }
            LODWORD(v81) = v81 | 0x800; //OF
            goto LABEL_103;
            case 1LL:
            //.....
```

case 7,8,0xb,0xd,0xe,0xf 分别对应add，sub，div，mul，and，or，逻辑类似

这里拿case 7分析，可以看到除了push(pop() + pop())的操作外，还有一系列其他的操作，其实这里是在设置eflags， \*(\_QWORD \*)(a1 + 0x210)存储了虚拟机的eflags。翻译为：

```
add reg, reg
```

sub，div，mul，and，or 以此类推。

### case 0x12: cmp

```
case 18:
        __asm { tzcnt   eax, ebx; jumptable 000000014009A7F8 case 18 }
        v102 = _RAX;
        switch ( v102 )
        {
          case 0LL:
            v103 = pop_16(a1);
            v104 = pop_16(a1);
            v105 = v104 - v103;
            v106 = *(_QWORD *)(a1 + 528) & 0x3F77D7LL;
            if ( v104 >= 0 )
            {
              if ( v105 >= 0 || v103 < 0 )
                goto LABEL_134;
LABEL_133:
              LODWORD(v106) = v106 | 0x800;
              goto LABEL_134;
            }
            if ( v105 >= 0 && v103 < 0 )
              goto LABEL_133;
LABEL_134:
            v107 = v106 & 0x3F7F17 | v105 & 0x80;
            v108 = v107 + 64;
            if ( v104 != v103 )
              v108 = v107;
            *(_QWORD *)(a1 + 528) = v108 & 0x3F7FD2 | (unsigned __int64)(unsigned __int8)(((unsigned __int8)v104 < (unsigned __int8)v103) | (4 * !__SETP__(v104, v103)));
            goto LABEL_7;
           case 1LL:
           //.....
```

乍一看和sub没什么区别，其实不如在case0x12中，v105 = v104 - v103后，并没有push(v105),但是保存了改变的标志位，符合cmp的特征，翻译为：

```
cmp reg，reg
```

case 0x15: jmp

```
case 21:
        v224 = *(_QWORD *)(a1 + 0x210);
        switch ( *(_BYTE *)v11 )
        {
          case 0:
            goto ture_jmp;                      // jmp
          case 1:
            goto LABEL_370;
          case 2:
            goto LABEL_363;
          case 3:
            if ( (v224 & 0x40) == 0 && (v224 & 1) == 0 )// ja
              goto false_jmp;                   // jbe
            goto ture_jmp;
          case 4:
            if ( (v224 & 0x40) != 0 || (((unsigned __int8)v224 ^ 1) & 1) == 0 )// jbe
              goto false_jmp;                   // ja
            goto ture_jmp;
          case 5:
            if ( (((unsigned __int8)v224 ^ 1) & 1) == 0 )// jb
              goto false_jmp;                   // jae
            goto ture_jmp;
          case 6:
            if ( ((v224 & 0x80u) != 0LL) != ((v224 & 0x800) != 0) )// jl
              goto ture_jmp;                    // jge
            goto LABEL_370;
          case 7:
            if ( ((v224 & 0x80u) != 0LL) != ((v224 & 0x800) == 0) )// jg
              goto LABEL_363;                   // jle
            goto false_jmp;
          case 8:
            if ( ((v224 & 0x80u) != 0LL) != ((v224 & 0x800) == 0) )// jg
              goto ture_jmp;
LABEL...