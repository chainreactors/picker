---
title: 对AgentTesla恶意软件多阶段加载器的一次手动分析
url: https://forum.butian.net/share/3696
source: 奇安信攻防社区
date: 2024-09-05
fetch_date: 2025-10-06T18:23:50.850383
---

# 对AgentTesla恶意软件多阶段加载器的一次手动分析

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

### 对AgentTesla恶意软件多阶段加载器的一次手动分析

前言（概述）
Agent Tesla 是一款自2014年就存在的密码窃取间谍软件，它通过记录按键和用户交互来收集有关受害者行为的信息。
Agent Tesla使用.Net软件框架（大多数窃密恶意软件都是基于.NET框...

前言（概述）
======
Agent Tesla 是一款自2014年就存在的密码窃取间谍软件，它通过记录按键和用户交互来收集有关受害者行为的信息。
Agent Tesla使用.Net软件框架（大多数窃密恶意软件都是基于.NET框架开发的），其目的是窃取个人数据并将其传输回C2服务器，该恶意软件能够从Web浏览器、电子邮件客户端和FTP服务器访问信息。
此外，Agent Tesla恶意软件还能够捕获屏幕截图和视频，记录剪贴板信息和表单值。除了窃密行为外，该恶意软件还配备了多种持久性操作和规避技术。例如在系统重启后自动恢复运行，关闭Windows进程以保持隐藏。
Agent Tesla的传播主要通过垃圾邮件活动，通常是经过恶意文档或恶意网络链传递给受害者，访问这些maldocs或url后，有效负载将自动下载倒受害者的系统上，一般间谍软件会将自身保存在`%temp%`文件夹中，然后自动执行。
IOC
===
| Hash | Value |
|---|---|
| SHA256 | 7512be2746137d9694e3ec3a83e8ab4c6e4d826798a04381de53d4c6973d519f |
| SHA1 | 0ccbe92478dca12afc4256bbfa0cefa95eed98d0 |
| MD5 | 3a8596945040461302d54f41d5fa9fb9 |
样本下载地址（沙箱链接）：<https://bazaar.abuse.ch/sample/7512be2746137d9694e3ec3a83e8ab4c6e4d826798a04381de53d4c6973d519f/?ref=embeeresearch.io>
DIE分析
=====
首先使用DIE查看一下该文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-a5c30506b1f9960b67d9bfee32b0ceef2331c26a.png)
一个\*\*Nullsoft Scriptable Install System（NSIS）\*\*打包的exe安装程序，NSIS会将一个`.nsi`脚本和其他程序打包起来,本质上是个压缩包,可以直接使用7-zip解压。
解压后可以得到三个文件，（理论上是还有一个nsi脚本的，但不知道为啥我解压出来没有）
![image-20240808141009017](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-70afcfbdae18c9b713f50cbf9789da97c0ee4398.png)
cwlkewfbz.exe
-------------
对三个文件依次DIE分析
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c16167a61b3bcf274d7f1094900f07ea1d25298d.png)
`cwlkewfbz.exe`是一个32位的程序，（意外的居然不是.NET框架构建的）看上去没有混淆保护，查看一下信息熵：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fe425f3b63bbeefabb61f19e81a03e561b4baaf9.png)
没有高而平坦的区域。
通常从DIE分析一个恶意样本，可以查看基本信息，信息熵判断有无加壳或嵌入有效负载，字符串查看是否有可疑混淆或者一些明显的特征，导入表或导出表也可以发现一些常见于恶意行为的函数，此处查看一下导入表：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-cbaa55c172b7bd0753d5674ac9b925093dcbdd6f.png)
发现一个`VirtualAlloc`,该函数用于在地址空间分配内存，一般用于嵌入有效负荷。
djdqvq.sra
----------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-213950f928970969e47ca0fa1c4b9a38aafa426b.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-5c4d910e7cdd04cceabafe3db580d22e2433fba3.png)
`.sra` 文件是一个二进制文件，基本信息没有，但是查看信息熵可以知道该文件被加密了。（高而平坦的曲线）
pgkayd.aq
---------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-92a4db6bfa9b8fb85d7dcab68448de26e4b38967.png)
`.aq` 文件同上。熵值不如上一个的的高，可能是低加密。
x32dbg动态分析
==========
先对`cwlkewfbz.exe`进行分析。根据上面DIE分析和以往的经验判断，推测一下该exe中应该是藏有有效负荷的，即该exe只是一个Loader。
载入Xdbg中。
利用硬件断点提取shellcode
-----------------
命令 `bp VirtualAlloc` ，F9运行：
![image-20240808142814691](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8c038419caa61af93be5bcbf4908b1e75dc7f2f7.png)
程序直接跑飞了，说明从`Entry`到`VirtualAlloc`之间还存在某种反调试。
### IDA静态分析
![image-20240808144926183](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-447fd7464f0024d8084dfadac8e5688c5ba6af16.png)
IDA32载入后，幸运的发现`VirtualAlloc`就在眼前，而且加密逻辑也很清晰，异或之后就执行代码了。
问题回到刚刚的 为什么`VirtualAlloc`之前就停止了呢？
### 时钟反调试
![image-20240808145121410](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-bc5a7ab591694ae031fd4d1ddf5b9b39ed939eca.png)
一处很简单的时钟反调试，由于沙箱或调试器的特性（经常将sleep设置为0）
这里先是`GetTickCount`获取自程序运行开始的时钟数，然后sleep了702毫秒（0x2BE=702毫秒，0x2BC=700毫秒）
睡眠之后再次`GetTickCount`，如果小于700则退出。
实际运行起来，发现这里并没有影响，将注意力放在 `CreatFileA`上：
### 监视CreateFile
![image-20240808145855894](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fe85426230fd2c48ded29f6b2415680e7ae0e06a.png)
回顾一下该函数的定义：
![image-20240808150152009](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f6debb56b73d0c77b35c0011cbe012d8145e210e.png)
根据函数的调用约定以及堆栈关系，可以知道 `ecx` 就是lpFileName，那么我们是否就可以根据该值来确定恶意软件要打开的文件是什么。（其实猜也猜到了，不是.aq就是.sra）
![image-20240808150447861](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-96bb63f3f671402eeb5e830d84bba6b74ed81551.png)
出现问题了，传入的ecx是0，也就是这一步导致后面的if判断都不可能实现。
最后问题还是回到`.nsi`脚本,该脚本可以控制包内应用程序的所有行为。后来发现是7-zip的版本太高了，一直降到15.05就可以提取到nsi脚本了。
使用notepad++查看一下：
![image-20240808153115734](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-bf9ab3622ae0202b667ca7bad38088b5194100b1.png)
看不懂，GPT解决一下，最后这句的意思就是，执行 `cwlkewfbz.exe` 传递 `pgkayd.aq`作为参数。那么逻辑就清晰了，接着回到xdbg中，借助xdbg的File Command Line功能
### Xdbg修复CreateFile
![image-20240808153419732](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4dfdaaf47472fac51fbd1680191d57040f8061ae.png)
![image-20240808153448863](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-44011c4482b00b4bf3c6caa7549945482718d71d.png)
这样执行的时候，`pgkayd.aq`就会作为参数执行了。
给`CreateFileA`和`virtualalloc`下断点，运行
![image-20240808153724677](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1c168b18853e937bc8a47ff5588f5987109cc4ab.png)
这次成功了。
### 解码shellcode
再次运行F9，就断在`VirtualAlloc`了。Ctrl+F9运行到函数结尾处，该值是`VirtualAlloc`的返回值，即分配内存的基地址。跳转过去到内存窗口：
![image-20240808154030037](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-d30fce4225f6827fc123ac9a7bccc5578bcc61b9.png)
在第一个字节处设置硬件断点
![image-20240808154121650](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-60aaf3dbda0f336aa6aa74589f4a7f0330a4c7b0.png)
F9 之后再Ctrl+F9，直到所有缓存区都被填满：
![image-20240808154210246](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-58bae3fdd992c81737ace0bc9a48dc98e69c1e15.png)
然而这部分缓存由DB A3开头，不是熟知的4D5A，也不是shellcode常见的标识。推测该处不是我们要的有效负荷。也可以通过选中第一个字节，右键点击在反汇编窗口中显示，这样你可以看到与窗口对其的第一个命令是红色的问号。这表明该处是不正常的。
我们回到IDA中查看该处代码：
![image-20240809093258842](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f4d240fa6eb4126cf8006826b311f06cdbad7875.png)
在执行恶意代码前，还对填充的数据做了一个异或操作。那么可以在后面执行处打一个断点，然后运行，直到全部解密完成。
最后能得到：
![image-20240809093525718](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b9c34bfbdb3f0c38ad30dd81c7911d4729fddc51.png)
一块，E9 97 的内存区，看反汇编窗口也成功识别出了第一条指令。接着就选中所有的数据dump出来。得到dump.bin
手动分析shellcode
-------------
shellcode通常是一段二进制数据，不同于PE文件，无法使用IDA正常的去分析它。我们可以通过一个叫做Blobrunner的工具，将shellcode附加到这个工具上，再使用Xdbg附加该进程。
### Ghidra静态分析
使用Ghidra分析的时候我们需要自己选择架构：
![image-20240809100348045](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-08887630f068211f70ce5e0ac6fa3e27dc6aa6cc.png)
通常只要是 X86、32、little就可以了。
Ghidra分析完，从基地址的E9跳转过去可以看到如下：
![image-20240809100833290](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b05d5a12968b87bcf0e3850be6151b3cce1b0143.png)
调用一个函数 其中传入参数是一个十六进制值，该值类似于API哈希，我们可以用Google搜索验证这一点（该恶意软件也正是使用NSIS打包的）： ![image-20240809101153852](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-df023a9703151f9961dc711b792166373f556071.png)
查看该API哈希函数，不同于使用0xD的API哈希函数。这里也有一个思路就是使用上图大佬给的hash算法来还原所有的API哈希。
![image-20240809101342514](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-020d88c00cb67c29b5e335a4094ac88e3a2dc071.png)
当然这里学习如何解密一个未知的API哈希函数。
### x32dbg调试API哈希
#### Blobrunner工具
Blorrunner是一个能够加载shellcode并提供可以使用调试器附加的进程的工具。这里我们从github上下载下来，和shellcode放在同一文件夹内，打开cmd 。 运行 `blobrunner.exe dump.bin`
![image-20240809101955558](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-d6debd9b820a2af7574d1a04362da5b37d23a240.png)
base:0x003e0000
x32dbg打开 附加进程：
![image-20240809102044545](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8ee7ab4cca7f2f9d413cc7e2eed26efd7c7d1e82.png)
#### 设置断点
首先在基地址上 下一个断点，再在API哈希函数上下一个断点...