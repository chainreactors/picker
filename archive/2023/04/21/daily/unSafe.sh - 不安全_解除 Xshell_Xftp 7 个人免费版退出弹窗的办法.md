---
title: 解除 Xshell/Xftp 7 个人免费版退出弹窗的办法
url: https://buaq.net/go-159693.html
source: unSafe.sh - 不安全
date: 2023-04-21
fetch_date: 2025-10-04T11:32:25.786277
---

# 解除 Xshell/Xftp 7 个人免费版退出弹窗的办法

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

![](https://8aqnet.cdn.bcebos.com/6e4812028432e627a7e151fe310f239c.jpg)

解除 Xshell/Xftp 7 个人免费版退出弹窗的办法

2022年NetSarang开发的著名SSH工具Xshell/Xftp，修改了免费版的规则，终于不再限制标签页个数了！但是在退出Xshell/Xftp的
*2023-4-20 23:18:54
Author: [blog.upx8.com(查看原文)](/jump-159693.htm)
阅读量:65
收藏*

---

![](https://cnboy.org/wp-content/uploads/f23bcf3bab29da2.png)

2022年NetSarang开发的著名SSH工具Xshell/Xftp，修改了免费版的规则，终于不再限制标签页个数了！但是在退出Xshell/Xftp的时候却增加了广告弹窗。

有不少朋友选择利用火绒的弹窗拦截对弹窗进行拦截。但是在拦截的时候，弹窗会闪现一下，对于强迫症用户还是有点不完美。今天我们就来介绍另一种方法：直接修改可执行文件，彻底解决弹窗问题！

## 准备工作

1、电脑已安装[Xshell/Xftp 7](https://www.netsarang.com/en/free-for-home-school/)，**且运行过一次**

2、window下的编程/调试程序，这里推荐2个：

* UltraEdit桌面版（大家自行搜索开心版。当然试用版也可以，这里就只用这一次，用完卸载，之后有需要再安装又能继续试用）

本教程以HexEd为例，UltraEdit的修改方式与其类似。

## 修改步骤

1、找到 Xshell 7 图标，右键 –  打开文件所在的位置 – 找到 **Xshell.exe**（建议备份该执行文件）

![](https://cnboy.org/wp-content/uploads/c04c2d1d082c0cb.png)

2、打开[HexEd在线平台](https://hexed.it/)，左上角【**打开文件**】，选择 **Xshell.exe**文件，然后查找：

`74 11 6A 00 6A 07 6A 01`

将第一位的**`74`**替换为**`EB`**，修改后的结果为：

`EB 11 6A 00 6A 07 6A 01`

![](https://cnboy.org/wp-content/uploads/27c36035e9469f1.png)

3、选择左上角的【**另存为**】，覆盖原文件即可！

4、参照上面同样的步骤对 **Xftp.exe** 文件按以下代码进行修改完成保存即可。

`75 10 6A 00 6A 07 50 6A`

将第一位**`74`**替换为**`EB`**，修改为：

`EB 10 6A 00 6A 07 50 6A`。

至此，全部修改完毕。再打开Xshell/Xftp 7，然后关闭。是不是不仅没有弹窗，也看不到闪现的情况了。

文章来源: https://blog.upx8.com/3430
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)