---
title: TP-Link TL-WR841N设备中的1day到0day漏洞
url: https://www.anquanke.com/post/id/282931
source: 安全客-有思想的安全新媒体
date: 2022-11-11
fetch_date: 2025-10-03T22:19:53.036101
---

# TP-Link TL-WR841N设备中的1day到0day漏洞

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

# TP-Link TL-WR841N设备中的1day到0day漏洞

阅读量**480858**

发布时间 : 2022-11-10 15:30:52

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

> 译者注：直接英译中后语句太过拗口，在不改变原意的情况下做了些许调整
> 原文：[1day to 0day(CVE-2022-30024) on TP-Link TL-WR841N](https://blog.viettelcybersecurity.com/1day-to-0day-on-tl-link-tl-wr841n/)

TP-Link TL-WR841N 设备中的漏洞

| 漏洞 | 描述 |
| --- | --- |
| CVE-2020-8423 | 数据解析 |
| CVE-2022-24355 | 文件扩展名处理 |
| CVE-2022-30024 | 数据分配 |

## CVE-2020-8423

### 描述

TP-LINK厂商，其TL-WR841N V10型号的路由器存在一漏洞，已分配CVE编号为 [CVE-2020-8423](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8423)。

型号为 TL-WR841N v10的 TP-LINK 路由器设备的漏洞被指定为 ID  [CVE-2020-8423](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8423)。经过身份验证的攻击者，通过向 wifi 网络配置发送 GET 请求，可在设备上实现远程代码执行。

**固件**

Firmware version: [3.16.9 Build 150310](https://www.tp-link.com/vn/support/download/tl-wr841n/v10/#Firmware).

### 漏洞分析

在进入漏洞点之前，我将分析 `Dispatcher()`函数，以理解程序是如何分配函数来处理其功能的。

当一个REQUEST提交时，`httpGenListDataGet()`函数将被调用并返回一个 `LIST_ENTRY` 指针，其指向了一个函数指针列表，这些函数用来处理对应的URL。

然后，程序将调用`httpGenListFuncGet()` 函数来返回列表中的某个函数指针，并检查该函数对应处理的URL是否出现在REQUEST中。

若检查通过，则将调用该函数，否则继续从列表中取回函数指针并检查URL，重复此过程直至检查通过。

![]()

![]()

程序通过`httpRpmConfigAdd()`函数，为每个URL分配具体的处理函数。

![]()

说的有点多，接下来将关注点放在漏洞分析上。

在`stringModify()`函数中处理某些字符时，错误发生了。该函数在遇到 `\, /, <,> "`等字符时，会添加`\`来转义，或者在下个字符不是 `\n` 和 `\r`时，添加字符串`<br>`，重复执行此操作，直至缓冲区满。

![]()

问题在于向dst缓冲区添加字符串`<br>`，数据增加了4个字节，但程序只处理了1个字节。

![]()

因此，只要找到一个调用此函数的位置，其src缓冲区来自用户输入，此漏洞就很可能触发。

发现了 `writePageParamSet()` 函数，它有一个创建页面的函数（即httpPrintf），还有一个缓冲区`dst[512]` ，将传递给 `stringModify()`函数来存放处理后的字符。

![]()

在地址 `0x45FA94` 处，我们发现了一个回调函数，用来处理包含`/userRpm/popupSiteSurveyRpm.htm` 字符串的URL。

![]()

该函数将接收GET请求的参数，并调用漏洞函数。

![]()

可通过 ssid 参数来控制该漏洞。

![]()

![]()

### 漏洞验证

使用 `Payload = "/%0a" * 0x55 + "A" * 100`.

设置断点并观察。

漏洞已被验证，`$ra`寄存器的值已被改变，此外 `$s0, $s1, $s2`三个寄存器的值也被覆盖。

![]()

### Exploit

检查后发现程序没有启动任何保护机制，因此可将shellcode注入到栈空间来执行任意代码。

![]()

对于MIPS架构有个问题，在执行 shellcode 之前需要清除 `Icache`缓存。为了解决这个问题，需要控制程序执行流，使其跳入`Sleep()` 函数。

在一个历史exp中（[here](https://www.exploit-db.com/exploits/46678)），发现一条Rop链，其采用的库与本程序使用的库相匹配。不过还需要简单调整一下。

![]()

![]()

#### 修复shellcode

我使用了一个shellcode（[here](https://www.exploit-db.com/exploits/45541)），但并不奏效。

通过调试，发现当shellcode传递给`stringModify()`函数时，如果其包含字节 `\x3c, \x3e, \x2f, \x22, \x5c`，程序将在 `\x5c\x3c`或 `\x5c\x3e`之前面添加1字节的`\x5c`，因此破坏了原有的shellcode。

检查这个 shellcode，发现其包含2个坏字节 `\x3c`和`\x2f`。我将修改此shellcode，通过指令替换的方式，来删除这些坏字节。

#### 修复字节 0x3c

这个字节位于 `lui` 指令中，按作者的逻辑，将保存4个字节到栈上。

![]()

修改 `lui`指令为 `li` 指令，保存2个字节到栈上，而非原本的4个。

![]()

#### 修复字节 0x2f

在这个命令字符串中，包含了`0x3c` 和 `0x2f`这两个坏字节，要将字符串`//bin/sh` 放置到栈上。

![]()

使用 `li` 指令来移除 `0x3c`，可使用包含立即数的 `xori` 指令来移除 `0x2f`。

![]()

通过此种方式修改shellcode后，可获取此路由器的控制权。

![]()

下一步要去检测此设备的整个固件，在此我发现了更多的1day和0day漏洞。

## CVE-2022-24355

**漏洞信息**

发现的第一个 1day 漏洞为 [CVE-2022-24355](https://nvd.nist.gov/vuln/detail/CVE-2022-24355)（critical等级）。其允许网络攻击者在未经认证的情况下，通过缓冲区溢出漏洞来执行任意代码。我的队友已分析了此漏洞（[here](https://blog.viettelcybersecurity.com/tp-link-tl-wr940n-httpd-httprpmfs-stack-based-buffer-overflow-remote-code-execution-vulnerability/) ），故在此不再赘述。

## CVE-2022-30024

### 漏洞描述

这是一个基于栈的缓冲区溢出，存在于二进制程序httpd（提供web服务）的`ipAddrDispose`函数中。漏洞发生在将 GET 请求的参数值分配给栈变量的过程中，该过程允许用户向栈内存中输入大量数据，而这些数据攻击者可控。

### 发现错误

首先，来到容易理解的 ping 功能点处。

![]()

发送字符串`aaaaaaaaa....aaa` ，检查程序是否可溢出崩溃，结果在UI中只可以输入50个字符，就得到报错`ping request could not find host ….. Please check the name and try again.`

![]()

好像什么都没有发生，继续寻找此功能的处理函数，并进行逆向。

打开burpsuite，得到URL包含 `/userRpm/PingIframeRpm.htm` 字符串的请求

![]()

打开 IDA寻找此URL字符串，在地址`0x44A530`处找到处理此URL的函数。

![]()

![]()

调用 `httpGetEnv`函数来获取`ping_addr, doType, isNew`的值，其通过GET请求的参数来传递。

![]()

调用`ipAddrDispose` 函数并传参`ping _addr` ，漏洞就发生在这。

![]()

初始化一个52字节大小的栈变量 `buf_ip`，其接收并保存`ping_addr`中的每个字符，直至字符串结尾。

问题在于，`ping_addr` 的长度并没有在代码中验证处理，仅仅在web UI中做了限制，可以很容易的通过burpsuite来绕过。

![]()

在burpsuite中进行测试，输入大约200个”a”字符来作为 `ping_addr`，结果程序崩溃了。返回地址即`$ra`寄存器的值被覆盖了，因此可确定漏洞存在。

![]()

编写了一个简单的python脚本来触发此漏洞，结果不出所料。

![]()

![]()

### Exploit

接下来的目标是对设备进行RCE。此设备没有启用任何的保护机制，ASLR也是关闭状态，因此可控制 $ra 寄存器，使其跳入shellcode来执行代码并接管设备。

查看程序开头和结尾的汇编语句，找栈变量`buf_ip`的位置，可计算覆盖到`$ra`的偏移，即`(0xD4 + 8) - (0xD4 – 0xA0) = 168 bytes`，同时，也可以控制另外两个寄存器`$s0` 和 `$s1`。

![]()

![]()

![]()

为了便于理解，作图如下：

![]()

在MIPS架构中，不可以直接跳到shellcode去执行代码，必须先通过跳转到 `sleep()`函数来清除 `Icache`缓存即 `Instruction cache` 。既然是相同的固件，我将采用上述同样的ROP链。

![]()

构建完整的ROP链，如下可见栈空间的布局

![]()

最终，我们可成功通过此栈溢出漏洞控制设备。因为进行了固件模拟，所以反弹shell时会打印日志，真实的设备上不会如此。

![]()

![]()

我发现这个漏洞存在于 TL-WR841N V12及以下版本中，并分配编号CVE-2022-30024。用户应该从 TP-Link 官方网站下载最新的固件来更新补丁。<https://www.tp-link.com/en/support/download/tl-wr841n/v12/#Firmware>

### 时间线

* 14/04/2022：向他们发送漏洞报告
* 27/04/2022：TP-Link安全团队发我一份修改后的固件来检查
* 04/08/2022：TP-Link发布了新固件

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**新概念攻防实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282931](/post/id/282931)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [栈溢出](/tag/%E6%A0%88%E6%BA%A2%E5%87%BA)
* [TP-LINK](/tag/TP-LINK)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t01b1026ab9ef3d3b0f.png)新概念攻防实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t01b1026ab9ef3d3b0f.png)](/member.html?memberId=164993)

