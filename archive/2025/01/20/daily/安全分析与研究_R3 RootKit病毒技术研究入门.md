---
title: R3 RootKit病毒技术研究入门
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490049&idx=1&sn=eec060b016a2c2c48b9a5a5a5a6ef745&chksm=902fb529a7583c3f0a2b0935cfd9f3df6108088566ca52d5bd9df83588d2b382a01ee1757d28&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-01-20
fetch_date: 2025-10-06T20:09:14.407123
---

# R3 RootKit病毒技术研究入门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5ZQDc97B4nEOt5VKQ810hQfq1kRZbhG4bKv1m2ZsybvFLLSgyPLdlVMQ/0?wx_fmt=jpeg)

# R3 RootKit病毒技术研究入门

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

RootKit简介

RootKit是一种特殊的恶意软件，它的功能是在安装目标上隐藏自身及指定的文件、进程和网络连接等信息，比较多见到的是Rootkit一般都和木马、后门等恶意程序结合使用。

技术研究入门

一般的恶意程序使用RootKit技术，主要功能分为下面两类：

(1) 隐藏文件

(2) 隐藏进程

RootKit技术使用在不同的操作系统中，如windows、linux等，同时使用的技术可以从应用层(R3)->驱动层(R0)->硬件层等，下面我将重点介绍一种在R3下使用RootKit技术隐藏文件和进程的方法，该方法被应用在之前发现的应急响应的恶意样本之种。这里先介绍R3级的RootKit技术，针对R0级的RootKit技术，遇到相关样本的时候也会进行分享。

隐藏进程技术

通过HOOK NtQuerySystemInformation函数，然后在进程链表中，摘除相关的进程，就可以达到隐藏进程的目的，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5Zs6zibfjnicZsicVtIhYej9NDdKeYtLwLfeZUibK5GDBVWOzS5jnygBhoZg/640?wx_fmt=png)

隐藏文件技术

通过HOOK ZwQueryDirectoryFile函数，然后在遍历目录时，发现相关的文件，则跳过，可以达到隐藏文件的目的，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5ZyIRP8ZoicKyJgq2po9ydM5WEysCkl10ffWKSBxj1yODlHxcicwMTjm5w/640?wx_fmt=png)

实战技术验证

验证环境：win7 64位

验证功能：隐藏进程，隐藏文件

验证地程：

(1) 运行程序，可以从进程列表中看到相关的进程$77-ExampleExecutable.exe，以及文件目录下的$77-ExampleExecutable.exe文件，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5ZlomQWnonC3dkmXcnyibD6U1Nhibdc1jiccSuVG8rmU5Os3W2COcRb2TKQ/640?wx_fmt=png)

 (2)使用安装程序，将RootKit的恶意DLL注册到AppInit\_DLLs，这样当进程启动时会自动加载相应的RootKit恶意DLL实现相关的RootKit技术，隐藏进程、隐藏文件等，当我们安装成功之后，重启taskmgr.exe和explorer.exe两个进程，发现进程列表中没有$77-ExampleExecutable.exe这个进程，同时相关的目录下也没有$77-ExampleExecutable.exe这个文件，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5Ze1ag4dD4AuR81nGicg4ODBOkyvgtNxLJuD6rrJyG4NlC1IwFOcEMPNw/640?wx_fmt=png)

这样就达到了隐藏进程和隐藏文件的目标。

反RootKit病毒技术

通过上面使用的R3级的RootKit技术，我们通过Explorer.exe和taskmgr.exe是看不到相关的文件和进程的，但可以通过专业的工具查看到相关进程和文件，使用PCHunter进行查看。

隐藏的进程，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5Zls1wyoS3CoFNLzrG0Dwog16AJJ3bcWDR3zNB5ZPOibbzNHaEyDRr2sQ/640?wx_fmt=png)

红色标记的就是之前通过R3级的RootKit隐藏的进程。

隐藏的文件，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5Zolbx1FtibfiasORZia5icrJMtwmZ1AkDhvOZLzCfCE1mxRicoe4LDBIYiaOg/640?wx_fmt=png)

可以看到我们之前用Explorer.exe进程无法看到的文件：$77-ExampleExecutable.exe

我们可以通过WinDbg工具查看系统的相关进程列表，运行命令:!process 0 0之后，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5ZCzyTiaXoQEsIPdEVwdEMMN5cTbbRB4jfhciagqKrXoLw34FsibPPXv9JQ/640?wx_fmt=png)

可以看到$77-ExampleExecutable.exe这个进程依然存在于内核进程模块之中，因为我们是能过R0级的函数进行的查看，上面的方法只是在R3级使用了HOOK技术，无法躲过R0级的进程遍历。

同样我们可以查看到相关的文件目录，以及对应的文件，运行命令：

.process /p fffffa8001a87b30; !Peb 7fffffd5000之后，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5Zj8JorvSxpDnDv88m0eu6fqZIGlhiagm2gj3VFazvZScFKdxiaic4QmEuw/640?wx_fmt=png)

针对于R3级的RootKit技术，我们可以通过R0级的方法，实现反R3级的RootKit相关的技术，通过驱动去遍历进程和文件，可以得到相关的隐藏的进程和文件。

R0级的RootKit技术一般使用HOOK技术有：

SSDT HOOK、InLine HOOK、IRPHOOK、

SYSENTER HOOK、EAT HOOK、IAT HOOK、

IDT HOOK、OBJECT HOOK等

也可以使用Minifilter技术过滤达到隐藏文件的目的，R0级的RootKit技术可以实现如下一些功能点：

(1) 文件隐藏

(2) 进程隐藏

(3) 注册表隐藏

(4) 网络端口隐藏

(5) 驱动自身隐藏

(6) 进程DLL模块隐藏

后面遇到了相关的样本，我们再来详细讲解这些高级的RootKit技术。

**RootKit&BootKit恶意软件一直是高端黑客组织研究的重点之一，笔者后面打算建立一个高级恶意样本研究群，专门针对Window\Linux\Mac平台下的各种涉及RootKit,BootKit(UEFI)技术的高级恶意软件进行分析和研究。**

总结结尾

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5ZIbicVuNWKM5WVvXtiaN6AYiaDicWUwgCiaFYIQ0BV0aRHicib0xpXGWjEmoyA/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过