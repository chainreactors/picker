---
title: 如何实现全部 QQ 群相册批量下载
url: https://buaq.net/go-143674.html
source: unSafe.sh - 不安全
date: 2023-01-02
fetch_date: 2025-10-04T02:52:00.657332
---

# 如何实现全部 QQ 群相册批量下载

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

![](https://8aqnet.cdn.bcebos.com/fe3797eb7d8b8c1035d4eb9cd7b1984b.jpg)

如何实现全部 QQ 群相册批量下载

*2023-1-1 14:46:24
Author: [www.appinn.com(查看原文)](/jump-143674.htm)
阅读量:36
收藏*

---

**QQ群相册批量下载** 是一款可以实现批量下载所有群相册的油猴脚本，支持迅雷。@[Appinn](https://www.appinn.com/qqgroup-album-batch-download/)

![如何实现全部 QQ 群相册批量下载](https://static1.appinn.com/images/202212/qqqun.jpg!o "如何实现全部 QQ 群相册批量下载 1")

QQ 群相册本身就可以批量下载单个相册的全部照片，但如果群里有很多相册，也比较麻烦。青小蛙最近就遇到里这个问题。于是发现了这个油猴脚本。

## QQ群相册批量下载

这是一个模拟用户点击每个群相册下载的油猴脚本，安装之后会在网页版群相册界面出现几个按钮：

![如何实现全部 QQ 群相册批量下载 1](https://static1.appinn.com/images/202212/bwmpji.jpg!o "如何实现全部 QQ 群相册批量下载 2")

点击批量下载就好了，浏览器会提示是否允许下载多个文件，允许就好。

脚本功能很简单，就是模拟点击，并且只有一键下载所有相册功能，别无其它。

### 使用说明

将**QQ群号**修改成需要下载的QQ群号：

`https://h5.qzone.qq.com/groupphoto/index?inqq=1&groupId=QQ群号https://h5.qzone.qq.com/groupphoto/album?inqq=1&groupId=QQ群号https://h5.qzone.qq.com/groupphoto/index?inqq=3&groupId=QQ群号https://h5.qzone.qq.com/groupphoto/album?inqq=3&groupId=QQ群号`

稍等片刻就能下载打包好的 zip 文件了。

另外如果安装有迅雷，可以直接发送给迅雷，或者复制链接，使用其他下载工具（比如 [aria2](https://www.appinn.com/tag/aria2/)）

## 获取

* [GreasyFork](https://greasyfork.org/zh-CN/scripts/440970-qq%E7%BE%A4%E7%9B%B8%E5%86%8C%E6%89%B9%E9%87%8F%E4%B8%8B%E8%BD%BD)

原文：https://www.appinn.com/qqgroup-album-batch-download/

文章来源: https://www.appinn.com/qqgroup-album-batch-download/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)