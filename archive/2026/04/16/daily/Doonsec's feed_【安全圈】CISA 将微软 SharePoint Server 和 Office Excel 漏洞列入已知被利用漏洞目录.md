---
title: 【安全圈】CISA 将微软 SharePoint Server 和 Office Excel 漏洞列入已知被利用漏洞目录
url: https://mp.weixin.qq.com/s/iZG6Ld-xjuEE30o3lTuJfg
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:59.715847
---

# 【安全圈】CISA 将微软 SharePoint Server 和 Office Excel 漏洞列入已知被利用漏洞目录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyG5XIqOzZM9BJMHZsbEtfy4aWiaT5deCxfhJlIqicWtprpibHU0du9HZzicUW7olbHWAc0zSUQvnKMQxwaiasHve9HYTu7eiabCet1Qc/0?wx_fmt=jpeg)

# 【安全圈】CISA 将微软 SharePoint Server 和 Office Excel 漏洞列入已知被利用漏洞目录

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

美国网络安全和基础设施安全局（CISA）还将苹果、Laravel Livewire 和 Craft CMS 的漏洞列入了其已知被利用漏洞（KEV）目录。

以下是新列入该目录的漏洞：

* CVE - 2009 - 0238：微软 Office 远程代码执行漏洞
* CVE - 2026 - 32201：微软 SharePoint Server 输入验证不当漏洞

第一个被列入的漏洞，编号为 **CVE - 2009 - 0238**（CVSS 评分为 9.3），影响多个版本的微软 Excel 及相关查看器。当用户打开一个特制的 Excel 文件，导致应用程序访问内存中的无效对象时，就会触发该漏洞。这会导致内存损坏，使远程攻击者能够以用户权限在受影响的系统上执行任意代码。该漏洞在 2009 年 2 月曾在野外被积极利用，特别是被 Trojan.Mdropper.AC 恶意软件利用，在当时是一个重大的现实威胁。

第二个被列入目录的漏洞，编号为 **CVE - 2026 - 32201**，是一个关键的 SharePoint 零日漏洞，据微软报告，该漏洞已在野外攻击中被利用。CVE - 2026 - 32201（CVSS 评分为 6.5）是微软 SharePoint Server 中的一个欺骗漏洞，可能与跨站脚本攻击（XSS）相关。虽然细节有限，但它可能允许攻击者查看或修改公开信息。微软尚未透露该漏洞被利用的广泛程度，但鉴于其潜在影响，各机构，尤其是那些拥有面向互联网的 SharePoint 服务器的机构，应优先测试并尽快应用补丁。

公告中写道：“微软 Office SharePoint 中的输入验证不当，允许未经授权的攻击者通过网络进行欺骗攻击”。“成功利用该漏洞的攻击者可以查看一些敏感信息（机密性），修改公开信息（完整性），但无法限制对资源的访问（可用性）。已检测到利用行为”。

根据《约束性操作指令（BOD）22 - 01：降低已知被利用漏洞的重大风险》，美国联邦民事行政部门（FCEB）机构必须在截止日期前解决已识别的漏洞，以保护其网络免受利用该目录中漏洞的攻击。专家还建议私营企业查看该目录，并解决其基础设施中的相关漏洞。

CISA 命令联邦机构在 2026 年 4 月 28 日前修复这些漏洞。

***END***

阅读推荐

[【安全圈】伊朗大量美制通信设备突然"失灵"](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075710&idx=1&sn=7f598c08c68d27461c854f8d3e905ff6&scene=21#wechat_redirect)

[【安全圈】苹果官方紧急提醒！iPhone用户立即更新系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075710&idx=2&sn=8bdb32668e0b1c00bb4c72c6fd322b4a&scene=21#wechat_redirect)

[【安全圈】全球最大零工平台Fiverr被曝数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075710&idx=3&sn=ca39bc8690f6cdb14f2e73f6d4c9749c&scene=21#wechat_redirect)

[【安全圈】Adobe 修复 PDF 阅读器零日漏洞，已被黑客利用至少四个月](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075679&idx=1&sn=6c0e8d061d29da3af35a3914330ee403&scene=21#wechat_redirect)

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