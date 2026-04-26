---
title: 新起了一个项目：漏洞扫描（远程安全评估系统）
url: https://mp.weixin.qq.com/s/OTIq98hhIv_qQzQODaunsg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:55:30.968363
---

# 新起了一个项目：漏洞扫描（远程安全评估系统）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Q71mAqQaURPNAr4QKWCff6ZW1WWgKJicics1evPhk3PO79whuaiaWKDGZiagkHibwASxjo1QicCdXMicjPOdNOqia5icAebOhgaa3z7PVEpTl4gOElV0/0?wx_fmt=jpeg)

# 新起了一个项目：漏洞扫描（远程安全评估系统）

原创

游侠安全网
游侠安全网

游侠安全网

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

4月22日，也就是4天前，跟几个朋友聊天，都提到了漏洞扫描软件。

但大家都反馈商业版的价格实在是太贵，有时候想给客户做个简单的服务，也没有什么特别好的选择。

想了一下：那就先搞一个出来吧。

从22日晚上开工，到今天也就是25日，也大概做了一个基本的MVP产品出来，演示是没什么问题了。

给各位精神股东汇报下今天的开发进度：
1、目前包含漏洞、验证、爆破引擎3个引擎，可并行扫描；
2、提升了漏扫稳定性、性能及扫描速度；
3、优化报表，支持多种报告格式，含领导们喜欢的概要页；
4、优化大屏，投屏效果相当OK的。
5、优化多种国产软件的扫描选项。

下面贴几张图，第一张图是做了个大屏，虽然我之前觉得这玩意无所谓，但毕竟还是有很多领导们喜欢，那咱就做上吧，主打一个听劝。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Q71mAqQaUROzUXhia0kd2EUbBQTnxkXEeF321ibib5jgfyW155aqOe3EicGiaLTzBQYkGsmykiakHnXEGEdibH6COibUO82Cf8nzSk8ibB8bSkREJuCA/640?wx_fmt=jpeg)

报告页，由于做的匆忙，现在这个花里胡哨的，最终交付的时候应该会看上去严肃一些。为了给领导汇报的时候方便，所以单独加了一个执行摘要，这个最终交付也还会再继续优化，至少要让领导们一眼就知道安全性大概如何，存在什么样的问题，以及修复的难度和时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Q71mAqQaUROKPibytwJKobvVIx3BcHdtJrDXG6taic8Be4XZ5TTDWQu2kDD07rS0c1bCpEYicrrHAasGwQ7TXPE1wbvCStwPSALJsKibBVGNLIg/640?wx_fmt=jpeg)

每一个漏洞也都有概要以及修复的方式，包括相关的CVE编号、CNVD和CNNVD编号，当然CVSS的评分这也会有。相关的一些文章也会加进来。这个进度没有那么快，但我会加快这个进度。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Q71mAqQaURN1CG4biagwgO4FW5pUwHtnPnxhEibcUn0NAdH0mEtuuZS5ShNlvc77f6T3zUhS5B2YE6oomwSHnc5rvicKuc0rFXvqxOJ66LGS1c/640?wx_fmt=jpeg)

当然对于国产化的支持这一块也是有的。常见的国产化操作系统、数据库、中间件、OA这些都有，并且现在也是在国产化的OpenEuler操作系统上开发的。其他的也会慢慢的支持，包括统信、麒麟等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Q71mAqQaUROicMvP8vjRJlxmeChFBdF68ibq78w81Gl7puFIQH7P3dW1gQ2mKzp8geQ8dbqXlmIOLsXj2coFCuxMtticn8xbCSvBnp3lhqAmrs/640?wx_fmt=jpeg)

现在并行开发了好几个东西，主要是日志审计（一个商业版、一个免费版，一款Windows日志采集和转发客户端，还有一款在线日志应急分析平台）、漏洞扫描，规划中的还有一两个产品，都是贴近实战的。

如果开发进度正常的话（毕竟还有其他的软件要更新），会在五一后把测试版放出来吧。

我的微信 cnbrian 欢迎大家和我交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Q71mAqQaURNPwJPolh8w8mNppjsZlSMFMNXQK5viaHeQ3ic475IicLMAsIZ8FibCibtjeLgr7ZsPN9uvsrUBaMN0dJg2Q1bT5PJhQqdghTHqnnicQ/640?wx_fmt=jpeg)

关于我：

张百川（@网路游侠）陕西省信息安全标准化技术委员会委员、数字丝路安全智库专家、榆林市信息网络安全专家库专家、延安市网络安全和信息化专家库专家；近30次任省市级网络安全攻防演习裁判组长/专家组长；机械工业出版社计算机领域专家咨询委员会委员；在《黑客防线》《中国信息安全》等专业网络安全媒体发表文章20余篇；持有MCP/MCSE/MCDBA/Linux/CISP等多项专业认证。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bgkwFOXObJpyJMF6qbW4AlsQrwQUrZ6nIvql5pwiciaiatSSWcKc7qKIRDsy7baaScKe4VpVibesiaJ66FbOzCmdx4g/0?wx_fmt=png)

游侠安全网

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bgkwFOXObJpyJMF6qbW4AlsQrwQUrZ6nIvql5pwiciaiatSSWcKc7qKIRDsy7baaScKe4VpVibesiaJ66FbOzCmdx4g/0?wx_fmt=png)

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