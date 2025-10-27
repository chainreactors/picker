---
title: 【安全圈】ChatGPT数据泄露，技术细节公布
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031907&idx=3&sn=8a78e3508e4a0d2075c01fad30581d59&chksm=f36fe7e3c4186ef5e2e6c263f466c2eda9a768be6720120effc69e5ef966bb03542ab168b13a&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-29
fetch_date: 2025-10-04T11:01:34.327210
---

# 【安全圈】ChatGPT数据泄露，技术细节公布

![cover_image](https://mmbiz.qlogo.cn/mmbiz_jpg/aBHpjnrGyliaLYNeEvKRnrE5TwGfqR8vakqdwy55RetlYjW9uCA1OaETtUIgSRPk28WJhNic5pV35b9E87EuAmXw/0?wx_fmt=jpeg)

# 【安全圈】ChatGPT数据泄露，技术细节公布

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

数据泄露

在上周一，ChatGPT 遭遇了一次用户数据泄漏事件，许多 ChatGPT 的用户都在自己的历史对话中看到了其他人的对话记录。不光是对话的历史记录，不少 ChatGPT Plus 用户还在 Reddit 和 Twitter 等平台发出了截图，表示在他们的订阅页面上看到了其他人的电子邮件地址。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dkwuWwLoRK9M8G5jKwzBa59VPLrff1RxVMMEia11f7ZdQctc1vxhBwT81AWN0N6h0Fz0xQfENfLRUlIlZNRKJWg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

事件发生后，OpenAI 临时关闭了 ChatGPT 服务以调查问题，后续 Open AI 的首席执行官 Sam Altman 也亲自发了推文，承认他们确实遭遇了重大问题，不过当时并没有公布问题的细节，只表示是一个开源库的错误导致的。

![](https://mmbiz.qpic.cn/mmbiz_png/dkwuWwLoRK9M8G5jKwzBa59VPLrff1RxIRiaFHkYzEGwIPfvmUIu05gZbNLOOt68zRQZEeqRDk1awbvqDbBjntA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

> 由于一个开源库的错误，我们在 ChatGPT 中出现了一个重大问题，现在已经发布了一个修复程序，我们刚刚完成了验证。
>
> 一小部分用户能够看到其他用户的对话历史的标题。

经过多日的调查，OpenAI 日前发布了一份包含技术细节的事件报告，该事件是 Redis 客户端开源库中的一个错误所引发的，导致 ChatGPT 服务暴露了其他用户的聊天查询历史和大约 1.2% 的 ChatGPT Plus 用户的个人信息。

### **技术细节**

这个错误是在 Redis 客户端开源库 redis-py 中发现的。发现这个 bug 后，OpenAI 就立即联系了 Redis 的维护者，提供了一个补丁来解决这个问题。以下是这个错误的具体细节：

* OpenAI 使用 Redis 在他们的服务器中缓存用户信息，所以 ChatGPT 不需要为每个请求检查数据库。
* OpenAI 使用 Redis Cluster 将这一负载分布到多个 Redis 实例上。
* OpenAI 使用 redis-py 库，以便让用了 Asyncio 的 Python 服务器与 Redis 对接。
* 该库在服务器和集群之间维护一个共享的连接池，并在完成后回收连接以用于另一个请求。
* 当使用 Asyncio 时，redis-py 的请求和响应表现为两个队列：调用者将请求推送到传入队列，并从传出队列中弹出响应，然后将连接返回到池中。
* 如果在请求被推送到传入队列之后，但在响应从传出队列中弹出之前，请求被取消，我们就会看到错误：连接因此被破坏，下一个为不相关的请求出列的响应可以接收连接中留下的数据。
* 在大多数情况下，这会导致一个无法恢复的服务器错误，而用户将不得不重新尝试他们的请求。
* 但在某些情况下，损坏的数据恰好与请求者所期望的数据类型相匹配，因此从缓存中返回的数据看起来是有效的，即使这些数据属于另一个用户。
* 在太平洋时间 3 月 20 日星期一凌晨 1 点，OpenAI 无意中给他们的服务器引入了一个变化，导致 Redis 请求取消的情况激增。这在一定程度上引发了每个连接返回错误数据的可能性。
* 这个错误只出现在 Redis Cluster 的 Asyncio redis-py 客户端，现在已经被修复。

经过深入调查，OpenAI 发现一些用户有可能看到其他活跃用户的姓名、电子邮件地址、账单地址、信用卡号码的最后四位数和信用卡到期日，OpenAI 特别强调道，完整的信用卡号码并没有暴露。

这部分受影响的用户占 ChatGPT Plus 用户总数的 1.2%，目前他们正在联系了所有受影响的 ChatGPT 用户。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLYNeEvKRnrE5TwGfqR8vaicib2fpBx3h5sL2ZicVBDHBm8wb0XQXI7Nib6hD7sEA2L1V0g2UdJ90FQw/640?wx_fmt=jpeg)[【安全圈】涉案流水超千万！清河公安分局破获一起侵犯公民个人信息案](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031880&idx=1&sn=0722862e0f276e3ac0e251cfce5ea047&chksm=f36fe7c8c4186ede6eaff1a00b41d50cdc61f360ef755c4770cf906b89aef0508a9943002b27&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLYNeEvKRnrE5TwGfqR8va2LL2RqCXgKJtvDOStVqOoibiacFYBVL3Ps3wIHay5GpPlMh1Klw5SoWw/640?wx_fmt=jpeg)[【安全圈】推特源代码遭泄露 事件嫌疑人已从推特离职](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031880&idx=2&sn=0fb8728a3e8e171245b378db2541e089&chksm=f36fe7c8c4186ede295ceb0091ad1c7fedab7ed0fb3c5b4460028e2e3499702c57fb5ab1aa70&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLYNeEvKRnrE5TwGfqR8vaqhhQ6n2pa9DoJ3IhFGhLicvOghQKiboiccq826OIKQhUicqHnA0fFJFhEw/640?wx_fmt=jpeg)[【安全圈】黑暗势力：新兴勒索软件团伙在不到一个月内勒索了10个目标](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031880&idx=3&sn=64d377bb6c1cacbf53334a7f80cedfbb&chksm=f36fe7c8c4186edeea793af9efb754bdd24238e71e95328ab33b9f3eb136ceaeba15d5319996&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaLYNeEvKRnrE5TwGfqR8vaq6wuHTmvxQmnohN84Swiaa49kWgy01iaNSibxvueYZAMOYO7WcJqLpBtw/640?wx_fmt=jpeg)[【安全圈】Emotet 恶意软件冒充美国税务局进行网络钓鱼](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031880&idx=4&sn=789ec5b06811f9194a1f2450ccc9d3f5&chksm=f36fe7c8c4186edec764bac7040aae7c8b41605d9d57773e280dc0b0bfa723acc380d37418b3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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