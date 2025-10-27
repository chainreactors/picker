---
title: Windows应急分析工具-HawkEye v2（GUI）
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247490424&idx=1&sn=257b5f4aa5a05e810bbff30bc3fa43e4&chksm=fad4c66fcda34f79a601e9d1b69386755ff4f0fe699ea62d249d09e92351eb27c263bc2b71a8&scene=58&subscene=0#rd
source: NOVASEC
date: 2025-02-25
fetch_date: 2025-10-06T20:38:22.226278
---

# Windows应急分析工具-HawkEye v2（GUI）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysnJw8Uic9ay9dibEzP1xgbicGe9pvWJMxsBa1sRHtzMoX6Mibd0g1hKaBxw/0?wx_fmt=jpeg)

# Windows应急分析工具-HawkEye v2（GUI）

爱做梦的大米饭

NOVASEC

## 前言

在25年年初，在公众号上以及Github发布了个人编写的Windows应急响应工具，github地址：https://github.com/mir1ce/Hawkeye，感谢捧场，目前已经收获117star。起初写这个工具的主要目的还是发现比较好的应急响应工具比较少，要么就是一大堆文件需要上传，有时候就比较麻烦。同时在分析Windows日志的时候，有的事件id和类型记起来确实挺头疼的，每次翻阅笔记也麻烦，更别说使用微软官方提供的工具了，一堆类似sql的语法，敲起来就比较烦。如果查询一个4624的日志，敲都敲好久。

同时在日常应急过程中，大部分场景除了找文件外，那么基本都是和日志分析、进程，C2外连以及权限维持打交道。就想着有没有一个能够覆盖绝大部分场景的工具，但是都没找到满意的，要么文件太大，要么不是特别全面或者使用起来各种命令行，作为一个懒人，还是想着怎么方便怎么来。那么就想着自己写一个，目前包含了进程查看(DLL模块加载、进程数查看、文件定位)、外连分析、主机信息、日志分析、以及yara内存扫描。目前按照个人的想法，这个应该是能够覆盖大多数场景了。那么Windows rootkit就不在考虑范围了，因为go应该是不能进入r0层去做检测的，那么rootkit这块儿就不做了（主要还是我菜，哈哈哈哈）。

当前HawkEye已经更新到V2版本，按照我个人的看法来看，大部分场景都能覆盖了。如果有好玩的想法，在应用层能实现的，可以在github issue提交，后面根据个人实际情况去实现。或者是关注微信公众号，后台留言，我也会去看。

目前我给这个工具的总结是，文件小巧，分析面多，哈哈哈哈。但是由于使用upx把程序压缩至4MB的大小，杀毒软件可能会查杀，那么本次在github上传的就包含了upx版本和无upx版本。希望各位下载后不会报毒，毕竟是go写的，里面还带了很多规则，难免会被查杀。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysE21OqQJZeGLhFeOgSzFicBwVOELbIqQpzeBHiaItXZH0gQgRicCyBQujg/640?wx_fmt=png&from=appmsg)

## 运行环境

当前支持Windows 7以上系统。以Windows server 2019 2G内存，2处理器为例，也在此性能情况下也能正常运行

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXyst2SgxiaFCEVPb0xSPiaYRorhOmkb1rvjQVq7YbJPFCa8uSv1OT4I6xaQ/640?wx_fmt=png&from=appmsg)
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys2aIHfNgPNsfgVb3ShrZqwwy4YJq17icAtU6MoCvsxPL3c9uIneibzUsg/640?wx_fmt=png&from=appmsg)

## 新增功能

本次版本更新如下：

1、Windows进程分析

2、进程加载DLL分析

3、yara进程扫描

## 功能介绍

### 进程分析

V2版本中新增进程分析，该功能能够获取到当前系统的所有进程，并将进程的相关信息展示到GUI界面，如进程的创建时间，文件创建时间，MD5值，以及是否存在签名信息。![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysQkQXibDbFkQHvQj4gwcwI2EuCuDZR2HV4BEo8uic6mb1ptWCneUDiaiaiaw/640?wx_fmt=png&from=appmsg) 并且在进程分析界面添加右键进行功能选择，方便应急响应工程师或者是安全分析工程师能够按照自己的需求展开相关工作。具体详情如下：

终止进程：用户可以根据右键选择相关进程信息终止当前进程；

复制：该功能主要是复制当前进程的所有信息，复制下来后，如下所示，方便安全工程师在编写报告时及时获取数据;

PID: 1112

