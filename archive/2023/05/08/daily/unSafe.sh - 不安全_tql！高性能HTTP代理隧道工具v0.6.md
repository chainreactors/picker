---
title: tql！高性能HTTP代理隧道工具v0.6
url: https://buaq.net/go-162115.html
source: unSafe.sh - 不安全
date: 2023-05-08
fetch_date: 2025-10-04T11:37:15.808725
---

# tql！高性能HTTP代理隧道工具v0.6

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

![](https://8aqnet.cdn.bcebos.com/e6b128a01ee4207e17e56e0031e56ed7.jpg)

tql！高性能HTTP代理隧道工具v0.6

声明：该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与
*2023-5-7 15:13:44
Author: [mp.weixin.qq.com(查看原文)](/jump-162115.htm)
阅读量:85
收藏*

---

**声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。

请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

现在只对常读和星标的公众号才展示大图推送，建议大家把潇湘信安“设为星标”，否则可能看不到了！

**工具简介**

suo5是一个全新的HTTP代理隧道，基于HTTP/1.1的Chunked-Encoding构建。相比Neo-reGeorg等传统隧道工具，suo5的性能可以达到其数十倍。

![](https://mmbiz.qpic.cn/mmbiz_gif/XOPdGZ2MYOfMwvtOrRUHOo3nMFDWw00FtXLTPBQhLyXwHyX9GnkyDn5oXhvgxyc9EzkJVP5DfqXkmqDiaAd15vA/640?wx_fmt=gif)

其主要特性如下：

```
同时支持全双工与半双工模式，传输性能接近 FRP支持在 Nginx 反向代理和负载均衡场景使用完善的连接控制和并发管理，使用流畅丝滑支持 Tomcat Jetty Weblogic Resin 等主流中间件支持 Java4 ~ Java 19 全版本同时提供提供命令行和图形化界面
```

**安装使用**

带 gui 的版本是界面版，不带 gui 的为命令行版。所有编译由 Github Action 自动构建，请放心使用。

使用时需上传 suo5.jsp 到目标环境中并确保可以执行。

### **界面版**

界面版基于 wails 实现，依赖 Webview2 框架。Windows 11 和 MacOS 已自带该组件，其他系统会弹框请允许下载安装，否则无法使用。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfMwvtOrRUHOo3nMFDWw00FGeYnVr1eczuIhlnSY6KRzYMkjUqPkVH6bwFfQVaBibs8zyvAj9uu7dg/640?wx_fmt=png)

### **命令行版**

```
USAGE:   suo5 [global options] command [command options] [arguments...]
VERSION:   v0.6.0
COMMANDS:   help, h  Shows a list of commands or help for one command
GLOBAL OPTIONS:   --target value, -t value                               set the remote server url, ex: http://localhost:8080/tomcat_debug_war_exploded/   --listen value, -l value                               set the listen address of socks5 server (default: "127.0.0.1:1111")   --method value, -m value                               http request method (default: "POST")   --redirect value, -r value                             redirect to the url if host not matched, used to bypass load balance   --no-auth                                              disable socks5 authentication (default: true)   --auth value                                           socks5 creds, username:password, leave empty to auto generate   --mode value                                           connection mode, choices are auto, full, half (default: "auto")   --ua value                                             the user-agent used to send request (default: "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.1.2.3")   --header value, -H value [ --header value, -H value ]  use extra header, ex -H 'Cookie: abc'   --timeout value                                        http request timeout in seconds (default: 10)   --buf-size value                                       set the request max body size (default: 327680)   --proxy value                                          use upstream socks5 proxy   --debug, -d                                            debug the traffic, print more details (default: false)   --no-heartbeat, --nh                                   disable heartbeat to the remote server which will send data every 5s (default: false)   --help, -h                                             show help   --version, -v                                          print the version
```

命令行版本与界面版配置完全一致，可以对照界面版功能来使用，最简单的只需指定连接目标

```
$ ./suo5 -t https://example.com/proxy.jsp
```

使用 GET 方法发送请求，有时可以绕过限制

```
$ ./suo5 -m GET -t https://example.com/proxy.jsp
```

自定义 socks5 监听在 0.0.0.0:7788，并自定义认证信息为 test:test123

```
$ ./suo5 -t https://example.com/proxy.jsp -l 0.0.0.0:7788 --auth test:test123
```

负载均衡场景下将流量转发到某一个固定的 url 解决请求被分散的问题 (需要尽可能的在每一个后端服务中上传 suo5)

```
$ ./suo5 -t https://example.com/proxy.jsp -t http://172.0.3.2/code/proxy.jsp
```

### **特别提醒**

User-Agent (ua) 的配置本地端与服务端是绑定的，如果修改了其中一个，另一个也必须对应修改才能连接上。

**下载地址**

**点击下方名片进入公众号**

**回复关键字【****230224****】获取****下载链接**

---

文章来源: http://mp.weixin.qq.com/s?\_\_biz=Mzg4NTUwMzM1Ng==&mid=2247503353&idx=1&sn=76d7bacb29d0bba9ec72d3b200a8f96e&chksm=cfa569eaf8d2e0fc7fbfb6b361f217a92d6ec00d65ce217e4bca688cee588e597ffc974f6ea0&mpshare=1&scene=1&srcid=05076EYkJYHpECyylELmCMla&sharer\_sharetime=1683443608547&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)