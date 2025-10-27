---
title: TOTOLINK NR1800X 系列 CVE 分析
url: https://www.anquanke.com/post/id/282739
source: 安全客-有思想的安全新媒体
date: 2022-11-09
fetch_date: 2025-10-03T22:01:42.247390
---

# TOTOLINK NR1800X 系列 CVE 分析

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

# TOTOLINK NR1800X 系列 CVE 分析

阅读量**573526**

发布时间 : 2022-11-08 14:00:23

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

<https://paper.seebug.org/1995/>

TOTOLINK NR1800X最近报了一些cve，现主要对其命令注入进行具体分析，以及对其登录绕过进行分析。

## 漏洞简介

固件下载地址：<https://www.totolink.net/home/menu/detail/menu_listtpl/download/id/225/ids/36.html>

## 环境搭建

### 固件提取

binwalk提取固件
`binwalk -Me TOTOLINK_C834FR-1C_NR1800X_IP04469_MT7621A_SPI_16M256M_V9.1.0u.6279_B20210910_ALL.web`

![]()

查看文件相关信息，mips架构，小端序，使用mipsel来进行模拟。
`readelf -h ./bin/busybox`

![]()

### 固件模拟

有两种模拟方式，user模式和system模式，感觉根据后面的模拟结果来看，好像差别不是很大。

#### user模式模拟

尝试用qemu模拟

```
cp $(which qemu-mipsel-static) .
sudo chroot . ./qemu-mipsel-static ./usr/sbin/lighttpd
```

会报错，显示`No configuration available. Try using -f option.`，这个报错是需要-f指定已有的配置文件。

运行`sudo chroot . ./qemu-mipsel-static ./usr/sbin/lighttpd -f ./lighttp/lighttpd.conf`即可，接着又会报错，说缺少一个文件，创建在对应目录创建一个即可。

```
cd ./var
mkdir run
cd run
touch touch lighttpd.pid
```

然后运行，可以看到服务启动成功。

![]()

但是这个路由器登录是需要密码的，并且由于是模拟的关系，大部分功能无法正常使用，登录不进去，但是还好经过搜索，发现看雪上有一篇文章讲述了如何进行绕过登录，登录过后，能观察到里面的一些设置，通过bp抓包能分析出一些有效的请求头内容，其数据传输通过json实现。

![]()

![]()

#### system模拟

user模拟中创建的文件都要有，后面会一起传到quem模拟的虚拟机中。

下载qemu启动虚拟机所需要的“镜像”，这是小端序，所以去下载mipsel的镜像。

```
wget https://people.debian.org/~aurel32/qemu/mipsel/debian_wheezy_mipsel_standard.qcow2
wget https://people.debian.org/~aurel32/qemu/mipsel/vmlinux-3.2.0-4-4kc-malta
```

创建虚拟网桥，实现虚拟机内部和Ubuntu的连接，并且启动虚拟机，创建一个shell文件。

```
#set network
sudo brctl addbr virbr0
sudo ifconfig virbr0 192.168.5.1/24 up
sudo tunctl -t tap0
sudo ifconfig tap0 192.168.5.11/24 up
sudo brctl addif virbr0 tap0

qemu-system-mipsel -M malta -kernel vmlinux-3.2.0-4-4kc-malta -hda debian_wheezy_mipsel_standard.qcow2 -append "root=/dev/sda1" -netdev tap,id=tapnet,ifname=tap0,script=no -device rtl8139,netdev=tapnet -nographic
```

然后`sudo ./test.sh`执行。

![]()![]()

最后会让登陆和输入密码，都写root就行，然后就能成功进入qemu虚拟机。

![]()

在启动的虚拟机里面添加一个IP，是在上面图片中的qemu虚拟机中执行命令。

```
ifconfig eth0 192.168.5.12 up
```

然后则是将提取出的固件的文件系统上传到qemu虚拟机中，在Ubuntu主机中执行命令。

```
scp -r squashfs-root/ root@192.168.5.12:/root/
```

![]()

然后到qemu虚拟机中进行挂载和启动。

```
chroot ./squashfs-root/ /bin/sh

./usr/sbin/lighttpd -f ./lighttp/lighttpd.conf
```

成功启动

![]()

界面这些和user模式都是差不多一样的。

## 漏洞分析

报了很多个漏洞，大部分是堆栈溢出，然后一些是命令注入，这里主要分析命令注入的相关漏洞。

### 登录验证绕过

这两个命令执行都是是需要登录验证的，这里先来分析如何进行登录验证绕过。

无论输入什么密码，都会返回错误，错误码为302。

先随便输入一个密码，看看发的包，可以看到主要的包有两个，先看第一个包。

![]()

可以看到处理http post请求的是cstecgi.cgi，传入了username和password，对应action是login，我们到相关位置去查看对应的代码。

![]()

可以看到，这里主要就是用sprinf初始一段语句，我们需要注意的是其中的topicurl，这个后面跟的就是对应接口的字符串，所以我们要去寻找loginAuth对应的处理函数。

这里再说一下，cstecgi.cgi处理不同的函数接口就是通过topicurl的值实现的，也就是后面goto LABEL\_16的代码部分。

![]()

所以这些函数名称和函数地址也是那种常见的结构体的形式，我们要寻找loginAuth对应的处理函数，找到字符串的交叉引用，然后在周围找找，d键一下，就能找到对应的处理函数，函数地址在sub\_42AEEC，下面来具体分析这个函数。

