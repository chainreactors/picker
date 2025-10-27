---
title: 逆向中巧遇MISC图片隐藏
url: https://www.secpulse.com/archives/205455.html
source: 安全脉搏
date: 2024-12-26
fetch_date: 2025-10-06T19:34:14.563077
---

# 逆向中巧遇MISC图片隐藏

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

# 逆向中巧遇MISC图片隐藏

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-25

13,094

这道题比较有意思，而且因为我对misc并不是很熟悉，发现该题目将flag隐藏在图片的颜色属性，巧妙的跟踪到这些密文位置，拿下题目一血，还是很有参考学习意义的。（题目附件，加V：dctintin）

## 1、图片RGB隐写

赛后去查阅了相关资料，发现该题采用了RGB隐写，特此总结一下，帮助读者理解。

lsb 隐写题在 ctf 中也经常考到，LSB即为最低有效位，我们知道，图片中的图像像素一般是由 RGB三原色（红绿蓝）组成，每一种颜色占用 8 位，取值范围为 0x00~0xFF，即有256 种颜色，一共包含了 256 的 3 次方的颜色，即 16777216种颜色。而人类的眼睛可以区分约 1000万种不同的颜色，这就意味着人类的眼睛无法区分余下的颜色大约有 6777216种。

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424826.png)

LSB 隐写就是修改 RGB颜色分量的最低二进制位也就是最低有效位（LSB），而人类的眼睛不会注意到这前后的变化，每个像数可以携带3 比特的信息。

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424827.png)

上图我们可以看到，十进制的 235表示的是绿色，我们修改了在二进制中的最低位，但是颜色看起来依旧没有变化。我们就可以修改最低位中的信息，实现信息的隐写

本题属于**修改RGB的最后一个位，一共可以隐藏三个位，RGB（三原色）**

R：隐藏最高位

G：隐藏最高位

B：隐藏最高位

## 2、实战

### 2.1 初识

题目给了一个ELF文件和一个png图片，猜测会对png进行解密操作

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424828.png)

很明显要么加密了图片，要么隐藏了数据

![pic_hide](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424829.png)

### 2.2 IDA 深入分析

我们先对整个题目流程做一定的理解，然后讨论解题思路

首先，自己搭建远程调试环境（比较简单，不在详细说明）

注意：要将题目提供的图片拖进dbgserv文件夹

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424830.png)

分析main函数

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424831.png)

发现代码可以分为三部分：

1、读取png图片内容和输入秘钥

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424832.png)

2、对png的RGB进行操作隐藏输入的秘钥

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424833.png)

3、关闭流环境

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424834.png)

我们可以这样理解，出题人会将flag作为输入的秘钥，经过程序操作隐藏在png的RGB中。

当然我们并不知道秘钥，但是可以构造一个假的flag，将其输入。此时我们可以看到程序将输入隐藏在png的哪些位置

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424835.png)

获得了这些位置之后（隐藏的是真正flag的组成位）就可以单独把这些隐藏的位拼接出来

```
0123456789abcdefghijklmnopqrstuv
```

从而得到flag

### 2.3 解题

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424836.png)

```
printf("Usage: %s [infile] [outfile]\n", *a2);

./cvhider pic_hide.png pic_hix.png
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424837.png)

运行程序会提示输入：

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424838.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424839.png)

分析part\_flag\_2

read\_png会返回加密数据存储的位置，我们直接复制，然后组成即可

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424840.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424841.png)

所以我们先解密part1

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424842.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424843.png)

```
lis1=[
    0xFF, 0xFF, 0xFF, 0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFE,
    0xFF, 0xFF, 0xFF, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01, 0x01, 0x01, 0x00, 0x01, 0x01, 0x01,
    0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x00,
    0x00, 0x00, 0x01, 0x01, 0x01, 0x00, 0x00, 0x01, 0x01, 0x00,
    0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x01, 0x00, 0x01, 0x01,
    0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01,
    0x00, 0x00, 0x01, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01, 0x01,
    0x00, 0x01, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
    0x01, 0x00, 0x00, 0x01, 0x01, 0x01, 0x00, 0x01, 0x01, 0x01,
    0x00, 0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00,
    0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00,
    0x00, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00,
    0x00, 0x00, 0xFE, 0x00, 0x00, 0xFE, 0x00, 0x00, 0xFE, 0x00,
    0x00, 0x00, 0x00, 0x00, 0xFE, 0x00, 0x00, 0xFE, 0x00, 0x00,
    0x00, 0x00, 0xFE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0xFE, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
```

```
]
for i in range(len(lis1)//8):

    for j in range(8):
        print(lis1[i*8+j] & 0x1, end="")
    print("", end=",")
```

生成

```
11100100,01110101,00000011,10111001,00001100,01110011,01001011,01100110,00101001,10100110,11001000,11001110,11101011,11110011,11111100,11010101,00000000,00000000,00000000,00000000,00000000,00000000,
```

拿到第一部分的flag

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202409201424844.png)

```
fa{9b1d692a3ae28
```

然后用同样的方法解密part2，注意part2密文长度为 32 字节

```
lis1=[
    0xFF, 0xFF, 0xFE, 0xFF, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
    0xFF, 0xFF, 0xFE, 0xFE, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFE, 0xFF, 0xFF, 0xFE, 0xFE, 0xFF, 0xFF, 0xFE, 0xFE, 0xFF,
    0xFE, 0xFE, 0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFE, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFE,
    0xFF, 0xFE, 0xFE, 0xFF, 0xFF, 0xFE, 0xFF, 0xFE, 0xFF, 0xFE,
    0xFE, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFE, 0xFE, 0xFE, 0xFF,
    0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFF, 0xFE,
    0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE,
    0xFF, 0xFE, 0xFE, 0xFE, 0xFE, 0xFF, 0xFE, 0xFF, 0xFE, 0xFE,
    0xFE, 0xFF, 0xFE, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFE, 0xFE, 0xFF, 0xFE, 0xFF, 0xFE, 0xFF,
    0xFF, 0xFF, 0xFE, 0xFE, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF, 0xFE,
    0xFE, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF, 0xFE, 0xFE,
    0xFF, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFE,
    0xFE, 0xFF, 0xFE, 0xFE, 0xFE, 0xFE, 0xFF, 0xFE, 0xFF, 0xFE,
    0xFE, 0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFF, 0xFF, 0xFE, 0xFE,
    0xFE, 0xFE, 0xFE, 0xFF, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFF,
    0xFE, 0xFE, 0xFE, 0xFF, 0xFF, 0xFF, 0xFE, 0xFE, 0xFE, 0xFF...