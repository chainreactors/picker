---
title: 探究SMC局部代码加密技术以及在CTF中的运用
url: https://www.secpulse.com/archives/197285.html
source: 安全脉搏
date: 2023-03-11
fetch_date: 2025-10-04T09:12:46.517458
---

# 探究SMC局部代码加密技术以及在CTF中的运用

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 探究SMC局部代码加密技术以及在CTF中的运用

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-10

17,361

## 前言

近些日子在很多线上比赛中都遇到了smc文件加密技术,比较出名的有Hgame杭电的比赛,于是我准备实现一下这项技术，但是在网上看了很多文章，发现没有讲的特别详细的，或者是无法根据他们的方法进行实现这项技术，因此本篇文章就是分享我在学习以及尝试smc文件加密技术时所遇到的麻烦以及心得。

该篇文章将会从我学习这项技术的视角，讲述我屡次失败的经历，一点点深入。

## SMC局部代码加密技术简介:

SMC（Software-Based Memory Encryption）是一种局部代码加密技术，它可以将一个可执行文件的指定区段进行加密，使得黑客无法直接分析区段内的代码，从而增加恶意代码分析难度和降低恶意攻击成功的可能性。

SMC的基本原理是在编译可执行文件时，将需要加密的代码区段（例如函数、代码块等）单独编译成一个section（段），并将其标记为可读、可写、不可执行（readable, writable, non-executable），然后通过某种方式在程序运行时将这个section解密为可执行代码，并将其标记为可读、可执行、不可写（readable, executable, non-writable）。这样，攻击者就无法在内存中找到加密的代码，从而无法直接执行或修改加密的代码。

SMC技术可以通过多种方式实现，例如修改PE文件的Section Header、使用API Hook实现代码加密和解密、使用VMProtect等第三方加密工具等。加密时一般采用异或等简单的加密算法，解密时通过相同的算法对密文进行解密。SMC技术虽然可以提高恶意代码的抗分析能力，但也会增加代码运行的开销和降低代码运行速度。

具体来说，SMC实现的主要步骤包括：

1. 1. 读取PE文件并找到需要加密的代码段。
2. 2. 将代码段的内容进行异或加密，并更新到内存中的代码段。
3. 3. 重定向代码段的内存地址，使得加密后的代码能够正确执行。
4. 4. 执行加密后的代码段。

SMC的优点在于：

1. 1. SMC采用的是软件实现方式，因此不需要硬件支持，可以在任何平台上运行。
2. 2. SMC对于程序的执行速度影响较小，因为代码解密和执行过程都是在内存中进行的。
3. 3. SMC可以对代码进行多次加密，增加破解的难度。
4. 4. SMC可以根据需要对不同的代码段进行不同的加密方式，从而提高安全性。

然而，SMC的缺点也显而易见，主要包括：

1. 1. SMC的实现比较复杂，需要涉及到PE文件结构、内存管理等方面的知识。
2. 2. SMC需要在运行时动态地解密代码，因此会对程序的性能产生一定的影响。
3. 3. SMC只能对静态的代码进行加密，对于动态生成的代码无法进行保护。
4. 4. SMC对于一些高级的破解技术（如内存分析）可能无法完全保护程序。

综上所述，SMC是一种局部代码加密技术，可以提高程序的安全性，但也存在一些局限性。在实际应用中，需要根据具体的情况选择最合适的保护方案，综合考虑安全性、性能和可维护性等因素。

**[流程图]**

```
+---------------------+
| 读取PE文件 |
| 找到代码段 |
+---------------------+
|
|
v
+---------------------------------+
| 对代码段进行异或加密 |
| 并更新到内存中的代码段 |
+---------------------------------+
|
|
v
+---------------------------------+
| 重定向代码段的内存地址， |
| 使得加密后的代码能够正确执行 |
+---------------------------------+
|
|
v
+---------------------+
| 执行加密后的代码段 |
+---------------------+
```

[**小结一下**]

前面说的非常的高端，其实通俗的讲就是程序可以自己对自己底层的字节码进行操作，就是所谓的自解密技术。其在ctf比赛中常见的就是可以将一段关键代码进行某种加密，然后程序运行的时候就直接解密回来,这样就可以干扰解题者的静态分析,在免杀方面也是非常好用的技术。可以利用该技术隐藏关键代码。

## 言归正传 如何实现这项技术

说实话，实现这项技术我是踩了非常多的坑的，接下来将会一一分享。

用伪代码解释一下该技术:

```
proc main:
............
IF .运行条件满足
  CALL DecryptProc （Address of MyProc）//对某个函数代码解密
  ........
  CALL MyProc                           //调用这个函数
  ........
  CALL EncryptProc （Address of MyProc）//再对代码进行加密，防止程序被Dump

......
end main
```

OK，非常明确，首先我是使用了Dev-C++ 6.7.5编译器,使用的MinGW GCC 9.2.0 32bit Debug的编译规则。

我们回忆一下该项技术，加入我们需要加密的是函数fun，那么我们首先需要使用指针找到fun的地址，一开始我使用的是int类型的指针，代码如下：

