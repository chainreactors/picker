---
title: ChatGPT漏洞：部分高级用户数据已泄露
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535800&idx=4&sn=a17c0503c033b8619929b8b72b99e8ba&chksm=fa93fa79cde4736f4a97f370e65e2f4fb1cbd28c9dc26e525df76befae755c4852763dc4c559&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-29
fetch_date: 2025-10-04T11:01:52.366290
---

# ChatGPT漏洞：部分高级用户数据已泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lvicjYfgfcjiaeYYZQq8cFty5annhLyLRu3cUF8FR51scQfnn2tuaianvMLJH2ANYqEefqHrBj3g0mQ/0?wx_fmt=jpeg)

# ChatGPT漏洞：部分高级用户数据已泄露

网络安全应急技术国家工程中心

以下文章来源于红数位
，作者红数位

![](http://wx.qlogo.cn/mmhead/574VdhMFwaFfLImg5A1CEvy3u7jvATicibOlBqb9a5FgKISWE85CAGhlPTibpU3rfMLGLRFmmovzpc/0)

**红数位**

此前，OpenAI在3月23日修复了允许您在账户内看到其他用户的历史记录并查看对话标题的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vDJXDPrW7A0UTkFPYGicesnTJSzI7VkMK3bUMpjibwt0pVicgShibdOxxkRHDQib0ZnTHQthibUGI2Viauq7H2HLxRib3Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

随后，经过深入调查，OpenAI自己发现部分ChatGPT Plus用户的数据已被错误泄露。OpenAI 还提供了有关该漏洞的技术细节。

透露您的付款信息

由于这个漏洞，OpenAI紧急关闭了ChatGPT。该服务在大约 10 小时后重新启动，但此后已恢复正常。在进行更深入的调查后，OpenAI 发现1.2% 的活跃 Plus 订阅者在 9 小时内被向其他用户显示了支付信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vDJXDPrW7A0UTkFPYGicesnTJSzI7VkMKbBSgEXsKCklJbKaCQGoSmbmOlse712b47x6o2Jn5PWKN3t6RwAC5Lg/640?wx_fmt=jpeg)

数据泄露以两种方式发生：付款确认电子邮件被发送给错误的用户。后者随后会看到订户信用卡号码的最后四位数字。一些用户还在自己的账户内看到了其他会员：账户名、姓氏、地址、信用卡号后四位和信用卡有效期内。OpenAI表示联系了所有泄露信息的用户。

导致问题的漏洞存在于Redis 客户端的 redis-py 库中。后者被 OpenAI 用于将用户信息存储在服务器缓存中，以避免每次请求都访问数据库。redis-py 库用于连接 Redis 和 Python 服务器。该库在 Redis 服务器和集群之间维护一个连接池，并回收一个连接以用于另一个请求。由于这个漏洞，对请求的响应从缓存中获取了另一个用户的数据。Redis 开发者已经提供补丁来解决这个问题。Redis 是允许 OpenAI 允许数百万同时访问 ChatGPT 的软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vDJXDPrW7A0UTkFPYGicesnTJSzI7VkMKKwJnb6t8DebrP9B1Ug0WlGHk5ZvhtcFeNJHmORJWhFXQw3Zkh973zA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

OpenAI官方提供的技术细节：

该错误是在 Redis 客户端开源库 redis-py 中发现的。一旦我们发现了这个错误，我们就联系了 Redis 维护者并提供了一个补丁来解决这个问题。这是错误的工作原理：

我们使用 Redis 在我们的服务器中缓存用户信息，因此我们不需要为每个请求检查我们的数据库。

* 我们使用 Redis Cluster 将此负载分布到多个 Redis 实例。
* 我们使用 redis-py 库与使用 Asyncio 运行的 Python 服务器与 Redis 交互。
* 该库在服务器和集群之间维护一个共享连接池，并在完成后回收连接以用于另一个请求。
* 使用 Asyncio 时，使用 redis-py 的请求和响应表现为两个队列：调用者将请求推送到传入队列，然后从传出队列弹出响应，然后将连接返回到池中。
* 如果在请求被推送到传入队列之后，但在响应从传出队列中弹出之前，请求被取消，我们会看到我们的错误：连接因此被破坏，并且为不相关请求出列的下一个响应可以接收遗留下来的数据在连接中。
* 在大多数情况下，这会导致不可恢复的服务器错误，用户将不得不再次尝试他们的请求。
* 但在某些情况下，损坏的数据恰好与请求者期望的数据类型相匹配，因此从缓存中返回的数据看起来是有效的，即使它属于另一个用户。
* 太平洋时间 3 月 20 日星期一凌晨 1 点，我们无意中对服务器进行了更改，导致 Redis 请求取消数量激增。这为每个连接返回错误数据创造了一个小概率。

此错误仅出现在 Redis Cluster 的 Asyncio redis-py 客户端中，现已修复。

看来Redis对于OpenAI是一个基础性地基，类似2021年的Java的Log4j2开源日志框架的核弹级漏洞，简直算是OpenAI的一块敲门砖啊！

原文来源：红数位

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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