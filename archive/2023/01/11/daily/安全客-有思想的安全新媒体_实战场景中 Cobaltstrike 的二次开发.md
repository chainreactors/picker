---
title: 实战场景中 Cobaltstrike 的二次开发
url: https://www.anquanke.com/post/id/285270
source: 安全客-有思想的安全新媒体
date: 2023-01-11
fetch_date: 2025-10-04T03:28:34.434217
---

# 实战场景中 Cobaltstrike 的二次开发

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

# 实战场景中 Cobaltstrike 的二次开发

阅读量**987129**

发布时间 : 2023-01-10 13:30:39

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

随着近几年HW实战的开展所有人都对Cobalstrike不再陌生，相关安防设备一直在思考如何在流量侧/终端侧识别出CS的行踪。攻击者除了使用习惯上基于插件进行开发提效外，还有一些需要关注对抗的点来提升CS的隐藏性，我们会分两篇文章将CS在流量层面、内存层面对抗侧二次开发做出的思考实践与大家分享交流。

## 流量层面的思考

从流量整体伪装的角度来看，最好的效果就是和正常流量混为一体，以此为出发点来构思流量隐蔽方案。

1. 有些思路会说改变CS原有的加密方式，自定义编码/加密的算法，不局限于C2 profile里面的几种算法。不管是哪种算法，我觉得目前基于HTTPS流量的通信方式是最好的，对于中间流量设备来说所观测到的https流量也是最多的，我们的c2混在其中让其无法区分。
2. 当然即使完全加密的流量，也会有其他办法去检测你，就比如说Rita，它是一个用于检测命令和控制通信的框架，根据多个变量识别恶意 C2 流量，包括通信频率、发送/接收的平均字节数、连接数等，数据量越大它的检测依据就越充分，结果也更为准确。当然我们也可以做出应对，无规律的随机发送正常流量，对于Beacon在静默状态和使用状态设置不同的通信频率，以此扰乱对时序层面上的流量特征。

## Cobalt Strike 流程概述

### cs.auth 认证流程

cs的 `license` 核心是非对称加密算法，对于关键的beacon相关文件使用rsa公钥加密，`license` 文件则是包含了cobalt stirke版本、watermark标志、license过期时间以及beacon解密私钥等信息。

### 主函数

客户端主函数 `agressor`， server端主函数 `server.TeamServer`，其中客户端主要是启动之前校验一下license，然后是启动图形界面，数据初始化。客户端这块不是主要关注的点，我们主要关注的点在服务端。也就是 `TeamServer` 类。

`TeamServer` 类也继承于 `Starter` 启动器父类，也会检测license合法性，获取过期时间水印等参数，解析 `c2profile` 配置文件，拉起server服务、listener，等待客户端连接上来，其中listener是由nanohttpd服务承载。

### beacon的生成

当选择一种生成模式之后从通用模板artifact.exe当中填充beacon.dll的shellcode，profile配置也是在这个时候经过xor加密填充到预留的空间。

### beacon的上线流程

收集一波主机信息之后向server发送一个上线包，此时产生一个session id作为这台肉鸡的标识，后续则不停发送心跳包（结合随机垃圾数据以免成为固定特征）等待下一次指令。

## 第一步明显特征规避

### 二阶段加载特征

二开第一步先把常规的cs特征规避了，像是profile配置、端口证书这些都不需要代码层面的改动，github上比较火的开源profile配置也已经被检测为特征了。我们更关注的是需要代码改动的特征，cs 的 stage 二阶段远程加载需要下载beacon的shellcode，当访问url路径符合checksum8计算的值，listener就会返回二阶段所需要运行的真正执行beacon的shellcode。使用二阶段加载beacon的功能会增加资产测绘被发现的风险，而且beacon的一阶段也不具备什么特殊的功能，不太符合实际场景的需求，大家可能更倾向于stageless或者定制化二阶段加载。这里的做法是直接删除该服务，毕竟怎么也不会用上单一的二阶段加载beacon。

### ja3/ja3s | jarm 指纹修改

