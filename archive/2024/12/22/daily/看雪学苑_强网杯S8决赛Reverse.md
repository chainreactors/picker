---
title: 强网杯S8决赛Reverse
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587593&idx=2&sn=d75b7bc1f33210cf17b4f9d3c8bfa298&chksm=b18c214386fba855317cd3ddece1d0add96f22753a325b45ea7df0604c8018e3a2d0d7bde360&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-22
fetch_date: 2025-10-06T19:37:36.242756
---

# 强网杯S8决赛Reverse

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8Kpdstndjs7NIU0SejibGIoPBmgS7icWiaPtbmlpPK3xt0PEBFXFe18x4pA/0?wx_fmt=jpeg)

# 强网杯S8决赛Reverse

xi@0ji233

看雪学苑

复盘一下强网决赛的Reverse题。

```
一

S1mpleVM
```

##

附件下载：*https://xia0ji233.pro/2024/12/11/qwb2024\_final\_reverse/S1mpLeVM\_6d429db3ceeba8f95131c477020ee899.zip*

题目名字已经很明显的告诉你了，就是 vm 逆向。

### 基本分析

入口其实没啥，就是输入 32 长度的 passcode 然后校验，启动方式是`./secret_box.exe quest`命令行传参。

可以找到最关键的函数`sub_140001D30`就是 VM 入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8Kp3pfKLPkpqBaFpOhYib06a7TH0KcLsFVOcp4yupy9To1AkWzJDVrtXw/640?wx_fmt=png&from=appmsg)

这个函数里面很明显的 vm\_handler

```
__int64 __fastcall vmrun(char *input, char *vmcode)
{
  //some defs for local variable
  v2 = 0LL;
  v3 = *vmcode - 16;
  v5 = v48;
  v6 = vmcode + 1;
  while ( 2 )
  {
    switch ( v3 )
    {
      case 0u:
        if ( v2 )
        {
          v9 = v2;
          v2 = (signed int *)*((_QWORD *)v2 + 1);
          v7 = *v9;
          free(v9);
          if ( v2 )
          {
            v10 = v2;
            v2 = (signed int *)*((_QWORD *)v2 + 1);
            v8 = *v10;
            free(v10);
          }
          else
          {
            v8 = 0x80000000;
          }
        }
        else
        {
          v7 = 0x80000000;
          v8 = 0x80000000;
        }
        v11 = (signed int *)j__malloc_base(0x10uLL);
        *v11 = v7 % v8;
        goto LABEL_53;
      case 1u:
        //...
LABEL_53:
      *((_QWORD *)v11 + 1) = v2;
      v2 = v11;
    }
  }
}
```

不难发现，v3 是所谓的 opcode，v6 是 PC 指针，并且 vmcode 是实际的字节码`- 0x10`，下面来一个个分析这些 vm 的指令。

首先是 0 号指令，做了一个较为复杂的指针操作。这里初看可能啥也看不明白，但是可以发现最下面它分配了 0x10 的空间同时又 v7 和 v8 做模运算了赋值给 v11 指向的地址。

操作完成之后又执行了`*((_QWORD *)v11 + 1) = v2;`和`v2 = v11;`，如此种种的迹象显然不难让人联想到一种结构：链表。如果将划分的 0x10 字节内存进行划分，也可以看出，前八个字节存储数据，后八个字节存储指针。

`shift+F1`打开 IDA 的`local type`窗口，按`insert`键插入结构体的定义：

```
struct LinkEntry{
    signed val;
    LinkEntry * next;
}
```

将 v11 和 v2 定义修改之后，IDA 将展示如下的伪代码：

```
case 0u:
if ( v2 )
{
    v9 = &v2->val;
    v2 = v2->next;
    v7 = *v9;
    free(v9);
    if ( v2 )
    {
        v10 = &v2->val;
        v2 = v2->next;
        v8 = *v10;
        free(v10);
    }
    else
    {
        v8 = 0x80000000;
    }
}
else
{
    v7 = 0x80000000;
    v8 = 0x80000000;
}
v11 = (LinkEntry *)j__malloc_base(0x10uLL);
v11->val = v7 % v8;
goto LABEL_53;
```

可以说，基本上是一目了然了，并且据此可以联想到一个栈的结果，将两个数 push 进栈中，再弹出来做计算，计算的结果重新入栈。

这里可以将所有 malloc 返回值接收的变量都改成`LinkEntry *`类型。

此时再来观察整个反编译的代码：

