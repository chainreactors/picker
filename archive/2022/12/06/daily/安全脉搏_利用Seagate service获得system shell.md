---
title: 利用Seagate service获得system shell
url: https://www.secpulse.com/archives/192747.html
source: 安全脉搏
date: 2022-12-06
fetch_date: 2025-10-04T00:33:50.965911
---

# 利用Seagate service获得system shell

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

# 利用Seagate service获得system shell

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-05

9,749

这是挖掘 CVE-2022-40286 漏洞的记录。

闲来无事，我上网随便找了一个驱动来进行测试。我想找一个知名公司的产品，但是又不能是太偏太难懂的东西。

我最先发现了一个叫"Seagate Media Sync"的软件，这是一个将文件复制到希捷无线硬盘上的工具。之后我安装并运行了该软件，然后我发现它创建了一个名为"MediaAggreService.exe"的后台SYSTEM服务。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207779.png "null")

然后发现这个工具还有一个UI安装程序。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207780.png "null")

我们一般常见的查找权限提升的方式是对低权限的进程（UI）和高权限服务（或驱动）之间的内部通信进行攻击开始的。要想使用这个方法，首先第一步我们要能够监控的来自UI的合法通信。然而，由于我没有与之配套的希捷硬盘，我们只能使用这个程序中非常少的功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207781.png "null")

通过查看进程资源管理器发现，该服务还包含了一个处理MEDIA\_AGGRE\_PIPE.PIP管道消息的句柄。猜测这个管道可能是用于用户界面（stxmediamanager.exe）和服务（MediaAggreService.exe）之间的通信。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207783.png "null")

通过观察用户界面，似乎我们可以点击的唯一按钮就是 "刷新"按钮。希望这能够让我们监控到一些服务通信。我们将调试器连接到用户界面进程，并在CreateFile和WriteFile函数上设置断点。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207784.png "null")

如上所示，当我们点击 "刷新 "按钮时，UI进程使用CreateFile函数进行了一个命名管道连接。我们可以检查之后调用的WriteFile函数来记录消息数据的内容。以下是写数据操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207786.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207790.png "null")

根据以上内容，我们可以猜测，第一个消息是一个4字节长度的字段，表示消息体的大小。第二条信息则是真实的命令数据。在这个事件中，它正在发送一条消息体长度为8个字节的命令。最初的4字节长度值与第二个WriteFile调用的nNumberOfBytesToWrite参数一致，这正符合我们的预期。我们现在可以检查该信息传递过程中的接收端。在MediaAggreService.exe中的ConnectNamedPipe函数上设置一个断点，该断点应该会在UI客户端调用CreateFile函数时触发。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-1670207791.png "null")

然后我们现在可以在ReadFile函数上设置一个断点，这样就可以看到从客户端发送的数据。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192747-16702077911.png "null")

现在我们已经找到了该服务中读取数据的代码，然后我们可以跟踪代码的执行流程。由于目前我们只能访问用户界面中的 "刷新 "命令，因此我们很有必要再进行一些静态分析，看看还有哪些命令可用。

在花了一些时间分析代码后，我可以看到每个命令都是以一个16位的签名（0x4B5C）开始的。之后是一个16位的 主命令ID，然后是一个32位的次命令ID。

```
001145BB | BA 5C4B0000             | mov edx,4B5C                                     | set expected command header signature: 0x4B5C
001145C0 | 0FB708                  | movzx ecx,word ptr ds:[eax]                      | get actual command header signature value
001145C3 | 66:3BCA                 | cmp cx,dx                                        | check 16-bit signature value
001145C6 | 74 1A                   | je mediaaggreservice.1145E2                      | jump if signature matches
001145C8 | 51                      | push ecx                                         |
001145C9 | 68 D8391200             | push mediaaggreservice.1239D8                    | "[PIPE] Failure: Bad Signature 0x%X"
001145CE | 68 F0841400             | push mediaaggreservice.1484F0                    |
001145D3 | E8 D866FFFF             | call mediaaggreservice.10ACB0                    | add_log_entry
001145D8 | 83C4 0C                 | add esp,C                                        |
001145DB | 33C0                    | xor eax,eax                                      |
001145DD | 5E                      | pop esi                                          |
001145DE | 8BE5                    | mov esp,ebp                                      |
001145E0 | 5D                      | pop ebp                                          |
001145E1 | C3                      | ret                                              | error, return
001145E2 | 57                      | push edi                                         |
001145E3 | FF70 04                 | push dword ptr ds:[eax+4]                        | log minor command ID (32-bit)
001145E6 | 0FB740 02               | movzx eax,word ptr ds:[eax+2]                    | log major command ID (16-bit)
001145EA | 50                      | push eax                                         |
001145EB | 68 203A1200             | push mediaaggreservice.123A20                    | "[PIPE] Command major/minor: [0x%X:0x%X]"
001145F0 | 68 F0841400             | push mediaaggreservice.1484F0                    |
001145F5 | E8 7667FFFF             | call mediaaggreservice.10AD70                    | add_log_entry
001145FA | 8B86 D0F00100           | mov eax,dword ptr ds:[esi+1F0D0]                 |
00114600 | C745 F8 00000000        | mov dword ptr ss:[ebp-8],0                       |
00114607 | 0FB740 02               | movzx eax,word ptr ds:[eax+2]                    | get major command value (message_base + 0x2)
0011460B | 83C4 10                 | add esp,10                                       |
0011460E | 83F8 10                 | cmp eax,10                                       | check if the major command value is 0x10
00114611 | 74 60                   | je mediaaggreservice.114673                      | jump to 0x10 command switch
00114613 | 83F8 20                 | cmp eax,20                                       | check if the major command value is 0x20
00114616 | 74 1A                   | je mediaaggreservice.114632                      | jump to 0x20 command switch
00114618 | 68 C83A1200             | push mediaaggreservice.123AC8                    | "[PIPE] Failure: Unknown Major Command"
0011461D | 68 F0841400             | push mediaaggreservice.1484F0                    |
00114622 | E8 8966FFFF    ...