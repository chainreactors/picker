---
title: RE新瓶装旧酒之printf虚拟机
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247505119&idx=1&sn=11a231ff7b4ce9154357f3fa9588bc0b&chksm=fa520161cd2588777ad64fd4e5c690458422fd03e125595adc61c2c3f239daa81396dccda915&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-03-07
fetch_date: 2025-10-06T17:09:30.816394
---

# RE新瓶装旧酒之printf虚拟机

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQgcHnYDCukP0fx1lucHx2BKSY5otMZTONcM63oqYrtEvmc5icmSvgZwyicIzEI2Sk077gwQ4bo0gEg/0?wx_fmt=jpeg)

# RE新瓶装旧酒之printf虚拟机

原创

c10udlnk

山石网科安全技术研究院

众所周知，printf中可以自定义格式占位符（spec）的行为，就像使用`%x`可以输出一个数的十六进制一样，在使用`register_printf_function`后可以将指定spec与指定转换函数绑定，从而自定义输出行为。

虽然这种方式已经弃用，但最近似乎在新的领域焕发了第二春——用它的自定义行为来运行一个CTF Reverse里常见的VM。单是2023年下半年居然有两场比赛碰到了printf虚拟机的题目，而再往前追溯或许只有2021年GoogleCTF那道经典的Weather了（**https://ctftime.org/task/16546**）。

本文将介绍printf虚拟机的实现原理，讲解该类逆向题目的解题方法，并以BRICS+CTF的`shellcode???`和楚慧杯的`scalar`两道今年做到的赛题为例将解题方法运用到实战中。

## 自定义printf

有关自定义printf的操作细节，我们可以在GNU的文档里看到：

**https://www.gnu.org/software/libc/manual/html\_node/Customizing-Printf.html**

这里仅挑出一些与赛题相关的主要知识点进行介绍

```
int register_printf_function (int spec, printf_function handler-function, printf_arginfo_function arginfo-function)
```

`register_printf_function`函数用于注册新的输出转换，需要在printf虚拟机前执行，一般为了掩人耳目会放在`init`中作为初始函数表的一部分。其参数含义如下：

* spec：格式占位符。

  如*spec*为`'A'`时，该函数注册的是`%A`的输出转换。可以覆盖如%x、%s等默认*spec*的定义，建议一般使用大写字母以示区分。
* handler-function：处理该*spec*的转换函数。

  ```
  int function (FILE *stream, const struct printf_info *info, const void *const *args)
  ```

  简单来说，*info*是在解析到spec时获取的信息结构体，如解析到`%20A`时，`info -> width = 20`（结构体的详细介绍见后文）；*args*是获取的参数列表，通过上文的arginfo-function指定参数个数n以后，它会在printf的参数列表中依次获取n个参数。
* arginfo-function：指定该*spec*所需的参数个数和参数类型。

  ```
  size_t parse_printf_format (const char *template, size_t n, int *argtypes)
  ```

  这里需要关注的是*argtypes*和返回值，argtypes是一个数组，分别指定了各参数的类型，如PA\_INT、PA\_CHAR等，最后返回该*spec*所需的参数个数。

## 解题方法

既然如此，我们的整体思路就是：

1. 找到register\_printf\_function
2. 记录各格式占位符的作用
3. 编写VM解释器将format字符串转换为汇编
4. 阅读汇编代码求解flag

除了第一步以外，剩下的步骤都与VM解题方法大致相同，printf虚拟机的作用是将原本VM的switch-case分派复杂化，并且在不起眼的printf中完成整个运行。

### BRICS+CTF | shellcode???

如果没做过printf虚拟机的话，这道题上来看到`main`函数里只有一句printf，大概会觉得很莫名其妙：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQgcHnYDCukP0fx1lucHx2B4ed0C6Gcf6DOPaAbHCfFCb1OTDxKBYCu6EWNFWPnoX7qPhRGtjX9bg/640?wx_fmt=png&from=appmsg)

找到`.init_array`，分别查看这里的各个函数，就能发现第二个函数就是我们所要找的注册printf转换函数的地方：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQgcHnYDCukP0fx1lucHx2BW47cssSQ9Picbgg17Csb4PBGDUM02bpNnmpQBkf6FyjEcVSGvBXQLwg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQgcHnYDCukP0fx1lucHx2BTTradt6H4GA2X6QLEYyhhh5sHFtt2rlEGicFkVt0EfXmwM7yyQhMCdA/640?wx_fmt=png&from=appmsg)

main函数里面的printf用了`%f`，所以看`'f'`的handler：

