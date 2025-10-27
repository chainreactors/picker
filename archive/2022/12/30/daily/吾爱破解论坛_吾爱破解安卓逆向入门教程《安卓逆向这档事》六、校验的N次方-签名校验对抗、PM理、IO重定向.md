---
title: 吾爱破解安卓逆向入门教程《安卓逆向这档事》六、校验的N次方-签名校验对抗、PM理、IO重定向
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651138693&idx=1&sn=a09896ce9c1aa5e7194600ff7ca011e9&chksm=bd50bad18a2733c7c536438f5181eb3d73a57c0349e010fda23d7973cb0ebf272f15b82be56a&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2022-12-30
fetch_date: 2025-10-04T02:45:03.265701
---

# 吾爱破解安卓逆向入门教程《安卓逆向这档事》六、校验的N次方-签名校验对抗、PM理、IO重定向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJLTHyibGJLZmrmCLsFnfuK7iagIJqcTB7ibTDTWrkJl4ibuo99A3TA4jW6CAvBzPhypIM8oZxeYxrK8w/0?wx_fmt=jpeg)

# 吾爱破解安卓逆向入门教程《安卓逆向这档事》六、校验的N次方-签名校验对抗、PM理、IO重定向

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：正己**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/LFPriaSjBUZJLTHyibGJLZmrmCLsFnfuK7icg3oiabicy5ftdG5ex7okzic9eO4Y9dln2kfpJ1qibcESbI2da938Pf3kA/640?wx_fmt=gif)

# 一、课程目标

---

1.了解APK文件签名
2.了解APK常见校验及校验对抗方法
3.了解PM代理和IO重定向
4.smali语法之赋值

# 二、工具

---

1.教程Demo(更新)
2.MT管理器/NP管理器
3.雷电模拟器
4.Jadx-gui(第三课课件里有)
5.算法助手(第四课课件里有)

# 三、课程内容

---

## 1.什么是校验

是开发者在数据传送时采用的一种校正数据的一种方式
常见的校验有:签名校验(最常见)、dexcrc校验、apk完整性校验、路径文件校验等

## 2.什么是APK签名

通过对 Apk 进行签名，开发者可以证明对 Apk 的所有权和控制权，可用于安装和更新其应用。而在 Android 设备上的安装 Apk ，如果是一个没有被签名的 Apk，则会被拒绝安装。在安装 Apk 的时候，软件包管理器也会验证 Apk 是否已经被正确签名，并且通过签名证书和数据摘要验证是否合法没有被篡改。只有确认安全无篡改的情况下，才允许安装在设备上。

简单来说，APK 的签名主要作用有两个：

1. 证明 APK 的所有者。
2. 允许 Android 市场和设备校验 APK 的正确性。

Android 目前支持以下四种应用签名方案：
v1 方案：基于 JAR 签名。
v2 方案：APK 签名方案 v2（在 Android 7.0 中引入）
v3 方案：APK 签名方案 v3（在 Android 9 中引入）
v4 方案：APK 签名方案 v4（在 Android 11 中引入）

V1 签名的机制主要就在 META-INF 目录下的三个文件，MANIFEST.MF，ANDROID.SF，ANDROID.RSA，他们都是 V1 签名的产物。
（1）MANIFEST.MF：这是摘要文件。程序遍历Apk包中的所有文件(entry)，对非文件夹非签名文件的文件，逐个用SHA1(安全哈希算法)生成摘要信息，再用Base64进行编码。如果你改变了apk包中的文件，那么在apk安装校验时，改变后的文件摘要信息与MANIFEST.MF的检验信息不同，于是程序就不能成功安装。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJLTHyibGJLZmrmCLsFnfuK7qndfQf342qDJhKMdwiapL1LP8cCv8TnNgFtg9Jj5ZtqtOE3Vh6G3iboQ/640?wx_fmt=png)

（2）c.SF：这是对摘要的签名文件。对前一步生成的MANIFEST.MF，使用SHA1-RSA算法，用开发者的私钥进行签名。在安装时只能使用公钥才能解密它。解密之后，将它与未加密的摘要信息（即，MANIFEST.MF文件）进行对比，如果相符，则表明内容没有被异常修改。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJLTHyibGJLZmrmCLsFnfuK7GjG7UhLd4ibc2r3scichuKwqmAdsfAFcTlQ2PnmcH6rFiazia29SauEMTA/640?wx_fmt=png)
（3）ANDROID.RSA文件中保存了公钥、所采用的加密算法等信息。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJLTHyibGJLZmrmCLsFnfuK7hb3iayicoHt5vjrONTHFYQ3yKSPqFc6viaVxnlTwbmrfVcYtglC3r79hw/640?wx_fmt=png)
在某些情况下，直接对apk进行v1签名可以绕过apk的签名校验

