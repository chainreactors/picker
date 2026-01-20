---
title: 接口泄露到任意账号登录
url: https://mp.weixin.qq.com/s/C0Y7EZTvH_tnES5JmPPTew
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:31:02.620759
---

# 接口泄露到任意账号登录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq0QcrEGMbEBL0JfGP9WDDeC3Pxtd1FT5lA3t48NdeORwNd6hGThJSTUg/0?wx_fmt=jpeg)

# 接口泄露到任意账号登录

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器中沉浸阅读

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

这是之前的一个授权渗透测试，测试目标是一个小程序，话不多说直接上正文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq05Dg4pcfPKu45fdmZPKajLyOHKQIELfpEibroK1f6vmndV0PVpcnupvg/640?wx_fmt=png&from=appmsg)

拿到小程序，直接点击登录，手机号授权登录，丝滑的一批。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq0OicvGCC0gCIQ3JHib99XqZjYFnbALe9BdySOJEYqcHGwGWDGo8LIByJw/640?wx_fmt=png&from=appmsg)

进入系统后，发现功能点似乎有点少，有和没有基本没啥区别，那就先脱离小程序，掏出小程序的域名跑一波dirsearch看看有没有啥敏感目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq0G8P2a0ZHOSQcXmuWMohfFvT11vSsbrfibdTM75f6CGpARhV5EytNNwQ/640?wx_fmt=png&from=appmsg)

很显然，啥也没有，出于好奇，想着带上我的登录凭证再跑呢，结果还真有点东西，有个swagger，emmm，这是一个好的开端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq059OQDkwXCAASsToibcxS5kwc6BQVbZ7UATooZF4XZB35IBICabic8xVA/640?wx_fmt=png&from=appmsg)

古语有言，一个好的开始那必然就会有一个丝滑的好结果，果不其然，还真是，有这么一个user list接口权限似乎校验的不严格，导致可查小程序所有用户的user信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq0Nrcd2ibIsiccIibm2DoYZlyhzKZeQfWraOur4J5SQCO4aDLTvorxazeIw/640?wx_fmt=png&from=appmsg)

当然，这不是关键点，关键是前面授权登录的地方，通过简化后（删除无关参数），基本确定就是通过openid来进行登录的，而上面user接口获取到的username即openid值。啥也不说，直接操作，成功丝滑登录其他用户账号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gTBzDIf6O6xPGSsrTSNoHq04Nfmzsy2Lpn6TY5roVTrvnRf1vqXmMhW3R2rorR474Q7w9BVEWqJLg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

安全无界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

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