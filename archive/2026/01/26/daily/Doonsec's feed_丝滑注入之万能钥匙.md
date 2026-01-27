---
title: 丝滑注入之万能钥匙
url: https://mp.weixin.qq.com/s/NJzUjsBQXSTRxB1qNldbag
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:34:25.099540
---

# 丝滑注入之万能钥匙

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtl9uuybPZ25RQxYfaTNmhAmMDzxtGy3EBlWARj5wj2leso3aJu0FjJLw/0?wx_fmt=jpeg)

# 丝滑注入之万能钥匙

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器中沉浸阅读

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

这是之前做过的一次授权渗透测试，目标系统还是熟悉的登录系统，当然客户也是熟悉的客户，依旧不提供账号，主打的就是想看看是否存在外部切入的风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtlAYvBPla7Q9kNcZYevtayKsQEmDm51YIZ66ZMT1QtBN2qImCcx6x5DQ/640?wx_fmt=png&from=appmsg)

话不多说，直接开干。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtlqOgBWxCufZClaCFIKtAel5BlibofSYw6SL2uibz5ZsMhTTYZYKelYM2Q/640?wx_fmt=png&from=appmsg)

还是一如既往的先拿祖传字典撞库一手，很可惜，没有撞到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtlm6lmwscgbL0aqxcr1G4sU0ybbPOUOYZEuiaelOd6hC3WW7KygOIgurw/640?wx_fmt=png&from=appmsg)

看了看JS，发现并没有啥API可以使用，emmmm，目录也小小的跑了一下，很可惜，也没有啥。虽然有部分路径遍历，但是都是些前端资源，本来就是公开的，并没有啥风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtlpNMaLsIM7ehKBibuyWFoGIugxXwS9icywf6ZcDibZxlLmXMibsd2Ng8Nng/640?wx_fmt=png&from=appmsg)

没有办法，只能回到登录的位置，象征性的试了试注入，emmmm，结果还真有。你这就让我很难堪呀，都好久没有看到这么丝滑的注入了。甚至于我都好久没有测试过SQL注入漏洞了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtluE9h1G89gcP2Y6BKCGLRpiaX8RM9RRMFfzdFpGQibylnRrB2m7WdvvcA/640?wx_fmt=png&from=appmsg)

好家伙，直接Sqlmap一把梭哈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtlAFniaujJnujib2HjPPdO2RxFEcCeWdQtTxTicghckpbaFIbrFRgNzHPpw/640?wx_fmt=png&from=appmsg)

不过hash密码没有碰撞出来，cmd5看了一下，还真是。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtl4jVEnUiatsicjXqIS3uw84XjNCVKAanibClvGCSCs8gicibJ4ANr3X6e1Lg/640?wx_fmt=png&from=appmsg)

好家伙，难怪祖传字典爆不出来，原因密码都设置的这么严实，不过呢，这可是登录的点存在SQL注入耶，我要什么密码，只要userid就行，跑就是想看看哪个ID才是管理员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtliaOtVickS6CII4CvNtoict9fiba5aMlYJ20jPeO72AEUDPicxMDPbibXrDibQ/640?wx_fmt=png&from=appmsg)

丝滑以管理员的身份进入系统，收工。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gT5iabdw2QW9SG3otUetcXtlOwFCqglZYHT1d5UIK3a4oUmBhhlCqiau2HkK2o3ye8rN3e7tUwzxYGQ/640?wx_fmt=png&from=appmsg)

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