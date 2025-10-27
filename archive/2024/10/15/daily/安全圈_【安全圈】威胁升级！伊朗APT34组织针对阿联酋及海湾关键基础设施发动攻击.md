---
title: 【安全圈】威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065207&idx=2&sn=5d2a6ee8cad3c1a93fd0258350d9c10e&chksm=f36e61f7c419e8e16198b5842f83c4e50a87fc6d753fd51721b9b6f94fe5110bdf922327062e&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-15
fetch_date: 2025-10-06T18:52:16.452197
---

# 【安全圈】威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQJhznx3HQrRtdeAtYiaNWGNfpmtKUTOGyxgpID7dOGoUVNnniaJ35soiaA/0?wx_fmt=jpeg)

# 【安全圈】威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQl6P9CYibZKkVPzMwKOxMhrPOADqYv3tz0t7pMr5Vnic3Se9d0OsLt9rw/640?wx_fmt=jpeg&from=appmsg)

伊朗国家支持的黑客组织 APT34（又名 OilRig）最近升级了其活动，针对阿拉伯联合酋长国和海湾地区的政府和关键基础设施实体发起了新的攻击。

在趋势科技研究人员发现的这些攻击中，OilRig 部署了一个新的后门，以微软 Exchange 服务器为目标窃取凭证，还利用 Windows CVE-2024-30088 漏洞提升了他们在受攻击设备上的权限。

除了这些活动，趋势科技还发现 OilRig 与另一个参与勒索软件攻击的伊朗 APT 组织 FOX Kitten 之间存在联系。

## 最新的 OilRig 攻击链

趋势科技表示，这种攻击首先会利用有漏洞的 Web 服务器上传 Web shell，使攻击者能够执行远程代码和 PowerShell 命令。

一旦 Web shell 处于活动状态，OilRig 就会利用它部署其他工具，包括一个旨在利用 Windows CVE-2024-30088 漏洞的组件。

CVE-2024-30088 是微软在 2024 年 6 月修复的一个高严重性权限升级漏洞，它使攻击者能够将权限升级到 SYSTEM 级别，从而对被入侵设备拥有重大控制权。

微软已承认存在 CVE-2024-30088 的概念验证漏洞，但尚未在其安全门户网站上将该漏洞标记为主动漏洞。CISA 也没有在 ts Known Exploited Vulnerability 目录中报告该漏洞曾被利用。

随后，OilRig 注册了一个密码过滤 DLL，以在密码更改事件中拦截明文凭证，然后下载并安装远程监控和管理工具 “ngrok”，用于通过安全隧道进行隐蔽通信。

威胁行为者的另一种新策略是利用内部 Microsoft Exchange 服务器，通过难以察觉的合法电子邮件流量窃取凭证和外流敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQAQzzohU6lXIiaoS3AGBWEHEe5Hs0BnZLI0KNQbtUZdCjkQ9ytBzpKxw/640?wx_fmt=jpeg&from=appmsg)

从 Exchange 窃取密码的后门，来源：趋势科技

名为 “StealHook ”的新型后门为密码外泄提供了便利，而趋势科技称，政府基础设施通常被用作支点，使这一过程看起来合法。

对此，趋势科技在报告中解释称这一阶段的关键目标是捕获窃取的密码，并将其作为电子邮件附件传输给攻击者。

此外，我们还观察到，威胁行为者利用带有被盗密码的合法账户，通过政府 Exchange 服务器路由这些电子邮件"。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQCAFccwGUYfK9mKibyVWBvxMvOZsibYMfINGZiaNDT8RtCdqoLkPUApdgw/640?wx_fmt=jpeg&from=appmsg)

石油钻机的最新攻击链，来源：趋势科技

趋势科技称，StealHook与OilRig在过去的活动中使用的后门（如Karkoff）之间存在代码相似性，因此最新的恶意软件似乎是一种进化，而不是从头开始的新创造。

这也并非 OilRig 首次使用微软 Exchange 服务器作为其攻击的活动组件。将近一年前，赛门铁克曾报告称，APT34 在内部部署的 Exchange 服务器上安装了一个名为 “PowerExchange ”的 PowerShell 后门，能够通过电子邮件接收和执行命令。

该威胁行为体在中东地区仍然非常活跃，它与 FOX Kitten 的关系目前还不清楚，但令人担忧的是，它有可能将勒索软件添加到其攻击武器库中。

据趋势科技称，由于大多数目标实体都在能源领域，因此这些组织一旦运营中断那么将影响十分广泛。

参考来源：Iranian hackers now exploit Windows flaw to elevate privileges (bleepingcomputer.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQyYkxqal233XMKoSdD5QRf49C2VMouZ5xh5Eb9vWP0v1YbZCZbH4Xpg/640?wx_fmt=jpeg)[【安全圈】](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=2&sn=38505d2516cdbe4a948e32101cbbebf5&chksm=f36e61e6c419e8f0e3861875cb5395af2defdb95e309b40b053c850d37a6e094e918bc6e63c9&scene=21#wechat_redirect)广东省教育厅：不法分子入侵短信平台、向师生家长发送含非法链接短信，已报警

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwf17RxsWCibGJAy5CqxkkY35X5XyICp9cbr4uNHYM4l2WfdzjsvH9ictA/640?wx_fmt=jpeg)[【安全圈】扫地机器人被黑客入侵，追逐宠物并辱骂主人](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=2&sn=38505d2516cdbe4a948e32101cbbebf5&chksm=f36e61e6c419e8f0e3861875cb5395af2defdb95e309b40b053c850d37a6e094e918bc6e63c9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwRAEImmIV5VaTKyv8mnMphplwnXJfBBbkk04zuAD1l3B7WLGON5Jh1Q/640?wx_fmt=jpeg)[【安全圈】互联网档案馆遭遇黑客攻击，3100 万用户数据被泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=3&sn=f278990431cd6c2598c9d914ee2b2e45&chksm=f36e61e6c419e8f010e3701d4e8cc0c32276cee6d24c47cc149b0fd7244f4cbe0799fd9ccc3a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwD5omE3x65h5waBCOc788Wc4OBAUNxbo9aFd5ibU6W9xRcFSenopDfng/640?wx_fmt=jpeg)[【安全圈】安全公司曝光黑客假借求职名义发送木马邮件，HR 打开就中招](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=4&sn=0401fbd7c8c87dba65ea5338166a7d73&chksm=f36e61e6c419e8f02fca8fa6dbad1acf009cdeab95878710b0d2a1a4f3adda6641690f978fe8&scene=21#wechat_redirect)

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