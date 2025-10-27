---
title: 网站访客统计PHP源码
url: https://buaq.net/go-148959.html
source: unSafe.sh - 不安全
date: 2023-02-12
fetch_date: 2025-10-04T06:25:22.790555
---

# 网站访客统计PHP源码

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

网站访客统计PHP源码

前言一个简单统计网站访客的PHP源码，实现前端网页显示访问量采用PV统计方式，单个用户连续点击N篇文章，记录N次访问量源码会自动生成TXT记录文档
*2023-2-11 17:52:0
Author: [blog.upx8.com(查看原文)](/jump-148959.htm)
阅读量:24
收藏*

---

## 前言

* 一个简单统计网站访客的`PHP`源码，实现前端网页显示访问量
* 采用`PV`统计方式，单个用户连续点击`N`篇文章，记录`N`次访问量
* 源码会自动生成`TXT`记录文档，记录的访问量可以自行修改

## 源码

在网站根目录新建一个名为`FKTJ.php`的文件，然后写入以下代码

```
<?php
$n=file_get_contents('FKTJ.txt');
$n++;
file_put_contents('FKTJ.txt',$n);
echo "document.write($n);";
?>
```

在需要显示的地方添加以下调用代码

```
你是第<script type=text/javascript src=FKTJ.php></script>位访问者
```

## 说明

加入调用代码后打开网页，会在后台生成一个名为`FKTJ.txt`的记录文件，编辑此文件可以实现修改访问量

文章来源: https://blog.upx8.com/3220
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)