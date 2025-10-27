---
title: WAF专题4 规则引擎原理
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247486638&idx=1&sn=747ff91a5b4711f842d140a8d46de282&chksm=fdf967bbca8eeead2c216042ec4ae90b9f17677f5d394a2b8ba2463f1e33cd4057bed41d5379&scene=58&subscene=0#rd
source: debugeeker
date: 2022-11-15
fetch_date: 2025-10-03T22:46:01.812966
---

# WAF专题4 规则引擎原理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbwmOB1ZKLjYu8dOBZ5XEwfD0aTm6eO7HHTjlY5NMtjjtlOlMpQRJIFvVcmomGKDcUPLTVrAeMFGEQ/0?wx_fmt=jpeg)

# WAF专题4 规则引擎原理

原创

debugeeker

奶牛安全

WAF无非就是拦截有害请求和伪装响应，出于性能考虑，拦截有害请求又分为两个层面，由网络层拦截和由应用层拦截，且任何请求应该先在网络层过滤再到应用层过滤。也就是说，规则引擎分为两块，对请求过滤和对响应过滤，而对请求过滤分为两大步，网络层过滤和应用层过滤。

原理图大致如下：

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbxfiafpJbP8siaE51DB71I6LzBxHQB5rHqVDxXLzbU0Tt4VvVZnFhDhM89w3GDBNXkNMbLTJQ9SnndA/640?wx_fmt=png)

* 请求部分

+ 网络层

- 白名单：很多时候部署在WAF后面的应用，需要测试接口对非法输入的处理，但又不想关闭对该站点的监控，为了防止WAF对测试活动的影响，对来源IP和目标IP设置白名单，绕过WAF的拦截。从性能角度来考虑，白名单过滤功能是不可能放在其它过滤功能后面，那么它应该是规则引擎在网络层过滤的第一步。
- 黑名单：同样，对于已知有害的来源IP，是越早拦截越好，出于性能考虑，黑名单拦截功能应该在网络层，那么它应该紧跟在白名单后面。

+ 应用层

1. https拆解：随着https越来越普及，WAF需要对https请求和响应进行检测和过滤，所以，WAF必须支持使用证书对https内容进行拆解。
2. http方法防护：不少http方法是有安全风险的，如果webserver的配置有问题，如果不在这一步拦截掉，而url白名单的来源IP又可能被攻击，那么就可以存在站点沦陷的风险。一般是拦截除了HEAD，GET，POST之外的方法
3. url白名单：由于某些接口（如请求某些静态资源）并不会存在漏洞，没必要对这些url进行规则过滤，或者防护站点某些url接口有所更新，需要特定的来源IP进行测试。应当存在url和来源IP对应的白名单
4. url黑名单：同样由于某些接口的实现可能会涉及大量运算，可能需要对该url访问进行次数限制，需要存在一个url和次数的黑名单。
5. http请求解码：http请求很多时候对头部和内容的数据往往会进行编码，如url编码，html编码，js编码，十六制编码，base64编码，主要是为了传输一些二进制数据，或攻击者用于绕过各种防护设备。只有对数据进行解码，才能够知道它真实的payload。所以需要对http请求进行解码。
6. http请求头部过规则：GET，HEAD方法的参数都是紧跟URL，这个阶段就可以进行过滤，而且先对请求头部过滤，也是基于性能考虑。毕竟请求url参数和头部都是key-value方式，解析相对比内容要快。
7. http请求内容过规则：POST方法的参数基本都是放在请求内容里。

* 响应部分

+ 响应头部过规则：响应头部有不少字段会泄露背后服务的关键信息，如server会泄露webserver软件及版本，x-powered-by会泄露cgi语言和版本（PHP，Python,Perl,Ruby之类），Via和Max-Forward会泄露WebServer的拓扑。为了避免攻击者利用这些信息攻击，需要对响应头部某些字段进行屏蔽或伪装。
+ 响应内容过规则：这一部分也叫做软补丁功能。为什么呢？如果webserver的应用服务抛异常了，并把异常信息显示在页面，这是一种常见的信息泄露。如果需要研发团队来修改和测试，运维团队对该服务进行打补丁上线，整个过程可能持续几周，存在很大的风险窗口。如果在WAF上，对这些信息进行伪装或屏蔽，就可以极大降低安全风险。更加不用那些会泄露用户信息，金融信息等服务。

**关注发消息“A9FDC”**

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