---
title: 【安全圈】俄罗斯黑客利用 7-Zip 零日漏洞攻击乌克兰
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=2&sn=634853ba2d9852cc240a7d5d46ce82c5&chksm=f36e7462c419fd74d29690ade86cd94c8f1353765e594a85d6f64779b2262b4aad515e3ff40c&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-19
fetch_date: 2025-10-06T20:47:36.064733
---

# 【安全圈】俄罗斯黑客利用 7-Zip 零日漏洞攻击乌克兰

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhgoXt2hbpqmqppK1kkAMhYX0K5Sh2Nx41eUeVodiaOgv71hJWWvsaMtr8UWFwNGKjA8vbhDaB5k2Q/0?wx_fmt=jpeg)

# 【安全圈】俄罗斯黑客利用 7-Zip 零日漏洞攻击乌克兰

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![俄罗斯黑客](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhgoXt2hbpqmqppK1kkAMhYj3icphZFasKDiaG7FqPYuY3AsjRuqlNOJSWueybic6KPGJy90fabwD0gw/640?wx_fmt=jpeg&from=appmsg)

据趋势科技报道，俄罗斯威胁组织利用 7-Zip 归档工具中的零日漏洞对乌克兰政府实体开展了网络间谍活动。

该漏洞编号为 CVE-2025-0411（CVSS 评分为 7.0），于 2024 年 9 月被发现，并于两个月后在 7-Zip 版本 24.09 中得到修补。

该漏洞被描述为对 Web 标记 (MoTW) 保护机制的绕过，该机制在 Windows 中引入，用于标记从不受信任来源下载的文件，以防止其自动执行并警告用户潜在风险。

7-Zip 于 2022 年 6 月引入了对 MoTW 的支持，但该工具并未将 MoTW 传播到从存档中提取的文件中。这允许攻击者对恶意文件进行双重存档，如果用户被说服提取并打开这些文件，这些文件将绕过保护机制。

零日计划公告指出： “攻击者可以利用此漏洞在当前用户的上下文中执行任意代码。”

现在，趋势科技透露，CVE-2025-0411 已被利用，在针对乌克兰政府实体和该国其他组织的 SmokeLoader 活动中，可能是为了进行网络间谍活动。

此次攻击据信是由未具名的俄罗斯网络犯罪集团精心策划的，攻击者利用被感染的电子邮件账户，使用同形文字攻击技术，发送利用零日漏洞制作的档案。

趋势科技发现，电子邮件来自受感染的乌克兰管理机构和商业账户，例如乌克兰司法部下属的国家行政服务局 (SES)。其中一些账户可能在之前的攻击活动中受到感染。

该网络安全公司还发现，该活动中使用的一个内部档案依靠同形文字攻击来欺骗 Word 文件 (.doc)，并诱骗目标受害者打开档案并执行其中的恶意文件。

“通过使用西里尔字符‘Es’，攻击者设计了一个模仿 .doc 文件的内部存档。这一策略有效地误导用户无意中触发 CVE-2025-0411 漏洞，导致存档内容在没有 MoTW 保护的情况下被发布，”趋势科技解释道。

此次活动的目标乌克兰实体可能包括 SES、扎波罗热汽车制造厂 (PrJSC ZAZ)、Kyivpastrans 和 Kyivvodokanal（基辅公共交通和供水服务）、SEA（电气和电子设备及电器制造商）、Verkhovyna 区国家行政机构、VUSA（保险组织）、第聂伯罗市区域药店和 Zalishchyky 市议会。

趋势科技指出：“请注意，受 CVE-2024-0411 零日攻击影响的组织的汇编并不全面；很有可能其他组织也受到了攻击或成为攻击目标。”

该网络安全公司表示，攻击者主要针对较小的当地政府机构，可能是因为它们往往缺乏必要的资源和知识来保持保护，并且因为它们可以被用作进入较大政府组织的支点。

来源：https://www.securityweek.com/russian-hackers-exploited-7-zip-zero-day-against-ukraine/

***END***

阅读推荐

[【安全圈】仿冒DeepSeek的手机木马病毒被捕获！相关部门提示](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=1&sn=00cebc4413ae6b74430262bd93033252&scene=21#wechat_redirect)

[【安全圈】航空公司客服倒卖艺人航班信息，被判刑！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=2&sn=49a6b4aa641e56248143edcac248d76d&scene=21#wechat_redirect)

[【安全圈】Steam 平台上的 PirateFi 游戏被发现安装了密码窃取恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067859&idx=3&sn=22a5fdac878492e3eb605cf3133cb536&scene=21#wechat_redirect)

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