JA3 是由 John Althouse、Jeff Atkinson 和 Josh Atkins 创建的开源项目。 JA3/JA3S 可以为客户端和服务器之间的通信创建 SSL 指纹。唯一签名可以表示从 Client Hello 数据包中的字段收集的几个值：

```
- SSL Version
- Accepted Ciphers
- List of Extensions
- Elliptic Curves
- Elliptic Curve Formats
```

JA3 工具用于为与服务器的客户端信标连接生成签名。另一方面，JA3S 能够生成服务器指纹。两者的结合可以产生最准确的结果。JA3S 可以捕获完整的加密通信并结合 JA3 的发现来生成签名。更详细的信息可以直接查看官方github仓库：<https://github.com/salesforce/ja3>。

本来 ja3/ja3s 指纹不算是什么很强的特征，因为它只是一个tls握手包的hash值，ja3s是被动流量，jarm是主动探测，这个指纹取决于你的tls所使用的参数，也就是说完全有可能别人写的https服务也和cs的listener撞上了，但是我们不能不修改，因为放着这样一个特征不去管也会成为可能突破口，修改的办法也很简单，在nanohttpd服务中，修改SSL相关的任意参数就能达到效果。

![]()

这里列出几个已知的ja3/ja3s指纹信息：

**JA3**

* 72a589da586844d7f0818ce684948eea
* a0e9f5d64349fb13191bc781f81f42e1

**JA3s**

* b742b407517bac9536a77a7b0fee28e9
* ae4edc6faf64d08308082ad26be60767

可以看到修改过后的值：

![]()

### Sigma 检测规则

根据开源的[sigma](https://github.com/SigmaHQ/sigma/blob/master/rules/network/net_mal_dns_cobaltstrike.yml)检测规则，上面公开了一些关于cs beacon的特征，像是cs默认证书以及检测被公开的一些profile配置，这里提几个实战中可能遇到的：

* 查看DNS日志基于dns\_stager\_subhost的默认DNS c2行为

![]()

* 基于对单个域的大量DNS查询检测

![]()

* 还有一分钟内从单一来源查找多条TXT记录

![]()

如果实战中遇到只有DNS出网的上线需求的话可以考虑使用DNS beacon, 注意一下默认的DNS行为就行，使得DNS请求趋于正常流量，根据配置就可以做到。只是需要注意一下一些通用的检测手段。

## 第二步隐蔽通信流量

接下来是本次二开CS中的重点，传统的CDN域前置隐藏c2的方式大家早已熟知了，CDN厂商也做了限制手段，想要再做出提升，唯有另辟蹊径，因此我们将目标对准了Shadow-TLS，以此达到更好的隐蔽流量的效果。

一般使用域前置时，把CDN作为白名单域名，当作一个靶子，中间设备所观测到的是一直与CDN通信：

![]()

现在CDN厂商使用应对手段禁止域前置被恶意使用:

1. 对比SNI和Host是否相等，如果是HTTPS流量需要解密
2. 禁止未验证的域名加速

传统CDN域前置遇到了些许阻碍，但有另一种思路，shadow-tls 将任意白名单域名作为影子域名，借用TLS连接建立起伪装，这或许是个不错的选择。

在讲shadow-tls之前我们先简单回顾下TLS握手的流程：

![]()

客户端发送握手，服务端返回握手、证书，双方协商密钥，之后统一用一个密钥对称加密之后的内容。那么怎么在这上面做文章呢？shadowtls的实现方式：

![]()

客户端请求与中间人服务器建立连接，握手阶段服务端将客户端的请求转发到⼀个可信域名上（顾名思义Shadow域名)，这样保证流量侧看到的服务端证书是⼀个可信域名的证书，在握手结束后，client 和 server 切换模式，利用已建立的连接传输自定义数据即可。这样做其实相当于一次 “TLS 表演”，给中间设备看的。并且在client Response中使用预定共享key返回8字节的hmac值，用于区分客户端流量和主动探测流量，正确响应主动探测流量。

### snowc2的实现方式

我们如何在CS中实现呢？这里我们用了更为直接的办法，在接收到影子域名的 server hello 握手包之后替换掉证书部分，使用c2 server的证书协商出密钥完成握手，接着就是正常的https流量 application data，同样给中间设备做了一次“TLS 表演”。

