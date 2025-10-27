---
title: 使用FirmAE 对zyxel路由器固件仿真实践
url: https://www.anquanke.com/post/id/288053
source: 安全客-有思想的安全新媒体
date: 2023-04-01
fetch_date: 2025-10-04T11:19:43.980073
---

# 使用FirmAE 对zyxel路由器固件仿真实践

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

# 使用FirmAE 对zyxel路由器固件仿真实践

阅读量**901015**

|评论**1**

发布时间 : 2023-03-31 17:14:28

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## 0x01.FirmAE简介

[FirmAE](https://github.com/pr0v3rbs/FirmAE) 是一个执行仿真和漏洞分析的全自动框架。FirmAE 使用五种仲裁技术显著提高仿真成功率（从[Firmadyne](https://github.com/firmadyne/firmadyne)的 16.28% 提高到 79.36%）。
![]()

FirmAE的整体架构为如上图所示。与Firmadyne类似，FirmAE在预先构建的自定义Linux内核和库上模拟固件镜像。它还模拟目标镜像两次，以收集各种系统日志，并利用这些信息进行进一步的仿真，前一个仿真步骤称为预仿真，后一个称为最终仿真。为了进行大规模分析，FirmAE致力于完全自动化。实际上Firmadyne的许多步骤已经自动化了，但是仍然需要一些用户交互。例如，用户必须首先使用特定选项提取目标固件的文件系统。然后，他们评估是否成功提取文件系统并检索架构信息。随后，他们为QEMU制作固件镜像并在预仿真中收集信息。最后，他们运行最终仿真的脚本并执行动态分析。FirmAE自动化了所有这些交互，并添加了一个用于网络可达性和Web服务可用性的自动评估过程。FirmAE还使用Docker 将仿真并行化，以有效评估大量固件镜像。每个固件镜像在每个容器中独立仿真，该容器配备所有所需的软件包和依赖项。这使得能够快速可靠地仿真目标镜像。更多详细细节可参考[FirmAE论文](https://syssec.kaist.ac.kr/pub/2020/kim_acsac2020.pdf)。

## 0x02. FirmAE安装

Ubuntu 18.04

Clone `FirmAE`

```
$ git clone --recursive https://github.com/pr0v3rbs/FirmAE
```

运行`download.sh`

```
$ ./download.sh
```

运行 `install.sh`

```
$ ./install.sh
```

## 0x03. FirmAE使用

执行`init.sh`脚本。

```
$ ./init.sh
```

检查仿真

```
$ sudo ./run.sh -c <brand> <firmware>
```

分析目标固件

* 分析模式，使用FirmAE分析器

```
$ sudo ./run.sh -a <brand> <firmware>
```

* 运行模式，有助于测试网络服务或执行自定义分析器

```
$ sudo ./run.sh -r <brand> <firmware>
```

完成`run.sh -c`后，可debug固件。

用户级基本调试实用程序

```
$ sudo ./run.sh -d <brand> <firmware>
```

内核级引导调试

```
$ sudo ./run.sh -b <brand> <firmware>
```

##

## 0x04. 使用FirmAE仿真zyxel路由器固件

一般情况下，按照上述方法使用FirmAE可自动化仿真固件，但也有一些固件自动化仿真的效果并不是很好，这时就需要做一些逆向分析，通过适当的调整来完成仿真。比如zyxel NWA1100-NH\_2.12固件，下面在使用FirmAE仿真该固件过程中，日志显示整个流程没有出错，顺利完成仿真，但实际上该路由器固件的web服务并没有被成功启动。
![]()

这里用调试模式模拟运行后选择2可以连接进入shell

但是发现无法正常访问http服务，通过分析发现，该固件文件系统中由两个http服务程序，FirmAE启动了httpd，实际上这个固件用的是mini\_httpd。
![]()

接下来尝试手动启动mini\_httpd，首先要清楚启动mini\_httpd需要哪些启动参数，通过查看/etc/default/mini\_httpd.conf，可以看到mini\_httpd默认启动参数
![]()

在/etc下可以看到有一个mini\_httpd.conf指向/tmp/mini\_httpd.conf，但实际上/tmp下并不存在这个文件
![]()

另外还有一个mini\_httpd.cnf文件，这里面有一下默认的内容，像是支持ssl的一些配置
![]()

直接尝试用这个配置文件启动是失败的，
![]()

在IDA里 打开mini\_httpd，搜索报错信息”unknown config option”
![]()

![]()

最终定位到解析配置文件的代码逻辑，这里可以看到在解析配置文件的一些字段，至于哪些是必要字段哪些是非必要字段，可以尝试构造文件，测试运行。

经过逆向分析和测试，最终我这里的配置文件内容构造如下

```
dir=/usr/www
cgipat=cgi-bin/*
user=root
port=8081
```

构造好配置文件就可以正常启动mini\_httpd了
![]()

此时发现可以成功访问http服务了
![]()

这里尝试用 admin admin登录，又发现了一个报错log\_maintain: not found
![]()

在mini\_httpd里面找到了调用log\_maintain的地方，找不到这个程序，说明这个程序所在路径不再环境变量，搜索到log\_maintain在

/etc/script/ 目录下，将该路径添加到环境变量

```
export PATH=/etc/scripts/:$PATH
```

![]()

继续分析登录逻辑，这里用户名密码会交给chkpwd程序验证
![]()
![]()

这里感觉用的是系统用户名密码，但是修改了系统用户名密码后没有成功登录，这里直接patch固件登录逻辑来绕过，可以看出如果用户名密码正确，v45会被写入字符串”Access granted”，后面以这个字符串为标志来判断是否成功登录，这里就直接将

`!srncmp(v84, "Access granted", 14)`改成`strncmp(v84, "Access granted", 14)` 即将bnez改成beqz
![]()
![]()

patch后成功登如路由器
![]()

登录后抓取到一个设置ip的请求包，下面定位处理http请求的代码，首先考虑字符串定位，但是在mini\_httpd程序中并未搜索到/cgi-bin/ip字符串。

```
POST /cgi-bin/ip HTTP/1.1
Host: 192.168.0.1:8081
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 192
Origin: http://192.168.0.1:8081
Connection: close
Referer: http://192.168.0.1:8081/cgi-bin/ip
Cookie: AUTH=; csd=3; cod=1
Upgrade-Insecure-Requests: 1

AP_IPADDR=1.1.1.1&AP_NETMASK=255.255.255.255&IPGW=192.168.0.2&IPV6_AUTO=none&IPV6_ADDR=&PRIDNS=8.8.8.8&SECDNS=1.1.1.1&DOT1Q_VLAN=&MGMT_VLAN_ID=22&MGMT_VLAN=&EEE_Status=&COMMIT=Apply&EXECUTE=ip
```

![]()

接着在固件文件夹下搜索/cgi-bin/ip字符串，发现了/usr/www/cgi-bin/ip这个目录，但实际在固件中没有找到ip这个程序，说明这个程序可能是固件运行起来后动态生成的。

最终在模拟运行的系统中发现了ip这个文件，ip链接到了/sbin/cgiMain，说明请求实际上是由cgiMain来处理。接下来就可以逆向cgiMain程序对http请求处理来进一步挖洞了，另外还可以在调试模式中使用gdb动态调试cgiMain。
![]()

## 0x05. 总结

通过FirmAE可以对一些IoT固件自动化仿真，同时也便于逆向和动态调试，大大方便了安全研究。但对一些无法完全自动仿真的固件，就需要安全研究员手动分析可能的原因， 本文分享了一个没有自动仿真成功的固件案例，以及解决问题的思路。另外对FirmAE的实现及FirmAE其他功能感兴趣的，可以阅读项目源码及论文。

## 0x06.参考链接：

1. <https://github.com/pr0v3rbs/FirmAE>
2. <https://syssec.kaist.ac.kr/pub/2020/kim_acsac2020.pdf>
3. <https://github.com/firmadyne/firmadyne>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**360安全应急响应中心**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288053](/post/id/288053)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [IOT安全](/tag/IOT%E5%AE%89%E5%85%A8)
* [固件仿真](/tag/%E5%9B%BA%E4%BB%B6%E4%BB%BF%E7%9C%9F)

**+1**12赞

收藏

![](https://p3.ssl.qhmsg.com/dm/200_200_100/t01b5d8fecc4d01072b.jpg)360安全应急响应中心

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhmsg.com/dm/200_200_100/t01b5d8fecc4d01072b.jpg)](/member.html?memberId=122586)

[360安全应急响应中心](/member.html?memberId=122586)

360安全应急响应中心（360 Security Response Center，简称360SRC）是360公司致力于保障产品及业务安全，促进白帽专家合作与交流的平台。诚邀白帽专家向我们反馈360产品安全漏洞、威胁情报，共筑数字安全基石，保障数亿用户业务和产品的安全。

* 文章
* **67**

* 粉丝
* **13**

### TA的文章

* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [诚邀莅临|三六零天御·亚马逊云科技安全合规沙龙](/post/id/308420)

  2025-06-13 14:18:45
* ##### [360 MCP 生态安全风险治理实践与思考](/post/id/307934)

  2025-05-29 11:07:56
* ##### [ingress-nightmare 漏洞利用分析与 k8s 相关组件理解](/post/id/306494)

  2025-04-14 15:24:44
* ##### [基于 RAG 提升大模型安全运营效率](/post/id/306214)

  2025-04-03 19:07:23

### 相关文章

* ##### [浅谈智能物联网家居平台安全隐患](/post/id/283465)

  2022-11-29 15:30:43
* ##### [电动汽车充电站管理系统安全深度分析](/post/id/267126)

  2022-02-07 10:00:51
* ##### [IoT 设备安全有妙招？蜜罐盲盒摇一摇！](/post/id/263933)

  2021-12-25 10:00:46
* ##### [通过更改3D打印机编译器进行的信息泄漏攻击](/post/id/249646)

  2021-09-09 14:30:24
* ##### [使用 GDB 获取软路由的文件系统](/post/id/249993)

  2021-08-16 12:00:44
* ##### [加密固件之依据老固件进行解密](/post/id/248741)

  2021-08-08 12:00:10
* ##### [D-Link DIR 3040 从信息泄露到 RCE](/post/id/248740)

  2021-08-03 12:00:41

### 热门推荐

文章目录

* [0x01.FirmAE简介](#h2-0)
* [0x02. FirmAE安装](#h2-1)
* [0x03. FirmAE使用](#h2-2)
* [0x04. 使用FirmAE仿真zyxel路由器固件](#h2-4)
* [0x05. 总结](#h2-5)
* [0x06.参考链接：](#h2-6)

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