前面还是会获取一些参数的值，比如username还有password这些，然后还对password进行了urldecode。

![]()

然后中间会有段比较password和http\_passwd的代码，其会修改v18的值。

```
v17 = strcmp(v6, v30);                        // username http_username
if ( !strcmp(v35, v32) )                      // passwd http_passwd
    v18 = v17 != 0;
else
    v18 = 1;
```

这里不知道是否是因为模拟环境的原因，无论使用什么密码都无法正常登陆，但是这里的v18，需要注意下，这是第二个包的参数之一，而且这个值在最后会为0。

![]()

这段代码会snprintf一个重定向一个url，然后进行访问，其流程由flag参数的值决定，我们随便输入密码，就会进入第3个redirectURL，需要注意其authCode参数，授权码，也就是之前v18的值，现在它的值为0。

接下来我们看第二个包，可以看到和我们前面分析的一样，get访问了这个url。

![]()

这个http get请求的处理在web服务进程lighttpd中，也就是我们quem启动的那个进程，我们通过authCode字符串，能交叉引用到其对应的函数为Form\_Login。

开始分析Form\_Login，开始还是先获取参数的值，然后根据goURL参数是否为空，来判断是否进入if里面。

![]()

接着向下看。

![]()

所以这里，我们可以了解到goURL就是接下来要访问的html文件，authCode则是验证是否正确登录的一个值，并且经过后面的测试访问home.html就可以进入到后台界面。
所以我们可以构造下面的url，来绕过登录，进入后台，并且可以获取到cookie的SESSION\_ID。

```
http://xxx.xxx.xxx.xxx/formLoginAuth.htm?authCode=1&userName=admin&goURL=home.html&action=login
http://xxx.xxx.xxx.xxx/formLoginAuth.htm?authCode=1&userName=admin&goURL=&action=login
```

goURL可有可无，因为goURL无值时，自动会strcpy “home.html”，效果如下。

![]()

### OpModeCfg 命令注入

第一个是 /cgi-bin/cstecgi.cgi 中的 OpModeCfg 函数的命令注入漏洞，其漏洞原因是传入的hostName参数，可执行到doSystem函数，通过简单的构造即可导致命令执行。
但是想要执行到doSystem函数，需要绕过一些判断语句，proto不能为0，3，4，6，hostName不能为空。

![]()

### UploadFirmwareFile 命令注入

第二个是 /cgi-bin/cstecgi.cgi 的 UploadFirmwareFile 函数，其参数FileName参数可控，并且将作为doSystem的参数被执行。

这个命令注入不需要绕过什么东西，代码位置比较靠前。

![]()

## 攻击测试

先尝试bp发一下包，可以看到攻击成功，并且带有回显

![]()

编写个poc进行攻击，先进行登录绕过获取cookie，然后进行攻击，攻击效果如下

![]()

对于另一个命令注入攻击方式也差不多，只是没有回显，简单修改下poc，在tmp目录创建一个hack文件，攻击效果如下

![]()

## 参考

TOTOLINK NR1800X系列cve：<https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=TOTOLINK%20NR1800X>

环境搭建usr模式和system模式，并绕过登录检测：<https://bbs.pediy.com/thread-271765.htm#msg_header_h2_1>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**知道创宇404实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282739](/post/id/282739)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t016a18426d2b84e450.png)知道创宇404实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t01ea242f2ebadc2f91.png)

[![](https://p0.ssl.qhimg.com/t016a18426d2b84e450.png)](/member.html?memberId=146603)

[知道创宇404实验室](/member.html?memberId=146603)

知道创宇404实验室，长期致力于Web 、IoT 、工控、区块链等领域内安全漏洞挖掘、攻防技术的研究工作，团队曾多次向国内外多家知名厂商如微软、苹果、Adobe 、腾讯、阿里、百度等提交漏洞研究成果，并协助修复安全漏洞，多次获得相关致谢，在业内享有极高的声誉。

* 文章
* **112**

* 粉丝
* **69**

### TA的文章

* ##### [虽迟但到！404 Paper 精粹新刊发布，抢2022套册](/post/id/287509)

  2023-03-16 17:00:32
* ##### [ProxmoxVE 下的 Windows 内核调试环境配置](/post/id/286802)

  2023-03-01 10:30:11
* ##### [Citrix CVE-2022-27518 漏洞分析](/post/id/286519)

  2023-02-21 14:30:10
* ##### [StealthHook - 一种在不修改内存保护的情况下挂钩函数的方法](/post/id/284688)

  2023-01-04 10:30:12
* ##### [DirectX Hook - 优雅的实现游戏辅助窗口](/post/id/284747)

  2023-01-03 10:30:51

### 相关文章

* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃](/post/id/308349)

  2025-06-11 16:08:49
* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03

### 热门推荐

文章目录

* [漏洞简介](#h2-0)
* [环境搭建](#h2-1)
  + [固件提取](#h3-2)
  + [固件模拟](#h3-3)
* [漏洞分析](#h2-4)
  + [登录验证绕过](#h3-5)
  + [OpModeCfg 命令注入](#h3-6)
  + [UploadFirmwareFile 命令注入](#h3-7)
* [攻击测试](#h2-8)
* [参考](#h2-9)

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