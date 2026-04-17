---
title: 应急响应打靶--windows2
url: https://mp.weixin.qq.com/s/RqexGmYJCOYuG8V7AfpPgQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:01.202365
---

# 应急响应打靶--windows2

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qkajCoyKpkB5gMFMqicdq3F79AMVwvB3icEiaJeiawTaOyeAKJuSMqxicYiaUlor6VkXP5uzVcmmWEJ15ByzsiaYh1q3HzPDcVcngNojxicJ732X1Cs/0?wx_fmt=jpeg)

# 应急响应打靶--windows2

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

靶机资源：

应急

本文能手工就手工，初次学习建议纯手工，后期上机排查时如果客户不让上传工具，最起码不会两眼一摸黑

实战过程中，建议先工具来一遍，之后再细节去应急

登录密码：Zgsf@qq.com

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDB7xZ3l8hUD1LKrmjYiaTKNN6pXQgKOvRLhCNpGqXl0UMuMX7baqhXHVI00CeRd9icgFZ9x18KTeYapLjEAKU95kY4ZBvVropto/640?wx_fmt=png&from=appmsg)

虽然是靶机，但靶机来源于实战，我们把靶机当作实战即可

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkARHgQtVVCUCPkm6KCDDee83nvFJFOyk3icouNkqw9uAyMicV0jDibcbEg10wx26sf1NIeqSauJJ28k7KdtNqL0TRrm3j6e9ehEEY/640?wx_fmt=png&from=appmsg)

登录靶机，可以看到Phpstudy程序，代表存在网站，可以简单记一个笔记，梳理流程

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCVBhSwzZia8JohFLa0sfmVU6oLCF3SuiaWgtI284jYscUJbfdyOSibvuxIggBonUF1pSzHpWT5aBiaTwia9mddS4leW43KJgE3TxLw/640?wx_fmt=png&from=appmsg)

打开文件资源管理器，发现有两个最近使用的文件，这里先记录下

还有一个frp程序，也记录下

之后直接找Apache日志，看看能不能找到有用的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDic4dicmAHMjuAvdJmcHh0ugLJvh2DQo9ZVMk1Zt5eGTpX8r0ibnUdNCNLF3jCbbKDVyJibWSmBZw0DwFSZnicw0PMy3zbhNJnQ5BE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBMwUbLZE7pVnVfwFiabmjVsQQZuteFMFRxzSFQzBTvjgG95cbnjviajqDvqKCtYGH8FuwwsN3LJjgoBpzA9dgbvfL04nVDXPb0g/640?wx_fmt=png&from=appmsg)

分析日志得到以下内容：

* 192.168.126.135    2024.02.29 12:35:10    第一次访问
* 192.168.126.135    2024.02.29 12:38:31    爆破目录   大量404
* 192.168.126.135    2024.02.29 13:02:00    突然使用GET访问/system.php
* 192.168.126.135    2024.02.29 13:08:49    之后使用POST访问/system.php

疑问？

为什么突然使用GET访问/system.php，之后使用POST访问/system.php，system.php怎么来的？

* system.php   修改日期为2024.02.29 13:07
* 但是发现一个3389.bat，很可疑，先留个疑问，修改日期为2024.02.29 13:14

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDOPUQlzrYGtoyzVTHw4bd8pmjwLhfuZMthnImxoiblkfa4R0wwJ1pRW62SiaIXTPvwwOPZGB7nwrQdxhjrpzzMDibByRCs5Mb0H4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAwmnDyW3svnotHPbApxY7ZgSb8WyvRwFHrq6q8cxNDu5gGahQcS1kUdHRrmH7NsRYcvmVga4sVeLCjxGBYKicibYribpJPXEUWhc/640?wx_fmt=png&from=appmsg)

* 得到system.php的密码为hack6618

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCQYV8ia9FfvbK3ic3rKNHJW845LwMv1vlUZ6ISPYtTh1uS8VTvW8wD0sOwPJUFCgcPuiau2sMYicoOQ7MlKDvyiaQcicwLia8NQwRSWM/640?wx_fmt=png&from=appmsg)

那system.php怎么来的呢？

* phpstudy有个ftp程序，会不会从这里来的？
* 翻找FTP日志

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDIoicaTxRMMYxKH2QFZz2NZGJW1GPbQwmThB2b0nqE0M1cWTQScdbzdRassdPZ5PVGRLfvk3SLicI4dByiay7LAwKMUcOibSYXGAA/640?wx_fmt=png&from=appmsg)

