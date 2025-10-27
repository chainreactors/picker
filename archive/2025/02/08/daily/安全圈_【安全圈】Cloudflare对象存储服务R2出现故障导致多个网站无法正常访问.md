---
title: 【安全圈】Cloudflare对象存储服务R2出现故障导致多个网站无法正常访问
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067692&idx=3&sn=b4bcff9fa2ad79fcb9370d738673957c&chksm=f36e7b2cc419f23a93b81f2e6c46c91f78b07e2fd0126b9be5c5613c8a501f2c90d29122bf96&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-08
fetch_date: 2025-10-06T20:47:06.869803
---

# 【安全圈】Cloudflare对象存储服务R2出现故障导致多个网站无法正常访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WicX0EhGb2EMQAqne4bETDd8cfahjczvK3HfRfIdmZOEzOmI0ys5SZibA/0?wx_fmt=jpeg)

# 【安全圈】Cloudflare对象存储服务R2出现故障导致多个网站无法正常访问

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

cloud flare

目前，由网络服务商 Cloudflare 提供的对象存储服务 R2 正遭遇故障，影响了多个服务，包括但不限于 R2、Durable Objects、Cache Reserve、Key Transparency Auditor、Stream、Logpush 和 Images 等。R2 通常作为网站或 App 的文件存储解决方案，外部通过 CDN 进行加速和嵌套访问，因此，虽然 CDN 能继续提供缓存中的静态文件，但对于新的文件请求则无法进行处理。

![Cloudflare对象存储服务R2出现故障无法正常访问 影响多个网站的使用](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WoZjFle3UqASROBQvGUHgmgBRR11YYR4BnnsK2SkWwibLTowPwo5Hhjw/640?wx_fmt=png&from=appmsg)

此外，一些网站和 App 将用户上传的文件直接存储在 R2 中，当前故障导致这些网站和 App 的上传功能也受到影响，而这一问题无法通过外层 CDN 来解决。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1W3oBL6T00PNnr7JwPibArNoUw5ibNDrBhJPzzuz36xcgficfoicG2m984LA/640?wx_fmt=png&from=appmsg)

图源：https://www.cloudflarestatus.com/incidents/pgz7g5xlpxzr

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WjNzfA6uexxSFRJKNbOWTb33hxHRia7JsqkcCC4VvSwQuaA1EjJWwlEQ/640?wx_fmt=png&from=appmsg)

来源：https://www.landiannews.com/archives/107777.html

***END***

阅读推荐

[【安全圈】PyPI 上的信息窃取恶意软件冒充了 DeepSeek AI 工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=1&sn=87a028f93da64d77ab88febfae2b2d56&scene=21#wechat_redirect)

[【安全圈】2024 年勒索软件支付额下降 35%，总额达 813,550,000 美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=2&sn=20f95ef580e0ec24f8d83012372886ab&scene=21#wechat_redirect)

[【安全圈】恶意 Go 软件包利用模块镜像缓存实现持久远程访问](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=3&sn=0a2ed43f7e7eb5e16bbf8a4cf07d0964&scene=21#wechat_redirect)

[【安全圈】研究人员发现新方法防御 AI 模型的通用越狱攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=4&sn=027c0126ec6f44288fe766c11d208124&scene=21#wechat_redirect)

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