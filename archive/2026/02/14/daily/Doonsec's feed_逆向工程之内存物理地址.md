---
title: 逆向工程之内存物理地址
url: https://mp.weixin.qq.com/s/0yi9APmSeAu2mGqkuCygbA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:28.207895
---

# 逆向工程之内存物理地址

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SfVJxH0muWXzR73fYSbgveS2UKgmJfZqKgSL4JbhLYjOnGBVticmjzwjjfI0ibsfHMhATrhy6dNQBQOn6iauzicUY9pnR4AObUmjcQ1GrF04A4U/0?wx_fmt=jpeg)

# 逆向工程之内存物理地址

原创

高尉峰
高尉峰

ShadowRoot

![]()

在小说阅读器中沉浸阅读

段寄存器

在x86汇编语言中，**DS**是**Data Segment**（数据段）寄存器的缩写，DS用于指向当前数据段的基地址。在访问内存中的数据时，CPU会使用基地址和偏移地址来定位数据的位置。

## 其他段寄存器：

* **CS (Code Segment) - 代码段**
* **SS(Stack Segment) - 堆栈段**
* **ES(Extra Segment) - 附加段**

**例子：**

```
cmp dword ptr ds:[var1], 20  ; 定义一个4字节的var1变量，初始值为20
```

* **ds：明确指定使用DS段寄存器**
* **[var1]：表示var1变量的偏移地址**
* **DWORD**（Double Word）是汇编语言中的一个**数据类型指示符**。

```
BYTE    = 1 字节 (8位)   范围: 0-255WORD    = 2 字节 (16位)  范围: 0-65535DWORD   = 4 字节 (32位)  范围: 0-4294967295QWORD   = 8 字节 (64位)  范围: 0-18446744073709551615
```

内存模型

平坦内存模型：

```
所有段寄存器（CS, DS, SS, ES）的基址都是0物理地址 = 0 + 变量的偏移地址
```

保护模式内存模型：

```
物理地址 = 段基址（从描述符表获取）+ 偏移地址
```

实模式内存模型：

```
物理地址 = DS基址 × 16 + 偏移地址
Example:DS寄存器基址(1000h)，偏移地址(0020h)物理地址 = 1000h × 16 = 10000h + 0020h = 10020h
```

例子：

```
  .386p  .model flat,stdcall  option casemap:none.data  var1 DWORD 20    ; 假设var1的偏移地址0x00403000  var2 DWORD 10    ; 假设var2的偏移地址0x00403004.code  ; 平坦内存模型  mov eax, ds:[var1]  ; 物理地址=0 + 00403000h = 00403000h  mov ebx, [var2]     ; 物理地址=0 + 00403004h = 00403004h                      ; (ds:可以省略)
```

C语言和汇编语言的关系

C:

```
#include <stdio.h>#include <windows.h>
int main(int argc,char * argv[]){  int var1 = 20;  int var2 = 10;  int var3 = 50;
  if (var1 >= 20 and var2 <= 100 and var3 == 50)  {    printf("xor eax,eax");  }  return 0;}
```

ASM:

```
  .386p  .model flat,stdcall  option casemap:noneinclude windows.incinclude kernel32.incincludelib kernel32.lib.data  var1 DWORD 20  var2 DWORD 10  var3 DWORD 50  flag DWORD ?.code  main PROC  ; if(var1 >= 20 and var2 <= 100 and var3 == 50)    cmp dword ptr ds:[var1],20     ; 判断是否大于20    jl L1                          ; 不大于则跳转    cmp dword ptr ds:[var2],100    ; 判断是否小于100    jg L1                          ; 不小于则跳转    cmp dword ptr ds:[var3],50     ; 判断是否等于50    jne L1                         ; 不等于则跳转    mov dword ptr ds:[flag],1      ; 说明等式成立 flag=1    jmp L2  L1: mov dword ptr ds:[flag],0  L2: cmp dword ptr ds:[flag],0    je lop_end                     ; 为0则跳转,不为0则继续执行    xor eax,eax                    ; 此处是执行if语句内部    xor ebx,ebx    xor ecx,ecx    jmp lop_end  lop_end:    nop                            ; 直接结束    invoke ExitProcess,0  main ENDPEND main
```

C:

```
#include <stdio.h>#include <windows.h>
int main(int argc,char * argv[]){  int var1 = 20;  int var2 = 10;  int var3 = 50;
  if (var1 > var2 || var2 <= var3)  {    printf("xor eax,eax");  }  else if(var3 == 50 || var2 > 10)  {    printf("xor ebx,ebx");  }  return 0;}
```

ASM:

```
  .386p  .model flat,stdcall  option casemap:noneinclude windows.incinclude kernel32.incincludelib kernel32.lib.data  var1 DWORD 20  var2 DWORD 10  var3 DWORD 50.code  main PROC  ; if (var1 > var2 || var2 <= var3)    mov eax,dword ptr ds:[var1]    cmp eax,dword ptr ds:[var2]     ; var1 > var2    jg L1    mov eax,dword ptr ds:[var2]    cmp eax,dword ptr ds:[var3]     ; var2 <= var3    jg L2                           ; 条件是 var2 > var3 则跳转  L1:    xor eax,eax                     ; printf("xor eax,eax")    jmp lop_end  L2:  ; else if(var3 == 50 || var2 > 10)    cmp dword ptr ds:[var3],50    je L3    cmp dword ptr ds:[var2],10      ; var2 > 10    jle lop_end  L3:    xor ebx,ebx                     ; printf("xor ebx,ebx")    jmp lop_end
  lop_end:    nop    int 3    invoke ExitProcess,0  main ENDPEND main
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w1Ih8BLBBL4FOlc45weOTleZgQc59vUn2Pms9mjhedcrtc4cJq1XLWO5516ZuNW77owtFfGSxZxAN9QzYZk5fg/0?wx_fmt=png)

ShadowRoot

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w1Ih8BLBBL4FOlc45weOTleZgQc59vUn2Pms9mjhedcrtc4cJq1XLWO5516ZuNW77owtFfGSxZxAN9QzYZk5fg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过