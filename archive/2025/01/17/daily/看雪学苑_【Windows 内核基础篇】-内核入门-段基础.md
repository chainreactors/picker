---
title: 【Windows 内核基础篇】-内核入门-段基础
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588707&idx=1&sn=d94feda75be18bc50c1a4e1b3e8562dc&chksm=b18c26a986fbafbf5d4bae96661feee0121f0b4a7d68ec53bf20422ad8be57c2d8885cbde9a1&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-17
fetch_date: 2025-10-06T20:10:50.797435
---

# 【Windows 内核基础篇】-内核入门-段基础

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4UwetPywrs8LhDuTuPUMN8FpxIWptXfGhwE9oGbV8JJzv9Ngic6wr2rg/0?wx_fmt=jpeg)

# 【Windows 内核基础篇】-内核入门-段基础

Gushang

看雪学苑

保护模式下通过段划分内存的权限以及访问的权限。

x86 和 x64都有六个段寄存器(Segment Register)：

```
DS: Data Segment 数据段 可读可写不可执行
CS: Code Segment 代码段 可读可执行不可写
SS: Stack Segment 堆栈段 可读可写不可执行
ES、FS、GS
```

根据intel白皮书3a的介绍，CPU额外提供了三个数据段寄存器，可以作为程序额外的段，正常情况下可能只使用到DS、CS、SS这三个段寄存器。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4dESGhfZMUklOHbFDo0ALIhQsPwtxPsQGB1iblgb2DstjTmTzQm4bmIA/640?wx_fmt=other&from=appmsg)

数据段中一般为全局变量，而局部变量一般会放入堆栈段中：

```
// test.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <Windows.h>

int value = 10;

int _tmain(int argc, _TCHAR* argv[])
{
    OpenProcess(0, 0, 0);
    __asm {
        mov eax, value;
    }

    return 0;
}
```

此时将value定义在main函数外，视为全局变量，可以看到，编译器会将该变量放在DS段中：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4PR3QDdyicJSzxsMV5DlU4v01c0eN0cMlCgTYXHdgWiaQcTQ7m283VLXg/640?wx_fmt=other&from=appmsg)

当将value定义为局部变量时：

```
// test.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <Windows.h>

int _tmain(int argc, _TCHAR* argv[])
{
    char a[] = "1234";
    int value = 10;
    __asm {
        mov eax, value;
    }

    return 0;
}
```

此时的段会识别成SS堆栈段：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN459DbR7r77y3lPrJIrGhEOZwuN46ibsCCdUcLombDaoqu0Q09ko4KnWA/640?wx_fmt=other&from=appmsg)

###

### 段选择子（Segment Selector）

通过段选择子（Segment Selector）来确定段的属性，默认`UserMode`可见部分：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4kxRxzykDsC5BJFjAMb03Br0gbdG0jhn9ttFzFGuk44Xcc9Cx02dvsA/640?wx_fmt=other&from=appmsg)

对于段的属性描述，通过3.4.2描述：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4vKA7qBrJV6oZabGibLibFEHGbDm9qZwlvbj3XZkOClibKqJGJcTPvicDxA/640?wx_fmt=other&from=appmsg)

段选择子总共是16位，分成三部分进行解析：Table Indicator表示从LDT或者是GDT表中查找段描述符，Index则表明表的下标.

```
#include <Windows.h>
#include <iostream>

#define TI 0x04
#define RPL 0x03
#define INDEX 0xfff8

#define LDT 1
#define GDT 0

using namespace std;

void analysisSegmentSelector(WORD selector) {
    // RPL
    cout << "RPL: ";
    cout << (selector & 0x03) << endl;

    // TI
    cout << " Specifies the descriptor table to use: ";
    (selector & TI) == 1 ? cout << "LDT" << endl : cout << "GDT" << endl;

    // Index
    cout << "Index: ";
    cout << ((selector & INDEX) >> 3) << endl;
}

int main() {
    // 0000 0000 0010 0011
    WORD selector = 0x0023;
    analysisSegmentSelector(selector);
    return 0;
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4tEg552RCQ8PMJozoiawYUAPt2TlC0iaA0PRYn9NC7icuBddQDFViaCp0NQ/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN41AtWIANiaBPEkZwybT6gwWWuYHlUWxGeod8X0JVF5YJO2qqaTVAEXRA/640?wx_fmt=other&from=appmsg)

可以发现DS和SS的段选择子都是`0x0023`，而CS的段选择子是`0x001B`，通过解析可以得到都是通过GDT表进行查表，通过WinDBG中的`r gdtr`查询，r默认输出的是通用寄存器和段寄存器：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4Y5YmA9Ze9kh1IMTPNn2zicGXKU7E2jzdRrp3umuQ7MA6ACGIOB3HVVA/640?wx_fmt=other&from=appmsg)

可以通过r后跟特定寄存器查询，**这里gdtr不代表真的有gdtr这个寄存器，只是通过sdtr来存储gdt表的地址.**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN42ouAeefA2Z1DjzkGovMf1xMaWbYBlnuQvr3FIvSrAvF3Js1EkrGLYA/640?wx_fmt=other&from=appmsg)

通过`dq gdtr`或者`dq 0x80b98800`查询：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4rnrzRYViaBHRV5wkjO5icvwbMvcVSGnQniabwSyJTWXba1htZtpqFDjag/640?wx_fmt=other&from=appmsg)

### 段描述符（Segment Descriptor）

可见部分的段描述符为64位QWORD

0x0023的Index为4，所以其对应的段描述符为：`00cff300 0000ffff`

0x001B的Index为3，所以其对应的段描述符为：`00cffb00 0000ffff`

intel白皮书3.4.5 Segment Descriptor描述了段描述符的组成部分：!

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4OGGFLacsm5zaUefrVlMjYWzpoqPgvgGrRcPDylxNeygUGQkWNNv8Mg/640?wx_fmt=other&from=appmsg)

```
#include <Windows.h>
#include <iostream>

