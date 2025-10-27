---
title: 【安全圈】施乐打印机漏洞危及数据防线，Versalink C7025 用户凭证面临窃取风险
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067894&idx=3&sn=b32c1ab569fca6e572624325f39c97ba&chksm=f36e7476c419fd60d6c90e1fe3b4a358f007fcdae3939c304c0695cbdcda2a5adc7d383310c4&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-20
fetch_date: 2025-10-06T20:35:54.324541
---

# 【安全圈】施乐打印机漏洞危及数据防线，Versalink C7025 用户凭证面临窃取风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic6ZwIkYhbCu5udzjRibTX20FQBvxFSeVpiaYUTztY7sUaQ9yAcCuia6GM7g/0?wx_fmt=jpeg)

# 【安全圈】施乐打印机漏洞危及数据防线，Versalink C7025 用户凭证面临窃取风险

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![CVE-2024-12510 and CVE-2024-12511](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic6suet2VX4Lr3TPEQaeiczm58awyXXXwGgWia5lciccDMjUHraq3lXAejfg/640?wx_fmt=other&from=appmsg)Rapid7 公司的研究人员发现，施乐（Xerox）Versalink C7025 多功能打印机存在漏洞，攻击者可能利用这些漏洞窃取用户凭证。这些漏洞被认定为 CVE-2024-12510 和 CVE-2024-12511，可导致一种被称为 “回传攻击” 的情况，即打印机被诱骗将身份验证数据发送给攻击者。

施乐 Versalink C7025 是一款广受欢迎的企业级打印机，具备打印、复印、扫描、传真和电子邮件功能。受这些漏洞影响的是运行固件版本 57.69.91 及更早版本的设备。

Rapid7 的报告解释道：“这种回传式攻击利用了一个漏洞，使恶意行为者能够更改多功能打印机（MFP）的配置，并导致 MFP 设备将身份验证凭证发送给恶意行为者。”

攻击者可以利用这些漏洞获取诸如轻量级目录访问协议（LDAP）、服务器消息块协议（SMB）和文件传输协议（FTP）等服务的凭证。这可能使他们得以访问敏感信息，甚至在组织的网络内横向移动，进而攻陷其他系统。

攻击者需要获得打印机的管理员账户权限，或者能够对打印机控制台进行物理访问。然后，他们可以修改打印机的配置，将身份验证请求重定向到他们控制的服务器上。当用户尝试通过 LDAP 或 SMB 等服务进行身份验证时，打印机在不知情的情况下会将用户的凭证发送到攻击者的服务器上。

施乐公司已经发布了固件更新来修复这些漏洞。强烈建议使用受影响的 Versalink 打印机的机构尽快升级到最新的已打补丁的版本。

作为临时缓解措施，Rapid7 建议为管理员账户设置复杂密码，并避免在 LDAP 和 SMB 等服务中使用具有提升权限的 Windows 身份验证账户。同时，也建议为未经验证的用户禁用远程控制控制台。

***END***

阅读推荐

[【安全圈】短视频平台“封号圈”乱象猖獗，IP查询如何助力防范](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=1&sn=77b78d28e626bb57cf51f82d0c472aa6&scene=21#wechat_redirect)

[【安全圈】俄罗斯黑客利用 7-Zip 零日漏洞攻击乌克兰](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=2&sn=634853ba2d9852cc240a7d5d46ce82c5&scene=21#wechat_redirect)

[【安全圈】微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=3&sn=b875bcdbb815582bbc7966d6ebc3a164&scene=21#wechat_redirect)

[【安全圈】马斯克与 OpenAI 的交锋：收购提案遇冷，立场分歧引争议](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=4&sn=38c4e0921e00478f77d52173d75865fa&scene=21#wechat_redirect)

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