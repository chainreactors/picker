---
title: 一种apc注入型的Gamarue病毒的变种
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-29
fetch_date: 2025-10-06T18:51:13.180665
---

# 一种apc注入型的Gamarue病毒的变种

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7cUgMdbXF8UpSGmic4csMtj4PuztOrcxnYk5Nepr5ARhxulZBGDPIfNw/0?wx_fmt=jpeg)

# 一种apc注入型的Gamarue病毒的变种

mb\_zuyotbmd

看雪学苑

##

```
一

概述
```

# 这个病毒通过可移动存储介质传播，使用了应用层APC注入和dga域名技术，整个执行过程分为4个阶段，首先从资源节中解密出一段shellcode和一个PE，执行shellcode，创建一个同名的傀儡进程，将解密出来的PE注入这个傀儡进程中启动，然后启动并通过apc注入的方式注入系统进程svchost.exe，从内存中解密了1248个dga域名尝试连接，并执行后续的恶意操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7osfTaWibzB2moAaEXdk9pOceAskwf5JXuibNQMkKfzHwojw18jL2XzgQ/640?wx_fmt=png&from=appmsg)

##

```
二

样本的基本信息
```

```
MD5: 9de070f6864bc64e0fcac70a0c881cfb
SHA1: 8b5c9c3f7ca2921542252b92d749696c75f617b2
SHA256: d59d469759bce4bb41ffa92a617570770db3e9712a1da308301131f6806c8123
文件大小: 118 KB (121,344 字节)
Link date:    6:43 2011/3/18
Publisher:    n/a
Company:    Tometa Software, Inc.
Description:    Owo Giqer Idif
Product:    Bomisyh
Prod version:    2, 8
File version:    2, 8, 7
MachineType:    32-bit
Verified:    Unsigned
```

#

# 第1阶段 病毒母体

从资源节中解密一段数据，数据包括一段shellcode和一个pe，执行这段shellcode,
这个样本的主体功能如下，注册了一个异常处理函数用来处理程序异常，后面会通过主动div 0来产生异常，会触发调用这个函数，应该是用来对抗调试用的。

注册一个回调函数，每隔20毫秒调用一次，主要功能在这个回调函数中。

```
TimeQueueHandle = CreateTimerQueue()
CreateEventA(hEvent,0,0,0)
RtlInitializeCriticalSection(gCriticalSection_40C7C0);
//捕获程序产生的异常，使用自定义函数TopLevelExceptionFilter_4011A0来处理
SetUnhandledExceptionFilter(TopLevelExceptionFilter_4011A0);
gTickCount_40C7E4 = GetTickCount();
//注册一个回调函数，每隔20毫秒调用一次
CreateTimerQueueTimer(hNewTimer_v6,TimeQueueHandle_v5,sub_401540,0,1,20,0);
```

从资源节中读取名为doma的资源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7qPJb2xdbbPGBkibiby7yqvWSwZ5TBQ1LQvGma8febYb17neu4MfgianibQ/640?wx_fmt=png&from=appmsg)

解密资源节中数据，分配一段0x820大小的可执行内存，将解密出内容的前0x820字节拷贝过去 这是一段shellcode,将0x820至0x27220作为参数传入（这是一个PE）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7Kdh6TYf1ib5iaaTdxlyEL9QIvZTm3AoTj20dx8fHmBE6jyVhkGIK5OrQ/640?wx_fmt=png&from=appmsg)

使用OD动态调试，将这段shellcode dump出来，下面分析这段shellocode。

# 第2阶段 shellcode

这段shellcode的主要功能是创建一个同名的傀儡进程，将pe注入其中执行。

首先获取下列api的地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7lFzBbRAueKLfhqRFH5z9sbRpWp65UfibWnFJ4TSP2OxZ61ibdnM2DW2w/640?wx_fmt=png&from=appmsg)

然后创建一个同名的进程，将参数中的PE注入到傀儡进程中启动。

下面重要分析这个PE。

# 第3阶段 同名傀儡进程

注入傀儡进程中的pe的基本信息如下：

```
Verified:    Unsigned
Link date:    20:23 2017/10/26
MachineType:    32-bit
MD5:    F5CD7C49DEF09E1DEBC4559F1A7EB3BB
SHA1:    980C52CACD969F9524FBE254F5F42753654AFA92
SHA256: 763e1dd259fde007e1d1bb28c46b5941d44dad8754b9604485cf24682847f786
编译器: Microsoft Visual C/C++(2010)[-]
链接程序: Microsoft Linker(10.0)[GUI32]
文件大小: 154 KB (158,208 字节)
```

