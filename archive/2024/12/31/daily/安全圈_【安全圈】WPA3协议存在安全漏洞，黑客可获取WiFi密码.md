---
title: 【安全圈】WPA3协议存在安全漏洞，黑客可获取WiFi密码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=3&sn=8a2de7555b1f2f62a08ba91e461c72ba&chksm=f36e7888c419f19e03066c42c1386cf46772d64aa9efbbe0f759e026ca142a7ccf31647ec3d6&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-31
fetch_date: 2025-10-06T19:41:47.440988
---

# 【安全圈】WPA3协议存在安全漏洞，黑客可获取WiFi密码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh3Zx3gialuSKrBLaasxkT7EM7LcuW1ibhUqBxoTCQ1vnJYpC5jl8bnPzxb3qn8nVaZZMGgWS1rORrA/0?wx_fmt=jpeg)

# 【安全圈】WPA3协议存在安全漏洞，黑客可获取WiFi密码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

研究人员成功结合中间人攻击（MITM）和社会工程学技术，绕过了Wi - Fi保护协议——WPA3 ，进而获取网络密码。此次研究由西印度大学的Kyle Chadee、Wayne Goodridge和Koffka Khan开展，这一研究揭示了最新无线安全标准存在的安全漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh3Zx3gialuSKrBLaasxkT7EsM7biayZFouh3dFwYWBnZ8z5EbPPeNUNpjOibguPuQeNpXc282S6Agcw/640?wx_fmt=jpeg&from=appmsg)

WPA3于2018年推出，其目的是弥补前身WPA2的缺陷，为Wi - Fi网络提供更强的安全性。其中，“对等同时认证”（SAE）协议是其关键功能之一，该协议旨在让密码能够抵御离线字典攻击。研究人员证实，可利用WPA3过渡模式中的弱点来达成目的，这种过渡模式允许与WPA2设备向后兼容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh3Zx3gialuSKrBLaasxkT7E9eweLN9UZFRRQXyOhibDVAJycDZsoVMGiaU6EbNYLQrcibPE1tbQ8zJZw/640?wx_fmt=jpeg&from=appmsg)

借助降级攻击，他们能够捕获部分WPA3交互信息，再结合社会工程技术恢复网络密码。

这种攻击方法主要包含三个步骤：

* 其一，运用降级攻击捕获交互信息；
* 其二，将用户从原始的WPA3网络中解除认证；
* 其三，创建带有强制门户的虚假账号接入点以获取密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh3Zx3gialuSKrBLaasxkT7EjRJhRFALibphWoaTaZIKX2tBOCtxq0K9NbF2hMKRXyQ9mbokZ6RibJYg/640?wx_fmt=jpeg&from=appmsg)

研究人员利用树莓派模拟WPA3接入点，并借助Airgeddon等开源工具创建恶意接入点。当不知情的用户尝试连接伪造网络时，就会被提示输入Wi - Fi密码，随后该密码会与捕获的交互信息进行验证。

这项研究引发了对WPA3安全性的担忧，特别是在其过渡模式下。研究发现，如果未实施保护管理，攻击就会成功，而很多用户可能并不清楚或者没有启用这一设置。有趣的是，研究人员还发现一些设备无法连接到WPA3网络，这与Wi - Fi联盟所说的与WPA2向后兼容的说法相互矛盾。

尽管这种攻击需要特定条件并且要有用户交互，但它展示了保护无线网络面临的持续挑战。研究人员强调了用户教育以及正确配置WPA3网络以降低此类风险的重要性。

网络安全专家呼吁进一步调查WPA3的漏洞，并开发额外的保护措施。随着Wi - Fi网络不断成为企业和个人的关键基础设施，确保其安全性至关重要。

这项研究的结果提醒我们，即便最先进的安全协议也可能受到技术漏洞与社会工程学巧妙组合的影响。随着WPA3的普及，用户和制造商都必须保持警惕，并实施最佳实践，从而保护无线网络免受潜在攻击。

参考来源：https://cybersecuritynews.com/researchers-bypass-wpa3-password/#google\_vignette

***END***

阅读推荐

[【安全圈】当加密货币不再加密！比特币迫在眉睫的威胁：量子黑客！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066994&idx=1&sn=85c83155adeab228eabfe5883b04e2df&scene=21#wechat_redirect)

[【安全圈】网安公司也中招！多家公司 Chrome 扩展被攻击对用户投毒](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066994&idx=2&sn=f52410b0ac0166d0bcefa544524a442e&scene=21#wechat_redirect)

[【安全圈】微软警告 Windows 11 安装介质错误将导致安全更新失败](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066994&idx=3&sn=89e9c1b57173a5732363258286d05d6f&scene=21#wechat_redirect)

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