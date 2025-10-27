---
title: LLVM IR 深入研究分析
url: https://www.secpulse.com/archives/205330.html
source: 安全脉搏
date: 2025-01-10
fetch_date: 2025-10-06T20:07:09.916864
---

# LLVM IR 深入研究分析

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

# LLVM IR 深入研究分析

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-09

12,487

# 前置知识

> LLVM是C++编写的构架编译器的框架系统，可用于优化以任意程序语言编写的程序。

LLVM IR可以理解为LLVM平台的汇编语言，所以官方也是以语言参考手册(Language Reference Manual)的形式给出LLVM IR的文档说明。既然是汇编语言，那么就和传统的CUP类似，有特定的汇编指令集。但是它又与传统的特定平台相关的指令集(x86,ARM,RISC-V等)不一样，它定位为平台无关的汇编语言。也就是说，LLVM IR是一种相对于CUP指令集高级，但是又是一种低级的代码中间表示（比抽象语法树等高级表示更加低级)。

LLVM IR即代码的中间表示，有三种形式：

* **.ll 格式**：人类可以阅读的文本(汇编码) -->这个就是我们要**学习**的IR
* .bc 格式：适合机器存储的二进制文件
* 内存表示

下面给出.ll格式和.bc格式生成及相互转换的常用指令清单：

```
.c -> .ll：clang -emit-llvm -S a.c -o a.ll
.c -> .bc: clang -emit-llvm -c a.c -o a.bc
.ll -> .bc: llvm-as a.ll -o a.bc
.bc -> .ll: llvm-dis a.bc -o a.ll
.bc -> .s: llc a.bc -o a.s
```

那么我们以一道CTF赛题来分析实验，学习LLVM IR

# 实验解析

题目附件直接给出了中间表示.II文件

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618479.png)

打开查看一下汇编码，毕竟.II文件是人类可以阅读的文本，这边笔者使用的是Sublime Text（使用VScode查看即可）代码量不多，大概600行

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618199.png)

## 题目初步分析

我们直接寻找一下main函数

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618569.png)

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618544.png)

我们可以看出题目经历了两次RC4，然后Base64，我们从上面可以看到密文，RC4\_key,我们直接一把锁，cyberchef启动，会发现解不出来，那么程序应该做了其他的操作，最朴素的，我们可以想到把RC4魔改了，base64魔改等等。

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618553.png)

So！继续学习研究ing

【帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：dctintin，备注 “安全脉搏” 获取！】

① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

## .II详细分析

所以本着学习的态度，我们这时候应该掏出**LLVM** **Language Reference Manual**(官方文档)来简单了解学习一些常见指令、符号标识以及特性。这边给出一些分析 .ll 中间文件的算法流程

```
@ - 全局变量
% - 局部变量
alloca - 在当前执行的函数的堆栈帧中分配内存，当该函数返回到其调用者时，将自动释放内存
i32 - 32位4字节的整数
align - 对齐
load - 读出，store写入
icmp - 两个整数值比较，返回布尔值
br - 选择分支，根据条件来转向label，不根据条件跳转的话类型goto
label - 代码标签
call - 调用函数
```

首先看到一些全局变量，知道了RC4\_key = llvmbitccipher = "TSz`kWKgbMHszXaj`@kLBmRrnTxsNtZsSOtZzqYikCw="

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618578.png)

我们继续分析，重点分析各个function

### b64encode

b64encode 魔改

1. 每三个字符，24位，切分成4断，每段6位。
2. 将6位对应的值 (value+ 59)&0xff 则是编码后的值。

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618312.png)

```
  %22 = getelementptr inbounds i8, i8* %19, i64 %21        // 取出当前处理字符
  %23 = load i8, i8* %22, align 1
  %24 = zext i8 %23 to i32                                 // 类型强制转化
  %25 = ashr i32 %24, 2                                   // 算数右移两位   input[i]>>2
  %26 = add nsw i32 %25, 59                                 //    input[i]+59
  %27 = trunc i32 %26 to i8                                //    强制转化  相当于 &0xff
  %28 = load i8*, i8** %6, align 8
  %29 = load i32, i32* %9, align 4
  %30 = sext i32 %29 to i64
  %31 = getelementptr inbounds i8, i8* %28, i64 %30        // 存储base64 编码串
  store i8 %27, i8* %31, align 1
  %32 = load i8*, i8** %4, align 8
  %33 = load i32, i32* %7, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds i8, i8* %32, i64 %34
  %36 = load i8, i8* %35, align 1
  %37 = zext i8 %36 to i32
  %38 = and i32 %37, 3                              // 获取第一个字符 低两位
  %39 = shl i32 %38, 4                                // 左移四位
```

### RC4\_init

RC4\_init 正常，无魔改

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618416.png)

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618452.png)

```
define dso_local void @Rc4_Init(i8*, i32) #0 {                           //RC4_init function
  %3 = alloca i8*, align 8
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i8* %0, i8** %3, align 8
  store i32 %1, i32* %4, align 4                                         //初始化S，T盒
  call void @llvm.memset.p0i8.i64(i8* align 16 getelementptr inbounds ([256 x i8], [256 x i8]* @s, i64 0, i64 0), i8 0, i64 256, i1 false)
  call void @llvm.memset.p0i8.i64(i8* align 16 getelementptr inbounds ([256 x i8], [256 x i8]* @t, i64 0, i64 0), i8 0, i64 256, i1 false)
  store i32 0, i32* %5, align 4
  br label %7

7:                                                ; preds = %26, %2
  %8 = load i32, i32* %5, align 4
  %9 = icmp slt i32 %8, 256
  br i1 %9, label %10, label %29                          //如果 %9 为真（即 %8 小于 256），跳转到标签 %10；否则跳转到标签 %29，根据t打乱s盒

10:                                               ; preds = %7
  %11 = load i32, i32* %5, align 4
  %12 = trunc i32 %11 to i8
  %13 = load i32, i32* %5, align 4
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds [256 x i8], [256 x i8]* @s, i64 0, i64 %14
  store i8 %12, i8* %15, align 1
  %16 = load i8*, i8** %3, align 8
  %17 = load i32, i32* %5, align 4
  %18 = load i32, i32* %4, align 4
  %19 = urem i32 %17, %18
  %20 = zext i32 %19 to i64
  %21 = getelementptr inbounds i8, i8* %16, i64 %20
  %22 = load i8, i8* %21, align 1
  %23 = load i32, i32* %5, align 4
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds [256 x i8], [256 x i8]* @t, i64 0, i64 %24
  store i8 %22, i8* %25, align 1
  br label %26

26:                                               ; preds = %10
  %27 = load i32, i32* %5, align 4
  %28 = add nsw i32 %27, 1
  store i32 %28, i32* %5, align 4
  br label %7

29:                                               ; preds = %7
  store i32 0, i32* %6, align 4
  store i32 0, i32* %5, align 4
  br label %30

30:                                               ; preds = %54, %29
  %31 = load i32, i32* %5, align 4
  %32 = icmp slt i32 %31, 256
  br i1 %32, label %33, label %57

33:                             ...