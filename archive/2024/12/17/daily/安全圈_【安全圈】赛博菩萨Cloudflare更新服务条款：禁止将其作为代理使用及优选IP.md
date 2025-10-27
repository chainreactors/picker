---
title: 【安全圈】赛博菩萨Cloudflare更新服务条款：禁止将其作为代理使用及优选IP
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=1&sn=eac9fa65e1d3c1f6c5688eacc6c39188&chksm=f36e7f0ec419f618a0388cac9858804b3c014ddde11a1155571592a286fc5cba452f8a30bca4&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-17
fetch_date: 2025-10-06T19:40:14.044132
---

# 【安全圈】赛博菩萨Cloudflare更新服务条款：禁止将其作为代理使用及优选IP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXY7kgOyFfvdBibwCl8ZgOZ2vFvMLVIpVtKiaY3gT4huXAPmukRnGzyQzvg/0?wx_fmt=jpeg)

# 【安全圈】赛博菩萨Cloudflare更新服务条款：禁止将其作为代理使用及优选IP

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Cloudflare

Cloudflare 于 2024 年 12 月 3 日更新了其用户协议，明确禁止将其服务用作代理用途，同时强调不得使用优选 IP，否则将视为违反服务条款，并可能导致账户封禁。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYI8XzsCEJMYGjJTBn9m0iaHfN8RMWqiawWtAoYUG15AYj3P0pxeiadPS9Q/640?wx_fmt=other&from=appmsg)

此更新的相关条款出现在 **Cloudflare Terms** 的第 2 项服务、第 2.2 项使用服务、第 2.2.1 项限制中。Cloudflare 在这些条款中列出了 10 项明确禁止的行为，其中包括明确禁止使用其服务来提供虚拟专用网络（VPN）或类似的代理服务。具体而言，第 2.2.1 条款的第 J 项规定：**"不得使用服务提供虚拟专用网络或其他类似的代理服务"**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXY87tjABtdtHWAlHSsNZRW1cQib90TRZkVDcjo5JjEMa2nKJC9vbM5NAQ/640?wx_fmt=jpeg&from=appmsg)

目前，确实有不少开发者和服务商利用 Cloudflare 提供的免费网络服务（如 **Cloudflare Workers** 和 **Cloudflare Pages**）来提供代理服务，这主要是由于 Cloudflare 的免费服务覆盖广泛，并且其全球多个数据中心可以帮助绕过例如 OpenAI 等防火墙的限制。然而，这种用法显然违背了 Cloudflare 服务的初衷和条款。

此外，另一个需要注意的问题是关于 **优选 IP** 的使用。所谓优选 IP 是指用户通过手动选择 Cloudflare 数据中心的特定 IP 地址，而不是依赖 Cloudflare 默认分配的任播（Anycast）地址来优化连接速度。这种做法在 Cloudflare 的第 2.2.1 限制第 B 项中也被明确禁止。该条款规定：**"不得干扰、破坏、更改或修改服务，或对网络和服务（包括 Cloudflare 合作伙伴的网络）造成不当负担，特别是不得通过非 Cloudflare 为该域分配的 IP 地址来处理流量"**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYCsHoGXeJpNN1dK0uP4VbliblyjxmcQnUa7m8IkhvkhPOt31M0BOfzSg/640?wx_fmt=jpeg&from=appmsg)

总结来说，Cloudflare 强调用户必须使用其为域名分配的 IP 地址，不能通过手动选择优选 IP 或修改默认的任播地址来规避这一规定。若用户进行此类操作，将被视为违反其使用条款。

对于长期使用 Cloudflare 服务的开发者和站长来说，这些更新可能会产生一定影响。为了避免账户被封禁，建议用户停止将 Cloudflare 服务用作代理，并确保不进行优选 IP 等违规行为。根据 Cloudflare Terms 第 8 项规定，任何违反条款的行为都将导致失去使用服务的许可，Cloudflare 还保留对违规行为进行调查和处理的权利。

来源：https://www.landiannews.com/archives/107113.html

***END***

阅读推荐

[【安全圈】千万悬赏：美国追捕四川黑客关天峰，指控其全球感染8万防火墙](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=1&sn=a53c860727d887307f935b429a2162da&scene=21#wechat_redirect)

[【安全圈】最高人民检察院：三名小伙「变相换汇」USDT 与人民币，遭判处五年徒刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=2&sn=7387c9bfc5ce3c826968c7e7dc0ec037&scene=21#wechat_redirect)

[【安全圈】超 30 万 Prometheus 服务器暴露：凭证和 API 密钥在线泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=3&sn=e357cb32259162fcaa4e589951d9e4ea&scene=21#wechat_redirect)

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