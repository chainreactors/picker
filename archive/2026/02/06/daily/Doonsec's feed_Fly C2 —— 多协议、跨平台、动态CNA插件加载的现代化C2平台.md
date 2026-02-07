---
title: Fly C2 —— 多协议、跨平台、动态CNA插件加载的现代化C2平台
url: https://mp.weixin.qq.com/s/Mq2OTTYzFFYcsf7aJLh6Wg
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:04:22.109967
---

# Fly C2 —— 多协议、跨平台、动态CNA插件加载的现代化C2平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBFF8f4SAXCGz3iam78x895eIzwz1gsIEQPC7YmajXt2UIIDqOMAUILXSDIxlJ1bGfdYewF6XYcibJDBzaTPgTU1w5yRWicqfeQOSA/0?wx_fmt=jpeg)

# Fly C2 —— 多协议、跨平台、动态CNA插件加载的现代化C2平台

原创

MaoKu
MaoKu

毛酷红队

![]()

在小说阅读器中沉浸阅读

## 前言：Fly C2和其他web C2平台相比有哪些优势?

书接上回,距离上次《Fly C2开发实录》文章发布已过去3个月了。按照之前的计划，预计是12月底完成Bete发布，但直到这周才完成了Bete版本的全部开发、功能测试、线上部署。为什么比预期慢了这么久呢？

我觉得主要有三点：

* • 把之前想砍掉的cs部分功能都加上了。
* • 整个平台开发难度比我预期的难很多，工期预估短了。
* • 测试过程花费的时间比较多，每个功能在本地和线上测试了一遍。

不过好在春节前顺利完成了Bete版本，大家可以在文末加入内部测试群，免费获取Fly C2。

Fly C2和其他web C2平台相比，优势有哪些？

* • 0学习成本，基于CS设计理念，开箱即用。
* • 首个支持CNA插件加载C2平台。
* • 可以saas化部署，支持多用户、多Teamserver连接。

## 一、核心功能

* • 多用户登入
* • 多Teamserver连接
* • 支持CS4.9.1版本95%的功能
* • 支持内置插件集和动态加载CNA插件
* • 仪表盘

## 二、多协议与跨平台

* • 支持windows、linux、macos平台
* • 支持386、amd64、arm64架构
* • 支持HTTP、HTTPS、TCP、UDP、DNS、DoH、DoH（TLS）、KCP、WebSocket、WebSocket（TLS）、OSS、SMB

## 三、效果展示

* • 登入界面
* ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBGz1KribShl09Loa3PO4XicviaSrp9KCcjPfgPQdt9OQGmicCCRqAloicHZ54DwnATdy0z5n6FRJpiaiaaShfYdNLH55vNHVIg4sTiaicQE/640?wx_fmt=jpeg&from=appmsg)