```
undefined8 FUN_00401fe0(void) {
  uint arg;
  char *format;
  int i;

  for (i = 0; i < 0x34; i = i + 1) {
    format = (char *)malloc(0x100);
    arg = 0;
    __isoc99_scanf("%s %d",format,&arg);
    printf(format,(ulong)arg);
    free(format);
  }
  printf("%w%V%b%s%V%m%J%s%R%H",0x1223f37,0x2af985a,0x2ba4c9,0x693d920,0x6f794f,0x62,0xfff1d63c,
         0x623c513,0x2584,0x474f4b2,0x27d8f97);
  printf("%w%V%b%s%V%m%J%s%R%H",0x3fe9fae,0x5d0a399,0x3c7c1e5,0x426e19e,0x3ac53d7,0x69,0xffee7c50,
         0x9abb47,0x2b11,0x25242a2,0x2f511fb);
  printf("%w%V%b%s%V%m%J%s%R%H",0x79bc35,0x1b7bd90,0x4383c74,0x580ac2a,0x73751d6,0x73,0xffe8d24e,
         0x45161b0,0x33a9,0x2f87765,0x10ad040);
  printf("%w%V%b%s%V%m%J%s%R%H",0xa6d19b,0x1a6a0d3,0x23784ab,0x170fb47,0x6279f4e,0x7b,0xffe3b18d,
         0x18d51b8,0x3b19,0x22e1923,0x44c107e);
  printf("%w%V%b%s%V%m%J%s%R%H",0x61d2d1a,0x2fd3ab5,0x3674d99,0x2ef1ece,0x4320e5,0x30,0xfffe7d90,
         0x72efd70,0x900,0x5054985,0x8a2648);
  printf("%w%V%b%s%V%m%J%s%R%H",0x73273e1,0x1ea1176,0x22750f6,0x43b6a7a,0x6fc9446,0x5f,0xfff32412,
         0x36aa1c2,0x2341,0x2bdfa2d,0x19df6c1);
  printf("%w%V%b%s%V%m%J%s%R%H",0x709b202,0x10c7776,0x1aca7bf,0x2846728,0x2acdfd,0x30,0xfffe6c39,
         0x50aceaf,0x900,0x3fd6e93,0x6f1ae51);
  printf("%w%V%b%s%V%m%J%s%R%H",0x2839ef3,0x14e6f45,0x3ac805f,0x3df8740,0x9ecc96,0x5f,0xfff3112a,
         0x878285,0x2341,0x1465a45,0x61cb62);
  printf("%w%V%b%s%V%m%J%s%R%H",0x48975af,0x3e4659f,0x2e62dba,0x43051c2,0x70c2c14,0x61,0xfff24223,
         0x726a781,0x24c1,0x3c59ed9,0x7013f38);
  printf("%w%V%b%s%V%m%J%s%R%H",0x5af8e8f,0x14a0790,0x11a0297,0x1639c3,0x2f4684f,0x5f,0xfff31a25,
         0x69dcc81,0x2341,0x3d1ec81,0x4b5c9aa);
  printf("%w%V%b%s%V%m%J%s%R%H",0x2384a5d,0x6023773,0x751b5a4,0x42906ae,0x2abc591,0x30,0xfffe8490,
         0x1ba4382,0x900,0x4c841a0,0x5d6c676);
  printf("%w%V%b%s%V%m%J%s%R%H",0x10f72b,0x4555f11,0x73006b8,0x4bd032f,0x21f61cb,0x5f,0xfff316c5,
         0x130456c,0x2341,0x66232ed,0x24880b7);
  printf("%w%V%b%s%V%m%J%s%R%H",0x61629be,0x142e4d1,0x6ef88f9,0x124e9d7,0x75323be,0x75,0xffe7c35c,
         0x13e54b,0x3579,0x2055d85,0x40a037e);
  printf("%w%V%b%s%V%m%J%s%R%H",0x1a974cb,0x4c13f72,0x3f91ead,0xc0b580,0x2ceb6c6,0x31,0xfffe57b0,
         0x73751fd,0x961,0x2448dd2,0x35e7795);
  printf("%w%V%b%s%V%m%J%s%R%H",0xd61454,0x5ea2480,0x638cf01,0xc1897,0x59b1f2b,0x70,0xffeaa081,
         0x12d8934,0x3100,0x2507798,0x58616c);
  printf("%w%V%b%s%V%m%J%s%R%H",0x2b7cfa7,0x27e600c,0x2aac5b2,0x58544a3,0x2b98aa3,0x72,0xffe99861,
         0x60f21dd,0x32c4,0x7021d82,0x1ee19b5);
  printf("%w%V%b%s%V%m%J%s%R%H",0x35491c5,0x2341b2f,0x21a5253,0x3d9b0ad,0x23c1e66,0x33,0xfffe1d16,
         0x3e89c02,0xa29,0x5c82116,0x4129fef);
  printf("%w%V%b%s%V%m%J%s%R%H",0x4e0a10d,0x71efc70,0x6092171,0x869088,0x63dba22,0x74,0xffe85900,
         0x570839b,0x3490,0x1a2b21d,0x2e03a43);
  printf("%w%V%b%s%V%m%J%s%R%H",0x296ee85,0x63d72c7,0x6d9cd72,0x70f9b7d,0x4dbbe1a,0x31,0xfffe6818,
         0x48cad9,0x961,0x581996e,0x58772);
  printf("%w%V%b%s%V%m%J%s%R%H",0x2fb0010,0x5c0791d,0x145d223,0xac2f74,0x5368a28,0x5f,0xfff31065,
         0x55bca2a,0x2341,0x4b1ebf8,0x6a49a88);
  printf("%w%V%b%s%V%m%J%s%R%H",0x70eecbd,0x36ecff2,0x4924a1d,0x1f74f07,0x11d896d,0x75,0xffe7ab43,
         0x23f3af7,0x3579,0x72f2132,0x25a98d9);
  printf("%w%V%b%s%V%m%J%s%R%H",0x2f1cb4,0x3f205f7,0x75aa10f,0x3e936c7,0x5188cee,0x5f,0xfff2fe92,
         0x708fd26,0x2341,0x2749ae8,0x6257695);
  printf("%w%V%b%s%V%m%J%s%R%H",0x4c7a950,0x5ec022e,0x4b9a7a4,0x2e278f4,0x6200e00,0x30,0xfffe8021,
         0x63b7839,0x900,0x42dc8d5,0x13d670a);
  printf("%w%V%b%s%V%m%J%s%R%H",0x47b6288,0x4f8f54e,0x142674c,0x8c3951,0x7037c99,100,0xfff0e101,
         0x3ecce47,10000,0x66fbc4d,0x37bed26);
  printf("%w%V%b%s%V%m%J%s%R%H",0x642ad16,0x740e6c5,0x258eae7,0x65e3017,0x586efb0,0x6a,0xffee03b9,
         0x4afb046,0x2be4,0x4c31ce0,0x52abb1f);
  printf("%w%V%b%s%V%m%J%s%R%H",0x55db7f6,0x6aef138,0x42210e5,0x72fd711,0xd8d75e,0x62,0xfff1e081,
         0x1ca0e4d,0x2584,0x325351f,0x69c0c21);
  putchar(0x59);
  putchar(0x65);
  putchar(0x73);
  return 0;
}
```

