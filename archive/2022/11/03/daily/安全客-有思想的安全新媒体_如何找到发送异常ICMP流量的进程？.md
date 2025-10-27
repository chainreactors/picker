---
title: 如何找到发送异常ICMP流量的进程？
url: https://www.anquanke.com/post/id/281835
source: 安全客-有思想的安全新媒体
date: 2022-11-03
fetch_date: 2025-10-03T21:36:14.053839
---

# 如何找到发送异常ICMP流量的进程？

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

# 如何找到发送异常ICMP流量的进程？

阅读量**223252**

发布时间 : 2022-11-02 10:30:50

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 引言

目前，在高级攻防对抗中，后门隐藏和通信流量隐藏一直是重点关注的焦点之一。
近年来HW中，时常遇到利用诸如Pingtunnel隧道工具进行流量隐藏的场景。虽然网络层设备能够捕获并识别异常ICMP流量，但是无法在主机找到目标进程。wireshark等抓包工具也无法建立进程与流量的对应关系。常见的网络连接查看命令和工具也无法对ICMP流量进行展示和标记。
本文主要介绍主机层（Windows和Linux）对发送ICMP异常流量的进程的捕获方法。

## Windows下

### 原理

Windows下ICMP请求与DNS类似，都是托管给系统进程svchost，依赖服务：

![]()

既然是进程托管，就一定会涉及到进程间通信，而Windows下进程通信又以本地调用机制为主。我们可以利用调用捕获工具，配合wireshark等抓包工具，得到ICMP流量与进程的对应关系。
Windows本地调用（LPC，Local Procedure Call）简单介绍，通常也被称为轻量过程调用或者本地进程间通信，是一种由Windows NT内核提供的内部进程间通信方式。通过这一方式，同一计算机上的进程可以进行轻量的通信。在Windows Vista中及以后，ALPC（Advanced Local Procedure Call，高级本地进程通信）替代了LPC。ALPC十分复杂，还被非常多的应用所使用，如RPC、WMI、COM组件、打印机等。即使最简单的windows程序都会有ALPC连接。可以用ProcessExplorer查看每个进程的ALPC Port的名字。例如：

![]()

#### 实战

本地调用捕获工具推荐使用开源工具AlpcLogger（[https://github.com/zodiacon/ALPCLogger）](https://github.com/zodiacon/ALPCLogger%EF%BC%89)
运行AlpcLogger和wireshark，前者负责监控谁对nsi服务宿主进程svchost发送调用，后者监控ICMP流量，然后以时间为纽带，关联到一起。我们以ping为例，捕获效果如图：

![]()

从图上可以看到，wireshark捕获到，在时间8:42:03.689，产生了对72.246.162.233的ICMP流量，而在AlpcLogger捕获结果中可以看到，在同一时刻，ping向nsi服务宿主进程svchost发送了调用。因此，我们确认ping进程产生了本次的ICMP流量。
当然，由于二次对应的关系，有时候可能出现偏差，但是默认情况下，windows下对nsi服务调用的程序不多，在时间维度上不会很密集，同样，正常的ICMP流量也不会大量出现，因此，可参考性、可信任性还是很高。

## Linux下

### 原理

由于Linux下不存在Windows那种托管机制，ICMP流量由本进程驱动发送，所以捕获起来更加容易且可信度高。
在Linux下实时捕获ICMP流量我们要用到基于Kprobe的内核调用调试机制。
这里推荐工具是Systemtap。
Systemtap 是利用Kprobe 提供的API来实现动态地监控和跟踪运行中的Linux内核的工具，相比Kprobe其他工具，systemtap更加简单，提供给用户简单的命令行接口，以及编写内核指令的脚本语言。对于开发人员，systemtap是一款难得的工具。
SystemTap 的工作原理是将脚本翻译成C语言，执行C编译器创建一个内核模块。当模块被加载后，通过挂载到内核来激活所有的探测事件。然后，当事件发生再任何处理器上时，编译后的处理程序就运行，最终，SystemTap会话停止，Hook取消，内核模块被移除，整个过程由命令行程序stap驱动。

![]()

### 实战

以CentOS6.x为例。查看内核版本，并下载与内核版本完全一致调试依赖包（可以google搜索下载）：
**kernel-debuginfo
kernel-debuginfo-common
kernel-devel**

![]()

然后手动安装上述三个包：

```
rpm -ivh kernel-debuginfo-common-x86_64-2.6.32-642.el6.x86_64.rpm
rpm -ivh kernel-debuginfo-2.6.32-642.el6.x86_64.rpm
rpm -ivh kernel-devel-2.6.32-642.el6.x86_64.rpm
```

安装systemtap：

```
yum install -y systemtap systemtap-runtime
```

使用stap -V测试没问题就开始编写用于监控ICMP流量的脚本了：

```
#! /usr/bin/env stap
probe netfilter.ip.local_out {
    if (0 == dport)
        printf("%s[PID:%d,TID:%d] sent %d to %s:%d\n", execname(), pid(),  tid(),length, daddr, dport)
}
probe netfilter.ip.local_in {
    if (0 == sport)
        printf("%s recv %d from %s:%d\n", execname(),length, saddr, sport)
}
```

（Systemtap脚本编写参考： [https://sourceware.org/systemtap/tutorial/）](https://sourceware.org/systemtap/tutorial/%EF%BC%89)
上述解释：监控netfilter.ip.local\_out、netfilter.ip.local\_in的调用，ICMP的目标端口为0，同时打印进程名、pid、tid、发送和接受的字节数（字节数是确认ICMP流量是否异常的关键指标）。
以ping为例效果如下：

![]()

## 相关参考

debuginfo下载
<https://mirrors.ocf.berkeley.edu/centos-debuginfo/>
<https://oss.oracle.com/el6/debuginfo/>
<http://debuginfo.centos.org/6/x86_64/>

kernel-devel下载
ftp://ftp.pbone.net/mirror/ftp.scientificlinux.org/linux/scientific/
<https://www.central.org/dl/linuxdev/>

systemtap 官方教程
<https://sourceware.org/systemtap/tutorial/1_Introduction.html>
《SystemTap: Instrumenting the Linux Kernel for Analyzing Performance and Functional Problems》
<https://www.redbooks.ibm.com/redpapers/pdfs/redp4469.pdf>

systemtap 内置函数库（tapset）
<https://sourceware.org/systemtap/tapsets/index.html>

Linux 系统动态追踪技术介绍
<https://blog.arstercz.com/introduction_to_linux_dynamic_tracing/>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**绿盟科技CERT**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/281835](/post/id/281835)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [APC](/tag/APC)
* [ICMP异常流量](/tag/ICMP%E5%BC%82%E5%B8%B8%E6%B5%81%E9%87%8F)
* [Systemtap](/tag/Systemtap)
* [AlpcLogger](/tag/AlpcLogger)
* [Pingtunnel](/tag/Pingtunnel)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t01efdaabad3236b679.png)绿盟科技CERT

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t01efdaabad3236b679.png)](/member.html?memberId=167503)

[绿盟科技CERT](/member.html?memberId=167503)

绿盟科技应急响应中心（NSCERT）

* 文章
* **1**

* 粉丝
* **0**

### TA的文章

* ##### [如何找到发送异常ICMP流量的进程？](/post/id/281835)

  2022-11-02 10:30:50

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47

### 热门推荐

文章目录

* [引言](#h2-0)
* [Windows下](#h2-1)
  + [原理](#h3-2)
* [Linux下](#h2-3)
  + [原理](#h3-4)
  + [实战](#h3-5)
* [相关参考](#h2-6)

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