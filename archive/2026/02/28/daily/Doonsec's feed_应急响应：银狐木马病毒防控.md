---
title: 应急响应：银狐木马病毒防控
url: https://mp.weixin.qq.com/s/PoEjFFX9u3d1ZY43DCyY-g
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:17:51.458857
---

# 应急响应：银狐木马病毒防控

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibPC5NLUVWb9A4ktwPiaVO3dGqPZsATAq8cmAaHic75kTxT1OfxBY7GXYDznlmtbespRZIrCdIBFABOl3F8U2ftPm5QuMpic6dKw3iakUlXLib4/0?wx_fmt=jpeg)

# 应急响应：银狐木马病毒防控

原创

小话安全
小话安全

小话安全

![]()

在小说阅读器中沉浸阅读

根据前期收集的威胁情报

https://s.threatbook.com/cybercrime/silverfox

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVXOjNlzN6sgXjfmRaIZjEEbKz9cZWyIaqU4QrpU9Bia2YZ37icibjQlZb9N7rPA7MsibB9KwhIxaRePf8Ysgxjw0hlQmQqnJYX1rxY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVVdTsosWQx4oQf6cWWBJztu5nYjcnkIEhKwibY2z0hvtZENG0bD7e9nCHX4u42j2XcyFzYtajhj907F8e69ciamsuP6LrxYWkLM8/640?wx_fmt=png&from=appmsg)

发现有终端访问了82.23.246.148

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVVMB2ozqjkaicIr63ObBfYGyls40hvzNvoTiaVDXUZDdUJtnlxiaBic6trIdm299Py4oRL7HicGjZbqNBF8wWiczd4jCKUqibbPKpSghs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVURibj2CY4nFlmiabhAxc0oxpFqI6DRt1K7Pz99GvnuOLdhCCiaagbvhy5USqszIf35Y8rqRSmkYDYibVSSlQ8QnopCibJ81hsiawiad0/640?wx_fmt=png&from=appmsg)

询问工作人员，下载了snipaste。

查看终端情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVWoO32PF2lg6xl8F3YkmAic9EBZibj94ia9CxwjGTPwYPTvqtQ8UyeuXKq0WmUaQvevw2vCuIaw3QmhB8VyNy4dcnI56eygRMZDKU/640?wx_fmt=png&from=appmsg)

病毒对系统正常程序进行了注入

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVXiabs8RjiaribQZDGXiaQT1nnfeXnp503fnUicAyRoRTyJBG1uTWP2VB9pjibtaxMG9D7atyqxKkU78c4s0E8xUXBAcb6Pe51yK7IbM/640?wx_fmt=png&from=appmsg)

竟然还访问IPV6的地址

将样本上传微步，执行了powershell，为无文件病毒。未获取到有效信息

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVU3ibNlW85nao8IGLtiaYIKVK92pib9WdRibPBATwZmZKibIsmx3QzxicicZiaPEqRa0sJ38J2yPeemKcTVAtYSh0cjRp2RasjtxUOxCbw/640?wx_fmt=png&from=appmsg)

结束进程病毒又注入到了其他程序上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVW4Ec1ZMVR2KLEX7mbuwRQF3vCGChOFYqIgNQMLdDPMiawI9ReTlwFzZqPBL7BD7JibpuKIY1hOhdvDAzdHC8FomyQZglYeKjP34/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVV2RlVeBTSbiaeJYprOBicwKaNv90yFuVSjPxrMgh1yPpuYT8IargJ6HP7iaiamLFZHQtWoa1DbWz38tibia1JWSXBg41qYa5sBTAtCA/640?wx_fmt=png&from=appmsg)

未能发现恶意程序

搜索外联时间或恶意程序安装期间，电脑文件的情况。

这里用everything搜索，发现可疑的文件夹

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVXiaOgzZ6InTb5u3SmZp0A281UY35mFldiaU1eOZlKYgh55xyklRYXYW2icGickP5hIWyL2eFcY13YZSu6OhyYODDV6CibZ4ICKbMgY/640?wx_fmt=png&from=appmsg)

打开文件夹，提示不存在

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVUV4icxmErs4chMa5kCZfrepqBPdRiaNWsHGka9iaTL0Mh30HQhXdRT3TPPibtGEgdVqlfrCDJf8J9b5DjUKTdeU9YRn0UBvMRcFaY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVVbVSia1wV4HNkZF99vMjibdbjrx56TGcBjxyhf9FbpibRcWULH5NFP9m5JCITlaVpYic4mF97fQiaLPmcm2eibQKLjJ1njI0IicvaOHs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVXiaMosiaEkibo5aLl19xBrqmRUUfIO3LdU0MfbsPYLqCkyLNJIGucnYMw5t0L7JRNGqBtB9iaaibIVvvvz6uOicpzUykD8OVIVUaMn4/640?wx_fmt=png&from=appmsg)

找到了病毒程序，用火绒粉碎即可，并全盘查杀。有条件可以进行重做系统。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0LTz7Lex94VETEbQs0hSVPQeBPLE3uKb2neVyEAGtFQRWzjtJ3uCHtVjllz6QdKmTDdE1ibkyVib0nokZd9LywDA/0?wx_fmt=png)

小话安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0LTz7Lex94VETEbQs0hSVPQeBPLE3uKb2neVyEAGtFQRWzjtJ3uCHtVjllz6QdKmTDdE1ibkyVib0nokZd9LywDA/0?wx_fmt=png)

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