[新概念攻防实验室](/member.html?memberId=164993)

这个人太懒了，签名都懒得写一个

* 文章
* **4**

* 粉丝
* **2**

### TA的文章

* ##### [TP-Link TL-WR841N设备中的1day到0day漏洞](/post/id/282931)

  2022-11-10 15:30:52
* ##### [补丁分析发现Zyxel认证绕过(CVE-2022-0342)](/post/id/277276)

  2022-08-04 14:30:52
* ##### [NETGEAR Nighthawk R7000 httpd PreAuth RCE](/post/id/272402)

  2022-04-24 14:30:05
* ##### [D-Link DIR-3060 命令注入漏洞 CVE-2021-28144](/post/id/266009)

  2022-01-24 15:30:10

### 相关文章

* ##### [Seedlab Ret2Libc 与 ROP WriteUp](/post/id/258025)

  2021-11-18 10:00:30
* ##### [CVE-2016-6909 Fortigate 防火墙 Cookie 解析漏洞复现及简要分析](/post/id/252842)

  2021-09-10 14:30:37
* ##### [ciscn 2021 Final Day2 Message Board 思路分享](/post/id/247645)

  2021-08-05 17:30:33
* ##### [CVE-2018-18708：Tenda路由器缓冲区溢出漏洞分析](/post/id/204403)

  2020-05-08 10:30:02
* ##### [写给初学者的IoT实战教程之ARM栈溢出](/post/id/204326)

  2020-05-07 15:30:51
* ##### [TP-Link Archer A7命令注入漏洞分析](/post/id/202671)

  2020-04-10 10:30:26
* ##### [CVE-2018-4901 Adobe Acrobat Reader远程代码执行漏洞预警](/post/id/99919)

  2018-03-06 09:56:50

### 热门推荐

文章目录

* [CVE-2020-8423](#h2-0)
  + [描述](#h3-1)
  + [漏洞分析](#h3-2)
  + [漏洞验证](#h3-3)
  + [Exploit](#h3-4)
* [CVE-2022-24355](#h2-5)
* [CVE-2022-30024](#h2-6)
  + [漏洞描述](#h3-7)
  + [发现错误](#h3-8)
  + [Exploit](#h3-9)
  + [时间线](#h3-10)

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