---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【3】：色彩空间
url: https://buaq.net/go-144824.html
source: unSafe.sh - 不安全
date: 2023-01-10
fetch_date: 2025-10-04T03:22:52.852009
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【3】：色彩空间

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

【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【3】：色彩空间

蒙娜丽宁 于 2023-01-09 21:
*2023-1-9 21:55:31
Author: [blog.csdn.net(查看原文)](/jump-144824.htm)
阅读量:26
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-01-09 21:55:31 发布
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
7
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本系列文章会深入讲解OpenCV 4（Python版）的核心技术，并提供了大量的实战案例（包括图像加密和解密，数字水印、物体计数、缺陷检测、手势识别、答题卡识别、识别车牌、指纹识别、以及与机器学习相关的项目）。这是本系列文章的第3篇，主要讲解OpenCV处理图像的基本方法，主要包括读取图像、显示图像、保存图像和获取图像的属性。

**目录**

[1. 灰度（GRAY）色彩空间](#1.%20%E7%81%B0%E5%BA%A6%EF%BC%88GRAY%EF%BC%89%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)

[2. 从RGB/BGR色彩空间转换到GRAY色彩空间](#2.%20%E4%BB%8ERGB%2FBGR%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4%E8%BD%AC%E6%8D%A2%E5%88%B0GRAY%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)

文章来源: https://blog.csdn.net/nokiaguy/article/details/128621423
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)