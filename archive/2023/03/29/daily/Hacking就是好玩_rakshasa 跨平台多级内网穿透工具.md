---
title: rakshasa 跨平台多级内网穿透工具
url: https://mp.weixin.qq.com/s?__biz=MzU2NzcwNTY3Mg==&mid=2247484755&idx=1&sn=fab8225f7bbd4b27419491cf0a7f7991&chksm=fc986c74cbefe56287ac6038d4ef339782a80b471d3b30a2d90cc27b6714ad48ed2d3f6f2a68&scene=58&subscene=0#rd
source: Hacking就是好玩
date: 2023-03-29
fetch_date: 2025-10-04T11:02:06.660898
---

# rakshasa 跨平台多级内网穿透工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eLgL5R4W3FjMT0nZH5qKmAyP1gZuLCrFxAoNY72a8qzBFku2Kc8qvPsD2apFt5JyQQW4AhF1aETOibYzAJicQaTA/0?wx_fmt=jpeg)

# rakshasa 跨平台多级内网穿透工具

Mob2003

Hacking就是好玩

推荐群友的一个开源作品，文末模仿了一下播客交谈的形式，和作者聊了开发软件背后的故事。

## rakshasa

rakshasa是一个使用Go语言编写的强大多级代理工具，专为实现多级代理，内网穿透而设计。它可以在节点群里面任意两个节点之间转发TCP请求和响应，同时支持socks5代理，http代理，并且可以引入外部http、socks5代理池，自动切换请求IP。

节点之间使用内置证书的TLS加密TCP通讯，再叠加一层自定义秘钥的AES加密，可以在所有Go支持的平台使用。可以在你所有的的Windows和Linux服务器上搭建节点并组成节点群网络。

## 功能

* 自动实现多层代理
* 支持Tcp转发代理。
* 支持Tcp反向代理
* 支持Socks5代理        （包含UDP和TCP6）
* 支持Socks5反向代理
* 支持HTTP代理           （爬虫利器，流量出口支持代理池）
* 去中心化。
* 支持多个节点连接。
* 支持配置文件，可以配置代理服务器的端口、目标服务器的地址和端口、证书文件等信息。
* 支持日志记录，记录代理服务器的请求和响应信息。
* CLI模式实现远程Shell。
* 执行shellcode。

## 编译与使用

首先生成证书：

```
cd gencert
go run main.go
cd ../
```

也可以使用其他工具生成证书，将 server.crt 和 server.key 放到 cert 目录下。然后再编译rakshasa

```
go build
```

在 Windows 下使用cmd跨平台编译 Linux 示例：

```
cd gencert
go run main.go
cd ../
set GOOS=linux
go build
```

## 使用图示

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjMT0nZH5qKmAyP1gZuLCrFrfG1eUGlPdiaa3sh76Sko2gfPFRSAsQx1fJKvWva2cwLkqcJibAY8P4g/640?wx_fmt=png)

## 交谈

最近再看一些播客，想用播客交流的形式问了作者一些问题。

### Q:为什么写rakshasa

渗透中经常会遇到使用.NET反射、代理池、内网转发等软件，频繁切换这些工具很麻烦，因此我自己写了一个内网软件，支持以上功能。我一共写了四个软件，其中之一是Rakshasa，另外还有一个Rust的内网扫描器、Rust Beacon、以及C2。

### Q:在写多级代理的时候有没有遇到什么困难，算法，编程方面的

在编写多级代理时，有一些困难。有人让我我支持UDP，但我认为国内会强。另外我写的那个Shellcode命令执行,使用Amssly和Donut使用的 .NET集合不同，我的可以带参数执行Shellcode命令。我还要实现节点上线广播、节点消息转发，以及解决广播风暴的问题，不过这些不困难。

### Q:这个软件还有哪些自己不满意或之后想优化的地方吗

有一点吧，考虑做一个mini版本，把文件上传，命令执行，节点，这些东西都删了，只留一个转发功能。
而且目前各节点是使用tcp传输的，测试环境也是以tcp为主，后面想要优化支持udp，icmp。受到我自己先入为主的思维影响，早期测试时候udp掉包厉害

### Q:在一些特殊的场景，一个节点要经过好几个节点才能出网，rakshasa有这类的解决方案吗，是怎么做到的

对于一些特殊场景，例如节点需要经过多个节点才能出网，Rakshasa有解决方案。
只要每个节点能够连通，就可以出网。

例如节点1是内网，通过-D参数连接节点2、节点3和节点4，即节点1 → 节点2 → 节点3 → 节点4（外网）。在节点内会生成类似于键值对的节点关系表，例如在节点1内，是节点2-节点2、节点3-节点2和节点4-节点2，这表示请求节点2、3和4的数据包都发送到节点2。

如果节点1发送请求到节点4的socks5，那么根据映射表（节点4-节点2），其数据包将被发往节点2，节点2根据映射表（节点4-节点3）将其发往节点3，最终到达节点4。节点4会根据Socks5包含的外网IP请求外网。

## 开源地址

开源地址：https://github.com/Mob2003/rakshasa ，点击阅读全文也能跳转到

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjHty0EhJ3ohRK5fgibRAto40C8GWzr2qkcQTpsQr3YSmiaWSxJsliaX7qic9zVVpU7YcKrgFuXPzjBDg/0?wx_fmt=png)

Hacking就是好玩

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjHty0EhJ3ohRK5fgibRAto40C8GWzr2qkcQTpsQr3YSmiaWSxJsliaX7qic9zVVpU7YcKrgFuXPzjBDg/0?wx_fmt=png)

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