---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【4】：通道详解
url: https://buaq.net/go-146870.html
source: unSafe.sh - 不安全
date: 2023-01-28
fetch_date: 2025-10-04T05:03:03.056827
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【4】：通道详解

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

![](https://8aqnet.cdn.bcebos.com/ec0c0ab4adb9ddd9f3507a56e8e4ae96.jpg)

【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【4】：通道详解

蒙娜丽宁
*2023-1-27 21:23:30
Author: [blog.csdn.net(查看原文)](/jump-146870.htm)
阅读量:17
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-01-27 22:15:24 修改
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
27
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

于 2023-01-27 21:23:30 首次发布

视频课程：[《Python OpenCV 4高级编程与实战》](https://edu.csdn.net/course/detail/37684)

相信很多读者朋友对“通道”这个词已经不陌生了，一副BGR图像是由3个通道组成的，这3个通道是B通道、G通道和R通道。本节将介绍如何对通道进行拆分与合并，并达到处理图像的目的。

## 1.拆分BGR图像中的通道

OpenCV提供的split函数可以拆分图像中的通道。split函数的原型如下：

```
    split(image)-> b,g,r
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vipListWhite.png)

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2021Black.png)

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUnHeart2021Black.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectBlack.png)

  0

  收藏
* [![](https://csdnimg.cn/release/blogv2/dist/pc/img/newComment2021Black.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newShareBlack.png)

01-05
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
296

04-16
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3016

04-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3万+

03-31
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
6378

05-20
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
4689

01-09
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1063

01-02
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
386

11-11
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
5571

09-13
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1283

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
561

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
346

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
466

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
335

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
344

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
410

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
314

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
409

07-15
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1156

06-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1376

06-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
881

### “相关推荐”对你有帮助么？

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel1.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey1.png)

  非常没帮助
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel2.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey2.png)

  没帮助
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel3.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey3.png)

  一般
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel4.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey4.png)

  有帮助
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel5.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey5.png)

  非常有帮助

文章来源: https://blog.csdn.net/nokiaguy/article/details/128772938
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)