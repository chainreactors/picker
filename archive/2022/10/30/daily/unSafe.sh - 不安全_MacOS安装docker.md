---
title: MacOS安装docker
url: https://buaq.net/go-133270.html
source: unSafe.sh - 不安全
date: 2022-10-30
fetch_date: 2025-10-03T21:17:20.008238
---

# MacOS安装docker

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

![]()

MacOS安装docker

MacOS之前都是在服务器上跑docker，最近在家使用 ssh 连接国外 VPS 经常被干扰(可能是免费的移动宽带加强了局域网管制！)，想到简单的东西直接在本地跑得了，省的被网络影响心情。在终端敲
*2022-10-29 22:39:41
Author: [itlanyan.com(查看原文)](/jump-133270.htm)
阅读量:32
收藏*

---

[MacOS](https://itlanyan.com/category/macos/)

之前都是在服务器上跑docker，最近在家使用 [ssh](https://itlanyan.com/tag/ssh/) 连接国外 [VPS](https://itlanyan.com/vps-merchant-collection/) 经常被干扰(可能是免费的移动宽带加强了局域网管制！)，想到简单的东西直接在本地跑得了，省的被网络影响心情。

在终端敲入`docker`命令，竟然有该命令，但是没记得之前安装过啊！好吧，看看之前都倒腾过啥：`docker images`，结果竟是：

```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

看起来是daemon服务端没运行。继续查看服务：`brew services`，没显示有dockerd服务；用spotlight查找docker也无任何结果，这说明只有客户端client？更大的可能是这是系统自带的客户端工具？

上网一查，还真是只有一个客户端，那就完整的安装一套docker吧！

```
brew remove docker
brew install --cask docker
```

因为已经存在了docker客户端，所以要先运行第一条命令卸载，否则安装过程中会报如下错误：

```
Error: It seems there is already a Binary at '/usr/local/share/zsh/site-functions/_docker'.
```

安装完后，从启动台里找到docker的小蓝鲸图标，点击启动并按照要求输入电脑密码安装组件，docker就可以用了。

跑一个熟悉的Debian镜像当作虚拟机：

```
$ docker run -it debian /bin/bash

Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
17c9e6141fdb: Pull complete
Digest: sha256:bfe6615d017d1eebe19f349669de58cda36c668ef916e618be78071513c690e5
Status: Downloaded newer image for debian:latest
```

一切正常。

## 参考

1. [Error: It seems there is already a Binary installing docker cask with homebrew](https://www.weplayinternet.com/posts/error-it-seem-there-is-already-a-binary/)
2. [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)

打赏赞

文章来源: https://itlanyan.com/install-docker-macos/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)