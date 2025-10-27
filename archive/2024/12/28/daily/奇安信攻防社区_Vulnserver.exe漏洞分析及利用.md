---
title: Vulnserver.exe漏洞分析及利用
url: https://forum.butian.net/share/4013
source: 奇安信攻防社区
date: 2024-12-28
fetch_date: 2025-10-06T19:33:34.481005
---

# Vulnserver.exe漏洞分析及利用

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Vulnserver.exe漏洞分析及利用

* [漏洞分析](https://forum.butian.net/topic/48)

本章为笔者在学习二进制安全过程中的学习记录，vulnserver为公开的二进制漏洞的练习程序，本章节的内容为vulnserver.exe的漏洞分析及复现，主要通过windbg和ida结合进行分析。因为vulnserver存在多种调试漏洞，本文主要使用trun参数进行漏洞分析及利用。

一、调试、查看vulnserver功能
-------------------
启动vulnserver后，其服务运行在9999端口上
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0552093ed15bf7ad603d5e4ed6c5fc9931a215ab.png)
知道服务运行的端口号后，为了更好的探测vulnserver的功能，我们可以使用简单的poc进行探测：
```php
#!/usr/bin/python
import socket
import sys
from struct import pack
try:
 server = sys.argv\[1\]
 port = `9999`
 size = 10
 inputBuffer = b"\\x41" \\* size
 buf = inputBuffer
 print("Sending evil buffer...")
 s = socket.socket(socket.AF\\_INET, socket.SOCK\\_STREAM)
 s.connect((server, port))
 s.send(buf)
 s.close()
 print("Done!")
except socket.error:
 print("Could not connect!")
```
同时打开ida查看程序的执行结构：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-969ebbd8144b36954d7f395387ce8ca6c7753697.png)
### 1.在数据接收处下断
在windbg中打开vulnserver后，我们可以看到程序导入的动态链接库，其中存在WS2\\_32.DLL，该dll一般用于程序使用其中的网络通信函数，因为我这里初始发送了10个41，所以我们可以对其中的recv函数下断：bp ws2\\_32!recv
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-93083ae10fe401e89bfb07676dcecfadd01c91d0.png)
Poc运行后，windbg成功断在WS2\\_32!recv处：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-bd4d7b029a8eb9ba6586ef1e80b1a3ca65b1f535.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-091a41a01d1463b61f5399b05b5e7f2a617bc434.png)
接下来需要对vulnserver的内部函数进行分析，而不是分析该通信函数。这里我们可以使用pt命令执行到函数的返回：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-2a6b5b85f365f14754500a03cbdc03eebd48727e.png)
此时，我们可以在ida中通过jump to address查看当前地址00401958：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-2ba075e5097d285cc89b0e6afb972bfda06c6722.png)
通过ida的跳转后，我们发现程序在完成recv函数后，主要有以下指令：
mov \[ebp+var\\_410\], eax 指令会将当前eax的内容传给ebp+var\\_410处的地址中；
cmp \[ebp+var\\_410\], 0 指令会将该地址中的值与0进行比较；
根据比较的结果在进行跳转，这里的jle指令意思就是ebp+var\\_410中的值如果是小于0的话，就执行跳转；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1e47458a7430ff63301c0496d7800bd079895c1a.png)
Windbg中进行调试，当前eax的值为ffffffff也就是负一，当mov指令执行后，ebp-410h的值也就为负一，所以这里的jle会进行跳转br=1。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4cb6d9f4ddfe613e788778f46807ff1682a919a5.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b48dafaff8823e8775f0af38452b6115c5b8dd68.png)
在ida中进行查看后我们发现，程序的多数功能都在右边，当jle跳转后，则直接来到了closesocket处了，这将让我们无法进行后续的分析。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1f9f142bfbd520966a84b78beb7f7d490390f696.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6c9453e2ef6ecc962d8e25116df9e623bb80d5b7.png)
### 2.分析vulnserver的参数
所以我们需要回过头再查看我们jle的跳转处，发现疑似存在多处指令参数。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4bcbedc26613543a0abc2ec05d85478e9a16b207.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-039490f04919cd32ce7a1dafcbab057f7509be04.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-dc6299d3497490d5f4bcd828dd1f8401149db3c6.png)
我们可以手动在windbg中进行确认，当程序执行来到0040195b地址处的mov指令时，我们可以先手动将eax的值修改为大于0的数，让jle不进行跳转。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-53b8f6b03fb8b578bfdd4e016ddd332f5575d75b.png)
此时我们来到地址0040196e处，该代码块中存在函数strncmp，其中string1, string2为要比较的字符串，count为要比较的字节数。函数原型如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4df5a644d921376f6ccebaa29337b4d1b8c97a57.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-74bf455518b7a85db4e9904138f15a4eb1534d1b.png)
### 3.输入HELP参数
我们可以在windbg中查看此处strncmp比较的内容，当程序执行来到call strncmp后，此时的esp的中包含该函数执行时的3个参数，其中00e883c8为第一个参数即我们输入的源缓冲区，00404244为比较的参数此处为HELP，00000005为比较的字节，但由于我们手动修改了eax的值，导致缓冲区复制错误，所以程序执行到此处时没有收到我们输入的数据。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-22b04a7f62f79e65cca0e3b1c531929c9ccd7223.png)
为了继续探测vulnserver的功能，我们需要更新poc：
```php
#!/usr/bin/python
import socket
import sys
from struct import pack
try:
 server = sys.argv\[1\]
 port = 9999
 size = 100
 inputBuffer = b"HELP"
 inputBuffer += b"\\x41" \\* size
 buf = inputBuffer
 print("Sending evil buffer...")
 s = socket.socket(socket.AF\\_INET, socket.SOCK\\_STREAM)
 s.connect((server, port))
 s.send(buf)
 s.close()
 print("Done!")
except socket.error:
 print("Could not connect!")
```
发送poc后，在windbg中进行调试，此时，我们可以在地址00401984处下断点并查看此时strncmp的参数，此时地址00e897d8即为我们输入的HELP和41字节，这里需要注意的是我们在poc中输入的参数为”HELP”而地址00e897d8处的参数为”HELP ”，是多了一个空格的：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-edc27418aed617c6b6efc322c6b02bcc619012cc.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-afeb682d246d40fc59aba884568a2108c4126925.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-87a1ade755d0ba823a18ecd88bafedd8100e44e4.png)
所以当执行来到地址004019F3处时，程序则不会进行跳转，而来到HELP参数对应的函数底部了：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-369ba37a0d0cca450bf23992b208ad60ecc11f75.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1ea559475adcd295de6f040521b8289e5f973f65.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a9651070293c831f840a086df61b0c4b2a4d3bd0.png)
考虑到vulnserver中还存在其他参数，而HELP指令并非我们进行主要需要分析的参数，所以，让我们回到ida中，分析是否还存在其他参数可以进行利用，而本文主要是通过trun参数进行漏洞分析及利用。
二、分析TRUN参数
----------
在知道如何使用不同的参数探测程序不同的功能点后，我们将使用TRUN参数来对后续的功能进行分析：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-46091b7ce5d06a64be8bc5f5a20290aa30fff8b5.png)
修改我们的poc：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-fa833c032e1ac277f84ccac833ad69e6937c250f.png)
发送poc后，windbg在地址00401CF1处下断点，此时我们来到地址00401CF8处的跳转时，由于eax的值为0，所以jne不会进行跳转，此时执行会来到00401CFE
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-48787372647c23d43225e6de898e531f06d83dd5.png)
在这里我们发现程序通过malloc分配一块内存，然后通过memset将数据复制到分配的内存中去：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3112a251bb72cfc2b2a772484776aa0f4b83c72b.png)
Malloc、memset函数原型如下：
dest为指向目标的指针，c为要设置的字符，count为字符数：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6e59f6293b7d42fc2be314cf0b3dd02a3d048426.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-27109d9c3276ed26a0d78beed523337ba842474e.png)
地址00401d05为malloc函数，通过windbg调试，发现程序通过malloc分配了3000字节的缓冲区，在00401d29处，memset将在地址006e4028开头初始化（置0）3000字节的空间：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0d864c760bb6b15e565b0a3854d9eb82714147f1.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0479fbdf719d7da7d55708165246220b9b7e5055.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-de6a9ebabb4363fd0af7d973cb4dfd982809ccf3.png)
完成上述操作后，执行来到地址00401D38处，通过windbg我们发现，这里程序将ebp+var\\_418的值也就是5传给eax，然后与ebp+len也就是我们poc中发送的0x41的长度1000字节进行比较，jge指令（大于或等于则跳转）则不会进行跳转：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/a...