v2方案会将 APK 文件视为 blob，并对整个文件进行签名检查。对 APK 进行的任何修改（包括对 ZIP 元数据进行的修改）都会使 APK 签名作废。这种形式的 APK 验证不仅速度要快得多，而且能够发现更多种未经授权的修改。

## 3.什么是签名校验

如何判断是否有签名校验？
不做任何修改，直接签名安装，应用闪退则说明大概率有签名校验

一般来说，普通的签名校验会导致软件的闪退，黑屏，卡启动页等
当然，以上都算是比较好的，有一些比较狠的作者，则会直接rm -rf /，把基带都格掉的一键变砖。

```
 复制代码 隐藏代码
kill/killProcess-----kill/KillProcess()可以杀死当前应用活动的进程，这一操作将会把所有该进程内的资源（包括线程全部清理掉）.当然，由于ActivityManager时刻监听着进程，一旦发现进程被非正常Kill，它将会试图去重启这个进程。这就是为什么，有时候当我们试图这样去结束掉应用时，发现它又自动重新启动的原因.

system.exit-----杀死了整个进程，这时候活动所占的资源也会被释放。

finish----------仅仅针对Activity，当调用finish()时，只是将活动推向后台，并没有立即释放内存，活动的资源并没有被清理
```

在我个人见过最恶心的签名校验中，当属三角校验(低调大佬教的)最烦人。
所谓三角校验，就是so检测dex，动态加载的dex(在软件运行时会解压释放一段dex文件，检测完后就删除)检测so，dex检测动态加载的dex

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJLTHyibGJLZmrmCLsFnfuK7ZRz6HrPj7P6ia6NQWibfUadzgSS6PO2sTjRgs4eMv32wCCvtXlFGk40Q/640?wx_fmt=png)

普通获取签名校验代码：

```
 复制代码 隐藏代码
private boolean SignCheck() {
    String trueSignMD5 = "d0add9987c7c84aeb7198c3ff26ca152";
    String nowSignMD5 = "";
    try {
        // 得到签名的MD5
        PackageInfo packageInfo = getPackageManager().getPackageInfo(getPackageName(),PackageManager.GET_SIGNATURES);
        Signature[] signs = packageInfo.signatures;
        String signBase64 = Base64Util.encodeToString(signs[0].toByteArray());
        nowSignMD5 = MD5Utils.MD5(signBase64);
    } catch (PackageManager.NameNotFoundException e) {
        e.printStackTrace();
    }
    return trueSignMD5.equals(nowSignMD5);
}
```

系统将应用的签名信息封装在 PackageInfo 中，调用 PackageManager 的 getPackageInfo(String packageName, int flags) 即可获取指定包名的签名信息

## 4.签名校验对抗

方法一:核心破解插件，不签名安装应用
方法二:一键过签名工具，例如MT、NP、ARMPro、CNFIX、Modex的去除签名校验功能
方法三:具体分析签名校验逻辑(手撕签名校验)
方法四:io重定向--VA&SVC：ptrace+seccomp
SVC的TraceHook沙箱的实现&无痕Hook实现思路
方法五:去作者家严刑拷打拿到.jks文件和密码

## 5.手动实现PM代理

### 1.什么是PMS

思路源自：Android中Hook 应用签名方法

PackageManagerService（简称PMS），是Android系统核心服务之一，处理包管理相关的工作，常见的比如安装、卸载应用等。

### 2.实现方法以及原理解析

HOOK PMS代码:

```
 复制代码 隐藏代码
package com.zj.hookpms;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

import android.content.Context;
import android.content.pm.PackageManager;
import android.util.Log;

public class ServiceManagerWraper {

    public final static String ZJ = "ZJ595";

    public static void hookPMS(Context context, String signed, String appPkgName, int hashCode) {
        try {
            // 获取全局的ActivityThread对象
            Class<?> activityThreadClass = Class.forName("android.app.ActivityThread");
            Method currentActivityThreadMethod =
                    activityThreadClass.getDeclaredMethod("currentActivityThread");
            Object currentActivityThread = currentActivityThreadMethod.invoke(null);
            // 获取ActivityThread里面原始的sPackageManager
            Field sPackageManagerField = activityThreadClass.getDeclaredField("sPackageManager");
            sPackageManagerField.setAccessible(true);
            Object sPackageManager = sPackageManagerField.get(currentActivityThread);
            // 准备好代理对象, 用来替换原始的对象
            Class<?> iPackageManagerInterface = Class.forName("android.content.pm.IPackageManager");
            Object proxy = Proxy.newProxyInstance(
                    iPackageManagerInterface.getClassLoader(),
                    new Class<?>[]{iPackageManagerInterface},
                    new PmsHookBinderInvocationHandler(sPackageManager, signed, appPkgName, 0));
            // 1. 替换掉ActivityThread里面的 sPackageManager 字段
            sPackageManagerField.set(currentActivityThread, proxy);
            // 2. 替换 ApplicationPackageManager里面的 mPM对象
            PackageManager pm = context.getPackageManager();
            Field mPmField = pm.getClass().getDeclaredField("mPM");
            mPmField.setAccessible(true);
            mPmField.set(pm, proxy);
        } catch (Exception e) {
            Log.d(ZJ, "hook pms error:" + Log.getStackTraceString(e));
        }
    }

    public static void hookPMS(Context context) {
        String Sign = "原包的签名信息";
        hookPMS(context, Sign, "com.zj.hookpms", 0);
    }
}
```

ActivityThread的静态变量sPackageManager
ApplicationPackageManager对象里面的mPM变量

## 6.IO重定向

什么是IO重定向？

例：在读A文件的时候指向B文件

平头哥的核心代码
Virtual Engine for Android(Support 12.0 in business version)

IO重定向可以干嘛？

1，可以让文件只读，不可写

2，禁止访问文件

3，路径替换

具体实现：
过签名检测(读取原包)
风控对抗(例:一个文件记录App启动的次数)
过Root检测，Xposed检测(文件不可取)

```
 复制代码 隐藏代码
using namespace std;
string packname;
string origpath;
string fakepath;

int (*orig_open)(const char *pathname, int flags, ...);
int (*orig_openat)(int,const char *pathname, int flags, ...);
FILE *(*orig_fopen)(const char *filename, const char *mode);
static long (*orig_syscall)(long number, ...);
int (*orig__NR_openat)(int,const char *pathname, int flags, ...);

void* (*orig_dlopen_CI)(const char *filename, int flag);
void* (*orig_dlopen_CIV)(const char *filename, int flag, const void *extinfo);
void* (*orig_dlopen_CIVV)(const char *name, int flags, const void *extinfo, void *caller_addr);

static inline bool needs_mode(int flags) {
    return ((flags & O_CREAT) == O_CREAT) || ((flags & O_TMPFILE) == O_TMPFILE);
}
bool startsWith(string str, string sub){
    return str.find(sub)==0;
}

bool endsWith(string s,string sub){
    return s.rfind(sub)==(s.length()-sub.length());
}
bool isOrigAPK(string  path){

    if(path==origpath){
        return true;
    }
    return false;
}
//该函数的功能是在打开一个文件时进行拦截，并在满足特定条件时将文件路径替换为另一个路径

//fake_open 函数有三个参数：
//pathname：一个字符串，表示要打开的文件的路径。
//flags：一个整数，表示打开文件的方式，例如只读、只写、读写等。
//mode（可选参数）：一个整数，表示打开文件时应用的权限模式。
int fake_open(const char *pathname, int flags, ...) {
    mode_t mode = 0;
    if (needs_mode(flags)) {
        va_list args;
        va_start(args, flags);
        mode = static_cast<mode_t>(va_arg(args, int));
        va_end(args);
    }
    //LOGI("open,  path: %s, flags: %d, mode: %d",pathname, flags ,mode);
    string cpp_path= pathname;
    if(isOrigAPK(cpp_path)){
        LOGI("libc_open, redirect: %s, --->: %s",pathname, fakepath.data());
        return orig_open("/data/user/0/com.zj.wuaipojie/files/base.apk", flags, mode);
...