这里主要用到的指令序列都是`"%w%V%b%s%V%m%J%s%R%H"`，而前面的for循环让我们输入字符串format作为指令和一个数字arg作为参数，姑且相当于是平时题目中的输入。

由于主指令序列很短，用出VM解释器倒有点杀鸡焉用牛刀的感觉，干脆直接手逆出汇编。如`%w`的handler：

```
undefined8 FUN_00400ed4(void) {
  long v1;
  double v0;

  ptr = ptr + -1;
  v0 = pow((double)arr[ptr],2.0);
  v1 = (long)ptr;
  ptr = ptr + 1;
  arr[v1] = (int)v0;
  return 0;
}
```

实际上实现的是：

```
arr[ptr-1] = arr[ptr-1] ** 2
```

表示成汇编（随便抓一个寄存器rsi用来表示ptr）：

```
POW [rsi-1], 2
```

那么主指令序列全部逆出来就是：

```
;%w
;POW [rsi-1], 2
POP rax
POW rax, 2
PUSH rax
;%V
;mov [rsi], [rsi-2]
;inc rsi
PUSH [rsp-2]
;%b
;POW [rsi-1], 3
POP rax
POW rax, 3
PUSH rax
;%s
;sub [rsi-2], [rsi-1]
;dec rsi
POP rax
POP rbx
sub rbx, rax
PUSH rbx
;%V
;mov [rsi], [rsi-2]
;inc rsi
PUSH [rsp-2]
;%m
;mul [rsi-1], arg5
POP rax
MUL rax, arg5
PUSH rax
;%J
;sub arg6, [rsi-1]
;mov [rsi-1], arg6
POP rax
MOV rbx, arg6
SUB rbx, rax
PUSH rbx
;%s
;sub [rsi-2], [rsi-1]
;dec rsi
POP rax
POP rbx
sub rbx, rax
PUSH rbx
;%R
;cmp [rsi-1], arg8
;jnz "No"
;dec rsi
POP rax
cmp rax, arg8
;%H
;dec rsi
POP
```

从注册printf转换函数的函数中可以看到，所有的arginfo都return了1，代表都需要一个参数，而有些handler里却没用到arg，这算是一个小坑：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQgcHnYDCukP0fx1lucHx2BVswficQKrmDRmZXz8y3Sibx3ZjSgDsNEAfChu6Coby2Ts5EcgqROdJlw/640?wx_fmt=png&from=appmsg)

所以上文汇编中的arg5是printf调用的参数列表中的第六个参数（从0标起），以此类推。

再写成Python是：

```
def f(v5, v6, v8):
    assert v8 == (arr[ptr-1] ** 2) - (arr[ptr-2] ** 3) - (v6 - (arr[ptr-2] * v5))
    ptr -= 2
```

v5、v6和v8这三个参数可以从程序的汇编代码中提取（伪代码的参数没有展示完全），可以用逐两字节爆...