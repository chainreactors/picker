---
title: 某vue网站的渗透测试
url: https://mp.weixin.qq.com/s/k8JJp3tYMrsOg4Ty2pX_tg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:35:20.922294
---

# 某vue网站的渗透测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WIsafK5ZZfkCuyZ5dSwFRjnSpFRUmh2KHrMSwBr6fI1erSp2xf7vBLQ/0?wx_fmt=jpeg)

# 某vue网站的渗透测试

点击关注 👉
点击关注 👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

作者：Asen

原文：https://xz.aliyun.com/news/19378

本文章中所有内容仅供学习交流，严禁用于商业用途和非法用途，否则由此产生的一切后果均与文章作者无关。

前言

记录在某次演练的过程中一个有趣的记录。

案例

还是开局一个登录框，先看看是什么指纹发现是Vue的就先偏向去测试接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5taQCibQzEEtQQnMjbcVCmwIeqTxqzmeMHQUsYE1qyMXVSV6zt5MPaibw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

就在findsomething上先看看有没有一些有用的接口,看到这一段接口就有点未授权的味道了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5DAkg2srzabgwUDMgfZYna8Z4xpnSRYDm6nib9ibSZSgxyIILlYF8Mstg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

先用Vue Crack看看有没有一些未授权的路径进去看看还真有东西，这个插件使用起来也是非常的方便，他会自动识别是否未vue，如果有的话他就会自动添加路由。

下载地址：https://github.com/Ad1euDa1e/VueCrack

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5mD9gA6UH3HVTKc4dLVqIsJJefFn7RdeoaG3XIm0QxpszxDVY6hE9QA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

随机找一个，直接就进来了可能这个时候虽然没有任何信息，但是我们可以点击网站功能点看这些功能点是否有鉴权问题，还可以测试以下sql注入这些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5LrfVnfBRiaXmMvzPFjzDiaBUibYE2RtDxN7S4DKvWHBOtzXQgeiamsu4Qw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

这里我简单的点击的一下查询功能，没想到就直接查询成功了还是有点意外第一次遇见这种情况，而且这里的数据量还是非常的大一页有十条一共有四千多条，就是4w+的数据了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5Bwk8VwFzRYeHMVFUm4ZicYRNm0dNrIoCnHBicAoaojy7xe0eUeBkKODA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

既然他一个点都没有鉴权哪肯定会有很多未授权的地方，重新回到登录口看看接口。插件匹配的接口肯定是不完全的，这里就f12看看前端的源码，然后在刚才的findsomething中看到有/api这个单独的接口这个站应该是一个前后端分离的网站，api应该是后端的接口，所以就直接搜api看看他有没有想关联的接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5jZlibfdNXafhSFvYegUJU4c4YoUWwJpTc4T4ZVYwBT7Avd66HkwxCcg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

这里果然有东西，也看到了api的前面标出为post请求，而且还有几个list结尾的如果能跑出来估计也能有不少的数据了，但这个地方需要注意一个点就是，不能把这些接口拿出来单独跑，他的前面是一定要加上/api，因为在前面的测试中我在抓取登录口的数据包是发现他的每一个接口前面都是加上了/api的因为路由前缀挂载机制，所有后端接口均被统一绑定到 /api下。因此实际调用接口时必须携带统一前缀。抓包测试！！！我这里就直接抓取刚才的查询接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5NcnqI0akshletK2AxjkHMuJPvPicPr13RyTWlRic1fk6QQFFk1Jw44Pg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

然后先进行一波fuzz，前面几个接口基本上都有数据这里就不做展示了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5uD2fh27poncGTd0e9I4ePbmOcetKGE5J1bkibFGmXNZxQ0xaIp5meSQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

然后这里有一个特别有意思的点，还是回到刚才的查询的功能点，这个是查询的那个数据包，返回的数据跟在前端的数据是一样的，但他的下面有一段请求参数，这些参数也是可以控制数据的数量，但是有一个很神奇的点是，我想对这个接口进fuzz，把那些参数删掉，他居然重新返回了新的数据，而且体量还非常的大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5R6o8Eah7TgFiaYm0hJMONHicT0liaXGfHun5Aic6JahckO1YRssknp9HjQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

我把以上参数删除以后，进行发包，他居然返回了十八万数据，我只能说太神奇了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEYyzAOgVboltbeFKtkaDR5r1KmfRjXzSvokMd3EDI2v54tyWnDbEeJgVvm24iaibP8FjMUI1lRmeFg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAkmMvIEVFdiaG19OichW7IMqrianjXzneqZoJ3rMMFygyGVdictzTMWy15vH5nhoWznKInJQ9yXzBpBFg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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