首先获取命令行参数，若带参数的话，说明用户点击了lnk文件，使用资源管理器打开同名的文件夹或执行同名的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7QoicLNJ9IkAnd3ibYIVAVM7AF0KzHLQibmibuBVxwGI5vQ5nH9oeCiceLAA/640?wx_fmt=png&from=appmsg)

读取系统的磁盘信息，判断当前系统是否为沙箱环境，是的话，退出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7iaRlomSg8VxJNTpcAuc5F3cZWxeYACVYnRmKTjNEuwwn2am9JjUummw/640?wx_fmt=png&from=appmsg)

遍历注册表中的开机启动项，跳过自身的启动项(`{893B0615-D58A-CE78-7A5B-D4C7F40D0C54}`)和文件路径中含有关键字`\\Microsoft\\Windows\\Themes、 \\WindowsUpdate、 \\Windows Live`的项。

若文件路径含有\Temp、'{'、'}'、.exe，或者启动项中含有'{'、'}'、 "Microsoft"、 "Windows" 、"Kernel"的话，删除相应的启动项。

对应其它启动项，关闭对应的进程，若是隐藏文件，重启后将其删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7nYPic9M88Iiclz2iaQWdg7wPswwWynx8TOhenHSIBS6LOibjdB3yQu9qlw/640?wx_fmt=png&from=appmsg)

创建一个名创建名为`{893B0615-D58A-CE78-7A5B-D4C7F40D0C54}`的事件对象，防双开，若存在同名的event，返回0x12345678。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7bac938sQANYDreU3EN3uNmnFjf5MvuNpvFs1v02AUpiaXEZsqWHWGUA/640?wx_fmt=png&from=appmsg)

创建进程`C:\windows\system32\svchost.exe`，并挂起，将当前病毒副本拷贝进行svchost进程空间，将当前程序的内存镜像复制到svchost进程中，APC注入svchost进程，执行sub\_407140函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7XEK5B7k4z7cW2AR552s6GibA5Q6s77NCeQKKia4JhuYa6jdT1GcMLYmQ/640?wx_fmt=png&from=appmsg)

#

# 第4阶段 svchost.exe

在svchost.exe的进程空间中主要执行sub\_407140的功能，病毒的主要的功能就在这个函数中。

1.首先添加了一个计划任务，然后在注册表中添加了一个开机启动项，启动项和计划任务均为`{152B2E26-FDB9-5268-7A5B-D4C7F40D0C54}`，均指向文件`c:\programdata\{893B0616-D589-CE78-7A5B-D4C7F40D0C54}\2484d689.exe`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7r7ZxOt9HaV7onNxmBZIHmav4A77OuJFPkgI9TmkicSw0JatibK7iakHibQ/640?wx_fmt=png&from=appmsg)

2.若当前病毒进程是从U盘上感染的，删除掉U盘上的病毒母体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7fWxN5jnWdPsAGX3aJYXDjkT1PBg6JY9cQ52QFIibQjB53ribjGCH248w/640?wx_fmt=png&from=appmsg)

接下来，创建了一系列线程，来执行不同的操作。

3.创建线程Thread\_405c20，创建一个死循环，每隔5秒，检查一次计划任务和注册表中的开机启动项，若被删除了，再添加一遍。

4.创建线程Thread\_406110，创建一个死循环线程(间隔10s)，通过CRC方式对比当前内存母体与磁盘母体文件是否相同，不同则将内存母体替换磁盘母体(便于实时更新，或者是防止母体文件被篡改)

5.创建线程Thread\_408F70，感染可移动存储介质。遍历U盘根目录的文件，根据不同的驱动器生成一个隐藏文件和文件名（不同的系统上不一样），将病毒副本释放其中。如这样的文件名

如`X:\\{d3137d55-925f-487e-48f8-5999785d98ab}\c39d5c50-e52b-3890-9a66-c4c1eff14215.exe`。

隐藏根目录下的文件夹，创建一个同名的快捷方式，lnk文件的target如`%comspec% /c "{d3137d55-925f-487e-48f8-5999785d98ab}\c39d5c50-e52b-3890-9a66-c4c1eff14215.exe '原来的目录名\'"`，当用户的点击这个lnk文件时，会先执行病毒副本，然后再打开原来的目录或文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7G3NRicBegeUic0BXbupzLKUJJZUOtyWUksMAHN0BDrAibia2t4OCajbTzw/640?wx_fmt=png&from=appmsg)

