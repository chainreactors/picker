---
title: 【安全圈】僵尸网络利用漏洞攻击网络录像机及TP-Link路由器
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066932&idx=4&sn=90071983b67d793ccd950d077faa76c0&chksm=f36e7834c419f1223f8c86ab18042512d1d737aaf42f177639389bb325faac193f7b9b9612a4&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-26
fetch_date: 2025-10-06T19:39:17.834194
---

# 【安全圈】僵尸网络利用漏洞攻击网络录像机及TP-Link路由器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLiaMBPg3icS9woo1QQEdrZHyibZ9oibRNHU1f3cx7UBqlo2bLjF3hncWTZVg/0?wx_fmt=jpeg)

# 【安全圈】僵尸网络利用漏洞攻击网络录像机及TP-Link路由器

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据BleepingComputer消息，一个基于Mirai的新型僵尸网络正在积极利用DigiEver网络录像机中的一个远程代码执行漏洞，该漏洞尚未获得编号，也暂无修复补丁。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLiag1vTX8CtucI9ryepcgd9sN3ldAD4RIZccBfNZwtr3Ya8gGzg6R879Q/640?wx_fmt=jpeg&from=appmsg)

Akamai 研究人员观察到，该僵尸网络于 11 月中旬开始利用该漏洞，但证据表明该活动至少自 9 月以来就一直活跃。

除了 DigiEver 漏洞外，新的 Mirai 恶意软件变体还分别利用CVE-2023-1389和 CVE-2018-17532 漏洞针对未打安全补丁的 TP-Link 和 Teltonika RUT9XX 路由器。

研究人员称，被用来攻击 DigiEver NVR 的远程代码执行 （RCE） 漏洞源自“/cgi-bin/cgi\_main. cgi”URI，该URI 未正确验证用户输入，允许未经身份验证的远程攻击者通过某些参数（如 HTTP POST 请求中的 ntp 字段）注入 "curl "和 "chmod "等命令。

通过命令注入，攻击者从外部服务器获取恶意软件二进制文件，并将设备加入其僵尸网络。设备一旦被入侵，就会被用来进行分布式拒绝服务（DDoS）攻击，或利用漏洞集和凭证列表扩散到其他设备。

Akamai表示，新Mirai变种的显著特点是使用了XOR和ChaCha20加密技术，并以x86、ARM和MIPS等多种系统架构为目标，这不同于许多基于 Mirai 的僵尸网络仍然依赖于原始的字符串混淆逻辑，这种逻辑来自于原始 Mirai 恶意软件源代码发布时包含的回收代码。虽然采用复杂的解密方法并不新颖，但这表明基于Mirai的僵尸网络的战术、技术和程序在不断发展。

据悉，早在去年罗马尼亚布加勒斯特举行的 DefCamp 安全会议上，TXOne 研究员 Ta-Lun Yen就曾揭露过该漏洞，该问题当时影响了多个 DVR 设备。

参考来源：New botnet exploits vulnerabilities in NVRs, TP-Link routers

***END***

阅读推荐

[【安全圈】盘点" 崩溃 " 的 2024](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066903&idx=1&sn=36c25e0bcd6b736bef1f2732300088c5&scene=21#wechat_redirect)

[【安全圈】突发！GitLab将停止对中国区用户提供GitLab.com账号服务](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066903&idx=2&sn=864191a625f27c17468da3dfdff3f8f7&scene=21#wechat_redirect)

[【安全圈】日本弹幕网站 NicoNico 向黑客支付 298 万美元勒索赎金](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066903&idx=3&sn=8e77e867c5725aad13410bfad8f64f09&scene=21#wechat_redirect)

[【安全圈】腾讯与跨境汇款平台Ria达成合作 用户可通过Ria将款项汇至微信支付或绑定的银行卡](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066835&idx=2&sn=fde78ad37031b6df96ec87167929947c&scene=21#wechat_redirect)

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