对于CS Server来说想要实现这部分功能，需要覆盖JDK类，这里用到了 java 提供的 endorsed 技术，可以简单理解为 `-Djava.endorsed.dirs` 指定的目录面放置的 jar 文件，将有覆盖系统 API 的功能。我们找到 `CertificateMessage.java` 文件中 `T12CertificateProducer` 类的 `onProduceCertificate` 方法，这个方法是处理tls握手时返回 sever hello 消息中的证书数据部分的，我们在其发送证书信息之前，替换成白名单域名的证书。这里给出演示DEMO，实际项目实现需完成更多细节。

![]()

既然服务端使用了白名单域名证书，客户端也要写一个替换证书，只不过要替换成原来的证书，写一个简单判断即可。

![]()

在tls握手阶段，判断 server hello 消息头，识别出证书消息，将其替换为我们原来的自签名证书。

### 最终效果

当我们自建域前置并结合shadow tls时：

```
client -> tls -> cdn -> c2 server
        tls 请求
        SNI: allow.com
        http 请求
        Host: allow.com
```

中间设备所观测到的将会是，客户端向 allow.com 发起了请求，经过TLS握手进行后续的通信，证书也是 allow.com，从明面上来讲，已经找不出毛病。

![client hello sni]()

![server certificate]()

可以看到客户端和cs server的tls握手通信变成了与 `www.baidu.com` 域名证书的握手。此外除了https连接请求之外，我们也加入了dns请求的流量，以让其看起来更像正常的通信流量。

这次二开我们专注在C2流量层面所做的事就告一段落，后续会更新内存层面的去特征化实践，请大家继续关注雪诺凛冬实验室。

本文首发公众号

## Reference

* <https://www.ihcblog.com/a-better-tls-obfs-proxy/>
* <https://thedfirreport.com/2022/01/24/cobalt-strike-a-defenders-guide-part-2/>
* <https://github.com/salesforce/ja3>
* <https://github.com/snowtech-cn/shadow-tls-client>
* <https://github.com/snowtech-cn/serverhelloEndorsed>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**雪诺凛冬实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285270](/post/id/285270)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [CobaltStrike](/tag/CobaltStrike)

**+1**22赞

收藏

![](https://p3.ssl.qhimg.com/t01b55da98ca58e651b.png)雪诺凛冬实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t01b55da98ca58e651b.png)](/member.html?memberId=167454)

[雪诺凛冬实验室](/member.html?memberId=167454)

雪诺凛冬实验室，隶属于北京雪诺科技，聚焦零信任赛道。主要职能包括红队技术、安全狩猎等前瞻攻防技术预研、工具平台孵化。

* 文章
* **4**

* 粉丝
* **3**

### TA的文章

* ##### [实战场景中 Cobaltstrike 的二次开发](/post/id/285270)

  2023-01-10 13:30:39
* ##### [漏洞分析 | 利用 CodeQL 分析 fastjson 1.2.80 利用链](/post/id/281733)

  2022-10-17 10:30:22
* ##### [5 种常见的前端加密渗透场景及案例](/post/id/280470)

  2022-09-21 12:00:24
* ##### [Bitbucket Server CVE-2022-36804 漏洞分析](/post/id/280193)

  2022-09-16 12:00:25

### 相关文章

* ##### [NSIC网络安全智能中心，重塑企业数据安全新范式](/post/id/308646)

  2025-06-23 10:17:20

### 热门推荐

文章目录

* [前言](#h2-0)
* [流量层面的思考](#h2-1)
* [Cobalt Strike 流程概述](#h2-2)
  + [cs.auth 认证流程](#h3-3)
  + [主函数](#h3-4)
  + [beacon的生成](#h3-5)
  + [beacon的上线流程](#h3-6)
* [第一步明显特征规避](#h2-7)
  + [二阶段加载特征](#h3-8)
  + [ja3/ja3s | jarm 指纹修改](#h3-9)
  + [Sigma 检测规则](#h3-10)
* [第二步隐蔽通信流量](#h2-11)
  + [snowc2的实现方式](#h3-12)
  + [最终效果](#h3-13)
* [Reference](#h2-14)

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