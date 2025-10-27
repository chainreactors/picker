---
title: WAF专题3--WAF工作模式
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247486634&idx=1&sn=2d841bdc53c5bfdf8b67c611b7b30351&chksm=fdf967bfca8eeea9d69b42c840b8da70db6d96a418fb33e90918547bb79164cb762454baf77a&scene=58&subscene=0#rd
source: debugeeker
date: 2022-11-14
fetch_date: 2025-10-03T22:41:15.754466
---

# WAF专题3--WAF工作模式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbwraiayrEUohVDu90PF2sCIhSQfzsyWyOpIniadGqhOzqfPtdEmZy95icSKalxh7rWWKNAIZITME4ialg/0?wx_fmt=jpeg)

# WAF专题3--WAF工作模式

原创

debugeeker

奶牛安全

> 暗号见文末

由于WAF一般和业务系统是串联的，并且还是部署在业务系统前面。如果采用反向代理部署模式，假设WAF出现故障，那么会导致单个或者多个站点不可用。这意味着WAF的功能必须是随时可以关闭的。一个WAF往往需要同时防护多个站点，如果把整个WAF关闭，是会导致整体业务群都失去保护。**所以，WAF的工作模式必须有对站点有随时关闭的模式。**

当WAF有新功能或者有新策略发布，是不可以立马把新功能或新策略对现有站点进行防护，需要一段时间来进行观察，看功能是否可用或策略的命中率，漏判率和误判率。如果贸然上线的话，很容易背锅走人的。**所以，WAF的工作模式必须有监听模式。**

不用说，WAF工作模式当然要有防护模式。这是WAF存在的意义。

那么，这些工作模式如何设计呢？？

先从关闭模式看起，对某个站点使用关闭模式，到这个站点的流量就感受不到WAF的存在。一般的做法，是解绑域名，再到web服务上绑定该域名。这种做法优缺点如下：

* 优点

+ 由于web服务和WAF完全分享，WAF的故障不会影响到web服务。
+ 少了WAF这个中间节点，web服务的响应速度不受影响。

* 缺点

+ 解绑和重绑，涉及到接入备案过程，流程较长，生效时间较长。
+ 原先隐藏在内网的web服务集群对公网开放，除了web应用本身的攻击面，还增加了主机层面的攻击面，增大了整体网络的攻击面。

关闭模式也有一种快速生效的实现方式。这种实现方式和监听，防护两种模式的实现很统一。

这种方式的优缺点如下：

* 优点

+ 不需要进行域名解绑和重绑，生效时间快
+ 不会增加整体网络的攻击面

* 缺点

+ 流量还是要经过WAF，对web服务响应速度还是影响
+ 流量要经过WAF，所以WAF的故障也会影响到web服务

由于一个IP可以对应多个域名，一个域名也可以对应多个IP，对针对每个域名来配置工作模式，WAF必须要获取到http请求的URL或头部的host字段。WAF解析完http/https，拿到了请求的域名，再根据域名的配置，决定是否送去过规则还是直接传递给web服务。所以，WAF的http/https模块解析要和规则引擎模块分开。

所以，WAF的关闭模式如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbzmHhhxV5Pc8Wsn2Pb1XzU7F2VMrlLModW1zzgkG1hJHtc29I19Rx8MvHFgXdZCwExczMJcvkaia7A/640?wx_fmt=png)

同样，WAF的监听模式是既过规则，也会直接传递给web服务，大致如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbzmHhhxV5Pc8Wsn2Pb1XzU7kyN9wA4JrAkibiaVXt5xCCNbPzHMu1Nibsib1Sph8QBlMPqBMQ6GsEbk4w/640?wx_fmt=png)

最后，WAF的防护模式是直接过规则，不会直接传递给web服务，大致如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbzmHhhxV5Pc8Wsn2Pb1XzU7C3ey7P78tWEK9kibpYOiaXNNHBxEyUHpCXCcs3OGZ27ZbunvS1icZXc9g/640?wx_fmt=png)

可见，这样的设计，会使得这三种工作模式在实现和原理上都非常统一。

**请关注本号，发消息“A5328”，获取封面照片**

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