```
void fun()
{
    char flag[]="flag{this_is_test}";
    printf("%s",flag);
}
int main ()
{

    int *a=(int *)fun;
    for(int i = 0 ; i < 10  ; i++ )
    {
        printf("%x ",*(a++));
    }
}
```

输出结果为:

```
83e58955 45c738ec 616c66e5 e945c767 6968747b 73ed45c7 c773695f 745ff145 c7667365 7d74f545
```

然后我们把编译出来的文件放到ida里面观察

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197285-1678419687.png "null")

可以发现输出的内容确实是fun的字节码,但是由于int在c语言中占用了四个字节,因此是由四个16进制的机器码根据小端序排列输出的，那么为了解决这种连续字节码的问题我们需要找到一个只占用一个字节的指针，首先我想到了char类型，于是我马上更改代码，使用char类型的指针，得到了如下的输出结果。

```
55 ffffff89 ffffffe5 ffffff83 ffffffec 38 ffffffc7 45 ffffffe5 66
```

显然，这里是忽略的char的符号位的问题，有符号char型如果最高位是1，意思是超过了0x7f，当%X格式化输出的时候，则会将这个类型的值拓展到int型的32位，所以才会出现0xff，被扩展为ffffffff。

一筹莫展之际，我想起了在c语言中还有一种数据类型是只占一个字节的，那就是byte类型的数据，将代码改成byte类型之后可以发现输出变得正常了。

输出为:

```
55 89 e5 83 ec 38 c7 45 e5 66
```

这个就是正确的字节码的形式了。

那么我们需要定位到程序段进行加密了,由于本次只是实验，我们采取简单的异或加密方式，异或加密的特点就是加密函数也可以是解密函数,极大的方便了我们此次实验。我们可以先在ida中看到我们需要加密的程序段的位置。

在ida中我们可以发现我们需要解密的fun函数占用的地址段是0x00401410-00401451,那我们只需要将这一段内存中的机器码进行异或加密理论上就可以实现smc文件加密技术了。

实现代码如下：

```
void fun()
{
    char flag[]="flag{this_is_test}";
    printf("%s",flag);
}
int main ()
{

    byte *a=(byte *)fun;
    byte *b = a ;
    for( ; a!=(b+0x401451-0x401410+1) ; a++ )
    {
        *a=*a^3;
    }
    fun();
}
```

这段代码直接运行的话会出现内存错误，这是因为代码运行的时候对原本未被加密的fun函数进行了异或处理，导致本来应该是解密的操作变成了加密操作，然后机器无法识别该段内存就出现了内存错误，因此在运行代码前我们需要将文件中的fun函数部分进行加密操作。我这里使用idapython对字节码进行操作，然后将文件dump出来，完成对文件的加密。

idapython脚本为:

```
for i in range(0x401410,0x401451):
    patch_byte(i,get_wide_byte(i)^3)
```

运行后把代码dump下来，再运行

发现出现内存错误告警，猜测可能是dev-c++的编译器开启了随机基地址和数据保护,因此选择更换编译器，并关闭随机基地址选项。这里使用的是visual studio 2019，32位的debug模式进行编译

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197285-16784196871.png "null")

但是遗憾的是仍然无法运行，思考了一会儿之后发现可能是该段内存没有被设置成可读、可执行、可写入，导致程序无法识别这段内存了，因此我们改变方法使用程序段的概念，通过对整个程序段进行加密解密，来实现smc技术。

使用的代码是:

```
#include<Windows.h>
#include<string>
#include<string.h>
using namespace std;
#include <iostream>

#pragma code_seg(".hello")
void Fun1()
{
      char flag[]="flag{this_is_test}";
    printf("%s",flag);
}
#pragma code_seg()
#pragma comment(linker, "/SECTION:.hello,ERW")

void Fun1end()
{

}

void xxor(char* soure, int dLen)   //异或
{
    for (int i = 0; i < dLen;i++)
    {
         soure[i] = soure[i] ^3;
    }
}
void SMC(char* pBuf)     //SMC解密/加密函数
{
    const char* szSecName = ".hello";
    short nSec;
    PIMAGE_DOS_HEADER pDosHeader;
    PIMAGE_NT_HEADERS pNtHeader;
    PIMAGE_SECTION_HEADER pSec;
    pDosHeader = (PIMAGE_DOS_HEADER)pBuf;
    pNtHeader = (PIMAGE_NT_HEADERS)&pBuf[pDosHeader->e_lfanew];
    nSec = pNtHeader->FileHeader.NumberOfSections;
    pSec = (PIMAGE_SECTION_HEADER)&pBuf[sizeof(IMAGE_NT_HEADERS) + pDosHeader->e_lfanew];
    for (int i = 0; i < nSec; i++)
    {
        if (strcmp((char*)&pSec->Name, szSecName) == 0)
        {
            int pack_size;
            char* packStart;
            pack_size = pSec->SizeOfRawData;
            packStart = &pBuf[pSec->VirtualAddress];
            xxor(packStart, pack_size);
            return;
        }
        pSec++;
    }
}

void UnPack()   //解密/加密函数
{
    char* hMod;
    hMod = (char*)GetModuleH...