---
title: 网络入侵检测系统之suricata概要介绍
url: https://www.anquanke.com/post/id/283260
source: 安全客-有思想的安全新媒体
date: 2022-11-30
fetch_date: 2025-10-04T00:02:18.618641
---

# 网络入侵检测系统之suricata概要介绍

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

# 网络入侵检测系统之suricata概要介绍

阅读量**803432**

发布时间 : 2022-11-29 15:00:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 1.简介

Suricata是一个免费、开源、成熟、快速、健壮的网络威胁检测引擎。Suricata引擎能够进行实时入侵检测(IDS)、内联入侵预防(IPS)、网络安全监控(NSM)和离线pcap处理。Suricata使用强大而广泛的规则和签名语言来检查网络流量，并提供强大的Lua脚本支持来检测复杂的威胁。使用标准的输入和输出格式(如YAML和JSON)，使用现有的SIEMs、Splunk、Logstash/Elasticsearch、Kibana和其他数据库等工具进行集成将变得非常简单。Suricata项目和代码由开放信息安全基金会(OISF)拥有和支持，OISF是一个非盈利基金会，致力于确保Suricata作为一个开源项目的开发和持续成功。
下面将介绍一下如何搭建一个suricata平台以及一些suricata的基本信息，重点会说一下suricata的工作模式，这个涉及到数据包的处理流程

## 2.suricata安装

### 2.1 依赖库安装

yum install -y git epel-release make autoconf gcc-c++ automake cmake libtool pcre-devel libyaml-devel jansson-devel libpcap-devel file-devel zlib-devel nss-devel libcap-ng-devel libnet-devel libnetfilter\_queue-devel lua-devel epel-release lz4-devel xz-devel json-c-devel librdkafka-devel luajit-devel python-pip ragel
yum install -y rust cargo pcre2-devel
cargo install —force cbindgen
cp /root/.cargo/bin/cbindgen /usr/bin/
pip install pyyaml json-lines

### 2.2源码下载编译

1.git clone <https://github.com/OISF/suricata.git>
2.cd suricata
3.git clone [https://github.com/OISF/libhtp（下载libhtp用于http协议解析）](https://github.com/OISF/libhtp%EF%BC%88%E4%B8%8B%E8%BD%BDlibhtp%E7%94%A8%E4%BA%8Ehttp%E5%8D%8F%E8%AE%AE%E8%A7%A3%E6%9E%90%EF%BC%89)
4../autogen.sh
5.生成对应的makfile FLAGS=-g ./configure —prefix=/usr —sysconfdir=/etc —localstatedir=/var —enable-nfqueue —enable-luajit —enable-debug ( -g表示保留符号信息，程序出core时，可以运用上，—prefix用于设置安装、配置、日志目录，—enable-nfqueue用于开启nfq网卡多队列模式支持 —enable-luajit用于开启对luajit的支持 —enable-debug开启日志模式 )
6.Make && make install && make install-conf (编译，安装，以及安装规则)
安装可执行程序及相关路径:
可执行程序(/usr/bin):
suricata/suricatactl/suricatasc/suricata-update
配置相关路径：
/var/log/suricata #log相关
/etc/suricata(include:classification.config/reference.config/suricata.yaml(可配置rules路径)/threshold.config) #配置信息 协议等
/var/lib/suricata/rules #规则相关

### 2.3 运行

suricata -c /etc/suricata/suricata.yaml -i enp0s3

![]()

这里用的是最新的版本7.0,我自己的网卡是enp0s3,把这个换成自己要监听的网卡即可

## 3.suricata基本信息介绍

![]()

## 4.suricata 工作模式分析

### 4.1 single模式

![]()

single只支持一个网卡设备，只有一个work线程

### 4.2 work模式

![]()

Work工作模式，每个网卡默认对应cpu数个工作线程(或者按照配置文件配置的线程数)，每个工作线程取对应的网卡队列中数据包

### 4.3 autofp工作模式

![]()

autofp模式相对比较复杂，相当于共用了work线程

### 4.4 work线程介绍

工作模式的重点在于工作线程的处理，下面介绍一下工作线程的处理流程

数据包工作线程是按照slot的注册跑，一个slot一个走
这是个流工作线程，以afpacket的work工作模式为例，函数执行流程如下：
TmThreadsSlotPktAcqLoop-》ReceiveAFPLoop-》AFPReadFromRing-》TmThreadsSlotProcessPkt-》TmThreadsSlotVarRun-》SlotFunc（FlowWorker）

ReceiveAFPLoop就是当时注册的收包slot,
FlowWorker就是当时注册的flow work slot

![]()

在多网卡收包的场景下，推荐使用work模式，该模式的性能会更好，同时可以调节收包模式，使得同一个五元组在同一个线程中处理，更有利于在攻击场景中做统计计算。

后续将再介绍一些：解包过程（比如mysql,pop3,http,dns协议的解析详细信息），日志记录，规则匹配，高性能场景性能优化的一些相关知识。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**LLSRC**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283260](/post/id/283260)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [货拉拉SRC](/tag/%E8%B4%A7%E6%8B%89%E6%8B%89SRC)

**+1**22赞

收藏

![](https://p5.ssl.qhimg.com/t011f2daffb9cd10c62.png)LLSRC

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t01a7b03f8b12427ba3.png)

[![](https://p5.ssl.qhimg.com/t011f2daffb9cd10c62.png)](/member.html?memberId=158408)

[LLSRC](/member.html?memberId=158408)

货拉拉安全应急响应中心，简称LLSRC，是致力于保障货拉拉用户、业务和产品等安全，促进与安全专家的合作与交流，而建立的漏洞收集及响应平台。

* 文章
* **13**

* 粉丝
* **5**

### TA的文章

* ##### [货拉拉SRC翻倍活动来啦！开年兔飞猛涨，钱兔无量](/post/id/286201)

  2023-02-08 17:30:02
* ##### [记一次DarkKomet synaptics 病毒应急响应事件](/post/id/283990)

  2022-12-02 16:00:49
* ##### [网络入侵检测系统之suricata概要介绍](/post/id/283260)

  2022-11-29 15:00:41
* ##### [新形势下安全风险评估实践](/post/id/283536)

  2022-11-24 12:00:54
* ##### [活动 | 货拉拉信息安全技术沙龙来袭！与你相约8月19日](/post/id/277712)

  2022-08-09 18:00:48

### 相关文章

* ##### [NSIC网络安全智能中心，重塑企业数据安全新范式](/post/id/308646)

  2025-06-23 10:17:20
* ##### [企业安全的工作沟通与交流平台，吱吱守护企业通讯安全](/post/id/307470)

  2025-05-22 14:49:44

### 热门推荐

文章目录

* [1.简介](#h2-0)
* [2.suricata安装](#h2-1)
  + [2.1 依赖库安装](#h3-2)
  + [2.2源码下载编译](#h3-3)
  + [2.3 运行](#h3-4)
* [3.suricata基本信息介绍](#h2-5)
* [4.suricata 工作模式分析](#h2-6)
  + [4.1 single模式](#h3-7)
  + [4.2 work模式](#h3-8)
  + [4.3 autofp工作模式](#h3-9)
  + [4.4 work线程介绍](#h3-10)

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