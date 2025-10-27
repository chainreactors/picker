---
title: 网页防篡改专题4---发布中心方式
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247487122&idx=1&sn=51cce009f5998d0d5910b6b352029fb6&chksm=fdf96587ca8eec915f238a98651911fd1d80163fa52fe0d64605a3bdf33b7ba8750fa14adea0&scene=58&subscene=0#rd
source: debugeeker
date: 2022-12-04
fetch_date: 2025-10-04T00:29:14.344419
---

# 网页防篡改专题4---发布中心方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbzMC1fDRXrpTic571IJf2455MPxibibOnQicNiaGAKMnqU2EByLlOdnhksiaDsxPI9NibKqNQG8bvfACFwBQ/0?wx_fmt=jpeg)

# 网页防篡改专题4---发布中心方式

原创

debugeeker

奶牛安全

在上面几节，都提到页面发布。如果网页防篡改功能和发布中心结合起来，会如何呢？

一提到发布中心，可能就会想起代码版本管理，持续集成，感觉很庞杂浩大。实际上，如果把发布中心当作是一个输入源来看，它的产物就是一堆文件，输出到一个目录作为基线，然后把这个基线同步到各个WebServer上。看到这一点，是不是想起了rsync?

那么，方案可以简化成下面：

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbyaR3ZGHiaQsaIKwic7OlAj5k2KnoPkyWU5orDic3icU4IcHGOh7mzL3gn2uuAIHibVNztIv6ianu2AHz8w/640?wx_fmt=png)

在这里，再回顾一下这两个问题：

1. 发现站点网页被恶意篡改或恶意上传，并对它恢复或删除，同时上报异常文件的日志。
2. 分辨出正常的网页更新，不会用旧版本的页面覆盖新版本的页面。

第一个问题，可以用上一章提到的inotify技术实时监控web目录变动，同时也用来监控发布中心的目录变动，以每次发布时的文件变动作为基线，再同步到WebServer。

第二个问题，每次更新都是单向的，不会存在旧版本覆盖新版本的情况。

这个方案的工作原理大致如下：

使用inotify技术，从Linux2.6.13内核开始支持的特性，可以实时监控目录变动（添加文件，删除文件，更改文件）。

使用rsync，因为它是增量同步，可以减少带宽，提高文件比对速度

具体原理如下：

* 发布中心：
* 不开放web服务，只有rsync服务
* 有一个监控脚本，实时监控发布目录的变动，一有变动，就认为有发布，把发布的文件列表放入到一个发布列表文件（保证不和页面放在一起），或存放到数据库
* Web服务器：存在监控脚本。主要做两件事情：
* 定时从发布中心同步发布列表文件，或从数据库读取发布列表。如果有发布，同步页面文件
* 监控web目录变动，如果有变动，和发布列表比较，如不在列表中，则删除和重新同步该文件，并把异常结果发送日志中心

这个方案有这样的优势：

1. 由于独立于WebServer，不会影响web服务稳定。
2. 不使用inotify监控方式，web变动又不频繁，对主机性能影响不大，不会影响web服务的响应速度。
3. 更安全。本方案有一个基线版本，且发布中心不和web服务关联，又通过inotify实时检测，可以实时检测和清除恶意篡改，同时它把异常篡改日志上传，可以作为WAF日志补充，毕竟WAF不可能100%拦截恶意请求。且发布中心可以部署在更安全的区域里。
4. 简单。在WAF上实现，每次更新页面，必须要把相应url去监控（引入安全风险），还增加维护步骤。Web服务模块方式，需要把web服务下线，上线预测试，再正式上线。镜像备份由于无法感知正常更新，每次发布，需要更新镜像。本方案无论是由发布平台发布，还是手动更新到基线目录，各个web服务会自动更新，自动识别正常和恶意改动，不用重启服务
5. 成本更低。市场上的三种方案，无论如何，在开发成本和运维成本都较高。本方案，利用Linux系统现有工具，可以用脚本实现，开发成本很低，实施也简单。

**暗号：5ae7d**

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