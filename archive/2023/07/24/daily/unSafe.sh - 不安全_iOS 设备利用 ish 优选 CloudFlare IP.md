---
title: iOS 设备利用 ish 优选 CloudFlare IP
url: https://buaq.net/go-172721.html
source: unSafe.sh - 不安全
date: 2023-07-24
fetch_date: 2025-10-04T11:51:02.510366
---

# iOS 设备利用 ish 优选 CloudFlare IP

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

![](https://8aqnet.cdn.bcebos.com/d4d4d33e2ce559c4625f2f147ceeca29.jpg)

iOS 设备利用 ish 优选 CloudFlare IP

在之前的教程中，我介绍了两位开源大佬的优选工具。但是对于一些没有电脑的部分读者来说，优 cf 的 ip 的操作会变得有一些困难。这篇文章中，我来和大家介
*2023-7-23 17:24:0
Author: [blog.upx8.com(查看原文)](/jump-172721.htm)
阅读量:81
收藏*

---

在之前的教程中，我介绍了两位开源大佬的优选工具。但是对于一些没有电脑的部分读者来说，优 cf 的 ip 的操作会变得有一些困难。这篇文章中，我来和大家介绍利用 ish 终端，使用犯罪高手这位开源大佬的优选工具来优选 cf 的 ip

## 准备材料

* iOS 设备

## 优选步骤

> 注意：请在开始优选前，断开所有的代理工具，否则会导致结果不准

1. 打开 ish，输入以下命令安装依赖

2. 输入以下命令，下载优选代码并运行

3. 如为移动用户，由于项目依赖地址可能被移动SNI阻断，请手动创建四个文件，分别为`colo.txt`、`ips-v4.txt`、`ips-v6.txt`和`url.txt`，内容在以下的链接内，其他运营商用户如无法下载可以使用本步骤

`colo.txt`：`wget https://www.baipiao.eu.org/cloudflare/colo -O colo.txt`

`ips-v4.txt`：`wget https://www.baipiao.eu.org/cloudflare/ips-v4 -O ips-v4.txt`

`ips-v6.txt`：`wget https://www.baipiao.eu.org/cloudflare/ips-v6 -O ips-v6.txt`

`url.txt`：`wget https://www.baipiao.eu.org/cloudflare/url -O url.txt`

4. 第一次执行的时候会下载依赖文件，如无特殊意外的话会来到主界面。根据自己的需要，选择对应的选项进行优选。输入设置的带宽值（不需要最低也不需要太高，适中即可）及测试线程数

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230718175945.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230718175945.png)

5. 等待一会之后，程序将会显示最优的 cf ip。

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230718180319.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230718180319.png)

文章来源: https://blog.upx8.com/3705
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)