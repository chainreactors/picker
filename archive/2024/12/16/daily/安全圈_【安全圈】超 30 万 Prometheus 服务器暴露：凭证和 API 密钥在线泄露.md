---
title: 【安全圈】超 30 万 Prometheus 服务器暴露：凭证和 API 密钥在线泄露
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=3&sn=e357cb32259162fcaa4e589951d9e4ea&chksm=f36e7f7ac419f66c8c355db59f14018402fb0a3cec7403d17da621251c17d96fb69baabea25f&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-16
fetch_date: 2025-10-06T19:36:50.314571
---

# 【安全圈】超 30 万 Prometheus 服务器暴露：凭证和 API 密钥在线泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgqspEEmN9EWkxjibHiaErqprmED6Pu1QIbKvSEzBHpWehD026Dx1XhzvUlX3RiaQKIxVb31xuMUiaKCA/0?wx_fmt=jpeg)

# 【安全圈】超 30 万 Prometheus 服务器暴露：凭证和 API 密钥在线泄露

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Prometheus

网络安全研究人员警告称，数千台托管Prometheus监控和告警工具包的服务器面临信息泄露以及拒绝服务（DoS）和远程代码执行（RCE）攻击的风险。

“Prometheus服务器或导出器常常缺乏适当的身份验证，允许攻击者轻松收集敏感信息，如凭证和API密钥，”Aqua安全研究人员Yakir Kadkoda和Assaf Morag在一份新报告中对The Hacker News表示。

这家云安全公司还表示，用于确定堆内存使用、CPU使用等的“/debug/pprof”端点的暴露，可能成为DoS攻击的向量，使服务器无法操作。

据估计，多达296,000个Prometheus Node Exporter实例和40,300个Prometheus服务器可以通过互联网公开访问，这使得它们成为一个巨大的攻击面，可能危及数据和服务。

通过互联网暴露的Prometheus服务器泄露敏感信息，如凭证、密码、认证令牌和API密钥，这一点之前已被JFrog在2021年和Sysdig在2022年记录。

“未经认证的Prometheus服务器允许直接查询内部数据，可能暴露攻击者可以利用的秘密，以在各种组织中获得初步立足点，”研究人员说。

此外，发现“/metrics”端点不仅可以揭示内部API端点，还可以揭示子域、Docker注册表和镜像的数据——这些都是攻击者进行侦察并寻求在网络内扩大影响力的宝贵信息。

这还不是全部。对手可以向“/debug/pprof/heap”等端点发送多个同时请求，以触发CPU和内存密集型的堆剖析任务，这些任务可以压垮服务器并导致它们崩溃。

Aqua进一步指出了供应链威胁，涉及使用repojacking技术利用与已删除或重命名的GitHub仓库相关联的名称，并引入恶意第三方导出器。

具体来说，它发现Prometheus官方文档中列出的八个导出器容易受到RepoJacking攻击，从而允许攻击者重新创建具有相同名称的导出器，并托管一个恶意版本。截至2024年9月，这些问题已由Prometheus安全团队解决。

“用户如果按照文档操作，可能会无意中克隆并部署这个恶意导出器，导致他们的系统上执行远程代码，”研究人员说。

建议组织使用适当的身份验证方法保护Prometheus服务器和导出器，限制公开暴露，监控“/debug/pprof”端点是否有任何异常活动的迹象，并采取措施避免RepoJacking攻击。

***END***

阅读推荐

[【安全圈】国内最大 IT 社区 CSDN 被挂马传播病毒！CDN 或被攻击成罪魁祸首](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066606&idx=1&sn=308e9637fcb9741e87940b691f20e9aa&scene=21#wechat_redirect)

[【安全圈】高中肄业的网络高手图一己私利，编写程序卖个人信息！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066606&idx=2&sn=0b819bf38f3cc2d19225010f632def89&scene=21#wechat_redirect)

[【安全圈】最新网络钓鱼活动利用损坏的 Word 文档来规避检测](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066606&idx=3&sn=d6db5800165d61a841b21b917d975bde&scene=21#wechat_redirect)

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