* • 仪表盘

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBEMsyKIq6BvcuibdtlhjdapmlueqdT0KVcKQWOvsW0ibtyWfeDxz82SVIHwCJcHtuhwpBFORX9p17iaUAgrDfZoUoCAZ4HpVKSACQ/640?wx_fmt=jpeg&from=appmsg)
* • Teamserver管理

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBEdWeMYXJQkIStWP9HTWLNS7FFv1VwnLUwR7cwzaicGJbJ0XyjbibJibEptDh3FkNCQLMWlmFH83ojlThF3eLKhSicOMW10w7EqPJc/640?wx_fmt=jpeg&from=appmsg)
* • 插件管理

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBHcWmDxPVzNP9OfFIzd8gR1ZPW6uuTLKEK3ibXL3xhA7iboqiavgCpwwF7ibs7iciacE49icicg18fbmDb81L7gZno2egLibE4EqQhX2ToE/640?wx_fmt=jpeg&from=appmsg)
* • 功能介绍

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBHsgiaYwoBkt0hFScaAael7SVhylwNgzFBs7H7067E5Tr4VIwXGsDN1x30BWsgF73WW9j9nUpL34seAFYg6x6wNzE9n3xMLrclk/640?wx_fmt=jpeg&from=appmsg)
* • eventLog

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBEaicNYBH7NkzD95Wl6dsC2LXbpGHHppWgvTXOWABB3hTfDhe2rV04bkuy3frGEWOUS1WE8x64HJ8SU9WWyDibZcibruGaaUB1XPA/640?wx_fmt=jpeg&from=appmsg)
* • beacon Interface

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHzfkbJictmw1oF5FQ8c8JyiaJTtJm85oOwerX230bUAfVt1cNF0qicnkW4KmZO7J7bEP6ibzqbN4hqeQHwdFHmH8eE160dIll8ELg/640?wx_fmt=jpeg&from=appmsg)
* • CNA插件

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHqEoIdlfia1MYPrM9qVopAwP4DXjWyn94uPWSo8aRejqhiatANicwlgHhmukGeqGAJRq78GwoiawCB1G0w4tibcmeo48EaSL3mCGxE/640?wx_fmt=jpeg&from=appmsg)
* ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBFXwGOP1UTGnnJ7BeQVSk3A5YJyxXnib69Olx9pzxsgoccd7kiaBCXYOicdgqFx1mUv3lRWAD6C2FaY7icXXibbyG35xH6AOiaLgqscY/640?wx_fmt=jpeg&from=appmsg)

  • 文件列表

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBHnichv1eM1cVAuYxw9jRTw4FiaF1szbYj6Mhn3cO9q4URZzKFZesBjm6mmyzicnHOXcQe5x6fMq1sDh0Vv3sgMmXkFhxUIVDx63s/640?wx_fmt=jpeg&from=appmsg)
* • 进程列表

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBEtXib7zyibV2GM4Q5c2DPMv29DelZ2gZpPBibTicMpxlxfSp4YoibAXJ099ichAn4zVyGA02lOVHtmeMArHWAZ8tHwFVia4OkaplJNcM/640?wx_fmt=jpeg&from=appmsg)
* • 文件下载

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBGfbibqGibgic4Q7JzFhHl4ia71KEPL8jK5F1Ko2ia9sA2xVcIWuF9EFMbrAjfwLPiaJalcJxVqs3VZ25RORW5MLx6u9IvIcact5RVWM/640?wx_fmt=jpeg&from=appmsg)
* • 截图管理

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBENRoeJBUgA70jVULZnibO7eepMyRgB8B69mbajQ4a6JQ85V9m281MMc5KibAgf5lyj8wicUkTP1jp8ibyuu5rnulnvFILQh8KLwtg/640?wx_fmt=jpeg&from=appmsg)
* • 监听器

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBFmgicmrRd2icRxyGxQCWTtqqG4VHIlx9H1EEiazIib7icth5BoRzW3IckKGUyVOpJqYC8jA3eFP7u3nLEMylia0c1R7N3Yb3hOfLU58/640?wx_fmt=jpeg&from=appmsg)
* ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBGHtqIPY1dQ3GUcfP81S3ibFfK6s7dvRh9CqnMVUE7O01kUeOCrweQb2XP5dgUrS2xB6x5afYscmF3UVpnVbBicIOVxPDg8NElWU/640?wx_fmt=jpeg&from=appmsg)

  • payload生成

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBHQAwIiawSiaT4SiaEhFs0HGBSKw1ROpj289bo3X6mmdgaUqL7zBdjoYyicbxNxTdgoKovpT70kCR05kr04m8hUnH5u5uZNlUuDzxA/640?wx_fmt=jpeg&from=appmsg)
* ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHRuJzuWFMqFSuefvC41B6AVmia1XLDvVHXShU9fgVb00jwoZzj05IicWcajoVba8IvmyvT2hvw7xJDaxtMOx1HVhjickctoRmjuU/640?wx_fmt=jpeg&from=appmsg)

  • pivot

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBFibJ5JYrCT6XV0GXy1mEic7lSrpmZJkjPnXyorbAJzhjHYxm3mnIdLdAkdxIX0llsmiaHDXwxfIq2e7gxIanxlt1VRkZgicPTpbrM/640?wx_fmt=jpeg&from=appmsg)
* • Targets

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBFLQBTDzN3wmkgiaic7d4Q2BB34fxkJTEm4YM0HQDL9ewk8LhyP2veeviapLoH8A69AottOkD8DlfRjBWxgMhmGnQCIthia0tzUjY8/640?wx_fmt=jpeg&from=appmsg)
* • web site

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBEzhH6vibmdfoYCwKs1xhlkZRpXgu0D3dkYYzp5gozK3icic2iazgl6ZfZc0K8BdDasIhAHymicFIbcXrkbg2P92vQtL1Pge7Xicbr7w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBGvAMI3FebwhRfqCWK7CdlC9OSP5yZmYFM8WCVJX1ZT22U3q2AlfthnxPic0MQy3AEr8DbCEfYlia1lLm3FfKsDQTHRExVUjzCa4/640?wx_fmt=jpeg&from=appmsg)

## 四、总结

从最初的想法,到Agent适配CS协议,再到现在的全栈开发,最后到今天Fly C2 Bete版本开发完毕，Fly C2项目走过了曲折但坚定的道路。

而这只是开始，Fly C2需要不断的**迭代优化**、从**能用到好用**是一个长期的过程，需要不断的努力。

如果你喜欢这个项目,**欢迎点赞、转发**让更多的人知道Fly C2!如果你有好的建议或想法,**欢迎私信交流**!

免费加入内部测试群，获取Fly C2，快快用起来吧！

---

**关注我,获取Fly C2最新消息**

#FlyC2 #C2平台 #红队工具 #网络安全 #自研工具

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oy1G7849AibBQDlENZ5c4usy9QawIN8mFQb8IiafOnZ7tW5KFMQ8Z5aHlEIsEvIiciaYmcT6hPhxFWd92CW6QlcXhw/0?wx_fmt=png)

毛酷红队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oy1G7849AibBQDlENZ5c4usy9QawIN8mFQb8IiafOnZ7tW5KFMQ8Z5aHlEIsEvIiciaYmcT6hPhxFWd92CW6QlcXhw/0?wx_fmt=png)

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