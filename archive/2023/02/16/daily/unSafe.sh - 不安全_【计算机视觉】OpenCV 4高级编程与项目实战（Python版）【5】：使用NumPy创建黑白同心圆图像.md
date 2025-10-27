---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【5】：使用NumPy创建黑白同心圆图像
url: https://buaq.net/go-149536.html
source: unSafe.sh - 不安全
date: 2023-02-16
fetch_date: 2025-10-04T06:44:52.337988
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【5】：使用NumPy创建黑白同心圆图像

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

【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【5】：使用NumPy创建黑白同心圆图像

蒙娜丽宁
*2023-2-15 21:44:23
Author: [blog.csdn.net(查看原文)](/jump-149536.htm)
阅读量:25
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-02-15 22:31:40 修改
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
7
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

于 2023-02-15 21:44:23 首次发布

OpenCV中使用数组表示图像数据，不过这里的数组并不是Python数组，而是NumPy数组。NumPy是非常著名的科学计算库，可用于进行各种科学计算，由于底层使用C语言实现，所以效率非常高。

读者使用type函数输出imread函数的返回值看看这个函数返回的到底是什么数据类型，代码如下：

```
rgb_image = cv2.imread("flower.png")
print(type(rgb_image))
```

运行程序，会输出如下的内容：

```
<class 'numpy.ndarray'>
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
332

04-16
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3029

04-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3万+

03-31
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
6395

05-20
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
4700

01-27
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
601

01-09
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1101

01-02
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
430

11-11
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
5624

09-13
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1458

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
586

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
364

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
483

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
355

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
361

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
433

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
332

08-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
446

07-15
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1251

06-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1421

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

文章来源: https://blog.csdn.net/nokiaguy/article/details/129051147
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)