using namespace std;

#define SEG_BASE_24_31	0xff000000
#define SEG_BASE_16_23	0xff0000
#define SEG_BASE_0_15	0xffff

#define SEG_LIMIT_16_19 0x000f0000
#define SEG_LIMIT_0_15 0xffff

#define SEG_G		0x00800000
#define SEG_D_B		0x00400000
#define SEG_L		0x00200000
#define SEG_AVL		0x00100000
#define SEG_P		0x00008000
#define SEG_DPL		0x00006000
#define SEG_S		0x00001000
#define SEG_TYPE	0x00000f00

// Descriptor Type
#define SYSTEM_TYPE 0
#define CODE_DATA_TYPE 1

// Default operation size
#define BIT_16 0
#define BIT_32 1

VOID analysisSegmentDescriptorOthers(DWORD descriptor) {
    DWORD seg_G = (descriptor & SEG_G) >> 0x17;
    DWORD seg_D_B = (descriptor & SEG_D_B) >> 0x16;
    DWORD seg_L = (descriptor & SEG_L) >> 0x15;
    DWORD seg_AVL = (descriptor & SEG_AVL) >> 0x14;
    DWORD seg_P = (descriptor & SEG_P) >> 0xf;
    DWORD seg_DPL = (descriptor & SEG_DPL) >> 0x0d;
    DWORD seg_S = (descriptor & SEG_S) >> 0x0c;
    DWORD seg_TYPE = (descriptor & SEG_TYPE) >> 0x08;

    cout << "Granularity: " << hex << seg_G << endl;

    cout << "Default operation size: ";
    seg_D_B == BIT_32 ? cout << "32-bit segment" : cout << "16-bit segment";
    cout << endl;

    cout << "64-bit code segment: " << hex << seg_L << endl;
    cout << "Available for use by system software: " << hex << seg_AVL << endl;
    cout << "Segment present: " << hex << seg_P << endl;

    cout << "Descriptor privilege level: " << hex << seg_DPL << endl;

    cout << "Descriptor type: ";
    seg_S == SYSTEM_TYPE ? cout << "system" : cout << "code or data";
    cout << endl;

    cout << "Segment type: " << hex << seg_TYPE << endl;
}

VOID analysisSegmentDescriptor(DWORD64 descriptor) {
    DWORD base = ((descriptor >> 0x10) & SEG_BASE_0_15)
        ^ ((descriptor >> 0x10) & SEG_BASE_16_23 )
        ^ ((descriptor >> 0x20) & SEG_BASE_24_31 );

    DWORD limit = (descriptor & SEG_LIMIT_0_15)
        ^ ((descriptor >> 0x20) & SEG_LIMIT_16_19);

    cout << "Segment Limit: " << hex << limit << endl;
    cout << "Segment base address: " << hex << base << endl;

    analysisSegmentDescriptorOthers(descriptor >> 0x20);

}

int main() {
    // 0x0023
    // 0000 0000 0010 0011
    WORD selector = 0x0023;
    analysisSegmentSelector(selector);

    DWORD64 descriptor = 0x00cff3000000ffff;
    analysisSegmentDescriptor(descriptor);

    cout << "-------------------------------------------------" << endl;

    // 0x001B
    // 0000 0000 0001 1011
    selector = 0x001B;
    analysisSegmentSelector(selector);

    descriptor = 0x00cffb000000ffff;
    analysisSegmentDescriptor(descriptor);

    return 0;
}
```

关于段类型（Segment Type) 在3.4.5.1 Code- and Data-Segment Descriptor Types中的表Table 3-1. Code- and Data-Segment Types：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4uw44xwqedeVh48uIG6Q6UA45Gib7iccNnUHPTcHjlo8Jz80Uic7x04raw/640?wx_fmt=other&from=appmsg)

最高位区分数据或代码段：0-Data，1-Code，低三位分别表示EWA和CRA，对比前面获取到的CS和DS的段描述符，也就是在Type的位置存在区别，DS的Type为`0b0011`，CS的Type为`0b1011/`

所以这里查表后的结果是：

CS段的属性为`Code`，Description为:`Execute/Read, accessed`

DS段的属性为`Data`，Description为：`Read/Write, accessed`

```
VOID checkSegmentType(BYTE segmentType) {
    segmentType & 0x8 ? cout << "Code " : cout << "Data ";
    cout << endl;
    cout << "Description: ";
    if (segmentType & 0x8) {
        cout << "Execute ";
        if (segmentType & 0x4) cout << "Conforming ";
        if (segmentType & 0x2) cout << "Read ";
        if (segmentType & 0x1) cout << "Accessed ";
    }
    else {
        cout << "Read ";
        if (segmentType & 0x4) cout << "Expand-down ";
        if (segmentType & 0x2) cout << "Write ";
        if (segmentType & 0x1) cout << "Accessed ";
    }
    cout << endl;
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4MGiaTwtCYu2etR3MjxfZFYJibo2L4qWOXIE04bdmzfYm2ZnE4ZUsJeZw/640?wx_fmt=other&from=appmsg)

这里Accessed的含义是是否已经使用过该段，例如`push esp`，此时会用到堆栈区域，该区域通过SS段选择子指向的段描述符进行管理，那么此时，即使将Accessed置0，内核也会将其设为1，表示该段在最后一次清零前被使用过。...