* 果然，攻击IP攻击过FTP，时间为2024.02.29 12:35:30

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBtLcPBkLzbNfZrAP1I38M1GHLnan0vDpice8buMc8AyoHyNUAMNeCLvR1YAvd78hjA0ctibccLZm1OrkaCYciaLjf24wmvr7iaibGI/640?wx_fmt=png&from=appmsg)

* 192.168.126.135   2024.02.29 12:42:03   尝试爆破root密码

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAInVNBDVicJibRYibOpUurXM0tAiaiappwqC0E5s4ibrlaIQlWeC88VY3vWhibNXw7GCggK3kTcTfmDXmGwUgX63Xc3CBTwfiaPCNxjAU/640?wx_fmt=png&from=appmsg)

* 192.168.126.135   2024.02.29 12:43:18   尝试爆破admin密码

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBRdliaW9c8KIRcktGicfIlx7TrGAT82fchkAyYEdGKsR32xpicXgrp0aEqk1Dy05ubp9ibmaMiaHmk2ibxekpvolriaoia2vWiab0iaONX0/640?wx_fmt=png&from=appmsg)

* 192.168.126.135   2024.02.29 12:48:11   成功爆破出admin密码
* 192.168.126.135   2024.02.29 12:48:39   进行一系列操作

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBmbq5RRBkslt07OJSJibXiaDsTryJgzWxQoNwuKaw1R1IHhcZwGddicK8Rtsauf7TXF5u9WuzIIP3YTJGueVQxbhttzQbVhk3ialM/640?wx_fmt=png&from=appmsg)

* 192.168.126.135   2024.02.29 13:01:39   上传system.php文件到服务器根目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBRibL48iclDWUSsE03dwfVCGibV4uASklmlAiapxl2BTBicTibKx73UREqofM6xxaaRn22tme0RumlguZiaf6t5cG248XabVEciacwicXU/640?wx_fmt=png&from=appmsg)

* 192.168.126.135   2024.02.29 13:07:58   上传system.php文件到服务器根目录

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDjias5WMbkpr3hrCvLMxcz8on3NDIXtpWo6gp02gBbfsD06n56tOWvte3p1bGj4APHDa7uzElxcSLSic1vdqK4MMPyIwCGl53jY/640?wx_fmt=png&from=appmsg)

* FTP根目录：C:\phpstudy\_pro\WWW\，system.php文件创建时间为2024.02.29 13:07:58，所以可以判定入口点是FTP弱口令漏洞

入口点找到了，web入侵之后做了什么？需要进行系统排查

* 检查系统账号：是否存在可疑账号、新增账号、隐藏账号、克隆账号

+ 检查方法：lusrmgr.msc
+ 发现隐藏账号：hack887$，只是普通账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDE75eEibSpRchnbqhIoa2rSnvIVb56mTfvfITjVYl9fj4RibZdibHiczhE7JT9JvBDgZnkaguz2ggefE4YhNdNnzxOXPwkvwbcCZg/640?wx_fmt=png&from=appmsg)

* 查看系统日志：

+ 检查方法：eventvwr.msc
+ 系统日志：记录操作系统组件产生的事件，主要包括驱动程序、系统组件和应用软件的崩溃以及数据丢失错误等。系统日志中记录的时间类型由Windows NT/2000操作系统预先定义
+ 应用程序日志：包含由应用程序或系统程序记录的事件，主要记录程序运行方面的事件，例如数据库程序可以在应用程序日志中记录文件错误，程序开发人员可以自行决定监视哪些事件。如果某个应用程序出现崩溃情况，那么我们可以从程序事件日志中找到相应的记录，也许会有助于你解决问题
+ 安全日志：记录系统的安全审计事件，包含各种类型的登录日志、对象访问日志、进程追踪日志、特权使用、账号管理、策略变更、系统事件。安全日志也是调查取证中最常用到的日志。默认设置下，安全性日志是关闭的，管理员可以使用组策略来启动安全性日志，或者在注册表中设置审核策略，以便当安全性日志满后使系统停止响应

| 事件ID | 说明 |
| --- | --- |
| 4624 | 登录成功 |
| 4625 | 登录失败 |
| 4634 | 注销成功 |
| 4647 | 用户启动的注销 |
| 4672 | 使用超级用户（如管理员）进行登录 |
| 4720 | 创建用户 |

