---
title: windows应急响应
url: https://www.anquanke.com/post/id/287417
source: 安全客-有思想的安全新媒体
date: 2023-03-16
fetch_date: 2025-10-04T09:42:10.144166
---

# windows应急响应

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# windows应急响应

阅读量**416423**

|评论**1**

发布时间 : 2023-03-15 15:30:13

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 分析排查介绍

分析排查是指对windows系统中的文件、进程、系统信息、日志记录等进行检查。查看windows系统中是否有运行异常的情况。主要目的在于保护windows系统的安全。

## 0x01 开机启动文件

一般情况下，被植入的木马病毒、恶意文件恶意程序等都会在计算机启动时自启动运行。

在windows中可通过以下三种方式查看开机启动项：

1.利用操作系统中的启动菜单

```
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup
```

![]()

2.利用系统配置msconfig

![]()

![]()

3.利用注册表regedit

```
计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

![]()

```
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
```

![]()

## 0x02 temp临时异常文件

temp临时文件夹，位于C:\Document and Settings\Administrator\Local Settings\内。很多文件放在这里，用来收藏夹，浏览网页的临时文件，编辑文件等。

在运行输入%temp%可直接打开temp文件夹。

![]()

![]()

排查对象：查看temp文件夹PE文件（exe、dll、sys），或者是否具有特别大的tmp文件。

相关可疑文件可上传到云沙箱进行在线分析。

<https://www.virustotal.com/gui/home/upload>

<https://x.threatbook.com/>

<https://ti.360.cn/#/homepage>

为什么要排查Temp文件夹？

使用Temp文件夹有几个优点。在某些系统中，Temp文件夹位于RAM DISK上。与通常的磁盘文件系统相比，写入操作和文件操作要快的很多。

另一个优点是Temp文件夹对当前登录的用户具有读写访问权限，从而解决了恶意软件安装程序在没有适当权限的情况下尝试将恶意软件安装在目标位置时出现的任何文件系统权限错误。一旦恶意软件安装程序或恶意软件本身具有升级的特权，Temp文件夹通常用作暂存点。

操作系统还具有清理Temp文件夹中临时文件的不完整写入的优点，因此在恶意软件安装失败的情况下，操作系统负责删除文件的任何痕迹，从而防止恶意软件的任何部分或版本损坏它的主要可执行文件。所以恶意软件安装程序通常在恶意软件感染期间利用TMP文件和Windows Temp文件夹。

## 0x03 浏览器分析

服务器被攻击者拿下后，攻击者可能会使用服务器的浏览器进行访问网站，进行一系列下载操作。因此我们可以查看浏览器记录，排查浏览器是否被使用下载恶意代码。

1.浏览器浏览痕迹查看

![]()

2.浏览器文件下载记录查看

3.浏览器cookie信息查看

浏览器记录查看工具：<https://launcher.nirsoft.net/downloads/index.html>

## 0x04 文件时间属性分析

在windows系统下，文件属性的时间属性具有：创建时间、修改时间、访问时间。默认系统以修改时间作为展示。

![]()

如果文件的修改时间早于创建时间这个文件存在可疑，异常的时间很有可能是攻击者进行恶意修改的不正常文件。

## 0x05 最近打开文件

Windows系统中默认记录系统中最近打开使用的文件信息。

可以在目录`C:\Documents and Settings\Administrator\Recent`下查看

![]()

也可以使用Win+R打开运行后输入`%UserProfile%\Recent`查看。然后利用Windows中的筛选条件查看具体时间范围的文件。

![]()

## 0x06 可疑进程发现与关闭

计算机与外部忘了通信是建立在TCP/UDP协议上的，并且每一次通信都是具有不同的端口（0-65535）。在计算机中木马病毒后，木马运行会与外部忘了进行通信，那么就可以通过查看忘了连接状态，找到对应的进程ID，然后关闭进程ID进行断开木马的通信连接。

使用如下相关命令进行排查：

```
netstat -ano | find "ESTABLISHED"  查看网络建立连接的状态
tasklist /svc | find "PID" 查看具体PID进程对应的程序
taskkill /PID xxx /T 关闭进程
```

![]()

![]()

## Windows分析排查-系统信息排查

### 0x01 异常计划任务排查

在计算机中可以通过设定计划任务，在固定时间执行固定操作。一般情况下，攻击者设定计划任务在固定时间设置执行恶意代码，以达到隐蔽实现攻击的效果。

在使用schtasks命令可以对计划任务进行管理，直接输入schtasks可以查看当前计算机中保存的计划任务。

![]()

使用任务管理器查看当前计算机中的计划任务，在开始菜单找到“计划任务程序”进行打开。

![]()

通过对相关的可疑计划任务进行排查，如发现相关运行程序可疑时，可根据文件路径找到程序使用云沙箱进行在线分析。

<https://www.virustotal.com/gui/home/upload>

<https://x.threatbook.com/>

<https://ti.360.cn/#/homepage>

### 0x02 隐藏账户发现与删除

隐藏账户是指攻击者入侵服务器后威朗能够持久保持对计算机的访问，在计算机系统中建立的不易被发现的计算机账户。

隐藏账户建立命令：

`net user test$ test /add && net localgroup administrator test$ /add`其中$符号可以导致系统管理员在使用net user时无法查看到test$用户。

![]()

![]()

检查注册表`计算机\HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\Names`中是否有隐藏的账户，通过注册表进行建立的隐藏账户无法在计算机管理中进行查看，隐蔽性极高。在排查隐藏账户时可进行查看是否有相关可疑账户。发现确认可疑账户可右击进行删除。

![]()

### 0x03 恶意进程发现与关闭

恶意代码在windows系统中运行过程中，将以进程的方式进行展示。其中恶意进程执行这各种恶意行为。对于可执行程序，可能直接使用杀毒软件进行查杀，但是并非所有的恶意程序都能被查杀。也可手动进行查杀，使用工具psexplore，然后利用在线云沙箱等进行检测分析。对恶意程序相关服务进行关闭。

### 0x04 补丁查看与更新

windows系统支持补丁以修复漏洞。可以使用systeminfo查看系统信息，并展示对应的系统补丁信息编号。也可以在卸载软件中查看系统补丁和第三方软件补丁。

![]()

在win10中使用快捷键win+i，然后选择Windows更新。他版本的Windows也具有Windows Update相关选项，可以进行更新操作。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Tide安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287417](/post/id/287417)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [应急响应](/tag/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)Tide安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)](/member.html?memberId=142933)

[Tide安全团队](/member.html?memberId=142933)

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，目前聚集了十多位专业的安全攻防技术研究人员，专注于网络攻防、Web安全、移动终端、安全开发、IoT/物联网/工控安全等方向。

* 文章
* **83**

* 粉丝
* **71**

### TA的文章

* ##### [windows应急响应](/post/id/287417)

  2023-03-15 15:30:13
* ##### [初识内存取证-volatility与Easy\_dump](/post/id/287019)

  2023-03-08 14:30:12
* ##### [车联网安全入门之从CAN模拟环境搭建到重放攻击](/post/id/287021)

  2023-03-06 15:30:43
* ##### [Pwn入门之ret2libc详解](/post/id/286999)

  2023-03-06 10:30:35
* ##### [Windows Defender的一些渗透知识](/post/id/285521)

  2023-01-18 10:30:41

### 相关文章

* ##### [如何在终端上定位发起恶意请求的进程？](/post/id/287604)

  2023-03-21 10:30:15
* ##### [应急响应不“摇人”，好的EDR做对了哪些事？](/post/id/286737)

  2023-02-27 14:00:57
* ##### [年度盘点 | 安全范儿技术沙龙的八期干货都在这里！](/post/id/285399)

  2023-01-12 15:30:27
* ##### [记一次DarkKomet synaptics 病毒应急响应事件](/post/id/283990)

  2022-12-02 16:00:49
* ##### [应急事件检测 入门篇-Linux信息检测](/post/id/264087)

  2021-12-30 15:30:41
* ##### [应急事件检测 入门篇-windows信息检测](/post/id/261348)

  2021-12-08 10:30:36
* ##### [应急响应入门篇-应急响应流程及数据保护](/post/id/260061)

  2021-12-02 10:30:31

### 热门推荐

文章目录

* [分析排查介绍](#h2-0)
* [0x01 开机启动文件](#h2-1)
* [0x02 temp临时异常文件](#h2-2)
* [0x03 浏览器分析](#h2-3)
* [0x04 文件时间属性分析](#h2-4)
* [0x05 最近打开文件](#h2-5)
* [0x06 可疑进程发现与关闭](#h2-6)
* [Windows分析排查-系统信息排查](#h2-7)
  + [0x01 异常计划任务排查](#h3-8)
  + [0x02 隐藏账户发现与删除](#h3-9)
  + [0x03 恶意进程发现与关闭](#h3-10)
  + [0x04 补丁查看与更新](#h3-11)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)