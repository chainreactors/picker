---
title: 在Ubuntu系统上编译安装最新版本Python 3
url: https://buaq.net/go-162177.html
source: unSafe.sh - 不安全
date: 2023-05-08
fetch_date: 2025-10-04T11:37:04.731696
---

# 在Ubuntu系统上编译安装最新版本Python 3

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

在Ubuntu系统上编译安装最新版本Python 3

在我们使用Ubuntu系统的过程中，一般系统自带的Python 3就已经够用了。但是由于某些软件包需要使用最新版本的Python 3，所以说我们需要更新
*2023-5-7 23:26:0
Author: [blog.upx8.com(查看原文)](/jump-162177.htm)
阅读量:28
收藏*

---

在我们使用Ubuntu系统的过程中，一般系统自带的Python 3就已经够用了。但是由于某些软件包需要使用最新版本的Python 3，所以说我们需要更新系统自带的Python 3的版本。在这篇文章中，我来和大家一起来了解、编译安装最新版本的Python 3

## 准备材料

* Ubuntu 系统

## 部署步骤

1. SSH进入控制台
2. 输入以下命令，更新系统组件

apt-get update

apt-get upgrade -y

3. 输入以下代码，下载最新版本Python 3源码包，并解压

wget -N https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tar.xz

4. 输入以下代码，以优化性能

./configure --enable-optimizations

5. 输入以下命令，编译并安装Python 3

sudo make

sudo make altinstall

6. 输入以下命令，验证安装是否成功

type -P python3.11.3

文章来源: https://blog.upx8.com/3518
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)