| 登录类型 | 描述 | 说明 |
| --- | --- | --- |
| 2 | 交互式登录（Interactive） | 用户在本地进行登录。 |
| 3 | 网络（Network） | 最常见的情况就是连接到共享文件夹或共享打印机时。 |
| 4 | 批处理（Batch） | 通常表明某计划任务启动。 |
| 5 | 服务（Service） | 每种服务都被配置在某个特定的用户账号下运行。 |
| 7 | 解锁（Unlock） | 屏保解锁。 |
| 8 | 网络明文（NetworkCleartext） | 登录的密码在网络上是通过明文传输的，如FTP。 |
| 9 | 新凭证（NewCredentials） | 使用带/Netonly参数的RUNAS命令运行一个程序。 |
| 10 | 远程交互，（RemoteInteractive） | 通过终端服务、远程桌面或远程协助访问计算机。 |
| 11 | 缓存交互（CachedInteractive） | 以一个域用户登录而又没有域控制器可用 |

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBZvgfxXyY5DYDzdYSQc3hCBwQibEjXRicRA6kPXbsiahicacBBKhT9o3MY4brHyK9icICUBkhr7AELkBdoSy5gHuODCicMBWBqlamUY/640?wx_fmt=png&from=appmsg)

* 已知：攻击者第一次上传system.php文件到服务器根目录的时间是：2024.02.29 13:07:58，我们只需要看这个时间之后的日志即可

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBwLGLGVKol6NXr0sZObicGq5InkjB6Kl3Q91ZibQyy2xeY6FhA2wicgDcb6jcFzPE7NR1Dq6WF9sUNfYK2oJMwbiabRQZSnsrzmxE/640?wx_fmt=png&from=appmsg)

* 系统日志：

+ 2024.02.29 13:27:11：创建hack887$用户
+ 2024.02.29 13:28:45：使用超级用户（hack887$）进行登录
+ 2024.02.29 13:28:45：hack887$用户登录成功并注销

疑问：之前hack887$看的是普通用户，为什么这里使用超级用户可以登录？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAFictglEuibuv4BVnMF4oDu9EMFN7UiaHic5TZSzb0Miady1G7xkdMyvAGEWguECMa4MKMd9BH1fCXICLboClQCXEBCaQicfWSKnPFI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBXZibopJCKktG5tRt4029U0EVmYLJib16lTFmShlFEU4YtvjXibTpgopJWOY3GeFic4xIG5yaZFNGEJegqkpC4sVJOLu11jXGwJkE/640?wx_fmt=png&from=appmsg)

如果是克隆账号，键值应该是一样的，可是这里不一样

使用D盾看，确实是克隆账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBHoYtoCaXibW1FyqMCd287sOFtZLa38bSSuThgLzEzH608oCjwlLLSz49J1vpIyR8oHEddlhOC3sobictAic6hlQU0XS43n1mDyc/640?wx_fmt=png&from=appmsg)

* 检查端口连接情况、是否有远程连接、可疑连接

+ 检查方法：

- netstat -ano 查看目前的网络连接，定位可疑的ESTABLISHED
- 根据netstat 定位出的pid，再通过tasklist命令进行进程定位 tasklist | findstr “PID”
- 只有LISTENING

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDicofzY3pZdNa7OkUicEdBxaRqDanhvTwuaxDJmsVJBgtIx9CDUqg20lM7HubL31fn7STqsCTrwcbIlrwDkbWeNicojzmzQI1qibE/640?wx_fmt=png&from=appmsg)

* 检查进程：

+ 检查方法：msinfo32，依次点击“软件环境→正在运行任务”就可以查看到进程的详细信息，比如进程路径、进程ID、文件创建日期、启动时间等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCXssDQbZl455nqh0ozocSFj4ialse4Ziav0UW9vJKDK9qbQUW3I4DqI3dGp047CLOIhcFv2jibFDNicvZKR7s1ddoUZNx57wLa0Ec/640?wx_fmt=png&from=appmsg)

+ 可观察以下内容：

- 没有签名验证信息的进程

- 没有描述信息的进程

- 进程的属主

- 进程的路径是否合法

- CPU或内存资源占用长时间过高的进程

* 小技巧：

+ 查看端口对应的PID： netstat -ano | findstr “port”

+ 查看进程对应的PID：任务管理器--查看--选择列--PID 或者 tasklist | findstr “PID”

+ 查看进程对应的程序位置：

- 任务管理器--选择对应进程--右键打开文件位置

- 运行输入 wmic，cmd界面 输入 process

+ tasklist /svc 进程--PID--服务

+ 查看Windows服务所对应的端口： %system%/system32/drivers/etc/services（一般%system%就是C:\Windows）

* 检查启动项：

+ 检查方法：

- 用户级目录：C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup    默认情况下此目录在是一个空目录，确认是否有非业务程序在该目录下

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDHG7IpGostNahtJY88m2ExApQ32fCguEpz6ZUkMw5uWdCibPPCuCFOA35t2dfhBrIWX8IoPrBZoLEI7Wf5SkdfGoaYJ9MDuq68/640?wx_fmt=png&from...