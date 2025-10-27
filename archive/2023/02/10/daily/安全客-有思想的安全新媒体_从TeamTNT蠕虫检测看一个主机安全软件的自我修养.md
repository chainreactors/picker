---
title: 从TeamTNT蠕虫检测看一个主机安全软件的自我修养
url: https://www.anquanke.com/post/id/286192
source: 安全客-有思想的安全新媒体
date: 2023-02-10
fetch_date: 2025-10-04T06:12:09.731854
---

# 从TeamTNT蠕虫检测看一个主机安全软件的自我修养

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

# 从TeamTNT蠕虫检测看一个主机安全软件的自我修养

阅读量**317885**

发布时间 : 2023-02-09 10:30:27

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 背景

近日，牧云（CloudWalker） 主机安全管理平台帮助用户检测并协助处置一起TeamTNT蠕虫感染事件，事后复盘该蠕虫使用了多种攻击逃逸技术进行自身的隐藏。本文主要结合实际的蠕虫事件介绍主机安全软件的对抗手段，从而阐述主机安全软件如何自我修炼，从而可以有效地应对持续迭代更新的恶意软件及其逃逸手段。

## 事件概述

事件的起源是一起异常网络连接告警引发的应急响应。

![]()

发现告警之后，上机排查发现并没有看到相应的进程，判断可能存在进程隐藏等对抗行为。利用牧云的安全基线进行分析，果然发现有两个rootkit。

通过加载LKM模块实现进程隐藏和rootkit自身的隐藏。

![]()

通过ld.so.preload在用户态实现进程隐藏。

![]()

参考牧云的解决方案对rootkit进行清理后，所有的后门进程都无所遁形，根据指引完成后门清理成功结束应急响应。

下文将继续结合这个典型的蠕虫来阐述牧云是如何有效和其对抗的技术实现。

## 主机安全的自我修养

### 健壮的感知能力

本次感染的蠕虫虽然通过各种手段实现进程的隐藏进行逃逸，但牧云仍能够有效的发现其异常网络连接，核心是通过tracing+kprobe实现有效的主机事件采集。

kprobe是Linux内核提供的一种动态调试机制，即Kernel Probe，用于收集内核函数运行时信息分析和监测内核函数的执行。相较于用户态通过hook libc的方式采集系统调用信息，kprobe直接在内核态进行监听，无论是采集率和对抗rootkit隐藏逃逸都更具优势。

相较于另一种在内核hook系统调用的方式进行事件采集，kprobe作为内核原生提供的调试机制具有更好的稳定性，这对主机安全软件也是至关重要的一环。而相较于内核新引入的ebpf等方式，在内核版本2.6.9即引入的kprobe无疑具有更广泛的普适性。

那么如何通过tracing+kprobe实现网络连接事件的采集，下面我们通过linux提供的ftrace框架，操作/sys/kernel/debug/tracing/文件系统来简单分享一下kprobe事件采集的实现。

针对TeamTNT蠕虫异常网络连接监控举例，首先我们需要通过ftrace注册一个kprobe监听事件，并针对监听的函数的ABI约定来选择需要采集的数据。因为是监听建立网络连接，我们选择\_\_sys\_connect系统调用，通过如下命令我们可以注册一个名为justtest的kprobe监听事件。

`echo -n 'p:justtest __sys_connect FD=%di:s64 Family=+0(%si):u16 Port=+2(%si):u16 Address=+4(%si):u32 Len=%dx:u64' >> /sys/kernel/debug/tracing/kprobe_events`

接下来，我们需要启用我们所注册的kprobe监听器，具体实现仍然是操作tracing文件系统，相应命令如下。

`echo 1 > /sys/kernel/debug/tracing/events/kprobes/justtest/enable`

最后我们就可以通过解析/sys/kernel/debug/tracing/trace对应的输出，分析是否有可疑的网络连接请求。

![]()

针对kprobe的更详细的参数以及调用方式可以查看内核的Documentation/trace/kprobetrace.txt文档了解细节。同时牧云也将其核心的事件采集能力开源成工具供大家尝试调试kprobe事件采集，以及可以结合systracer程序进行恶意软件分析，详情见开源项目 <https://github.com/chaitin/systracer> 。

### 深度的洞察能力

作为一个优雅的主机安全产品牧云兼具深度的洞察能力，在TeamTNT蠕虫事件中，牧云通过用户态工具对内核的内存分布进行深度的洞察，从而有效检出蠕虫使用LKM rootkit，下面我们详细阐述牧云是如何洞察rootkit隐藏痕迹。

