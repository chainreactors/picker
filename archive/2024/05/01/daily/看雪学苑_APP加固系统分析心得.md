---
title: APP加固系统分析心得
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553405&idx=1&sn=b3ca13638151d7aa77848ad505aa3096&chksm=b18dbcb786fa35a115aa7fd0b81633a1e670edc74a30f2ef7380e1227129dcb9c867f395f612&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-01
fetch_date: 2025-10-06T17:18:56.138722
---

# APP加固系统分析心得

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FQicadOCiboLpxXIRw7OaqYT0BS65VDNLl8qLfagsHrzgdqS5RHLRsiauAvzpSAWuq4REpFdJgmpNnA/0?wx_fmt=jpeg)

# APP加固系统分析心得

fxyang

看雪学苑

本分析还是基本上以AndroidNativeEmU模拟器分析日志为主。不过为了保证函数可以正常运行，部分数据来自真实环境，并还原到原偏移地址中，保证模拟器正常执行。本次分析还首次在模拟器中实现art模式下的Dex加载过程，不用到真实环境中去dump dex了。

第一、对自身模块的保护：

APP加固系统都自身模块的保护并没有像360加固保护系统那么强大和复杂，就是使用了code段加密，然后中so的init\_array中进行解密，然后抹除so头，防止内存dump的方式。到JNI\_OnLoad的时候代码段已经解密完成，这个时候dump下代码，然后把原始的头还原回去基本上就能用来分析了，如果要用模拟器调试，还得patch掉解密和抹除so头的代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYP8u0vibnmgRb3gznxkOORduaSvmrwd86lLzHGJkOIk3QiaAtlZoCibAlicA/640?wx_fmt=jpeg&from=appmsg)

下面来看具体的代码实现。

Calling Init for: samples/appjiagu/libappprotect-up.so

Calling Init function: cbff8d85//这个就是init\_array中的第一个函数，解密函数。

把so头0x1000字节清零：

```
Executing syscall mprotect(cbfab000, 00001000, 00000003) at 0xcbffd165call mprotect:0xcbfab000  ç基地址，即so头地址======================= Registers =======================  R0=0xcbfab034  R1=0x0  R2=0x1  R3=0x1R4=0x7ffce8  R5=0x7ffce8  R6=0x7ffe90  R7=0x7ffff8  R8=0x0R9=0x0  R10=0x0  R11=0x0  R12=0x7ffce0  SP=0x7ffce0LR=0xcbffd165  PC=0xcbffd60c======================= Disassembly =====================0xcbffd60c:    0170   strb   r1, [r0]   ç开始把so头清零0xcbffd60e:    6e48   ldr    r0, [pc, #0x1b8]0xcbffd610:    7f49   ldr    r1, [pc, #0x1fc]0xcbffd612:    7944   add    r1, pc0xcbffd614:    4018   adds   r0, r0, r1
```

解密代码段中加密的代码：

Executing syscall mprotect(cbfae6f1, 00042C22, 00000007) at 0xcbffab7f

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYPMIL0KGBNGapl6aENzYZ6tJO3AaISyjSXbjNys2AQjz1jkgqFVRwaaQ/640?wx_fmt=jpeg&from=appmsg)

解密代码段中加密的代码：

Executing syscall mprotect(cbfae6f1, 00042C22, 00000007) at 0xcbffab7f

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYPMIL0KGBNGapl6aENzYZ6tJO3AaISyjSXbjNys2AQjz1jkgqFVRwaaQ/640?wx_fmt=jpeg&from=appmsg)

到这里：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYPCRuicyQmM2S1lFougWU3jXCtibneWNhmB698NBGmoyQ5iaicnEOtrqYl5A/640?wx_fmt=jpeg&from=appmsg)

都是被加密的代码。