进程名称: svchost.exe

创建时间: 2025-02-20 14:20:11

可执行文件路径: C:\Windows\System32\svchost.exe

文件创建时间: 2024-09-06 12:12:53

可执行文件MD5: 0cd128f416a04c06d50ec56392c25d9f

同理，复制PID、复制进程名称以及复制可执行文件MD5值，都是复制进程的相关信息

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXyseCYdf2DzV0uT94YmJ4KKtMyKice9Stv5eZnzrzbWicgv4N1QlL00r6Ng/640?wx_fmt=png&from=appmsg)

查看进程树，当前仅支持查看到他的父父进程相关信息以及其子进程相关信息，如下所示

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysiaZEJwufLykZG0vOyiaEXyNvloxiaFrcg1WbGuhXFZQHxSrynSfpW5B1w/640?wx_fmt=png&from=appmsg)

在资源管理器中打开同样旨在方便安全工程师快速的跳转到指定的文件资源所在位置。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys2slqBZQI65h11o7k0ojEicAsrALcC2kdqgjfe8uRlo4bdACISp1wdAA/640?wx_fmt=png&from=appmsg)

同时进程分析模块，采用调用Windows API的功能，解析进程加载的模块信息。并获取相关文件的MD5值，可执行文件路径，以及是否存在嵌入式签名信息，方便安全工程师查看进程加载的模块是否存在问题。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysm7noD5ibRamibF6ib8Dy9SB3OAsZX0yfZxEPvgpdVj2ydhvQPcdvicGLpA/640?wx_fmt=png&from=appmsg)

为了方便用户及时获取信息，在程序界面上方，添加了程序刷新模块，更新进程信息。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysB4ehib65QdxibsyDKRMiabNZDP8FCdgDLO0RdvTS7vvABAmIgl3xUwraw/640?wx_fmt=png&from=appmsg)

同时为了检索到用户，也添加了输入框，方便用户进行检索。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysV8Tz5kUqopKfRmmvFMnuDhFibBCjfeVv4jEicAMYH0jdiblNd0ticCKN4g/640?wx_fmt=png&from=appmsg)

### 外连分析

外连分析从v1版本就存在，旨在帮助用户在挖矿场景，或者是异常外连场景能够及时的分析是哪个进程在外连，并且自动化分析出他存在的常见权限维持项目(小白也能快速上手)

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysYg1rAEbN7y7uVzr3kgbYDdXyHsiaSPtjZaleqddCevPJF9uiaJFA6zog/640?wx_fmt=png&from=appmsg)

### Beacon扫描

这里引入了EvilEye该项目，用来在攻防场景下检测是否存在C2外连进程，当然新版本更新里可以使用另外一个功能进行检测（后面再介绍）

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysB4Fe0alUEvjCZ7mKlgFSmibGmGF7NicvPRGfB6LflMF8jbRP0kKUS41g/640?wx_fmt=png&from=appmsg)

### 主机信息

该功能能够查看常见的主机信息，具体如下：

* 用户信息 能够查看当前主机用户，以及主机是否存在隐藏账号

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys0yblp8ousARRDQWuMo3Mk66e0Oy0Y6BsKWa7uqoymWNvvZCNSxS1Xg/640?wx_fmt=png&from=appmsg)

* 计划任务 查看当前主机的计划任务以及触发时间，并且会检测计划任务的可执行文件是否存在签名。方便用户发现异常的计划任务

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys150VhDr2fibZtm2JshWr4IGIXfrYXMKv3edrTko8f1RpdK8JqmgWlYA/640?wx_fmt=png&from=appmsg)

* 同样，服务信息也对签名信息做了校验。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXyswXAiaeGHSic81kz5zanKRxCqM6CdZ97YrVZElSQvgpibvLbBH7EcLRHDw/640?wx_fmt=png&from=appmsg)

* 启动项信息

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys6uicqZPNUQhTBXOMchIdKvvjHZ49BhWdNtVLcnHtPHvXlVpsInHgCog/640?wx_fmt=png&from=appmsg)

### 日志分析

‍

#### 网络登录日志

网络登录日志，hawkeye也支持显示，如果用户主机登录成功的话，那么这里就会在GUI界面显示登录事件，登录类型以及登录的源IP

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys9Yibbic2YX9UvxLh1dKiaKByIrc4p68I9tOUhOUx2wWu0QlLib1hMGiaH0A/640?wx_fmt=png&from=appmsg)

