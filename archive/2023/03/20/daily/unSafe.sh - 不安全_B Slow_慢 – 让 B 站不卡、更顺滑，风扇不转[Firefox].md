---
title: B Slow/慢 – 让 B 站不卡、更顺滑，风扇不转[Firefox]
url: https://buaq.net/go-154206.html
source: unSafe.sh - 不安全
date: 2023-03-20
fetch_date: 2025-10-04T10:04:44.289664
---

# B Slow/慢 – 让 B 站不卡、更顺滑，风扇不转[Firefox]

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

![](https://8aqnet.cdn.bcebos.com/b562f292fb8c53729c9e6e8d754e4595.jpg)

B Slow/慢 – 让 B 站不卡、更顺滑，风扇不转[Firefox]

*2023-3-19 20:47:51
Author: [www.appinn.com(查看原文)](/jump-154206.htm)
阅读量:48
收藏*

---

**B Slow/慢** 是一个针对 [B 站](https://www.appinn.com/tag/b%E7%AB%99/)的 Firefox 扩展，通过错峰执行脚本，让用户在通过 Firefox 浏览 B 站的时候不卡。如果你「每次打开一个 B 站视频，电脑风扇开始转，小浏览器受不了」，那么你需要它。@[Appinn](https://www.appinn.com/b-slow-for-firefox/)

![B Slow/慢 - 让 B 站不卡、更顺滑，风扇不转[Firefox]](https://static1.appinn.com/images/202303/b-slow.jpg!o "B Slow/慢 - 让 B 站不卡、更顺滑，风扇不转[Firefox] 1")

来自[**发现频道**](https://meta.appinn.net/c/faxian/10)，@gary 同学的作品：<https://meta.appinn.net/t/topic/41231>

就叫它《B Slow》或《B慢》。这个名字意为「 Be slow 」

## 脚本错峰执行

每次打开一个 B 站视频，电脑风扇开始转，小浏览器受不了

做了一个扩展（仅Firefox。无Chrome。sorry），原理是在 webrequestBlocking 里加`await sleep()`，让非核心视频功能资源经过 10-20 秒的随机延时后再加载，**错峰出行**。而播放功能不受影响。

经过简单的对 B 站的网络活动分析之后撸出来的，不对网站内容和功能做任何修改。

## 需要对视频点赞收藏留言时

是可以临时禁用的，如果你想要发表留言、点赞收藏等，最好点一下工具栏上的按钮（临时在此标签中禁用）然后刷新一下再操作，就不用等1分钟才能加载功能了。

另外，技术上，仍有两点可改进的：

1. 发现在 webrequestBlocking 里，纯await sleep()的时候也要占用少量的 cpu 。
2. B 站的网页全屏功能要等全部资源加载后才能用（全屏幕倒是可以正常用）。搞不清网页全屏是在哪个.js 里

## 对浏览器的支持

仅Firefox。可惜 Chrome 无法使用。Chrome 的 webqurestBlocking 竟然不支持 async 。而且以后 mv3 更没希望了

## 获取

* [Firefox Addons](https://kutt.appinn.com/PhC6V7)

另外开发者 @gary 还说在 B 站有个账号：**[挑柴看剑](https://space.bilibili.com/2123686105)**，欢迎关注（不常更）。

再另外青小蛙在 B 站也有账号：[小众软件](https://space.bilibili.com/10979326)，欢迎关注（不常更）。

原文：https://www.appinn.com/b-slow-for-firefox/

文章来源: https://www.appinn.com/b-slow-for-firefox/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)