---
title: 【安全圈】D-Link忽视旧款VPN路由器补丁更新，关键漏洞未修复
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066187&idx=4&sn=c4be9926d771d2293619bbe2dcc12b29&chksm=f36e7dcbc419f4ddb491db67e4fc6ec1515f6d7f688561be3515419ed7095a39ba6fc3b91bf9&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-24
fetch_date: 2025-10-06T19:15:30.799769
---

# 【安全圈】D-Link忽视旧款VPN路由器补丁更新，关键漏洞未修复

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliabPJFLzw0e3nD6AjIjP1g7RWorwffcsHpdicjBBAt4qDBmfLXtK139VSSV37eNqzuxiabG9rurZhpw/0?wx_fmt=jpeg)

# 【安全圈】D-Link忽视旧款VPN路由器补丁更新，关键漏洞未修复

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

在发现严重的远程代码执行 (RCE) 漏洞后，D-Link 强烈建议其旧款 VPN 路由器用户更换设备。由于这些型号的路由器已达到其使用寿命和终止支持的日期，因此不会再对其打补丁以防范该漏洞。

安全研究人员"delsploit"向D-Link报告了该漏洞，但尚未分配CVE标识符。该漏洞的技术细节也未披露，因此客户有时间在网络犯罪分子开始尝试利用该漏洞之前做出反应。我们知道这是一个堆栈缓冲区溢出漏洞，允许未经认证的用户执行远程代码执行。

以下设备的所有硬件版本和固件版本都受到了影响：

* DSR-150 （2024 年 5 月到期）
* DSR-150N（2024 年 5 月到期）
* DSR-250（2024 年 5 月退出市场）
* DSR-250N（2024 年 5 月退出市场）
* DSR-500N（2015 年 9 月退出市场）
* DSR-1000N（2015 年 10 月停用）

D-Link 强调，它将不会为四个受影响的型号发布补丁，因为它们都已达到 EOL 或 EOS 状态，也就是产品处于结束支持的期限之后，其中大多数是在 2024 年 5 月，还有几个是在 2015 年。该公司写道，公司的一般政策是，当产品达到 EOS/EOL 时，将不再对其提供支持，并且停止对这些产品的所有固件开发。

D-Link 强烈建议这些路由器的所有者升级到较新的型号，因为继续使用可能会对与其连接的设备造成危险。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliabPJFLzw0e3nD6AjIjP1g7qaLDSjjsRRuicAmfr6sxL30Jv9EcPrzsuHpJFn71o6oibQxm0bSM8cbg/640?wx_fmt=jpeg&from=appmsg)

D-Link DSR 150 路由器

该公司正试图安抚那些可能对此感到恼火的用户，为不受漏洞影响的新服务路由器（DSR-250v2）提供 20% 的折扣。

D-Link 还指出，虽然第三方开放固件可用于许多受影响的设备，但使用这些固件会导致保修失效，设备所有者应自行承担责任。

这是 D-Link 在一个月内第二次确认不会为已达到报废/服务终止状态的高危设备打补丁。这家台湾公司建议其已停产的 NAS 设备的所有者升级到较新的型号，因为这些设备不会打补丁以防止关键命令注入漏洞。

2022 年，网络安全& 基础设施安全局（CISA）建议消费者更换存在 RCE 漏洞的 D-Link 路由器，因为这些设备已达到使用寿命，将不再收到补丁。

***END***

阅读推荐

[【安全圈】AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066127&idx=1&sn=54cc25bc1157b1fcde3352264a6e6737&chksm=f36e7d0fc419f419eba06e5a96d15df8e4c6984457ffe2caa95bdb960aa38174100f2f438f01&scene=21#wechat_redirect)

[【安全圈】全球175国和地区面临风险：14.5万个工控系统暴露于互联网中](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066127&idx=2&sn=dd1d3315135df42f2ea52b1674729329&chksm=f36e7d0fc419f4192a5775c039991fdc86f879e8aea0eff72fc8e6eca0bbba94596cd83ce603&scene=21#wechat_redirect)

[【安全圈】CISA红队发现惊人的关键基础设施风险](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066127&idx=3&sn=3f367e65a291df4dd3e563a38a83b973&chksm=f36e7d0fc419f41913bc610f4a13cbd59bba300672bf8878380204ffc70703bb263e153edcc0&scene=21#wechat_redirect)

[【安全圈】麻省理工发布2024年最危险的漏洞TOP 25](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066127&idx=4&sn=1c50f0f483942910d6d8ae2633bccc0b&chksm=f36e7d0fc419f41947fb8dfdbb8302260500102916778a3058e716cddad6866b03c80673964d&scene=21#wechat_redirect)

[【安全圈】Ubuntu系统软件中的5个漏洞潜藏了10年才被发现](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=1&sn=00fc32fb2126236a289beba3ec9b7b29&chksm=f36e7d00c419f41616a3b529fd231f5c9cb584fc1c962df2286ebe434d3081d23b39cd91ade2&scene=21#wechat_redirect)

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