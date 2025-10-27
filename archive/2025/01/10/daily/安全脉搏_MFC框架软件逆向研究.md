---
title: MFC框架软件逆向研究
url: https://www.secpulse.com/archives/205348.html
source: 安全脉搏
date: 2025-01-10
fetch_date: 2025-10-06T20:07:10.872173
---

# MFC框架软件逆向研究

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

# MFC框架软件逆向研究

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-09

13,198

# MFC框架简介

什么是mfc？

> MFC库是开发Windows应用程序的C++接口。MFC提供了面向对象的框架，采用面向对象技术，将大部分的Windows API 封装到C++类中，以类成员函数的形式提供给程序开发人员调用。

简单来说，MFC是一种面向对象，用于开发windows应用程序的框架，突出特点是封装了大部分windows API，便于开发人员使用（写win挂方便）。

MFC程序的运行过程分为以下四步：

1. 利用全局应用程序对象theApp启动应用程序。
2. 调用全局应用程序对象的构造函数，从而调用基类（CWinApp）的构造函数,完成应用程序的一些初始化工作，并将应用程序对象的指针保存起来。
3. 进入WinMain函数。在AfxWinMain函数中获取子类的指针，利用指针实现上述的三个函数，从而完成窗口的创建注册等工作。
4. 进入消息循环，一直到WM\_QUIT。

那么问题来了，我们如何逆向mfc程序呢？因为其封装了大部分windows API，逆向起来也复杂了不少，因为需要了解大量的windows api 并且熟悉windows编程。下面进行讲解。

# MFC如何逆向

如下图，是MFC框架软件的基本界面，可以看到，就是一堆button，主要逆向也是check button。

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514389.png)

那么，对于MFC逆向，我们主要需要知道的是，当我们执行某个操作（点击某个按钮）的时候，程序会执行什么处理函数。在mfc中，程序是使用消息机制来实现操作响应的，这个是消息映射表的代码：

```
struct AFX_MSGMAP{
    AFX_MSGMAP * pBaseMessageMap;
    AFX_MSGMAP_ENTRY * lpEntries;
}
struct AFX_MSGMAP_ENTRY{
    UINT nMessage;    //Windows Message
    UINT nCode        //Control code or WM_NOTIFY code
    UINT nID;         //control ID (or 0 for windows messages)
    UINT nLastID;     //used for entries specifying a range of control id's
    UINT nSig;        //signature type(action) or pointer to message
    AFX_PMSG pfn;     //routine to call (or specical value)
}
```

其中这个**AFX\_MSGMAP\_ENTRY**中的最后一个成员**AFX\_PMSG**就是一个函数指针，指向了当前控件绑定的函数。同时，这个nID成员描述的是当前控件的ID，利用这个ID就能确定我们所寻找的控件。然后这个AFX\_MSGMAP结构体则会记录一个指向AFX\_MSGMAP\_ENTRY的指针，于是查找控件的注册函数的思路可以缩小为:

* 找到AFX\_MSGMAP
* 找到控件的ID --- 关键就是找ID

那么，我们又该怎么找到控件ID呢，俗话说“**工欲善其事，必先利其器**”，作为逆向分析人员，肯定要选择好分析的工具了，很庆幸，我们站在巨人的肩膀上，针对mfc软件程序的逆向分析，前辈们已经开发了一些非常好用的小工具，我们可以直接使用它们。例如：

1. xspy
2. ResourceHacker
3. 彗星小助手

其中我们主要用的是xspy，mfc分析利器如下图所示

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514386.png)

# 逆向实验-以CTF赛题为例讲解

## demo1 - MFC初探

打开程序软件

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514378.png)

程序的标题**Flag就在控件中**，然后界面内容是让我们找一个key。很明显，我们需要找到两个东西

1. 标题找Flag（也就是找窗口句柄）
2. 内容找key

根据这些内容，告诉我们我们去找控件，然后这时候就要掏出xspy了。不然的话，我们如果使用老一套经典分析流程，die+ida对用架构分析，会发生下面这样的事。首先die查个架构，查个壳

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514401.png)