```
__int64 __fastcall vmrun(char *input, char *vmcode)
{
  LinkEntry *v2; // rdi
  unsigned int opcode; // eax
  unsigned int v5; // r14d
  char *PC; // rbp
  signed int v7; // esi
  signed int v8; // ebx
  signed int *v9; // rcx
  signed int *v10; // rcx
  LinkEntry *v11; // rcx
  int v12; // ebx
  LinkEntry *v13; // rax
  unsigned int *v14; // rcx
  unsigned int v15; // esi
  unsigned int v16; // ebx
  unsigned int *v17; // rcx
  unsigned int *v18; // rcx
  LinkEntry *v19; // rax
  unsigned int v20; // esi
  unsigned int v21; // ebx
  unsigned int *v22; // rcx
  unsigned int *v23; // rcx
  int v24; // eax
  int v25; // ebx
  LinkEntry *v26; // rax
  int v27; // esi
  int v28; // ebx
  signed int *v29; // rcx
  int *v30; // rcx
  LinkEntry *v31; // rax
  unsigned int v32; // esi
  unsigned int v33; // ebx
  unsigned int *v34; // rcx
  unsigned int *v35; // rcx
  LinkEntry *v36; // rax
  unsigned int v37; // ebx
  unsigned int v38; // esi
  unsigned int *v39; // rcx
  unsigned int *v40; // rcx
  LinkEntry *v41; // rax
  signed int v42; // esi
  signed int v43; // ebx
  signed int *v44; // rcx
  signed int *v45; // rcx
  int v46; // eax
  unsigned int v48; // [rsp+58h] [rbp+10h]

  v2 = 0LL;
  opcode = *vmcode - 16;
  v5 = v48;
  PC = vmcode + 1;
  while ( 2 )
  {
    switch ( opcode )
    {
      case 0u:
        if ( v2 )
        {
          v9 = &v2->val;
          v2 = v2->next;
          v7 = *v9;
          free(v9);
          if ( v2 )
          {
            v10 = &v2->val;
            v2 = v2->next;
            v8 = *v10;
            free(v10);
          }
          else
          {
            v8 = 0x80000000;
          }
        }
        else
        {
          v7 = 0x80000000;
          v8 = 0x80000000;
        }
        v11 = (LinkEntry *)j__malloc_base(0x10uLL);
        v11->val = v7 % v8;
        goto LABEL_53;
      case 1u:
        v12 = *PC;
        v13 = (LinkEntry *)j__malloc_base(0x10uLL);
        ++PC;
        v13->next = v2;
        v2 = v13;
        v13->val = v12;
        goto LABEL_54;
      case 2u:
        if ( v2 )
        {
          v14 = (unsigned int *)v2;
          v2 = v2->next;
          v5 = *v14;
          free(v14);
        }
        else
        {
          v5 = 0x80000000;
        }
        goto LABEL_54;
      case 3u:
        if ( v2 )
        {
          v17 = (unsigned int *)v2;
          v2 = v2->next;
          v15 = *v17;
          free(v17);
          if ( v2 )
          {
            v18 = (unsigned int *)v2;
            v2 = v2->next;
            v16 = *v18;
            free(v18);
          }
          else
          {
            v16 = 0x80000000;
          }
        }
        else
        {
          v15 = 0x80000000;
          v16 = 0x80000000;
        }
        v19 = (LinkEntry *)j__malloc_base(0x10uLL);
        v19->next = v2;
        v2 = v19;
        v19->val = v15 * v16;
        goto LABEL_54;
      case 4u:
        if ( v2 )
        {
          v22 = (unsigned int *)v2;
          v2 = v2->next;
          v20 = *v22;
          free(v22);
          if ( v2 )
          {
            v23 = (unsigned int *)v2;
            v2 = v2->next;
            v21 = *v23;
            free(v23);
          }
          else
          {
            v21 = 0x80000000;
          }
        }
        else
        {
          v20 = 0x80000000;
          v21 = 0x80000000;
        }
        v11 = (LinkEntry *)j__malloc_base(0x10uLL);
        v24 = v21 + v20;
        goto LABEL_52;
      case 5u:
        sub_1400011B0("%c", v5);
        goto LABEL_54;
      case 6u:
        v25 = *input;
        v26 = (LinkEntry *)j__malloc_base(0x10uLL);
        v26->next = v2;
        v2 = v26;
        v26->val = v25;
        goto LABEL_54;
      case 7u:
        if ( v2 )
        {
          v29 = &v2->val;
          v2 = v2->next;
          v27 = *v29;
          free(v29);
          if ( v2 )
          {
            v30 = &v2->val;
            v2 = v2->next;
            v28 = *v30;
            free(v30);
          }
          else
          {
            v28 = 0x80000000;
          }
        }
        else
        {
          LOBYTE(v27) = 0;
          v28 = 0x80000000;
        }
        v31 = (LinkEntry *)j__malloc_base(0x10uLL);
        v31->next = v2;
        v2 = v31;
        v31->val = (v28 >> v27) & 1;
        goto LABEL_54;
      case 8u:
        if ( v2 )
        {
          v34 = (unsigned int *)v2;
          v2 = v2->next;
          v32 = *v34;
          free(v34);
          if ( v2 )
          {
            v35 = (unsigned int *)v2;
            v2 = v2->next;
            v33 = *v35;
            free(v35);
          }
          else
          {
            v33 = 0x80000000;
          }
        }
        else
        {
          v32 = 0x80000000;
          v33 = 0x80000000;
        }
        v36 = (LinkEntry *)j__malloc_base(0x10uLL);
        v36->next = v2;
        v2 = v36;
        v36->val = v32 ^ v33;
        goto LABEL_54;
      case 9u:
        ++input;
        goto LABEL_54;
      case 0xAu:
        return v5;
      case 0xBu:
        if ( v2 )
        {
          v39 = (unsigned int *)v2;
          v2 = v2->next;
          v37 = *v39;
          free(v39);
          if ( v2 )
          {
            v40 = (unsigned int *)v2;
            v2 = v2->next;
            v38 = *v40;
            free(v40);
          }
          else
          {
            v38 = 0x80000000;
          }
        }
        else
        {
          v37 = 0x80000000;
          v38 ...