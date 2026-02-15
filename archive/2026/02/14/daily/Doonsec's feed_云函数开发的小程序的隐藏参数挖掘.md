---
title: 云函数开发的小程序的隐藏参数挖掘
url: https://mp.weixin.qq.com/s/vlzvLHg8b7-6oOssPa60Gw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:55.669190
---

# 云函数开发的小程序的隐藏参数挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OmrJwhwoWJr8B7LbdViaT2dRM8QLhC3RgG7Cavw9icsbo7eQNBPZL8buy2vuSAkbd3nic5nYNoZtGoJ3R87P8wib1SxicSZ9PmJ6Kxaic2KPl81zU/0?wx_fmt=jpeg)

# 云函数开发的小程序的隐藏参数挖掘

迷途
迷途

希望对技术保存热情

![]()

在小说阅读器中沉浸阅读

正常登录小程序之后点击任意功能

![](https://mmbiz.qpic.cn/mmbiz_png/OmrJwhwoWJq4Q86bpeFVujG0DmkajH1eAcT6pIRgAexiaOJ9QcVCOdRGPSdw4Oqw5wQmY5AgnADkUQYBx5IIfSBtibYD07brWibKwxeImzpENU/640?wx_fmt=png&from=appmsg)

直接来到流程管理可以看到我们是什么都没有

![](https://mmbiz.qpic.cn/mmbiz_png/OmrJwhwoWJr0AuQg87tqPwBdcMwpcnNdzYBm0jOayiaibqmIPXxTBtuib1TpokUxeH9XuMduLe7pY0rXx7UWDqmsU4Lmh4InVvlzasgBMAYOlo/640?wx_fmt=png&from=appmsg)

全程开着burp怎么样都抓不到包，开始没感觉，以为自己的环境出问题了，一直在后面了解到云函数开发才知道，不走常规协议

那怎么测？

两种方法

1、有大佬好像写了工具但是2k一年，额有点贵。

2、开控制台全程f12断点开始测

这里全程控制台测直接开f12

在退出的时候F12调试来到

b01593202e9f0d920278aae7287df1e5-11159-V0FTZXJ2aWNlTWFpb

这个文件下断点，全局搜索log: u，在这里下断点，可以看到断点也是说明云函数开发

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OmrJwhwoWJr0GJnVPoMSFDRnyggs32y0icXJ9kJvMxGOszsNpNT8perBySBTV4FLoCw2nF6y2VwWYpibZKPsT5fHswAQgMxum1pOYiaG5VjiaWo/640?wx_fmt=png&from=appmsg)

然后一直放包直到出现存在内容，然后添加t和u的索引1的数组插入上”admin”:”1”，这个u这里就是我们正常抓包的参数，呈现如下最后一张（为什么插入这个，纯fuzz的）

![](https://mmbiz.qpic.cn/mmbiz_png/OmrJwhwoWJrRDibCNHZibTHUs3yfr83YibbSggLneicMx4ziahdtjV0ibKmpRMSuP90fRSQQBZSh8VaEquT3XUUOokaRm1fOto0licyFVYWuh5ApKA/640?wx_fmt=png&from=appmsg)

然后在看直接数据拉满了，直接admin账户了

从0变成有数据了

![](https://mmbiz.qpic.cn/mmbiz_png/OmrJwhwoWJrvdvJ66hjgfbJlAu7gWic11fMmdvlqLy86jqtxlyR7XCesbQKicibxL9YoJhwCg2CTQINztKuic9Eaia1DibkLicelGKmraxtqIX1GOc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkIP0OOqvdFXbgPjK5wic9lE6sU2zPOm9furhribFbZvfaSOXOicfPSUhuLicPcqN8bWcmTmJX6Sj5ZiajEg/0?wx_fmt=png)

希望对技术保存热情

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkIP0OOqvdFXbgPjK5wic9lE6sU2zPOm9furhribFbZvfaSOXOicfPSUhuLicPcqN8bWcmTmJX6Sj5ZiajEg/0?wx_fmt=png)

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