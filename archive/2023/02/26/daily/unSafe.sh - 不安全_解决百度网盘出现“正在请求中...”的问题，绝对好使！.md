---
title: 解决百度网盘出现“正在请求中...”的问题，绝对好使！
url: https://buaq.net/go-150952.html
source: unSafe.sh - 不安全
date: 2023-02-26
fetch_date: 2025-10-04T08:08:19.457875
---

# 解决百度网盘出现“正在请求中...”的问题，绝对好使！

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

解决百度网盘出现“正在请求中...”的问题，绝对好使！

蒙娜丽宁 于 2023-02-25 10:
*2023-2-25 10:24:43
Author: [blog.csdn.net(查看原文)](/jump-150952.htm)
阅读量:177
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-02-25 10:24:43 发布
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
4
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

最近百度网盘客户端总出现“正在请求中..."，尽管充的SVIP，还是这样，经过摸索，重要找到原因了，对于macOS版本百度网盘客户端，请按下面方式操作，windows版也类似。

找到/Users/用户名/Library/Application Support/com.baidu.BaiduNetdisk-mac/ 目录，请将”用户名“换成自己机器的登录用户名，然后清除该目录中的所有文件和目录。并重启百度网盘客户端，第一次重启需要重新登录。重新登录后，以前下载的文件列表可能会消失，重新下载文件即可解决这个问题。通常会出现"正在请求中...”几秒钟，就可以正常下载了。1000M宽带下载速度大概在25MB/s左右。

文章来源: https://blog.csdn.net/nokiaguy/article/details/129212591
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)