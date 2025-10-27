---
title: 反混淆Shell脚本的一种思路
url: https://buaq.net/go-165949.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:04.886422
---

# 反混淆Shell脚本的一种思路

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

![](https://8aqnet.cdn.bcebos.com/4144bb17d13c53061131fbcb51f73963.jpg)

反混淆Shell脚本的一种思路

最后编辑时间: 2023-05-26（New Article）
*2023-5-26 23:29:50
Author: [blog.upx8.com(查看原文)](/jump-165949.htm)
阅读量:54
收藏*

---

最后编辑时间: 2023-05-26（New Article）

在之前，我碰到了一些加密的脚本。于是我通过Core Dump的方法对其进行了代码解密。而最近我在分析代码的时候，发现了另外一种shell脚本。这种脚本的特点就是将代码打乱，使得代码难以分析。于是我利用了调试Shell脚本的命令 `bash -x test.sh` ，通过调试的方法，将Shell脚本进行反混淆。在这里我将思路分享给大家

## 准备材料

* 被混淆的shell脚本

## 部署步骤

1. 分析将反混淆的脚本，可以看到，第一和第二行是利用了无规律的变量名，将脚本内容分开存放于其中，第三行是利用了 `eval` 方法，调用其变量的值

![](https://img.imgdd.com/f210f3.0b6b584d-a1d3-4ca7-9822-136daa2d60b6.png)

2. 运行Shell脚本的调试命令，将脚本的内容显示出来

```
bash -x test.sh
```

3. 可以看到，代码的真面貌就完全显示出来了

![](https://img.imgdd.com/f210f3.dabf2e24-100f-451d-a498-8a8c6f992d34.png)

文章来源: https://blog.upx8.com/3592
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)