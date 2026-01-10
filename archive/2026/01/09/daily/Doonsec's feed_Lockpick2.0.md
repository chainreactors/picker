---
title: Lockpick2.0
url: https://mp.weixin.qq.com/s/_wAP7RKK9_sl2l-4RYIX0A
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:23:33.237298
---

# Lockpick2.0

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cSZq3JiaYf9PS0lufRqk77j6dOoWj19A8nW3Gom1SNTvicuhPjPuwdbWMY2250dwFficfWsIprhVwlwQD0EIrcJTg/0?wx_fmt=jpeg)

# Lockpick2.0

原创

漫路修行

微痕鉴远

![]()

在小说阅读器中沉浸阅读

We've been hit by Ransomware again, but this time the threat actor seems to have upped their skillset. Once again a they've managed to encrypt a large set of our files. It is our policy NOT to negotiate with criminals. Please recover the files they have encrypted - we have no other option! Unfortunately our CEO is on a no-tech retreat and so can't be reached.

In this Sherlock, you confront another serious ransomware threat at Forela: another significant number of UNIX servers have been infected by a suspected ransomware. Forela has decided not to negotiate with the attackers, putting the onus on the you to recover the encrypted files. This task demands players to utilize their understanding of ransomware operations, UNIX server structures, and digital forensics to restore the affected files. It's another high-pressure race against time, testing the your resilience, ingenuity, and technical prowess.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9PS0lufRqk77j6dOoWj19A8pViciblOFLxvNSFYFpszPqGhSQ76ECvsT2rovlo6UySDhYa0ibzic3FaIQ/640?wx_fmt=png&from=appmsg)

What was used to pack the malware?

upx

What type of encryption has been utilised to encrypt the files provided?

解包之后翻一翻函数就能看出来。

AES

What is the BTC wallet address the TA is asking for payment to?

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdI6HUsia6Q99vgbYickGvFFR1Fuj9ywJ72aWBusF9lOur9V25ibCYubF6g/640?wx_fmt=png&from=appmsg)

How much is the TA asking for?

要一百万英镑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdEWmUZFXS9Ly9aWIKkPlcSgOsrBhcWrNia2rg1iaWYvE0vlUCgOibGfwSg/640?wx_fmt=png&from=appmsg)

剩下的问题都是需要分析和解密才能回答的，接下来进入分析环节：分析AES加密逻辑。

追踪加密逻辑，先定位到encrypt\_file：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdgVaqUuDUriadN8dz2d3UxEYBdLxKEOfoCSbbFywrPfO6bZPeAIwAQtg/640?wx_fmt=png&from=appmsg)

这个函数为handle\_directory函数所调用

handle\_directory->encrypt\_file

查看发现main中调用handle\_directory

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdSNqKzyGLOlTibZEIythXUDDT5ufqMQA14Qb2dnDcQLIvtxKXibBu5mRg/640?wx_fmt=png&from=appmsg)

其中有个参数v6 ，这个参数经过get\_key\_from\_url函数的处理：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdJDEplV74ZicTYaElTptoxJF7cCbUZnUenuYOpWxHSLwVoVneAJjwLfg/640?wx_fmt=png&from=appmsg)

get\_key\_from\_url函数，发现是使用curl库实现的，找一下url

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdDq1Hc6SqqcpDAia4PliaS72ibtrJ0yFJL77icPjUafK6vEprcMiaicbtzBcA/640?wx_fmt=png&from=appmsg)

xor\_chiper这个函数用来做字符串加密用，main中已经见过多次。来解密一下aClig字符串

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82Jdc8jjwnTvyB5utobKbT2kicPo9XJcpQaHMtEACibe3k7Q0fD3icvclBkaA/640?wx_fmt=png&from=appmsg)

解密字符串

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdWiavrqqq3PzHqicBpzibxd5gcK9akBwHWQVW3iclJvjLf0ppxH0gicucPNg/640?wx_fmt=png&from=appmsg)

得到url

访问下载得到一个名为updater的文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdCPQstueERE0JHE9OGqYicv4ib9NGSbbgNqkWl9uyoibic7D7g8JGQqjtiaQ/640?wx_fmt=png&from=appmsg)

根据 EVP\_EncryptInit\_ex 这个API的函数原型去找key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82Jd2NkiaxZ8oMqMowODc7aHNJZblhntxibAj7iaKDy0iazBDR3vYF2r5Lbic6w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82Jd0pRqlw3tzTMQJjnYodtsFeljRgA1vTNhtwbtM9FlZsaV7hAyiaANIkw/640?wx_fmt=png&from=appmsg)

看到长度是32位，是作为aes加密的key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdsoZsVa6r3XbZ6xHsRcIHhMtlPTwJkp7Vp6B530iaSRRCHWpGl7icXuUg/640?wx_fmt=png&from=appmsg)

那就取前面32位作为key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdSzlhz1P8NDlmB0P42shVxf83gAxkSq7IHpjWmBHxibxibwTWmZib0tY6A/640?wx_fmt=png&from=appmsg)

看到模式是cbc，那还需要找IV

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdY2JWibN3gia9ic0rDtRJRWep6Q5Jo0RVwPLtZIich4asgWeLWyOVlrwtcg/640?wx_fmt=png&from=appmsg)

IV在反编译的伪代码中并不直观：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdSCDtWmVGddicAOWZ0zZvQmJHIuZskMqBRtCQ79ibvFA07NenawDPTicvg/640?wx_fmt=png&from=appmsg)

顶多只能追踪到局部变量v7，v8，但v7，v8和src[32]局部变量在内存中其实是连续的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdlHr86EO4rvTcrZvuuQMdg7qagQNzfT3WTBHCGtwE2WYDJYfq2TF4DQ/640?wx_fmt=png&from=appmsg)

剩下的刚好16个bytes，可以作为IV，测试解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdxwTakxyxfWZyVt3cKoDiaShwpXUc4Zk5hbZ4icIXdMyC8gMia09SwHT0g/640?wx_fmt=png&from=appmsg)

还原两个文件。

What is the file name of the key utlised by the attacker?

updater

What is the file hash of the key utilised by the attacker?

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82Jdnq8vFW0b25lSMuibHeQNnbbeUXQKdZMLicqmfNWuicEWMfq9tjUQZcicFw/640?wx_fmt=png&from=appmsg)

Which market is our CEO planning on expanding into? (Please answer with the wording utilised in the PDF)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82Jd2QpHt3qM9TxDibwzvftdCI8sfaO8ic3RNKgXwQrWTZJwLKRXqGeBibIYg/640?wx_fmt=png&from=appmsg)

Please confirm the name of the bank our CEO would like to takeover?

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9Mt97ECMVsatAEJNMfl82JdxVPPldzeHgldBdcSGVNKMLZYEczFsptaoWLRxuSvibickFx9EQrvLyQg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9OiakFicRXS9aR9GCECbu4Z6vewLpRbydMLRZlHOaz1I2icK3ohbWCCJTSIBQaDj29a9c8fiayibhX4BEQ/0?wx_fmt=png)

微痕鉴远

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9OiakFicRXS9aR9GCECbu4Z6vewLpRbydMLRZlHOaz1I2icK3ohbWCCJTSIBQaDj29a9c8fiayibhX4BEQ/0?wx_fmt=png)

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