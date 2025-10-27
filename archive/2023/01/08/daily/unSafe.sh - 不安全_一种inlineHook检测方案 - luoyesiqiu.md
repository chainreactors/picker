---
title: 一种inlineHook检测方案 - luoyesiqiu
url: https://buaq.net/go-144561.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:49.308298
---

# 一种inlineHook检测方案 - luoyesiqiu

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

![](https://8aqnet.cdn.bcebos.com/06c7fdbec75e70d96e2b757b51c7ce65.jpg)

一种inlineHook检测方案 - luoyesiqiu

定义inlinehook是修改内存中的机器码来实现hook的方式我们用frida查看一个函数hook之前和hook之后的机器码，这里以open函数为例：let bytes\_count = 32
*2023-1-7 15:11:0
Author: [www.cnblogs.com(查看原文)](/jump-144561.htm)
阅读量:43
收藏*

---

## 定义

inlinehook是修改内存中的机器码来实现hook的方式

我们用frida查看一个函数hook之前和hook之后的机器码，这里以open函数为例：

```
let bytes_count = 32
let address = Module.getExportByName("libc.so","open")

let before = ptr(address)
console.log("")
console.log("[*] before hook: ")
console.log(hexdump(before, {
    offset: 0,
    length: bytes_count,
    header: true,
    ansi: true
  }));

let isOutput = false

Interceptor.attach(address, {
	onEnter:function(args){
        if(isOutput) return;
		let after = ptr(address)
        console.log("")
		console.log("[*] after hook: ")
        console.log(hexdump(after, {
            offset: 0,
            length: bytes_count,
            header: true,
            ansi: true
        }))
        isOutput = true
	},
	onLeave:function(retv){
	}
});
```

hook之前：

![](https://img2023.cnblogs.com/blog/1456902/202301/1456902-20230107151004770-173554130.jpg)

hook之后：

![](https://img2023.cnblogs.com/blog/1456902/202301/1456902-20230107150949425-396068488.jpg)

可见，hook之后，函数开头的字节被修改了

## 思考

inlinehook只修改了内存中的机器码，而内存中的机器码是从文件加载而来的，所以我们可以将函数在内存中字节和本地对应的字节进行比较，如果不一致，那么可以认为内存中的字节被修改了，即被inlinehook了。

## 实现

```
#ifdef __LP64__
    const char *lib_path = "/system/lib64/libc.so";
#else
    const char *lib_path = "/system/lib/libc.so";
#endif
#define CMP_COUNT 8
    const char *sym_name = "open";

    struct local_dlfcn_handle *handle = static_cast<local_dlfcn_handle *>(local_dlopen(lib_path));

    off_t offset = local_dlsym(handle,sym_name);

    FILE *fp = fopen(lib_path,"rb");
    char file_bytes[CMP_COUNT] = {0};
    if(fp != NULL){
        fseek(fp,offset,SEEK_SET);
        fread(file_bytes,1,CMP_COUNT,fp);
        fclose(fp);
    }

    void *dl_handle = dlopen(lib_path,RTLD_NOW);
    void *sym = dlsym(dl_handle,sym_name);

    int is_hook = memcmp(file_bytes,sym,CMP_COUNT) != 0;

    local_dlclose(handle);
    dlclose(dl_handle);

    char text[128] = {0};
    snprintf(text,128,"Function \"%s\" is Hook: %s",sym_name,is_hook ? "true" : "false");
```

这里`local_`开头的函数是读取本地符号偏移库，库代码：<https://github.com/luoyesiqiu/local_dlfcn>

用frida hook测试demo:`frida-trace -U -i "open" -f com.luoye.localdlfcn`

![](https://img2023.cnblogs.com/blog/1456902/202301/1456902-20230107151020057-5317422.png)

文章来源: https://www.cnblogs.com/luoyesiqiu/p/inlineHookDetect.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)