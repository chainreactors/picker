---
title: Magic Wormhole 魔法虫洞 – 安全地将文件从一台计算机转移到另一台计算机
url: https://buaq.net/go-257971.html
source: unSafe.sh - 不安全
date: 2024-08-25
fetch_date: 2025-10-06T18:02:03.465277
---

# Magic Wormhole 魔法虫洞 – 安全地将文件从一台计算机转移到另一台计算机

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

![](https://8aqnet.cdn.bcebos.com/251dca36ffbb480c22b980993744973b.jpg)

Magic Wormhole 魔法虫洞 – 安全地将文件从一台计算机转移到另一台计算机

Home在线应用Magic Wormhole 魔法虫洞 – 安全地将文件从一台计算机转移到另一台计算机
*2024-8-24 18:21:44
Author: [www.appinn.com(查看原文)](/jump-257971.htm)
阅读量:27
收藏*

---

[Home](https://www.appinn.com)

[在线应用](https://www.appinn.com/category/online-tools/)

Magic Wormhole 魔法虫洞 – 安全地将文件从一台计算机转移到另一台计算机

**Magic Wormhole** 是一个十分复杂，但使用却又非常简单的开源**跨平台文件传输工具**，它可以安全的将文本、文件或者目录从一台计算机转移到另一台计算机，支持 Windows、macOS、Linux，命令行工具。@[Appinn](https://www.appinn.com/magic-wormhole/)

![Magic Wormhole 魔法虫洞 - 安全地将文件从一台计算机转移到另一台计算机](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-feature-images-2024-08-24T175607.875.jpg "Magic Wormhole 魔法虫洞 - 安全地将文件从一台计算机转移到另一台计算机 1")

## Magic Wormhole 魔法虫洞

Magic Wormhole 的使用是非常简单的，在需要传输文件的两台计算机上都安装之后，先发送：

```
$ wormhole send appinn.pdf
```

![Magic Wormhole 魔法虫洞 - 安全地将文件从一台计算机转移到另一台计算机 1](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-2024-08-24-17.58.31@2x.avif "Magic Wormhole 魔法虫洞 - 安全地将文件从一台计算机转移到另一台计算机 2")

然后你会得到一个传输代码，只需要在接受端输入：

```
$ wormhole receive 9-businessman-sentence
```

就可以了。

Magic Wormhole 自带了**邮件服务器**与**中继服务器**用来做这件事情，并提到：

> 公共服务器的 URL 作为默认使用，并且将免费提供，直到大量或滥用使其变得不可用。邮件服务器对小型密钥交换和控制消息执行存储转发传递。批量数据通过直接 TCP 连接或通过[中转中继](https://github.com/magic-wormhole/magic-wormhole-transit-relay)发送。

## 获取

* [GitHub](https://github.com/magic-wormhole/magic-wormhole)
* [下载](https://magic-wormhole.readthedocs.io/en/latest/welcome.html#installation)

关于传输的文件，仅在收件人下载该文件时才通过中继服务器（如果需要中继），并且文件端到端加密的，并不会存储在服务器上。

### 另外…

如果说，这真的是一款简单的工具，那么介绍到此就结束了。但当我看到开发者为了它，还做了一个30多分钟的[演讲](https://youtu.be/oFrTqQw0_3c)、几万字的[文档](https://magic-wormhole.readthedocs.io/en/latest/)，还真是…很能写啊 😂

通过 Magic Wormhole 协议创建的魔法虫洞生态系统，目前已经有不少应用了：

* [Warp](https://apps.gnome.org/Warp/)是一个用 Rust 编写的 GNOME GUI
* [Winden](https://winden.app/)是一个 Web 客户端和部署（通过 WASM 使用 Go 实现）
* [Destiny](https://f-droid.org/packages/com.leastauthority.destiny/)是一款使用 Flutter（使用 Go 实现虫洞）的 Android（和 iOS）应用程序。也在专有应用商店上。
* Android 版[虫洞](https://gitlab.com/lukas-heiligenbrunner/wormhole)。基于 Rust 实现。
* [Mobile Wormhole](https://github.com/pavelsof/mobile-wormhole) for Android（也在[f-droid上](https://github.com/pavelsof/mobile-wormhole)。基于Python实现，使用Kivy）
* 适用于 Android 和 iOS 的 [Wormhole William Mobile](https://github.com/psanford/wormhole-william-mobile)
* [Rymdport](https://github.com/Jacalz/rymdport)是一个基于 wormhole-william 的跨平台图形桌面应用程序。

并且可以集成道一些应用程序中（比如 [tmux-wormhole](https://github.com/gcla/tmux-wormhole) 一个 tmux 插件，允许在 tmux 会话中使用文件传输（基于 Go 实现））

---

文章来源: https://www.appinn.com/magic-wormhole/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)