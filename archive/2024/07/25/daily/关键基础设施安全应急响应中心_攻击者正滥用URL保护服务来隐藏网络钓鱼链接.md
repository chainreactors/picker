---
title: 攻击者正滥用URL保护服务来隐藏网络钓鱼链接
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545063&idx=4&sn=6509a19d024c3912e727595d234aa40f&chksm=c1e9bcb6f69e35a045bf9107dcc6a0d189231c5a208794485b64ebcfc805be18f497700c6afc&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-25
fetch_date: 2025-10-06T17:43:53.529104
---

# 攻击者正滥用URL保护服务来隐藏网络钓鱼链接

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs3gFteicP6rfs4zmic9RZeiaURB1BZSSvUEkL5ze8FthW7DIrnjrkdpcRNaXdHauqibztiayvibRKUCePQ/0?wx_fmt=jpeg)

# 攻击者正滥用URL保护服务来隐藏网络钓鱼链接

关键基础设施安全应急响应中心

据网络安全公司Barracuda近期的一项研究报告，一些攻击者正滥用电子邮件安全服务隐藏恶意链接并传播钓鱼邮件，到目前为止这些攻击已针对至少数百家公司。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs3gFteicP6rfs4zmic9RZeiaUGboZ1gtibohjCJhkVjpHMDkGxjJ0FhlyRh3n44QuLw5ZaIv3663nZkQ/640?wx_fmt=jpeg&from=appmsg)

这些攻击主要利用了电子邮件安全网关中的URL保护功能，该功能能够检查链接是否指向已知的网络钓鱼或恶意软件网站，并根据结果阻止对该链接的访问或将请求重定向到最终目的地，以此来保护用户免受钓鱼或恶意软件威胁。

从2024 年 5 月中旬开始，Barracuda观察到网络钓鱼攻击利用三种不同的 URL 保护服务来掩盖他们的网络钓鱼链接，且提供这些保护服务的都是信誉良好的合法品牌。

目前还不清楚这些攻击者是如何生成指向其虚假网站的重写 URL， 不过，研究人员推测，他们很可能入侵了企业内部使用这些服务的电子邮件账户，向这些被入侵的账户发送电子邮件（或从这些账户发出电子邮件），以强制重写URL。随后，只需从生成的电子邮件信息中获取重写的URL，并重复使用来制作新的网络钓鱼电子邮件即可。

在目标域被标记为恶意域之前，这些 URL 将在多个用户的点击中无限期地发挥作用。一些使用这种技术的钓鱼电子邮件可以伪装成微软的密码修改提醒或 DocuSign 的文档签名请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogs3gFteicP6rfs4zmic9RZeiaU2tDGw9RnVHUpTFx1ZpfsyQlg0swK8cJNtyQTU9dyun521QkmVcHeog/640?wx_fmt=png&from=appmsg)

伪装成微软账户密码修改的钓鱼邮件

URL保护功能在实施过程中存在一些争议，最大的一项缺陷是该功能的黑名单制度，难以有效快速更新最新生成的网络钓鱼网站。因为攻击者已经擅长使用便宜的域名生成大量钓鱼URL，当某一个链接被标记为网络钓鱼网站时，可能已经产生了数百名受害者。

另一个缺陷在于该功能会破坏加密电子邮件签名，因为安全电子邮件网关会通过更改链接来修改原始电子邮件。例如，微软为 Office 365 用户提供了名为 「安全链接」的功能，在 Outlook 和 Teams 等应用程序中，收到的电子邮件和信息中的链接会被重写为 na01.safelinks.protection.outlook.com/?url=[original\_URL]，这一方式过去曾受到安全公司的批评，因为它实际上没有执行动态扫描，且很容易被基于 IP 的流量重定向绕过，或者被使用来自合法和可信域的开放重定向 URL 绕过。

目前，传统的电子邮件安全工具可能很难检测到这些攻击，最有效的防御是通过多层级安全的方法，全面检测和阻止异常或意外活动。

**参考资料：**

https://www.csoonline.com/article/2519035/attackers-abuse-url-protection-services-to-hide-phishing-links-in-emails.html

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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