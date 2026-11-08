---
title: 美国白宫网络沦为全球住宅代理
url: https://mp.weixin.qq.com/s/g0RK2t_dscJlcA3KOJGlXw
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:10:23.784746
---

# 美国白宫网络沦为全球住宅代理

# 美国白宫网络沦为全球住宅代理

原创

泼猴
泼猴

表哥带我

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OxTIFcCrmM53icLINibicj5RCf2hbNe9h1M53LFQ8ibymVMXjbZC96XOA3pxafSd0Mibh37vXS3Qg7h5GSP5Q8vdyACqp9ZlCQ4JTGA/640?wx_fmt=webp&animated=1&from=appmsg)

**住宅代理服务允许客户使用世界各地的日常设备来路由他们的互联网流量得他们的活动看起来好像来自设备的正常家庭互联网连接。但研究人员发现有流量从在AS2650出口，该网络注册在美国白宫总统执行办公室。**

| 地址 |
| --- |
| 165.119.0[.]0/16 |
| 165.119.250[.]0/24 |
| 165.119.252[.]0/24 |
| 165.119.253[.]0/24 |
| 204.68.207[.]0/24 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzZtlwMjHLrdz9baH8bMR7CMpBrrdAiaH6icXgyom97M5qJ0M0eCjKOyfqhpDnXJSQwzQ0tDYzLE2MibvIEHasTFCmXDUtpI0FvpQ/640?wx_fmt=webp&from=appmsg)

在10月5日至11月3日期间，研究人员通过该网络检测到236个连接。流量来自六个IP地址，并在30天中的26天被记录下来。共有28个住宅代理服务能够使用该网络。为了检查他们的发现，研究人员将IP地址与其他安全服务（包括Spur和Synthient）的数据进行了比较。这两种服务也将这些地址确定为住宅代理出口点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OyTQNWyOgj4xjdJDjCzUcJJ0X9XUC0A8VkDm3WrTLyLRKZFZAduJ4Dp4KvzPAGAaicdL5mCbUicv2E7WakuZZEmrzh40fM1KRQbg/640?wx_fmt=webp&from=appmsg)

获取这些数据不需要特殊技能。任何人都可以注册公共住宅代理服务，支付几美元并通过它发送请求。研究人员表示，它没有针对网络或试图将其探测器引导到那里，它只是通过这些服务请求全局轮换访问，就偶然发现了活动。

时机表明，不仅仅是一个访客网络。大约一半的活动发生在东部时间下午5点到午夜之间，几乎没有活动发生在清晨。第3层将其解读为一个人，而不是公众客人Wi-Fi：某人经常在白宫网络上深夜，他们的设备带有代理SDK，这是一个将设备变成出口点的软件套件。

“过去的研究表明，安全性差的代理SDK可以允许内部网络访问和横向移动。这就是过去的僵尸网络的传播方式。在《A Broken System Fueling Botnets》中，Synthient的研究人员记录了Kimwolf僵尸网络如何通过住宅代理网络接触到至少200万台设备，其中大部分是带有公开ADB服务的Android设备。”报告继续说道。“如果此网络上的SDK存在相同的缺陷，任何购买代理访问权限的人都可以使用它来访问内部系统。”

这很重要，因为安全性低的代理SDK以前让攻击者进入内部网络。Synthient的研究《一个破碎的系统为僵尸网络提供燃料》记录了Kimwolf僵尸网络如何通过住宅代理网络接触到至少200万台设备，其中大部分是具有暴露ADB服务的Android设备。如果白宫网络上的SDK存在相同的缺陷，任何购买代理访问权限的人都可以访问内部系统。研究人员没有声称这里的情况就是这样，它把风险描述为有条件的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzvYqPkLn46UhDVWvdibzkMIEibaOY0zEh40hTlfpkSlf4z7Kgf1CeDeUhWsJ2Sfaqbm3gS4V4FmIZtdEWjvK6NeiboGQSfHKrcgY/640?wx_fmt=webp&from=appmsg)

白宫并不是唯一的惊喜。天文台还在地球上一些最偏僻的地方发现了住宅代理。圣赫勒拿岛、阿森松岛和特里斯坦达库尼亚岛是南大西洋领土，包括世界上最偏远的有人居住的岛屿，显示413个地址和32,000多个观测结果，由Starlink和当地提供商Sure Saint Helena划分。

研究人员还检测到南极洲的三个代理活动实例。所有这些都来自链接到McMurdo Station的Cloudflare WARP地址。研究人员开玩笑地指出，企鹅不是嫌疑人。在皮特凯恩岛上，他们发现了一个Starlink地址和一个观测。诺福克岛有一个诺福克电信地址，有四个观测，而斯瓦尔巴岛在朗伊尔比恩有一个Starlink地址，有三个观测。

研究人员还在福克兰群岛发现了388个地址，查戈斯群岛有43个地址，托克劳有21个地址，南乔治亚州有7个地址。这些发现表明，住宅代理网络现在几乎在世界每个角落都在运行。对于安全团队来说，主要担心的是，连接到受保护网络的设备可能会在不知不觉中成为代理出口点，有可能将这些网络暴露在外部流量中。

“居民代理已经感染了世界的每个角落，似乎没有他们无法到达的地方。”

---

对此`你怎么看`在评论区发表你的意见吧

其他推荐阅读

[【吃瓜速修】OpenSSH严重漏洞：长密码绕过认证](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488293&idx=1&sn=bfcd4695caa6b26a1e7cf03e4e50c56c&scene=21#wechat_redirect)

[【吃瓜】腾讯游戏部分官方启动器被投毒](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488267&idx=1&sn=c9c4f8e09b5be73458eee0057a167a65&scene=21#wechat_redirect)

[【吃瓜速查】ARTEX二开项目存在后门](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488259&idx=1&sn=68d008fb05472de84ef2cda4ddcd91c3&scene=21#wechat_redirect)

[【吃瓜】DeepSeek服务再次中断梁补又要来了吗](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488233&idx=1&sn=4d1061cf12e9900f2c3537298cecaf3c&scene=21#wechat_redirect)

[Claude官方扩展被投毒植入持久化SSH后门](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488217&idx=1&sn=389ce49437cd6b5a414c18bc051119ba&scene=21#wechat_redirect)

[【吃瓜】黑客公布美国国土安全局4.1万条信息](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488217&idx=2&sn=8f572d619978ad4d73843f1e2c2915db&scene=21#wechat_redirect)

[【吃瓜】无印良品泄露2726万条信息](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488203&idx=1&sn=cdf85e55414edcec4dcd182168aba91c&scene=21#wechat_redirect)

[【吃瓜】朝鲜黑客盗走交易所60亿美元](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488197&idx=2&sn=7213e22ab5b2ccd819fbb725858fdb64&scene=21#wechat_redirect)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

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