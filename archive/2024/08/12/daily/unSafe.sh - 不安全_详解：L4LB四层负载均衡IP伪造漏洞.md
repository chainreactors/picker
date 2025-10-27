---
title: 详解：L4LB四层负载均衡IP伪造漏洞
url: https://buaq.net/go-255443.html
source: unSafe.sh - 不安全
date: 2024-08-12
fetch_date: 2025-10-06T18:01:25.410385
---

# 详解：L4LB四层负载均衡IP伪造漏洞

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ad7ee22d5634e11cd2db8c4fdb6c1c38.jpg)

详解：L4LB四层负载均衡IP伪造漏洞

前言 去年11月，在国家信息安全漏洞共享平台CNVD、国家信息安全漏洞库CNNVD报告过TOA的IP伪造漏洞，到今天快过去1年了，各受影响方也基本修复完毕，今天聊一下细节吧。回顾当初演示时，使用了百度
*2024-8-11 22:39:13
Author: [govuln.com(查看原文)](/jump-255443.htm)
阅读量:86
收藏*

---

## 前言

去年11月，在`国家信息安全漏洞共享平台CNVD`、`国家信息安全漏洞库CNNVD`报告过TOA的IP伪造漏洞，到今天快过去1年了，各受影响方也基本修复完毕，今天聊一下细节吧。