好家伙，VMP壳，PE32ida走起，如下图，emmm....

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514435.png)

这样的话，我们很难继续往下分析，所以我们使用xspy分析。使用方法如下图

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514418.png)

首先我们找到了Flag\_enc(944c8d100f82f0c18b682f63e4dbaa207a2f1e72581c2f1b)我们知道特定的，窗口句柄叫 HWND

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514154.png)

然后我们可以发现一条特殊的onMsg`OnMsg:0464,func= 0x00402170(MFC1.exe+ 0x002170 )`为什么特殊呢，因为只有它并不是以宏的形式出现，应该是作者自定义的消息，没有button等东西，所以程序怎么点击都无法触发任何效果；并且传入一个特殊数字0464，来触发效果。

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514242.png)

那么，我们需要去发送这条消息来出发func函数以获取我们需要的key

```
#include<Windows.h>
#include<stdio.h>
int main()
{
    HWND h = FindWindowA(NULL, "Flag就在控件里");
    if (h)
    {
        SendMessage(h, 0x0464, 0, 0);
        printf("success");
    }
    else printf("failure");
}
```

使用 API FindWindow 获取窗口句柄，SendMessage发送消息，得到了key{I am a Des key}

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514217.png)

最后DES解密即可

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514272.png)

flag{thIs\_Is\_real\_kEy\_hahaaa}

## Junk\_instruction-西湖论剑

下面，再讲解一道大型比赛的赛题来实验打开，看到这个朴素的界面可以鉴定是MFC框架。

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514403.png)

我们看到了一个input，还有一个check button，很明显，我们首先就需要去找check button的id&注册函数。

### xspy-MFC分析

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514982.png)

check按钮的id为03e9，同时窗口存在OnCommand: notifycode=0000 id=03e9,func= 0x00C72420(Junk\_Instruction.exe+ 0x002420 )函数。那么对应的check逻辑肯定在基址+偏移0x002420处。打开ida，找到check函数 sub\_402420 ，如下图

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514965.png)

可以看到有一个条件判断：if ( (unsigned \_\_int8)sub\_402600(v2 + 16) )。一眼顶针，两个分支分别是弹出正确和错误的对话框，为什么呢？if else函数体内容基本一样。当然我们还是动态调试一下

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514996.png)

所以enc函数很明显就是sub\_402600这个函数中就出现了很多垃圾指令了，也就对应上题目名称Junk\_instruction了。

### 去花-IDA分析

爆红

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514059.png)

花指令，经典call $+5起手，就是先用一个call压好返回地址，再把栈里的返回地址弹出来，改一下，压回去，如此反复。去掉也很简单，我们把下述累死指令块全部nop掉即可，有好几处，一模一样。

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514173.png)

当然，我们使用idapython脚本自动去花

```
    from ida_bytes import get_bytes, patch_bytes
    import re
    addr = 0x402600
    end = 0x402fe3
    buf = get_bytes(addr, end-addr)
    def nopp(s):
        s = s.group(0)
        print("".join(["%02x"%i for i in s]))
        s = b"\x90"*len(s)
        return s
    pattern  = b"\xe8\x00\x00\x00\x00\x58\x89.*?\xc3.*?\x22"
    buf = re.sub(pattern , nopp, buf, flags=re.I)
    patch_bytes(addr, buf)
    print("Done")
```

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514187.png)

### 加密

去除花指令，简单审计发现是对程序进行RC4加密，最后还对输入进行了个倒叙

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514831.png)

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514790.png)

![image.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408141514798.png)

去花后，整理一下，代码如下

```
char __thiscall sub_402600(void *this, int a2)
{
  const WCHAR *v2; // eax
  void *v3; // eax
  char v5[511]; // [esp+9h] [ebp-4BBh] BYREF
  int v6; // [esp+208h] [ebp-2BCh]
  char *v7; // [esp+20Ch] [ebp-2B8h]
  int v8; // [es...