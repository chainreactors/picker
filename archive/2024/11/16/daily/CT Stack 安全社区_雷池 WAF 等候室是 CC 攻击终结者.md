---
title: 雷池 WAF 等候室是 CC 攻击终结者
url: https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247499317&idx=1&sn=3ff32f9e22450999f088a657c01bfc97&chksm=e92cea96de5b6380b71f3113811097050a69e3f54e09bfcfe549ad5a1af5b95c015831ba3c86&scene=58&subscene=0#rd
source: CT Stack 安全社区
date: 2024-11-16
fetch_date: 2025-10-06T19:18:00.411913
---

# 雷池 WAF 等候室是 CC 攻击终结者

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpMHHzW3ObLiafa1ibYQnbQibwXkIWAk4sGFvhWEHDCiciad84oReaibWcIRYA/0?wx_fmt=jpeg)

# 雷池 WAF 等候室是 CC 攻击终结者

原创

CT Stack

CT Stack 安全社区

作为用了雷池一年多的老用户，非常荣幸能应官方邀请来体验一下雷池本周的新版本。

首先，这不是一个恰饭文章，虽然运营杰哥送了我半个月的付费授权，但是本次测评是我主动提出的，我还是会本着公正客观的态度对雷池做出评价。

昨天雷池 WAF 社区版发布了 7.2.3 版本

雷池官网：https://waf-ce.chaitin.cn/

从更新记录来看，“CC 防护“ 和 “Bot 防护” 两个功能有重大更新，其中比较有意思的是 “等候室” 这个功能，官方功能介绍如下

开启等候室后，当网站同时访问人数过多时可以起到有效的削峰作用。

看起来是一个限流 & 防 CC 攻击的功能，官方还给了一个张效果展示图。

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpASKJw8pZwyn6gxvfAvxWMJ76QzaicWGVIanzbR3VO3l1ibUe3lbJicgMA/640?from=appmsg)

# CC 攻击及传统防护方式

![](https://mmbiz.qpic.cn/mmbiz_svg/4h0Uv4XOMvOySPIIiaMhRtCbpIibicuSJHABmz3Ho7EQt2uSCCaQ5yemAJ52nqHpyicaUicnA3eWppuo1YoakC7TDN8U0DoIkDjU8/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/4h0Uv4XOMvOySPIIiaMhRtCbpIibicuSJHApNebcJm4RLksgo9TeKtAicqxlCwgVk8olFwQOicWGuf4y5ZBHemQ0ejjcZ7GfGSpLD/640?from=appmsg)

首先，CC 攻击（Challenge Collapsar）是一种常见的 DDoS 攻击方式。传统 DDoS 攻击往往是以消耗服务器带宽为目的，攻击者发送大量网络包来堵塞服务器的网络出口，使正常用户无法访问服务器。

CC 攻击区别于传统的 DDoS 攻击，它主要活跃在 HTTP 层，攻击者会模拟多个合法用户持续请求网站，从而使服务器的 CPU、内存等资源被大量消耗使正常用户无法访问服务器。

相信各位站长朋友对 CC 攻击并不陌生，这种攻击在互联网上非常流行，而且难以防御。

以往最常见的抵御 CC 攻击的方式是对源 IP 访问网站的频率做限制，如果某个 IP 在短时间内发起大量 HTTP 请求，就阻断该 IP 后续的所有访问。这种方式对于 CC 攻击的防护来说肯定是有效的，但也有不少弊端，比如：

* 某个 IP 可能是个大型出口，整个公司或者整个学校都用同一个 IP 的情况很常见，这种情况下这个 IP 的访问频率高于其他 IP 其实也是正常现象

  攻击者可能会使用一大批 IP 代理来降低每个独立 IP 的访问频率

  某些事件可能会引起突发的业务高峰，在业务高峰来临时并没有人发起攻击，只是正常用户的流量就非常大爆

由此可见，对抗 CC 攻击只做简单的频率限制是不够的，有技巧的攻击者会想办法规避检测，而且还容易误伤正常用户。

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpSEV1F0mBbP2EbNxvG1GMPn1lgY8QTHbveK8nibRRBVAnn3RqKgI2lvA/640?from=appmsg)

实际上，每个应用能够承载的业务量是有相对明确的上限的，比如：

* 大学生选课系统，同时 1000 人选课是没问题的，但同时 2000 人来抢课就会把服务器挤爆

  **买**票系统，同时 1000 人抢票是没问题的，但同时 2000 人来抢票就会把服务器挤爆

  论坛，同时 200 人发言讨论是没问题的，但遇到热点新闻时 1000 人同时发言就会把服务器挤爆

这时候最好的方案实际是对用户做限流，就好比逛街吃饭，遇到餐馆人太多需要排队等位一样。

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpkTUH3aJ9DyI9jN84wicU7y5nGQxlevsjETlDO52Op6aWGKb2tOo2ozg/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/4h0Uv4XOMvOySPIIiaMhRtCbpIibicuSJHA3icy6R8qSCNomV8xM5jyDWu7DItcls0xVKcoubeJlSY6pCNtialHGamcWMTk0RicjA0/640?from=appmsg)

### 雷池 WAF 等候室

雷池等候室是参考 “餐馆等位” 的模式，专为网站设计的一套限流方案，用于解决流量高峰可能会冲垮网站服务器的问题。

雷池 WAF 默认是不启用等候室功能的，如果需要开启等候室，只需要在界面上点击 ”CC 防护“ 按钮，然后配置等候室的相关参数即可。

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpegqxAoEY5yOMZYL9vc9Eia51bH1YNJ4IluATTlTINibKvWiaGluQcxh6g/640?from=appmsg)

如上图所示，雷池 WAF 的等候室功能有两个可供配置的参数：

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpkCJsGibEL0Rl0YjHYIbDgIspn5l1Bic91HgwrXQGqTp5VguZatTHe3uA/640?from=appmsg "头像")

允许同时访问的用户数：看名字就很好理解，表示网站同时最大能容纳的用户数量，超过这个数量就要开始等位

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpkCJsGibEL0Rl0YjHYIbDgIspn5l1Bic91HgwrXQGqTp5VguZatTHe3uA/640?from=appmsg "头像")

活跃超时时间：成功进入雷池的用户如果一段时间在网页上没有操作，就会被踢出房间重新排队

根据业务的情况填上配置即可，雷池演示站点的配置是 ”1“，直接来测试看看：

1. 用浏览器打开网站，成功进入了网站，刷新了多次，没有发生任何变化，代表我是网站目前唯一一个用户，还没有超过限制，这很棒；

2. 换了个浏览器再打开网站，就会发现雷池提示我需要排队；

3. 再用手机浏览器也打开网站，这时候雷池提示我有两人在排队；

4. 关掉前面两个浏览器，等了几秒钟以后手机终于排到号了，成功进入了网站。

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpdYvde839D2akjoLCCO0wzzwzGwCkZv6sqoVCAr6iasibd3INDDqHVRgw/640?from=appmsg)

流程十分丝滑，限流效果也非常好。粗略看了一眼前端代码，雷池是使用 WebSocket 实现的等位逻辑，服务器排队人数有变化的时候会自动通知浏览器，性能和安全性应该也都没问题。

最后，对 WAF 技术感兴趣的同学，欢迎扫描下方二维码加入雷池社区版技术交流群与我们一起交流～

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpTjQREdKcGpx4icc9gb8YNTpyVZic1YQiaRK7lCr42PCf0qDU83lAOHreFibAsoXrEKlS0FKZEIP6TXbQ/640?from=appmsg)

预览时标签不可点

个人观点，仅供参考

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

CT Stack 安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

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