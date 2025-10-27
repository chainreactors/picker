---
title: 网页防篡改3---WebServer方式
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247486795&idx=1&sn=a9981b308636db3ab74c2bba7159d5b7&chksm=fdf9665eca8eef4817c61f3ff8816aad536b9a049221ec5e1f9683a070d8fdd7c65245249374&scene=58&subscene=0#rd
source: debugeeker
date: 2022-11-22
fetch_date: 2025-10-03T23:24:02.941228
---

# 网页防篡改3---WebServer方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbwu466PadE40LJ2voD9qmxWtibgRSTXtzB33KicCbnOgX4X0eZ8wssRiamJWPGGpib1ZelkI8doctxU9w/0?wx_fmt=jpeg)

# 网页防篡改3---WebServer方式

原创

debugeeker

奶牛安全

由于waf方式并没有解决网页篡改，只是缓解而已，特别是网页防篡改功能可能导致整个站点断服的风险，让waf方式差强人意。

不把鸡蛋放在一个篮子里，考虑一下把网页防篡改功能在WebServer上实现。这样，即使一个WebServer出现问题，不会影响整个站点。

那么，它应该是怎样的实现方式？

先回顾一下这两个问题：

1. 发现站点网页被恶意篡改或恶意上传，并对它恢复或删除，同时上报异常文件的日志。
2. 分辨出正常的网页更新，不会用旧版本的页面覆盖新版本的页面。

根据上一节的讨论，第2个问题，可以通过操作同步的方式，把新发布的文件来更新cache里的内容，可以使用WebServer的重载或重启方式。

那么，WebServer应该怎么检测网页文件被恶意篡改？

一般有三种方式：

1. 定时扫描web目录，把里面的内容和cache对比，有问题就恢复或删除。这种方式，时间间隔太短对资源消耗很大，会影响WebServer的性能，时间间隔太长，又会延误恶意文件发现的时机。
2. 通过inotify监听web目录的变动，一旦有变动，立马可以检测对比，有问题可以立刻恢复或删除。这种方式的实时性很好，对于并发量大的WebServer，可能会出现线程抢占的问题，导致WebServer死锁停服。即使没有这样的问题，也要对WebServer进行修改。
3. 请求触发，对每个请求处理都进行请求文件进行鉴别。目前主流的WebServer主要是apache httpd和nginx，两者都支持在http请求处理周期里添加模块定制特定功能。根据https://httpd.apache.org/docs/2.4/developer/request.html和http://www.nginxguts.com/2011/01/phases/，都可以在content这个phase上插入模块，来返回cache内容，并且随后检测cache的文件和实际文件的区别。这种方式的好处是，可以不改变WebServer处理逻辑，也不需要改动WebServer代码。

PS: 目前市场上有不少网页防篡改产品使用请求触发的方式，还使用了数字水印的技术。个人觉得这种技术过于噱头了。从WebServer的日志一般可以看到，几K大小的页面，大概2-3ms的处理时间。对页面进行md5sum或sha1sum，可以发现这个时间是处理时间十几倍到几十倍。如果WebServer一秒钟可以处理上百万请求，那么用了数字水印技术，估计只有几万，性能劣化会非常厉害。其实，在WebServer检测和清除时，只是读取页面文件的stat信息，已经非常消耗IO了。

虽然WebServer方式是可以解决网页防篡改的问题，但它还是有这样的问题：

1. 每次发布新版本时，还是需要重载或重启WebServer。对于那些访问量大的站点，动辄几百上千台WebServer，重载或重启的工作量会非常大，只会让运维人员冲冠一怒rm –fr /
2. 无论如何，都和WebServer耦合在一起，还是会影响WebServer的稳定性
3. 无论哪种方式，都会延长WebServer处理请求的时间，劣化WebServer的性能。

**暗号：5fcab**

**觉得好，请关注本公众号和分享到朋友圈。麻烦点击一下右下角的“在看”。谢谢！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

奶牛安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过