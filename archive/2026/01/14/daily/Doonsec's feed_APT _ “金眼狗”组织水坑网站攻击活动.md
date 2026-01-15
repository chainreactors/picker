---
title: APT | “金眼狗”组织水坑网站攻击活动
url: https://mp.weixin.qq.com/s/HTpBduTnQK5wSJ1i_RA3jw
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:29:43.149470
---

# APT | “金眼狗”组织水坑网站攻击活动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MNZOLibV9HGA1nqXSkL4XlDR951gW9guadB2bT1KTWM9ogw9uialeOdgw/0?wx_fmt=jpeg)

# APT | “金眼狗”组织水坑网站攻击活动

原创

Tahir

TahirSec

![]()

在小说阅读器中沉浸阅读

概述

“金眼狗”是一个东南亚方向的，从事博彩、狗推相关人员以及海外华人群体的黑客团伙，其业务范围涵盖远控、挖矿、DDoS攻击等。

该团伙通过部署爱思助手、快连VPN、QuickQ等仿冒网站，使用SEO排名优化，诱导受害者下载安装恶意安装包，运行后释放合法安装软件，通过合法pythonw程序内存执行Winos4.0类“银狐”木马与Gh0st远控木马。

TTPs分析

受害者点击恶意安装包，释放并执行pyinstaller打包的恶意程序，该程序释放后阶段攻击套件，利用pythonw.exe程序特性，加载库压缩包中恶意pyc字节码，最终通过线程池注入shellcode，在远程进程内存中执行Winos4.0远控木马，并且启动新进程内存执行Gh0st远控木马，外连C2服务器qaqbba.com、qaqkongtiao.com，实施远程控制。

金眼狗团伙攻击链，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MyoBqxricTuKpStyplnAicROeLlHTATvu7JfTyVPibL0OLjwhtWoZ5R6WA/640?wx_fmt=png&from=appmsg)

2024年年底至今，金眼狗团伙频繁使用winos4.0类“银狐”木马进行攻击活动，其仿冒的软件用户分布广泛，受水坑网站攻击影响的群体行业分布不确定，逐渐不具有定向性。该团伙手法和攻击目标，与“银狐”黑产类似，金眼狗团伙或与东南亚“银狐”达成某种合作。

样本分析

本次攻击活动涉及的样本以爱思助手样本分析为例。

恶意安装包(msi)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 文件名 | 功能 | 文件大小 | 编译时间 | md5 |
| v9.06.018\_Setup.msi | 恶意msi文件，释放恶意Visang.exe与爱思助手安装包 | 276201984 | / | 9063c7ff73318411ebbd6429dd3762da |
| Visang.exe | Pyinstaller打包的exe文件，释放后续攻击套件 | 19425737 | 2025-11-29 18:43:37 | 2ead2b26d7c9745a57f087bd5b33d72c |

安装包v9.06.018\_Setup.msi包含Visang.exe恶意程序与合法i4Tools\_v9.06.018\_Setup\_x64.exe安装程序。

Visang.exe为pyinstaller打包的python程序，反编译main.pyc后，可知该程序解压多个文件到以下目录：

C:\Users\Public\Python

C:\ProgramData\Python312

并复制x.ini到C:\Users\Public\x.ini，最后启动C:\ProgramData\Python312\run.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbn9ynicusNmWl0xuwA2mPeD1NQaVicPaNPa5LfW8frIBZUnH1TNMLzRdibCM5TBO8UINic6iarFz5dSsw/640?wx_fmt=png&from=appmsg)

第一阶段pyc加载器(run.exe)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 文件名 | 功能 | 文件大小 | 编译时间 | md5 |
| run.exe（pythonw.exe） | 合法pythonw.exe程序，加载同目录下python39.zip中恶意\_\_init\_\_.pyc字节码 | 98832 | 2020-10-05 23:37:47 | 21e55edcfd0c384c85503061a9027ddb |
| \_\_init\_\_.pyc | shellcode加载器，加载自身数据执行shellcode | 568368 | 2025-11-29 18:39:08 | fc4cf7677668701ae93b85e3a74b5ba2 |

