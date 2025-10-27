---
title: 利用LLVM解释器执行你的代码
url: https://forum.butian.net/share/3743
source: 奇安信攻防社区
date: 2024-09-20
fetch_date: 2025-10-06T18:20:00.750948
---

# 利用LLVM解释器执行你的代码

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

### 利用LLVM解释器执行你的代码

* [渗透测试](https://forum.butian.net/topic/47)

llvm工具链中的lli.exe可以执行中间bitcode文件，通过这一方法在目标环境执行代码，能够绕过Windows Defender检测。

前言
==
撰写这一篇文章的起因是看到CrowdStrike最近的一篇[博客](https://www.crowdstrike.com/blog/malicious-inauthentic-falcon-crash-reporter-installer-ciro-malware/)， 文章中介绍一个MSI样本将Mythic的agent编译为LLVM的IR bitcode，在目标上通过LLVM解释器执行。
这种技术似曾相识，.NET代码可以转换为公共中间语言(CIL)在内存中编译执行，Python代码通过解释器执行，JAVA代码通过JVM虚拟机执行，如今C代码也可以转换为LLVM IR语言解释执行。
使用方法
====
llvm与clang
----------
LLVM是一套编译器基础设施项目，以C++写成，包含一系列模块化的编译器组件和工具链，用来开发编译器前端和后端。
其中Clang是基于LLVM开发的一个编译器前端工具，用来解析C/C++代码，将其转换为LLVM中间语言IR，最后通过不同的编译器后端编译成可执行代码。差不多过程就是下面这样
C/C++代码 --&gt;LLVM IR --&gt; MachineCode(x86、ARM...)
clang.exe和gcc.exe差不多，Visual Studio则是cl.exe
clang工具
-------
clang工具可以自行下载llvm的源码进行编译，也可以通过https://github.com/llvm/llvm-project/releases 下载，注意要下载clang+llvm-18.1.8-x86\\_64-pc-windows-msvc.tar.xz，这里面才包含可以执行LLVM IR bitcode的工具lli.exe。
首先打开x64 Native Tools Command Prompt for VS 2019 并切换到源代码目录
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-5f9c7ec67e7d63b1eb20406a4e38ee10cadee644.png)
以简单的hellloworld代码为例，使用clang正常编译cpp文件为可执行文件:
(clang-cl是clang适配MSVC的版本)
```php
clang-cl helloworld.cpp -o hello.exe
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1aba9cbdd8ba7bdeeecaa6f336949956a8b23405.png)
bitcode生成与使用
------------
使用clang编译cpp文件为LLVM IR bitcode
```php
clang -emit-llvm -c helloworld.cpp -o helloworld.bc
```
bitcode文件是这样的：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-a1ec0ed35f97fe64ff0bd6af8be6e762ea3a5d6e.png)
那么我们使用工具中的llc.exe来执行bitcode文件:
```php
llc helloworld.bc
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-da91763ba39fc691f6fd75dfdc40e7e64e4d7ecb.png)
可以看到bitcode文件被成功执行了，而且将lli.exe以及bc文件放到另一个主机可以成功执行。
其实LLVM IR还有另外一种可读形态ll，通过下面的方式即可获得，但是这样会暴露源码中的信息，所以上述博客中的技术才会使用bitcode。
```php
clang -emit-llvm -S helloworld.cpp -o helloworld.ll
```
可读形态ll文件内容如下所示
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-07c62282d45b91af874746110942fad08b168146.png)
免杀效果
====
执行弹计算器shellcode
---------------
既然可以能够执行helloworld，为什么不来加载shellcode呢
通过msf生成一段弹计算器的shellcode，使用CreateThread加载执行
```php
clang-cl shellcode\_calc.cpp -o shellcode\_calc.exe
shellcode\_calc.exe
```
在关闭Windows Defender的情况下可以正常运行
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b76e9011757d23599a9c9f1c6006e3ba9ecc35c9.png)
但是一旦放到开启Windows Defender的环境中，就会被检测删除
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7ef398a3e123dd864b6cbfba207a62d3f0a1b990.png)
如果使用lli.exe + shellcode\\_calc.bc呢，则可以成功在Windows Defender下执行这段shellcode
```php
clang -emit-llvm -c shellcode\_calc.cpp -o shellcode\_calc.bc
lli.exe shellcode\_calc.bc
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-593344d6eba852bf522bad950db94a299c450ddd.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4050d994af643fc314d10fb4b6185a303074787e.png)
执行回连shellcode
-------------
让我们使用msf生成一个reverse\\_tcp，使用lli工具在开启了Windows Defender的环境下执行，同样可以看到成功回连。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-762d4803190bd592abc71f298d2511a1ad590f8a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-3867e9d06920183252a470415acd320030b770c1.png)
原理分析
====
那么lli文件是如何加载执行我们的代码？让我们使用x64dbg对lli文件进行调试，并执行之前弹计算器的bitcode，同时在NtCreateThreadEx下断点(为什么自在这下断点？后面会说)
当在NtCreateThreadEx断下时
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-76fb2d905929488bc87f7575f0c062249f7dd058.png)
持续回溯，当我们回到lli.exe的代码空间时，会看到这段类似于shellcode\\_calc.cpp中功能的汇编代码。不难看出，这里调用的是KernelBase中的CreateThread，而其他函数也是调用的KernelBase的API，所以在NtCreateThreadEx下断点。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-58c1874c2c8b5a0455345913420d106ac6180a65.png)
而这段代码的地址为245B0DA0000，在内存布局中可以看到这应该是属于堆内存，并且由执行权限。汇编代码中的245B0DB0000则是用于弹计算器的shellcode，该空间只读。245B0DC0000也是同样的shellcode，而这个地址空间则有通过VirtualAlloc函数分配的RWX权限。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-016be53a7bc408371a21be8c25a638720f56fc7a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f09c1674498ff7d09079abd22e5dd2454456a5fe.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f17ed28c1c66189ba5863fff1a0035148c2607ac.png)
查看此时的堆栈，返回到lli的代码7FF61F44D42E，而且还返回到ntdll.RtlFreeHeap。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-66f1df68a3e6521f9ac454d25e330ce41d8dff72.png)
重新运行，在7FF61F44D42C处下断点（在执行shellcode\\_calc汇编代码之前）
通过此时的堆栈，能知道是使用RtlAllocateHeap函数分配的内存。在之前调用了memmove函数将bitcode转成的本机代码移动到rax指向的地址空间，再call进去。
至于lli.exe如何将bitcode转成的本机代码，则涉及到编译器的范畴了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7457b6f5a564c711a0c584802ae9f1dfb85fcdbc.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9f0cc2a924ebf624d574c3c78b1f2bb54c759e6c.png)
思考
==
1. lli.exe文件大小为24M，放到目标环境比较明显。因此上述CrowdStrike博客中描述的那样，将该文件放到MSI安装程序中，可以降低可疑性。或者也能自己修改lli.exe的源代码，去除多余功能代码，编译一个较小的版本。
2. lli.exe使用RtlAllocateHeap函数在自身进程空间中分配内存，然后call，并且代码中也没有直接调用Kernel32中的函数，而是调用的KernelBase中的函数。 那么lli.exe文件有数字签名是不是更安全了？很遗憾，llvm github发布的版本没有数字签名(也没有必要花钱去签名，毕竟llvm的版本更新太快了)。而VS2019、VS2022提供的llvm工具链中的工具倒是有微软的数字签名，但是却没有lli工具。其他提供llvm工具链的工具管理包譬如MSYS2、Anaconda，也没有lli.exe或带数字签名。
3. Rust语言也是基于llvm的，是否也具备这样的特性？
4. 对于这种技术的防范，则需要监控是否存在可疑的lli工具被执行。

* 发表于 2024-09-19 09:00:00
* 阅读 ( 4868 )
* 分类：[安全工具](https://forum.butian.net/community/Sec_tools)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![br1ght](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/34389)

[br1ght](https://forum.butian.net/people/34389)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![br1ght](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---