---
title: 【勒索防护】曾经江湖地位并列如今却惨遭吞并揭秘 Conti 和 Lockbit 的“相爱相杀”
url: https://www.secpulse.com/archives/196489.html
source: 安全脉搏
date: 2023-02-22
fetch_date: 2025-10-04T07:41:18.926519
---

# 【勒索防护】曾经江湖地位并列如今却惨遭吞并揭秘 Conti 和 Lockbit 的“相爱相杀”

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

# 【勒索防护】曾经江湖地位并列如今却惨遭吞并揭秘 Conti 和 Lockbit 的“相爱相杀”

[漏洞](https://www.secpulse.com/archives/category/vul)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-21

11,092

**恶意家族名称：**

Lockbit

**威胁类型：**

勒索病毒

**简单描述：**

近期发现了 Lockbit 家族的新成员 LockbitGreen ，该勒索软件再次基于其他勒索软件修改而来，此前推出的 LockbitBlack 基于BlackMatter 勒索软件的代码编写，而 LockbitGreen 基于 Conti 泄露的源代码编写。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966042.gif)

**1.恶意事件描述**

2022 年 2 月，Conti 集团泄密者使用账号名为 @ContiLeaks 的 Twitter 帐号来发布 Conti 勒索组织的内部数据,包括来自 Jabber 的内部聊天记录、基础设施的详细信息、内部文件及 Conti 勒索软件的源代码。2022 年 5 月，Conti 勒索软件集团决定进行重组和更名。下图为 Conti 勒索软件与 LockbitGreen 勒索软件主函数的流程预览窗口，通过预览整个函数流程，发现代码逻辑极为相像，此外他们设置相同的互斥量 “hsfjuukjzloqu28oajh727190”。

此次发现的 LockbitGreen 使用了 Conti 的新加密器，而 Lockbit 家族本身的加密器工作正常，猜测二者可能达成了某种合作关系，重用和改编知名竞争对手的源代码的方法有助于降低开发成本和时间。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966043.png)

**Lockbit 勒索家族的发展**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966044.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966049.gif)

**2.恶意事件分析**

本次勒索病毒活动共发现两个样本，文件名为 LBB.malz 为 32 位的勒索程序，该勒索程序的分析可以完全参考如下链接：https://mp.weixin.qq.com/s/zT1GbqXFkj0FHiUhNlisZg，整体代码及功能逻辑几乎一致。文件名为 LBG64.malz 为 64 位的勒索程序，该程序为 Lockbit3.0 新增的成员 LockbitGreen。本文分析以 LBG64.malz 为主。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966050.png)

LBG64.malz 执行后，被加密后的文件默认添加后缀名 “.fb7c204e”，勒索信文件名为 “!!!-Restore-My-Files-!!!.txt”，内容如下图所示。每个受害者有唯一的个人 ID,受害者可以借助 Tor 浏览器或正常的浏览器通过链接与攻击者取得联系，勒索信中并未提及赎金金额，并且建议受害者不要试图联系网络保险及数据恢复组织并阐述原因。

**!!!-Restore-My-Files-!!!.txt 勒索信内容**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-16769660501.png)

**加密后文件系统情况**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966059.png)

**ATT&CK**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-16769660591.png)

**功能分析**

参数启动

该样本可以无参数启动，也可以以可选参数的形式启动，可供选择的参数如下所示，GetCommandLineW 和 CommandLineToArgvW 函数来获取运行恶意软件时使用的命令行字符串。这两个函数的输出将用于检查执行恶意软件时是否使用了额外的参数：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966062.png)

网络通信

它首先扫描同一网络子网并尝试使用 SMB 端口 445 连接到其他设备，并感染同一网段其他设备

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-16769660621.png)

下图显示了 Process Monitor 捕获了该勒索软件尝试使用 TCP 连接到从 192.168.83.1 到 192.168.83.254 的 IP 地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966064.png)

**防御规避**

1、 动态解密 API

解密出 API 该勒索软件使用动态 API 加载和 hash 来隐藏库和 API 名称，这些库和 API 名称用于隐藏静态分析和传统的基于签名的恶意软件扫描程序的功能。混淆了其所有 API 调用和库名称，并在运行时动态解析它们。这种混淆技术确保 Conti 仍然可以访问其所有 API，而无需将它们直接写入导入表，这将使它们对可能的逆向工程师完全隐藏。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966070.png)

它会动态解析模块名称并加载它们以供执行。该勒索软件解析模块名称，包括netapi32.dll、apphelp.dll、kernelbase.dll、msvcp\_win.dll、win32u.dll、gdi32full.dll、ucrtbase.dll、msvcrt.dll、rpcrt4.dll、kernel32.dll、user32.dll、imm32.dll、ws2\_32.dll、gdi32.dll、ntdll.dll

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966078.png)

该勒索软件会创建 ”hsfjuukjzloqu28oajh727190” 的互斥体，以确保只有一个勒索软件实例正在受害者的机器上运行，多个实例同时运行的话，会干扰并减慢加密过程。**值得注意的是，Putin和Conti勒索软件的部分样本也会创建 ”hsfjuukjzloqu28oajh727190” 互斥锁。**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966085.png)

**发现**

1、文件和目录发现

调用 GetLogicalDriveStringsW，获取驱动器信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966090.png)

从 C:-Z: 枚举磁盘驱动器

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966091.png)

2、枚举进程

调用 CreateToolhelp32Snapshot 为系统中所有的进程和线程拍摄一个快照

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966093.png)

调用 Process32FirstW 获得句柄和指定的进程信息，搜索目录下的文件 / 目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966096.png)

调用 Process32NextW 根据句柄循环查找其他进程的信息，并搜索其文件目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966100.png)

**影响**

1、阻止系统恢复

删除卷影，避免受害者通过卷影恢复系统

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966103.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966106.png)

2、数据加密

避免加密的文件或扩展

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-16769661061.png)

避免加密的目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966107.png)

生成被加密扩展 ”.fb7c204eb”。加密操作完成后，将 .fb7c204e 扩展名附加到被加密的每个文件名后

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966108.png)

该样本采用 AES-256 和 ChaCha20 算法相结合的加密方式，根据文件的大小和类型提供三种不同的加密模式，加密模式分别为 0x24、0x25、0x26

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966109.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196489-1676966110.png)

**IOCs**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploa...