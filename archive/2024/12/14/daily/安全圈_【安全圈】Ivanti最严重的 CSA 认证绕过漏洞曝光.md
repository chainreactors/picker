---
title: 【安全圈】Ivanti最严重的 CSA 认证绕过漏洞曝光
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066594&idx=4&sn=b010357e9e80003c07a80b440507c355&chksm=f36e7f62c419f674bf2fcde34f7aed14f464143ef5283e001b7ce427b24ed44858953afd2a85&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-14
fetch_date: 2025-10-06T19:41:25.288852
---

# 【安全圈】Ivanti最严重的 CSA 认证绕过漏洞曝光

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljGyHYwcz2gbXHesVAr8IpfTicFQtADI8xA1kez4DTpQSPOooIzBQSZ0gRrHrCP1d5qVNtMicHnokTA/0?wx_fmt=jpeg)

# 【安全圈】Ivanti最严重的 CSA 认证绕过漏洞曝光

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

12月11日，Ivanti 向客户发出警告，提醒其 Cloud Services Appliance (CSA)解决方案存在一个新的最高严重性的认证绕过漏洞。![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljGyHYwcz2gbXHesVAr8IpfRkDLyEfg6ibzWEmhvBasAu9PZLnhDvopKDuoyicv4k83Ug6QwBEAEKrw/640?wx_fmt=jpeg&from=appmsg)

这个安全漏洞（编号 CVE-2024-11639）能够使远程攻击者在运行 Ivanti CSA 5.0.2 或更早版本的易受攻击设备上获得管理员权限，而无需进行身份验证或用户交互，通过绕过认证，使用替代路径或通道。Ivanti 建议管理员根据提供的详细信息将易受攻击的设备升级到 CSA 5.0.3，详细信息可以在支持文档中找到。

“我们目前尚未了解到在公开披露之前有任何客户受到这些漏洞的利用。这些漏洞是通过我们的负责任披露计划公开披露的。”

Ivanti 今天还修补了 Desktop and Server Management (DSM)，Connect Secure and Policy Secure，Sentry 和Patch SDK 产品中的其他中等、高等和关键性漏洞。然而，正如周二发布的安全通告中所指出的，目前没有证据表明这些漏洞在野外被利用。

CVE-2024-11639 是近几个月中修补的第六个 CSA 安全漏洞，之前的五个漏洞分别是：

九月：CVE-2024-8190（远程代码执行）
九月：CVE-2024-8963（管理员身份验证绕过）
十月：CVE-2024-9379 、CVE-2024-9380 、CVE-2024-9381（SQL 注入、操作系统命令注入、路径遍历）
在九月份，该公司还警告客户，CVE-2024-8190 和CVE-2024-8963 漏洞已经成为攻击目标。

此外，它还提醒管理员，十月份修复的三个安全漏洞与 CVE-2024-8963 CSA 管理员绕过漏洞相结合，通过 SQL 注入运行 SQL 语句，绕过安全限制，并通过命令注入执行任意代码。

这些被积极利用的漏洞连续出现，与此同时，Ivanti 表示，它正在加强测试和内部扫描能力，并改进其负责任披露流程，以更快地修复安全漏洞。

今年早些时候，还有其他几个漏洞在广泛的攻击中作为零日漏洞被利用，攻击目标包括 Ivanti VPN 设备以及 ICS 、IPS 和ZTA 网关。

参考来源：https://www.bleepingcomputer.com/news/security/ivanti-warns-of-maximum-severity-csa-auth-bypass-vulnerability/

***END***

阅读推荐

[【安全圈】大量用户吐槽，Microsoft 365 又大面积宕机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=1&sn=1294f1f07ab020666e22003bce0314b4&scene=21#wechat_redirect)

[【安全圈】OpenAI、Facebook、Instagram、WhatsApp 集体全球宕机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=2&sn=464a287f7dc747494c68e686a161ab77&scene=21#wechat_redirect)

[【安全圈】知名企业级文件传输产品存在漏洞，正在被黑客利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=3&sn=55d3538cbf8999a9aa8be86d3ea965e6&scene=21#wechat_redirect)

[【安全圈】Windows 远程桌面服务漏洞允许攻击者执行远程代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=4&sn=fb9fe492092fe4a3088d8bcf368835be&scene=21#wechat_redirect)

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