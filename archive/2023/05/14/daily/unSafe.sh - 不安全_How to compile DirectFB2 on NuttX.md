---
title: How to compile DirectFB2 on NuttX
url: https://buaq.net/go-163221.html
source: unSafe.sh - 不安全
date: 2023-05-14
fetch_date: 2025-10-04T11:37:21.707879
---

# How to compile DirectFB2 on NuttX

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

How to compile DirectFB2 on NuttX

Skip to contentRecently Nicolas Carameli from DirectFB2 project ported i
*2023-5-13 22:34:41
Author: [acassis.wordpress.com(查看原文)](/jump-163221.htm)
阅读量:51
收藏*

---

[Skip to content](#content)

Recently Nicolas Carameli from DirectFB2 project ported it to NuttX: [see here](https://github.com/directfb2/DirectFB2/pull/107/commits/d11102daba0af1f75339d9a27b3b5c9eba242884).

Today I decided to test it and to create a tutorial to help other people to do the same!

First we need to compile the fluxcomp tool that is not integrated on Ubuntu yet:

```
$ sudo apt install libdirectfb-dev

$ mkdir ~/TropDirect

$ cd ~/TropDirect

$ git clone https://github.com/deniskropp/flux
Cloning into 'flux'…
remote: Enumerating objects: 329, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 329 (delta 0), reused 3 (delta 0), pack-reused 325
Receiving objects: 100% (329/329), 73.65 KiB | 897.00 KiB/s, done.
Resolving deltas: 100% (201/201), done.

$ cd flux/

$ ./autogen.sh

$ ./configure

$ make

$ sudo make install
```

Now you can clone NuttX, NuttX Apps and DirectFB2 and compile everything:

```
$ mkdir ~/nuttxspace

$ cd ~/nuttxspace

$ git clone https://github.com/apache/nuttx

$ git clone https://github.com/apache/nuttx-apps apps

$ cd apps/graphics

$ git clone https://github.com/directfb2/DirectFB2

$ cd ~/nuttxspace

$ cd nuttx

$ ./tools/configure.sh sim:nsh

$ make menuconfig

Application Configuration --->
    Graphics Support --->
        [*] DirectFB2 ----

$ make -j
```

As you can see the compilation worked fine, now you can use the DirectFB2 to port your Linux Applications to NuttX! \o/

文章来源: https://acassis.wordpress.com/2023/05/13/how-to-compile-directfb2-on-nuttx/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)