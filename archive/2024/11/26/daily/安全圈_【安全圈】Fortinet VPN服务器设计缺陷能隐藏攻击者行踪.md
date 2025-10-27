---
title: 【安全圈】Fortinet VPN服务器设计缺陷能隐藏攻击者行踪
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=3&sn=383839a7010797557f1d931f08bba980&chksm=f36e7deac419f4fc94bbb26eedf237c8473fa5cc4389f090589a14aaef297d0334b75cabe253&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-26
fetch_date: 2025-10-06T19:20:41.632071
---

# 【安全圈】Fortinet VPN服务器设计缺陷能隐藏攻击者行踪

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1onmGQXCMYucl4PTjFia23sFSBE2sFibF9NvqLzia3PLhfELKF4esicGtYThEhSyHk2QWUYxEDYIaEQ/0?wx_fmt=jpeg)

# 【安全圈】Fortinet VPN服务器设计缺陷能隐藏攻击者行踪

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

FortiClient

据BleepingComputer消息，网络安全厂商Fortinet产品中的VPN 服务器存在一个设计漏洞，其日志记录机制能够隐藏成功实施暴力攻击的行为记录，无法让防御者察觉到系统可能已被入侵。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1onmGQXCMYucl4PTjFia23hNhNJJRRPw0mfpXOx1IYqibCjCRtibDiacaa8FWfPwcHuiaZicVZzIhUrYQ/640?wx_fmt=jpeg&from=appmsg)

FortiClient 终端防御软件的VPN 服务器使用两步过程存储登录活动，该过程包括身份验证和授权阶段。只有当该过程同时通过身份验证和授权步骤时，才会记录成功登录；否则会记录验证失败。

自动化安全验证解决方案公司 Pentera 的研究人员发现，通过一种设计，在验证阶段后停止整个登录过程，从而在不记录成功登录的情况下验证 VPN 凭证。

研究人员使用 Burp 应用程序安全测试工具来记录客户端和 VPN 服务器之间的交互，他们注意到，初始 HTTPS 请求的响应会显示有效凭证、验证失败或在连续多次尝试失败时显示 "发生错误 "的响应。如果该过程在身份验证阶段后停止，则 VPN 服务器仅记录失败的尝试，而不记录成功的尝试，因为它没有继续执行下一个授权步骤。

因此，防御者无法确定此类攻击中的暴力尝试是否成功，并且只能看到失败进程的日志。尤其是当攻击者成功验证凭证后，防御者将无法察觉这些恶意活动。

值得注意的是，即使威胁行为者确定了正确的登录设置并将其用于攻击，授权过程也只有在 FortiClient VPN 发送两个 API 调用以验证设备的安全合规性和用户的访问级别后才会完成。此验证使实施攻击变得复杂，但资源充足的攻击者仍然可以使用 Pentera 的研究方法成功入侵目标网络。

Pentera 与 Fortinet 分享了这项研究，但对方不认为该问题是个漏洞。目前尚不清楚 Fortinet 是否会解决这个问题。事后，Pentera 发布了一个脚本，能利用此设计缺陷来验证 Fortinet VPN 凭证。

参考来源：Fortinet VPN design flaw hides successful brute-force attacks

***END***

阅读推荐

[【安全圈】太空技术巨头 Maxar 证实攻击者获取了员工数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=1&sn=81e535202f431485c12dac88cf705ffe&chksm=f36e7ddbc419f4cdfa6b93222991880723ead5b1224f5aea3c430d89ee2ad3f9ea5556553fc9&scene=21#wechat_redirect)

[【安全圈】微软公司推出 “Windows 恢复能力计划”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=2&sn=6d88527a3838dd59d8bbccb332540518&chksm=f36e7ddbc419f4cd51a855d822237f84592f66ad951174261234f7641e5c6bb1e6cd2cfcacca&scene=21#wechat_redirect)

[【安全圈】苹果解决了两个被积极利用的零日漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=3&sn=98b7c0046c725ff8299a89a706c8ee43&chksm=f36e7ddbc419f4cdfd1a5b1325eeaa6a76fad3e86c3a04d39a3c93255a412bb3e8ee77745d9d&scene=21#wechat_redirect)

[【安全圈】微软已通过更新修复Windows 10安装商店应用时出现发生错误无法安装问题](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=4&sn=fa5c5885a0aa428e589410762dd813ac&chksm=f36e7ddbc419f4cdd12380c085a00117007aeacb6e8ac0816c71f80f4a0aa82a15a7f149aff5&scene=21#wechat_redirect)

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