```
======================= Registers =======================  R0=0x47  R1=0xcbfae6f1  R2=0x7ffe60  R3=0x7ffe58R4=0x7ffcf8  R5=0x7ffdd8  R6=0x7ffe90  R7=0x7ffff8  R8=0x0R9=0x0  R10=0x0  R11=0x0  R12=0xffff1c30  SP=0x7ffce0LR=0xcbffe2f3  PC=0xcbffca94======================= Disassembly =====================0xcbffca94:    0870   strb   r0, [r1] < --R1=0xcbfae6f10xcbffca96:    1878   ldrb   r0, [r3]0xcbffca98:    1168   ldr    r1, [r2]0xcbffca9a:    0870   strb   r0, [r1]0xcbffca9c:    1020   movs   r0, #0x10
```

这个函数执行完就可以dump so，然后修复代码了。

JNI\_OnLoad：代码已经解密出来了：

```
0xcbfae9c4:    f0b5   push   {r4, r5, r6, r7, lr}0xcbfae9c6:    03af   add    r7, sp, #0xc0xcbfae9c8:    89b0   sub    sp, #0x240xcbfae9ca:    6e46   mov    r6, sp0xcbfae9cc:    3162   str    r1, [r6, #0x20]>dump 0xcbfab000CBFAB000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................CBFAB010: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................CBFAB020: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................CBFAB030: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
```

可以看到so头被清除了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYPBbq2IfQTtEqEZY7SascuDGpfVz91xWBHgzJQeUibHw3iatTcibRdmGjCg/640?wx_fmt=jpeg&from=appmsg)

修复so方法：

先dump 数据，然后用010Editor 把原始的头贴回去。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYPz0KJZ67iaBPxggFWYIOnqib912k6DAZH174oScqUcq8jINDWI56rJjSw/640?wx_fmt=jpeg&from=appmsg)

由于代码已经被解出来，所以后面不能再被解密了，patch代码，第一个就是把清除so头的代码除掉。然后把解密代码的写入操作代码也nop掉。这样就保证了可以二次加载这个so进行运行分析。

0xcbffd60c:    0170   strb   r1, [r0]   ç开始把so头清零   nop掉代码

0xcbffca94:    0870   strb   r0, [r1]    < --R1=0xcbfae6f1   nop掉

0xcbffca96:    1878   ldrb   r0, [r3]

0xcbffca98:    1168   ldr    r1, [r2]

0xcbffca9a:    0870   strb   r0, [r1]     nop掉代码

0xcbffca9c:    1020   movs   r0, #0x10

从分析来看，APP加固对自身模块的保护力度不是很强，修复起来也比较容易。

JNI\_OnLoad 函数主要就是把libc中的这些函数填到函数列表中，然后通过列表的索引进行调用。这样防止分析代码：

```
Called dlopen(libc.so)Loading module 'vfs/system/lib/libc.so'.call malllos size:0x9 at 0xcbfc15e7malloc addr:0x2022000Called dlsym(0xcbbdf000, _exit) at 0xcbfb1669symbol:_exit addr->: 0xcbc2780ccall malllos size:0x9 at 0xcbfc166fmalloc addr:0x2023000Called dlsym(0xcbbdf000, exit) at 0xcbfb167f
```

导入的函数有：

```
#libc_fun_name = ["_exit","exit","pthread_create","pthread_join","memcpy","malloc","calloc","memset","fopen","fclose","fgets","strtoul","strtoull","strstr","ptrace","mprotect","strlen","sscanf","free","strdup","strcmp","strcasecmp","utime","mkdir","open","close","unlink","stat64","time","snprintf","strchr","strncmp","pthread_detach","pthread_self","opendir","readdir","closedir","mmap","munmap","lseek","fstat","read","select","bsd_signal","fork","prctl","setrlimit","getppid","getpid","waitpid","kill","flock","write","execve","execv","execl","sysconf","__system_property_get","ftruncate","gettid","pread64","pwrite64","pread","pwrite"," ","statvfs"]
```

后面就是注册加固系统com.app.protect.A 主功能函数：