如果登录失败，那么这里也会显示出来

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys5hPdbqGKEdkPJfrpxzV8YxFolHW1ZvXPw7u38KDdnCicLoNvOZclaKA/640?wx_fmt=png&from=appmsg)

#### RDP登录以及连接日志

RDP日志，通过调用Windows API的方式，根据应急响应经验总结出需要查看的日志信息，并显示在GUI界面。在面临勒索病毒，或者是内网横向攻击时，攻击者可能使用RDP展开横向攻击，那么在此场景下就能够很好的去分析相关事件了。

![image12](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXyscDyzSB5JxjasnX4ZE1WBmxtiboTuu3bLuZahkT6gjibBdpNqQyp1EBxg/640?wx_fmt=png&from=appmsg)

![image13](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys0ASiboeOeO9FUj6ftS6YrZGBOGXRM2DbB4ea7TxQcOHVA9dQcsqlwGQ/640?wx_fmt=png&from=appmsg)

#### 服务创建日志

一般在内网横向过程中，服务可能会使用psexec或者是smbexec.py这类工具，这类工具在横向移动时会产生一些痕迹，那么分析服务创建日志就很有必要了。

这里以smbexec为例，这里横向过去后成功登录到目标主机

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys52qnwSSicWlo4NdiaGiaAxFgx8FRUOgaRhr1RMdL5iayoz1VZoEiapcIRPg/640?wx_fmt=png&from=appmsg)

那么我们在hawkeye中查看服务创建日志就会发现，工具已经打标签进行标记，提示用户主机遭受到内网横向攻击行为

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysmdEUjDzo6jSMmhIcDz2joXvIDtia6gjMqudiaCvsjQJKj8FNeibJNB1Wg/640?wx_fmt=png&from=appmsg)

#### 用户创建日志

该日志能够帮助安全分析师查看看当前pc的用户创建信息，及时及时知道账户是否存在异常

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysxqyCAS9tGyzAVp0R1QQaj7HKqhbmeabvodZ3Eibl4GRJjHFsDsibCrMg/640?wx_fmt=png&from=appmsg)

#### SqlServer日志

在安全分析过程中，攻击者可能通过sqlserver弱口令结合MDUT等数据库利用工具，或者是SQL注入漏洞，实现命令执行的操作，那么我们就需要重点关注sqlsever数据库的登录日志，以及show advance options的操作日志，本次版本更新，新增该场景，方便工程师快速识别相关风险，并且，针对xp\_cmdshell的操作日志，进行标注，方便新手朋友快速查看存在的问题

![image14](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXyscicj2xIAM3AohOfy7u461bTavJsBjQu82kYfqgW2GFf5h7fhBKd90og/640?wx_fmt=png&from=appmsg)

#### powershell日志

攻击者利用漏洞后可能会使用powershell上线cs或者是展开更深层次的利用，该版本新增powershell日志，方便安全工程师进行分析。

![image15](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys7ds8KOibIIfI6BKAUjqRrST3crt5pBksgHAcj4dJnXoabbD2XbkHfgA/640?wx_fmt=png&from=appmsg)

### 进程扫描

当前HawkEye已经引入yara内存扫描引擎，并且内置了多个yara规则对主机内存进行扫描（规则地址：https://github.com/reversinglabs/reversinglabs-yara-rules、https://github.com/m-sec-org/d-eyes/tree/master/yaraRules），在进程扫描界面，用户可以根据自己的选择，是否使用内置yara规则，还是使用自定义规则进行扫描

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXys2B0uUnvLD5bnWOFRf08olxd9iaoHlbDNqdmic6Flem4kHs0BXgbrojng/640?wx_fmt=png&from=appmsg)

这里使用msf进行测试，我们在msf生成一个后门木马后，在受害者主机运行。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysLmv6icSmWAZCo7MCfZIO00WZxiaWY1bp41hj5rZukOEkAlLovKewS1jw/640?wx_fmt=png&from=appmsg)

那么我们在受害者主机上输入我们跳过最大内存后（我这里是超过50MB就不会扫描），输入好后，那么这里点击扫描就能够快速扫出来，扫描结果也会以日志的形式保留到本地文件夹中。
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwiaCCfXhqlFNo910CCnhicXysmib4y9tVJdDzFLeOPrJMcicf61MuIhvn5dFrrWOIfKTibna4aQ5xyhwQQ/640?wx_fmt=png&from=appmsg)

然后不适用内置规则，使用指定路径下的yara规则扫描也是可以发现msf恶意进程

![image](https://mm...