6.创建线程Thread\_406370，从C2下载新的病毒版本，若比当前版本新，则会更新内存和磁盘上的病毒文件。这个下载的链接是从全局变量gPayload\_428010中解密得到的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7s2EsN5sW7XQJSlaoTgbGnz7h9C1ia4RKx5ek47YsEp2XLdcLInmC25A/640?wx_fmt=png&from=appmsg)

7.从系统中寻找一个进程（跳过teamviewer.exe和tv\_w32.exe，当前进程和64位的进程），将sub\_401fc0注入，作用是当当前进程退出后，启动病毒母体。

没有找到合适的进程的话，启动一个notepad进程进行注入。用来保护自身进程被kill。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7eGrYZP5TOHJqb5Nx3mtL1h0fsK5mrRxataMxujynvBL2uWf6P8VAEQ/640?wx_fmt=png&from=appmsg)

8.将当前时间写入注册表`HKEY_CURRENT_USER\Software\Classes\CLSID\{893B0615-D58A-CE78-7A5B-D4C7F40D0C54}`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7NZrA1qtEgQKsicWpvl0pJxR1Mz4eypXiakDV4U2FXCbDb26ceHfy296g/640?wx_fmt=png&from=appmsg)

9.连接C2，这里共解密出1428个不同的C2地址，会逐个请求这些域名，直到找到可用的c2地址，与其建立连接，会将当前系统信息发送给控制端，从c2下载载荷执行，执行后续的恶意行为。这一部分逻辑比较复杂。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7ItML8pFibQY7uA7vs8kftgOQGBHRGg8YZgwWOb6OlLs2GXYIGJicGqVQ/640?wx_fmt=png&from=appmsg)

#

# 感染U盘的症状

感染前

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7KmoHKDBibIcyEdD35f5SiaX6VFxnCk2FAFuuErOpr44aiabcw0VHibqWmw/640?wx_fmt=png&from=appmsg)

感染后

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7JBwAyyaLpVWdVpNM0glcWQz9hkgtLv2F5M146hFVBQ734CAACVoBRw/640?wx_fmt=png&from=appmsg)

lnk文件的目标为`%comspec% /c "{d3137d55-925f-487e-48f8-5999785d98ab}\c39d5c50-e52b-3890-9a66-c4c1eff14215.exe 'python逆向\'"`

这样，用户在点击快捷方式之后，就会运行病毒，并将对应的目录名传递给病毒，病毒会打开相应的目录，并执行感染系统的操作。

##

```
三

IOC
```

```
hash
MD5: 9de070f6864bc64e0fcac70a0c881cfb
SHA1: 8b5c9c3f7ca2921542252b92d749696c75f617b2
MD5:    F5CD7C49DEF09E1DEBC4559F1A7EB3BB
SHA1:    980C52CACD969F9524FBE254F5F42753654AFA92

文件
c:\programdata\{893B0616-D589-CE78-7A5B-D4C7F40D0C54}\2484d689.exe
U盘中类类似这种文件
X:\{d3137d55-925f-487e-48f8-5999785d98ab}\c39d5c50-e52b-3890-9a66-c4c1eff14215.exe

Event对象 {152B2E26-FDB9-5268-7A5B-D4C7F40D0C54} 防双开
名为{152B2E26-FDB9-5268-7A5B-D4C7F40D0C54}的计划任务
注册表
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\{152B2E26-FDB9-5268-7A5B-D4C7F40D0C54}

HKEY_CURRENT_USER\Software\Classes\CLSID\{893B0615-D58A-CE78-7A5B-D4C7F40D0C54} 用来记录时间戳

域名
v1.eakalra.ru:1281
v1.op17.ru:6006
v1.zgclgdb.ru:8518
v1.yekfhsh.ru:7372
v1.fasefja.ru:3410
v1.hpifnad.ru:3721
......更多请查看原文
```

#

# 参考资料

*◆一款正在活跃的U盘感染型病毒分析-华盟网 (77169.net)https://www.77169.net/html/185673.html*

*◆一款正在活跃的U盘感染型病毒分析 (sohu.com)https://www.sohu.com/a/204633647\_354899*

*◆终端安全系列-计划任务详解-腾讯云开发者社区-腾讯云 (tencent.com)https://cloud.tencent.com/developer/article/2318604*

![](https://mmbi...