run.exe为合法pythonw.exe程序，当run.exe启动时自动加载同目录下pyc库文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MkLdBdNKrfDybd2LibUET4ECIcBwB0WhJND5L1JtE3iau8zCdhSWYnMHQ/640?wx_fmt=png&from=appmsg)

其中python39.zip中包含恶意的pyc字节码文件\_\_init\_\_.pyc，反编译恢复python代码，可知该pyc字节码为shellcode加载器，分配内存调用CreateThread执行shellcode。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MSLCMX4TVgYHibtp1iaQsSlloicvhuM41Az5cUaauupAsNicW82TL76DAtA/640?wx_fmt=png&from=appmsg)

shellcode加载到run.exe内存中执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MkcP3k0T8PTFlX84ic1KmTkVbUKN16sB0KfMAxEnnCU2JHiagwLdADB9g/640?wx_fmt=png&from=appmsg)

解密自身数据，从内存中恢复PE文件，映射后执行PE导出函数f。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MEFZCdorX85xvtyxFEJF4FIibkCibbf0lic3gxsmMdPQLDc1EDNjG6IAdg/640?wx_fmt=png&from=appmsg)

第一阶段shellcode加载器(run\_shellcode.dll)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 文件名 | 功能 | 文件大小 | 编译时间 | md5 |
| run\_shellcode.dll | 加载器，被pyc内存加载的shellcode解密后映射的PE，利用线程池注入taskhostw.exe进程，创建计划任务启动gcc.exe（KOOK.exe） | 347512 | 2025-11-29 18:22:22 | ccc5907c14bf8516de88acd1325f0512 |

run\_shellcode.dll为被pyc加载的shellcode内存执行的dll文件，存在恶意的导出函数f。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MER1haYib51WcCn6XRB1FJmLMLbkicO0F4vwDRxFDAblLfzQdwtElnWfw/640?wx_fmt=png&from=appmsg)

判断360tray.exe进程是否存在，若不存在则尝试注入taskhostw.exe进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M8pDKydtRwChyHG04sz51HPwUVpGFspdfawrJBIQmCI6If4iabk8Zkxw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MsmxUncxrfFCg6BPsIIxSN3ekOjpNjBXpT5HZUkPeGmXWWVibZTbibyQw/640?wx_fmt=png&from=appmsg)

利用线程池TP\_IO方式注入shellcode。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MvyXKD2eGSoaUzLeVWtFjYr8h23rSMZMqBNY5ZgfMlU6YfW3AoGueUA/640?wx_fmt=png&from=appmsg)

创建一个异步的文件句柄，然后利用NtSetIoCompletion将TP\_IO写入到目标进程的 I/O 完成队列，将I/O队列设置为文件完成队列，并和创建的TP\_IO关联，最后通过WriteFile文件写入操作，触发回调执行shellcode。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M797umEW6XunyvA80qKfgmzm3LrIoIopOYWym8LeeDcQoWR84MaRoVA/640?wx_fmt=png&from=appmsg)

最后创建名为MicrosoftUpdate计划任务，通过登录事件触发执行Visang.exe释放的第二个目录下的C:\Users\Public\Python\gcc.exe恶意程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MLKQQZ93ibZM5WppgwATkjZtRHdZHIl6gJDQtnicZLFDdRQiaHB57GWcpg/640?wx_fmt=png&from=appmsg)

run\_shellcode.dll向Taskhostw.exe进程注入的shellcode，同样的操作，解密自身数据恢复PE文件，映射后执行PE。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MfoAGEpn3jSJ4hxE80lT0skjP6q3xUrCiceRibbId4Xsgnic8bPQdFhUQQ/640?wx_fmt=png&from=appmsg)

第一阶段Winos远控木马(injected\_winos.exe)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 文件名 | 功能 | 文件大小 | 编译时间 | md5 |
| injected\_winos.exe | 内存解密执行的Winos4.0远控木马 | 134520 | 2024-03-04 07:41:45 | 8f6011307ba03bd564e102793e3f65b5 |

内存恢复PE文件为exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M71icrsIj7e7PV4OX2ibFiciaGaUGx1sgX2XprLUUVIQT2r3EGSEcmbuS2A/640?wx_fmt=png&from=appmsg)

