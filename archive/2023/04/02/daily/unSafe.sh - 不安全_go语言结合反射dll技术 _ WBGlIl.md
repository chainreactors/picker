---
title: go语言结合反射dll技术 | WBGlIl
url: https://buaq.net/go-156421.html
source: unSafe.sh - 不安全
date: 2023-04-02
fetch_date: 2025-10-04T11:26:36.812240
---

# go语言结合反射dll技术 | WBGlIl

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

go语言结合反射dll技术 | WBGlIl

*2023-4-1 10:50:29
Author: [wbglil.github.io(查看原文)](/jump-156421.htm)
阅读量:103
收藏*

---

* [关于](https://wbglil.github.io/about/)
* [标签](https://wbglil.github.io/tags/)
* [分类](https://wbglil.github.io/categories/)
* [归档](https://wbglil.github.io/archives/)

发表于

2020-03-15

没有找到适合的图片

好久没写博客了随便写写

反射dll技术什么的已经出现了很久了原理什么的自己谷歌看看吧，懒得写
这里利用的就是cgo（golang 和 C 语言相互调）把go和c的反射dll核心代码结合了一下

这个模板可以很方便的把go代码编译成反射dll文件

直接上关键文件代码

dllmain.c

```
#include "dllmain.h"
#include

DWORD WINAPI MyThreadFunction() {
OnProcessAttach();
    return 0;
}

BOOL WINAPI DllMain(
    HINSTANCE hinstDLL,  // handle to DLL module
    DWORD fdwReason,     // reason for calling function
    LPVOID lpReserved)   // reserved
{
    switch (_fdwReason) {
    case DLL_PROCESS_ATTACH:
        {
        OnProcessAttach();
        MyThreadFunction();
        }
        break;
    case DLL_PROCESS_DETACH:
        // Perform any necessary cleanup.
        break;
    case DLL_THREAD_DETACH:
        // Do thread-specific cleanup.
        break;
    case DLL_THREAD_ATTACH:
        // Do thread-specific initialization.
        break;
    }
    return TRUE; // Successful.
}
```

main.go

```
package main

import "C"

import (
    "syscall"
    "unsafe"
)

func IntPtr(n int) uintptr {
    return uintptr(n)
}
func StrPtr(s string) uintptr {
    return uintptr(unsafe.Pointer(syscall.StringToUTF16Ptr(s)))
}
func MessageBox(title, text string) {
    user32 := syscall.NewLazyDLL("user32.dll")
    MessageBoxW := user32.NewProc("MessageBoxW")
    MessageBoxW.Call(IntPtr(0), StrPtr(text), StrPtr(title), IntPtr(0))
}

//export OnProcessAttach
func OnProcessAttach() {
    MessageBox("OnProcessAttach","OnProcessAttach")
}
//export test
func test() {
    MessageBox("test","test")
}

func main()  {

}
```

其他文件去github看吧

支持编译为x86和x64
x64.bat编译为x64 dll
x86.bat编译为x86 dll

## 测试

![image.png](https://i.loli.net/2020/03/15/LaNMJBwEpyzYjch.png)

github地址:<https://github.com/WBGlIl/go-ReflectiveDLL>

想深入了解原理的可以自己去研究一下其中使用的一些技术比如反射dll cgo什么的

文章来源: https://wbglil.github.io/2020/03/15/go%E8%AF%AD%E8%A8%80%E7%BB%93%E5%90%88%E5%8F%8D%E5%B0%84dll%E6%8A%80%E6%9C%AF/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)