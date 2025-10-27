---
title: IOS逆向(二)-绕过某租车app越狱和代理检测
url: https://zgao.top/ios%e9%80%86%e5%90%91%e4%ba%8c-%e7%bb%95%e8%bf%87%e6%9f%90%e7%a7%9f%e8%bd%a6app%e8%b6%8a%e7%8b%b1%e5%92%8c%e4%bb%a3%e7%90%86%e6%a3%80%e6%b5%8b/
source: Zgao's blog
date: 2023-05-16
fetch_date: 2025-10-04T11:36:52.894629
---

# IOS逆向(二)-绕过某租车app越狱和代理检测

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# IOS逆向(二)-绕过某租车app越狱和代理检测

* [首页](https://zgao.top)
* [IOS逆向(二)-绕过某租车app越狱和代理检测](https://zgao.top:443/ios%E9%80%86%E5%90%91%E4%BA%8C-%E7%BB%95%E8%BF%87%E6%9F%90%E7%A7%9F%E8%BD%A6app%E8%B6%8A%E7%8B%B1%E5%92%8C%E4%BB%A3%E7%90%86%E6%A3%80%E6%B5%8B/)

[5月 15, 2023](https://zgao.top/2023/05/)

### IOS逆向(二)-绕过某租车app越狱和代理检测

作者 [Zgao](https://zgao.top/author/zgao/)
在[[逆向](https://zgao.top/category/%E9%80%86%E5%90%91/)](https://zgao.top/ios%E9%80%86%E5%90%91%E4%BA%8C-%E7%BB%95%E8%BF%87%E6%9F%90%E7%A7%9F%E8%BD%A6app%E8%B6%8A%E7%8B%B1%E5%92%8C%E4%BB%A3%E7%90%86%E6%A3%80%E6%B5%8B/)

![](https://zgao.top/wp-content/uploads/2023/05/IMG_072D6FF7A8AC-1.jpeg)

因为日常使用shadowrocket，所以每次打开某租车app都会提示检测到手机开了代理，并且在越狱设备上打开还会直接闪退。如何绕过app的代理和越狱检测呢？

文章目录

[ ]

* [难度](#%E9%9A%BE%E5%BA%A6 "难度")
* [工具环境](#%E5%B7%A5%E5%85%B7%E7%8E%AF%E5%A2%83 "工具环境")
* [IDA逆向分析](#IDA%E9%80%86%E5%90%91%E5%88%86%E6%9E%90 "IDA逆向分析")
* [frida-trace hook越狱函数](#frida-trace_hook%E8%B6%8A%E7%8B%B1%E5%87%BD%E6%95%B0 "frida-trace hook越狱函数")
* [定位程序退出的堆栈](#%E5%AE%9A%E4%BD%8D%E7%A8%8B%E5%BA%8F%E9%80%80%E5%87%BA%E7%9A%84%E5%A0%86%E6%A0%88 "定位程序退出的堆栈")
* [IDA分析程序退出的堆栈](#IDA%E5%88%86%E6%9E%90%E7%A8%8B%E5%BA%8F%E9%80%80%E5%87%BA%E7%9A%84%E5%A0%86%E6%A0%88 "IDA分析程序退出的堆栈")
* [frida 踩坑](#frida_%E8%B8%A9%E5%9D%91 "frida 踩坑")
  + [为什么用frida给的偏移地址hook不成功？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E7%94%A8frida%E7%BB%99%E7%9A%84%E5%81%8F%E7%A7%BB%E5%9C%B0%E5%9D%80hook%E4%B8%8D%E6%88%90%E5%8A%9F%EF%BC%9F "为什么用frida给的偏移地址hook不成功？")
* [交叉应用定位外层函数调用](#%E4%BA%A4%E5%8F%89%E5%BA%94%E7%94%A8%E5%AE%9A%E4%BD%8D%E5%A4%96%E5%B1%82%E5%87%BD%E6%95%B0%E8%B0%83%E7%94%A8 "交叉应用定位外层函数调用")
* [绕过越狱检测](#%E7%BB%95%E8%BF%87%E8%B6%8A%E7%8B%B1%E6%A3%80%E6%B5%8B "绕过越狱检测")
* [效果演示](#%E6%95%88%E6%9E%9C%E6%BC%94%E7%A4%BA "效果演示")

## 难度

★★☆☆☆

## 工具环境

* 越狱IOS 14.4
* frida-ios-dump
* frida
* frida-trace
* IDA 7.7

## IDA逆向分析

通过砸壳得到app的maco文件，直接扔进ida里面分析。既然app做了越狱检测，那么先直接搜索 jail 相关的函数名。

![](https://zgao.top/wp-content/uploads/2023/05/image-12-1024x645.png)

确实存在越狱检测的函数，通过检查一些特定的文件和目录是否存在来判断设备是否已经越狱。”Cydia.app”是一个在越狱设备上常见的应用商店，而”/bin/bash”和”/usr/sbin/sshd”则表示设备已经获得了全面的文件系统访问权限。

![](https://zgao.top/wp-content/uploads/2023/05/image-13-1024x639.png)

检测的过程是通过NSFileManager的fileExistsAtPath:方法来实现的。如果检测到任何一个文件或目录存在，函数就会返回1，表示设备已经越狱。如果所有的文件和目录都不存在，函数就会返回0，表示设备没有越狱。

## frida-trace hook越狱函数

看到这里大家可能会想到，那我直接用frida来hook越狱检测函数 `+[_priv_NBSProbe isJailBreak]` 不就可以了？

一开始我也是这样想的，所以直接用frida-trace进行hook。

```
frida-trace -U -f  com.szzc.szzc -m "+[_priv_NBSProbe isJailBreak]"
```

修改hook代码如下，替换函数返回值为0绕过检测。

```
{
  onEnter(log, args, state) {
    log(`进入 +[_priv_NBSProbe isJailBreak] 检测函数`);
    log(args[0]);
  },
  onLeave(log, retval, state) {
    log('退出 +[_priv_NBSProbe isJailBreak] 检测函数');
    retval.replace(0);
  }
}
```

![](https://zgao.top/wp-content/uploads/2023/05/image-14-1024x389.png)

程序在进入该函数之前，已经退出了。说明是app还有其他的检测函数在该函数之前先执行并退出了。

## 定位程序退出的堆栈

如何定位程序退出时的堆栈？可以通过frida-trace来hook系统的exit或abort函数。

```
frida-trace -U -i "exit" -i "abort" -f com.szzc.szzc
```

并添加exit的js代码如下：

```
{
  onEnter(log, args, state) {
    log(`exit(status=${args[0]})`);
    log('exit() called from:\n' +
    Thread.backtrace(this.context, Backtracer.ACCURATE)
    .map(DebugSymbol.fromAddress).join('\n') + '\n');
  },
  onLeave(log, retval, state) {
  }
}
```

![](https://zgao.top/wp-content/uploads/2023/05/image-15-1024x609.png)

frida打印程序退出时的堆栈，可以看到是在0x275d4b8的偏移地址执行退出的。

## IDA分析程序退出的堆栈

这里解释一下frida打印的三个地址的含义。

```
0x1047994b8 WCCApp!0x275d4b8 (0x10275d4b8)
```

* 0x1047994b8 是程序在内存中实际的内存地址，因为存在地址空间布局随机化（ASLR），运行看到的地址都是相对于程序的基址的偏移，这个基址在每次运行时都会改变。
* 0x275d4b8 是该函数相对于基址的偏移地址
* 0x10275d4b8 是该函数在IDA中的地址，因为IDA的默认基址为0x100000000，0x10275d4b8 = 0x100000000 + 0x275d4b8

在IDA中来到0x10275d4b8的地址。

![](https://zgao.top/wp-content/uploads/2023/05/image-16-1024x618.png)

发现没有并不是判断异常的代码逻辑，来到堆栈的上一层0x100007464。

![](https://zgao.top/wp-content/uploads/2023/05/企业微信截图_28f672a4-fc69-4fab-a73c-155fab957465-1024x635.png)

这里有几十个判断逻辑，可以看到越狱检测的和代理检测都有，应该是所有的检测都放到了一起，依次检测判断。从字符串可以推断是app集成了爱加密的sdk。

## frida 踩坑

那么是否直接hook 0x7464 地址就行呢？

```
frida -U -l wcc.js -f com.szzc.szzc
```

wcc.js 代码如下：

```
var baseAddr = Module.findBaseAddress('WCCApp');
var offsetAddr = 0x7464 // 0x100007464
var targetAddr = baseAddr.add(offsetAddr);

console.log("WCCApp 基址: " + baseAddr);
console.log("目标函数地址： " + targetAddr);

Interceptor.attach(targetAddr, {
    onEnter: function(args) {
        console.log("函数hook成功！");
        console.log(' called from:\n' +
        Thread.backtrace(this.context, Backtracer.ACCURATE)
        .map(DebugSymbol.fromAddress).join('\n') + '\n');
        this.skip = true;
    },
    onLeave: function(retval) {
        console.log("Function execution finished.");
    }
});
```

![](https://zgao.top/wp-content/uploads/2023/05/image-17-1024x563.png)

这里frida执行没有打印出堆栈信息是为什么呢？

![](https://zgao.top/wp-content/uploads/2023/05/image-18-1024x557.png)

frida hook函数需要对函数名的偏移地址然后在基址上添加，而不是函数内部的偏移地址。

![](https://zgao.top/wp-content/uploads/2023/05/image-19-1024x818.png)

### 为什么用frida给的偏移地址hook不成功？

查看函数的交叉应用。

![](https://zgao.top/wp-content/uploads/2023/05/image-20-1024x377.png)
![](https://zgao.top/wp-content/uploads/2023/05/image-21-1024x391.png)

这里我推测是上层函数中调用里面用了异步方法导致的。

## 交叉应用定位外层函数调用

![](https://zgao.top/wp-content/uploads/2023/05/image-22-1024x597.png)

再往上查找一层，IDA能识别出这是一个objc的方法。

![](https://zgao.top/wp-content/uploads/2023/05/image-23-1024x649.png)

## 绕过越狱检测

到这一步思路就很清晰了，直接用frida 来hook这个函数然后把把sub\_100007008替换成一个空函数就行。重新写一个frida脚本为wcc\_jail.js

```
var baseAddr = Module.findBaseAddress('WCCApp');
console.log("WCCApp base address: " + baseAddr);
//0x7008是sub_100007008越狱检测函数的偏移地址
var targetFunctionAddr = baseAddr.add(0x7008);
console.log("Target function address: " + targetFunctionAddr);

const targetFunction = new NativeFunction(targetFunctionAddr, 'void', []);

// 把sub_100007008替换成一个空函数
Interceptor.replace(targetFunctionAddr, new NativeCallback(function () {
    console.log("Skip the execution of sub_100007008");
}, 'void', []));
//0x8A24是-[RootViewController viewDidLoad]的偏移地址
const targetFunctionAddrRootVC = baseAddr.add(0x8A24);

Interceptor.attach(targetFunctionAddrRootVC, {
    onEnter: function (args) {
        console.log('Entering -RootViewController viewDidLoad!');
    },
    onLeave: function (retval) {
        console.log('Leaving -RootViewController viewDidLoad!');
    }
});
```

执行命令如下：

```
frida -U -l wcc_jail.js -f com.szzc.szzc
```

![](https://zgao.top/wp-content/uploads/2023/05/image-24-1024x551.png)

## 效果演示

[](https://zgao.top/wp-content/uploads/2023/05/ec86f5983fc1f3203ebdf04cfb6ccebf_0_1684153985.mp4)

Post Views: 3,395

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/ios%E9%80%86%E5%90%91%E4%BA%8C-%E7%BB%95%E8%BF%87%E6%9F%90%E7%A7%9F%E8%BD%A6app%E8%B6%8A%E7%8B%B1%E5%92%8C%E4%BB%A3%E7%90%86%E6%A3%80%E6%B5%8B/#respond)

Δ

版权©2020 Author By : Zgao