该样本为2024-03-04编译的Winos 4.0修改版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M0BOewicFA4ZDEATvctyMWoXv5o8SicSAsjt0FsZNR4gmY6AvRWvEQzhQ/640?wx_fmt=png&from=appmsg)

外连C2服务器地址qaqbba.com：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MK9jWqfTnpvGXia7xobvOTv2hh7fKwd8iaDK3lFrQOGGmbfdEaewicXZQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M1V1y0sq7yxCL8rSnw3C6PF6xoCGQ7icezzbJHIQMPZNuSqiaJxZiaesAg/640?wx_fmt=png&from=appmsg)

第二阶段pyc加载器(gcc.exe)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 文件名 | 功能 | 文件大小 | 编译时间 | md5 |
| gcc.exe（KOOK.exe） | 合法KOOK.exe程序，启动子目录app-0.99.0下的gcc.exe | 716752 | 2025-06-05 15:53:14 | 19ec6238327eb0358711f6259e443959 |
| gcc.exe（pythonw.exe） | 合法pythonw.exe程序，加载同目录下python39.zip中恶意\_\_init\_\_.pyc字节码 | 98832 | 2020-10-05 23:37:47 | 21e55edcfd0c384c85503061a9027ddb |
| \_\_init\_\_.pyc | shellcode加载器，加载自身数据执行shellcode | 314162 | 2025-11-29 13:08:16 | 2f6e1b4b33993ea8e00cf8ed3d339438 |

第一阶段pyc加载器创建名为MicrosoftUpdate计划任务启动C:\Users\Public\Python\gcc.exe。

gcc.exe为合法KOOK程序，主要功能为执行同目录下app-0.99.0的gcc.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MwB34fv5yqtwOnk8yIQh6oWfZJkMsPDiap0icicP6rYpyFOFwnUOa7ZibHQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MVDe6GKFvdeTky9mmG6XCfpAOJgwfqV7rK7ZpBkLgXfXGR4f2jGbdRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MJ4I1QYwGJga2Th9vKSlYFQeCmYRtTnnKV8NOOicmmG4JjLDouzW62vw/640?wx_fmt=png&from=appmsg)

执行C:\Users\Public\Python\app-0.99.0\gcc.exe，该gcc.exe 为合法pythonw.exe程序，启动时自动加载同目录下pyc库文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9MPHJM3p22nPty0O8KKAC9HDiceFXJva7tiaZiavaDo55LW06ribl8pdYS5Q/640?wx_fmt=png&from=appmsg)

其中python39.zip中encodings目录下包含恶意的pyc字节码文件\_\_init\_\_.pyc，反编译可知该pyc字节码为shellcode加载器，分配内存调用CreateThread执行shellcode。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M9icTrLWiaXh8icmicb1a1uajX5edweeprDeDzo18r0w9bMsFHDgIKhq2rQ/640?wx_fmt=png&from=appmsg)

gcc.exe内存中加载shellcode，与第一阶段\_\_init\_\_.pyc加载的shellcode相似过程，解密自身数据，内存中恢复PE文件，映射后执行导出函数k。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M62BFcE75hvOLGSOIcxUJjb1kobu01icjC5wNMN2Yj0PuNbsQwk6bqicg/640?wx_fmt=png&from=appmsg)

第二阶段shellcode加载器(gcc\_shellcode.dll)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 文件名 | 功能 | 文件大小 | 编译时间 | md5 |
| gcc\_shellcode.dll | 加载器，被pyc内存加载的shellcode解密后映射的PE，创建自启动项，读取x.ini文件并加载shellcode | 155000 | 2025-11-29 12:21:47 | 09509c014e980cbb378f6741c835f338 |

gcc\_shellcode.dll为被pyc加载的shellcode内存执行的dll文件，存在恶意的导出函数k。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bTmZNzhzqrbaFUGbcy6DISulTcJp0j9M2H8wqmVQDEyOgmteE8zSzibicrJf3G88zuLP8oMH1d4Vtb3cY8zcgT9w/640?wx_fmt=png&from=appmsg)

创...