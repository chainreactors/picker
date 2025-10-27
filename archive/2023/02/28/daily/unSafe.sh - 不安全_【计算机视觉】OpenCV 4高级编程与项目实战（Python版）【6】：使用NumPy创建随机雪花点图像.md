---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【6】：使用NumPy创建随机雪花点图像
url: https://buaq.net/go-151250.html
source: unSafe.sh - 不安全
date: 2023-02-28
fetch_date: 2025-10-04T08:13:49.623604
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【6】：使用NumPy创建随机雪花点图像

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

【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【6】：使用NumPy创建随机雪花点图像

蒙娜丽宁 已于 2023-02-27 21
*2023-2-27 21:20:45
Author: [blog.csdn.net(查看原文)](/jump-151250.htm)
阅读量:15
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-02-27 21:22:05 修改
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
5
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

于 2023-02-27 21:20:45 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

上一篇文章演示了如何使用二维数组创建黑白图像，如果要创建彩色图像，就需要使用三维数组。例如，在BGR色彩空间创建200 × 200的彩色图像，就需要一个200 ×200 ×3的三维数组存储像素的颜色值，其中第3维可以存储3个通道的颜色值，分别是B通道、G通道和R通道。也就是我们平常说的三原色：蓝（B）、绿（G）和红（R）。

1. ### 创建彩色图像

下面的代码，创建一个三维数组，数组元素初始值都是0，然后将该数组复制3份，将第1个数组的通道1（B通道）设置为255，将第2个数组的通道2（G通道）设置为255，将第3个数组的通道3（R通道）设置为255，这将形成3幅纯色的图像。代码如下：

```
import cv2
import numpy as np

width = 200      # 图像的宽
height = 200      # 图像的高
# 创建指定宽高、3通道、像素值都为0的
```

文章来源: https://blog.csdn.net/nokiaguy/article/details/129250204
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)