![](https://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8appH4B9nlYIJT1cZJ1jzKjcq70RKCvUxoPMzicbk4cuTHhutgXQwr5lTw/640?wx_fmt=png&from=appmsg)

### ![](https://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8apBSdmgmkYq2JXmhvIexeC3ELoIfjAhibMJvQoI6vwZAuYW7Px6b62TXA/640?wx_fmt=png&from=appmsg) 回顾

当初演示时，使用了百度搜索里的IP查询接口。演示视频中，通过muou程序，参数中指定任意IP，即可使得当前电脑的出口IP为指定的任意IP。

### 炒冷饭？

有同学猜测这是HTTP的Header追加伪造？有同学说这是装神弄鬼，炒冷饭？有同学说自己早发现了公司内部不重视，不修复。

![](https://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8apibYuZC5ePhicUXozyJQnkOLp6hPZsicWJTwpNBMkNOo5gBYsruh6VeIGw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8apmJhlaib25r7kbpYVIYOI6SPQwUp3WUvW0jMf6fmFduwbjqbaQAenWuw/640?wx_fmt=png&from=appmsg)

那么，这漏洞到底是什么？？

网上有聪明的同学，有一定IP伪造基本知识，结合我在推特上的历史内容，很快重现了演示视频里的IP伪造，即TOA(TCP Option Address)[1]伪造IP，那么仅仅如此吗？

## 漏洞描述：

显然不是。不过，对了一点。 （点开背景音乐，阅读更带感）

### 大型IDC内部客户端IP如何透传？

L4LB四层负载均衡[2]后业务需要使用用户原始IP，这是常见的功能需求。在大型IDC内部，一般会在RS节点上部署`TOA（TCP Option Address）`内核模块，用来获取TCP Option中的原始IP，也就是下图中`TCP Segment`部分。

![](https://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8apFp98K53aCOkRibWibamvK6PwKmTibBQ1KkCtsOf2ibP8ibmQZGOPCJ07qow/640?wx_fmt=png&from=appmsg)

### 漏洞如何出现？

开源的4层负载均衡，在FNAT模式下，未能很好的清除TCP Option中恶意构造的TOA信息，将恶意数据透传至RS服务器，导致业务服务器取到伪造IP。

### 危害是什么？

**业务受损**

IP在很多Web防火墙、反爬虫系统、防刷系统（薅羊毛）是用于做策略控制的基础强依赖，IP的伪造将导致这些系统完全失效，造成极大的风险损失。

**信息安全风险**

在很多后台系统中，IP同样被用于ACL的网络边界数据，IP的伪造，也依旧成成为可以突破的入口，比如对特定IP加白，直接放行等等。

### 我是如何发现IP伪造漏洞的？

这个漏洞原理确实如阿里的安全专家pyn3rd[3]在多年前所写，直接在TCP Option里追加即可，网上聪明的同学也猜到了。

不过，笔者并不是安全研究相关，平时从事的工作也是安全产品的研发，没有看过那篇PPT。发现这漏洞时，也是意外。在研发一款零信任四层负载均衡产品时，为了实现IP透传使用了相关技术。扩展一下，便想到了这里可能存在安全问题，顺便验证了各大厂的IP伪造可能性。

### 国内友商情况

国内大厂，不管是腾讯、华为、阿里、小米、阿里、百度等等，几乎都是使用了FNAT TOA的技术向后透传IP，很多技术方案都源于早期的开源项目`LVS（Linux Virtual Server）` ，各大厂按照各自的需求逐步迭代，有些机制上的安全问题，也被保留下来了。当然也有部分是`IOA（IP Option Address）`，为了兼容UDP协议的IP透传。

### 相似之处

区别无非是`opcode`是`28`，是`200`还是`254` 还是 `253`，亦或是其他。也无非是`opsize` 是8 还是精简的`7`。也无非是读取`TOA`信息的时机，是`1SYN`还是`3SYN-ACK` ，亦或是为了兼容而都去读取。整体来看，大同小异。

### 差异

而最大的差异在于L4LB处理来自客户端TCP Option 既有信息。

1. 已有TOA信息清理还是不清理？
2. 相同`opcode`如何处理？
3. LB串联时，如何保留客户端（来自LB）的TOA信息？
4. 原包内容中的TCP Option长度已经满了，怎么办？

而这些情况只是L4LB的难题，那么对于RS服务器上的TOA 内核模块又会有哪些问题呢？

1. 读到TOA 信息后，要继续读，还是终止读取了？
2. 继续读的话，又读到了TOA，那么选择哪个？
3. 都读完了，却没有读到TOA信息怎么办？

带着这些问题，我们回头看下本次漏洞的各厂商表现。

### 入门级漏洞

演示视频中的漏洞，是百度引入的外部IP查询API，这个API后端L4LB也是使用了TOA技术向后透传IP，因为LB跟后面RS服务器配合问题，造成了客户端可伪造IP的问题。此漏洞的发生有以下几个条件

1. L4LB产品使用FNAT模式传递客户端IP
2. L4LB未清除客户端TCP协议中Option信息，自己也追加了一个TOA，之后就直接向后传递
3. 服务器主机启用TOA模块获取IP，且解析Option时，读到了伪造的IP，没有读到L4LB追加的IP

**TOA加在前面还是后面？**

L4LB 把TOA 放在TCP Option的最前面，还是最后面呢？这里就涉及到RS上的TOA内核模块读取机制了，这里也是很容易出漏洞的地方。

当然，也不排除是L4LB读取到TCP Option中已经有了TOA信息，便不在追加。（这在**L4LB串联**的场景中，是十分常见的做法）。

显然，这种实现方式，大概率是L4LB 这边问题很大，利用成本很低。

### 进阶级漏洞

国内大部分厂商都不存在这么简单的漏洞，那么意味着他们都没问题吗？然而并不是。

**L4LB的难题：TCP Option 满了**回到前面的问题，L4LB收到的客户端TCP Option 的长度已经超过最大长度40字节了，那么L4LB怎么处理？ 没有空间去追加客户端IP了，还要读取吗？

**不读**很多L4LB丢弃本次真实客户端IP 的诉求，直接透传给下游了。问题就出现在这里，那么，只要客户端恶意填满TCP Option ，不留给L4LB追加的机会，即可伪造任意IP给下游。而这就是国内大厂出现这个安全漏洞的地方。

> 注意，我这里用了**下游**，并没有说是**RS**，很多时候是L4LB串联，那么它的下游还是L4LB了。

**读取**如果L4LB发现已经满了，无法追加了，那么他要继续读取，而且要要清理、删除，才能规避这类问题。

#### DPVS 的漏洞

**LB侧（DPVS）：**dpvs中，在`src/ipvs/ip_vs_proto_tcp.c`文件的`tcp_in_add_toa`函数中，387行附近，判断当前TCP包中TCP option是否有足够空间来追加TOA结构体。若不够，则直接返回，够则追加。在 TCP OPTION规范中，长度为40字节。在DPVS 的TOA定义长度为8字节（ipv6为20字节）。

**RS侧（TOA）：**内核模块TOA hook了获取IP的函数，来获取客户端IP，在`toa.c`里最终是调用`get_toa_data`来获取。以IPv4为例，其中378行开始，读取到TCP Option中数据，匹配TOA的特征后，即返回。IPv6也是类似问题，不再赘述。

### 变态级漏洞

读取`TCP Option` ，清空`TOA`信息，就高枕无忧了吗？然而并不是，那思路是什么？

如果黑客构造了一个完全合规的`TCP Option` ，并且长度超过40字节，里面没有恶意的TOA IP，也**不留给L4LB留下填充客户端IP**的机会，那么，后端的RS 服务器，会**拿到什么IP**？还能**造成安全风险**吗？  客户端拿到的是L4LB的内网IP，难道把这些内网IP拉入黑名单吗？你确定敢这么干？

**内网IP**

再说了，内网IP一般会出现在你的各种风控策略、ACL策略中吗？

思路这么多，那么到底该如何修复呢？

## TOA 问题修复

通过前面的原理讲解，聪明的你一定知道要如何修复这个安全漏洞了。

也就是说整个TCP Option都要逐一字节读取、清理，防止有多个TOA的信息在里面。然而，L4LB这种产品，QPS都是十万、几十万的性能挑战，突然每个网络包都要多了这么多内存复制的动作，性能下降是最大的挑战，不过，这就是研发同学去考虑的问题了。

### DPVS 修复方案

我在像DPVS反馈这个BUG时，提了一个PR Remove toa field, fix security vulnerability. #925[4]，将所有恶意TOA字段都使用`TCP_OPT_NOP` 设置为空。然而这样，面对TCP Option被填满的清空，是丢失了客户端原始IP的。虽然性能上影响不大，但依旧有一些安全风险。

DPVS的专家ywc689[5] 给了一个更专业的、更安全的修复方案ipvs: toa enhancements #928[6]，只允许了以下几个`opcode`的Option，以及对应长度的`opsize`，并且选择了特别好的重置时机，在应对几十万QPS的网络包处理时，几乎没有新增性能损耗问题。（了解相应opcode含义，请阅读TCP Option Kind Numbers[7]）

```
// ...
```

> 虽然，这里`opcode` 为`30（Multipath TCP (MPTCP)）`的Option存在，但也仅允许SYN包时出现，如果RS的TOA内核模块是读取ACK内的TOA，那么这里是不受影响的。但是，如果你的TOA内核模块读取的是首个SYN包的TOA，那么**变态级思路**的问题依旧在。

## 问题验证

笔者实现了一个TCP Option自定义的工具，叫木偶(muou)[8]，你可以通过`sudo ./muou t -b 020405b4`命令来实现自定义TCP Option，这里演示了一个修改Maximum segment size的Option，MSS值为：1460。

按照你对这个漏洞的理解，假如这些漏洞都还存在，你需要实现一个通杀各大厂商的payload，那么该如何构造呢？

笔者的技术方案是`eBPF sockops` 操作TCP Option，此工具有一定危害，这里做了一定限制，本次只开源了二进制程序，防止定制成为攻击工具。

具体的技术方案，以后分享。

## 国外的现状

国外的L4LB产品资料相对比较少，现在的产品都是基于`eBPF XDP`做的，比如Isovalent公司的Cilium[9]、Facebook公司的Katran[10]、CloudFlare公司的Unimog[11]等产品。相对来说，不需要使用TCP Option/IP Option等方案，直接在L4LB侧转发给相应的RS服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8apOU79kg6eApDJkYnlr3J7PoZmq3ZiceiaQbKlu1MCXl5dW9utRiaacNI7g/640?wx_fmt=png&from=appmsg)

这里插一句，笔者没有吹捧eBPF，国外的现状确实如此，大多使用eBPF + XDP 实现的L4LB。

### 关于L4LB 四层负载均衡

更多关于，请阅读SRE技术专家laixintao的四层负载均衡漫谈[12] 系列文章。

## IOA 安全吗？

本文重点讨论了 基于TCP Option传递的客户端IP信息方案，从L4LB负载均衡到RS的TOA内核模块，不管是代码实现，还是协同机制，都存在着细微的差异，而这些细节恰恰是安全问题所在。

那么，基于IP Option的客户端IP透传方案国内哪些大厂在用？他们安全吗？

![](https://mmbiz.qpic.cn/mmbiz_jpg/IjnZ9ic9bGHuk6kVdCJWH6TaOmibMOJ8apPK4zhFr35ibLox8ohIfk3mSe9ceFBxR5L1CBYl5FIYKEG31HDhbbIQQ/640?wx_fmt=jpeg&from=appmsg)

参考资料

[1]

TOA(TCP Option Address): *https://datatracker.ietf.org/doc/html/rfc7974*

[2]

L4LB四层负载均衡: *https://avinetworks.com/glossary/layer-4-load-balancing/*

[3]

pyn3rd: *https://weibo.com/u/1977418460*

[4]

Remove toa field, fix security vulnerability. #925: *https://github.com/iqiyi/dpvs/pull/925*

[5]

ywc689: *https://github.com/ywc689*

[6]

ipvs: toa enhancements #928: *https://github.com/iqiyi/dpvs/pull/928*

[7]

TCP Option Kind Numbers: *https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml*

[8]

木偶(muou): *https://github.com/gojue/muou*

[9]

Cilium: *https://github.com/cilium/cilium*

[10]

Katran: *https://github.com/facebookincubator/katran/*

[11]

Unimog: *https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/*

[12]

四层负载均衡漫谈: *https://www.kawabangga.com/posts/5301*

文章来源: https://govuln.com/news/url/B16r
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)