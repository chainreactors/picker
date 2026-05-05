---
title: 天命战队 DeSCTF Devil.exe 逆向思路分析
url: https://mp.weixin.qq.com/s/u8ipYKk33usvQDiiV3iDZA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:23.208518
---

# 天命战队 DeSCTF Devil.exe 逆向思路分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2j5jUku0JOYUW4PdkjCOYW4SC9N2dwDFIEbDUlWWQ2iaksWJrictuhY6zlicM7ibncmaiamWJ0ZeBWZU7lzW30tHC3icMQGqQMI9Py4/0?wx_fmt=jpeg)

# 天命战队 DeSCTF Devil.exe 逆向思路分析

n00bzx
n00bzx

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本次分享的题目已征得原作者同意，题目设计精巧、极具思考价值，也正因如此，我才在学习任务之余完成了相关代码编写，并整理思路发布此文。本文仅分享解题思路，不提供完整Writeup。

题目核心分析

程序为C++编写，无符号表，IDA分析即可。核心特征如下：

1. 程序包含反调试逻辑，会计算指定段的哈希值并存储至全局变量；

2. 关键技术点：通过VEH实现对CRT的inline hook，该hook兼具反调试功能，需借助驱动相关思路绕过；

3. 前置反调试、hook等逻辑建议15分钟内解决，后续直接进入核心算法部分；

4. 经IDA静态分析（结构体构建、变量重命名等常规操作），可梳理出核心逻辑代码。

文中代码存在少量人为设置的bug，不可直接编译运行，即便能编译，结果也必然错误。做题的核心是学习思考，需形成自己的解题思路。

程序编译说明：禁用了默认库以缩小体积，可直接编译运行，无额外环境要求。

