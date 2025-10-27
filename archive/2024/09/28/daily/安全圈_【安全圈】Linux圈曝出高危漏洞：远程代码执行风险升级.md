---
title: 【安全圈】Linux圈曝出高危漏洞：远程代码执行风险升级
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064708&idx=2&sn=bf69c637c7d271c8d448931606eaae24&chksm=f36e6784c419ee924165c15dde3c2a7866369a8243bcdc17416bd9e83f80b425804d7f0d3c77&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-28
fetch_date: 2025-10-06T18:27:54.545488
---

# 【安全圈】Linux圈曝出高危漏洞：远程代码执行风险升级

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgNJia6hlJRqTia35eOteXiasajwXQNGgYU9sibHibPpeiaAIp3w7C9CDyxdMlmwicEOjr9vfZkXLc1ELEmg/0?wx_fmt=jpeg)

# 【安全圈】Linux圈曝出高危漏洞：远程代码执行风险升级

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

2024年9月27日，Linux社区爆出了一起引发广泛关注的重大安全事件。著名软件开发人员Simone Margaritelli在社交平台X上发布了关于一个严重的远程代码执行（RCE）漏洞的警告，声称该漏洞已经隐匿存在超过十年，几乎影响了所有的GNU/Linux发行版。根据Margaritelli的评级，该漏洞的严重性达到9.9/10，标志着潜在的重大安全隐患。

这一漏洞主要存在于Unix打印系统CUPS中，尤其是在启用了cups-browsed服务的用户面临着极大的风险。攻击者若能够利用该漏洞，便可远程控制用户的设备，从而造成灾难性的后果。然而，目前还没有可用的修复补丁，这令不少用户感到不安。

在漏洞被公开后，CUPS开发团队对此次事件的处理方法存在分歧，部分成员甚至质疑该漏洞在实际应用中的安全影响。这种对漏洞严重性的争论使得用户更加无所适从。尽管研究人员已经提供了多个概念验证（PoC），但在实际解决方案的推广和落实上却进展显著缓慢。

**一、 漏洞介绍**

CUPS（Common UNIX Printing System，通用Unix打印系统）是一个打印系统，它主要是使用 IPP（Internet Printing Protocol）等协议来管理打印工作及队列。

2024年9月27日，互联网上披露 Unix CUPS 远程代码执行详情，利用链涉及多个CVE（CVE-2024-47176/CVE-2024-47076/CVE-2024-47175/CVE-2024-47177等）。当cups-browsed进程监听（默认631端口）接收UDP数据包时，攻击者可构造恶意请求，在无需认证的情况下可能在受害者机器上执行任意命令，控制服务器。漏洞实际是否可利用和触发需要依赖具体环境（例如存在打印任务等）。

**二、 风险等级**

Unix CUPS 远程代码执行漏洞 高危

**三、 初步影响范围**

CVE-2024-47176 cups-browsed <= 2.0.1

CVE-2024-47076 libcupsfilters <= 2.1b1

CVE-2024-47175 libppd <= 2.1b1

CVE-2024-47177 cups-filters <= 2.0.1

由于各软件方以及各操作系统发行方尚未发布新版本，具体影响范围仍可能有变动

**四、 安全建议**

1、若无需要，建议关闭 cups-browsed 进程。

2、利用安全组设置 cups-browsed 进程端口（默认631）禁止接收UDP数据包，或者仅对可信地址开放。

3、截止目前尚未有安全更新版本或补丁正式发布，待发布后建议升级更新至最新版本。

**四、 相关链接**

https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/

https://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8

https://github.com/OpenPrinting/libcupsfilters/security/advisories/GHSA-w63j-6g73-wmg5

https://github.com/OpenPrinting/libppd/security/advisories/GHSA-7xfx-47qg-grp6

https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47

***END***

阅读推荐

[【安全圈】只需10分钟即可被绕过，Chrome浏览器最新cookie安全功能纸糊的一样？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064683&idx=1&sn=167e100c99decc05bab52a43df1f9287&chksm=f36e67ebc419eefddb6532c146b8a9cbe2061fd1bb632b0b2a5c12c9699792c57e0d8d267cc9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljplzibkdYwJLibrdAUDEFuPgPYdQoBeqzFImyoib7wT7fGSBJhUAaZRJ4bpGTlrMRTQ4fjHvgI4UYhg/640?wx_fmt=jpeg)[【安全圈】黑客囤积法国9500万条公民数据，竟直接免费公开了](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064683&idx=2&sn=2c60b1ffb25d0b1af1b1f4c1e5daa42d&chksm=f36e67ebc419eefd07e516386056f703b314e62a31df8c8f4abfaf37b84e876f24de6e9a729f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljplzibkdYwJLibrdAUDEFuPgUOMjwOQfZuYsyliafM4wvQn6EBA8UTvlPjMwfhbJOmFfZmCRU3710Sg/640?wx_fmt=jpeg)[【安全圈】众议院听证会上，CrowdStrike 将蓝屏事件归咎于“多种因素叠加”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064683&idx=3&sn=dd24580e6a869ea3a0f9fcd6bbcfa5eb&chksm=f36e67ebc419eefd5aebc183d2fda654e56bacd0e9610128d8dc24acd9dbd96a22f1b7d1852d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljplzibkdYwJLibrdAUDEFuPguFic64c57uFCPLFatI9cdQzOlkZ5IueqYNCkLlqyibuq7krjP1gIalfQ/640?wx_fmt=jpeg)[【安全圈】HP报告：已在野外发现生成式AI制作的恶意软件有效载荷](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064683&idx=4&sn=ab35e9c62ad8ef0e9ed86ac8f3a5162a&chksm=f36e67ebc419eefd41730cf0e995b4bed45106792cee6c3f3b62dee630212dfa1d37a9641d4e&scene=21#wechat_redirect)

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