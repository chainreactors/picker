---
title: 解决Debian系统环境中文乱码的问题 检查设置UTF-8编码
url: https://buaq.net/go-146862.html
source: unSafe.sh - 不安全
date: 2023-01-28
fetch_date: 2025-10-04T05:02:58.478466
---

# 解决Debian系统环境中文乱码的问题 检查设置UTF-8编码

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

![](https://8aqnet.cdn.bcebos.com/07c90cfae5860aa5cbee28ecfa76d00d.jpg)

解决Debian系统环境中文乱码的问题 检查设置UTF-8编码

晚上升级mdserver-web面板，出现了乱码，应该是开发者干掉debian编码设置影响的。此时，需要重新设置编码格式。#如果在安装Debian时编码
*2023-1-27 23:15:0
Author: [blog.upx8.com(查看原文)](/jump-146862.htm)
阅读量:22
收藏*

---

晚上升级[mdserver-web](https://blog.upx8.com/3051)面板，出现了乱码，应该是开发者干掉debian编码设置影响的。此时，需要重新设置编码格式。

#如果在安装Debian时编码选择不正确，可能会导致终端输出的提示内容是乱码。

在终端输入命令：dpkg-reconfigure locales

这时候会弹出编码列表

![](https://imgsrc.baidu.com/super/pic/item/3912b31bb051f819367c218c9fb44aed2f73e79f.jpg)

选中下面1项（光标移上去，空格选中）：**zh\_CN.UTF-8 UTF-8 ，**按tab键，切换到下面的确定按钮（确定按钮也可能是乱码，左边那个是），回车。

![](https://imgsrc.baidu.com/super/pic/item/4f4a20a4462309f7713e8fd4370e0cf3d6cad6a7.jpg)

此时，让你选择默认的编码，选择**zh\_CN.UTF-8**。

回车后，成功后**重启**即可。

文章来源: https://blog.upx8.com/3202
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)