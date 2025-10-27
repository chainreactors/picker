---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【9】：计算图像均值和标准差
url: https://buaq.net/go-153605.html
source: unSafe.sh - 不安全
date: 2023-03-16
fetch_date: 2025-10-04T09:42:51.484166
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【9】：计算图像均值和标准差

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

【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【9】：计算图像均值和标准差

蒙娜丽宁 于 2023-03-15 21:
*2023-3-15 21:10:2
Author: [blog.csdn.net(查看原文)](/jump-153605.htm)
阅读量:11
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-03-15 21:10:02 发布
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
11
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

图像的均值表示图像整体的亮暗程度，图像的均值越大，图像整体越亮。标准差表示图像中明暗变化的程度，标准差越大，表示图像中明暗变化越明显。

OpenCV提供了mean函数用于计算图像的均值，提供了meanStdDev函数用于同时计算图像的均值和标准差。

mean函数的原型如下：

```
mean(src[, mask]) ->   retval
```

参数说明：

* src：待求均值的图

文章来源: https://blog.csdn.net/nokiaguy/article/details/129568725
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)