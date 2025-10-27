---
title: 美国网件Netgear RAX30路由器RCE漏洞分析
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500323&idx=1&sn=d490cc0d8bd8298a3d0a093c388f2701&chksm=fa52179dcd259e8bb50fe3de14bfb67612204aaf46be994c7a5da67713f1cdf296f8a8007d49&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-10
fetch_date: 2025-10-04T09:09:21.899887
---

# 美国网件Netgear RAX30路由器RCE漏洞分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnT5kl9cLM5iamNPNIRd7umvgibibUhYicdK37OkiakwO5lIdrMvGjLtOYVjnicGNtlS6QyBocb4JzOvmkAw/0?wx_fmt=jpeg)

# 美国网件Netgear RAX30路由器RCE漏洞分析

原创

B2eFly

山石网科安全技术研究院

‍

## ‍Netgear RAX30 漏洞分析

2022年**Pwn2Own**比赛前一天，Netgear官方修复了RAX30设备多个高危漏洞。

**设备品牌:** Netgear

**设备型号:** RAX30

固件版本:  [RAX30 1.0.7.70](Nighthawk RAX30 | WiFi 6 Router | NETGEAR Support)

##

**0****1**

**漏洞概述‍**

* **CVE-2022-47208**

默认情况下运行的“puhttpsniff”服务由于用户输入不当导致容易受到命令注入的影响。与路由器位于同一网段上的用户可无需身份验证即可在设备上执行任意命令。

* **CVE-2022-47209**

默认情况下，设备上有四个用户帐户。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgE96l3c6N1BhxlO04Bmtuscu1REJfWWvvXOyic09gBNaGNRDPUtJSN5yQ/640?wx_fmt=png)

admin -> 常规用户，通常为web服务和其他服务

support->后台技术支持后门账户

* 未查到CVE号

默认情况下运行的/bin/pucfu程序在boot过程中将会尝试连接Netgear域名并获得JSON响应数据。使用DHCP服务器去控制DNS服务器给路由器WAN口分配地址。通过控制DNS 查询响应报文触发命令注入。

**0****2‍**

**漏洞分析**

### 2.1 CVE-2022-47208

查看命令注入危险函数，发现获取User-Agent参数没有进行过滤，导致命令注入。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgEflUFpatgVN8TBYaxlJLwahaphtbJRogyRjicic4wWVH0iaPCwiba4zzOJQ/640?wx_fmt=png)

### 漏洞利用条件

伪造User-Agent

### 漏洞原理

Web服务在获取客户端请求包中User-Agent数据字段未能有效筛选危险字符导致设备任意命令执行。

### 2.2 **CVE-2022-47209**

硬编码

```
admin:$1$redacted:0:0:Administrator:/:/bin/sh
support:$1$QkcawmV.$VU4maCah6eHihce5l4YCP0:0:0:Technical Support:/:/bin/sh
user:$1$9RZrTDt7$UAaEbCkq.Qa4u0QwXpzln/:0:0:Normal User:/:/bin/sh
nobody:$1$OWpQjger$j7CFLUn8yoD8agVf6x5gA0:0:0:nobody for ftp:/:/bin/sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgErmqCHJXrc47icKWicibLHAQAXdrRQeWgvMaTibbP0TscoemgGotwGN9pow/640?wx_fmt=png)

### 2.3 pucfu 引发的命令注入

#### 漏洞原理

pucfu在启动过程中会向域名https://devcom.up.netgear.com/的netgear官网获取一个json数据，该数据最终北SetFileValue函数接卸，该函数存在命令执行漏洞，如果获取得到的json数据可以伪造的话，就会执行任意命令。‍

#### 漏洞触发

/bin/pucfu->/usr/lib/fwcheck.so(get\_check\_fw)->fw\_check\_api->curl\_post

/lib/libpu\_util.so(SetFileValue)->pegaPopen->libc.so(execve)

```
graph LR
A[pucfu] -->B(fwcheck.so) -->C(fw_check_api) -->D(curl_post) -->E(libpu_tuil.so) -->F(SetFileValue) -->G(pegaPopen) -->H(libc.so) -->J(execve)
```

#### 2.3.1 pucfu

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgE7smmBJn4f1yCHOTT5yZ4IPfapm63m8s6ybbs3ogFaZHa2YtpttkkkQ/640?wx_fmt=png)

将获取得到的json数据存储到v29变量中，最后将v29数据传递给SetFileValue函数。

#### 2.3.2 get\_check\_fw

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgEaEoNyOlq6u7mmYWnNPibT4NXIaOO2LRSXB1qW0cXuibM5vSBMLwU2sRA/640?wx_fmt=png)

从D2数据库中获取UpBaseURL,调用Netgear API 将从服务器端获取的数据进行保存。

#### 2.3.3 fw\_check\_api

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgEKVSynEc946q0IXnmAFLVLGoZEIT57AFJV48iatfZAUMaNMOhCxfss7A/640?wx_fmt=png)

最终pucfu bufferA获取到的数据就是url对应的数据内容，strcpy(bufferB,bufferA)

#### 2.3.4 SetFileValue

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgErxzHelV5TMfehwnEhx1DmXUab3VF2ibvW2FafAkuLdNu83FstmsTpWg/640?wx_fmt=png)

判断是否有'/'

```
SetFileValue("/tmp/fw/cfu_url_cache", "lastURL", bufferB); #lastURL 可控
sed -i 's|^lastURL=.*|lastURL=/'可控数据;# /'/tmp/fw/cfu_url_cache
sed -i 's|^lastURL=.*|lastURL=|'可控数据;# |'/tmp/fw/cfu_url_cache
```

pegaPopen

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgEmczuBZOgLL9F7Yz8PotnZjfBxoo0NWMiaq0zWSmdmbELoiax8lAZbVAA/640?wx_fmt=png)

构造数据，实现命令执行

```
"url":"';reboot#"
```

#### 漏洞利用条件

运行DHCP和DNS服务端劫持路由器原来指向的域名，然后通过伪造响应来实现任意命令执行。

**0****3‍**

**漏洞修复**

**固件版本:**1.0.9.90

### 3.1 puhttpsniff 漏洞修复

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgEa6libU2crWKQbeTfRcjWAeLxYU1q18IRz8za9AGN8IFVtO82HptxibhQ/640?wx_fmt=png)

使用带参数的调用而不是直接命令调用。

### 3.2 pucfu漏洞修复

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ1YfRNHzjcvTzwY8IVLMgEQ3uia53PDe4GVlibttRB57RkhXLEKNA1DQbnPpaLthv2kxNEGPjicgeBg/640?wx_fmt=png)

使用带参数的调用而不是直接命令调用。

**0****4‍**

**总结‍**

此次Netgear RAX30设备漏洞，主要还是开发者没能处理好数据是否可控、是否存在危险字符。Netgear官方在Pwn2own比赛前一天修复漏洞，对参赛选手来说也是一种考验。

固件下载地址：https://www.netgear.com/support/product/RAX30#download

‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过