对LKM rootkit的发现，牧云是基于对比内核中/proc/kallsyms符号表和内核的内存镜像/proc/kcore从而发现系统调用被异常篡改，最终实现威胁检出。

首先我们需要分析kcore来查找系统调用的地址，首先我们通过readelf获取kcore中内核代码的偏移地址。通过读取代码段的偏移地址，其中VirtAddr-Offset即为内核态逻辑内存地址映射到/proc/kcore文件中的偏移位置。

![]()

然后通过kallsyms获取系统调用表的偏移地址
`# grep 'R sys_call_table' /proc/kallsyms
ffffffffbc2013c0 R sys_call_table`

基于上面获取的信息，可以计算出在kcore中系统调用表的偏移地址为

0xffffffffbc2013c0-(0xffffffffff600000-0x00007fffff603000)=0x7fffbc2043c0，通过hexdump来读取系统调用表的内存地址为一个平坦数组，我们可以通过系统调用号作为下标直接获取对应系统调用的跳转地址。

`# hexdump -s 0x7FFFBC2043C0+ -n 64 -e '2/4 "%08x" "\n"' /proc/kcore
bb4d2d60ffffffff
bb4d2e80ffffffff
bb4cea30ffffffff
bb4ccae0ffffffff
bb4d7ec0ffffffff
bb4d80e0ffffffff
bb4d7f80ffffffff
bb4ebef0ffffffff`

最后我们将kcore中获取的系统调用地址和kallsyms中的符号地址进行对比，可以看到sys\_kill系统调用存在异常。后续我们可以进一步基于内存异常找到对应进行系统调用劫持的内核模块，在这里就不详细阐述了。

![]()

从上面蠕虫逃逸的对抗过程可以看出，作为一款主机安全软件，面对不断升级和迭代的恶意软件，健壮的感知能力和深度的洞察能力是我们能够持续检测的基础和自我修养。

## IOC

#### IP

220.167.141.174
205.185.118.246

#### URL

hxxp://205.185.118.246/b2f628/cronb.sh
hxxp://kiss.a-dog.top/b2f628/m/xm.jpg
hxxp://kiss.a-dog.top/s3f815/d/h.sh
hxxp://kiss.a-dog.top/s3f815/d/w.sh
hxxp://kiss.a-dog.top/s3f815/d/d.sh
hxxp://kiss.a-dog.top/s3f815/d/c.sh
hxxp://kiss.a-dog.top/bWVkaWEK/zgrab
hxxp://kiss.a-dog.top/bWVkaWEK/1.0.4.tar.gz
hxxp://kiss.a-dog.top/b2f628/m/xm.tar
hxxp://kiss.a-dog.top/b2f628/d/ai.sh
hxxp://kiss.a-dog.top/b2f628/d/ar.sh
hxxp://kiss.a-dog.top/b2f628/b.sh
hxxp://kiss.a-dog.top/b2f628/s/s.sh

#### MD5

b66fe14854d5c569a79f7b3df93d3191
7691c55732fded10fca0d6ccc64e41dc
8fbbe3860823e397f3be82fa78026238
ded99b45dd74384689b276b1b35bce64
1e2bb44cd88e4763db54993638472f62
974edee6a70b66eac6de05045e542715

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**长亭科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286192](/post/id/286192)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**1赞

收藏

![](https://p4.ssl.qhimg.com/t012a2b2cc9165a693a.jpg)长亭科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t01771e47b7b4fab146.png)

[![](https://p4.ssl.qhimg.com/t012a2b2cc9165a693a.jpg)](/member.html?memberId=122590)

[长亭科技](/member.html?memberId=122590)

Smart Makes Security

* 文章
* **118**

* 粉丝
* **116**

### TA的文章

* ##### [硬核技术 | 长亭智能推测嵌套编码，百倍提升检测效率](/post/id/288070)

  2023-04-03 17:30:41
* ##### [钟馗捉鬼 | 长亭万象（COSMOS）安全运营操作实录](/post/id/287068)

  2023-03-06 14:34:57
* ##### [2000亿！单日检测流量，长亭WAF花式演绎](/post/id/286756)

  2023-02-27 14:31:40
* ##### [放羊式管理云主机：一款面向技术爱好者的远程主机管理助手](/post/id/286534)

  2023-02-22 16:30:34
* ##### [三项全能！长亭科技获通信网络安全服务认证](/post/id/286529)

  2023-02-21 15:06:00

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

### 热门推荐

文章目录

* [背景](#h2-0)
* [事件概述](#h2-1)
* [主机安全的自我修养](#h2-2)
  + [健壮的感知能力](#h3-3)
  + [深度的洞察能力](#h3-4)
* [IOC](#h2-5)

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