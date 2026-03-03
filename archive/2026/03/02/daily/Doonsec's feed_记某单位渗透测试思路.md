---
title: 记某单位渗透测试思路
url: https://mp.weixin.qq.com/s/7ZuNe0TAzq70eGhRwVasyw
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:48.414219
---

# 记某单位渗透测试思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zLpYr6HwSa2d6uwFQvibgJ4GB0TZUWbwh3rtpD5CSv4zyHKyLcKOXhramlj3FR15MRU4qPl7ibAN9yXUcUcCA8ezB5CBreGY7TIRzicGGiat7uk/0?wx_fmt=jpeg)

# 记某单位渗透测试思路

原创

XingyuSec
XingyuSec

XYsec

![]()

在小说阅读器中沉浸阅读

首先转子女神信息收集一波，找到一个敏感的js![](https://mmbiz.qpic.cn/sz_mmbiz_png/zLpYr6HwSa1NiaibqqYmKbnUhe9OWibjVVOgJiaTib3XIufdUR1gxMWIF0N43jCgOkZzjIBJy8a4XXFiaF4dIlP4AkZ6gxvWCY2sqn2IjMmicvkkKY/640?wx_fmt=png&from=appmsg)对这个jeecg不是很了解，当时是丢给了ai

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zLpYr6HwSa1ia3MiaeoKclUwUwebrOKibxo4VZkgtlLcczsD0Ajjz0u09ovGnZfEG3AGqDsOL7doI5ibfweBso0t8vvdOgTibzQNCTZjfeTSXfibo/640?wx_fmt=png&from=appmsg)拼接一波接口

```
/jeecg-system/sys/common/static
/jeecg-system/sys/dict/getDictItems/
POST /jeecg-system/sys/login
POST /jeecg-system/sys/login/login
POST /jeecg-system/auth/login
```

显示了Token失效![](https://mmbiz.qpic.cn/sz_mmbiz_png/zLpYr6HwSa0cRNL01B8z4licRVRoPBTvpwSXSFjumoB2ls5e61S5mK0Yffiaia7eK7LiafpVeIicUwqibW1Jwvib3aaFavs13a0icskicmPHibdSayYk8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zLpYr6HwSa1mp0jialXvBm2WDWewKXkMjia8Vj9InVkFl6S1icU2yeAJVSSJcC2MCbGJJFURM7JuaAWJSqpRQ9AznGcfibq0t4BNMtSwJoiaGolg/640?wx_fmt=png&from=appmsg)然后前台通过信息收集的账号密码进行登录，前台是若依的框架，然后复制cookie，通过x-access-token访问成功，x-access-token是jeecg框架的用来身份认证的请求字段

![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa3hZNequ8icRqYPprhBmxicFz1ZdAM5hwS9R04Aic55k4YezNx3HnbcibIQibmw8PkaUepcdZdLyzJauicE8U29YbTY9CUjw6nxDiaEV4/640?wx_fmt=png&from=appmsg)看到报错是一个spring框架

![](https://mmbiz.qpic.cn/mmbiz_jpg/zLpYr6HwSa1ndTbwSHEcnqe7gAvqLicWs4ibSo1vwZvpLOhB7kuKgeGptfvjboUiafRbhsS0LPbqFnf3HkUPoNEJrPO4ibRuicAnBlZ6n4d15SvM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa3xiasovLGbnvIfN9xiaw5MYBjNRbaOeLcJvKoRyw16ibicpd0OibW3ZXljuA5QqUIiaP38edafAyRy4DZgsxFd2ibXtplibybLCMle3UQ/640?wx_fmt=png&from=appmsg)其中heapdump可以下载![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa19Wc6GiaEessxd6gZUnwruJHoHA8R4WF7ZASWibC58khhPcUVmwnaNxAWVU0sNqXm7YibUbgKrO75YJ7s94YZpqmA68dictPVTy44/640?wx_fmt=png&from=appmsg)其它的就先不说了，很多信息泄露的东西，去上搜一下漏洞

使用nday进行测试，报错了![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa0PIIicuhnzplyenuaaKZibfl2Ql6628gqadrkVn80oxYrlqnNteFVktA9nemaQrPUUaQ7SILoplbb3x9VcdGxcoUyWYCrkhhNbQ/640?wx_fmt=png&from=appmsg)错误提示正确的语句应该是

```
GET /jeecg-system/sys/api/loadDictItemByKeyword?dictCode=字典编码&keyword=搜索关键词
```

获取字典列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zLpYr6HwSa0RMfpne5HJ14P6WLu2EkgKqcUcLVmBlGy6IYfMXuSKlgdqkGsxlXWKibjhw3T2JIiaU2IYRxcMJKUdmOktgiaCbiayP8LDL6RdwqQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa3l20psymTGPoAweVrwcib2rBStticqfMa9IG4D4OZbcg8JL9YTXfJWNMtNaXWNj84mIqYQJsCOrnA6fot99icST5S0Ejn4HvibYyU/640?wx_fmt=png&from=appmsg)然后sql注入

![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa1y4MNMtFU3h5wrurXZkNWHLFhPlZNvlsjOQlQkyFWMOwpR2uPWicBxZ00zJH8rVgOBiaP2F8LWQpx68EFltAO1aKarcFrx1BCkI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa1rjLpqEdfmwxYUPyKXoXYJzW6UqlluFdTT2YQYeT8pab3VoRhia8U2nibbhvFUTiboZGlbhPAQl5Pvf2bsaagtticu0ibETZHKrjsU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zLpYr6HwSa3w5I9VS75y3Xyp8jOj027bZ3QWRDMITHN5cdMlHLRveJhBu9hn1YjFuibokXtbDhiaQ7eGJIRvD5JV800WZOXl3WysfDMgY02u0/640?wx_fmt=png&from=appmsg)参考文章

```
https://github.com/jeecgboot/JeecgBoot/issues/3663
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xe5wgJuYy6Pnk1mmNGtzEKF9wPQ4W4gjckagzJndmymJ7ic6iacxcLCfVzuQRAwZApuib09TwF0EqsLn5Z23JUJDg/0?wx_fmt=png)

XYsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xe5wgJuYy6Pnk1mmNGtzEKF9wPQ4W4gjckagzJndmymJ7ic6iacxcLCfVzuQRAwZApuib09TwF0EqsLn5Z23JUJDg/0?wx_fmt=png)

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