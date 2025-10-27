---
title: Linux安装lolcat彩虹特效工具
url: https://buaq.net/go-173205.html
source: unSafe.sh - 不安全
date: 2023-07-30
fetch_date: 2025-10-04T11:50:55.305143
---

# Linux安装lolcat彩虹特效工具

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

![](https://8aqnet.cdn.bcebos.com/159d3f7e15f1c749c03443bf1440db8e.jpg)

Linux安装lolcat彩虹特效工具

什么是lolcat？Lolcat是用于Linux，BSD和OSX的实用程序，其连接方式类似于cat命令，并为其添加了彩虹颜色。Lolcat主要为Linu
*2023-7-29 23:3:57
Author: [blog.upx8.com(查看原文)](/jump-173205.htm)
阅读量:41
收藏*

---

#### 什么是lolcat？

Lolcat是用于Linux，BSD和OSX的实用程序，其连接方式类似于cat命令，并为其添加了彩虹颜色。Lolcat主要为Linux终端中的文本添加彩虹般的颜色。

#### 在Linux中安装Lolcat

由于 Lolcat 是一个 ruby gem 程序，所以在你的系统中必须安装有最新版本的 ruby。

`apt-get install ruby`    [在基于 APT 的系统中]

接下来，使用以下命令从git存储库下载并安装最新版本的lolcat。

`wget https://github.com/busyloop/lolcat/archive/master.zip`

`unzip master.zip`

`cd lolcat-master/bin`

`gem install lolcat`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_20-49-50.png)

安装lolcat后，使用以下命令检查lolcat版本。

`lolcat -v`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_20-48-07.png)

#### Lolcat帮助文档

`lolcat -h`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_20-51-36.png)

**给文本赋予彩虹颜色的动画:**

`echo Hello World 2022 | lolcat -a -d 200`

![](https://loukas.cn/wp-content/uploads/2022/02/dklw6-qlulc.gif)

这里选项 -a 指的是 Animation(动画)， -d 指的是 duration(持续时间)。在上面的例子中，持续 200 次动画。

**配合neofetch使用:**

`apt-get install neofetch`

`neofetch | lolcat`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-07_21-09-46.png)

文章来源: https://blog.upx8.com/3724
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)