---
title: 【突发】国内大量家用路由器网络访问异常和流量劫持事件分析
url: https://mp.weixin.qq.com/s?__biz=MzkyNzcxNTczNA==&mid=2247486584&idx=1&sn=03a1cac7b66eca88493eee29fe840a5a&chksm=c2229481f5551d971935db53798793eaf66ea135623b09ec7fdd6f291b9dca33779995d5c721&scene=58&subscene=0#rd
source: Beacon Tower Lab
date: 2024-08-08
fetch_date: 2025-10-06T18:06:23.806862
---

# 【突发】国内大量家用路由器网络访问异常和流量劫持事件分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8OoibLIQWxP7D3mKsSibZpNGPtNgKJuueV1OaNH5KhfMJMRjHs3k2RvQQ/0?wx_fmt=jpeg)

# 【突发】国内大量家用路由器网络访问异常和流量劫持事件分析

原创

烽火台实验室

Beacon Tower Lab

*以下内容由WebRAY和Panabit联合发布*

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8IJ7nDDJPYaulKf9m7I1BFwyckDDsKPLthBXu9dQgLPCq8kCPQPAClA/640?wx_fmt=png&from=appmsg)

**0x01 事件背景**

从2024年5月开始，国内部分家用路由器开始出现间歇性断网、域名解析延迟高以及解析到海外IP等情况，今年8月该现象变得尤为严重。前几天在做应急响应时候发现某企业暴露在公网上的路由器配置的DNS地址被莫名其妙篡改了，主DNS地址是一个阿里云上的节点，备用DNS地址为1.1.1.1。起初以为这次事件跟近期的攻防演习相关，后面经过深入分析发现该事件并不是个例，我们已排查到有大量暴露在公网上的路由器都存在DNS被篡改的情况，且大部分用户基本没有感知。经过初步统计，攻击者使用的劫持DNS节点数已有百余个，用户访问受影响的目标主要覆盖了阿里云CDN、腾讯云CDN、华为云CDN等，导致了一系列的解析异常。短时间范围内，大量用户投诉对国内重要目标单位访问异常，造成严重安全隐患。

**0x02 事件分析**

盛邦安全烽火台实验室联合Panabit对该事件进行了专项分析，这起事件是属于典型的DNS劫持攻击事件，符合国外黑灰产组织的攻击特征。攻击者通过搜集公网可访问的路由器地址，利用漏洞或弱口令获取路由器控制权限，修改路由器DNS服务器地址，达到中间人攻击的效果。整体的攻击流程如下图所示：

*（图中假设攻击者对webray.com.cn进行了dns劫持）*

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8bOWu8HZ9icqF5IgKlrxxKD3NvamicALL1fZhgoFLSAicTwZySHjh6Hibrw/640?wx_fmt=png&from=appmsg)

用户在发起HTTP请求之前首先会进行DNS请求，由于绝大部分个人用户不会自定义DNS服务器，所以默认情况下会使用路由器的DNS服务器来进行域名解析。攻击者通过漏洞把路由器DNS服务器篡改为自己可控的恶意DNS服务器，并添加解析记录webray.com.cn到恶意IP地址。用户拿到webray.com.cn响应的IP地址之后会与攻击者可控恶意IP建立链接，攻击者可控恶意IP通过实现中间人代理功能，把用户的请求转发的真实目标服务器并响应真实服务器结果给用户。

基于DNS劫持的中间人攻击一般可以造成做到用户无感知，但这个事件还是导致了用户访问异常，从而慢慢发酵了出来，引起用户访问异常的原因有以下两点：

经过攻击者可控的服务器进行代理转发之后，会明显降低系统访问速度，造成访问请求延迟增大。

用户访问https协议的网站目标时，会因为中间人可控服务器没有受信任的证书而导致访问失败。

**0x03 排查过程**

中间人攻击是一种常见的网络攻击方式，一般情况下可以造成下面的两种危害：

造成信息泄漏，通过中间人攻击可以劫持用户流量，通过对流量中的敏感信息进行提取，获取用户认证信息等敏感内容。

造成远程权限获取，通过中间人攻击可以篡改用户流量，一般情况下中间人会把用户请求转发到真实服务器，但是部分情况下可以通过对流量进行篡改达到RCE的效果。其中经典的用法是通过修改软件的升级更新包的响应内容，通过把响应内容替换为木马文件，达到自动运行的效果。

由于事件还在发酵，很难判断攻击者的最终目的是属于流量获取还是远程权限获取。但是不论何种情况，对用户来说都是属于较大的安全隐患。

那么用户应该如何排查自己的DNS服务器是否正常呢？我们把目前的情况做了总结，本次事件中的恶意DNS服务器普遍具有以下特征：

能解析的域名ttl改为了86400秒，即1天

使用unbound-1.16.2作为版本名称

以已知的恶意DNS 60.205.130.150为例，查询DNS服务器中ttl时间，可以通过dig发送任意一个未解析过的域名，此处的daydaymap.com可替换为随机其它域名。

```
dig @60.205.130.150 daydaymap.com
```

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8Jwd153RXBHaicCUGrdNVUoa6xSV23gNGnpKgysxH4lIV77cjHaIHGyw/640?wx_fmt=png&from=appmsg)

查询DNS服务器中版本名称，可以通过dig发送version.bind的txt查询请求，并通过chaos的方式进行展示。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8lYzJyV0IZ3OnyN97cYNZZCBZLibjAicujsv5LTkhU8uuPS8YhBnjQZoQ/640?wx_fmt=png&from=appmsg)

如果满足以上两个特征，基本就可以认定是被劫持的DNS服务器。

**0x04 用户自查**

我们基于以上特征对互联网上的DNS服务器做了全网摸排，情况不容乐观。典型的被劫持IP包括：

```
47.109.22.118.140.204.3947.108.228.5047.103.220.24739.108.114.149120.77.221.246106.15.3.137120.26.147.194106.15.192.10106.14.245.3047.108.190.13847.106.38.9647.100.115.82122.9.187.125120.79.129.19647.108.55.233123.56.132.204101.37.182.110101.201.60.214
```

目前这些IP都还存活，且基本都是国内公有云上的IP，更多被劫持的IP我们会在www.daydaymap.com上陆续公开出来，查看方式如下：

访问DayDayMap首页，点击DNS劫持标签：

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8XLhfDcrWP7D08VKnMsIHIeUnd4g8JYOJhoic1Oj4H1Eo8n3ClpicVxUQ/640?wx_fmt=png&from=appmsg)

点击后会检索语法ip.tag="DNS劫持"，列出已探测到的被篡改的DNS地址：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8E5sfrfkeAM5WjscRwXjEBr0SXvicpyz8ppibMfaBpe0LbHekW2IHIl0JS2pVHanrvibI79J4YeR1qziaLYvGqTn3Q/640?wx_fmt=jpeg&from=appmsg)

用户自查方式：

1、登陆路由器后台，查看现有的DNS配置，如果备用DNS地址已被改为了1.1.1.1，需要尤其引起注意！

2、将主备DNS地址输入www.daydaymap.com进行查询，看是否有“DNS劫持”的标签，如存在该标签，尽快更换路由器并进行终端安全检测。

**0x05 参考文献**

```
https://lovelyping.com/?p=294
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

Beacon Tower Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

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