```
JNIEnv->FindClass(com/app/protect/A) was calledJNIEnv->RegisterNatives(1, 0x007fff58, 4) was calledRegister native ('n001', '(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IZ)V',function->'0xcbfaf829') failed on class com_app_protect_A.Register native ('n002', '(Landroid/content/Context;)V',function->'0xcbfaf999') failed on class com_app_protect_A.Register native ('n003', '()[Ljava/lang/String;',function->'0xcbfaf9f9') failed on class com_app_protect_A.Register native ('n004', '()V',function->'0xcbfafad5') failed on class com_app_protect_A.
```

这个版本的加固中，注册了四个函数。主要的功能在'n001'这个函数中。包括dex解压，解密，加载，附加数据的处理。Dex\_VMP数据初始化。

另外Native so中大量使用字符串加密，防止关键字符串暴露，也是APP加固的技术特点：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FPztLBtRhK5G8AO5lZyLYPJk4iatWccB1zxIdlIM9e6j7uck0LJUd60UmNczRQ5t3Q9aojmFwc4Bg/640?wx_fmt=jpeg&from=appmsg)

第一、

第二、对dex文件的保护：

Android APP加固系统保护的重点就是dex，所以对dex文件的保护是比较重要的。APP加固系统这块也做的比较好，甚至全程没有dex明文文件落地，都是从apk包中在运行时解压解密加载。具体我们来看看流程：

APP加固的JNI\_OnLoad中注册了四个Native函数，其中n001函数就是处理dex解压，解密，加载和vmp数据的。

```
    protected void attachBaseContext(Context arg8) {        StubApplication.mContext = arg8;        StubApplication.mBootStrapApplication = this;        AppInfo.APKPATH = arg8.getApplicationInfo().sourceDir;        AppInfo.DATAPATH = StubApplication.getDataFolder(arg8.getApplicationInfo().dataDir);        if(!Debug.isDebuggerConnected()) {            StubApplication.loadLibrary();            A.n001(AppInfo.PKGNAME, AppInfo.APPNAME, AppInfo.APKPATH, AppInfo.DATAPATH, Build.VERSION.SDK_INT, AppInfo.REPORT_CRASH);        }
        if(AppInfo.APPNAME != null && AppInfo.APPNAME.length() > 0) {            StubApplication.mRealApplication = MonkeyPatcher.createRealApplication(AppInfo.APPNAME);        }
        super.attachBaseContext(arg8);        if(StubApplication.mRealApplication != null) {            MonkeyPatcher.attachBaseContext(arg8, StubApplication.mRealApplication);        }}
```

Java层的入口，可以看出来，首先对调试状态进行了检测，如果是调试状态就不会加载so模块，也不会执行dex的解密函数A.n001.防止APP被调试。如果没有被调试则加载完libappprotect.so后进入dex的加载函数，即n001函数。从上面我们知道JNI\_OnLoad中注册了这个函数，函数地址是：function->'0xcbfaf829'，我们就看看这个Native函数的具体功能：

首先获取APP的包信息，从包信息中获取signatures，从apk包的META-INF目录读取签名文件TRANSLAT.RSA，然后从0x3A开始读两个字节的签名数据长度，根据长度读取后面的签名数据。比如这个APP的签名长度是0x235

读取数据如下：

```
00000040: 30 82 02 31 30 82 01 9A  A0 03 02 01 02 02 04 4E  0..10..........N00000050: 25 42 6B 30 0D 06 09 2A  86 48 86 F7 0D 01 01 05  %Bk0...APP.H......00000060: 05 00 30 5D 31 0B 30 09  06 03 55 04 06 13 02 43  ..0]1.0...U....C00000070: 4E 31 10 30 0E 06 03 55  04 08 13 07 62 65 69 6A  N1.0...U....beij
```

然后对这个签名文件取hash：

```
.text:CBFB71CE 28 4D                       LDR     R5, =(_GLOBAL_OFFSET_TABLE_ - 0xCBFB71D4).text:CBFB71D0 7D 44                       ADD     R5, PC          ; _GLOBAL_OFFSET_TABLE_.text:CBFB71D2 44 19                       ADDS    R4, R0, R5      ; byte_CC00F664.text:CBFB71D4 20 46             ...