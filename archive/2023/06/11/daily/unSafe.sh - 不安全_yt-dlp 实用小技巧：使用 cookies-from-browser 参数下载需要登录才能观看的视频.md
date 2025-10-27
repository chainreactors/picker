---
title: yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频
url: https://buaq.net/go-168149.html
source: unSafe.sh - 不安全
date: 2023-06-11
fetch_date: 2025-10-04T11:44:47.885859
---

# yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频

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

![](https://8aqnet.cdn.bcebos.com/0d0eb4707ee17279fee8c8b21c87ca48.jpg)

yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频

Home电脑技巧yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频
*2023-6-10 14:43:13
Author: [www.appinn.com(查看原文)](/jump-168149.htm)
阅读量:55
收藏*

---

[Home](https://www.appinn.com)

[电脑技巧](https://www.appinn.com/category/pcskill/)

yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频

**yt-dlp** 是一款非常著名的开源、在线视频下载工具，命令行方式，目前开发状态很活跃。它源自更加著名的 youtube-dl。今天介绍 2 个小技巧，可以更方便的自动获取浏览器 cookies，让那些需要登录才能观看的视频，在命令行下也非常容易下载。另外就是下载指定格式。@Appinn

![yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频](https://static1.appinn.com/images/202306/yt-dlp.jpg!o "yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 1")

感谢 @WM 的推荐。

## yt-dlp

yt-dlp 项目在 [GitHub](https://github.com/yt-dlp/yt-dlp)，掠过安装，命令行工具比较烦的地方在于完全不知道自己输入的是什么，跟着来就好。两个技巧：

### 1. 下载指定格式

只需要加上 `-F` 参数：

```
yt-dlp -F https://www.youtube.com/watch?v=7SH4irC_xMs
```

然后你会看到所有检测到的格式：

![yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 1](https://static1.appinn.com/images/202306/appinn-2023-06-10-10-28-122x.jpg!o "yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 2")

找到你需要的格式序号，就是最前面那个数字，注意你的终端里不一定是绿色的，可能就是白色字体。

然后使用 `-f 序号` 下载：

```
yt-dlp -f 599 https://www.youtube.com/watch?v=7SH4irC_xMs
```

就能下载到指定格式了，这里是 m4a，仅音频。

![yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 2](https://static1.appinn.com/images/202306/appinn-2023-06-10-10-33-462x.jpg!o "yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 3")

### 2. 下载需要登录的视频

这个时候，往常会需要先导出 cookie，然后再下载，略麻烦不说，将 cookie 会让命令行更长，更头痛。

yt-dlp 有一个简单的参数：`--cookies-from-browser`，它的意思是从浏览器获取 cookies，就不需要导出了，让 yt-dlp 自己去获取，支持很多浏览器：brave, chrome, chromium, edge, firefox, opera, safari, vivaldi。

你只需要先在浏览器里登录，然后使用命令行下载即可。

以下为使用里 Firefox 的例子：

```
yt-dlp --cookies-from-browser firefox:/Users/appinn/Library/Application\ Support/Firefox/Profiles/12345.default-release-12345/ https://www.bilibili.com/video/BV1Rp4y187y5/
```

你需要找到浏览器的 Profile 文件夹位置，对于不同的系统和浏览器，都是不同的，举几个例子：

#### Windows & Edge：

```
yt-dlp.exe --cookies-from-browser edge:"C:\Users\appinn\AppData\Local\Microsoft\Edge\User Data\Profile 1" -F https://www.bilibili.com/video/xxxx
```

注意 Windows 下需要用引号把路径包起来。

#### Windows & Chrome

```
yt-dlp.exe --cookies-from-browser chrome:"C:\Users\scavi\AppData\Local\Google\Chrome\User Data\Default" -F https://www.bilibili.com/video/xxxx
```

#### macOS & Firefox

```
yt-dlp --cookies-from-browser firefox:/Users/appinn/Library/Application\ Support/Firefox/Profiles/xxxxx.default-release-123455/ https://www.bilibili.com/video/xxxx/
```

#### macOS & Edge

```
yt-dlp --cookies-from-browser edge:/Users/appinn/Library/Application\ Support/Microsoft\ Edge/Default/ -F https://www.bilibili.com/video/BV1Rp4y187y5/
```

注意 macOS 下，如果路径中有空格，需要转义，即使用 `\` 来代替空格。

当你在命令行中看到下面的提示：

```
[Cookies] Extracting cookies from edge
[Cookies] Extracted 102 cookies from edge
```

就代表正确了，否则还需要确认路径。不过这已经比导出 cookie 这件事简单多了。

![yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 3](https://static1.appinn.com/images/202306/appinn-2023-06-10-14-33-362x.jpg!o "yt-dlp 实用小技巧：使用 cookies-from-browser 参数下载需要登录才能观看的视频 4")

大概就是这样了。

---

文章来源: https://www.appinn.com/yt-dlp-cookies-from-browser/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)