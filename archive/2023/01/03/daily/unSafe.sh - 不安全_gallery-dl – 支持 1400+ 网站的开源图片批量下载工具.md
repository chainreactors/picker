---
title: gallery-dl – 支持 1400+ 网站的开源图片批量下载工具
url: https://buaq.net/go-143793.html
source: unSafe.sh - 不安全
date: 2023-01-03
fetch_date: 2025-10-04T02:54:33.953861
---

# gallery-dl – 支持 1400+ 网站的开源图片批量下载工具

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

![](https://8aqnet.cdn.bcebos.com/02dcaa16c3f84bf5d69e32c0b62c5ba1.jpg)

gallery-dl – 支持 1400+ 网站的开源图片批量下载工具

*2023-1-2 20:56:10
Author: [www.appinn.com(查看原文)](/jump-143793.htm)
阅读量:42
收藏*

---

gallery-dl 是一款开源命令行工具，它能够从多达 1400+ 个网站批量下载图片与合集，常见有微博、500px、unsplash、imgur 等网站，有一种图片版 [youtube-dl](https://www.appinn.com/?s=youtube-dl) 的感觉。@[Appinn](https://www.appinn.com/gallery-dl/)

![gallery-dl - 支持 1400+ 网站的开源图片批量下载工具](https://static1.appinn.com/images/202301/gallery-dl.jpg!o "gallery-dl - 支持 1400+ 网站的开源图片批量下载工具 1")

在今天的[**问题求助频道**](https://meta.appinn.net/c/wen-ti-qiu-zhu/7)中，有一个问题：《[求一键打包下载一条微博中的 N 张图的工具](https://meta.appinn.net/t/topic/39305)》，求的是网页版本工具，青小蛙觉得著名的油猴脚本 [Picviewer CE+](https://www.appinn.com/picviewer-ce/) 是能解决问题的，它可以把网页变成相册，然后批量下载。

不过在 [Appinnfeed 频道](https://appinnfeed.t.me/)群组中，@久美子 同学推荐的工具更引起了青小蛙的注意。

## gallery-dl

gallery-dl 可以从 1400+ 个图片托管网站下载图片库和图片集，是一款命令行工具，基于 [Python](https://www.appinn.com/tag/Python/)，可以在 Windows、Linux 以及 macOS 上使用。

### 安装

官网提供了多种安装方式，或者直接从 [GitHub](https://github.com/mikf/gallery-dl) 下载。

```
python3 -m pip install -U gallery-dl
snap install gallery-dl 【Ubuntu】
choco install gallery-dl 【Windows】
scoop install gallery-dl 【Windows】
brew install gallery-dl 【macOS】
```

### 使用

由于是命令行工具，所以需要使用终端、命令提示符来使用。

![gallery-dl - 支持 1400+ 网站的开源图片批量下载工具 1](https://static1.appinn.com/images/202301/gallery-dl.gif!o "gallery-dl - 支持 1400+ 网站的开源图片批量下载工具 2")

最简单的方式，以微博为例：

```
gallery-dl https://weibo.com/1684197391/Ml66KtQMR -o headers.Referer=https://weibo.com/
```

由于微博有防盗链设置，所以添加来参数 `-o headers.Referer=https://weibo.com/`

而 gallery-dl 的参数非常丰富，支持用户名密码：

```
gallery-dl -g -u "<username>" -p "<password>" "https://twitter.com/i/web/status/604341487988576256"
```

按章节编号和语言过滤漫画章节：

```
gallery-dl --chapter-filter "10 <= chapter < 20" -o "lang=fr" "https://mangadex.org/title/59793dd0-a2d8-41a2-9758-8197287a8539"
```

对于有机器人认证（CAPTCHA）的网站，可以使用 cookie 模式，具体可以参考 [GitHub 的示例部分](https://github.com/mikf/gallery-dl#examples)。青小蛙还是觉得 gallery-dl 非常实用的，所有支持的站点列表[在这里查看](https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md)。

---

文章来源: https://www.appinn.com/gallery-dl/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)