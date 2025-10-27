---
title: 【安全圈】建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064524&idx=3&sn=ac02f46258dacbf415152fe2bad17d2e&chksm=f36e674cc419ee5aebd784b2bec5e460e41f1df53702204b3d3abd741b7d28e67b64223ab4db&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-20
fetch_date: 2025-10-06T18:28:27.909356
---

# 【安全圈】建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgFjLgEspOZUQtsh00n9cLHLWKGnKH7jaicDknW5RlpJ1xwTognxj3v5tV3hEP8SsAv2Q2fhhGbjaw/0?wx_fmt=jpeg)

# 【安全圈】建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgFjLgEspOZUQtsh00n9cLHCmyEKbw5ek76hVbm5P0icl3AicwvsMGCA2ibqwwiaoyttWCsgPb8LPv68w/640?wx_fmt=jpeg&from=appmsg)

威胁行为者一直以建筑行业总承包商常用的 Foundation 会计软件为目标，利用管道、HVAC 和混凝土子行业等中的积极漏洞。

Huntress 的研究人员最初在 9 月 14 日跟踪活动时发现了这种威胁。“让我们感到震惊的是，主机/域枚举命令是从 sqlservr.exe 的父进程中生成的，”研究人员在他们的咨询中写道。

应用程序使用的软件包括一个 Microsoft SQL Server （MSSQL） 实例，用于处理其数据库操作。据研究人员称，虽然将数据库服务器保存在内部网络或防火墙后面很常见，但 Foundation 软件包含允许通过移动应用程序访问的功能。因此，“TCP 端口 4243 可能会公开供移动应用程序使用。这个 4243 端口提供对 MSSQL 的直接访问。

同时，Microsoft SQL Server 有一个默认的系统管理员帐户，称为“sa”，该帐户对整个服务器具有完全管理权限。凭借如此高的权限，这些账户可以让用户运行 shell 命令和脚本。

据观察，针对该应用程序的威胁行为者大规模暴力破解应用程序，并使用默认凭据来访问受害者帐户。此外，威胁行为者似乎正在使用脚本来自动化他们的攻击。

建议组织轮换与 Foundation 软件关联的凭据，并保持安装与 Internet 断开连接，以防止成为这些攻击的受害者。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHJSAQgRNWYZtFiaw1LXj9icwrViaYZKaTF8ERIWtLpaHAv8KIfuC1DTo9g/640?wx_fmt=jpeg)[【安全圈】对BP机发起网络攻击，竟可以制造全国性大爆炸？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064505&idx=1&sn=0ffe66627ed00d0d827324314965442b&chksm=f36e66b9c419efafdb27398c8ad24d37d3fa2cd14681f534127f237056cb1184eb3e941d651a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHtjbFLiahibic0tYD0K2XEo41KeRFgxtWDliaWApAJGjOG9o7p1mPlxiaXmQ/640?wx_fmt=jpeg)[【安全圈】VMware vCenter Server 漏洞让攻击者能够执行远程代码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064505&idx=2&sn=4f43301ff2f7aea69701f9caee393e63&chksm=f36e66b9c419efaf8abe64f74ac1deebb763a2ad3298be33ecad40d79f7d7eb8c50ee69e6649&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHOnu9T3jCbzYTuljyhw0UXXgTia9pV5mZIzxTEpDN15ulOlU3G0Q7Nvg/640?wx_fmt=png)[【安全圈】适用于Mac的第三方防火墙Little Snitch存在缺陷 会让macOS系统绕过DNS加密](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064505&idx=3&sn=693ca73fffc7de30a69c915a55ed9850&chksm=f36e66b9c419efaf202b5972af4bb80775f5c6c71c35b1be6b1b17755bf142704353f11b99ae&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHE1NGyiaVcpeHPicRu5Mgam6wUURWES1PNVYa9XxfX5hJPTwfe78KlUGw/640?wx_fmt=png)[【安全圈】微软推出更新修复Outlook等多个应用在输入文本或拼写检查时崩溃的问题](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064505&idx=4&sn=ebcdb9f9c76d2a93f37b2a1813282766&chksm=f36e66b9c419efaf413a17321d883fa8ee8d70b22a722d0d8b9e263824b6b691f0f7b8a98659&scene=21#wechat_redirect)

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