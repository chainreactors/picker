---
title: Foxit Reader堆溢出漏洞研究
url: https://www.secpulse.com/archives/189987.html
source: 安全脉搏
date: 2022-10-29
fetch_date: 2025-10-03T21:11:43.652021
---

# Foxit Reader堆溢出漏洞研究

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

# Foxit Reader堆溢出漏洞研究

[漏洞](https://www.secpulse.com/archives/category/vul)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-10-28

10,389

写在前面：最近在做样本分析时，关注到了Foxit Reader阅读器在2017年公布的堆溢出漏洞，但是值得注意的是，该漏洞在其补丁版本和最新版本中，均没有得到较好的修补，使得Foxit禁用了bmp图片转换功能。该漏洞点其实可以通过检查实现修补，补丁也在下文中附带，但是Foxit依旧禁用了该功能，说明可能存在溢出的漏洞点非常之多......

## 漏洞介绍：

在ConverToPDF\_x86.dll文件sub\_101F6593函数中，存在堆溢出漏洞。由于在sub\_101F5FF9处理bmp文件时，对bmp文件的biWidth不做过滤，直接和biBitCount相乘，造成整数溢出，进而导致为像素分配的缓冲区过小，在后续复制操作中，造成堆溢出。
版本：Foxit Reader<=9.0.1
复现版本：Foxit Redaer8.2.1

## **静态分析**

首先分析恶意的bmp文件，bmp文件格式如下，首先是14字节的头部信息，之后就是位图信息，注意恶意bmp文件中，位图信息的biWidth属性超长，为0x40000001。

```
typedef struct tagBITMAPFILEHEADER  #14bytes
{
    UINT16 bfType;
    DWORD bfSize;
    UINT16 bfReserved1;
    UINT16 bfReserved2;
    DWORD bfOffBits;
} BITMAPFILEHEADER;

typedef struct tagBITMAPINFOHEADER
 {
    DWORD biSize;
    LONG biWidth;
    LONG biHeight;
    WORD biPlanes;
    WORD biBitCount;
    DWORD biCompression;
    DWORD biSizeImage;
    LONG biXPelsPerMeter;
    LONG biYPelsPerMeter;
    DWORD biClrUsed;
    DWORD biClrImportant;
} BITMAPINFOHEADER;
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939078.png)

当利用Foxit打开bmp文件时，Foxit会调用ConverToPDF\_x86.dll中的sub\_101F5FF9函数进行处理，其中，对biWidth和biBitCount进行了相关运算，导致整数溢出，被截断后，生成的缓冲区大小过小。在之后对堆中的指针进行申请，作为后续复制操作的目的地址，并对申请的指针进行记录，注意，这里其实有3个可能的整数溢出点:
（1）imul指令（biWidth\*biBitCount）可能导致整数溢出
（2）add eax,ebx指令（ebx最大为0x1F），如果imul没有造成溢出，若eax过大，则加法也可能导致溢出
（3）add eax,edx指令（edx最大为0x1F），若eax过大，也可能导致溢出

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939080.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939086.png)

之后，程序会调用sub\_101F6593函数，在刚刚申请得到的堆中，进行相关复制操作，到那时由于申请的堆空间过小，造成溢出：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939099.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939109.png)

## **动态调试**

**1.漏洞复现与定位**
为了能让windbg捕捉堆溢出时的位置，需要开启page heap功能，page heap将进程中使用的堆空间独立开，发生越界操作会报错：

```
gflags.exe /p /enable Foxit Reader.exe /full
```

然后打开Foxit阅读器，windbg加载之后，可能存在符号表解析问题，需要创建符号表的文件夹（在C盘下创建，然后在windbg下指定即可）

```
.symfix+ c:symbols
.reload
```

然后打开恶意bmp文件，windbg捕捉到溢出的错误信息，发现应该是复制时造成的越界，对应的恰好是静态分析中对应的101F66FA的位置

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939112.png)

利用!heap -p -a指令追踪一下对edi空间进行的操作，也能够对应到其中对bmp文件进行处理的sub\_101F5FF9函数，此处的操作就是该函数正在记录申请得到的堆指针。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939113.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939114.png)

**2.堆空间分析**
我们跟踪一下对堆的操作过程，sub\_101F5FF9函数最终申请得到的堆空间如图，申请得到的堆指针为eax=1b52dff8，并保存。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-16669391141.png)

查看1b51dff8的堆信息，由于前面的整数溢出，导致申请的空间过小，因此申请得到的堆指针距离堆块的结束地址只有8字节，因此当后期复制内容超过8字节，即触发崩溃。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-16669391142.png)

## **临时补丁**

因此打临时补丁时，需要防止三处溢出，分别为乘法溢出和两处加法溢出。两次加法均为0x1f，乘法中的biBitCount最大为0x20（像素点只有1、4、8、16、24、32），并且此函数定义的变量均为无符号整数，因此最大缓冲区大小为0x7FFFFFFF，因此biWidth最大为：

```
(0xFFFFFFFF-0x1F-0x1F)/0x20=0x03FFFFFF
```

补丁代码patch如下，可以通过注入进程的方式实现防护和检测

```
MODULE_PATH "C:install_pathConvertToPDF_x86.dll"
PATCH_ID 1000031
PATCH_FORMAT_VER 2
VULN_ID 3556
PLATFORM win32

patchlet_start
PATCHLET_ID 1
PATCHLET_TYPE 2
PATCHLET_OFFSET 0x2098d9
JUMPOVERBYTES 3
N_ORIGINALBYTES 2

code_start
    mov edi, [esi+54h]
    cmp edi, 03ffffffh
    jb skip
    call PIT_ExploitBlocked
    xor edi,edi
    skip:
patchlet_end
```

## **官方修补**

值得关注的是，在其之后一个版本的Foxit版本(Foxit Reader9.1)中，此漏洞依旧没有得到修补，而是直接禁用了这个函数，当使用Foxit Reader加载bmp文件时，直接显示无法加载。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939115.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-16669391151.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189987-1666939116.png)

在官网下载最新版的Foxit版本（Foxit Reader12.1）中，索性直接禁用了所有的转换型功能，看来针对格式转换中的计算导致的整形溢出点还是依旧存在，于是Foxit索性放弃了此类功能。

**本文作者：[ChaMd5安全团队](newpage/author?author_id=3747)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189987.html**](https://www.secpulse.com/archives/189987.html)

Tags: [Foxit Reader](https://www.secpulse.com/archives/tag/foxit-reader)、[临时补丁](https://www.secpulse.com/archives/tag/%E4%B8%B4%E6%97%B6%E8%A1%A5%E4%B8%81)、[堆溢出](https://www.secpulse.com/archives/tag/%E5%A0%86%E6%BA%A2%E5%87%BA)、[堆溢出漏洞](https://www.secpulse.com/archives/tag/%E5%A0%86%E6%BA%A2%E5%87%BA%E6%BC%8F%E6%B4%9E)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)、[漏洞复现](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157....