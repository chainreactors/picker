---
title: Fuzzing 101 with LibAFL 学习（一）
url: https://buaq.net/go-260760.html
source: unSafe.sh - 不安全
date: 2024-09-08
fetch_date: 2025-10-06T18:22:42.126429
---

# Fuzzing 101 with LibAFL 学习（一）

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

![](https://8aqnet.cdn.bcebos.com/74322c1fc3535ce8e674091e64f47245.jpg)

Fuzzing 101 with LibAFL 学习（一）

参考 Fuzzing101 with LibAFL - Part I: Fuzzing Xpdf1 和 Fuzzing101 with LibAFL - Part I.V: Speed Improve
*2024-9-7 23:15:50
Author: [5ec.top(查看原文)](/jump-260760.htm)
阅读量:24
收藏*

---

参考 Fuzzing101 with LibAFL - Part I: Fuzzing Xpdf[1](#user-content-fn-libafl-1) 和 Fuzzing101 with LibAFL - Part I.V: Speed Improvements to Part I[2](#user-content-fn-libafl-2) 做一下笔记。libafl 的自由度相当高，我觉得学习路线会比较陡峭，这一次我就不求甚解一波。

## 复现

先下载 xpdf

```
cd fuzzing-101-solutions/exercise-1
wget https://dl.xpdfreader.com/old/xpdf-3.02.tar.gz
tar xvf xpdf-3.02.tar.gz
rm xpdf-3.02.tar.gz
mv xpdf-3.02 xpdf
```

build.rs 本质上是做了如下工作：

```
# these are example commands that will be executed automatically by build.rs
# and were taken almost verbatim from Fuzzing101's README
cd fuzzing-101-solutions/exercise-1/xpdf
make clean
rm -rf install
export LLVM_CONFIG=llvm-config-15
CC=afl-clang-fast CXX=afl-clang-fast++ ./configure --prefix=./install
make
make install
```

具体实现方法之后再看，先照抄。

复制完代码之后发现默认的 libafl 版本是 0.10.1，编译不起来就改成了 0.13.2，结果发现好多东西都变了，比如 `libafl::bolts` 变成了 `libafl_bolts`，还有一个 Executor ：

> We deleted `TimeoutExecutor` and `TimeoutForkserverExecutor` and make it mandatory for `InProcessExecutor` and `ForkserverExecutor` to have the timeout. Now `InProcessExecutor` and `ForkserverExecutor` have the default timeout of 5 seconds.

---

---

文章来源: https://5ec.top/00-notes/00-fuzz/libafl/fuzzing101/study-note-1
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)