```
#include<stdio.h>
#include<windows.h>
BYTE* unk_51E000 = 0;
BYTE* unk_866000 = 0;
BYTE* unk_7F6000 = 0;
BYTE* unk_43D000 = 0;
typedef int my_sprintf(char* a, size_t b, const char* c, va_list d);
void my_printf(const char* format, ...)
{
DWORD i;
char buffer[1024];
for (i = 0; i < 1024; i++)
    {
buffer[i] = 0;
    }
va_list args;
va_start(args, format);
PVOID fuck_crt = GetProcAddress(GetModuleHandleA("ntdll.dll"), "_vsnprintf");
((my_sprintf*)fuck_crt)(buffer, sizeof(buffer), format, args);
DWORD bytes_written;
WriteConsoleA(GetStdHandle(STD_OUTPUT_HANDLE), buffer, lstrlenA(buffer), &bytes_written, NULL);
}
void sub_4011A0(BYTE* a1)
{
int v2[16];
int i;
char v4[16];
v2[0] = 0;
v2[1] = 5;
v2[2] = 10;
v2[3] = 15;
v2[4] = 4;
v2[5] = 9;
v2[6] = 14;
v2[7] = 3;
v2[8] = 8;
v2[9] = 13;
v2[10] = 2;
v2[11] = 7;
v2[12] = 12;
v2[13] = 1;
v2[14] = 6;
v2[15] = 11;
for (i = 0; i < 16; ++i)
    {
v4[i] = a1[v2[i]];
    }
memcpy(a1, v4, 0x10);
}
void sub_4011A0_inv(BYTE* a1)
{
int v2[16];
BYTE temp[16];
int i;
v2[0] = 0;
v2[1] = 5;
v2[2] = 10;
v2[3] = 15;
v2[4] = 4;
v2[5] = 9;
v2[6] = 14;
v2[7] = 3;
v2[8] = 8;
v2[9] = 13;
v2[10] = 2;
v2[11] = 7;
v2[12] = 12;
v2[13] = 1;
v2[14] = 6;
v2[15] = 11;
memcpy(temp, a1, 0x10);
for (i = 0; i < 16; ++i)
    {
a1[v2[i]] = temp[i];
    }
}
void sub_401270(BYTE *input_pass, BYTE *out)
{
int n;
int m;
int i;
BYTE aa, bb, cc, dd;
BYTE low, high;
int j;
int k;
BYTE const1[] = { 0xB8,0xA1,0xD9,0xB9,0xD8,0x3B,0x17,0x91,0x75,0x12,0x1B,0x74,0x18,0x5B,0x16,0x39,0x76,0xA2,0x0C,0xFA,0x90,0x94,0x36,0x41,0x58,0x59,0x43,0xD4,0x47,0x92,0x2D,0xEA };
BYTE const2[] = { 0x65,0xD6,0xCD,0xFE,0xFF,0x1C,0x41,0x65,0x15,0x6E,0x18,0x4C,0xF5,0xB9,0x4E,0x13 };
for (i = 0; i < 16; ++i)
    {
input_pass[i] ^= const2[i];
    }
for (j = 0; j < 13; ++j)
    {
sub_4011A0(input_pass);
for (k = 0; k < 4; ++k)
        {
BYTE v14_a = unk_51E000[3 + 4 * (53248 * ((int)*const1 >> 4) + 4096 * j + 1024 * k + input_pass[4 * k])];
BYTE v12_a = unk_51E000[3 + 4 * (53248 * ((int)*const1 >> 4) + 256 + 4096 * j + 1024 * k + input_pass[4 * k + 1])];
BYTE v10_a = unk_51E000[3 + 4 * (53248 * ((int)*const1 >> 4) + 512 + 4096 * j + 1024 * k + input_pass[4 * k + 2])];
BYTE v8_a = unk_51E000[3 + 4 * (53248 * ((int)*const1 >> 4) + 768 + 4096 * j + 1024 * k + input_pass[4 * k + 3])];
BYTE v14_b = unk_51E000[2 + 4 * (53248 * ((int)*const1 >> 4) + 4096 * j + 1024 * k + input_pass[4 * k])];
BYTE v12_b = unk_51E000[2 + 4 * (53248 * ((int)*const1 >> 4) + 256 + 4096 * j + 1024 * k + input_pass[4 * k + 1])];
BYTE v10_b = unk_51E000[2 + 4 * (53248 * ((int)*const1 >> 4) + 512 + 4096 * j + 1024 * k + input_pass[4 * k + 2])];
BYTE v8_b = unk_51E000[2 + 4 * (53248 * ((int)*const1 >> 4) + 768 + 4096 * j + 1024 * k + input_pass[4 * k + 3])];
BYTE v14_c = unk_51E000[1 + 4 * (53248 * ((int)*const1 >> 4) + 4096 * j + 1024 * k + input_pass[4 * k])];
BYTE v12_c = unk_51E000[1 + 4 * (53248 * ((int)*const1 >> 4) + 256 + 4096 * j + 1024 * k + input_pass[4 * k + 1])];
BYTE v10_c = unk_51E000[1 + 4 * (53248 * ((int)*const1 >> 4) + 512 + 4096 * j + 1024 * k + input_pass[4 * k + 2])];
BYTE v8_c = unk_51E000[1 + 4 * (53248 * ((int)*const1 >> 4) + 768 + 4096 * j + 1024 * k + input_pass[4 * k + 3])];
BYTE v14_d = unk_51E000[4 * (53248 * ((int)*const1 >> 4) + 4096 * j + 1024 * k + input_pass[4 * k])];
BYTE v12_d = unk_51E000[4 * (53248 * ((int)*const1 >> 4) + 256 + 4096 * j + 1024 * k + input_pass[4 * k + 1])];
BYTE v10_d = unk_51E000[4 * (53248 * ((int)*const1 >> 4) + 512 + 4096 * j + 1024 * k + input_pass[4 * k + 2])];
BYTE v8_d = unk_51E000[4 * (53248 * ((int)*const1 >> 4) + 768 + 4096 * j + 1024 * k + input_pass[4 * k + 3])];

low = unk_866000[319488 * ((int)const1[5] >> 4) + 1280 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 512 + 24576 * j + 6144 * k + 16 * (v14_a & 0xF) + (v12_a & 0xF)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 768 + 24576 * j + 6144 * k + 16 * (v10_a & 0xF) + (v8_a & 0xF)]];
high = unk_866000[319488 * ((int)const1[5] >> 4) + 1024 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 24576 * j + 6144 * k + 16 * (v14_a >> 4) + (v12_a >> 4)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 256 + 24576 * j + 6144 * k + 16 * (v10_a >> 4) + (v8_a >> 4)]];
aa = high;
aa <<= 4;
aa |= low;

low = unk_866000[319488 * ((int)const1[5] >> 4) + 2816 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 2048 + 24576 * j + 6144 * k + 16 * (v14_b & 0xF) + (v12_b & 0xF)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 2304 + 24576 * j + 6144 * k + 16 * (v10_b & 0xF) + (v8_b & 0xF)]];
high = unk_866000[319488 * ((int)const1[5] >> 4) + 2560 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 1536 + 24576 * j + 6144 * k + 16 * (v14_b >> 4) + (v12_b >> 4)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 1792 + 24576 * j + 6144 * k + 16 * (v10_b >> 4) + (v8_b >> 4)]];
bb = high;
bb <<= 4;
bb |= low;

low = unk_866000[319488 * ((int)const1[5] >> 4) + 4352 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 3584 + 24576 * j + 6144 * k + 16 * (v14_c & 0xF) + (v12_c & 0xF)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 3840 + 24576 * j + 6144 * k + 16 * (v10_c & 0xF) + (v8_c & 0xF)]];
high = unk_866000[319488 * ((int)const1[5] >> 4) + 4096 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 3072 + 24576 * j + 6144 * k + 16 * (v14_c >> 4) + (v12_c >> 4)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 3328 + 24576 * j + 6144 * k + 16 * (v10_c >> 4) + (v8_c >> 4)]];
cc = high;
cc <<= 4;
cc |= low;

low = unk_866000[319488 * ((int)const1[5] >> 4) + 5888 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 5120 + 24576 * j + 6144 * k + 16 * (v14_d & 0xF) + (v12_d & 0xF)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 5376 + 24576 * j + 6144 * k + 16 * (v10_d & 0xF) + (v8_d & 0xF)]];
high = unk_866000[319488 * ((int)const1[5] >> 4) + 5632 + 24576 * j + 6144 * k + 16
* unk_866000[319488 * ((int)const1[5] >> 4) + 4608 + 24576 * j + 6144 * k + 16 * (v14_d >> 4) + (v12_d >> 4)]
+ unk_866000[319488 * ((int)const1[5] >> 4) + 4864 + 24576 * j + 6144 * k + 16 * (v10_d >> 4) + (v8_d >> 4)]];
dd = high;
dd <<= 4;
dd |= low;

input_pass[4 * k] = aa;
input_pass[4 * k + 1] = bb;
input_pass[4 * k + 2] = cc;
input_pass[4 * k + 3] = dd;

BYTE v15_a = unk_7F6000[3 + 4 * (57344 * ((int)const1[10] >> 4) + 4096 * j + 1024 * k + input_pass[4 * k])];
BYTE v13_a = unk_7F6000[3 + 4 * (57344 * ((int)const1[10] >> 4) + 256 + 4096 * j + 1024 * k + input_pass[4 * k + 1])];
BYTE v11_a = unk_7F6000[3 + 4 * (57344 * ((int)const1[10] >> 4) + 512 + 4096 * j + 1024 * k + input_pass[4 * k + 2])];
BYTE v9_a = unk_7F6000[3 + 4 * (57344 * ((int)const1[10] >> 4) + 768 + 4096 * j + 1024 * k + input_pass[4 * k + 3])];
BYTE v15_b = unk_7F6000[2 + 4 * (57344 * ((int)const1[10] >> 4) + 4096 * j + 1024 * k + input_pass[4 * k])];
BYTE v13_b = unk_7F6000[2 + 4 * (57344 * ((int)const1[10] >> 4) + 256 + 4096 * j + 1024 * k + input_pass[4 * k + 1])];
BYTE v11_b = unk_7F6000[2 + 4 * (57344 * ((int)const1[10] >> 4) + 512 + 4096 * j + 1024 * k + input_pass[4 * k + 2])];
BYTE v9_b = unk_7F6000[2 + 4 * (57344 * ((int)const1[10] >> 4) + 768 + 4096 * j + 1024 * k + input_pass[4 * k + 3])];
BYTE v15_c = unk_7F6000[1 + 4 * (57344 * ((int)const1[10] >> 4) + 4...