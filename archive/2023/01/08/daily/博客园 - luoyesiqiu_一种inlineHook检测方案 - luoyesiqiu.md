---
title: 一种inlineHook检测方案 - luoyesiqiu
url: https://www.cnblogs.com/luoyesiqiu/p/inlineHookDetect.html
source: 博客园 - luoyesiqiu
date: 2023-01-08
fetch_date: 2025-10-04T03:19:32.672611
---

# 一种inlineHook检测方案 - luoyesiqiu

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

## Loading

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/luoyesiqiu/)

# [luoyesiqiu](https://www.cnblogs.com/luoyesiqiu)

## 好记性不如烂笔头

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/luoyesiqiu/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)

* [管理](https://i.cnblogs.com/)

# [一种inlineHook检测方案](https://www.cnblogs.com/luoyesiqiu/p/inlineHookDetect.html "发布于 2023-01-07 15:11")

inlinehook是修改内存中的机器码来实现hook的方式

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

posted @
2023-01-07 15:11
[luoyesiqiu](https://www.cnblogs.com/luoyesiqiu)
阅读(1305)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)