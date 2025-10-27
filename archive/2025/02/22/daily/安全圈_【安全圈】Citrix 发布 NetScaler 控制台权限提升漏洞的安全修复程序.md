---
title: 【安全圈】Citrix 发布 NetScaler 控制台权限提升漏洞的安全修复程序
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067926&idx=4&sn=0caef5e797b3df5141d039002092ba83&chksm=f36e7416c419fd00723e1f3194bd59381a229e4856a99f755ce8b3534ef54f025b33b154a77d&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-22
fetch_date: 2025-10-06T20:37:34.863352
---

# 【安全圈】Citrix 发布 NetScaler 控制台权限提升漏洞的安全修复程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgoGN68urjja0Qn4If7Y9vCZv51mjkEc6wV1Bo67qVvK5QBDd5LqfACBAVTcV5E7Xic9fmRBPkn4XA/0?wx_fmt=jpeg)

# 【安全圈】Citrix 发布 NetScaler 控制台权限提升漏洞的安全修复程序

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![权限提升漏洞](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgoGN68urjja0Qn4If7Y9vCU699r7mfY9KzIfm0KShxH1mNdKtZibIQPzScZaHJnUvlcoHaZTOcHgQ/640?wx_fmt=other&from=appmsg "权限提升漏洞")Citrix 发布了针对影响 NetScaler 控制台（以前称为 NetScaler ADM）和 NetScaler 代理的高严重性安全漏洞的安全更新，该漏洞可能在某些条件下导致权限提升。

该漏洞的编号为CVE-2024-12284，CVSS v4 评分为 8.8（满分 10.0）。

它被描述为权限管理不当的案例，如果部署了 NetScaler 控制台代理，则可能导致经过身份验证的权限提升，并允许攻击者执行后续操作。

Netscaler指出：“该问题是由于权限管理不充分而引起的，经过身份验证的恶意行为者可以利用该问题在未经额外授权的情况下执行命令。”

“但是，只有具有 NetScaler 控制台访问权限的经过身份验证的用户才能利用此漏洞，从而将威胁面限制在经过身份验证的用户身上。”

此缺陷影响以下版本 ：

* NetScaler Console 14.1 14.1-38.53 之前版本
* 13.1-56.18 之前的 NetScaler 控制台 13.1
* 14.1-38.53 之前的 NetScaler Agent 14.1
* 13.1-56.18 之前的 NetScaler Agent 13.1

该问题已在以下软件版本中得到修复 ：

* NetScaler 控制台 14.1-38.53 及更高版本
* NetScaler 控制台 13.1-56.18 及更高版本 13.1
* NetScaler Agent 14.1-38.53 及更高版本
* NetScaler Agent 13.1-56.18 及更高版本 13.1

该公司表示：“云软件集团强烈建议 NetScaler Console 和 NetScaler Agent 的客户尽快安装相关更新版本”，并补充说目前没有办法解决该漏洞。

也就是说，使用 Citrix 管理的 NetScaler 控制台服务的客户无需采取任何行动。

来源：https://thehackernews.com/2025/02/citrix-releases-security-fix-for.html

***END***

阅读推荐

[【安全圈】国家网信办依法集中查处一批侵害个人信息权益的违法违规App](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=1&sn=7e609708df11dd4fd5db116fdd3991fb&scene=21#wechat_redirect)

[【安全圈】与俄罗斯有关的威胁行为者利用 Signal 的“链接设备”功能劫持账户](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=2&sn=2bff61f8a1dd9ad950eef1a27e02540e&scene=21#wechat_redirect)

[【安全圈】Sophos 斥资 8.59 亿美元成功收购 Secureworks](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=3&sn=6a03d738e3a7cb11f91482d431d77f9e&scene=21#wechat_redirect)

[【安全圈】Windows磁盘清理工具漏洞被利用获取系统权限，PoC已公开（CVE-2025-21420）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=4&sn=dc16ae2f429d6a98d49cbc1c5cc21999&scene=21#wechat_redirect)

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