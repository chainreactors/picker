---
title: 【安全圈】谷歌DNS服务器8.8.8.8/8.8.4.4出现短时间宕机 大量用户报告谷歌服务不可用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066435&idx=1&sn=07ab021fa1b5dbcc0323dbb29955eaca&chksm=f36e7ec3c419f7d580a99656a0506d7c5b52e6b557383f56465e6e41fabe477eba0032e6a807&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-07
fetch_date: 2025-10-06T19:40:11.763306
---

# 【安全圈】谷歌DNS服务器8.8.8.8/8.8.4.4出现短时间宕机 大量用户报告谷歌服务不可用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgdme7EAeBhHP74oFZvnicp3Wek491e5MyarVk5RPB9lqiawS9yqa4x7agwACJ3Y4Pw4p24M9OvtZjg/0?wx_fmt=jpeg)

# 【安全圈】谷歌DNS服务器8.8.8.8/8.8.4.4出现短时间宕机 大量用户报告谷歌服务不可用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

DNS

谷歌公共 DNS 服务器 8.8.8.8/8.8.4.4 出现短时间宕机，大量用户报告谷歌各项服务不可用。这次故障发生在5号下午五点多 (太平洋时间为凌晨 1 点多)，期间用户报告谷歌地图、Gmail、谷歌搜索等不可用，随后这被确认是谷歌 DNS 服务器故障导致解析大多数网站都返回错误，该错误持续不到 10 分钟被修复

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgdme7EAeBhHP74oFZvnicp3uQ37RsEFRRS0heic4F4MuhqgSVCQvyNqnD0QrWtTicFJqBJ6yNzwH7nw/640?wx_fmt=png&from=appmsg)

原本大家以为这是谷歌服务器出现故障 (这么说也没错)，不过后续发现出现故障的是谷歌公共 DNS 服务器 8.8.8.8 和 8.8.4.4，这些 DNS 服务器解析谷歌相关服务时返回错误信息。

当然除了谷歌服务外用户如果打开其他网站或服务也发现出现解析问题，谷歌暂时还未公布详细情况，但已经可以确定这是谷歌公共 DNS 服务器发生短时间中断出现的故障。

这次故障只持续了几分钟就恢复正常，由于是 DNS 服务器本身故障，在完成修复后用户可以立即恢复各项服务的使用，不需要等待 DNS 解析传播到全球。

根据 Downdetector 网站显示的用户报告，我们可以推测故障发生时间大约是 12 月 5 日凌晨 01:58 (太平洋时间，UTC-8) 到 02:04，具体情况可能还需要谷歌后续更新状态页才能知道。

还有个可能要提下的是，建议各位设置 DNS 服务器时最好分开设置不同提供商的，例如你可以设置 8.8.8.8 作为首选 DNS 服务器，将 1.1.1.1 设置为备选 DNS 服务器。

这样假如首选服务器出现故障还能通过备选服务器进行 DNS 查询，然而这种方式似乎不适用于谷歌这种故障，因为 DNS 服务器本身是可以连接的，但内部系统出现问题导致无法正常返回解析值，这种情况下操作系统应该不会认为 DNS 服务器故障从而切换查询。

来源：https://www.landiannews.com/archives/106926.html

***END***

阅读推荐

[【安全圈】Crypto.com 与 HackerOne 一起推出 200 万美元的漏洞赏金计划](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=1&sn=8b5178681a68125be7487364041e0e92&scene=21#wechat_redirect)

[【安全圈】立即修复，微软驱动程序关键漏洞已被APT组织利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=2&sn=c856137ec845bc74a8a86abc23c1eb69&scene=21#wechat_redirect)

[【安全圈】谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=3&sn=28c802936604146904c583d74c14846f&scene=21#wechat_redirect)

[【安全圈】知名伏特加品牌因勒索攻击而倒闭](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=4&sn=7bf50178818225897c7e681c7ddab487&scene=21#wechat_redirect)

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