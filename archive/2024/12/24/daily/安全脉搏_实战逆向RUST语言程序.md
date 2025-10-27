---
title: 实战逆向RUST语言程序
url: https://www.secpulse.com/archives/205490.html
source: 安全脉搏
date: 2024-12-24
fetch_date: 2025-10-06T19:35:01.415075
---

# 实战逆向RUST语言程序

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

# 实战逆向RUST语言程序

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-23

12,004

实战为主，近日2024年羊城杯出了一道Rust编写的题目，这里将会以此题目为例，演示Rust逆向该如何去做。

题目名称：sedRust\_happyVm

题目内容：unhappy rust, happy vm

关于Rust逆向，其实就是看汇编，**考验选手的基础逆向能力**。在汇编代码面前，任何干扰都会成为摆设。

## 1、初步分析

64为程序，使用IDA 64打开

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544787.png)

通过字符串定位分析点

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544788.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544789.png)

现在我们知道 inputflag的长度大于 0x15

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544791.png)

接下来在汇编层面下一个断点，输入假flag，去观察相关寄存器的值

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544792.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544793.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544794.png)

好像并没有什么内容

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544795.png)

继续单步 步过，直到发现下一个要注意的地方！

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544796.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544797.png)

字符串长度：0x28

我们继续单步步过跟踪

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544798.png)

开辟空间的时候，说明快到真正函数处理过程了。

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544799.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544800.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544801.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544803.png)

## 2、分析加密流程

### 2.1 base64分割模块

这里简单将 3 字节变成4字节的操作，称之为 base64分割模块

这里举个例子

```
输入的："111"
->二进制字符串 001100010011000100110001
经过base64分割模块
->001100 010011 000100 110001
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544804.png)

发现程序执行完后正好是这样的结果

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544805.png)

### 2.2 组合

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544806.png)

举个例子：

假如分割之后的4字节为：

```
0xC、0x13、0x4、0x31
```

那么组合后的字符串

```
rax = 0xC
rcx = 0x1300
edx = 0xB1130C18
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544807.png)

### 2.3 VM处理模块

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544808.png)

发现func3 非常乱

并且频繁调用sub\_40A800()

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544809.png)

发现这是一道VM类型的题，那么VM的题加密应该会很简单，基本是异或之类。

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544810.png)

在 sub\_40A800 里面找到 异或，下断点

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544811.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544812.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544814.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544815.png)

这个al每经过两次就是秘钥

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544816.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410081544817.png)

### 解题脚本

```
int main() {
    //提取的密文
    unsigned char s1[] = { 0x00,0x82,0x11,0x92,0xa8,0x39,0x82,0x28,0x9a,0x61,0x58,0x8b,0xa2,0x43,0x68,0x89,0x4,0x8f,0xb0,0x43,0x49,0x3a,0x18,0x39,0x72,0xc,0xba,0x76,0x98,0x13,0x8b,0x46,0x33,0x2b,0x25,0xa2,0x8b,0x27,0xb7,0x61,0x7c,0x3f,0x58 };
    //提取的秘钥
    unsigned char s2[] = { 0x18,0xb1,0x9,0xa4,0xa6,0x2a,0x9e,0x1b,0x96,0x57,0x5d,0xad,0xae,0x75,0x65,0xac,0x9,0x8c,0xa0,0x76,0x47,0x2c,0x10,0x1,0x7c,0xf,0xba,0x47,0x95,0x30,0x9b,0x74,0x3f,0x2d,0x2d,0x9a,0x87,0x31,0xba,0x43,0x70,0x2c,0x4c };

    unsigned char s3[128] = { 0 };

    for (int i = 0; i < 43; i++) {
        s3[i] = s1[i] ^ s2[i];
    }
    //还原base64分割模块
    char s4[128] = { 0 };
    int j = 0;
    for (int i = 0; i < 44; i += 4, j += 3) {
        s4[j] = (s3[i] << 2) | (s3[i + 1] >> 4);
        s4[j+1] = (s3[i+1] << 4) | (s3[i + 2] >> 2);
        s4[j+2] = (s3[i+2] << 6) | s3[i + 3];

    }

    printf("%s", s4);

    return 0;
}
```

‍

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205490.html**](https://www.secpulse.com/archives/205490.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![solar应急响应月赛（5月）](https://pic1.imgdb.cn/item/683c718a58cb8da5c8218a94.png)

  solar应急响应月赛（5月）](https://www.secpulse.com/archives/206357.html "详细阅读 solar应急响应月赛（5月）")
* [![ApoorvCTF Rust语言逆向实战](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503061655549.png)

  ApoorvCTF Rust语言逆向实战](https://www.secpulse.com/archives/205975.html "详细阅读 ApoorvCTF Rust语言逆向实战")
* [![【总结】逻辑运算在Z3中运用+CTF习题](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407161541323.png)

  【总结】逻辑运算在Z3中运用+CTF习题](https://www.secpulse.com/archives/205237.html "详细阅读 【总结】逻辑运算在Z3中运用+CTF习题")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content...